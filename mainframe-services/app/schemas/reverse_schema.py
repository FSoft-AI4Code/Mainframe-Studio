from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from bson import ObjectId

from app.constants.cobol import FileType
from app.schemas.common_schema import PyObjectId


class ReverseEngineeringBase(BaseModel):
    name: str
    description: Optional[str] = None
    status: str = "init"
    result: Optional[str] = None

    path: str
    url: str

    output: Optional[dict] = None


class ReverseEngineeringCreate(ReverseEngineeringBase):
    repository_id: PyObjectId

class ReverseEngineeringStatus(str, Enum):
    """
    Status codes for reverse engineering process.
    """

    CLASSIFIED = "classified"
    CLASSIFIED_ERROR = "classified_error"
    ASSESSED = "assessed"
    ASSESSED_ERROR = "assessed_error"
    PARSED = "parsed"
    PARSED_ERROR = "parsed_error"
    LINKED = "linked"
    LINKED_ERROR = "linked_error"
    
    # Statuses for JCL
    EXTRACTED_DATASET_ASSIGNMENT = "extracted_dataset_assignment"
    EXTRACTED_DATASET_ASSIGNMENT_ERROR = "extracted_dataset_assignment_error"


class ReverseEngineeringUpdate(BaseModel):
    status: str
    output: Optional[dict] = None
    type: Optional[str] = None

class ReverseEngineering(ReverseEngineeringBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    repository_id: PyObjectId
    created_at: datetime
    updated_at: datetime

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        from_attributes = True


# Add new response schema for getting reverse by name
class ReverseEngineeringOutputResponse(BaseModel):
    status: str
    output: Optional[dict] = None
    type: str = None
    name: str = None
    class Config:
        populate_by_name = True
        from_attributes = True

class ReverseEngineeringReportResponse(BaseModel):
    status: str
    type: str
    name: str
    is_reversed: bool
    

# Response schema for reverse assets coverage
class ReverseAssetsCoverageByTypeResponse(BaseModel):
    type: str | None = None
    coverage: float

class ReverseAssetsCoverageResponse(BaseModel):
    total_coverage: float
    by_types: list[ReverseAssetsCoverageByTypeResponse]

class UpdateNodeLabelRequest(BaseModel):
    file_name: str
    label: FileType
    new_label: FileType
    comment: Optional[str] = None
    description: Optional[str] = None

class UpdateNodeLabelResponse(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    repository_id: PyObjectId
    label: FileType
    group: Optional[list] = None
    is_entry_point: Optional[bool] = False
    status: str
    comment: Optional[str] = None
    description: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
