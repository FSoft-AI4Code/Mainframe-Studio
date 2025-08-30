import os
from loguru import logger
from pymongo import MongoClient
from bson import ObjectId
from collections import deque
from typing import Callable

from parsers.grammar.common.base_cobol_schemas import Statement
from parsers.constants import DEFAULT_VALUES_TO_SKIP


# TODO (Improvement): Define types
# For now just define some frequently used keys
class VarExtraProps:
    FLOWS = "flow_entries"
    CHILDREN = "children"


class VariableFlowUtils:
    @staticmethod
    def extract_main_var_name(var_name: str) -> str:
        """
        Extracts the main part of a COBOL variable name
        Example:
        - "X(7:8)" -> "X"
        - "X" -> "X"
        """
        main_var_name = ""
        for c in var_name:
            if c == "(":
                break
            main_var_name += c
        return main_var_name

    @staticmethod
    def extract_var_name_suffix(var_name: str) -> str:
        """
        Extracts the suffix part of a COBOL variable name
        Example:
        - "X(7:8)" -> "(7:8)"
        - "X" -> ""
        """
        suffix = ""
        in_parens = False
        for c in var_name:
            if c == "(":
                in_parens = True
            if in_parens:
                suffix += c
        return suffix

    @staticmethod
    def get_statements_generator(
        interested_stmt_tags: list[str],
    ):
        """
        Return a generator that yields all interested Statements,
        along with the condition (type, clause) from the parent Evaluate/If statement.
        """

        def __generator(possible_statements: list, current_condition=None):
            for possible_stmt in possible_statements:
                condition = current_condition

                if isinstance(possible_stmt, Statement):
                    stmt = possible_stmt

                    # Yield the Move/ExecSQL statement with current condition
                    if stmt.tag in interested_stmt_tags:
                        yield stmt, current_condition
                        continue  # Skip processing other attributes

                    # Process If statement
                    elif stmt.tag == "IfStatement":
                        yield from __generator(
                            stmt.ifThen,
                            {"type": "If", "clause": stmt.condition},
                        )
                        yield from __generator(
                            stmt.ifElse,
                            {"type": "If", "clause": f"NOT({stmt.condition})"},
                        )
                        continue  # Skip processing other attributes

                    # Process Evaluate statement
                    elif stmt.tag == "EvaluateStatement":
                        condition_type = f"Evaluate {stmt.evaluate_identifier}"
                        for when_clause in stmt.evaluateWhenPhrase:
                            yield from __generator(
                                when_clause.statement,
                                {
                                    "type": condition_type,
                                    "clause": when_clause.evaluateWhen,
                                },
                            )
                        continue  # Skip processing other attributes

                # Search for statements in all fields
                if hasattr(possible_stmt, "__dict__"):
                    for attr_name, attr_value in possible_stmt.__dict__.items():
                        if attr_name.startswith("_"):
                            continue  # Skip private fields
                        if isinstance(attr_value, list):
                            yield from __generator(attr_value, condition)
                        elif hasattr(attr_value, "__dict__"):
                            yield from __generator([attr_value], condition)

        return __generator

    @staticmethod
    def get_copybook_variable_declarations(
        repository_id: str, copybook: dict
    ) -> list[dict]:
        """
        Fetch copybook data and retrieve the variable declarations list.
        Replace the variable names according to replacing rule.
        """
        copybook_name = copybook.get("copybook_name").strip("'")
        replacing_rules = copybook.get("replacing", [])
        copybook_data = VariableFlowUtils.__query_copybook(copybook_name, repository_id)
        variable_declarations = copybook_data.get("variables_declaration", [])

        for declaration in variable_declarations:
            replaceable, replacement = ("", "")
            for rule in replacing_rules:
                if rule.get("replaceable").replace("=", "") in declaration.get(
                    "name", ""
                ):
                    replaceable = rule.get("replaceable").replace("=", "")
                    replacement = rule.get("replacement").replace("=", "")
                    break
            declaration["name"] = declaration.get("name", "").replace(
                replaceable, replacement
            )

        return variable_declarations

    @staticmethod
    def get_copybook_first_var_level(repository_id: str, copybook: dict) -> int:
        """
        Retrieve the lowest level (highest in hierarchy) of variable in a copybook.
        Return -1 if there are no variable declarations.
        """
        copybook_name = copybook.get("copybook_name").strip("'")
        copybook_data = VariableFlowUtils.__query_copybook(copybook_name, repository_id)
        variable_declarations = copybook_data.get("variables_declaration", [])
        return (
            int(variable_declarations[0].get("level")) if variable_declarations else -1
        )

    @staticmethod
    def __query_copybook(copybook_name: str, repository_id: str) -> dict:
        try:
            mongo_uri = f"mongodb://{os.getenv('MONGODB_USER')}:{os.getenv('MONGODB_PASSWORD')}@{os.getenv('MONGODB_HOST')}:{os.getenv('MONGODB_PORT')}/{os.getenv('MONGODB_DB_NAME')}?authSource=admin"
            client = MongoClient(mongo_uri)
            db = client.mainframe
            collection = db.reverse_engineering

            result = collection.find_one(
                {
                    "name": copybook_name,
                    "repository_id": ObjectId(repository_id),
                    "type": "COPY",
                }
            )

            if result and result.get("output"):
                return result["output"]
            else:
                logger.error(f"No copybook found for {copybook_name}")
                return {}

        except Exception as e:
            logger.error(f"Error querying copybook: {str(e)}")
            return {}

    @staticmethod
    def get_working_storage_copybooks(
        copybooks: list[dict], io_files: list[dict]
    ) -> list[dict]:
        """
        Find working storage copybooks by excluding all io_file copybooks from the main copybooks list
        """
        # Note: we can use the below implementation because:
        # - The copybooks order is kept when collected
        # - All COPY statements from IO files come before working storage

        if not io_files:
            return copybooks

        io_last_copybook = VariableFlowUtils.__get_io_files_last_copybook(io_files)
        if not io_last_copybook:
            return copybooks

        io_last_copybook_index = VariableFlowUtils.__get_io_files_last_copybook_index(
            io_last_copybook, copybooks
        )
        return copybooks[io_last_copybook_index + 1 :]

    @staticmethod
    def __get_io_files_last_copybook(io_files: list[dict]):
        """Find the last copybook for IO files. Return None if not found"""
        for i in range(len(io_files) - 1, 0, -1):
            file = io_files[i]
            file_copybooks = file.get("copybooks")
            if file_copybooks:
                return file_copybooks[-1]
        return None

    @staticmethod
    def __get_io_files_last_copybook_index(
        io_last_copybook: dict, copybooks: list[dict]
    ) -> int:
        """Find index of the last copybook for IO files in all copybooks"""
        io_last_copybook_index = -1
        for i, copybook in enumerate(copybooks):
            if (
                copybook["copybook_name"] == io_last_copybook["copybook_name"]
                and copybook["line_number"] == io_last_copybook["line_number"]
            ):
                io_last_copybook_index = i
                break
        return io_last_copybook_index

    @staticmethod
    def build_expanded_variable_tree_dict(
        repository_id: str, variables: list[dict], copybooks: list[dict]
    ) -> dict[str, dict]:
        """
        Expand copybook variables and merge with direct variables.
        Build variable hierarchy and populate byte length.
        Return the dictionary that map variable name to variable tree.
        """
        # Expand copybooks, build variable hierarchy and populate byte length
        variable_hierarchy = VariableFlowUtils.build_expanded_variable_hierarchy(
            repository_id, variables, copybooks
        )

        # Return the dictionary that maps variable name to variable tree
        return VariableFlowUtils.__build_var_name_to_var_tree_dict(variable_hierarchy)

    @staticmethod
    def build_expanded_variable_hierarchy(
        repository_id: str, variables: list[dict], copybooks: list[dict]
    ) -> list[dict]:
        """
        Expand copybook variables and merge with direct variables.
        Build variable hierarchy and populate byte length.
        Return the variable hierarchy.
        """
        # Expand copybook variables and merge with direct variables
        expanded_vars = VariableFlowUtils.__expand_copybooks(
            repository_id, variables, copybooks
        )

        # Build variable hierarchy
        variable_hierarchy = VariableFlowUtils.__build_variable_hierarchy(expanded_vars)

        # Populate byte length for variables with higher hierarchy
        VariableFlowUtils.__backfill_byte_length(variable_hierarchy)

        # Return the variable hierarchy
        return variable_hierarchy

    @staticmethod
    def __expand_copybooks(
        repository_id: str, variables: list[dict], copybooks: list[dict]
    ) -> list[dict]:
        """Expand copybook variables and merge with direct variables"""
        # Get all copybook variables along with line number of the COPY statement
        copybook_vars_with_position = (
            VariableFlowUtils.__get_copybook_vars_with_position(
                repository_id, copybooks
            )
        )

        # Merge direct variables with copybook variables based on line numbers
        expanded_variables = VariableFlowUtils.__merge_direct_vars_and_copybook_vars(
            variables, copybook_vars_with_position
        )

        return expanded_variables

    @staticmethod
    def __merge_direct_vars_and_copybook_vars(
        variables, copybook_vars_with_position
    ) -> list[dict]:
        """Merge direct variables with copybook variables based on line numbers"""
        merged_variables = []
        var_cursor = 0

        for copybook_line, copybook_vars in copybook_vars_with_position:
            # Append direct variables that come before current COPY statement
            while var_cursor < len(variables):
                var = variables[var_cursor]
                if int(var.get("line_number")) > copybook_line:
                    break
                merged_variables.append(var)
                var_cursor += 1

            # Append all copybook variables for current COPY statement
            merged_variables.extend(copybook_vars)

        # Append the remaining direct variables
        merged_variables.extend(variables[var_cursor:])

        return merged_variables

    @staticmethod
    def __get_copybook_vars_with_position(
        repository_id: str, copybooks: list[dict]
    ) -> list[tuple[int, list[dict]]]:
        """Get copybook variables along with the corresponding COPY statement line number"""
        copybook_vars_with_position = []
        for copybook in copybooks:
            copybook_vars = VariableFlowUtils.get_copybook_variable_declarations(
                repository_id, copybook
            )
            if copybook_vars:
                copybook_vars_with_position.append(
                    (int(copybook.get("line_number")), copybook_vars)
                )
        return copybook_vars_with_position

    @staticmethod
    def __build_variable_hierarchy(variables: list[dict]) -> list[dict]:
        """
        Build a hierarchy of variables based on their levels.
        Add children field to the processed variables (mutate).
        """
        hierarchy = []
        stack = []  # a monotonically increasing stack based on variable level

        for var in variables:
            # Keep popping variable with higher level (lower hierarchy) than current variable
            while stack and int(stack[-1].get("level")) >= int(var.get("level")):
                stack.pop()

            if stack:
                # If the stack is not empty, the last variable is the parent of the current variable
                parent = stack[-1]
                parent[VarExtraProps.CHILDREN].append(var)
                var["parent_name"] = parent.get("name")
            else:
                # If the stack is empty, the current variable is a top-level variable
                hierarchy.append(var)
                var["parent_name"] = None

            # Push the variable to the stack to populate their children
            var[VarExtraProps.CHILDREN] = []
            stack.append(var)

        return hierarchy

    @staticmethod
    def __backfill_byte_length(variable_hierarchy: list[dict]) -> None:
        """
        Iteratively backfill the byte_length of parent variables (0 initially) by summing their children's byte_length.
        The variable trees need to be expanded fully (expand all copybook declarations).
        """
        queue = deque()
        node_list = []

        # Flatten all nodes using a queue (breadth-first)
        for top_variable in variable_hierarchy:
            queue.append(top_variable)
            while queue:
                node = queue.popleft()
                node_list.append(node)
                queue.extend(VariableFlowUtils.get_var_children(node))

        # Process nodes in reverse order (ensure children's byte_length are backfilled before parents)
        for i in range(len(node_list) - 1, -1, -1):
            node = node_list[i]
            node_children = VariableFlowUtils.get_var_children(node)
            if node_children:
                node["byte_length"] = sum(
                    child["byte_length"] for child in node_children
                )

    @staticmethod
    def __build_var_name_to_var_tree_dict(
        variable_hierarchy: list[dict],
    ) -> dict[str, dict]:
        """Build dictionary to lookup variable tree by variable name"""
        var_name_to_var_tree_dict = {}
        stack = variable_hierarchy
        while stack:
            var = stack.pop()
            var_name_to_var_tree_dict[var["name"]] = var
            stack.extend(VariableFlowUtils.get_var_children(var))
        return var_name_to_var_tree_dict

    @staticmethod
    def build_var_name_to_var_dict(variables: list[dict]) -> dict[str, dict]:
        """Build dictionary to lookup variable by variable name"""
        var_name_to_variable_dict = {}
        for var in variables:
            var_name_to_variable_dict[var["name"]] = var
        return var_name_to_variable_dict

    @staticmethod
    def get_var_children(var_node: dict) -> list[dict]:
        """Retrieve the children of a variable tree node"""
        return var_node.get(VarExtraProps.CHILDREN, [])

    @staticmethod
    def process_redefine_occur(declarations: list[dict]) -> None:
        """
        Find array variables and variables that are redefined.
        Map default values from redefined variables to array variables.
        (This function mutate 'declarations')
        """
        # Identify array variables and variables that are redefined
        (redefined_var_name_set, array_var_name_to_redefined_var_name_dict) = (
            VariableFlowUtils.__identify_redefined_and_array_vars(declarations)
        )

        # Build variable trees for identified variables
        (array_var_name_to_var_tree_dict, redefined_var_name_to_var_tree_dict) = (
            VariableFlowUtils.__build_redefined_and_array_var_trees(
                declarations,
                redefined_var_name_set,
                array_var_name_to_redefined_var_name_dict,
            )
        )

        # Map default values from redefined variables to array variables
        for array_var_name, array_var_tree in array_var_name_to_var_tree_dict.items():
            redefined_var_name = array_var_name_to_redefined_var_name_dict[
                array_var_name
            ]
            redefined_var_tree = redefined_var_name_to_var_tree_dict[redefined_var_name]
            VariableFlowUtils.__map_redefine_occur_values(
                array_var_tree, redefined_var_tree
            )

    @staticmethod
    def __identify_redefined_and_array_vars(
        declarations: list[dict],
    ) -> tuple[set[str], dict[str, str]]:
        """Identifies redefined and array variables from the declarations"""
        redefined_var_name_set = set()
        array_var_name_to_redefined_var_name_dict = {}

        for i in range(len(declarations)):
            var = declarations[i]
            remarks = var["remarks"]
            var_name = var["name"]

            # 'remarks' is redefined variable name (type str) OR number of occurs (type int)
            # the variable with 'int remarks' must exists and come right after the variable with 'str remarks'
            # TODO: handle no intermediate variable for defining occur
            if remarks and isinstance(remarks, str):
                next_var = declarations[i + 1] if i < len(declarations) - 1 else None
                if not next_var or not isinstance(next_var.get("remarks"), int):
                    continue

                redefined_var_name_set.add(remarks)
                array_var_name_to_redefined_var_name_dict[var_name] = remarks

        return redefined_var_name_set, array_var_name_to_redefined_var_name_dict

    @staticmethod
    def __build_redefined_and_array_var_trees(
        declarations,
        redefined_var_name_set,
        array_var_name_to_redefined_var_name_dict,
    ) -> tuple[dict[str, dict], dict[str, dict]]:
        """Builds variable trees for redefined and array variables"""
        array_var_name_to_var_tree_dict = {}
        redefined_var_name_to_var_tree_dict = {}

        i = 0
        while i < len(declarations):
            var = declarations[i]
            var_name = var["name"]

            if (
                var_name not in redefined_var_name_set
                and var_name not in array_var_name_to_redefined_var_name_dict
            ):
                i += 1
                continue

            # Collect variables in this tree
            variables_in_tree = [var]
            i += 1
            while i < len(declarations) and int(declarations[i]["level"]) > int(
                var["level"]
            ):
                variables_in_tree.append(declarations[i])
                i += 1

            # Build the variable tree
            variable_tree = VariableFlowUtils.__build_variable_hierarchy(
                variables_in_tree
            )[0]

            # Add the variable tree to the correct dictionary
            if var_name in redefined_var_name_set:
                redefined_var_name_to_var_tree_dict[var_name] = variable_tree
            elif var_name in array_var_name_to_redefined_var_name_dict:
                array_var_name_to_var_tree_dict[var_name] = variable_tree

        return array_var_name_to_var_tree_dict, redefined_var_name_to_var_tree_dict

    @staticmethod
    def __map_redefine_occur_values(
        array_var_tree: dict, redefined_var_tree: dict
    ) -> None:
        """
        Iteratively map default values from redefined variables to array variables.
        Only process children after the root nodes
        """
        # TODO: handle no intermediate variable for defining occurs
        # (for now assume that there's always one)
        root_children = VariableFlowUtils.get_var_children(array_var_tree)
        if not root_children:
            return
        occur_var_tree = root_children[0]

        array_children = VariableFlowUtils.get_var_children(occur_var_tree)
        redefined_children = VariableFlowUtils.get_var_children(redefined_var_tree)

        if not array_children or not redefined_children:
            return

        # Cycle through the array variables repeatedly until all redefined variables are mapped.
        i, j = 0, 0
        array_var_count = len(array_children)
        redefined_var_count = len(redefined_children)

        while j < redefined_var_count:
            array_node = array_children[i]
            redefined_node = redefined_children[j]

            array_node.setdefault("default_value_set", set())
            redefined_node_default_value = redefined_node["default_value"].strip()
            if (
                redefined_node_default_value
                and redefined_node_default_value not in DEFAULT_VALUES_TO_SKIP
            ):
                array_node["default_value_set"].add(redefined_node_default_value)

            i = (i + 1) % array_var_count
            j += 1

    @staticmethod
    def add_single_flow_entry(
        entry, existing_entries: list[dict], existing_key_set: set[tuple]
    ) -> bool:
        """
        Add a variable flow entry if it is not duplicate.
        Return True if the entry is added, False otherwise.
        """
        key = VariableFlowUtils.__get_flow_entry_key(entry)
        if key in existing_key_set:
            return False

        existing_entries.append(entry)
        existing_key_set.add(key)
        return True

    @staticmethod
    def __get_flow_entry_key(entry: dict) -> tuple:
        """Generate unique and hashable key for a variable flow entry."""
        return (
            entry["name"],
            entry["parent_name"],
            entry["data_type"],
            entry["length"],
            entry["src_variable"],
            entry["src_parent_name"],
            entry["src_data_type"],
            entry["src_length"],
            VariableFlowUtils.__normalize_condition_clause(
                entry.get("condition_clause")
            ),
            entry.get("condition_type"),
        )

    @staticmethod
    def __normalize_condition_clause(clause: list[str] | str) -> tuple[str] | str:
        # Condition clause for Evaluate statement is a list -> convert it to a tuple
        if isinstance(clause, list):
            return tuple(clause)
        return clause

    @staticmethod
    def process_children_of_pair(
        var_children: list[dict],
        src_var_children: list[dict],
        add_children_flow_fn: Callable[[dict, dict], None],
        var_start_index: int = 0,
        src_start_index: int = 0,
    ) -> None:
        """
        Process children for a pair of variables that have flow entry.
        Matches children based on order and byte_length.
        """
        # (*) Assumption:
        # Mapping 1-1 and 1-many between variables
        #
        # (*) TODO:
        # Handle variable overlapping, for example:
        # 01 A length = 3
        #     03 A1 length = 2
        #         05 A11 length = 1
        #         05 A12 length = 1
        #     03 A2 length = 1
        # 01 B length = 3
        #     03 B1 length = 1
        #     03 B2 length = 2
        #         05 B21 length = 1
        #         05 B21 length = 1
        # move B to A

        var_index = var_start_index
        src_index = src_start_index

        # Running byte_length sums to match variables and their children
        var_byte_sum = 0
        src_byte_sum = 0

        while var_index < len(var_children) and src_index < len(src_var_children):
            var_child = var_children[var_index]
            src_child = src_var_children[src_index]

            # Add flow entry for current matching pair
            add_children_flow_fn(var_child, src_child)

            var_child_children = VariableFlowUtils.get_var_children(var_child)
            src_child_children = VariableFlowUtils.get_var_children(src_child)

            # Compute the start indices for children recursion
            # - Check if the first child of 1 side should corresponding to which child of the other side
            # - If var_byte_sum < src_byte_sum, it means we need to skip over some children of var_child,
            #   because var_byte_sum actually becomes greater in the last iteration. And vice versa.
            child_var_start_index = 0
            child_src_start_index = 0

            if var_byte_sum < src_byte_sum:
                child_var_start_index = VariableFlowUtils.__find_child_start_index(
                    var_child_children, src_byte_sum - var_byte_sum
                )
            elif var_byte_sum > src_byte_sum:
                child_src_start_index = VariableFlowUtils.__find_child_start_index(
                    src_child_children, var_byte_sum - src_byte_sum
                )

            # Recursively process the overlapping children of this pair
            VariableFlowUtils.process_children_of_pair(
                var_child_children,
                src_child_children,
                add_children_flow_fn,
                child_var_start_index,
                child_src_start_index,
            )

            # Update byte_length sums when the current pair is involved
            var_byte_sum += var_child["byte_length"]
            src_byte_sum += src_child["byte_length"]

            # Adjust indices (advance 1 or both pointers)
            if var_byte_sum == src_byte_sum:
                var_index += 1
                src_index += 1
            elif var_byte_sum < src_byte_sum:
                var_index += 1
                src_byte_sum -= src_child[
                    "byte_length"
                ]  # will be added again in the next iteration
            else:
                src_index += 1
                var_byte_sum -= var_child[
                    "byte_length"
                ]  # will be added again in the next iteration

    @staticmethod
    def __find_child_start_index(children: list[dict], skipped_bytes: int) -> int:
        """Finds the index in children where the accumulated byte_length exceeds skipped_bytes"""
        current_byte_sum = 0
        for i, child in enumerate(children):
            current_byte_sum += child["byte_length"]
            if current_byte_sum > skipped_bytes:
                return i
        return 0
