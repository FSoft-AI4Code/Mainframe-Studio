from typing import Dict, List

from loguru import logger

from controller.reverse_controller import ReverseController
from parsers.grammar.common.base_cobol_schemas import ImportedCopybook


def analyze_missing_paragraphs(repository_id: str, local_missing_paragraphs: List[dict], copybook_list: List[ImportedCopybook]) -> List[str]:
    """
    Analyze missing paragraphs by checking if they are defined in any included copybooks.
    
    This function takes a list of paragraphs that are referenced but not defined in the main program,
    and searches through the included copybooks to determine if they are defined there.
    
    Args:
        repository_id (str): The repository ID to use for database queries
        local_missing_paragraphs (List[dict]): A list of missing paragraph dictionaries,
                                               each containing at least a "name" key
        copybook_list (List[ImportedCopybook]): A list of imported copybook objects
        
    Returns:
        List[str]: A list of paragraph names that are missing (not found in the main program
                  or any included copybooks)
    """
    copybook_reverse_map = _get_copybook_reverses(repository_id, copybook_list)
    found_paragraphs: set[str] = set()
    
    for paragraph in local_missing_paragraphs:
        paragraph_name = paragraph.get("name", "")
        for copybook_name, copybook_reverse in copybook_reverse_map.items():
            paragraph_list = copybook_reverse.get("paragraph_list", [])
            copybook_paragraph_names = [paragraph.get("paragraph_name") for paragraph in paragraph_list]
            
            if paragraph_name in copybook_paragraph_names:
                found_paragraphs.add(paragraph_name)

    local_missing_paragraph_names: set[str] = set(paragraph.get("name") for paragraph in local_missing_paragraphs)
    missing_paragraphs = local_missing_paragraph_names - found_paragraphs
    
            
    return list(missing_paragraphs)


def _get_copybook_reverses(repository_id: str, copybook_list: List[ImportedCopybook]) -> Dict[str, Dict]:
    """
    Retrieve reverse engineering data for a list of copybooks.
    
    This function queries the database for information about each copybook in the list
    and returns a dictionary mapping copybook names to their reverse engineering data.
    
    Args:
        repository_id (str): The repository ID to use for database queries
        copybook_list (List[ImportedCopybook]): A list of imported copybook objects
        
    Returns:
        Dict[str, Dict]: A dictionary mapping copybook names to their reverse engineering data
    """
    reverse_controller = ReverseController()
    copybook_reverses = {}
    for copybook in copybook_list:
        copybook_name = copybook.copybook_name
        copybook_name = copybook_name.replace("'", "")
        copybook_reverse = reverse_controller.query_reverse_engineering_full(copybook_name,repository_id, type_="COPY")
        if copybook_reverse:
            copybook_reverses[copybook_name] = copybook_reverse.get("output", {})
        else:
            logger.warning(f"Copybook {copybook_name} not found in the database.")

    return copybook_reverses