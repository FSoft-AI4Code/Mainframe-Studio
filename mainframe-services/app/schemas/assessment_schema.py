from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from app.schemas.common_schema import PyObjectId


# Base Assessment Schema
class AssessmentBase(BaseModel):
    repository_id: PyObjectId
    name: str
    description: Optional[str] = None
    status: str = "pending"
    result: Optional[dict] = None


# Create Assessment Endpoints
class AssessmentCreate(BaseModel):
    repository_id: PyObjectId

class AssessmentCreateResponse(BaseModel):
    id: PyObjectId
    repository_id: PyObjectId
    status: str


# Get Assessment Endpoints
class GetAssessmentResponse(AssessmentCreateResponse):
    result: Optional[dict] = None
    created_at: datetime
    updated_at: datetime

class GetAssessmentsResponse(BaseModel):
    assessments: List[GetAssessmentResponse]
    total: int
    skip: int
    limit: int


# Get Assessments by Repository Endpoint
class GetAssessmentsByRepositoryResponse(BaseModel):
    assessments: List[GetAssessmentResponse]

# Get File Counts by Repository Endpoint
class FileCountItem(BaseModel):
    count: int
    label: str
class GetFileCountsByRepositoryResponse(BaseModel):
    total: int
    file_counts: List[FileCountItem]


# Get Assessment Overview (by Repository) Endpoint
class GetAssessmentOverviewByRepositoryResponse(BaseModel):
    coverage: float
    average_complexity: float 
    dead_code_percentage: float 


# Update Assessment Endpoints
class UpdateAssessmentRequest(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    result: Optional[dict] = None

class UpdateAssessmentResponse(GetAssessmentResponse):
    pass


# Delete Assessment Response
class DeleteAssessmentResponse(BaseModel):
    success: bool = True
    message: str = "Assessment successfully deleted"


# Common Config
class Config:
    populate_by_name = True
    arbitrary_types_allowed = True
    json_encoders = {PyObjectId: str}
    from_attributes = True
