from enum import Enum
from typing import Optional

from pydantic import BaseModel, SerializeAsAny

from parsers.grammar.common.base_cobol_schemas import (
    CobolVariable,
    Comment,
    Division,
    FileControlEntry,
    FileDescriptionEntry,
    ImportedCopybook,
    ProcedureSection,
    Statement,
)
from parsers.grammar.ibm_cobol.MyCobol85Visitor import Paragraph


class ReverseEngineeringStatus(str, Enum):
    """
    Status codes for reverse engineering process.
    """

    CLASSIFIED = "classified"
    CLASSIFIED_ERROR = "classified_error"
    ASSESSED = "assessed"
    ASSESSED_ERROR = "assessed_error"
    PARSED = "parsed"
    PARSED_ERROR = "parsed_error"
    LINKED = "linked"
    LINKED_ERROR = "linked_error"
    
    # Statuses for JCL
    EXTRACTED_DATASET_ASSIGNMENT = "extracted_dataset_assignment"
    EXTRACTED_DATASET_ASSIGNMENT_ERROR = "extracted_dataset_assignment_error"


class ReverseEngineeringUpdate(BaseModel):
    name: Optional[str] = None
    output: Optional[dict] = None
    type: Optional[str] = None
    status: Optional[ReverseEngineeringStatus] = None


class ParsedProgramAntlr(BaseModel):
    program_id: str
    copybook_list: list[ImportedCopybook]
    file_control_list: list[FileControlEntry]
    file_description_list: list[FileDescriptionEntry]
    variable_list: SerializeAsAny[list[CobolVariable]]
    paragraph_list: list[Paragraph]
    statements: SerializeAsAny[list[Statement]]
    section_list: list[ProcedureSection]
    comment_list: list[Comment]
    division_list: list[Division]
