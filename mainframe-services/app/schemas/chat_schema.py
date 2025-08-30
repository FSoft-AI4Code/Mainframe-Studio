from datetime import datetime
from typing import List, Optional, Any

from bson import ObjectId
from pydantic import BaseModel, Field

from app.models.chat import Message
from app.schemas.common_schema import PyObjectId


# Base Models
class ChatBase(BaseModel):
    project_id: PyObjectId


# Create Chat Endpoint
class ChatCreate(ChatBase):
    messages: List[Message] = []
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class ChatCreateResponse(BaseModel):
    id: PyObjectId


# Get Chat Endpoints
class GetChatResponse(ChatBase):
    id: PyObjectId
    messages: List[Message] = []
    created_at: datetime
    updated_at: datetime

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        from_attributes = True


# WebSocket Message Schemas
class MessageConfig(BaseModel):
    is_assessed: bool = False
    is_reversed: bool = False

class MessageCreate(BaseModel):
    repository_id: Optional[str] = None
    content: str
    sender: str
    config: Optional[MessageConfig] = Field(default_factory=MessageConfig)

    class Config:
        populate_by_name = True

class WSMessageRequest(BaseModel):
    content: str
    repository_id: Optional[str] = None
    sender: str = "user"
    config: Optional[MessageConfig] = None

class WSMessageResponse(BaseModel):
    success: bool = True
    type: str = "message"
    data: Any

class WSErrorResponse(BaseModel):
    success: bool = False
    type: str = "error"
    message: str
    error_code: str


# Delete Chat Response
class ChatDeleteResponse(BaseModel):
    success: bool
    message: str = "Chat successfully deleted"
