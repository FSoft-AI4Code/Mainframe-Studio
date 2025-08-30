from typing import List, Optional

from pydantic import BaseModel


class CobolVariable(BaseModel):
    level: str
    name: str
    picture_clause: Optional[str] = None
    default_value: Optional[str] = None
    redefine: Optional[str] = None
    occur: Optional[int] = None


class CopybookReplace(BaseModel):
    replaceable: str
    replacement: str


class ImportedCopybook(BaseModel):
    copybook_name: str
    line_number: int
    replacing: list[CopybookReplace] = []


class FileControlEntry(BaseModel):
    file_name: str
    assignment_name: str
    code_content: str
    access_mode: str


class FileDescriptionEntry(BaseModel):
    file_name: str
    code_content: str
    code_content: str
    code_content: str
    variables: List[CobolVariable]
    copybooks: List[ImportedCopybook]


class Paragraph(BaseModel):
    paragraph_name: str
    section: Optional[str] = None
    paragraph_code: str
    paragraph_lines: List[int]
    ref_paragraphs: List[str]


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
