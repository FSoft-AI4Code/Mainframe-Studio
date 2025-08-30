from typing import List, Optional

from pydantic import BaseModel, SerializeAsAny


class LDLPStatement(BaseModel):
    raw: str
    start_line: int
    stop_line: int
    tag: str


class ParsedLDLP(BaseModel):
    statements: SerializeAsAny[List[LDLPStatement]]


class MoveStatement(LDLPStatement):
    source: str
    source_position: Optional[str] = None
    length: Optional[str] = None
    target: str
    target_position: Optional[str] = None
    sort_order: Optional[str] = None
    gs_status: Optional[str] = None


class Assignment(LDLPStatement):
    source: str
    target: str


class DowhenStatement(LDLPStatement):
    condition: str
    statements: SerializeAsAny[List[LDLPStatement]] = []
    else_statements: SerializeAsAny[List[LDLPStatement]] = []


class RecallStatement(LDLPStatement):
    object_name: Optional[str] = None
    is_recall_bye: bool = False
    is_recall_exit: bool = False
    teach_screen: Optional[str] = None


class AdvanceStatement(LDLPStatement):
    number_of_lines: Optional[int] = None
    is_to_new_page: bool = False
    channel: Optional[int] = None
    output_stream: Optional[str] = None


class AddStatement(LDLPStatement):
    first_operand: str
    second_operand: str
    results: str
    is_rounded: bool = False
    gs_status: Optional[str] = None


class DivideStatement(LDLPStatement):
    dividend: str
    divisor: str
    results: str
    is_rounded: bool = False
    remainder: Optional[str] = None
    gs_status: Optional[str] = None


class MultiplyStatement(LDLPStatement):
    multiplicand: str
    multiplier: str
    results: str
    is_rounded: bool = False
    gs_value: Optional[str] = None


class DateConvertStatement(LDLPStatement):
    input_date_variable: str
    offset: Optional[str] = None
    format: str
    gs_status: Optional[str] = None


class InsertStatement(LDLPStatement):
    insertable: str
    mapping: List[str] = []


class Case(BaseModel):
    values: List[str] = []
    statements: SerializeAsAny[List[LDLPStatement]] = []


class CaseStatement(LDLPStatement):
    control_value: str
    cases: List[Case]
    otherwise_statements: SerializeAsAny[List[LDLPStatement]] = []


class ComputeStatement(LDLPStatement):
    results: str
    evaluate_expression: str
    is_rounded: bool = False
    gs_status: Optional[str] = None


class DetermineStatementBase(LDLPStatement):
    is_serial: bool = False
    is_secure: bool = False
    is_key_only: bool = False
    gs_status: Optional[str] = None
    multi_records: Optional[str] = None


class DetermineActualStatement(DetermineStatementBase):
    variant: str
    iterator: Optional[str] = None
    extract_file: Optional[str] = None
    extracted_as: Optional[str] = None
    retained_as: Optional[str] = None
    statements: SerializeAsAny[List[LDLPStatement]] = []


class DetermineEveryStatement(DetermineStatementBase):
    iterator: str
    statements: SerializeAsAny[List[LDLPStatement]] = []


class DetermineBackStatement(DetermineStatementBase):
    iterator: str
    statements: SerializeAsAny[List[LDLPStatement]] = []


class DetermineFromStatement(DetermineStatementBase):
    iterator: str
    statements: SerializeAsAny[List[LDLPStatement]] = []


class DetermineGroupStatement(DetermineStatementBase):
    iterator: str
    arguments: List[str] = []
    until_arguments: List[str] = []
    statements: SerializeAsAny[List[LDLPStatement]] = []


class DetermineLastStatement(DetermineStatementBase):
    iterator: str


class DetermineTotalStatement(DetermineStatementBase):
    identifier: str
    attribute_name: str
    arguments: List[str] = []
    statements: SerializeAsAny[List[LDLPStatement]] = []


class BreakStatement(LDLPStatement):
    is_break_all: bool = False


class AccessExtStatement(LDLPStatement):
    db_name: str
    access_ext_type: str
    database: str
    item: Optional[str] = None


class LookupBaseStatement(LDLPStatement):
    primary_key: str
    class_name: str
    is_secure: bool = False
    is_key_only: bool = False
    gs_status: Optional[str] = None


class LookupFromStatement(LDLPStatement):
    primary_key: str
    class_name: str
    is_serial: bool = False
    is_secure: bool = False
    is_key_only: bool = False
    multi_command: Optional[str] = None
    gs_status: Optional[str] = None
    statements: SerializeAsAny[List[LDLPStatement]] = []


class LookupEveryStatement(LDLPStatement):
    class_name: str
    is_serial: bool = False
    is_secure: bool = False
    is_key_only: bool = False
    multi_command: Optional[str] = None
    gs_status: Optional[str] = None


class LookupGroupStatement(LDLPStatement):
    class_name: str
    read_order: str
    primary_key: str
    primary_key_final_record: Optional[str] = None
    is_serial: bool = False
    is_secure: bool = False
    is_key_only: bool = False
    multi_command: Optional[str] = None
    gs_status: Optional[str] = None


class AttachStatement(LDLPStatement):
    value: str
    attach_variable: str


class AttachAndSpaceStatement(LDLPStatement):
    value: str
    attach_variable: str


class MessageStatement(LDLPStatement):
    message_type: str
    message: str


class AcceptStatement(LDLPStatement):
    object_name: str


class JumpToStatement(LDLPStatement):
    label: str


class ExtractStatement(LDLPStatement):
    attribute: str
    header: Optional[str] = None
    extract_file: str
    retain_as: Optional[str] = None


class SleepStatement(LDLPStatement):
    suspend_time: Optional[str] = None
    is_no_commit: bool = False


class LabelStatement(LDLPStatement):
    label: str


class CursorStatement(LDLPStatement):
    position: str


class FlagStatement(LDLPStatement):
    source_value: str
    variable: str


class DetachStatement(LDLPStatement):
    value: str
    detach_variable: str
    start_position: Optional[str] = None
    delimiter: Optional[str] = None


class MoveDateStatement(LDLPStatement):
    date_variable: str
    format: Optional[str] = None


class InitializeStatement(LDLPStatement):
    variable: str
    initialization_value: Optional[str] = None


class AbortStatement(LDLPStatement):
    message: Optional[str] = None
    recall_item_name: Optional[str] = None


class ContinueStatement(LDLPStatement):
    pass


class IfStatement(LDLPStatement):
    condition: str
    statements: SerializeAsAny[List[LDLPStatement]] = []
    else_statements: SerializeAsAny[List[LDLPStatement]] = []


class LoopStatement(LDLPStatement):
    condition: Optional[str] = None
    statements: SerializeAsAny[List[LDLPStatement]] = []


class ReturnStatement(LDLPStatement):
    return_value: Optional[str] = None


class RocStatement(LDLPStatement):
    name: str
    roc_command: Optional[str] = None


class StartStatement(LDLPStatement):
    program: str
    parameter: Optional[str] = None


class SendListDynamicStatement(LDLPStatement):
    list_box_name: str
    variable_add_to_list_box: str


class SendListStaticStatement(LDLPStatement):
    list_box_name: str
    download_file: Optional[str] = None
    pack_name: Optional[str] = None
    existing_extract_file: Optional[str] = None


class SendMessageStatement(LDLPStatement):
    receiver: str
    message: str


class SendPrintStatement(LDLPStatement):
    report_name: Optional[str] = None
    device: Optional[str] = None
    output_device: Optional[str] = None
    at_expression: Optional[str] = None


class SetDBStatement(LDLPStatement):
    db_name: str
    class_name: Optional[str] = None
    is_all_classes: bool = False


class SetTitleStatement(LDLPStatement):
    extract_file: str
    name_assign_to_file: str
    pack_name: Optional[str] = None
    is_exist: bool = False


class StnInfoStatement(LDLPStatement):
    name: str
    variable_receive_request_info: str


class SubtractStatement(LDLPStatement):
    minuend: str
    subtrahend: str
    results: str
    is_rounded: bool = False
    gs_status: Optional[str] = None


class SwitchToStatement(LDLPStatement):
    destination_system_name: str
    data_pass_to_target_system: Optional[str] = None
    partition_name: Optional[str] = None
    is_log_off_from_origin_application: bool = False
    is_clear: bool = False
    is_inherit: bool = False


class WakeStatement(LDLPStatement):
    report_name: str
    data_pass_to_report: Optional[str] = None
    gs_status: Optional[str] = None


class RunStatement(LDLPStatement):
    report_name: str
    output_device: Optional[str] = None
    is_trace: bool = False
    initial_language: Optional[str] = None
    parameter: Optional[str] = None


class CriticalPointStatement(LDLPStatement):
    suspend_time: Optional[str] = None
    is_no_release: bool = False


class EndUseStatement(LDLPStatement):
    class_name: str


class ExcludeStatement(LDLPStatement):
    class_name: str


class LoadStatement(LDLPStatement):
    length: str
    ispec_attribute: str


class MatchStatement(LDLPStatement):
    compare_type: str
    extract_files: List[str]
    gs_status: Optional[str] = None


class AttributeStatement(LDLPStatement):
    bdname_attribute: str
    user_code: Optional[str] = None
    gs_status: Optional[str] = None


class BeginPageStatement(LDLPStatement):
    is_clear: bool = False
    heading_frame_name: Optional[str] = None
    output_stream: Optional[str] = None


class OnChangeStatement(LDLPStatement):
    controlling_variable: str
    as_literal: str
    footer_frame_name: Optional[str] = None
    footer_line_number: Optional[str] = None
    headerframe_name: Optional[str] = None
    header_line_number: Optional[str] = None
    routine_call: Optional[str] = None


class PageStatement(LDLPStatement):
    destination_page_number: str
    variable_to_destination_page: str


class ReleaseStatement(LDLPStatement):
    report_name: Optional[str] = None


class RestartStatement(LDLPStatement):
    profile_name: str


class LogStatement(LDLPStatement):
    mode: str
    level: Optional[str] = None
    messages: List[str]


class MoveTimeStatement(LDLPStatement):
    variable: str


class FunctionCallingStatement(LDLPStatement):
    function_name: str
    params: List[str] = []
