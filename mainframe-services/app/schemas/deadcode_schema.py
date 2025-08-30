from typing import List, Optional

from pydantic import BaseModel

from app.constants.cobol import FileType


class DeadTotal(BaseModel):
    dead: int
    total: int


class FileForDeadCode(BaseModel):
    file_name: str
    type: Optional[FileType] = None
    lines_of_code: int
    complexity: int


# Get Deadcode Endpoints
class GetDeadcodeResponse(BaseModel):
    dead_total: DeadTotal
    complexity_reduction_percentage: float
    files: List[FileForDeadCode]
    skip: int
    limit: int
