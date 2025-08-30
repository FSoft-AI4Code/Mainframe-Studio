from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
from datetime import datetime

class CopybookReverseModel(BaseModel):
    name: str
    content: str
    output: Dict[str, Any]
    path: str
    url: str
    status: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow) 