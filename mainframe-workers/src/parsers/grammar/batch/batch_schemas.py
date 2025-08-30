from typing import List, Optional

from pydantic import BaseModel, SerializeAsAny


class BatchStatement(BaseModel):
    """Base class for all Batch statements"""

    raw: str
    start_line: int
    stop_line: int
    tag: str


class BatchLabel(BaseModel):
    """Represents a label in a Batch script"""

    label_name: str
    start_line: int
    stop_line: int
    statements: SerializeAsAny[List[BatchStatement]]


class SetStatement(BatchStatement):
    """Represents a 'set' statement in a Batch script"""

    switches: List[str]
    source: str
    target: Optional[str] = None


class SetLocalStatement(BatchStatement):
    """Represents a 'setlocal' statement in a Batch script"""

    option: str


class DelStatement(BatchStatement):
    """Represents a 'del' statement in a Batch script"""

    file_path: str


class PauseStatement(BatchStatement):
    """Represents a 'pause' statement in a Batch script"""

    pass


class MkdirStatement(BatchStatement):
    """Represents a 'mkdir' statement in a Batch script"""

    value: str


class XcopyStatement(BatchStatement):
    """Represents an 'xcopy' statement in a Batch script"""

    source: str
    destination: str
    switches: List[str]


class CallStatement(BatchStatement):
    """Represents a 'call' statement in a Batch script"""

    label: Optional[str] = None
    file_path: Optional[str] = None
    condition: Optional[str] = None
    parameters: List[str]


class IfStatement(BatchStatement):
    """Represents an 'if' statement in a Batch script"""

    condition: str
    then_statements: SerializeAsAny[List[BatchStatement]]
    else_statements: Optional[SerializeAsAny[List[BatchStatement]]] = None


class GotoStatement(BatchStatement):
    """Represents a 'goto' statement in a Batch script"""

    label: Optional[str] = None


class EchoStatement(BatchStatement):
    """Represents an 'echo' statement in a Batch script"""

    message: str


class RemStatement(BatchStatement):
    """Represents a 'rem' statement in a Batch script"""

    comment: str


class EndlocalStatement(BatchStatement):
    """Represents an 'endlocal' statement in a Batch script"""

    pass


class ExitStatement(BatchStatement):
    """Represents an 'exit' statement in a Batch script"""

    exit_code: Optional[str] = None
    is_exit_current_branch: bool = False


class ExecStatement(BatchStatement):
    """Represents an 'exec' statement in a Batch script"""

    file: str
    switches: Optional[List[str]] = None
    parameters: Optional[List[str]] = None


class RmdirStatement(BatchStatement):
    """Represents an 'rmdir' statement in a Batch script"""

    value: str
    switches: Optional[List[str]] = None


class ForStatement(BatchStatement):
    """Represents a 'for' statement in a Batch script"""

    variable: str
    values: List[str]
    do_statements: SerializeAsAny[List[BatchStatement]]


class TypeStatement(BatchStatement):
    """Represents a 'type' statement in a Batch script"""

    file_path: str


class Z7Statement(BatchStatement):
    """Represents a '7z' statement in a Batch script"""

    file_path: str
    command: str
    switches: List[str]


class BsortexStatement(BatchStatement):
    """Represents a 'bsortex' statement in a Batch script"""

    sort_parameters: List[str]
    input_parameters: List[str]
    record_parameters: List[str]
    option_parameters: List[str]
    output_parameters: List[str]
