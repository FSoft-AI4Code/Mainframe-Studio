from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

from app.schemas.common_schema import ResponseBase


class FileInfo(BaseModel):
    """Basic information about a file"""
    id: str = Field(alias="_id")
    repository_id: str
    name: str
    label: Optional[str] = None
    path: str
    encoding: str
    loc: int

    class Config:
        populate_by_name = True
        json_encoders = {
            str: lambda v: v
        }

class DuplicateNameGroup(BaseModel):
    """Group of files that have the same name and label"""
    name: str
    label: str
    files: List[FileInfo]
    has_content_duplicates: bool = False
    content_duplicates: List[List[FileInfo]] = []


class DuplicatesResponse(BaseModel):
    """Overall structure for duplicate files response, primarily grouped by name and label"""
    duplicate_name_groups: List[DuplicateNameGroup] = []
    total: int = 0


class GetDuplicateFilesByRepositoryResponse(ResponseBase[DuplicatesResponse]):
    """Response wrapper for duplicate files by repository"""
