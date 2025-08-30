from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime


class AssessmentModel(BaseModel):
    repository_id: ObjectId
    result: Optional[dict] = None
    status: Literal['running', 'done'] = 'running'
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
