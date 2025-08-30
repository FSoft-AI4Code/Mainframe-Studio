from typing import List, Optional
from pydantic import BaseModel, SerializeAsAny

class Statement(BaseModel):
    raw: str
    start_line: int
    stop_line: int
    start_idx: int
    stop_idx: int
    tag: str
class Label(BaseModel):
    raw: str
    start_line: int
    stop_line: int
    start_idx: int
    stop_idx: int
    tag: str
    label_name: str
    statement: SerializeAsAny[Statement] = None
class ControlStatement(Statement):
    control_options: List[str] = []

class WriteStatement(Statement):
    content: str

class WriteNrStatement(Statement):
    content: str

class IfStatement(Statement):
    condition: str
    then_statement: SerializeAsAny[List[Statement]] = []
    else_statement: Optional[SerializeAsAny[List[Statement]]] = None


class DoEndStatement(Statement):
    statements: SerializeAsAny[List[Statement]] = []

class SubmitStatement(Statement):
    dataset_name: Optional[str] = None
    jcl_code: Optional[str] = None
    
class ISPExecStatement(Statement):
    service_name: str

class VgetService(ISPExecStatement):
    name_list: List[str] = []
    vget_parameter: Optional[List[str]] = None

class FTOpenSevice(ISPExecStatement):
    open_name: Optional[str] = None
class FTInclService(ISPExecStatement):
    skel_name: str = None
    ftincl_parameters: Optional[List[str]] = None

class FTCloseService(ISPExecStatement):
    close_name: Optional[str] = None
    ftclose_library: Optional[str] = None
    ftclose_parameters: Optional[List[str]] = None

class BrowseService(ISPExecStatement):
    dataset_list: Optional[List[str]] = None
    file_name: Optional[List[str]] = None
    data_id: Optional[str] = None
    browse_parameters: Optional[List[str]] = None

class EditService(ISPExecStatement):
    dataset_list: Optional[List[str]] = None
    file_name: Optional[List[str]] = None
    data_id: Optional[str] = None
    edit_parameters: Optional[List[str]] = None

class FtEraseService(ISPExecStatement):
    member_name: str
    library_name: str


class VputService(ISPExecStatement):
    name_list: List[str] = []
    vput_parameter: Optional[List[str]] = None

class LminitService(ISPExecStatement):
    data_id: str
    dataset_list: Optional[List[str]] = None
    parameters: Optional[List[str]] = None
class LmcopyService(ISPExecStatement):
    copy_from: str
    from_member: str
    copy_to: str
    to_member: str
    parameters: Optional[List[str]] = None
class LmfreeService(ISPExecStatement):
    data_id: str

class TableService(ISPExecStatement):
    table_service_name: str
    table_name: str
    table_parameters: Optional[List[str]] = None
class ControlService(ISPExecStatement):
    parameters: Optional[List[str]] = None
class LogService(ISPExecStatement):
    message: str
class DisplayService(ISPExecStatement):
    parameters: Optional[List[str]] = None
class AddpopService(ISPExecStatement):
    parameters: Optional[List[str]] = None



class ATTNStatement(Statement):
    statements: SerializeAsAny[List[Statement]] = []
  
class InlineStatement(Statement):
    name_of_statement: str


class ReadStatement(Statement):
    variables: Optional[List[str]] = None

class SmCopyStatement(Statement):
    copy_from: str
    copy_to: str
    copy_options: Optional[List[str]] = None

class EditStatement(Statement):
    data_name: str
    edit_options: Optional[List[str]] = None


class InsertStatement(Statement):
    string_to_insert: str

class FindStatement(Statement):
    find_string: str

class ChangeStatement(Statement):
    change_string: str
    original_string: str
    change_parameters: Optional[List[str]] = None



class GotoStatement(Statement):
    label: str


class FreeFileStatement(Statement):
    list_of_files: List[str] = []
    list_of_attributes: Optional[List[str]] = None
    list_of_datasets: Optional[List[str]] = None


class AllocStatement(Statement):
    list_of_files: List[str] = []
    list_of_datasets: List[str] = []
    alloc_parameters: List[str] = []

class RunStatement(Statement):
    program_name: str
    plan_name: str
    library_name: str
    run_parameter: str
class DSNEndStatement(Statement):
    system_name: str
    statements: SerializeAsAny[List[Statement]] = []

class CallStatement(Statement):
    dataset_name: str
    member_name: str
    call_options: Optional[List[str]] = None

class OpenfileStatement(Statement):
    file_name: str
    open_file_option: Optional[str] = None

class GetfileStatement(Statement):
    file_name: str

class ClosefileStatement(Statement):
    file_name: str

class SetStatement(Statement):
    variable: str
    value: Optional[str] = None

class DeleteStatement(Statement):
    dataset_name: str

class GlobalStatement(Statement):
    variable: List[str] = []


class AttributeStatement(Statement):
    attribute_name_list: List[str] = []
    attribute_parameters: Optional[List[str]] = None

class ListDmsStatement(Statement):
    parameters: Optional[List[str]] = None

class ErrorStatement(Statement):
    statement: SerializeAsAny[Statement]

class ReturnStatement(Statement):
    pass

class DoWhileStatement(Statement):
    condition: str
    statements: SerializeAsAny[List[Statement]] = []
    labels: Optional[List[Label]] = None

class PutfileStatement(Statement):
    file_name: str

class ReaddvalStatement(Statement):
    variables: Optional[List[str]] = None

class SelectStatement(Statement):
    test_variable: str
    when_clauses: List[tuple] = []  # List of (condition, statement) tuples
    otherwise_statement: Optional[SerializeAsAny[Statement]] = None

class ExecStatement(Statement):
    dataset_name: List[str] = []

class OutputStatement(Statement):
    job_name: Optional[str] = None
    job_id: Optional[str] = None
    parameters: Optional[List[str]] = None

class CancelStatement(Statement):
    job_name: Optional[str] = None
    job_id: Optional[str] = None

class KdsPrintStatement(Statement):
    parameters: Optional[List[str]] = None
    file_name: Optional[List[str]] = None

class HrecoverStatement(Statement):
    dataset_name: str
    parameters: Optional[List[str]] = None

class JprintrStatement(Statement):
    content: str
    parameters: Optional[List[str]] = None

class HlistStatement(Statement):
    parameters: Optional[List[str]] = None



