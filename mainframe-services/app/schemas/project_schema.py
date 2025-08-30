from typing import Optional, List

from bson import ObjectId
from pydantic import BaseModel

from app.schemas.common_schema import PyObjectId


# Base Models
class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None


# Create Project Endpoints
class ProjectCreate(ProjectBase):
    pass


class ProjectCreateResponse(BaseModel):
    id: PyObjectId
    name: str
    description: Optional[str] = None
    user_id: PyObjectId


# Get Project Endpoints
class GetProjectsResponse(BaseModel):
    projects: List[ProjectCreateResponse]
    total: int
    skip: int
    limit: int


class GetProjectResponse(ProjectCreateResponse):
    pass


# Update Project Endpoints
class UpdateProjectRequest(ProjectBase):
    pass


class UpdateProjectResponse(ProjectCreateResponse):
    pass


# Delete Project Endpoints
class DeleteProjectResponse(BaseModel):
    success: bool = True
    message: str = "Project successfully deleted"


# Common Config for Response Models
class Config:
    populate_by_name = True
    arbitrary_types_allowed = True
    json_encoders = {ObjectId: str}
    from_attributes = True
