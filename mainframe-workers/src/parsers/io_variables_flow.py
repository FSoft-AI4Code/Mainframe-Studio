from collections import defaultdict
from copy import deepcopy
from typing import Callable, Any

from parsers.variable_flow_utils import VariableFlowUtils, VarExtraProps
from parsers.grammar.common.base_cobol_schemas import (
    CobolVariable,
    ImportedCopybook,
    FileControlEntry,
    FileDescriptionEntry,
    Statement,
)


class IOVariableFlowBuilder:
    def __init__(
        self,
        repository_id: str,
        file_control_list: list[FileControlEntry],
        file_description_list: list[FileDescriptionEntry],
        working_storage_vars: list[dict],
        working_storage_copybooks: list[dict],
        statements: list[Statement],
        map_picture_clause_fn: Callable[[str], str],
    ):
        self._repository_id = repository_id
        self._file_control_list = file_control_list
        self._file_description_list = file_description_list
        self._working_storage_vars = deepcopy(working_storage_vars)
        self._working_storage_copybooks = working_storage_copybooks
        self._statements = statements
        self._map_picture_clause_fn = map_picture_clause_fn

        self._variables_flow = []
        self._flow_key_set = set()  # to check duplicates

    def build(self) -> list[dict]:
        # Collect OUTPUT/IO file names
        file_names_to_process = []
        for file_control in self._file_control_list:
            if file_control.open_type in ["OUTPUT", "I-O"]:
                file_names_to_process.append(file_control.file_name)

        # Skip processing if there are no OUTPUT/IO files
        if len(file_names_to_process) == 0:
            return []

        # Build dictionary to look up Move/Write/Rewrite statements along with condition
        (
            self._write_dest_to_write_statements_with_condition_dict,
            self._rewrite_dest_to_rewrite_statements_with_condition_dict,
            self._move_dest_to_move_statements_with_condition_dict,
        ) = self.__build_dest_to_statements_with_condition_dicts(self._statements)

        # Build dictionaries to lookup variables and copybooks of a file
        (self._file_vars_dict, self._file_copybooks_dict) = (
            self.__build_file_vars_and_copybooks_dicts(self._file_description_list)
        )

        # Build dictionary to lookup working storage variable tree
        self._working_storage_var_name_to_var_tree_dict = (
            VariableFlowUtils.build_expanded_variable_tree_dict(
                self._repository_id,
                self._working_storage_vars,
                self._working_storage_copybooks,
            )
        )

        # Process the variables to add flow entries
        for file_name in file_names_to_process:
            vars = self.__get_file_variables_as_dicts(file_name)
            copybooks = self.__get_file_copybooks_as_dicts(file_name)
            variable_hierarchy = VariableFlowUtils.build_expanded_variable_hierarchy(
                self._repository_id, vars, copybooks
            )
            self.__process_variable_hierarchy(variable_hierarchy)
            self.__collect_flows_from_variables(
                variable_hierarchy, self._variables_flow
            )

        return self._variables_flow

    def __collect_flows_from_variables(
        self, variable_hierarchy: list[dict], variables_flow: list[dict]
    ) -> list[dict]:
        """Recursively collect flow entries from variables"""
        for var_tree in variable_hierarchy:
            variables_flow.extend(var_tree.get(VarExtraProps.FLOWS, []))
            self.__collect_flows_from_variables(
                VariableFlowUtils.get_var_children(var_tree), variables_flow
            )

    def __dump_variable_fn(self, var: CobolVariable) -> dict:
        """Convert the variable object to dictionary and add extra fields"""
        return {
            **var.model_dump(),
            "byte_length": self.__calculate_byte_length(var),
            "data_type": (
                self._map_picture_clause_fn(var.picture_clause)
                if var.picture_clause
                else ""
            ),
        }

    def __calculate_byte_length(self, var: CobolVariable) -> int:
        """Calculate byte length for a variable"""
        return (var.length if var.length else 0) * (var.occur if var.occur else 1)

    def __build_dest_to_statements_with_condition_dicts(
        self, statements: list[Statement]
    ) -> tuple[
        dict[str, list[tuple[Statement, Any]]],
        dict[str, list[tuple[Statement, Any]]],
        dict[str, list[tuple[Statement, Any]]],
    ]:
        """
        Build dictionaries to lookup Move/Write/Rewrite statements by destination variable name quickly.
        along with the condition from the parent Evaluate/If statements.
        """
        write_dest_to_write_statements_with_condition_dict = defaultdict(list)
        rewrite_dest_to_rewrite_statements_with_condition_dict = defaultdict(list)
        move_dest_to_move_statements_with_condition_dict = defaultdict(list)

        statements_generator = VariableFlowUtils.get_statements_generator(
            ["MoveStatement", "WriteStatement", "RewriteStatement"]
        )
        for statement, condition in statements_generator(statements):
            if statement.tag == "WriteStatement":
                write_dest_main_name = VariableFlowUtils.extract_main_var_name(
                    statement.record_name
                )
                write_dest_to_write_statements_with_condition_dict[
                    write_dest_main_name
                ].append((statement, condition))

            elif statement.tag == "RewriteStatement":
                rewrite_dest_main_name = VariableFlowUtils.extract_main_var_name(
                    statement.record_name
                )
                rewrite_dest_to_rewrite_statements_with_condition_dict[
                    rewrite_dest_main_name
                ].append((statement, condition))

            elif statement.tag == "MoveStatement":
                for destination in statement.to_identifiers:
                    move_dest_main_name = VariableFlowUtils.extract_main_var_name(
                        destination
                    )
                    move_dest_to_move_statements_with_condition_dict[
                        move_dest_main_name
                    ].append((statement, condition))

        return (
            write_dest_to_write_statements_with_condition_dict,
            rewrite_dest_to_rewrite_statements_with_condition_dict,
            move_dest_to_move_statements_with_condition_dict,
        )

    def __build_file_vars_and_copybooks_dicts(
        self,
        file_description_list: list[FileDescriptionEntry],
    ) -> tuple[dict[str, list[CobolVariable]], dict[str, list[ImportedCopybook]]]:
        """Build dictionaries to lookup variables and copybooks of a file by filename"""
        file_vars_dict = {}
        file_copybooks_dict = {}

        for file_description in file_description_list:
            file_vars_dict[file_description.file_name] = file_description.variables
            file_copybooks_dict[file_description.file_name] = file_description.copybooks

        return file_vars_dict, file_copybooks_dict

    def __get_file_variables_as_dicts(self, file_name: str) -> list[dict]:
        """Get list of variables in a file as dictionaries"""
        vars = self._file_vars_dict.get(file_name, [])
        vars = [self.__dump_variable_fn(var) for var in vars]
        return vars

    def __get_file_copybooks_as_dicts(self, file_name: str) -> list[dict]:
        """Get list of variables in a file as dictionaries"""
        copybooks = self._file_copybooks_dict.get(file_name, [])
        copybooks = [copybook.model_dump() for copybook in copybooks]
        return copybooks

    def __should_process_variable(self, var_name: str) -> bool:
        """Check if a variable is the destination of a write statement or a move statement"""
        return (
            (var_name in self._move_dest_to_move_statements_with_condition_dict)
            or (var_name in self._write_dest_to_write_statements_with_condition_dict)
            or (
                var_name in self._rewrite_dest_to_rewrite_statements_with_condition_dict
            )
        )

    def __process_variable_hierarchy(self, variable_hierarchy: list[dict]) -> None:
        """Recursively process each variable in the hierarchy"""
        for var_tree in variable_hierarchy:
            if self.__should_process_variable(var_tree.get("name")):
                self.__process_variable(var_tree)

            # Process the children of current variable
            self.__process_variable_hierarchy(
                VariableFlowUtils.get_var_children(var_tree)
            )

    def __process_variable(self, var_tree: dict) -> None:
        """Handle current variable and intermediate variables from write statement"""
        original_var_name = var_tree.get("name")
        var_name_and_src_var_name_with_condition = []
        intermediate_var_names_to_track_children = []

        # Collect (var_name, src_var_name, condition) from Move statements with current variable as destination
        move_statements_with_condition = (
            self._move_dest_to_move_statements_with_condition_dict.get(
                original_var_name, []
            )
        )
        for statement, condition in move_statements_with_condition:
            for destination in statement.to_identifiers:
                # Check if this destination is a substring reference of current variable
                if original_var_name in destination:
                    var_name_and_src_var_name_with_condition.append(
                        (destination, statement.move_from, condition)
                    )

        # Collect from write and rewrite statements
        write_collected_results = self.__collect_from_write_or_rewrite_statement(
            self._write_dest_to_write_statements_with_condition_dict.get(
                original_var_name, []
            ),
            lambda stmt: (
                stmt.write_from_phrase.identifier if stmt.write_from_phrase else None
            ),
        )
        rewrite_collected_results = self.__collect_from_write_or_rewrite_statement(
            self._rewrite_dest_to_rewrite_statements_with_condition_dict.get(
                original_var_name, []
            ),
            lambda stmt: stmt.rewrite_from_identifier,
        )

        # Combine the results
        var_name_and_src_var_name_with_condition.extend(write_collected_results[0])
        var_name_and_src_var_name_with_condition.extend(rewrite_collected_results[0])
        intermediate_var_names_to_track_children.extend(write_collected_results[1])
        intermediate_var_names_to_track_children.extend(rewrite_collected_results[1])

        # Add flow entries for current variable
        self.__add_variable_flow(
            var_tree,
            var_name_and_src_var_name_with_condition,
            intermediate_var_names_to_track_children,
        )

    def __collect_from_write_or_rewrite_statement(
        self,
        statements_with_condition: list[tuple[Statement, Any]],
        extract_source_var_name_fn: Callable[[Statement], str | None],
    ) -> tuple[list[tuple[str, str, Any]], list[str]]:
        """
        Helper for process_variable: collect (var_name, src_var_name, condition) tuples and intermediate_var_names_to_track_children
        from write_statements_with_condition or rewrite_statements_with_condition.
        """
        var_name_and_src_var_name_with_condition = []
        intermediate_var_names_to_track_children = []

        for statement, condition in statements_with_condition:
            var_name = statement.record_name
            intermediate_var_name = extract_source_var_name_fn(statement)
            if not intermediate_var_name:
                continue

            intermediate_var_main_name = VariableFlowUtils.extract_main_var_name(
                intermediate_var_name
            )
            if (
                intermediate_var_main_name
                in self._move_dest_to_move_statements_with_condition_dict
            ):
                # Collect (var_name, src_var_name, condition) move statements with this intermediate variable as destination
                # (the variable flow entry will be for current variable, not intermediate variable)
                for (
                    move_statement,
                    move_condition,
                ) in self._move_dest_to_move_statements_with_condition_dict[
                    intermediate_var_main_name
                ]:
                    var_name_and_src_var_name_with_condition.append(
                        (var_name, move_statement.move_from, move_condition)
                    )

                # Collect intermediate variables that are not added as source variables to track their children
                intermediate_var_names_to_track_children.append(intermediate_var_name)
            else:
                # Use this intermediate variable as source variable
                var_name_and_src_var_name_with_condition.append(
                    (var_name, intermediate_var_name, condition)
                )

        return (
            var_name_and_src_var_name_with_condition,
            intermediate_var_names_to_track_children,
        )

    def __add_variable_flow(
        self,
        var_tree: dict,
        var_name_and_src_var_name_with_condition: list[tuple[str, str, Any]],
        intermediate_var_names_to_track_children: list[str],
    ) -> None:
        """
        Add flow entries for a variable and children that indirectly affected.
        Attach the flow entries directly to variable for flattening later (to keep order).
        """
        for (
            var_name,
            src_var_name,
            condition,
        ) in var_name_and_src_var_name_with_condition:
            src_var_main_name = VariableFlowUtils.extract_main_var_name(src_var_name)
            src_var_tree = self.__find_expanded_variable_tree(src_var_main_name)

            entry = {
                "name": var_name,
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
                "condition_clause": condition.get("clause") if condition else None,
                "condition_type": condition.get("type") if condition else None,
            }

            VariableFlowUtils.add_single_flow_entry(
                entry,
                existing_entries=var_tree.setdefault(VarExtraProps.FLOWS, []),
                existing_key_set=self._flow_key_set,
            )

            if src_var_tree:
                # Process and add indirect flow entries for children
                VariableFlowUtils.process_children_of_pair(
                    VariableFlowUtils.get_var_children(var_tree),
                    VariableFlowUtils.get_var_children(src_var_tree),
                    self.__add_children_variable_flow,
                )

        # Process and add indirect flow entries for children
        for intermediate_var_name in intermediate_var_names_to_track_children:
            intermediate_var_main_name = VariableFlowUtils.extract_main_var_name(
                intermediate_var_name
            )
            intermediate_var_tree = self.__find_expanded_variable_tree(
                intermediate_var_main_name
            )
            if intermediate_var_tree:
                # Process and add indirect flow entries for children
                VariableFlowUtils.process_children_of_pair(
                    VariableFlowUtils.get_var_children(var_tree),
                    VariableFlowUtils.get_var_children(intermediate_var_tree),
                    self.__add_children_variable_flow,
                )

    def __add_children_variable_flow(self, var_tree: dict, src_var_tree: dict) -> None:
        """
        Process a pair of children variables from a pair of ancestor variables that have flow entry.
        Attach the flow entries directly to variable for flattening later (to keep order).
        """
        # Check if the source variable is the destination of some move statements
        src_var_main_name = src_var_tree.get("name")
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
            src_of_src_var = self.__find_variable(src_of_src_var_main_name)

            for destination in statement.to_identifiers:
                # Handle both full variable name and substring reference
                if src_var_main_name not in destination:
                    continue

                # Use src_var suffix as var suffix
                src_var_name_suffix = VariableFlowUtils.extract_var_name_suffix(
                    destination
                )
                var_name_with_suffix = var_tree.get("name") + src_var_name_suffix

                entry = {
                    "name": var_name_with_suffix,
                    "parent_name": var_tree.get("parent_name"),
                    "data_type": var_tree.get("data_type"),
                    "length": var_tree.get("length"),
                    "src_variable": statement.move_from,
                    "src_parent_name": (
                        src_of_src_var.get("parent_name") if src_of_src_var else None
                    ),
                    "src_data_type": (
                        src_of_src_var.get("data_type") if src_of_src_var else None
                    ),
                    "src_length": (
                        src_of_src_var.get("length") if src_of_src_var else None
                    ),
                    "condition_clause": (
                        condition.get("clause") if condition else None
                    ),
                    "condition_type": (condition.get("type") if condition else None),
                }

                VariableFlowUtils.add_single_flow_entry(
                    entry,
                    existing_entries=var_tree.setdefault(VarExtraProps.FLOWS, []),
                    existing_key_set=self._flow_key_set,
                )

    def __find_expanded_variable_tree(self, var_name: str) -> dict | None:
        """Find an expanded variable tree with variable name"""
        # Find in working storage variables
        if var_name in self._working_storage_var_name_to_var_tree_dict:
            return self._working_storage_var_name_to_var_tree_dict[var_name]

        # Find in variable list of each file (both direct and through copybooks)
        for file_control in self._file_control_list:
            vars = self.__get_file_variables_as_dicts(file_control.file_name)
            copybooks = self.__get_file_copybooks_as_dicts(file_control.file_name)
            var_tree = self.__find_variable_with_incremental_copybook_expansion(
                self._repository_id, var_name, vars, copybooks
            )
            if var_tree:
                return var_tree

        return None

    def __find_variable_with_incremental_copybook_expansion(
        self,
        repository_id: str,
        target_var_name: str,
        variables: list[dict],
        copybooks: list[dict],
    ) -> dict | None:
        """
        Search for a variable incrementally in the direct variable list and expand copybooks as needed.
        Once found, collect that variable and children below it.
        Build the variable subtree, populate byte length, and return the subtree.
        """
        var_cursor = 0
        copybook_cursor = 0

        target_found = False
        target_level = None
        collecting = False
        vars_in_subtree = []

        while var_cursor < len(variables) or copybook_cursor < len(copybooks):
            # Decide whether to check copybook or direct variable next
            should_check_copybook = False
            if copybook_cursor < len(copybooks) and var_cursor < len(variables):
                var_line = int(variables[var_cursor].get("line_number"))
                copybook_line = int(copybooks[copybook_cursor].get("line_number"))
                should_check_copybook = copybook_line < var_line
            elif copybook_cursor < len(copybooks):
                should_check_copybook = True

            # Check copybook
            if should_check_copybook:
                copybook = copybooks[copybook_cursor]
                copybook_vars = VariableFlowUtils.get_copybook_variable_declarations(
                    repository_id, copybook
                )
                for cb_var in copybook_vars:
                    target_found, target_level, collecting, should_break = (
                        self.__update_variable_tree_search_state(
                            cb_var,
                            target_var_name,
                            target_found,
                            collecting,
                            target_level,
                            vars_in_subtree,
                        )
                    )
                    if should_break:
                        break
                copybook_cursor += 1

            # Check direct variable
            else:
                var = variables[var_cursor]
                target_found, target_level, collecting, should_break = (
                    self.__update_variable_tree_search_state(
                        var,
                        target_var_name,
                        target_found,
                        collecting,
                        target_level,
                        vars_in_subtree,
                    )
                )
                if should_break:
                    break
                var_cursor += 1

            # Variable found and all variables in the subtree have been collected
            if target_found and not collecting:
                break

        # Variable not found
        if not target_found:
            return None

        # Build the variable hierarchy (with a single root)
        variable_hierarchy = VariableFlowUtils.__build_variable_hierarchy(
            vars_in_subtree
        )

        # Populate byte_length
        VariableFlowUtils.__backfill_byte_length(variable_hierarchy)

        # Return the target variable tree (the single root in the hierarchy)
        return variable_hierarchy[0]

    def __update_variable_tree_search_state(
        self,
        var: dict,
        target_var_name: str,
        target_found: bool,
        target_level: int | None,
        collecting: bool,
        vars_in_subtree: list[dict],
    ) -> tuple[bool, int | None, bool, bool]:
        """
        Update search state: target_found, target_level, collecting.
        Collect the variable if it is in the target subtree.
        Return the updated state and a flag to determine whether to keep checking.
        """
        should_break = False
        _target_found = target_found
        _target_level = target_level
        _collecting = collecting

        if not target_found:
            # If current variable is the target, start collecting
            if var.get("name") == target_var_name:
                target_found = True
                target_level = int(var.get("level"))
                collecting = True
                vars_in_subtree.append(var)
        elif collecting:
            if int(var.get("level")) > target_level:
                # Collect current variable if it is a child of the target
                vars_in_subtree.append(var)
            else:
                # Stop collecting when encounter a non-child
                collecting = False
                should_break = True

        return _target_found, _target_level, _collecting, should_break

    def __find_variable(self, var_name: str) -> dict | None:
        """Find a variable with variable name (don't return the entire subtree)"""
        # Find in working storage variables
        if var_name in self._working_storage_var_name_to_var_tree_dict:
            var_tree = self._working_storage_var_name_to_var_tree_dict[var_name]
            return {k: v for k, v in var_tree.items() if k != "children"}

        for file_control in self._file_control_list:
            # Find in variable list of each file
            var_objs = self._file_vars_dict.get(file_control.file_name, [])
            var = self.__find_variable_in_file(var_name, var_objs)
            if var:
                return var

            # Find in variable list of copybooks in used in the file
            copybook_objs = self._file_copybooks_dict.get(file_control.file_name, [])
            var = self.__find_variable_in_copybooks(var_name, copybook_objs)
            if var:
                return var

        return None

    def __find_variable_in_file(
        self, var_name: str, var_objs: list[CobolVariable]
    ) -> dict | None:
        """Find a variable in the variables of a file (don't return the entire subtree)"""
        for var_obj in var_objs:
            if var_obj.name == var_name:
                return self.__dump_variable_fn(var_obj)
        return None

    def __find_variable_in_copybooks(
        self, var_name: str, copybook_objs: list[ImportedCopybook]
    ) -> dict | None:
        """Find a variable in the variables of copybooks (don't return the entire subtree)"""
        for copybook_obj in copybook_objs:
            declarations = VariableFlowUtils.get_copybook_variable_declarations(
                copybook_obj.model_dump()
            )
            for declaration in declarations:
                if declaration.get("name") == var_name:
                    return declaration
        return None
