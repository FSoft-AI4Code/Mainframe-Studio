from enum import Enum
from typing import Literal, Optional

from bson import ObjectId
from pydantic import BaseModel, Field

from app.constants.cobol import SystemType
from app.schemas.common_schema import PyObjectId


class Repository(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    url: str
    description: Optional[str] = None
    project_id: PyObjectId
    status: Literal["init", "uploaded", "readed", "classified", "parsed", "assessed", "reversed", "summarizing", "summarized", "migrating", "migrated"] = "init"
    is_assessed: bool = False
    is_reversed: bool = False
    system_type: Optional[SystemType] = SystemType.IBM

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
