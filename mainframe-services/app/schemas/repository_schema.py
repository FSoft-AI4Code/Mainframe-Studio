from typing import List, Literal, Optional

from bson import ObjectId
from pydantic import BaseModel, Field

from app.constants.cobol import SystemType
from app.schemas.common_schema import PyObjectId


# Base Models
class RepositoryBase(BaseModel):
    name: str
    description: Optional[str] = None
    url: str


# Create Repository Endpoints
class RepositoryCreate(RepositoryBase):
    project_id: str
    token: Optional[str] = None
    system_type: SystemType = Field(default=SystemType.IBM)


class RepositoryCreateResponse(BaseModel):
    id: PyObjectId
    name: str
    status: str = Field(default="running")
    is_assessed: bool = Field(default=False)
    is_reversed: bool = Field(default=False)


# Get Repository Endpoints
class GetRepositoryResponse(RepositoryCreateResponse):
    project_id: PyObjectId
    url: Optional[str] = None
    description: Optional[str] = None


class GetRepositoriesResponse(BaseModel):
    repositories: List[GetRepositoryResponse]
    total: int
    skip: int
    limit: int


class File(BaseModel):
    name: str
    path: str
    label: str
    code: int
    comment: int


class GetFilesByRepositoryResponse(BaseModel):
    files: List[File]
    total: int
    skip: int
    limit: int


# Get Repository by Project Endpoint
class GetRepositoryByProjectResponse(RepositoryCreateResponse):
    pass


# Parsed Data Endpoints
class CreateParsedDataResponse(BaseModel):
    id: PyObjectId
    status: str
    message: str = "Parsing initiated"


# Dependency Graph Endpoints
class CreateGraphResponse(BaseModel):
    id: PyObjectId
    nodes: List[dict]
    edges: List[dict]


class GetEntrypointsResponse(BaseModel):
    entrypoints: List[dict]


class GetGraphResponse(CreateGraphResponse):
    pass


class GetFileContentResponse(BaseModel):
    title: str
    content: str


class DeleteGraphResponse(BaseModel):
    success: bool = True
    message: str = "Graph successfully deleted"


# Update Repository Endpoints
class UpdateRepositoryRequest(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None
    token: Optional[str] = None
    status: Optional[Literal[
        "init", "uploaded", "readed", "classified", "parsed", "assessed", "reversed", "summarizing", "summarized", "migrating", "migrated"]] = (
        None
    )
    is_assessed: Optional[bool] = None
    is_reversed: Optional[bool] = None

    class Config:
        populate_by_name = True


class UpdateRepositoryResponse(GetRepositoryResponse):
    pass


# Common Config for Response Models
class Config:
    populate_by_name = True
    arbitrary_types_allowed = True
    json_encoders = {ObjectId: str}
    from_attributes = True
