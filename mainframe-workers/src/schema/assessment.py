from typing import Literal, Optional
from pydantic import BaseModel


class AssessmentUpdate(BaseModel):
    status: Literal['running', 'done']
    result: Optional[dict] = None
