from typing import List, Optional

from pydantic import BaseModel, SerializeAsAny

class WFLStatement(BaseModel):
    raw: str
    start_line: int
    stop_line: int
    tag: str

class Parameter(BaseModel):
    param: str

class Attribute(WFLStatement):
    name: str
    value: str

class Label(WFLStatement):
    label_identifer: str

class Declaration(WFLStatement):
    vars: List[str]

class JobName(WFLStatement):
    file_path: str

class StartAndWaitStatement(WFLStatement):
    file_path: str
    run_parameter_list: List[str]

class WrapAndCompressStatement(WFLStatement):
    wrap_and_compress_from: List[str]
    into_clause: str
    from_clause: Optional[str]
    to_clause: Optional[str]
    task_identifier: Optional[str]

class PrintStatement(WFLStatement):
    print_specification: str
    print_default: str

class MyjobTaskAssignment(WFLStatement):
    reserved_keyword_1: str
    reserved_keyword_2: str
    reserved_keyword_3: str

class MyselfTaskAssignment(WFLStatement):
    reserved_keyword_1: str
    reserved_keyword_2: str

class CopyAndCompareStatement(WFLStatement):
    task_identifier: Optional[str]
    file_path: List[str]
    file_referenced_variable: List[str]
    from_clause: Optional[str]
    to_clause: Optional[str]

class CopyAndRemoveStatement(WFLStatement):
    task_identifier: Optional[str]
    file_path: List[str]
    file_referenced_variable: List[str]
    from_clause: Optional[str]
    to_clause: Optional[str]

class ReplaceStatement(WFLStatement):
    replace_options: Optional[str]
    copy_request: str
    task_identifier: Optional[str]
    task_attribute_assignment: Optional[List[str]]

class ReleaseStatement(WFLStatement):
    file_identifier: str

class LockStatement(WFLStatement):
    file_identifier: str

class OpenStatement(WFLStatement):
    file_identifier: str

class OnStatement(WFLStatement):
    on_type: str
    statements: SerializeAsAny[List[WFLStatement]]

class RemoveStatement(WFLStatement):
    file_path: List[str]
    on_clause: Optional[str]
    from_clause: Optional[str]

class ModifyStatement(WFLStatement):
    file_path: str
    storage_unit: Optional[str]
    run_parameter_list: Optional[List[str]]
    task_identifier_1: Optional[str]
    task_identifier_2: Optional[str]
    task_equation_list: Optional[List[str]]
    local_data_specification: Optional[str]

class GoStatement(WFLStatement):
    label_identifer: str

class CrunchStatement(WFLStatement):
    file_identifier: str

class ChangeStatement(WFLStatement):
    change_item_1: str
    change_item_2: str
    family_name: Optional[str]
    from_clause: Optional[str]

class AlterStatement(WFLStatement):
    long_name: str
    storage_unit: Optional[str]
    alter_attribute_list: List[str]

class CaseClause(BaseModel):
    case_constant_expression: str
    statement_list: Optional[SerializeAsAny[List[WFLStatement]]]

class CaseStatement(WFLStatement):
    case_expression: str
    case_clauses: List[CaseClause]
    else_clause: Optional[SerializeAsAny[List[WFLStatement]]]

class WhileStatement(WFLStatement):
    condition: str
    statements: Optional[SerializeAsAny[List[WFLStatement]]]

class DoStatement(WFLStatement):
    condition: str
    statements: SerializeAsAny[List[WFLStatement]]

class IfStatement(WFLStatement):
    condition: str
    then_clause: SerializeAsAny[List[WFLStatement]]
    else_clause: Optional[SerializeAsAny[List[WFLStatement]]]

class StartStatement(WFLStatement):
    file_path: str
    task_identifier: Optional[str] = None
    start_parameter_list: Optional[List[str]] = None
    storage_unit: Optional[str] = None
    string_primary: str
    start_time_attribute: str

class TaskAssignmentStatement(WFLStatement):
    task_identifier: str
    task_attribute_assignment: List[str]
    file_equation: List[str]

class FileAssignmentStatement(WFLStatement):
    file_identifier: str
    file_attribute_assignment: List[str]

class StringAssignmentStatement(WFLStatement):
    string_identifier: str
    string_expression: str

class RealAssignmentStatement(WFLStatement):
    real_identifier: str
    real_expression: str

class IntegerAssignmentStatement(WFLStatement):
    integer_identifier: str
    integer_expression: str

class BooleanAssignmentStatement(WFLStatement):
    boolean_identifier: str
    boolean_expression: str

class ProcessStatement(WFLStatement):
    statement: Optional[SerializeAsAny[WFLStatement]] = None
    task_identifier: Optional[str] = None
    task_equation_list: Optional[List[str]] = None

class CopyStatement(WFLStatement):
    copy_protocol: Optional[str] = None
    copy_from_clause: Optional[List[str]] = None
    #copy_from_clause: Optional[str] = None
    to_clause: Optional[str] = None
    task_identifier: Optional[str] = None

class AddStatement(WFLStatement):
    task_identifier: Optional[str] = None
    add_options: Optional[List[str]] = None
    copy_request: str
    task_attribute_assignment: Optional[str]
    from_clause: Optional[str]
    to_clause: Optional[str]

class InitializeStatement(WFLStatement):
    task_identifier: str

class AbortStatement(WFLStatement):
    task_identifier: str
    string_expression: Optional[str] = None

class WaitStatement(WFLStatement):
    wait_content: str

class InitializeStatement(WFLStatement):
    task_identifier: str

class DisplayStatement(WFLStatement):
    string_expression: str

class CompileStatement(WFLStatement):
    file_path : str
    task_identifier_1: Optional[str] = None
    compiler_name: Optional[str] = None
    family_name: Optional[str] = None
    compiler_title: Optional[str] = None
    task_identifier_2: Optional[str] = None
    compiler_task_equation_list: Optional[str] = None
    storage_unit: Optional[str]

class SubRoutineDeclaration(WFLStatement):
    subroutine_name: str
    subroutine_parameters: Optional[List[str]] = None
    declarations: Optional[List[Declaration]] = None
    statements: SerializeAsAny[List[WFLStatement]]
    

class SubroutineInvocationStatement(WFLStatement):
    subroutine_identifier: str
    argument_list: Optional[List[str]] = None

class RunStatement(WFLStatement):   
    file_path: str
    task_identifier: Optional[str] = None
    run_parameter_list: Optional[List[str]] = None
    subroutine_name: str
    task_equation_list: Optional[List[str]] = None
    local_data_specification: Optional[str]
    storage_unit: Optional[str]