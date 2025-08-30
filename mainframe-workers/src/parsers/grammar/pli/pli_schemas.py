from typing import List, Optional
from pydantic import BaseModel

class Statement(BaseModel):
    raw: str
    start_line: int
    stop_line: int
    start_idx: int
    stop_idx: int
    tag: str

class CallStatement(Statement):
    call_option_list: List[str] = []
    file_name: Optional[str] = None