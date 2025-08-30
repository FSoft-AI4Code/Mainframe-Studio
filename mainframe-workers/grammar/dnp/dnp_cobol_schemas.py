from typing import List, Literal, Optional, Union

from pydantic import BaseModel, SerializeAsAny

from grammar.common.base_cobol_schemas import Statement


class AcceptStatement(Statement):
    """Accept statement in COBOL"""

    identifier: str
    on_exception_clause: SerializeAsAny[List[Statement]] = []
    not_on_exception_clause: SerializeAsAny[List[Statement]] = []


class AcceptFromDateStatement(AcceptStatement):
    """Accept statement in COBOL for dates"""

    datetime: str


class AcceptFromMnemonicStatement(AcceptStatement):
    """Accept statement in COBOL for mnemonics"""

    mnemonic_name: str


class AcceptMessageCountStatement(AcceptStatement):
    """Accept statement in COBOL for message count"""


class AcceptEscapeKeyStatement(AcceptStatement):
    """Accept statement in COBOL for escape key"""


class AddStatement(Statement):
    """Add statement in COBOL"""

    identifier_1: List[str] = []
    literal_1: List[str] = []
    identifier_2: List[str] = []
    literal_2: List[str] = []
    identifier_3: List[str] = []
    literal_3: List[str] = []


class AlterProcedure(BaseModel):

    procedure_name_1: str
    procedure_name_2: str


class AlterStatement(Statement):
    """Alter statement in COBOL"""

    alterProceedTo: List[AlterProcedure] = []


class CallStatement(Statement):
    """Call statement in COBOL"""

    call_type: Optional[Literal["SYSTEM", "USING"]] = None
    call_identifiers: List[str] = []
    call_literal: Optional[str] = None
    using_identifiers: List[str] = []
    using_literals: List[str] = []
    giving_identifier: Optional[str] = None


class CommandBody(BaseModel):
    parameterName: str
    parameterValue: str


class ExecCicsStatement2(Statement):
    """CICS statement in COBOL"""

    commandName: str
    commandBody: List[CommandBody] = []


class CloseFile(BaseModel):
    file_name: str
    close_option: Optional[str] = None
    on_exception_clause: SerializeAsAny[List[Statement]] = []


class CloseStatement(Statement):
    """Close statement in COBOL"""

    close_files: List[CloseFile] = []


class ComputeStatement(Statement):
    """Compute statement in COBOL"""

    identifier_1: List[str] = []
    arithmetic_expression: str


class ContinueStatement(Statement):
    """Continue statement in COBOL"""


class ReplacePhrase(BaseModel):
    """Replace phrase in COBOL"""

    partial_word_1: str
    partial_word_2: str


class CopyStatement(Statement):
    """Copy statement in COBOL"""

    literal_1: Optional[str] = None
    text_name: Optional[str] = None
    replaceingPhrase: List[ReplacePhrase] = []


class DisplayStatement(Statement):
    """Display statement in COBOL"""

    identifier_1: List[str] = []
    literal_1: List[str] = []


class EvaluateWhenPhrase(BaseModel):
    evaluateWhen: List[str] = []
    statement: SerializeAsAny[List[Statement]] = []


class EvaluateStatement(Statement):
    """Evaluate statement in COBOL"""

    evaluate_identifier: Optional[str] = None
    evaluate_literal: Optional[str] = None
    evaluateAlsoSelect: List[str] = []
    evaluateWhenPhrase: List[EvaluateWhenPhrase] = []
    evaluateWhenOther: List[str] = []


class ExitStatement(Statement):
    """Exit statement in COBOL"""


class GobackStatement(Statement):
    """Go back statement in COBOL"""


class GoToStatement(Statement):
    """Goto statement in COBOL"""

    procedure_name_1: str


class IfStatement(Statement):
    """If statement in COBOL"""

    condition: str
    ifThen: SerializeAsAny[List[Statement]] = []
    ifElse: SerializeAsAny[List[Statement]] = []


class InitializeStatement(Statement):
    """Initialize statement in COBOL"""

    identifier_1: List[str] = []


class InspectBeforeAfter(BaseModel):
    position: Literal["BEFORE", "AFTER"]
    replacing_identifier: Optional[str] = None
    replacing_literal: Optional[str] = None


class InspectCharacters(BaseModel):
    before_after: List[InspectBeforeAfter] = []
    inspect_type: Literal["CHARACTERS"] = "CHARACTERS"


class InspectAllLeading(BaseModel):
    identifier: Optional[str] = None
    literal: Optional[str] = None
    before_after: List[InspectBeforeAfter] = []


class InspectAllLeadings(BaseModel):
    leading_type: Literal["ALL", "LEADING"]
    inspect_all_leading: List[InspectAllLeading] = []


class InspectFor(BaseModel):
    identifier: str
    for_targets: List[Union[InspectCharacters, InspectAllLeadings]] = []


class InspectBy(BaseModel):
    by_identifier: Optional[str] = None
    by_literal: Optional[str] = None


class InspectTo(BaseModel):
    to_identifier: Optional[str] = None
    to_literal: Optional[str] = None


class InspectReplacingCharacters(BaseModel):
    by: InspectBy
    before_after: List[InspectBeforeAfter] = []


class InspectReplacingAllLeading(BaseModel):
    replacing_identifier: Optional[str] = None
    replacing_literal: Optional[str] = None
    inspect_by: List[InspectBy] = []
    before_after: List[InspectBeforeAfter] = []


class InspectReplacingAllLeadings(BaseModel):
    leading_type: Literal["ALL", "LEADING", "FIRST"]
    replacements: List[InspectReplacingAllLeading]


class InspectReplacingPhrase(BaseModel):
    inspect_type: Literal["REPLACING"] = "REPLACING"
    replacements: List[Union[InspectReplacingCharacters, InspectReplacingAllLeadings]]


class InspectTallyingPhrase(BaseModel):
    inspect_type: Literal["TALLYING"] = "TALLYING"
    tallying: List[InspectFor]


class InspectTallyingReplacingPhrase(BaseModel):
    inspect_type: Literal["TALLYING_REPLACING"] = "TALLYING_REPLACING"
    tallying: List[InspectFor]
    replacing: List[InspectReplacingPhrase]


class InspectConvertingPhrase(BaseModel):
    inspect_type: Literal["CONVERTING"] = "CONVERTING"
    converting_from_identifier: Optional[str] = None
    converting_from_literal: Optional[str] = None
    to: InspectTo
    before_after: List[InspectBeforeAfter] = []


class InspectStatement(Statement):
    identifier: str
    phrase: Union[
        InspectTallyingPhrase,
        InspectReplacingPhrase,
        InspectTallyingReplacingPhrase,
        InspectConvertingPhrase,
    ]


class MoveStatement(Statement):
    """Move statement in COBOL"""

    move_option: Optional[Literal["ALL", "ATTRIBUTE"]] = None
    move_type: Literal["TO", "CORRESPONDING"]
    move_from: str  # full FROM phrase
    from_identifier: Optional[str] = None
    from_literal: Optional[str] = None
    move_to: str  # full TO phrase
    to_identifiers: List[str] = []


class PerformInline(BaseModel):
    performType: str
    statement: SerializeAsAny[List[Statement]] = []


class PerformStatement(Statement):
    """Perform statement in COBOL"""

    sub_tags: List[str] = []
    procedure_name_1: Optional[str] = None
    procedure_name_2: Optional[str] = None
    loop_times: Optional[str] = None
    condition: Optional[str] = None
    varying_variable: Optional[str] = None
    varying_from: Optional[str] = None
    varying_by: Optional[str] = None
    performInlineStatement: Optional[PerformInline] = None


class ReadStatement(Statement):
    """Read statement in COBOL"""

    fileName: str
    next_record: bool = False  # set to true if has NEXT
    read_into_identifier: Optional[str] = None
    read_with: Optional[Literal["KEPT LOCK", "KEPT WAIT", "NO LOCK", "NO WAIT"]] = None
    read_key: Optional[str] = None
    invalid_key_phrase: SerializeAsAny[List[Statement]] = []
    not_invalid_key_phrase: SerializeAsAny[List[Statement]] = []
    at_end_phrase: SerializeAsAny[List[Statement]] = []
    not_at_end_phrase: SerializeAsAny[List[Statement]] = []


class RewriteStatement(Statement):
    """Rewrite statement in COBOL"""

    record_name: str
    rewrite_from_identifier: Optional[str] = None
    invalid_key_phrase: SerializeAsAny[List[Statement]] = []
    not_invalid_key_phrase: SerializeAsAny[List[Statement]] = []


class SearchWhen(BaseModel):
    condition: str
    statements: SerializeAsAny[List[Statement]] = []


class SearchStatement(Statement):
    """Search statement in COBOL"""

    is_all: bool = False
    record_name: str
    varying_record_name: Optional[str] = None
    condition: Optional[str] = None
    when: List[SearchWhen] = []
    at_end_phrase: SerializeAsAny[List[Statement]] = []


class StringSendingPhrase(BaseModel):
    source_identifiers: List[str] = []
    source_literals: List[str] = []
    delimiter_identifier: Optional[str] = None
    delimiter_literal: Optional[str] = None


class StringStatement(Statement):
    """String statement in COBOL"""

    stringSendingPhrase: List[StringSendingPhrase] = []
    destination_identifier: str
    pointer_name: Optional[str] = None
    on_overflow_phrase: SerializeAsAny[List[Statement]] = []
    not_on_overflow_phrase: SerializeAsAny[List[Statement]] = []


class Operand(BaseModel):
    identifier: Optional[str] = None
    literal: Optional[str] = None


class DifferenceResult(BaseModel):
    identifier: str
    is_rounded: bool = False


class SubtractStatement(Statement):
    """Substract statement in COBOL"""

    minuends: List[Operand] = []
    subtrahends: List[Operand] = []
    results: List[DifferenceResult] = []
    on_size_error_phrase: SerializeAsAny[List[Statement]] = []
    not_on_size_error_phrase: SerializeAsAny[List[Statement]] = []


class SetTo(BaseModel):
    source_identifier: List[str] = []
    target_identifier: Optional[str] = None
    target_literal: Optional[str] = None


class SetUpDown(BaseModel):
    source_identifier: List[str] = []
    by_identifier: Optional[str] = None
    by_literal: Optional[str] = None


class SetStatement(Statement):
    """Set statement in COBOL"""

    set_type: Literal["TO", "UP", "DOWN"]
    set_to: List[SetTo] = []
    set_up_down: Optional[SetUpDown] = None


class OpenFile(BaseModel):
    file_name: str
    open_type: Literal["INPUT", "OUTPUT", "IO", "INQUIRY", "EXTEND", "UPDATE"]
    on_exception_clause: SerializeAsAny[List[Statement]] = []


class OpenStatement(Statement):
    """Open statement in COBOL"""

    open_files: List[OpenFile] = []


class FindStatement(Statement):
    """Find statement in COBOL"""

    find_option: List[Literal["NEXT", "FIRST", "LAST", "PRIOR", "KEY OF"]] = []
    record_name: str
    via_find_option: Optional[str] = None
    via_identifier: Optional[str] = None
    condition: Optional[str] = None
    on_exception_clause: SerializeAsAny[List[Statement]] = []


class AttachStatement(Statement):
    """Attach statement in COBOL"""

    section_name: str
    event_identifier: str


class CancelStatement(Statement):
    """Cancel statement in COBOL"""

    identifier: str
    literal: str


class ChangeStatement(Statement):
    """Change statement in COBOL"""

    attribute_type: Literal["FILE", "LIBRARY"]
    source_identifier: Optional[str] = None
    source_literal: Optional[str] = None
    source_option: Optional[str] = None
    library_name: Optional[str] = None
    target_identifier: Optional[str] = None
    target_literal: Optional[str] = None
    target_option: Optional[str] = None


class CreateStatement(Statement):
    """Create statement in COBOL"""

    create_type: Literal["CREATE", "RECREATE"]
    identifier: str
    on_exception_clause: List[Statement] = []


class DeleteStatement(Statement):
    """Delete statement in COBOL"""

    file_name: str
    invalid_key_phrase: List[Statement] = []
    not_invalid_key_phrase: List[Statement] = []
    on_exception_clause: List[Statement] = []


class DisableStatement(Statement):
    """Disable statement in COBOL"""

    type: str
    identifier: str
    key: str


class DivideStatement(Statement):
    """Divide statement in COBOL"""

    divide_type: Literal["INTO", "BY"]
    dividend_identifiers: List[str] = []
    dividend_literal: Optional[str] = None
    divisor_identifier: Optional[str] = None
    divisor_literal: Optional[str] = None
    results: List[str] = []
    remainder_identifier: Optional[str] = None
    on_size_error_phrase: List[Statement] = []
    not_on_size_error_phrase: List[Statement] = []


class EnableStatement(Statement):
    """Enable statement in COBOL"""

    type: str
    identifier: str
    key: str


class ExhibitStatement(Statement):
    """Exhibit statement in COBOL"""

    identifier: List[str] = []
    literal: List[str] = []
    type: Optional[str] = None


class GenerateStatement(Statement):
    """Generate statement in COBOL"""

    report_name: str


class InitiateStatement(Statement):
    """Initiate statement in COBOL"""

    report_names: List[str] = []


class MergeStatement(Statement):
    """Merge statement in COBOL"""

    file_name: str
    merge_key: List[str] = []
    merge_collating: Optional[str] = None
    merge_using_file_names: List[str] = []
    output_procedure_name: Optional[str] = None
    merge_giving_file_name: Optional[str] = None
    merge_giving_option: Optional[str] = None


class FreeStatement(Statement):
    """Free statement in COBOL"""

    identifier: str
    on_exception_clause: SerializeAsAny[List[Statement]] = []


class LockStatement(Statement):
    """Lock statement in COBOL"""

    lock_type: Optional[Literal["FIRST", "NEXT"]]
    database_name: str
    via_identifier: Optional[str] = None
    lock_option: Optional[str] = None
    condition: Optional[str] = None
    on_exception_clause: SerializeAsAny[List[Statement]] = []


class ModifyStatement(Statement):
    """Modify statement in COBOL"""

    file_name: str
    modify_to: Optional[str] = None
    condition: Optional[str] = None
    on_exception_clause: SerializeAsAny[List[Statement]] = []


class StoreStatement(Statement):
    """Store statement in COBOL"""

    database_name: str
    on_exception_clause: SerializeAsAny[List[Statement]] = []


class TransactionDetails(BaseModel):
    audit_option: Optional[Literal["AUDIT", "NO-AUDIT"]] = None
    database_name: str
    sync: bool = False
    on_exception_clause: SerializeAsAny[List[Statement]]


class TransactionStatement(Statement):
    """Transaction statement in COBOL"""

    transaction_type: Literal["BEGIN", "END", "CANCEL"]
    transaction_details: Optional[TransactionDetails] = None


class WaitStatement(Statement):
    """Wait statement in COBOL"""

    is_reset: bool = False
    is_wait_until: bool = False
    option: str
    identifier: Optional[str] = None
    literal: Optional[str] = None
    using_data_names: List[str] = []
    giving_data_name: Optional[str] = None


class WriteFromPhrase(BaseModel):
    identifier: Optional[str] = None
    literal: Optional[str] = None


class WriteAdvancingLines(BaseModel):
    identifier: Optional[str] = None
    literal: Optional[str] = None


class WriteAdvancingMnemonic(BaseModel):
    mnemonic_name: str  # Placeholder for mnemonic name


class WriteAdvancingPhrase(BaseModel):
    position: Literal["BEFORE", "AFTER"]
    advancing_type: Optional[Literal["ADVANCING", "CHANNEL"]] = None
    advancing: Union[Literal["PAGE"], WriteAdvancingLines, WriteAdvancingMnemonic]


class WriteStatement(Statement):
    """Write statement in COBOL"""

    record_name: str
    write_from_phrase: Optional[WriteFromPhrase] = None
    write_advancing_phrase: Optional[WriteAdvancingPhrase] = None
    write_at_end_of_page_phrase: SerializeAsAny[List[Statement]] = []
    write_not_at_end_of_page_phrase: SerializeAsAny[List[Statement]] = []
    invalid_key_phrase: SerializeAsAny[List[Statement]] = []
    not_invalid_key_phrase: SerializeAsAny[List[Statement]] = []


class DNPStatementFactory:
    @staticmethod
    def from_dict(data: dict) -> Statement:
        tag = data.get("tag", None)

        if tag is None:
            raise ValueError(f"Tag not found in statement {data}")

        schema_dict = {
            "AcceptStatement": AcceptStatement,
            "AcceptFromDateStatement": AcceptFromDateStatement,
            "AcceptFromMnemonicStatement": AcceptFromMnemonicStatement,
            "AcceptMessageCountStatement": AcceptMessageCountStatement,
            "AcceptEscapeKeyStatement": AcceptEscapeKeyStatement,
            "AddStatement": AddStatement,
            "AlterStatement": AlterStatement,
            "CallStatement": CallStatement,
            "CloseStatement": CloseStatement,
            "ComputeStatement": ComputeStatement,
            "ContinueStatement": ContinueStatement,
            "CopyStatement": CopyStatement,
            "DisplayStatement": DisplayStatement,
            "EvaluateStatement": EvaluateStatement,
            "ExecCicsStatement2": ExecCicsStatement2,
            "ExitStatement": ExitStatement,
            "GobackStatement": GobackStatement,
            "GoToStatement": GoToStatement,
            "IfStatement": IfStatement,
            "InitializeStatement": InitializeStatement,
            "InspectStatement": InspectStatement,
            "MoveStatement": MoveStatement,
            "PerformStatement": PerformStatement,
            "ReadStatement": ReadStatement,
            "RewriteStatement": RewriteStatement,
            "StringStatement": StringStatement,
            "SubtractStatement": SubtractStatement,
            "SetStatement": SetStatement,
            "SearchStatement": SearchStatement,
            "OpenStatement": OpenStatement,
            "FindStatement": FindStatement,
            "AttachStatement": AttachStatement,
            "ChangeStatement": ChangeStatement,
            "CreateStatement": CreateStatement,
            "FreeStatement": FreeStatement,
            "LockStatement": LockStatement,
            "ModifyStatement": ModifyStatement,
            "StoreStatement": StoreStatement,
            "TransactionStatement": TransactionStatement,
            "WaitStatement": WaitStatement,
            "WriteStatement": WriteStatement,
        }

        schema = schema_dict.get(tag, Statement)
        statement = schema(**data)

        # correctly instantiate the subclass of Statement in the statement
        # cannot use **data because the type will be Statement instead of subclass of Statement

        if isinstance(statement, AcceptStatement):
            on_exception_clause = data.get("on_exception_clause", [])
            for i, statement_dict in enumerate(on_exception_clause):
                statement.on_exception_clause[i] = DNPStatementFactory.from_dict(
                    statement_dict
                )
            not_on_exception_clause = data.get("not_on_exception_clause", [])
            for i, statement_dict in enumerate(not_on_exception_clause):
                statement.not_on_exception_clause[i] = DNPStatementFactory.from_dict(
                    statement_dict
                )

        if isinstance(statement, CloseStatement):
            close_files = data.get("close_files", [])
            for i, file_dict in enumerate(close_files):
                statement.close_files[i] = CloseFile(**file_dict)
                on_exception_clause = file_dict.get("on_exception_clause", [])
                for j, statement_dict in enumerate(on_exception_clause):
                    statement.close_files[i].on_exception_clause[j] = (
                        DNPStatementFactory.from_dict(statement_dict)
                    )

        if isinstance(statement, EvaluateStatement):
            evaluate_when_phrases = data.get("evaluateWhenPhrase", [])
            for i, phrase in enumerate(evaluate_when_phrases):
                statement_dict_list = phrase.get("statement", [])
                for j, statement_dict in enumerate(statement_dict_list):
                    statement.evaluateWhenPhrase[i].statement[j] = (
                        DNPStatementFactory.from_dict(statement_dict)
                    )

        if isinstance(statement, FindStatement):
            on_exception_clause = data.get("on_exception_clause", [])
            for i, statement_dict in enumerate(on_exception_clause):
                statement.on_exception_clause[i] = DNPStatementFactory.from_dict(
                    statement_dict
                )

        if isinstance(statement, FreeStatement):
            on_exception_clause = data.get("on_exception_clause", [])
            for i, statement_dict in enumerate(on_exception_clause):
                statement.on_exception_clause[i] = DNPStatementFactory.from_dict(
                    statement_dict
                )

        if isinstance(statement, LockStatement):
            on_exception_clause = data.get("on_exception_clause", [])
            for i, statement_dict in enumerate(on_exception_clause):
                statement.on_exception_clause[i] = DNPStatementFactory.from_dict(
                    statement_dict
                )

        if isinstance(statement, ModifyStatement):
            on_exception_clause = data.get("on_exception_clause", [])
            for i, statement_dict in enumerate(on_exception_clause):
                statement.on_exception_clause[i] = DNPStatementFactory.from_dict(
                    statement_dict
                )

        if isinstance(statement, OpenStatement):
            open_files = data.get("open_files", [])
            for i, file_dict in enumerate(open_files):
                statement.open_files[i] = OpenFile(**file_dict)
                on_exception_clause = file_dict.get("on_exception_clause", [])
                for j, statement_dict in enumerate(on_exception_clause):
                    statement.open_files[i].on_exception_clause[j] = (
                        DNPStatementFactory.from_dict(statement_dict)
                    )

        if isinstance(statement, IfStatement):
            if_then = data.get("ifThen", [])
            for i, statement_dict in enumerate(if_then):
                statement.ifThen[i] = DNPStatementFactory.from_dict(statement_dict)
            if_else = data.get("ifElse", [])
            for i, statement_dict in enumerate(if_else):
                statement.ifElse[i] = DNPStatementFactory.from_dict(statement_dict)

        if isinstance(statement, PerformStatement):
            perform_inline = data.get("performInlineStatement", None)
            if perform_inline:
                statement.performInlineStatement = PerformInline(**perform_inline)
                perform_inline_statement = perform_inline.get("statement", [])
                for i, statement_dict in enumerate(perform_inline_statement):
                    statement.performInlineStatement.statement[i] = (
                        DNPStatementFactory.from_dict(statement_dict)
                    )

        if isinstance(statement, ReadStatement):
            invalid_key_phrase = data.get("invalid_key_phrase", [])
            for i, statement_dict in enumerate(invalid_key_phrase):
                statement.invalid_key_phrase[i] = DNPStatementFactory.from_dict(
                    statement_dict
                )
            not_invalid_key_phrase = data.get("not_invalid_key_phrase", [])
            for i, statement_dict in enumerate(not_invalid_key_phrase):
                statement.not_invalid_key_phrase[i] = DNPStatementFactory.from_dict(
                    statement_dict
                )
            at_end_phrase = data.get("at_end_phrase", [])
            for i, statement_dict in enumerate(at_end_phrase):
                statement.at_end_phrase[i] = DNPStatementFactory.from_dict(
                    statement_dict
                )
            not_at_end_phrase = data.get("not_at_end_phrase", [])
            for i, statement_dict in enumerate(not_at_end_phrase):
                statement.not_at_end_phrase[i] = DNPStatementFactory.from_dict(
                    statement_dict
                )

        if isinstance(statement, RewriteStatement):
            invalid_key_phrase = data.get("invalid_key_phrase", [])
            for i, statement_dict in enumerate(invalid_key_phrase):
                statement.invalid_key_phrase[i] = DNPStatementFactory.from_dict(
                    statement_dict
                )
            not_invalid_key_phrase = data.get("not_invalid_key_phrase", [])
            for i, statement_dict in enumerate(not_invalid_key_phrase):
                statement.not_invalid_key_phrase[i] = DNPStatementFactory.from_dict(
                    statement_dict
                )

        if isinstance(statement, SearchStatement):
            when = data.get("when", [])
            for i, when_dict in enumerate(when):
                statement.when[i] = SearchWhen(**when_dict)

                when_statements = when_dict.get("statements", [])
                for j, statement_dict in enumerate(when_statements):
                    statement.when[i].statements[j] = DNPStatementFactory.from_dict(
                        statement_dict
                    )

            at_end_phrase = data.get("at_end_phrase", [])
            for i, statement_dict in enumerate(at_end_phrase):
                statement.at_end_phrase[i] = DNPStatementFactory.from_dict(
                    statement_dict
                )

        if isinstance(statement, StoreStatement):
            on_exception_clause = data.get("on_exception_clause", [])
            for i, statement_dict in enumerate(on_exception_clause):
                statement.on_exception_clause[i] = DNPStatementFactory.from_dict(
                    statement_dict
                )

        if isinstance(statement, StringStatement):
            on_overflow_phrase = data.get("on_overflow_phrase", [])
            for i, statement_dict in enumerate(on_overflow_phrase):
                statement.on_overflow_phrase[i] = DNPStatementFactory.from_dict(
                    statement_dict
                )
            not_on_overflow_phrase = data.get("not_on_overflow_phrase", [])
            for i, statement_dict in enumerate(not_on_overflow_phrase):
                statement.not_on_overflow_phrase[i] = DNPStatementFactory.from_dict(
                    statement_dict
                )

        if isinstance(statement, SubtractStatement):
            on_size_error_phrase = data.get("on_size_error_phrase", [])
            for i, statement_dict in enumerate(on_size_error_phrase):
                statement.on_size_error_phrase[i] = DNPStatementFactory.from_dict(
                    statement_dict
                )
            not_on_size_error_phrase = data.get("not_on_size_error_phrase", [])
            for i, statement_dict in enumerate(not_on_size_error_phrase):
                statement.not_on_size_error_phrase[i] = DNPStatementFactory.from_dict(
                    statement_dict
                )

        if isinstance(statement, TransactionStatement):
            transaction_details = data.get("transaction_details", None)
            if transaction_details:
                statement.transaction_details = TransactionDetails(
                    **transaction_details
                )
                on_exception_clause = transaction_details.get("on_exception_clause", [])
                for i, statement_dict in enumerate(on_exception_clause):
                    statement.transaction_details.on_exception_clause[i] = (
                        DNPStatementFactory.from_dict(statement_dict)
                    )

        if isinstance(statement, WriteStatement):
            write_at_end_of_page_phrase = data.get("write_at_end_of_page_phrase", [])
            for i, statement_dict in enumerate(write_at_end_of_page_phrase):
                statement.write_at_end_of_page_phrase[i] = (
                    DNPStatementFactory.from_dict(statement_dict)
                )
            write_not_at_end_of_page_phrase = data.get(
                "write_not_at_end_of_page_phrase", []
            )
            for i, statement_dict in enumerate(write_not_at_end_of_page_phrase):
                statement.write_not_at_end_of_page_phrase[i] = (
                    DNPStatementFactory.from_dict(statement_dict)
                )
            invalid_key_phrase = data.get("invalid_key_phrase", [])
            for i, statement_dict in enumerate(invalid_key_phrase):
                statement.invalid_key_phrase[i] = DNPStatementFactory.from_dict(
                    statement_dict
                )
            not_invalid_key_phrase = data.get("not_invalid_key_phrase", [])
            for i, statement_dict in enumerate(not_invalid_key_phrase):
                statement.not_invalid_key_phrase[i] = DNPStatementFactory.from_dict(
                    statement_dict
                )

        return statement
