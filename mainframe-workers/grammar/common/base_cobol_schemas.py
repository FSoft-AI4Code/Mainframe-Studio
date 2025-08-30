from typing import List, Optional

from pydantic import BaseModel


class CalledProgram(BaseModel):
    program_id: str
    line_number: int
    parameters: List[str]
    call_type: str


class CobolVariable(BaseModel):
    level: str
    name: str
    line_number: int
    picture_clause: Optional[str] = None
    default_value: Optional[str] = None
    redefine: Optional[str] = None
    occur: Optional[int] = None
    compression_format: Optional[str] = None
    length: Optional[int] = None


class CobolProgramVariables(BaseModel):
    working_storage: List[CobolVariable]
    linkage_section: List[CobolVariable]


class CopybookReplace(BaseModel):
    replaceable: str
    replacement: str


class Division(BaseModel):
    division_name: str
    start_line: int
    stop_line: int


class ImportedCopybook(BaseModel):
    copybook_name: str
    line_number: int
    replacing: list[CopybookReplace] = []


class FileControlEntry(BaseModel):
    file_name: str
    assignment_name: str
    code_content: str
    open_type: str
    access_mode: str


class FileDescriptionEntry(BaseModel):
    file_name: str
    code_content: str
    code_content: str
    code_content: str
    variables: List[CobolVariable]
    copybooks: List[ImportedCopybook]


class DatabaseEntry(BaseModel):
    database_name: str
    invoke_name: Optional[str] = None
    using_names: List[str] = []


class SystemDatabaseEntry(BaseModel):
    system_database_name: str
    invoke_name: Optional[str] = None
    databases: List[DatabaseEntry]


class Comment(BaseModel):
    content: str
    line_number: int


class ProcedureSection(BaseModel):
    section_name: str
    start_line: int
    stop_line: int
    paragraph_name_list: List[str]


class Paragraph(BaseModel):
    paragraph_name: str
    section: Optional[str] = None
    paragraph_code: str
    paragraph_lines: List[int]


class Statement(BaseModel):
    """Base class for all statements"""

    raw: str
    start_line: int
    stop_line: int
    start_idx: int
    stop_idx: int
    paragraph: Optional[str] = None
    section: Optional[str] = None
    tag: str
