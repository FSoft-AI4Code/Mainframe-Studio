from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Optional
from app.models.user import PyObjectId


class ComplexityBase(BaseModel):
    repository_id: PyObjectId
    name: str
    description: Optional[str] = None
    status: str = "pending"
    result: Optional[dict] = None


class ComplexityCreate(ComplexityBase):
    repository_id: PyObjectId

class ComplexityCreateResponse(BaseModel):
    id: PyObjectId
    repository_id: PyObjectId
    status: str

# Get Complexity Endpoints
class GetComplexityResponse(ComplexityCreateResponse):
    result: Optional[dict] = None
    created_at: datetime
    updated_at: datetime

class GetComplexitiesResponse(BaseModel):
    complexities: List[GetComplexityResponse]
    total: int
    skip: int
    limit: int


# Get Complexitys by Repository Endpoint
class GetComplexitiesByRepositoryResponse(BaseModel):
    complexities: List[GetComplexityResponse]
    average_complexity: float
    number_of_complexities: int


# Update Complexity Endpoints
class UpdateComplexityRequest(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    result: Optional[dict] = None

class UpdateComplexityResponse(GetComplexityResponse):
    pass


# Delete Complexity Response
class DeleteComplexityResponse(BaseModel):
    success: bool = True
    message: str = "Complexity successfully deleted"


# Common Config
class Config:
    populate_by_name = True
    arbitrary_types_allowed = True
    json_encoders = {PyObjectId: str}
    from_attributes = True
