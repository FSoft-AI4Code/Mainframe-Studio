from typing import List
from bson import ObjectId
from pydantic import BaseModel, Field
from app.schemas.common_schema import PyObjectId
from app.schemas.graph_schema import EntryPoint, Node, Edge

class NodeModel(Node):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    repository_id: PyObjectId
    is_entry_point: bool = False

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        from_attributes = True

class EdgeModel(Edge):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    repository_id: PyObjectId

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        from_attributes = True

class EntryPointModel(EntryPoint):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    repository_id: PyObjectId

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        from_attributes = True