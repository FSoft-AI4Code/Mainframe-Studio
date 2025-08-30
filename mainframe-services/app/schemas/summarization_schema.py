from typing import Dict, Optional, Literal, List

from pydantic import BaseModel, Field

from app.schemas.common_schema import PyObjectId


class Summarization(BaseModel):
    id: PyObjectId
    repository_id: str = Field(..., description="Repository or project ID")
    status: Literal['running', 'done'] = Field(..., description="Processing status")
    path: str = Field(..., description="File path to the BMS screen")
    short_description: str = Field(..., description="Brief purpose of the screen")
    parameters: Dict[str, str] = Field(..., description="Field name -> metadata string")
    linked_bms: List[str] = Field(default_factory=list)
    result: Optional[dict] = Field(default=None, description="Optional full summary or error details")
