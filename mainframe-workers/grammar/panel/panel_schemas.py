from typing import List, Optional
from pydantic import BaseModel, SerializeAsAny

class AttributeComponent(BaseModel):
    attribute_character: str
    attribute_parameters: List[str]

class Section(BaseModel):
    raw: str
    start_line: int
    stop_line: int
    start_idx: int
    stop_idx: int
    tag: str

class Statement(BaseModel):
    raw: str
    start_line: int
    stop_line: int
    start_idx: int
    stop_idx: int
    tag: str

class AttributeSection(Section):
    default_parameter: Optional[str] = None
    format_parameter: Optional[str] = None
    attribute_components: List[AttributeComponent]

class BodySection(Section):
    body_parameters: List[str]
    body_text: str

class InitSection(Section):
    statements: SerializeAsAny[List[Statement]]

class ProcedureSection(Section):
    statements: SerializeAsAny[List[Statement]]

class ModelSection(Section):
    model_parameters: List[str]
    models: List[Statement]

class ReInitSection(Section):
    statements: SerializeAsAny[List[Statement]]

class AssignStatement(Statement):
    variable: str
    value: str
class VgetStatement(Statement):
    name_list: List[str]
    vget_parameters: List[str]


class VputStatement(Statement):
    name_list: List[str]
    vput_parameters: List[str]

class RefreshStatement(Statement):
    variable: str

class IfStatement(Statement):
    condition: str
    then_statements: SerializeAsAny[List[Statement]]
    else_statements: Optional[SerializeAsAny[List[Statement]]] = None

class VerStatement(Statement):
    variable: str
    criteria: List[str]
    message: Optional[str] = None
