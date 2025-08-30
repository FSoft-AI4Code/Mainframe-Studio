from pydantic import BaseModel, Field
from typing import Optional, List, Union
from datetime import datetime
from bson import ObjectId
from app.schemas.common_schema import PyObjectId


class ReverseEngineering(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    description: Optional[str] = None
    status: Optional[str] = "init"  
    result: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    repository_id: PyObjectId

    output: Optional[Union[dict, List]] = None
    path: Optional[str] = None
    url: Optional[str] = None

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
