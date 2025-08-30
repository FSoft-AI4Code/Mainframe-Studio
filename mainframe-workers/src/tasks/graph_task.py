from collections import defaultdict, deque
from typing import Any, Deque, Dict, List, Set, Tuple
import structlog
import re
from pymongo import MongoClient
from bson import ObjectId
import os
from classifier.constants import FileType
from config.constants import IBM_MAINFRAME_UTILITIES
from controller.edge_controller import (
    DependencyGraphEdge,
    EdgeController,
    RelationshipLabel,
)
from controller.entry_flow_edges import (
    EntryFlowEdge,
    EntryFlowEdgeController
)
from controller.entry_point_controller import EntryPoint, EntryPointController
from controller.node_controller import (
    DependencyGraphNode,
    FileType,
    NodeController,
    NodeStatus,
)
from controller.reverse_controller import ReverseController
from parsers.variable_flow_utils import VariableFlowUtils
from parsers.constants import DEFAULT_VALUES_TO_SKIP
from schema.reverse_engineering import (
    ReverseEngineeringStatus,
    ReverseEngineeringUpdate,
)
from .base_task import BaseTask

logger = structlog.get_logger()


class GraphTask(BaseTask):
    def __init__(self):
        self.reverse_controller = ReverseController()
        self.node_controller = NodeController()
        self.edge_controller = EdgeController()
        self.entry_flow_edge_controller = EntryFlowEdgeController()
        self.entry_point_controller = EntryPointController()

    def validate(self, data: dict) -> bool:
        if not data.get("repository_id"):
            logger.error("No repository_id provided in task data")
            return False
        if not data.get("name"):
            logger.error("No name provided in task data")
            return False
        if not data.get("label"):
            logger.error("No label provided in task data")
            return False

        # Validate FileType enum
        try:
            label = data.get("label")
            if label not in FileType.__members__:
                logger.error(f"Invalid file type: {label}")
                return False
        except Exception as e:
            logger.error(f"Error validating file type: {str(e)}")
            return False

        return True

    def _add_edge(
        self,
        repository_id: str,
        existing_nodes: Dict[Tuple[str, FileType], DependencyGraphNode],
        id_to_nodes: Dict[str, DependencyGraphNode],
        source: DependencyGraphNode,
        target_key: Tuple[str, FileType],
        edge_type: RelationshipLabel,
        edge_properties: Dict[str, Any],
    ):
        target = existing_nodes.get(target_key)
        if not target:
            target_name, target_label = target_key

            # UTILITY files are built-in files, so we set their status to ALIVE
            if target_label == FileType.UTILITY:
                status = NodeStatus.ALIVE
            else:
                # Create new node with MISSING status since we haven't had its source code
                status = NodeStatus.MISSING

            target_is_entry_point = self.__is_entry_point(target_label)
            target = DependencyGraphNode(
                repository_id=repository_id,
                name=target_name,
                label=target_label,
                status=status,
                is_entry_point=target_is_entry_point,
                group=self.__get_initial_group(target_name, target_is_entry_point),
            )

            self.node_controller.save_node(target)
            id_to_nodes[target.id] = target
            existing_nodes[target_key] = target

        # If the source node is a DEAD entry point, mark it as ALIVE
        if source.is_entry_point and source.status == NodeStatus.DEAD:
            source.status = NodeStatus.ALIVE
            self.node_controller.save_node(source)

        # Create or update the edge
        self.edge_controller.save_edge(
            DependencyGraphEdge(
                repository_id=repository_id,
                source=source.id,
                target=target.id,
                type=edge_type,
                properties=edge_properties,
            )
        )

    def __add_entry_flow_edge(
        self,
        repository_id: str,
        existing_nodes: Dict[Tuple[str, FileType], DependencyGraphNode],
        id_to_nodes: Dict[str, DependencyGraphNode],
        source: DependencyGraphNode,
        target_key: Tuple[str, FileType],
        edge_type: RelationshipLabel,
        edge_properties: Dict[str, Any]
    ):
        """
        Use to handle EXEC CICS statement with SEND and XCTL command.
        Source label is COBOL. Target label is BMS/COBOL.
        Save the edge from COBOL to BMS/COBOL to new collection 'entry_flow_edges'.
        This is used to track the flow of entry points in the dependency graph.
        and downsize the current edge collection.
        the node is still saved in the current collection.
        """

        target = existing_nodes.get(target_key)
        if not target:
            target_name, target_label = target_key

            target_is_entry_point = self.__is_entry_point(target_label)

            target = DependencyGraphNode(
                repository_id=repository_id,
                name=target_name,
                label=target_label,
                status=NodeStatus.MISSING,
                is_entry_point=target_is_entry_point,
                group=self.__get_initial_group(target_name, target_is_entry_point),
            )

            self.node_controller.save_node(target)
            id_to_nodes[target.id] = target
            existing_nodes[target_key] = target

        self.entry_flow_edge_controller.save_edge(
            EntryFlowEdge(
                repository_id=repository_id,
                source=source.id,
                target=target.id,
                type=edge_type,
                properties=edge_properties,
            )
        )

    def __add_reverse_edge(
        self,
        repository_id: str,
        existing_nodes: Dict[Tuple[str, FileType], DependencyGraphNode],
        id_to_nodes: Dict[str, DependencyGraphNode],
        target: DependencyGraphNode,
        source_key: Tuple[str, FileType],
        edge_type: RelationshipLabel,
        edge_properties: Dict[str, Any],
    ) -> DependencyGraphNode:
        """
        Use to handle EXEC CICS statement with RECEIVE command.
        Source label is BMS. Target label is COBOL.
        Return the source BMS node.
        """
        source_name, source_label = source_key
        if source_label != FileType.BMS and target.label != FileType.COBOL:
            raise ValueError("Reverse edge must be from BMS to COBOL")

        source = existing_nodes.get(source_key)
        if not source:
            # Create new node with MISSING status since we haven't had its source code
            # The new node will be an entrypoint and has its own group (because source label is BMS)
            source = DependencyGraphNode(
                repository_id=repository_id,
                name=source_name,
                label=source_label,
                status=NodeStatus.MISSING,
                is_entry_point=True,
                group=set([source_name]),
            )

            self.node_controller.save_node(source)
            id_to_nodes[source.id] = source
            existing_nodes[source_key] = source
        else:
            # If the source node is a DEAD entry point, mark it as ALIVE
            if source.status == NodeStatus.DEAD:
                source.status = NodeStatus.ALIVE
                self.node_controller.save_node(source)
        edge_properties = {**edge_properties, "is_reverse": True}
        # Create or update the edge
        edge = DependencyGraphEdge(
            repository_id=repository_id,
            source=source.id,
            target=target.id,
            type=edge_type,
            properties=edge_properties,
        )
        entry_flow_edge_instance = EntryFlowEdge(
            repository_id=repository_id,
            source=source.id,
            target=target.id,
            type=edge_type,
            properties=edge_properties,
        )
        self.edge_controller.save_edge(edge)
        self.entry_flow_edge_controller.save_edge(entry_flow_edge_instance)

        return source

    def _mark_reachable_nodes(
        self,
        edges: List[Dict],
        entry_points: List[DependencyGraphNode],
        id_to_nodes: Dict[str, DependencyGraphNode],
    ):
        """Mark all nodes reachable from entry points as ALIVE"""
        # Build adjacency list
        graph = defaultdict(list)
        for edge in edges:
            source_id = str(edge["source"])
            target_id = str(edge["target"])
            # Only add edge if both nodes exist
            if source_id in id_to_nodes and target_id in id_to_nodes:
                graph[source_id].append(target_id)

        # BFS from entry points with outgoing edges
        visited = set()
        queue = deque([ep.id for ep in entry_points if graph[ep.id]])

        while queue:
            node_id = queue.popleft()
            if node_id in visited or node_id not in id_to_nodes:
                continue

            visited.add(node_id)
            node = id_to_nodes[node_id]

            # Mark reachable node as ALIVE if not MISSING
            if node.status != NodeStatus.MISSING:
                node.status = NodeStatus.ALIVE
                self.node_controller.save_node(node)

            # Add unvisited neighbors
            for neighbor_id in graph[node_id]:
                if neighbor_id not in visited and neighbor_id in id_to_nodes:
                    queue.append(neighbor_id)

        # Mark unreachable nodes as DEAD if not MISSING
        for node in id_to_nodes.values():
            if node.id not in visited and node.status != NodeStatus.MISSING:
                node.status = NodeStatus.DEAD
                self.node_controller.save_node(node)

    def _mark_group_helper(
        self,
        graph: Dict[str, List[str]],
        current_node: DependencyGraphNode,
        id_to_nodes: Dict[str, DependencyGraphNode],
        nodes_to_be_visited: Deque[DependencyGraphNode],
    ):
        for id in graph[current_node.id]:
            new_node = id_to_nodes[id]
            if any(current_node.group - new_node.group):
                new_node.group |= current_node.group
                self.node_controller.save_node(new_node)
                nodes_to_be_visited.append(new_node)

    def _mark_group(
        self,
        graph: Dict[str, List[str]],
        root_node: DependencyGraphNode,
        id_to_nodes: Dict[str, DependencyGraphNode],
    ):
        """Add groups from the root node to its descendants"""
        nodes_to_be_visited = deque([root_node])
        while len(nodes_to_be_visited) > 0:
            current_node = nodes_to_be_visited.popleft()
            self._mark_group_helper(
                graph, current_node, id_to_nodes, nodes_to_be_visited
            )

    @staticmethod
    def _find_label_for_copybooks(node_name):
        return (
            FileType.UTILITY if node_name in IBM_MAINFRAME_UTILITIES else FileType.COPY
        )

    @staticmethod
    def _extract_jcl_step_properties(step_info: Dict) -> Dict:
        """
        Extracts and structures properties from a JCL step.
        """
        step_name = step_info.get("step_name", "")
        statements = step_info.get("dd_statement", [])

        return {
            "step_name": step_name,
            "statements": [
                {
                    "ddname": stmt.get("ddname"),
                    "parameters_map": stmt.get("parameters_map"),
                    "dataset_map_list": stmt.get("dataset_map_list"),
                    "logic": stmt.get("logic"),
                }
                for stmt in statements
            ],
        }

    @staticmethod
    def _find_node_key_for_copybooks(
        node_name: str, existing_nodes: Set[Tuple[str, FileType]]
    ) -> Tuple[str, FileType]:
        """Find correct node key for copybook with path handling"""
        # Strip quotes and normalize path
        name = node_name.strip("\"'").replace("\\", "/")

        # Try different name variations in order
        variations = [
            node_name,  # Original name
            name,  # Normalized name
            name.replace("_", "/"),  # Underscores as slashes
            name.split("/")[-1],  # Just filename
        ]

        # Try each variation until we find a match
        for variation in variations:
            key = (variation, GraphTask._find_label_for_copybooks(variation))
            if key in existing_nodes:
                return key

        # Return last variation if no match found
        return (variations[-1], GraphTask._find_label_for_copybooks(variations[-1]))

    def _update_entry_point(
        self,
        repository_id: str,
        entrypoint_node_key: Tuple[str, FileType],
        existing_nodes: List[DependencyGraphNode],
    ):
        reverse_engineerings = []
        entrypoint_node_name, entrypoint_node_label = entrypoint_node_key

        for node in existing_nodes:
            if node.status != NodeStatus.MISSING and entrypoint_node_name in node.group:
                rv = self.reverse_controller.query_reverse_engineering(
                    node.name,
                    repository_id,
                    str(node.label),
                    projection={"output.line_of_code": 1, "output.complexity": 1},
                )
                if rv is None:
                    logger.error(
                        f"Can't get reverse engineering for {node.name}, {node.label}"
                    )
                else:
                    reverse_engineerings.append(rv)

        entry_point_complexity = sum(
            rv.get("complexity", 0) for rv in reverse_engineerings
        )
        # default complexity of entry point is 1
        entry_point_complexity = entry_point_complexity or 1

        entry_point_data = {
            "number_of_files": len(reverse_engineerings),
            "line_of_code": sum(
                rv.get("line_of_code", 0) for rv in reverse_engineerings
            ),
            "complexity": entry_point_complexity,
        }

        self.entry_point_controller.save_entry_point(
            EntryPoint(
                repository_id=repository_id,
                name=entrypoint_node_name,
                label=entrypoint_node_label,
                **entry_point_data,
            )
        )

    def execute(self, data: dict) -> dict:
        input_node_reverse_engineering = (
            self.reverse_controller.query_reverse_engineering(
                data.get("name", "").replace("'", ""),
                data.get("repository_id", ""),
                data.get("label"),
            )
        )

        if input_node_reverse_engineering:
            is_input_node_missing = False
        else:
            is_input_node_missing = True

        try:
            if not self.validate(data):
                error_msg = "Invalid task data"
                logger.error(error_msg, data=data)
                return {"status": "error", "message": error_msg}

            repository_id = data.get("repository_id")
            name = data.get("name").replace("'", "")
            label_str = data.get("label")

            try:
                label = (
                    FileType.UTILITY
                    if name in IBM_MAINFRAME_UTILITIES
                    else FileType[label_str]
                )
            except KeyError:
                error_msg = f"Unsupported file type: {label_str}"
                logger.error(error_msg, data=data)
                return {"status": "error", "message": error_msg}

            source_node_key = (name, label)
            logger.info(f"Processing graph node", name=name, label=label_str)

            try:
                # Setup nodes
                existing_nodes = {
                    (node["name"], node["label"]): DependencyGraphNode.from_dict(node)
                    for node in self.node_controller.get_all_nodes(repository_id)
                }
                id_to_nodes = {node.id: node for node in existing_nodes.values()}

                # Track entry points for later
                entry_points = []

                # Create or update source node
                source_node = existing_nodes.get(source_node_key)

                if source_node:
                    if source_node.is_entry_point:
                        entry_points.append(source_node)
                    if source_node.status == NodeStatus.MISSING:
                        source_node.status = NodeStatus.DEAD
                        self.node_controller.save_node(source_node)
                else:
                    is_entry_point = self.__is_entry_point(label)
                    source_node = DependencyGraphNode(
                        repository_id=repository_id,
                        name=name,
                        label=label,
                        status=NodeStatus.DEAD,
                        is_entry_point=is_entry_point,
                        group=self.__get_initial_group(name, is_entry_point),
                    )

                    existing_nodes[source_node_key] = source_node
                    self.node_controller.save_node(source_node)
                    id_to_nodes[source_node.id] = source_node
                    if is_entry_point:
                        entry_points.append(source_node)

                swapped_source_nodes = (
                    []
                )  # source node may be swapped for EXEC CICS RECEIVE

                # Process based on file type
                if label != FileType.BMS:
                    parser_output = self.reverse_controller.query_reverse_engineering(
                        name, repository_id, label.value
                    )
                    handlers = {
                        FileType.WFL: self._handle_wfl_nodes,
                        FileType.JCL: self._handle_jcl_nodes,
                        FileType.COBOL: self._handle_cobol_nodes,
                        FileType.PANEL: self._handle_Panel_nodes
                    }
                    handler = handlers.get(label)
                    if handler:
                        swapped_source_nodes = (
                            handler(
                                repository_id,
                                parser_output,
                                source_node,
                                existing_nodes,
                                id_to_nodes,
                            )
                            or []
                        )

                elif "program" in data:
                    # Handle BMS
                    program = data.get("program").replace("'", "")
                    program_node_key = (program, FileType.COBOL)
                    self._add_edge(
                        repository_id,
                        existing_nodes,
                        id_to_nodes,
                        source_node,
                        program_node_key,
                        RelationshipLabel.HAS_INTERACT,
                        {},
                    )

                # Get all existing entry points
                for node in existing_nodes.values():
                    if node.is_entry_point and node not in entry_points:
                        entry_points.append(node)

                # Get all edges and mark reachable nodes
                entry_flow_edge = self.entry_flow_edge_controller.get_all_edges(repository_id)
                non_reverse_entry_flow_edge = [
                    edge for edge in entry_flow_edge if not edge.get("properties", {}).get("is_reverse", False)
                ]
                edges = self.edge_controller.get_all_edges(repository_id) + non_reverse_entry_flow_edge
                self._mark_reachable_nodes(edges, entry_points, id_to_nodes)

                # Process groups
                edges = self.edge_controller.get_all_edges(repository_id)  + non_reverse_entry_flow_edge
                graph = defaultdict(list)
                for edge in edges:
                    for id_field in ["_id", "source", "target"]:
                        edge[id_field] = str(edge[id_field])
                    graph[edge["source"]].append(edge["target"])
                    del edge["repository_id"]

                # Build dictionary to lookup entry point quickly,
                # and flatten existing node list from exiting_nodes dictionary
                entry_point_name_to_key_dict = {}
                existing_node_list = []
                for node_key, node in existing_nodes.items():
                    existing_node_list.append(node)
                    if node.is_entry_point:
                        entry_point_name_to_key_dict[node.name] = node_key

                # First, assign groups starting from the swapped source nodes (if there are any)
                # Then, assign groups starting from the current node.
                # This is necessary because the first step may stop at the current node (if no new groups are found),
                # but the current node's children still need to be processed.
                if swapped_source_nodes:
                    for entrypoint_node in swapped_source_nodes:
                        self._mark_group(graph, entrypoint_node, id_to_nodes)
                self._mark_group(graph, source_node, id_to_nodes)

                # Update data for entrypoints
                entrypoint_nodes_to_update = swapped_source_nodes
                if source_node.is_entry_point:
                    entrypoint_nodes_to_update.append(source_node)

                for entrypoint_node in entrypoint_nodes_to_update:
                    for group_name in entrypoint_node.group:
                        if group_name not in entry_point_name_to_key_dict:
                            continue
                        entrypoint_node_key = entry_point_name_to_key_dict[group_name]
                        self._update_entry_point(
                            repository_id, entrypoint_node_key, existing_node_list
                        )

                if not is_input_node_missing:
                    reverse_engineering_status_update = ReverseEngineeringUpdate(
                        status=ReverseEngineeringStatus.LINKED
                    )
                    self.reverse_controller.save_reverse_engineering(
                        name,
                        repository_id,
                        reverse_engineering_status_update,
                        type=label_str,
                    )

                return {
                    "status": "success",
                    "message": f"Successfully added file {name} of repository {repository_id} into the dependency graph",
                    "output": {"graph": {"repository_id": repository_id}},
                }

            except Exception as e:
                if not is_input_node_missing:
                    reverse_engineering_status_update = ReverseEngineeringUpdate(
                        status=ReverseEngineeringStatus.LINKED_ERROR
                    )
                    self.reverse_controller.save_reverse_engineering(
                        name,
                        repository_id,
                        reverse_engineering_status_update,
                        type=label_str,
                    )

                error_msg = f"Error processing graph node: {str(e)}"
                logger.error(error_msg, error=str(e), data=data, exc_info=True)
                return {"status": "error", "message": error_msg}

        except Exception as e:
            if not is_input_node_missing:
                reverse_engineering_status_update = ReverseEngineeringUpdate(
                    status=ReverseEngineeringStatus.LINKED_ERROR
                )
                self.reverse_controller.save_reverse_engineering(
                    data.get("name", "").replace("'", ""),
                    data.get("repository_id"),
                    reverse_engineering_status_update,
                    type=data.get("label"),
                )

            error_msg = f"Error creating graph: {str(e)}"
            logger.error(error_msg, error=str(e), data=data, exc_info=True)
            return {"status": "error", "message": error_msg}

    def _handle_wfl_nodes(
        self, repository_id, parser_output, source_node, existing_nodes, id_to_nodes
    ):
        """Handle WFL specific node processing"""
        if not parser_output:
            logger.error("No parser output for WFL file")
            return

        statements = parser_output.get("statements", [])
        logger.info(f"Processing WFL statements: {len(statements)}")
        for stmt in statements:
            if stmt.get("tag") == "RunStatement":
                file_path = stmt.get("file_path", "")
                if file_path:
                    program_id = file_path.split("/")[-1].replace("'", "")
                    target_node_key = (program_id, FileType.COBOL)
                    self._add_edge(
                        repository_id,
                        existing_nodes,
                        id_to_nodes,
                        source_node,
                        target_node_key,
                        RelationshipLabel.EXEC_PGM,
                        {
                            "full_path": file_path,
                            "label": RelationshipLabel.EXEC_PGM.value,
                        },
                    )
    @staticmethod
    def __query_label_by_name(name: str, repository_id: str):
        try:
            mongo_uri = f"mongodb://{os.getenv('MONGODB_USER')}:{os.getenv('MONGODB_PASSWORD')}@{os.getenv('MONGODB_HOST')}:{os.getenv('MONGODB_PORT')}/{os.getenv('MONGODB_DB_NAME')}?authSource=admin"
            client = MongoClient(mongo_uri)
            db = client.mainframe
            collection = db.reverse_engineering

            result = collection.find_one(
                {
                    "name": name,
                    "repository_id": ObjectId(repository_id),
                }
            )

            if result and result.get("type"):
                return result["type"]
            else:
                logger.error(f"No type found for {name}")
                return None

        except Exception as e:
            logger.error(f"Error querying label by name: {str(e)}")
            return None

    def _handle_jcl_nodes(
        self, repository_id, parser_output, source_node, existing_nodes, id_to_nodes
    ):
        """Handle JCL specific node processing"""
        if not parser_output:
            logger.error("No parser output for JCL file")
            return

        step_list = parser_output.get("step_list", [])
        for step_info in step_list:
            pgm = step_info.get("program_executed")
            if not pgm:
                continue
            pgm = pgm.replace("'", "")
            step_properties = self._extract_jcl_step_properties(step_info)
            label = (
                FileType.UTILITY if pgm in IBM_MAINFRAME_UTILITIES else FileType.COBOL
            )
            pgm_key = (pgm, label)
            self._add_edge(
                repository_id,
                existing_nodes,
                id_to_nodes,
                source_node,
                pgm_key,
                RelationshipLabel.EXEC_PGM,
                {"steps": [step_properties]},
            )
        exec_statement_map = parser_output.get("exec_statement_map", {})
        for exec_statement in exec_statement_map.values():
            if isinstance(exec_statement, dict):
                pgm = exec_statement.get("parameters_map", {}).get("PGM", None)
                if pgm == "IKJEFT01":
                    # Handle special case for IKJEFT01
                    code = exec_statement.get("code", {}).get("content")
                    pattern = r"RUN PROGRAM\((.*?)\)"
                    program_names = re.findall(pattern, code)
                    for program_name in program_names:
                        program_name = program_name.replace("'", "")
                        label = self.__query_label_by_name(program_name, repository_id)
                        if label:
                            target_node_key = (program_name, label)
                            self._add_edge(
                                repository_id,
                                existing_nodes,
                                id_to_nodes,
                                source_node,
                                target_node_key,
                                RelationshipLabel.EXEC_PGM_ULTITY,
                                {"label": RelationshipLabel.EXEC_PGM_ULTITY}
                            )

    def _handle_Panel_nodes(
        self,
        repository_id,
        parser_output,
        source_node,
        existing_nodes,
        id_to_nodes
    ):
        """Handle PANEL specific node processing"""
        if not parser_output:
            logger.error("No parser output for PANEL file")
            return
        assignStatement = []
        sections = parser_output["sections"]
        for section in sections:
            if section.get("tag") == "ProcSection":
                for statement in section.get("statements", []):
                    if statement.get("tag") == "AssignStatement":
                        assignStatement.append(statement)

        for statement in assignStatement:
            value = statement.get("value")
            if isinstance(value, dict):
                for trans_param in value.get("trans_params", []):
                    if trans_param.get("trans_return_type") == "CMD":
                        program_id = trans_param["trans_return_value"]
                        program_id = program_id.replace("'", "")
                        target_node_key = (program_id, FileType.CLIST)
                        self._add_edge(
                            repository_id,
                            existing_nodes,
                            id_to_nodes,
                            source_node,
                            target_node_key,
                            RelationshipLabel.COMMAND_EXEC,
                            {"label": RelationshipLabel.COMMAND_EXEC}
                        )

    def _handle_cobol_nodes(
        self,
        repository_id,
        parser_output,
        source_node,
        existing_nodes,
        id_to_nodes,
    ) -> List[DependencyGraphNode]:
        """
        Handle COBOL specific node processing.
        Returns a list of swapped source nodes (exists if EXEC CICS RECEIVE is encountered).
        """
        if not parser_output:
            logger.error("No parser output for COBOL file")
            return []

        all_copybooks = parser_output.get("copybook_list", [])
        called_program_list = parser_output.get("called_program_list", [])
        statements = parser_output.get("statements", [])
        io_files = parser_output.get("io_files", [])
        working_storage_variables = parser_output.get("working_storage_variables", [])

        working_storage_copybooks = VariableFlowUtils.get_working_storage_copybooks(
            all_copybooks, io_files
        )
        working_storage_copybooks_declarations = (
            self.__get_declarations_in_all_copybooks(
                repository_id, working_storage_copybooks
            )
        )
        expanded_working_storage_variables = (
            working_storage_variables + working_storage_copybooks_declarations
        )
        working_storage_var_name_to_var_dict = VariableFlowUtils.build_var_name_to_var_dict(
            expanded_working_storage_variables
        )
        exec_cics_statements, move_target_to_move_statements_dict = (
            self.__collect_move_and_exec_cics_statements(statements)
        )

        # Handle CALL
        self.__handle_call_edges(
            repository_id,
            source_node,
            existing_nodes,
            id_to_nodes,
            called_program_list,
            working_storage_var_name_to_var_dict,
            move_target_to_move_statements_dict,
        )

        # Handle COPY
        for copybook in all_copybooks:
            copybook_id = copybook.get("copybook_name").replace("'", "")
            target_node_key = GraphTask._find_node_key_for_copybooks(
                copybook_id, existing_nodes
            )
            self._add_edge(
                repository_id,
                existing_nodes,
                id_to_nodes,
                source_node,
                target_node_key,
                RelationshipLabel.HAS_COPYBOOK,
                {"label": RelationshipLabel.HAS_COPYBOOK},
            )

        # Handle EXEC CICS
        swapped_source_nodes = self.__handle_exec_cics_edges(
            repository_id,
            source_node,
            existing_nodes,
            id_to_nodes,
            exec_cics_statements,
            working_storage_var_name_to_var_dict,
            move_target_to_move_statements_dict,
        )

        return swapped_source_nodes

    def __handle_call_edges(
        self,
        repository_id,
        source_node,
        existing_nodes,
        id_to_nodes,
        called_program_list,
        working_storage_var_name_to_var_dict,
        move_target_to_move_statements_dict,
    ):
        for called_program in called_program_list:
            relationship_type = {
                "STATIC": RelationshipLabel.STATIC_CALL,
                "DYNAMIC": RelationshipLabel.DYNAMIC_CALL,
            }.get(called_program.get("call_type"))
            if not relationship_type:
                continue

            program_id = called_program.get("program_id")
            direct_program_name = self.__extract_program_name(program_id)
            program_names = (
                [direct_program_name]
                if direct_program_name
                else self.__find_program_names(
                    program_id,
                    called_program["line_number"],
                    move_target_to_move_statements_dict,
                    working_storage_var_name_to_var_dict,
                )
            )
            if not program_names:
                continue

            program_parameters = called_program.get("parameters", [])
            target_label = (
                FileType.UTILITY
                if program_id in IBM_MAINFRAME_UTILITIES
                else FileType.COBOL
            )

            for program_name in program_names:
                target_node_key = (program_name, target_label)
                self._add_edge(
                    repository_id,
                    existing_nodes,
                    id_to_nodes,
                    source_node,
                    target_node_key,
                    relationship_type,
                    {"parameters": program_parameters, "label": relationship_type},
                )

    def __handle_exec_cics_edges(
        self,
        repository_id,
        source_node,
        existing_nodes,
        id_to_nodes,
        exec_cics_statements,
        working_storage_var_name_to_var_dict,
        move_target_to_move_statements_dict,
    ) -> List[DependencyGraphNode]:
        """
        Processes EXEC CICS statements to establish edges in the dependency graph.
        If EXEC CICS RECEIVE is encountered, the source node may be swapped, and a reverse edge is created.
        Returns a list of swapped source nodes
        """
        # Track swapped source nodes for EXEC CICS RECEIVE
        swapped_source_node_key_set = set()  # use set to ensure uniqueness

        for statement in exec_cics_statements:
            program_value = self.__extract_program_value(statement)
            if not program_value:
                continue

            target_node_label = self.__get_program_node_label(statement)
            if not target_node_label:
                continue

            # Use direct program name or find program names through variable
            direct_program_name = self.__extract_program_name(program_value)
            program_names = (
                [direct_program_name]
                if direct_program_name
                else self.__find_program_names(
                    program_value,
                    statement["start_line"],
                    move_target_to_move_statements_dict,
                    working_storage_var_name_to_var_dict,
                )
            )

            if not program_names:
                continue

            edge_type = RelationshipLabel.EXEC_CICS

            for program_name in program_names:
                target_node_key = (program_name, target_node_label)

                if statement["commandName"] == "RECEIVE":
                    swapped_source_node = self.__add_reverse_edge(
                        repository_id,
                        existing_nodes,
                        id_to_nodes,
                        target=source_node,
                        source_key=target_node_key,
                        edge_type=edge_type,
                        edge_properties={"label": edge_type},
                    )
                    swapped_source_node_key_set.add(
                        (swapped_source_node.name, swapped_source_node.label)
                    )
                else:
                    self.__add_entry_flow_edge(
                        repository_id,
                        existing_nodes,
                        id_to_nodes,
                        source_node,
                        target_node_key,
                        edge_type,
                        {"label": edge_type},
                    )

        return [existing_nodes[key] for key in swapped_source_node_key_set]

    def __iterate_statements(self, possible_statements: list[dict]):
        """A generator that recursively yields all Move/ExecCICS statements (as dictionaries)"""
        for possible_statement in possible_statements:
            if isinstance(possible_statement, dict):
                if possible_statement.get("tag") in [
                    "MoveStatement",
                    "ExecCicsStatement2",
                ]:
                    yield possible_statement

                for _, value in possible_statement.items():
                    if isinstance(value, list):
                        yield from self.__iterate_statements(value)
                    elif isinstance(value, dict):
                        yield from self.__iterate_statements([value])

    def __collect_move_and_exec_cics_statements(
        self, statements: list[dict]
    ) -> tuple[list[dict], dict[str, dict]]:
        """
        Collect ExecCICS statements with SEND/RECEIVE/XCTL command name.
        Build dictionary to lookup Move statements by move target.
        """
        exec_cics_statements = []
        move_target_to_move_statements_dict = defaultdict(list)

        for statement in self.__iterate_statements(statements):
            if statement["tag"] == "ExecCicsStatement2":
                command_name = statement["commandName"]
                if command_name in ["XCTL", "SEND", "RECEIVE"]:
                    exec_cics_statements.append(statement)

            if statement["tag"] == "MoveStatement":
                for destination in statement["to_identifiers"]:
                    # Use destination directly (no suffix handling)
                    move_target_to_move_statements_dict[destination].append(statement)

        return (exec_cics_statements, move_target_to_move_statements_dict)

    def __get_declarations_in_all_copybooks(
        self, repository_id: str, copybooks: list[dict]
    ) -> list[dict]:
        """Merge all (name-replaced) variable declarations in all copybooks"""
        all_declarations = []
        for copybook in copybooks:
            declarations = VariableFlowUtils.get_copybook_variable_declarations(
                repository_id, copybook
            )
            VariableFlowUtils.process_redefine_occur(declarations)
            all_declarations.extend(declarations)
        return all_declarations

    def __extract_program_value(self, exec_cics_statement: dict) -> str:
        """Extract the program value based on ExecCICS statement's command name"""
        command_name = exec_cics_statement["commandName"]
        param_to_check = {"SEND": "MAPSET", "RECEIVE": "MAPSET", "XCTL": "PROGRAM"}

        param_name = param_to_check.get(command_name)
        if not param_name:
            return ""

        for param in exec_cics_statement["commandBody"]:
            if param["parameterName"] == param_name:
                return param["parameterValue"].strip()
        return ""

    def __extract_program_name(self, value: str) -> str:
        """Extracts a program name if it's wrapped in single quotes, by stripping the surrounding quotes and whitespace"""
        value = value.strip()
        if len(value) > 2 and value[0] == value[-1] == "'":
            return value[1:-1].strip()
        return ""

    def __get_program_node_label(self, exec_cics_statement: dict) -> FileType | None:
        command_name = exec_cics_statement["commandName"]
        command_to_node_type = {
            "SEND": FileType.BMS,
            "RECEIVE": FileType.BMS,
            "XCTL": FileType.COBOL,
        }
        return command_to_node_type.get(command_name)

    def __is_entry_point(self, node_label: FileType) -> bool:
        """
        Check if a node is a 'possible' entry point.
        (is_entry_point can be updated to False if being pointed to by another entry point)
        """
        return node_label in [FileType.BMS, FileType.JCL, FileType.WFL, FileType.PANEL]

    def __get_initial_group(self, node_name: str, is_entry_point: bool) -> set[str]:
        """Create initial group for the node"""
        return set([node_name]) if is_entry_point else set()

    def __find_program_names(
        self,
        program_value: str,
        max_line: int,  # start line of the current statement that uses the program variable
        move_target_to_move_statements_dict: dict[str, list[dict]],
        working_storage_var_name_to_var_dict: dict[str, dict],
    ) -> list[str]:
        """
        Find all possible program names saved by program_value variable in ExecCICS statement.
        There may be multiple valid paths that lead to program_value.
        """
        program_name_set: Set[str] = set()  # use a set to avoid duplicates

        # DFS move statements starting from program_value
        stack: List[Tuple[str, int]] = [
            (program_value, max_line)
        ]  # Track (variable name, max line)

        while stack:
            var_name, max_line = stack.pop()
            var_name = VariableFlowUtils.extract_main_var_name(var_name)

            var = working_storage_var_name_to_var_dict.get(var_name)
            if not var:
                continue

            # If this variable has default values -> record program name & stop exploring this path
            default_value_set = var.get(
                "default_value_set"
            )  # already stripped and exclude SPACE/SPACES
            default_value = var.get("default_value", "").strip()

            if default_value_set:
                # Handle array variable
                for value in default_value_set:
                    possible_program_name = self.__extract_program_name(value)
                    if possible_program_name:
                        program_name_set.add(possible_program_name)
                continue

            elif default_value and default_value not in DEFAULT_VALUES_TO_SKIP:
                # Handle normal variable
                possible_program_name = self.__extract_program_name(default_value)
                if possible_program_name:
                    program_name_set.add(possible_program_name)
                continue

            # If the variable has no default value, keep tracking through move statements
            move_statements = move_target_to_move_statements_dict.get(var_name, [])
            if not move_statements:
                continue

            for i in range(len(move_statements) - 1, -1, -1):
                statement = move_statements[i]
                statement_start_line = statement["start_line"]

                # Ensure the move statement is before current max line
                if statement_start_line >= max_line:
                    continue

                # If move from literal -> record program name & stop exploring this path
                if statement.get("from_literal"):
                    possible_program_name = self.__extract_program_name(
                        statement.get("from_literal")
                    )
                    if possible_program_name:
                        program_name_set.add(possible_program_name)

                    break  # also stop checking previous move statements to the same target
                    # TODO: Handle move statements to the same target on different branches of conditional statements
                    #       In that case we cannot simply break

                # Push the source variable (with updated max line) to the stack if it's a working storage variable
                source_var_name = statement.get("move_from")
                if source_var_name in working_storage_var_name_to_var_dict:
                    stack.append((source_var_name, statement_start_line))

        return list(program_name_set)
