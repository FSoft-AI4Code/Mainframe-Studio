from datetime import datetime
from typing import Optional, Any
from pydantic import BaseModel, Field
from bson import ObjectId
from app.config.constants import IBM_MAINFRAME_UTILITIES
from app.schemas.common_schema import PyObjectId

class UtilityBase(BaseModel):
    name: str
    description: Optional[str] = None
    category: str
    node_id: PyObjectId
    repository_id: PyObjectId
    comment: str = ""  # Default empty string
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def __init__(self, **data):
        super().__init__(**data)
        # Set description from IBM_MAINFRAME_UTILITIES if not provided
        if not self.description and self.name in IBM_MAINFRAME_UTILITIES:
            self.description = IBM_MAINFRAME_UTILITIES[self.name]

class UtilityCreate(UtilityBase):
    pass

class UtilityUpdate(BaseModel):
    description: Optional[str] = None
    category: Optional[str] = None
    comment: Optional[str] = None
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def __init__(self, **data):
        super().__init__(**data)
        # Update description from IBM_MAINFRAME_UTILITIES if available
        if self.description is None and "name" in data and data["name"] in IBM_MAINFRAME_UTILITIES:
            self.description = IBM_MAINFRAME_UTILITIES[data["name"]]

class UtilityInDB(UtilityBase):
    id: PyObjectId = Field(alias="_id")

    class Config:
        populate_by_name = True
        json_encoders = {
            ObjectId: str
        }
        arbitrary_types_allowed = True
        from_attributes = True

class UtilityResponse(UtilityInDB):
    pass

class UtilityListResponse(BaseModel):
    utilities: list[UtilityResponse]
    total: int
    skip: int
    limit: int 