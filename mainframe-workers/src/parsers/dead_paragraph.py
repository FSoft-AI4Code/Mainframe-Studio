from typing import List
from parsers.execution_flow import GraphData, NodeType, RawNode
from parsers.grammar.common.base_cobol_schemas import Paragraph


def get_dead_paragraphs(paragraph_list: List[Paragraph], execution_flow_graph: GraphData, excluded_paragraph_names: List[str]) -> List[str]:
    """Analyze the execution flow graph to identify dead paragraphs.

    Args:
        paragraph_list (List[Paragraph]): List of paragraphs to analyze.
        execution_flow_graph (Dict[str, Any]): The execution flow graph to evaluate.
        excluded_paragraph_names (List[str]): List of paragraph names to exclude from the analysis.
    
    Returns:
        List[str]: List of dead paragraphs.
    """
    
    dead_paragraphs = set()
    
    for paragraph in paragraph_list:
        if paragraph.paragraph_name not in excluded_paragraph_names and not _is_paragraph_node_alive(paragraph.paragraph_name, execution_flow_graph):
            dead_paragraphs.add(paragraph.paragraph_name)
    
    return list(dead_paragraphs)

def _is_paragraph_node_alive(paragraph_name: str, execution_flow_graph: GraphData) -> bool:
        """Find a paragraph node in the execution flow graph by its name.

        Args:
            paragraph_name (str): The name of the paragraph to find.
            execution_flow_graph (Dict[str, Any]): The execution flow graph to search.
        
        Returns:
            bool: True if the paragraph node is alive, otherwise False.
        """
        for node in execution_flow_graph['nodes']:
            if node['name'] == paragraph_name and node['type'] == NodeType.PARAGRAPH:
                return True
            
        return False