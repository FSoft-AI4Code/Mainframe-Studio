from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime
from bson import ObjectId
from app.models.user import PyObjectId


class Complexity(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    repository_id: PyObjectId
    result: Optional[dict] = None
    status: Literal['running', 'done'] = 'running'
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        'populate_by_name': True,
        'arbitrary_types_allowed': True,
        'json_encoders': {ObjectId: str},
        'from_attributes': True
    }
