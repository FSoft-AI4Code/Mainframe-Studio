from pathlib import Path
import re
from typing import Any, Dict, List, Optional, Tuple

from loguru import logger

from config.settings import settings
from controller.edge_controller import EdgeController
from controller.node_controller import DependencyGraphNode, FileType, NodeController, NodeStatus
from controller.reverse_controller import ReverseController
from parsers.grammar.common.base_cobol_schemas import FileControlEntry
from parsers.jcl_parser import ParsedJCLAntlr
from schema.dataset_assignment import JclDatasetAccessOperation, JclDatasetAssignment
from schema.reverse_engineering import ReverseEngineeringStatus


class JclDatasetAssignmentExtractor:
    """
    Analyzes JCL files to extract dataset information and determine how programs access these datasets.

    This class builds a dependency graph starting from a JCL file, traverses the call hierarchy
    of all programs referenced in the JCL, and identifies dataset access patterns across the entire
    application. It uses graph traversal algorithms to map relationships between JCL, programs,
    and datasets.

    The analyzer requires database controllers to query nodes, edges, and reverse engineering data
    from the system's dependency graph.

    Attributes:
        reverse_controller: Controller for querying reverse engineering data
        node_controller: Controller for querying node information from the dependency graph
        edge_controller: Controller for querying relationships between nodes
    """

    def __init__(
        self,
        reverse_controller: ReverseController,
        node_controller: NodeController,
        edge_controller: EdgeController,
    ):
        """
        Initialize the analyzer with database controllers.

        Args:
            reverse_controller: Controller for querying reverse engineering data
            node_controller: Controller for querying node information
            edge_controller: Controller for querying relationships between nodes
        """
        self.reverse_controller = reverse_controller
        self.node_controller = node_controller
        self.edge_controller = edge_controller
        self.JCL_KEYWORDS = self._load_jcl_keywords()

    def _load_jcl_keywords(self) -> set[str]:
        """
        Load JCL keywords from a file specified in settings.

        Args:
            settings: Configuration object with JCL_KEYWORDS_FILE attribute.

        Returns:
            A set of JCL keywords.
        """
        keywords = set()

        project_root = Path(__file__).resolve().parents[1]
        keywords_file = project_root / settings.JCL_KEYWORDS_FILE

        try:
            if keywords_file.exists():
                with keywords_file.open("r", encoding="utf-8") as f:
                    for line in f:
                        keyword = line.strip()
                        if keyword:
                            keywords.add(keyword)
                logger.debug(
                    f"Loaded {len(keywords)} JCL keywords from {keywords_file}"
                )
            else:
                logger.warning(
                    f"JCL keywords file not found at {keywords_file}. "
                    "Skipping JCL keyword filtering."
                )

            return keywords
        except Exception as e:
            logger.error(
                f"Failed to load JCL keywords from {keywords_file}: {str(e)}. "
                "Skipping JCL keyword filtering."
            )
            return keywords

    def extract_jcl_datasets(
        self, jcl_name: str, repository_id: str
    ) -> List[JclDatasetAssignment]:
        """
        Extract dataset information from a JCL file and analyze access patterns.

        This method performs the following steps:
        1. Locates the JCL node in the dependency graph
        2. Builds a complete call graph of all programs referenced by the JCL
        3. Retrieves reverse engineering data for all nodes in the call graph
        4. Extracts dataset definitions from the JCL
        5. Analyzes how each dataset is accessed throughout the program call hierarchy

        Args:
            jcl_name: Name of the JCL file to analyze
            repository_id: ID of the repository containing the artifacts

        Returns:
            List of JclDatasetAccessMapping objects representing datasets and their access patterns
        """
        jcl_node = self.node_controller.query_node(
            repository_id=repository_id, name=jcl_name, label="JCL"
        )

        if not jcl_node:
            logger.warning(f"JCL node not found for name '{jcl_name}', skipping")
            return []

        call_graph, node_id_to_node_map = self._extract_call_graph(
            jcl_node=jcl_node, repository_id=repository_id
        )

        # Build a map of node IDs to their reverse engineering data
        # This allows us to quickly access parsed data for any node in the call graph
        node_id_to_reverse_engineering_map = {}
        for _, node in node_id_to_node_map.items():
            reverse_engineering = (
                self.reverse_controller.query_reverse_engineering_full(
                    name=node.name, repository_id=repository_id, type_=node.label
                )
            )

            # If the reverse engineering data is not found, the node is missing
            # and we skip it
            # The reverse engineering is created after running classfier for every files in the repo
            # Therefore don't need to check the status of the node
            if not reverse_engineering:
                logger.warning(
                    f"Extracting datasets for {jcl_node.name}: Reverse engineering not found for node '{node.id}' '{node.name}' '{node.label}' '{node.status}'"
                )
                continue
            
            if reverse_engineering.get("status") == ReverseEngineeringStatus.PARSED_ERROR:
                logger.warning(
                    f"Skipping analyzing dataset assignment of node '{node.id}' with name '{node.name}' type '{node.label}' because of parsing error",
                )
                continue
            
            if reverse_engineering.get("status") == ReverseEngineeringStatus.LINKED_ERROR:
                logger.warning(
                    f"Skipping analyzing dataset assignment of node '{node.id}' with name '{node.name}' type '{node.label}' because the node is failed to be added to the call graph",
                )
                continue

            # After running the parser, the reverse engineering data is updated with the output
            # field containing the parsed data
            # If the output field is not present, it means the parsing is not done yet or failed (handled above)
            if not reverse_engineering.get("output"):
                raise ValueError(
                    f"Parsing is not done for node '{node.id}' with name '{node.name}' type '{node.label}'",
                    {
                        "error_type": "parsing_not_done",
                    },
                )

            node_id_to_reverse_engineering_map[node.id] = reverse_engineering.get(
                "output"
            )

        jcl_datasets = self._extract_datasets(
            jcl_node=jcl_node,
            call_graph=call_graph,
            node_id_to_node_map=node_id_to_node_map,
            node_id_to_reverse_engineering_map=node_id_to_reverse_engineering_map,
        )

        # Merge duplicated datasets with different access operations
        # This can happen when a dataset is used in multiple steps in JCL
        merged_datasets: Dict[str, JclDatasetAssignment] = {}
        for dataset in jcl_datasets:
            key = f"{dataset.repository_id}_{dataset.jcl_name}_{dataset.exec_program_id}_{dataset.dataset_name}"
            if key not in merged_datasets:
                merged_datasets[key] = dataset
            else:
                existing_ops = {
                    (op.open_by_program_id, op.open_mode)
                    for op in merged_datasets[key].access_operations
                }

                access_operations_merge = merged_datasets[key].access_operations.copy()

                for op in dataset.access_operations:
                    op_key = (op.open_by_program_id, op.open_mode)
                    if op_key not in existing_ops:
                        access_operations_merge.append(op)
                        existing_ops.add(op_key)

                merged_datasets[key].access_operations = access_operations_merge

        jcl_datasets = list(merged_datasets.values())

        return jcl_datasets

    def _extract_datasets(
        self,
        jcl_node: DependencyGraphNode,
        call_graph: Dict[str, List[str]],
        node_id_to_node_map: Dict[str, DependencyGraphNode],
        node_id_to_reverse_engineering_map: Dict[str, Any],
    ) -> List[JclDatasetAssignment]:
        """
        Process JCL datasets and build access mapping objects.

        Takes the parsed JCL data and analyzes how each dataset is accessed by
        traversing the call graph of all relevant programs.

        Args:
            jcl_node: The JCL node being analyzed
            call_graph: Dictionary mapping node IDs to lists of called node IDs
            node_id_to_node_map: Dictionary mapping node IDs to node objects
            node_id_to_reverse_engineering_map: Dictionary mapping node IDs to reverse engineering data

        Returns:
            List of JclDatasetAccessMapping objects representing datasets and their access patterns
        """
        jcl_reverse_engineering = node_id_to_reverse_engineering_map[jcl_node.id]
        jcl_parsed_data = ParsedJCLAntlr(**jcl_reverse_engineering)

        dataset_mappings = []

        # Process each dataset defined in the JCL
        # For each one, we'll find all programs that might access it throughout the call hierarchy
        for dataset in jcl_parsed_data.dataset_list:
            exec_program_name = dataset.get("program_id", "")
            exec_program_node = None
            for node in node_id_to_node_map.values():
                if node.name == exec_program_name:
                    exec_program_node = node
                    break
            
            # The node_id_to_node_map only contains JCL and COBOL nodes
            if exec_program_node is None:
                continue
            
            ddname = dataset.get("variable_name", "")

            if ddname in self.JCL_KEYWORDS:
                continue

            access_operations = self._extract_dataset_access_operations(
                ddname,
                exec_program_name,
                call_graph,
                node_id_to_node_map,
                node_id_to_reverse_engineering_map,
            )

            dataset_type = self._get_dataset_type(
                ddname,
                exec_program_name,
                call_graph,
                node_id_to_node_map,
                node_id_to_reverse_engineering_map,
            )
            
            if dataset_type in ("FLAT", "OTHER"):
                gdg_pattern = r"\([+-]?\d+\)$"
                if re.search(gdg_pattern, dataset.get("dataset_name", "")):
                    dataset_type = "GDG"

            dataset_mapping = JclDatasetAssignment(
                job=jcl_parsed_data.job,
                step=dataset.get("step", ""),
                repository_id=jcl_node.repository_id,
                jcl_name=jcl_node.name,
                exec_program_id=exec_program_name,
                dataset_name=dataset.get("dataset_name", ""),
                ddname=ddname,
                access_operations=access_operations,
                dataset_type=dataset_type,
            )

            dataset_mappings.append(dataset_mapping)

        return dataset_mappings

    def _extract_dataset_access_operations(
        self,
        ddname: str,
        program_name: str,
        call_graph: Dict[str, List[str]],
        node_id_to_node_map: Dict[str, DependencyGraphNode],
        node_id_to_reverse_engineering_map: Dict[str, Any],
    ) -> List[JclDatasetAccessOperation]:
        """
        Identify all programs that access a specific dataset and their access modes.

        Finds the starting program node and performs a depth-first search through
        the call graph to identify all programs that might access the dataset.

        Args:
            ddname: The DD name of the dataset to analyze
            program_name: The name of the program specified in the JCL EXEC statement
            call_graph: Dictionary mapping node IDs to lists of called node IDs
            node_id_to_node_map: Dictionary mapping node IDs to node objects
            node_id_to_reverse_engineering_map: Dictionary mapping node IDs to reverse engineering data

        Returns:
            List of JclDatasetOpenMode objects representing how programs access the dataset
        """
        program_node = None
        for node_id, node in node_id_to_node_map.items():
            if node.name == program_name:
                program_node = node

        if program_node is None:
            return []

        access_operations = []

        self._dfs_access_operations(
            ddname,
            program_node.id,
            call_graph,
            node_id_to_reverse_engineering_map,
            node_id_to_node_map=node_id_to_node_map,
            access_operations=access_operations,
        )

        return access_operations

    def _get_dataset_type(
        self,
        ddname: str,
        program_name: str,
        call_graph: Dict[str, List[str]],
        node_id_to_node_map: Dict[str, DependencyGraphNode],
        node_id_to_reverse_engineering_map: Dict[str, Any],
    ) -> str:
        """
        Determine the type of dataset (VSAM or FLAT) based on the program's reverse engineering data.

        Args:
            ddname: The DD name of the dataset to analyze
            program_name: The name of the program specified in the JCL EXEC statement
            call_graph: Dictionary mapping node IDs to lists of called node IDs for traversal
            node_id_to_node_map: Dictionary mapping node IDs to node objects
            node_id_to_reverse_engineering_map: Dictionary mapping node IDs to reverse engineering data

        Returns:
            The type of dataset
        """
        program_node = None
        for node_id, node in node_id_to_node_map.items():
            if node.name == program_name:
                program_node = node

        # We have already validated the program node existence in the call graph
        # The node_id_to_node_map only contains the COBOL and JCL nodes
        # If the program node is not found, it must be a UTILITY file
        # We currently don't support UTILITY files
        if program_node is None:
            return None

        reverse_engineering = node_id_to_reverse_engineering_map.get(program_node.id)

        # If the reverse engineering data is not found, it means the the file is MISSING
        if reverse_engineering is None:
            return "OTHER"

        file_control_list = reverse_engineering.get("file_control_list", None)

        if file_control_list is None:
            raise ValueError(
                f"Parse data of '{program_node.name}' type '{program_node.label}' is missing file_control_list",
            )

        dataset_type = self._dfs_dataset_type(
            ddname,
            program_node.id,
            call_graph,
            node_id_to_reverse_engineering_map,
            node_id_to_node_map,
        )
        
        if dataset_type is None:
            return "OTHER"

        return dataset_type

    def _dfs_dataset_type(
        self,
        ddname: str,
        node_id: str,
        call_graph: Dict[str, List[str]],
        node_id_to_reverse_engineering_map: Dict[str, Any],
        node_id_to_node_map: Dict[str, DependencyGraphNode],
    ) -> Optional[str]:
        """
        Recursively traverse the call graph to find the dataset type.

        Args:
            ddname: The DD name of the dataset being analyzed
            node_id: ID of the current program node being checked
            call_graph: Dictionary mapping node IDs to lists of called node IDs
            node_id_to_reverse_engineering_map: Dictionary mapping node IDs to reverse engineering data
            node_id_to_node_map: Dictionary mapping node IDs to node objects

        Returns:
            The type of dataset (VSAM or FLAT) if found, otherwise OTHER
        """
        node = node_id_to_node_map.get(node_id)
        if node is None:
            raise ValueError(f"Unexpected missing node with id '{node_id}'")

        reverse_engineering = node_id_to_reverse_engineering_map.get(node_id)

        # If the reverse engineering data is not found, it means the the file is MISSING
        if reverse_engineering is None:
            return None

        file_control_list = reverse_engineering.get("file_control_list", None)

        if file_control_list is None:  # None is different from empty list
            raise ValueError(
                f"Parse data of '{node.name}' type '{node.label}' is missing file_control_list",
            )

        file_control_list = [
            FileControlEntry(**file_control) for file_control in file_control_list
        ]
        program_name = reverse_engineering.get("program_id", None)

        if program_name is None:
            raise ValueError(
                f"Parse data of '{node.name}' is missing program_id",
            )

        for file_control in file_control_list:
            if file_control.assignment_name == ddname:
                return file_control.dataset_type

        # If the dataset is not found in the current node, check the called programs
        for called_program_id in call_graph.get(node_id, []):
            node = node_id_to_node_map.get(called_program_id)
            if node is None:
                raise ValueError(
                    f"Unexpected missing called program node id {called_program_id}"
                )

            if node.status == NodeStatus.MISSING:
                continue

            dataset_type = self._dfs_dataset_type(
                ddname,
                called_program_id,
                call_graph,
                node_id_to_reverse_engineering_map,
                node_id_to_node_map,
            )

            if dataset_type:
                return dataset_type

    def _dfs_access_operations(
        self,
        ddname: str,
        node_id: str,
        call_graph: Dict[str, List[str]],
        node_id_to_reverse_engineering_map: Dict[str, Any],
        node_id_to_node_map: Dict[str, DependencyGraphNode],
        access_operations: List[JclDatasetAccessOperation],
    ):
        """
        Recursively traverse the call graph to find all dataset access operations.

        For each program in the call hierarchy, checks if it accesses the specified
        dataset and adds the access mode to the results. Then recursively checks
        all programs called by this program.

        Args:
            ddname: The DD name of the dataset being analyzed
            node_id: ID of the current program node being checked
            call_graph: Dictionary mapping node IDs to lists of called node IDs
            node_id_to_reverse_engineering_map: Dictionary mapping node IDs to reverse engineering data
            access_operations: List to accumulate dataset access operations
        """
        # We have checked for missing nodes in the call graph traversal previously
        node = node_id_to_node_map.get(node_id)
        if node is None:
            raise ValueError(f"Unexpected missing node with id '{node_id}'")

        reverse_engineering = node_id_to_reverse_engineering_map.get(node_id)
        # If the reverse engineering data is not found, it means the the file is MISSING
        if reverse_engineering is None:
            return None

        file_control_list = reverse_engineering.get("file_control_list", None)

        if file_control_list is None:  # None is different from empty list
            raise ValueError(
                f"Parse data of '{node.name}' type '{node.label}' is missing file_control_list",
            )

        file_control_list = [
            FileControlEntry(**file_control) for file_control in file_control_list
        ]
        program_name = reverse_engineering.get("program_id", None)

        if program_name is None:
            raise ValueError(
                f"Parse data of '{node.name}' is missing program_id",
            )

        open_type = self._get_open_type(file_control_list, ddname)

        if open_type:
            access_operations.append(
                JclDatasetAccessOperation(
                    open_by_program_id=program_name, open_mode=open_type
                )
            )

        for called_program_id in call_graph.get(node_id, []):
            node = node_id_to_node_map.get(called_program_id)
            if node is None:
                raise ValueError(
                    f"Unexpected missing called program node id {called_program_id}"
                )

            if node.status == NodeStatus.MISSING:
                continue

            self._dfs_access_operations(
                ddname,
                called_program_id,
                call_graph,
                node_id_to_reverse_engineering_map,
                node_id_to_node_map,
                access_operations,
            )

    def _extract_call_graph(
        self, jcl_node: DependencyGraphNode, repository_id: str
    ) -> Tuple[Dict[str, List[str]], Dict[str, DependencyGraphNode]]:
        """
        Build a complete call graph starting from a JCL file.

        Creates a directed graph where nodes are programs and edges represent
        program calls or execution relationships. The graph includes the JCL file
        itself and all programs directly or indirectly called.

        Args:
            jcl_node: The JCL node to start the graph traversal from
            repository_id: ID of the repository containing the artifacts

        Returns:
            A tuple containing:
            - call_graph: Dictionary mapping node IDs to lists of called node IDs
            - node_id_to_node_map: Dictionary mapping node IDs to node objects
        """
        call_graph: Dict[str, List[str]] = {}
        node_id_to_node_map = {jcl_node.id: jcl_node}

        self._dfs_call_graph(jcl_node.id, call_graph, node_id_to_node_map)

        return call_graph, node_id_to_node_map

    def _dfs_call_graph(
        self,
        current_node_id: str,
        call_graph: Dict[str, List[str]],
        node_id_to_node_map: Dict[str, DependencyGraphNode],
    ):
        """
        Perform depth-first search traversal to build the call graph.

        For each node, finds all outgoing EXEC_PGM, STATIC_CALL, and DYNAMIC_CALL
        edges whose target is a COBOL node, adds the target nodes to the graph, and recursively processes those
        target nodes if they haven't been processed already.

        Args:
            current_node_id: ID of the current node being processed
            call_graph: Dictionary to populate with the call graph
            node_id_to_node_map: Dictionary to populate with node objects
        """
        outgoing_edges = self.edge_controller.query_outgoing_edges(
            source_id=current_node_id,
            edge_type=["EXEC_PGM", "STATIC_CALL", "DYNAMIC_CALL"],
        )

        target_node_ids = [str(edge["target"]) for edge in outgoing_edges]
        target_node_ids = list(set(target_node_ids))

        for target_node_id in target_node_ids:
            if target_node_id not in node_id_to_node_map:
                target_node = self.node_controller.query_node_by_id(
                    node_id=target_node_id
                )

                if not target_node:
                    raise ValueError(
                        f"Missing target node with ID '{target_node_id}' in call graph",
                        {
                            "error_type": "parse_graph_not_done",
                        },
                    )

                # EXEC_PGM relationship can be used for UTILITY files
                # We only want to keep COBOL programs
                if target_node.label != FileType.COBOL:
                    continue
                
                node_id_to_node_map[target_node_id] = target_node

        call_graph[current_node_id] = target_node_ids

        for target_node_id in target_node_ids:
            if target_node_id not in call_graph:
                self._dfs_call_graph(target_node_id, call_graph, node_id_to_node_map)

    def _get_called_programs(self, parsed_exec_program: dict) -> List[str]:
        """
        Extract the list of programs directly called by a program.

        Parses the called_program_list from the parsed program data and returns
        a deduplicated list of program IDs.

        Args:
            parsed_exec_program: Parsed data for a COBOL program

        Returns:
            List of unique program IDs that are called by this program
        """
        if parsed_exec_program is None:
            return []

        called_programs = parsed_exec_program.get("called_program_list", [])

        called_programs = [
            called_program["program_id"].replace("'", "")
            for called_program in called_programs
        ]

        called_programs = list(set(called_programs))

        return called_programs

    def _get_open_type(
        self, file_control_list: List[FileControlEntry], file_name: str
    ) -> Optional[str]:
        """
        Determines how a file is accessed based on file control entries.

        Searches through file control entries to find the specified file and
        returns its access mode.

        Args:
            file_control_list: List of file control entries from COBOL program
            file_name: The name of the file to find

        Returns:
            The open type (INPUT, OUTPUT, I-O, etc.) if found, None otherwise
        """
        for file_control in file_control_list:
            if file_control.assignment_name == file_name:
                return file_control.open_type
        return None
