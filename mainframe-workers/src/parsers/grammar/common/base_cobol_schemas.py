from typing import List, Optional, Literal

from pydantic import BaseModel


class CodeBlock(BaseModel):
    content: str
    start_line: int
    end_line: int


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

class MultiLayoutFileDescription(BaseModel):
    file_name: str
    variable_names: List[str]
    copybook_names: List[str]


class MultiLayoutVariable(BaseModel):
    redefined_variableName: str
    redefining_variableNames: List[str]

class MultiLayoutProgram(BaseModel):
    name_program: str
    type: Literal["COBOL", "COPY"]
    working_storage: Optional[List[MultiLayoutVariable]] = None
    linkage_section: Optional[List[MultiLayoutVariable]] = None
    File_section: Optional[List[MultiLayoutFileDescription]] = None

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
    dataset_type: str
    organization: Optional[str] = None


class FileDescriptionEntry(BaseModel):
    file_name: str
    code_content: str
    code_content: str
    code_content: str
    variables: List[CobolVariable]
    copybooks: List[ImportedCopybook]


class DatabaseTable(BaseModel):
    table_name: str
    invoke_name: Optional[str] = None
    using_names: List[str] = []


class Database(BaseModel):
    database_name: str
    invoke_name: Optional[str] = None
    tables: List[DatabaseTable]


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
