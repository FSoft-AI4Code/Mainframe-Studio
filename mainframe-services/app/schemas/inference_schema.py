from typing import Any, Dict, Optional
from pydantic import BaseModel, Field

class SummarizationRequest(BaseModel):
    repository_id: str = Field(..., description="Repository ID")
    type: str = Field(..., description="File type (e.g., COBOL)")
    name: str = Field(..., description="File name to summarize")

class ModernizationRequest(BaseModel):
    repository_id: str = Field(..., description="Repository ID")
    type: str = Field(..., description="File type (e.g., BMS)")
    name: str = Field(..., description="File name to modernize")

class SummarizationResponse(BaseModel):
    summarization: Dict[str, Any]

class ModernizationResponse(BaseModel):
    url: Optional[str] = Field(None, description="URL to the modernized code view")
    # html_content: Optional[str] = Field(None, description="HTML content of the modernized view")