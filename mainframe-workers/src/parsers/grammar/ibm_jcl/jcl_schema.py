from abc import ABC
from typing import Dict, List, Literal, LiteralString, Optional, Type

from loguru import logger
from pydantic import BaseModel, Field, SerializeAsAny

from parsers.grammar.common.base_cobol_schemas import CodeBlock

_jcl_statement_registry: Dict[str, Type["JclStatement"]] = {}


class JclStatement(BaseModel):
    raw: str
    start_line: int
    stop_line: int
    start_idx: int
    stop_idx: int
    tag: str

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        _jcl_statement_registry[cls.__name__] = cls

    @classmethod
    def subclass_registry(cls) -> Dict[str, Type["JclStatement"]]:
        return _jcl_statement_registry

    class Config:
        extra = "allow"


def _deserialize_jcl_statements(statements_list: List) -> List:
    """Convert dictionaries in statements list to appropriate JclStatement objects"""
    if not statements_list:
        return []

    tag_to_class = {
        subclass.model_fields["tag"].default: subclass
        for name, subclass in JclStatement.subclass_registry().items()
    }

    result = []
    for statement in statements_list:
        if isinstance(statement, dict):
            statement_tag = statement.get("tag")
            statement_class = tag_to_class.get(statement_tag)
            if statement_class:
                result.append(statement_class(**statement))
            else:
                logger.warning(
                    "Unknown JCL statement tag, skipping deserialization for this statement",
                    tag=statement_tag,
                    statement=statement,
                )
        elif isinstance(statement, JclStatement):
            result.append(statement)
        else:
            logger.warning(
                "Invalid statement type, expected a dictionary or JclStatement object, skipping deserialization",
                statement=statement,
            )

    return result


class JclParameter(BaseModel):
    param_name: str
    param_value: str


class ContinueStatement(JclStatement):
    tag: str = "ContinueStatement"
    parameters: List[JclParameter]


class DdStatement(JclStatement):
    tag: str = "DdStatement"
    ddname: str
    parameters_map: dict[str, str]
    dataset_map_list: list[dict[str, str]]
    logic: Optional[str] = None
    statements: SerializeAsAny[List[JclStatement]] = []

    def __init__(self, **kwargs):
        if "statements" in kwargs:
            kwargs["statements"] = _deserialize_jcl_statements(kwargs["statements"])
        super().__init__(**kwargs)


class JobStatement(JclStatement):
    tag: str = "JobStatement"
    job_name: Optional[str] = None
    parameters: List[JclParameter]
    statements: SerializeAsAny[List[JclStatement]] = []

    def __init__(self, **kwargs):
        if "statements" in kwargs:
            kwargs["statements"] = _deserialize_jcl_statements(kwargs["statements"])
        super().__init__(**kwargs)


class JoblibStatement(JclStatement):
    tag: str = "JoblibStatement"
    job_name: Optional[str] = None
    parameters: List[JclParameter]
    statements: SerializeAsAny[List[JclStatement]] = []

    def __init__(self, **kwargs):
        if "statements" in kwargs:
            kwargs["statements"] = _deserialize_jcl_statements(kwargs["statements"])
        super().__init__(**kwargs)


class ExecStatement(JclStatement):
    tag: str = "ExecStatement"
    step_name: str
    parameters_map: dict[str, str]
    code: CodeBlock
    statements: SerializeAsAny[List[JclStatement]]

    def __init__(self, **kwargs):
        if "statements" in kwargs:
            kwargs["statements"] = _deserialize_jcl_statements(kwargs["statements"])

        super().__init__(**kwargs)


class IncludeStatement(JclStatement):
    tag: str = "IncludeStatement"
    member_name: str


class JclLibStatement(JclStatement):
    tag: str = "JclLibStatement"
    lib_name: str
    parameters: List[JclParameter]
    statements: SerializeAsAny[List[JclStatement]] = []

    def __init__(self, **kwargs):
        if "statements" in kwargs:
            kwargs["statements"] = _deserialize_jcl_statements(kwargs["statements"])

        super().__init__(**kwargs)


class SetStatement(JclStatement):
    tag: str = "SetStatement"
    name: str
    parameters: List[JclParameter]


class ProcStatement(JclStatement):
    tag: str = "ProcStatement"
    parameters: List[JclParameter]


class IfStatement(JclStatement):
    tag: str = "IfStatement"
    condition: str
    then: SerializeAsAny[List[JclStatement]]
