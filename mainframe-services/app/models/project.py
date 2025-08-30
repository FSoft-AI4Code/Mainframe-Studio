from pydantic import BaseModel, Field
from typing import Optional, List
from bson import ObjectId
from app.schemas.common_schema import PyObjectId


class Project(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    description: Optional[str] = None
    user_id: PyObjectId

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
