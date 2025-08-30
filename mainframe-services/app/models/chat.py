from datetime import datetime
from typing import List, Optional

from bson import ObjectId
from pydantic import BaseModel, Field

from app.schemas.common_schema import PyObjectId


class Message(BaseModel):
    content: str
    sender: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class ChatBase(BaseModel):
    project_id: PyObjectId
    messages: List[Message] = []


class ChatCreate(ChatBase):
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class Chat(ChatBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        from_attributes = True
