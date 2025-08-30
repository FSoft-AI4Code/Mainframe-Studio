from typing import Optional

from pydantic import BaseModel

from ...utils import CodeBlock


class DdStatement(BaseModel):
    ddname: str
    parameters_map: dict[str, str]
    dataset_map_list: list[dict[str, str]]
    logic: Optional[str] = None


class ExecStatement(BaseModel):
    step_name: str
    parameters_map: dict[str, str]
    code: CodeBlock
    statements: list[DdStatement]
