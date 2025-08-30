from typing import List
from pydantic import BaseModel
class asmCallStatement(BaseModel):        
    subroutine_called: str
    parameter: List[str] = []
    operands: List[str] = []
            