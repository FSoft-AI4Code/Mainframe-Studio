from typing import Dict, List, Optional, Set, Generator, Any, TypedDict
from dataclasses import dataclass
from collections import deque, defaultdict

from parsers.grammar.common.base_cobol_schemas import Statement

DEFAULT_SECTION_NAME = 'default_section'
DEFAULT_PARAGRAPH_NAME = 'default_paragraph'
SECTION_ENTRY_PARAGRAPH_NAME = 'section_entry'

def iterate_statements(possible_statements) -> Generator[Statement, None, None]:
    """
    A generator that recursively yields all COBOL Statement objects.
    (exhausts all levels of nesting).
    """
    for possible_statement in possible_statements:
        if isinstance(possible_statement, Statement):
            yield possible_statement

        if hasattr(possible_statement, '__dict__'):
            # Get all attributes that might contain nested statements
            for attr_name, attr_value in possible_statement.__dict__.items():
                # Skip private attributes
                if attr_name.startswith("_"):  
                    continue
                
                # Handle list of possible statements
                if isinstance(attr_value, list):
                    yield from iterate_statements(attr_value)
                
                # Handle nested pydantic models or custom objects that may contain statements
                elif hasattr(attr_value, '__dict__'):
                    yield from iterate_statements([attr_value])

class DocumentOrganizer:
    def __init__(self):
        self.structure = {}

    def add_statement(self, statement):
        section = getattr(statement, 'section', None) or DEFAULT_SECTION_NAME 
        paragraph = getattr(statement, 'paragraph', None) or DEFAULT_PARAGRAPH_NAME

        if section not in self.structure:
            self.structure[section] = {}
        
        if paragraph not in self.structure[section]:
            self.structure[section][paragraph] = []
        
        self.structure[section][paragraph].append(statement)

    def get_structure(self):
        return self.structure

def organize_statements(statements):
    organizer = DocumentOrganizer()
    
    for statement in statements:
        organizer.add_statement(statement)
    
    return organizer.get_structure()

@dataclass
class Node:
    id: str
    type: str = "paragraph"
    name: str = ""  # Name of the paragraph/subroutine
    section: str = ""  # Section containing this node

class NodeType:
    PROGRAM = "program"
    SUBROUTINE = "subroutine"
    PARAGRAPH = "paragraph"

class EdgeType:
    SEQUENCE = "sequence"
    PERFORM_SECTION = "perform_section"
    RETURN = "return"
    GOTO = "goto"
    CALL = "call"
    ALTER = "alter"
    PERFORM = "perform"
    THRU_PERFORM = "thru_perform"
    IMPLICIT_PERFORM = "implicit_perform"

class RawNode(TypedDict):
    id: str
    type: str 
    name: str 
    section: str

class Edge(TypedDict):
    source: str
    target: str
    type: str

class GraphData(TypedDict):
    nodes: List[RawNode]
    edges: List[Edge]

class TreeNode(TypedDict):
    id: str
    type: str 
    name: str 
    section: str
    label: str
    level: int
    children: List["TreeNode"]

class CallGraph:
    def __init__(self):
        self.nodes: Dict[str, Dict[str, Any]] = {}
        
    def add_node(self, node_id: str, node_type: str = NodeType.PARAGRAPH, name: str = "", section: str = "") -> None:
        if node_id not in self.nodes:
            self.nodes[node_id] = {
                "type": node_type,
                "name": name,
                "section": section,
                "edges": []
            }
            
    def add_edge(self, source: str, target: str, edge_type: str) -> None:
        edge = {"target": target, "type": edge_type}
        if edge not in self.nodes[source]["edges"]:
            self.nodes[source]["edges"].append(edge)
            
    def get_edges(self, node_id: str) -> List[Dict[str, str]]:
        return self.nodes[node_id]["edges"]
        
    def get_node_type(self, node_id: str) -> str:
        return self.nodes[node_id]["type"]
        
    def get_node_name(self, node_id: str) -> str:
        return self.nodes[node_id]["name"]
        
    def get_node_section(self, node_id: str) -> str:
        return self.nodes[node_id]["section"]


class ExecutionFlowBuilder:
    def __init__(self, organized_statements: Dict[str, Dict[str, List[Statement]]], program_id: str):
        self._program_id = program_id
        self.organized_statements = organized_statements
        self.call_graph = CallGraph()
        self.section_paragraphs = {}  # Added to track paragraphs in sequential order by section
        self.sections = set(self.organized_statements.keys())  # Track all section names
        self._single_exit_paragraph_set: Set[str] = set() # Track paragraphs (node ids) that contain a single EXIT statement 
        
        # IMPORTANT!!!:
        # These missing paragraphs are analyzed locally in the file, the paragraphs may be defined in COPYBOOK
        self.missing_paragraphs: List[Dict[str, str]] = []  # 
        
    def build(self) -> Dict[str, Any]:
        """Build full execution flow graph"""
        self._initialize_nodes()
        self._build_section_paragraph_order()  # Build paragraph order
        self._process_all_statements()
        exec_paths = self._find_execution_paths()
        self.__prune_single_exit_paragraphs(exec_paths)
        return self._convert_to_graph(exec_paths)

    def build_tree(self, data: GraphData) -> Optional[TreeNode]:
        """Build the execution flow tree from the given graph data (nodes and edges)"""
        node_dict: Dict[str, TreeNode] = {}
        child_node_id_set: Set[str] = set()
        seen: Set[str] = set()

        # Create tree nodes from raw nodes
        for node in data["nodes"]:
            node_id = node["id"]
            if node_id in seen:
                continue
            seen.add(node_id)

            node_dict[node_id] = TreeNode(
                **node,
                label=self.__get_node_label(node),
                level=0,
                children=[]
            )

        # Populate children property for tree nodes from edges info
        for edge in data["edges"]:
            source_node_id = edge["source"]
            target_node_id = edge["target"]
            source_node = node_dict.get(source_node_id)
            target_node = node_dict.get(target_node_id)

            if source_node and target_node:
                if edge["type"] == EdgeType.SEQUENCE:
                    continue
                source_node["children"].append(target_node)
                child_node_id_set.add(target_node_id)

        # Identify root node
        root_id = next((node["id"] for node in data["nodes"] if node["id"] not in child_node_id_set), None)
        if root_id:
            root = node_dict[root_id]
            root["label"] = self._program_id
            root["type"] = NodeType.PROGRAM
            root = self.__assign_levels(root)
            return root

        return None
    
    def __get_node_label(self, node: RawNode) -> str:
        """Produce node label for displaying purposes"""
        node_id = node["id"]
        if "." not in node_id:
            return node_id

        section, paragraph = node_id.split(".")
        if section == DEFAULT_SECTION_NAME and paragraph == DEFAULT_PARAGRAPH_NAME:
            return self._program_id
        if section == DEFAULT_SECTION_NAME:
            return paragraph
        if paragraph in [DEFAULT_PARAGRAPH_NAME, SECTION_ENTRY_PARAGRAPH_NAME]:
            return section
        return node_id
    
    def __assign_levels(self, node: TreeNode, level: int = 0, visited: Dict[str, Dict[int, TreeNode]] = {}) -> TreeNode:
        """Recursively assign level to all nodes. Allow different levels for the same node on different branches"""
        node_id = node["id"]
        if node_id not in visited:
            visited[node_id] = {}

        # Reuse the instance at the same level
        if level in visited[node_id]:
            return visited[node_id][level]
        
        # Clone if the node appeared at a new level
        cloned_node = TreeNode(
            id=node["id"],
            type=node["type"],
            name=node["name"],
            section=node["section"],
            label=node["label"],
            level=level,
            children=[] # rebuild because we may need to clone the children
        )
        # Store the node instance for the new level
        visited[node_id][level] = cloned_node

        # Assign levels to children recursively
        new_children = []
        for child in node["children"]:
            new_child = self.__assign_levels(child, level + 1, visited)
            new_children.append(new_child)

        cloned_node["children"] = new_children
        return cloned_node

    def _make_node_id(self, section: str, paragraph: str) -> str:
        """Create node identifier from section and paragraph"""
        return f"{section}.{paragraph}" if section else f"{DEFAULT_SECTION_NAME}.{paragraph}"
        
    def _resolve_node_id(self, target: str) -> str:
        # Check if target is an entire section
        if target in self.sections:
            # For a section, we return its first paragraph or create a special node
            if target in self.section_paragraphs and self.section_paragraphs[target]:
                # Return first paragraph in the section
                return self._make_node_id(target, self.section_paragraphs[target][0])
            else:
                # Create a special section node if there are no paragraphs
                return f"{target}.{SECTION_ENTRY_PARAGRAPH_NAME}"
                
        # First check if it's already a fully qualified name (section.paragraph)
        if "." in target and target in self.call_graph.nodes:
            return target
            
        # If it's already a node ID, return it
        if target in self.call_graph.nodes:
            return target

        # Check if it's a paragraph in any section
        for section in self.organized_statements:
            if target in self.organized_statements[section]:
                section_prefix = f"{section}." if section else f"{DEFAULT_SECTION_NAME}."
                return f"{section_prefix}{target}"
                
        # Default to the default section
        return f"{DEFAULT_SECTION_NAME}.{target}"
        
    def _initialize_nodes(self) -> None:
        """Initialize graph nodes from organized statements"""
        for section, paragraphs in self.organized_statements.items():
            # If section has no paragraphs, create a special section entry node
            if not paragraphs:
                node_id = f"{section}.{SECTION_ENTRY_PARAGRAPH_NAME}"
                self.call_graph.add_node(
                    node_id=node_id,
                    node_type="section",
                    name=f"{section}_entry",
                    section=section
                )
                
            for paragraph in paragraphs:
                node_id = self._make_node_id(section, paragraph)
                self.call_graph.add_node(
                    node_id=node_id,
                    node_type=NodeType.PARAGRAPH, 
                    name=paragraph,
                    section=section if section else DEFAULT_SECTION_NAME
                )

    def _build_section_paragraph_order(self) -> None:
        """Build ordered list of paragraphs by section"""
        for section, paragraphs in self.organized_statements.items():
            self.section_paragraphs[section] = list(paragraphs.keys())
                
    def _process_all_statements(self) -> None:
        """Process all statements to build edges, including fall-through execution"""
        for section, paragraphs in self.organized_statements.items():
            prev_paragraph_name = None  # Track previous paragraph within a section

            for paragraph_name, statements in paragraphs.items():
                current_node_id = self._make_node_id(section, paragraph_name)
                self._process_statements(statements, current_node_id)

                # Check fall-through execution (implicit perform)
                if prev_paragraph_name == DEFAULT_PARAGRAPH_NAME and not self._has_prevent_fallthrough_statement(paragraphs[prev_paragraph_name]):
                    prev_node_id = self._make_node_id(section, prev_paragraph_name)
                    self.call_graph.add_edge(prev_node_id, current_node_id, EdgeType.IMPLICIT_PERFORM)

                prev_paragraph_name = paragraph_name 

    def _has_prevent_fallthrough_statement(self, statements: List[Statement]) -> bool:
        """Check if there are any statement that prevents fall-through execution"""
        for stmt in iterate_statements(statements):
            if stmt.tag in {"StopStatement", "GoToStatement"}:
                return True 
        return False
                
    def _process_statements(self, statements: List[Statement], current_node: str) -> None:
        """Process statements to add edges to graph"""
        # Record paragraph with a single Exit statement to prune them later
        if len(statements) == 1 and statements[0].tag == "ExitStatement":
            self._single_exit_paragraph_set.add(current_node)
            return 

        for stmt in iterate_statements(statements):
            self._handle_statement(stmt, current_node)

    def __prune_single_exit_paragraphs(self, exec_paths: List[List[RawNode]]):
        """
        Remove the edges to paragraphs with a single Exit statement. 
        Run after building the full execution paths.
        """
        for path in exec_paths:
            # Check the last node in each path
            if path[-1]["id"] in self._single_exit_paragraph_set:
                path.pop()
                
    def _handle_statement(self, stmt: Statement, current_node: str) -> None:
        """Handle different statement types"""
        if stmt.tag == "StopStatement":
            # Stop statement terminates the paragraph - remove any outgoing edges
            self.call_graph.nodes[current_node]["edges"] = []
            return
            
        handlers = {
            "PerformStatement": self._handle_perform,
            "GoToStatement": self._handle_goto,
            "CallStatement": self._handle_call,
            "AlterStatement": self._handle_alter  # Add handler for ALTER statement
        }
        
        handler = handlers.get(stmt.tag)
        if handler:
            handler(stmt, current_node)
            
    def _handle_perform(self, stmt: Statement, current_node: str) -> None:
        """Handle PERFORM statement"""
        proc1 = getattr(stmt, 'procedure_name_1', None)
        proc2 = getattr(stmt, 'procedure_name_2', None)
        sub_tags = getattr(stmt, 'sub_tags', [])
        
        if proc1:
            # Check if proc1 is a section name
            if proc1 in self.sections:
                self._handle_perform_section(current_node, proc1)
            else:
                self._add_perform_edge(current_node, proc1)
            
                if "THRU" in sub_tags and proc2:
                    self._handle_perform_thru(current_node, proc1, proc2)

    def _handle_perform_section(self, current_node: str, section: str) -> None:
        """Handle PERFORM of an entire section"""
        # If section has paragraphs, we perform all paragraphs in order
        if section in self.section_paragraphs and self.section_paragraphs[section]:
            # Get the first paragraph of the section
            first_para = self.section_paragraphs[section][0]
            first_node = self._make_node_id(section, first_para)
            
            # Add perform edge to first paragraph
            self.call_graph.add_edge(current_node, first_node, EdgeType.PERFORM_SECTION)
            
            # Get the last paragraph of the section
            last_para = self.section_paragraphs[section][-1]
            last_node = self._make_node_id(section, last_para)
            
            # Add return edge from last paragraph back to current node
            # self.call_graph.add_edge(last_node, current_node, EdgeType.RETURN)
        else:
            # Section has no paragraphs, use special section entry node
            section_node = f"{section}.{SECTION_ENTRY_PARAGRAPH_NAME}"
            
            # Create node if it doesn't exist
            if section_node not in self.call_graph.nodes:
                self.call_graph.add_node(
                    node_id=section_node,
                    node_type="section",
                    name=f"{section}_entry",
                    section=section
                )
                
            # Add perform edge to section entry node
            self.call_graph.add_edge(current_node, section_node, EdgeType.PERFORM_SECTION)
            
            # Add return edge from section node back to current node
            # self.call_graph.add_edge(section_node, current_node, EdgeType.RETURN)
    
    def _handle_goto(self, stmt: Statement, current_node: str) -> None:
        """Handle GOTO statement"""
        if hasattr(stmt, 'procedure_name_1'):
            target_node = self._resolve_node_id(stmt.procedure_name_1)
            self.call_graph.add_edge(current_node, target_node, EdgeType.GOTO)
            
    def _handle_call(self, stmt: Statement, current_node: str) -> None:
        """Handle CALL statement"""
        if hasattr(stmt, 'call_literal') and stmt.call_literal:
            program = stmt.call_literal.strip('"').strip("'")
            self.call_graph.add_node(
                node_id=program,
                node_type=NodeType.SUBROUTINE,
                name=program,
                section=""
            )
            self.call_graph.add_edge(current_node, program, EdgeType.CALL)

    def _handle_alter(self, stmt: Statement, current_node: str) -> None:
        """Handle ALTER statement"""
        if hasattr(stmt, 'alterProceedTo'):
            for alter_proc in stmt.alterProceedTo:
                source_para = alter_proc.procedure_name_1
                target_para = alter_proc.procedure_name_2
                
                source_node = self._resolve_node_id(source_para)
                target_node = self._resolve_node_id(target_para)
                
                # Record the ALTER as an edge in the graph
                self.call_graph.add_edge(source_node, target_node, EdgeType.ALTER)

    def _add_perform_edge(self, source: str, target: str) -> None:
        """Add PERFORM edge between nodes"""
        target_node = self._resolve_node_id(target)
        self.call_graph.add_edge(source, target_node, EdgeType.PERFORM)

    def _handle_perform_thru(self, current_node: str, start_proc: str, end_proc: str) -> None:
        """Handle PERFORM THRU statement by adding edges between procedures"""
        start_node = self._resolve_node_id(start_proc)
        end_node = self._resolve_node_id(end_proc)
        
        # Find the section containing both procedures
        start_section = ""
        end_section = ""
        
        # Extract section names from node IDs
        if "." in start_node:
            start_section = start_node.split(".")[0]
        if "." in end_node:
            end_section = end_node.split(".")[0]
        
        # If they're in the same section, connect them with thru_perform edges
        if start_section == end_section and start_section in self.section_paragraphs:
            paragraphs = self.section_paragraphs[start_section]
            
            # Get paragraph names from node IDs
            start_para = start_node.split(".")[-1] if "." in start_node else start_node
            end_para = end_node.split(".")[-1] if "." in end_node else end_node
            
            if start_para in paragraphs and end_para in paragraphs:
                start_idx = paragraphs.index(start_para)
                end_idx = paragraphs.index(end_para)
                
                # Connect all paragraphs in between with thru_perform edges
                for i in range(start_idx, end_idx):
                    curr_para = paragraphs[i]
                    next_para = paragraphs[i + 1]
                    
                    curr_node = self._make_node_id(start_section, curr_para)
                    next_node = self._make_node_id(start_section, next_para)
                    
                    self.call_graph.add_edge(curr_node, next_node, EdgeType.THRU_PERFORM)

    def _find_execution_paths(self, entry_nodes: Optional[List[str]] = None) -> List[List[Dict]]:
        """Find all execution paths through the graph"""
        if not entry_nodes:
            entry_nodes = list(self.call_graph.nodes.keys())[:1]

        all_paths = []
        for entry in entry_nodes:
            if entry in self.call_graph.nodes:
                for path in self._dfs_paths(entry):
                    all_paths.append(path)
        return all_paths
        
    def _dfs_paths(
        self, 
        start_node: str,
        path: List[Dict] = None,
        visited: Set[str] = None,
        max_depth: int = 100
    ) -> Generator[List[Dict], None, None]:
        """DFS to find all paths from start_node"""
        if path is None:
            path = []
        if visited is None:
            visited = set()
            
        if len(path) > max_depth or start_node in visited:
            return
            
        # Resolve node id before processing
        start_node = self._resolve_node_id(start_node)
        
        if start_node not in self.call_graph.nodes:
            node_name = start_node.split(".")[-1]
            self.missing_paragraphs.append(
                {
                    "id": node_name,
                    "type": "paragraph",
                    "name": node_name,
                    "section": ""
                }
            )
            return
        current_node = {
            "id": start_node,
            "type": self.call_graph.get_node_type(start_node),
            "name": self.call_graph.get_node_name(start_node),
            "section": self.call_graph.get_node_section(start_node)
        }
        
        # Create a new path and visited set for this branch
        new_path = path.copy()
        new_visited = visited.copy()
        
        # Add to current path and mark as visited for this path
        new_path.append(current_node)
        new_visited.add(start_node)
        
        # Yield the current path - do this for EVERY node we visit, not just leaf nodes
        yield new_path.copy()
        
        # Get all outgoing edges
        edges = self.call_graph.get_edges(start_node)
        
        # For each outgoing edge, continue DFS
        for edge in edges:
            target_node = self._resolve_node_id(edge["target"])
            # Each recursive call gets its own copy of the path and visited set
            yield from self._dfs_paths(target_node, new_path.copy(), new_visited.copy(), max_depth)
    
    def _convert_to_graph(self, exec_paths: List[List[Dict]]) -> Dict[str, Any]:
        """Convert execution paths to graph structure"""
        nodes = {}
        edges = []
        
        for path in exec_paths:
            for node in path:
                nodes[node["id"]] = node
                
            for i in range(len(path) - 1):
                current = path[i]["id"]
                next_node = path[i + 1]["id"]
                
                edge_type = next(
                    (edge["type"] for edge in self.call_graph.get_edges(current)
                     if edge["target"] == next_node),
                    "unknown"
                )
                
                edge = {
                    "source": current,
                    "target": next_node,
                    "type": edge_type
                }
                
                if edge not in edges:
                    edges.append(edge)
                    
        return {
            "nodes": list(nodes.values()),
            "edges": edges
        }
