from typing import List, Optional

from pydantic import BaseModel, SerializeAsAny

from ...utils import CodeBlock


class JclStatement(BaseModel):
    raw: str
    start_line: int
    stop_line: int
    start_idx: int
    stop_idx: int
    tag: str


class JclParameter(BaseModel):
    param_name: str
    param_value: str


class ContinueStatement(JclStatement):
    parameters: List[JclParameter]


class DdStatement(JclStatement):
    ddname: str
    parameters_map: dict[str, str]
    dataset_map_list: list[dict[str, str]]
    logic: Optional[str] = None
    statements: SerializeAsAny[List[JclStatement]] = []


class JobStatement(JclStatement):
    job_name: Optional[str] = None
    parameters: List[JclParameter]
    statements: SerializeAsAny[List[JclStatement]] = []


class JoblibStatement(JclStatement):
    job_name: Optional[str] = None
    parameters: List[JclParameter]
    statements: SerializeAsAny[List[JclStatement]] = []


class ExecStatement(JclStatement):
    step_name: str
    parameters_map: dict[str, str]
    code: CodeBlock
    statements: SerializeAsAny[list[JclStatement]]


class IncludeStatement(JclStatement):
    member_name: str


class JclLibStatement(JclStatement):
    lib_name: str
    parameters: List[JclParameter]
    statements: SerializeAsAny[List[JclStatement]] = []


class SetStatement(JclStatement):
    name: str
    parameters: List[JclParameter]


class ProcStatement(JclStatement):
    parameters: List[JclParameter]


class IfStatement(JclStatement):
    condition: str
    then: SerializeAsAny[List[JclStatement]]
