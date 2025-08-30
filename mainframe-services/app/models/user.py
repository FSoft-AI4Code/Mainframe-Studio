from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Any, List, Optional, Dict
from app.schemas.user_schema import Permission
from app.schemas.common_schema import PyObjectId


class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    email: str
    hashed_password: str
    is_active: bool = True
    permissions: List[Permission] = []

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
