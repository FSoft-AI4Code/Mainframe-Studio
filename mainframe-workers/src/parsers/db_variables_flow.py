from collections import defaultdict
from copy import deepcopy
from loguru import logger
import re
import sqlparse
from sqlparse import tokens, sql
from typing import Any, Callable

from parsers.grammar.common.base_cobol_schemas import Statement
from parsers.grammar.ibm_cobol.ibm_cobol_schemas import ExecSqlStatement2
from parsers.variable_flow_utils import VariableFlowUtils


class DBVariableFlowBuilder:
    def __init__(
        self,
        repository_id: str,
        working_storage_variables: list[dict],
        working_storage_copybooks: list[dict],
        statements: list[Statement],
    ):
        self._repository_id = repository_id
        self._working_storage_variables = deepcopy(working_storage_variables)
        self._working_storage_copybooks = working_storage_copybooks
        self._statements = statements

        self._variables_flow = []
        self._flow_key_set = set()  # to check duplicates

    def build(self) -> list[dict]:
        """Build variables flow and return it"""
        # Collect Move/ExecSQL statements
        (
            self._move_dest_to_move_statements_with_condition_dict,
            exec_sql_statements,
        ) = self.__collect_move_and_exec_sql_statements(self._statements)

        # Skip processing if there are no ExecSQL statements
        if len(exec_sql_statements) == 0:
            return []

        # Extract variable names, variable-to-column name mapping, and SQL INCLUDE statements from ExecSQL statements
        db_var_names = []
        self._db_var_name_to_column_names_dict = defaultdict(list)
        sql_include_statements_with_line_number = []

        for statement in exec_sql_statements:
            var_names, var_name_to_column_names_dict, sql_include_statements = (
                self.__extract_db_variables_and_sql_include_statements(statement)
            )

            db_var_names.extend(var_names)
            for var_name, column_names in var_name_to_column_names_dict.items():
                self._db_var_name_to_column_names_dict[var_name].extend(column_names)

            sql_include_statements_with_line_number.append(
                (sql_include_statements, statement.start_line)
            )

        # Skip processing if cannot extract variable names from ExecSQL statements
        if len(db_var_names) == 0:
            return []

        # Extract working storage copybooks from ExecSQL INCLUDE statements
        extra_copybooks = []
        for (
            sql_include_statements,
            line_number,
        ) in sql_include_statements_with_line_number:
            for statement in sql_include_statements:
                extra_copybooks.extend(
                    self.__extract_copybooks_from_sql_include_statement(
                        statement, line_number
                    )
                )

        # Merge extra copybooks to existing working storage copybooks
        extended_working_storage_copybooks = self.__extend_working_storage_copybooks(
            extra_copybooks
        )

        # Build dictionary to lookup working storage variable tree by name
        self._var_name_to_var_tree_dict = (
            VariableFlowUtils.build_expanded_variable_tree_dict(
                self._repository_id,
                self._working_storage_variables,
                extended_working_storage_copybooks,
            )
        )

        # Process the variables to add flow entries
        for var_name in db_var_names:
            self.__process_variable(var_name)

        return self._variables_flow

    def __extract_db_variables_and_sql_include_statements(
        self, exec_sql_statement: ExecSqlStatement2
    ) -> tuple[list[str], dict[str, list[str]], list]:
        """Extract variable names, variable-to-column mapping, and SQL INCLUDE statements from Exec SQL statement"""
        sql_code = exec_sql_statement.sql_code
        modified_sql_code, replaced_set = self.__wrap_sql_variables(sql_code)

        parsed_sql = None
        try:
            parsed_sql = sqlparse.parse(modified_sql_code)
        except Exception as e:
            logger.error(f"Error parsing SQL: {e}")
        if not parsed_sql:
            return []

        db_var_names = []
        db_var_name_to_column_names_dict = defaultdict(list)
        sql_include_statements = []

        for sql_statement in parsed_sql:
            first_token = sql_statement.token_first(skip_cm=True, skip_ws=True)
            if not first_token:
                continue

            first_token_value = first_token.value
            first_token_type = first_token.ttype

            # Collect SQL INCLUDE statements
            if first_token_type == tokens.Keyword and first_token_value == "INCLUDE":
                sql_include_statements.append(sql_statement)

            # Skip if not a DML command
            if first_token_type != tokens.DML:
                continue

            # Extract variable names from SQL INSERT/UPDATE statement
            sql_statement_type = sql_statement.get_type()
            if sql_statement_type == "INSERT":
                var_names, var_name_to_column_names_dict = (
                    self.__extract_variables_from_sql_insert_statement(
                        sql_statement, replaced_set
                    )
                )
            elif sql_statement_type == "UPDATE":
                var_names, var_name_to_column_names_dict = (
                    self.__extract_variables_from_sql_update_statement(
                        sql_statement, replaced_set
                    )
                )
            else:
                continue  # skip if not SQL INSERT/UPDATE statement

            db_var_names.extend(var_names)
            for var_name, column_names in var_name_to_column_names_dict.items():
                db_var_name_to_column_names_dict[var_name].extend(column_names)

        return db_var_names, db_var_name_to_column_names_dict, sql_include_statements

    def __extract_copybooks_from_sql_include_statement(
        self, sql_include_statement: sql.Statement, line_number: int
    ):
        """Extract copybook info from SQL INCLUDE statement"""
        copybooks = []

        stack: list[sql.Token | sql.TokenList] = []
        for i in range(len(sql_include_statement.tokens) - 1, -1, -1):
            stack.append(sql_include_statement.tokens[i])

        while stack:
            current_token = stack.pop()

            # Retrieve the copybook
            if isinstance(current_token, sql.Identifier):
                copybooks.append(
                    {
                        "copybook_name": current_token.value,
                        "line_number": line_number,
                        "replacing": [],
                    }
                )

            if isinstance(current_token, sql.TokenList):
                for i in range(len(current_token.tokens) - 1, -1, -1):
                    stack.append(current_token.tokens[i])
                continue

        return copybooks

    def __extend_working_storage_copybooks(self, extra_copybooks: list[dict]):
        """
        Merge extra copybooks to existing working storage copybooks.
        Handle consecutive items with the same line number in extra_copybooks.
        """
        ws_copybooks = self._working_storage_copybooks
        extended_copybooks = []
        i, j = 0, 0

        # Append items in correct order
        while i < len(ws_copybooks) and j < len(extra_copybooks):
            ws_copybook = ws_copybooks[i]
            extra_copybook = extra_copybooks[j]
            if int(ws_copybook["line_number"]) <= int(extra_copybook["line_number"]):
                extended_copybooks.append(ws_copybook)
                i += 1
            else:
                extended_copybooks.append(extra_copybook)
                j += 1

        # Append remaining items
        if i < len(ws_copybooks):
            extended_copybooks.extend(ws_copybooks[i:])
        if j < len(extra_copybooks):
            extended_copybooks.extend(extra_copybooks[j:])

        return extended_copybooks

    def __extract_variables_from_sql_insert_statement(
        self,
        sql_insert_statement: sql.Statement,
        replaced_set: set[str],
    ) -> tuple[list[str], dict[str, list[str]]]:
        """Extract variable names and variable-to-column name mapping from SQL INSERT statement"""
        table_name = None
        columns_recorded = False
        columns: list[str] = []
        values: list[str] = []

        stack: list[sql.Token | sql.TokenList] = []
        for i in range(len(sql_insert_statement.tokens) - 1, -1, -1):
            stack.append(sql_insert_statement.tokens[i])

        while stack:
            current_token = stack.pop()

            # Record table name
            if not table_name and isinstance(current_token, sql.Identifier):
                table_name = current_token.value
                continue

            # Retrieve the list of columns
            if not columns_recorded and isinstance(current_token, sql.IdentifierList):
                for identifier in current_token.get_identifiers():
                    columns.append(identifier.value)
                columns_recorded = True
                continue

            # Retrieve the list of values
            if isinstance(current_token, sql.Values):
                parenthesis_token = next(
                    token
                    for token in current_token.get_sublists()
                    if isinstance(token, sql.Parenthesis)
                )

                # Remove parentheses and whitespaces on both ends, then split
                values = re.split(r"\s*,\s*", parenthesis_token.value[1:-1].strip())
                break

            if isinstance(current_token, sql.TokenList):
                for i in range(len(current_token.tokens) - 1, -1, -1):
                    stack.append(current_token.tokens[i])
                continue

        # Record variable names and variable-to-column mapping
        var_names = []
        var_name_to_column_names_dict = defaultdict(list)

        for i in range(len(columns)):
            column = columns[i]
            value = values[i]

            # Check for a wrapped variable (:"VAR-NAME")
            if value and value[0] == ":" and value[1:] in replaced_set:
                var_name = value[1:].strip('"')
                var_names.append(var_name)
                var_name_to_column_names_dict[var_name].append(f"{table_name}.{column}")

        return var_names, var_name_to_column_names_dict

    def __extract_variables_from_sql_update_statement(
        self,
        sql_update_statement: sql.Statement,
        replaced_set: set[str],
    ) -> tuple[list[str], dict[str, list[str]]]:
        """Extract variable names and variable-to-column name mapping from SQL UPDATE statement"""
        var_names = []
        var_name_to_column_names_dict = defaultdict(list)

        table_name = None
        current_column = None
        last_token = None

        stack: list[sql.Token | sql.TokenList] = []
        for i in range(len(sql_update_statement.tokens) - 1, -1, -1):
            stack.append(sql_update_statement.tokens[i])

        while stack:
            current_token = stack.pop()

            # Record table name
            if not table_name and isinstance(current_token, sql.Identifier):
                table_name = current_token.value
                last_token = current_token
                continue

            # Stop if encounter a WHERE clause
            if isinstance(current_token, sql.Where):
                break

            # Record current column
            if not current_column and isinstance(current_token, sql.Identifier):
                current_column = current_token.value
                last_token = current_token
                continue

            if isinstance(current_token, sql.TokenList):
                for i in range(len(current_token.tokens) - 1, -1, -1):
                    stack.append(current_token.tokens[i])
                continue

            # Ignore whitespace tokens
            if current_token.ttype in tokens.Whitespace:
                last_token = current_token
                continue

            # Reset current column when encounter ','
            if current_token.ttype == tokens.Punctuation and current_token.value == ",":
                current_column = None
                last_token = current_token
                continue

            # Check for a wrapped variable (:"VAR-NAME")
            if (
                current_column
                and self.__last_was_colon(last_token)
                and current_token.value in replaced_set
            ):
                var_name = current_token.value.strip('"')
                var_names.append(var_name)
                var_name_to_column_names_dict[var_name].append(
                    f"{table_name}.{current_column}"
                )

            last_token = current_token

        return var_names, var_name_to_column_names_dict

    def __last_was_colon(self, token: sql.Token | sql.TokenList):
        """Check if the last token was a ':' (for tracking bind variables)"""
        return token.ttype == tokens.Punctuation and token.value == ":"

    def __wrap_sql_variables(self, sql_code: str) -> tuple[str, set[str]]:
        """
        - Wraps SQL bind variables (starting with ':') in double quotes
          (sqlparse parses '-' in variable names as operator)
        - Example: :A-B-C -> :"A-B-C"
        - Returns the modified SQL string and the set of wrapped variable names
        """
        replaced_set = set()

        def replacer(match):
            original = match.group(0)[1:]  # Remove leading ':'
            wrapped = f'"{original}"'  # Wrap variable name in double quotes
            replaced_set.add(wrapped)  # Store the wrapped variable name
            return f":{wrapped}"  # Add ':' back

        pattern = r":\w+(?:-\w+)*"  # Match bind variables (including ones with '-')
        modified_sql = re.sub(pattern, replacer, sql_code)

        return modified_sql, replaced_set

    def __collect_move_and_exec_sql_statements(
        self, statements: list[Statement]
    ) -> tuple[dict[str, list[tuple[Statement, Any]]], list[Statement]]:
        """
        Build dictionaries to lookup Move statements by destination variable name,
        along with the condition from the parent Evaluate/If statement.
        Collect ExecSQL statements.
        """
        move_dest_to_move_statements_with_condition_dict = defaultdict(list)
        exec_sql_statements = []

        statements_generator = VariableFlowUtils.get_statements_generator(
            ["MoveStatement", "ExecSqlStatement2"]
        )
        for statement, condition in statements_generator(statements):
            if statement.tag == "MoveStatement":
                for destination in statement.to_identifiers:
                    move_dest_main_name = VariableFlowUtils.extract_main_var_name(
                        destination
                    )
                    move_dest_to_move_statements_with_condition_dict[
                        move_dest_main_name
                    ].append((statement, condition))

            elif statement.tag == "ExecSqlStatement2":
                exec_sql_statements.append(statement)

        return (move_dest_to_move_statements_with_condition_dict, exec_sql_statements)

    def __process_variable(self, var_name: str) -> None:
        # Check if the variable exists
        original_var_name = VariableFlowUtils.extract_main_var_name(var_name)
        var_tree = self._var_name_to_var_tree_dict.get(original_var_name)

        # Skip processing if variable not found
        if not var_tree:
            return

        move_statements_with_condition = (
            self._move_dest_to_move_statements_with_condition_dict.get(
                original_var_name, []
            )
        )

        # Skip processing if there are no Move statements to this variable
        if len(move_statements_with_condition) == 0:
            return

        # Collect (var_name, src_var_name, condition) from Move statements with current variable as destination
        var_name_and_src_var_name_with_condition = []
        for statement, condition in move_statements_with_condition:
            for destination in statement.to_identifiers:
                # Handle both full variable name and substring reference
                if original_var_name in destination:
                    var_name_and_src_var_name_with_condition.append(
                        (destination, statement.move_from, condition)
                    )

        # Add flow entries for current variable
        self.__add_variable_flow(
            var_tree,
            var_name_and_src_var_name_with_condition,
        )

    def __add_variable_flow(
        self,
        var_tree: dict,
        var_name_and_src_var_name_with_condition: list[tuple[str, str, Any]],
    ):
        """Add flow entries for a variable and children that indirectly affected"""
        for (
            var_name,
            src_var_name,
            condition,
        ) in var_name_and_src_var_name_with_condition:
            src_var_main_name = VariableFlowUtils.extract_main_var_name(src_var_name)
            src_var_tree = self._var_name_to_var_tree_dict.get(src_var_main_name)
            db_column_names = self._db_var_name_to_column_names_dict[var_name]

            new_entry_added = False
            for db_column_name in db_column_names:
                entry = {
                    "name": db_column_name,
                    "parent_name": var_tree.get("parent_name"),
                    "data_type": var_tree.get("data_type"),
                    "length": var_tree.get("length"),
                    "src_variable": src_var_name,
                    "src_parent_name": (
                        src_var_tree.get("parent_name") if src_var_tree else None
                    ),
                    "src_data_type": (
                        src_var_tree.get("data_type") if src_var_tree else None
                    ),
                    "src_length": src_var_tree.get("length") if src_var_tree else None,
                    "condition_clause": (
                        condition.get("clause") if condition else None
                    ),
                    "condition_type": condition.get("type") if condition else None,
                }

                # Check if any new entry is added
                if VariableFlowUtils.add_single_flow_entry(
                    entry,
                    existing_entries=self._variables_flow,
                    existing_key_set=self._flow_key_set,
                ):
                    new_entry_added = True

            if new_entry_added and src_var_tree:
                VariableFlowUtils.process_children_of_pair(
                    VariableFlowUtils.get_var_children(var_tree),
                    VariableFlowUtils.get_var_children(src_var_tree),
                    self.__make_add_children_flow_fn(var_name),
                )

    def __make_add_children_flow_fn(
        self, root_var_name: str
    ) -> Callable[[dict, dict], None]:
        def __add_flow_fn(var_tree: dict, src_var_tree: dict) -> None:
            """
            Process a pair of children variables from a pair of ancestor variables that have flow entry.
            """

            # Check if the source variable is the destination of some move statements
            src_var_main_name = src_var_tree.get("name")
            db_column_names = self._db_var_name_to_column_names_dict[root_var_name]
            move_statements_with_condition_to_src_var = (
                self._move_dest_to_move_statements_with_condition_dict.get(
                    src_var_main_name, []
                )
            )

            # Add flow entries for var with 'source of src_var' as source variable
            for statement, condition in move_statements_with_condition_to_src_var:
                src_of_src_var_name = statement.move_from
                src_of_src_var_main_name = VariableFlowUtils.extract_main_var_name(
                    src_of_src_var_name
                )
                src_of_src_var_tree = self._var_name_to_var_tree_dict.get(
                    src_of_src_var_main_name
                )

                for destination in statement.to_identifiers:
                    # Handle both full variable name and substring reference
                    if src_var_main_name not in destination:
                        continue

                    for db_column_name in db_column_names:
                        entry = {
                            "name": db_column_name,
                            "parent_name": var_tree.get("parent_name"),
                            "data_type": var_tree.get("data_type"),
                            "length": var_tree.get("length"),
                            "src_variable": statement.move_from,
                            "src_parent_name": (
                                src_of_src_var_tree.get("parent_name")
                                if src_of_src_var_tree
                                else None
                            ),
                            "src_data_type": (
                                src_of_src_var_tree.get("data_type")
                                if src_of_src_var_tree
                                else None
                            ),
                            "src_length": (
                                src_of_src_var_tree.get("length")
                                if src_of_src_var_tree
                                else None
                            ),
                            "condition_clause": (
                                condition.get("clause") if condition else None
                            ),
                            "condition_type": (
                                condition.get("type") if condition else None
                            ),
                        }

                        VariableFlowUtils.add_single_flow_entry(
                            entry,
                            existing_entries=self._variables_flow,
                            existing_key_set=self._flow_key_set,
                        )

        return __add_flow_fn
