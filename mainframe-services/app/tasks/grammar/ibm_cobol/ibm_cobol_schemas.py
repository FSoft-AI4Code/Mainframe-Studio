from typing import List, Literal, Optional, Union

from pydantic import BaseModel, SerializeAsAny

from app.tasks.grammar.common.base_cobol_schemas import Statement


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

    call_identifiers: List[str] = []
    call_literal: Optional[str] = None
    using_identifiers: List[str] = []
    using_literals: List[str] = []
    giving_identifier: Optional[str] = None


class CloseStatement(Statement):
    """Close statement in COBOL"""

    file_name_1: List[str] = []


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

    evaluateAlsoSelect: List[str] = []
    evaluateWhenPhrase: List[EvaluateWhenPhrase] = []
    evaluateWhenOther: List[str] = []


class CommandBody(BaseModel):
    parameterName: str
    parameterValue: str


class ExecCicsStatement2(Statement):
    """CICS statement in COBOL"""

    commandName: str
    commandBody: List[CommandBody] = []


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
    inspect_by: InspectBy
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

    identifier_1: Optional[str] = None
    literal_1: Optional[str] = None
    identifier_2: List[str] = []
    literal_2: List[str] = []


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

    record_name_1: str
    invalidKeyPhrase: SerializeAsAny[List[Statement]] = []
    notInvalidKeyPhrase: SerializeAsAny[List[Statement]] = []


class StringSendingPhrase(BaseModel):
    identifier_1: List[str] = []
    literal_1: List[str] = []
    identifier_2: Optional[str] = None
    literal_2: Optional[str] = None


class StringStatement(Statement):
    """String statement in COBOL"""

    stringSendingPhrase: List[StringSendingPhrase] = []
    literal_3: List[str] = []


class SubtractStatement(Statement):
    """Substract statement in COBOL"""

    identifier_1: List[str] = []
    literal_1: List[str] = []
    identifier_2: List[str] = []


class SetTo(BaseModel):
    identifier_1: List[str] = []
    identifier_2: Optional[str] = None
    literal_2: Optional[str] = None


class SetStatement(Statement):
    """Set statement in COBOL"""

    setToStatement: List[SetTo] = []


class OpenFile(BaseModel):
    file_name: str
    open_type: Literal["INPUT", "OUTPUT", "IO", "EXTEND"]
    on_exception_clause: SerializeAsAny[List[Statement]] = []


class OpenStatement(Statement):
    """Open statement in COBOL"""

    open_files: List[OpenFile] = []


class FindStatement(Statement):
    """Find statement in COBOL"""


class AttachStatement(Statement):
    """Attach statement in COBOL"""


class ChangeStatement(Statement):
    """Change statement in COBOL"""


class CreateStatement(Statement):
    """Create statement in COBOL"""


class FreeStatement(Statement):
    """Free statement in COBOL"""


class LockStatement(Statement):
    """Lock statement in COBOL"""


class ModifyStatement(Statement):
    """Modify statement in COBOL"""


class StoreStatement(Statement):
    """Store statement in COBOL"""


class TransactionStatement(Statement):
    """Transaction statement in COBOL"""


class WaitStatement(Statement):
    """Wait statement in COBOL"""


class WriteStatement(Statement):
    """Write statement in COBOL"""


class StopStatement(Statement):
    """Stop statement in COBOL"""


class IBMStatementFactory:
    @staticmethod
    def from_dict(data: dict) -> Statement:
        tag = data.get("tag", None)

        if tag is None:
            raise ValueError(f"Tag not found in statement {data}")

        schema_dict = {
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
            "OpenStatement": OpenStatement,
            "FindStatement": FindStatement,
            "AttachStatement": AttachStatement,
            "ChangeStatement": ChangeStatement,
            "CreateStatement": CreateStatement,
            "FreeStatement": FreeStatement,
            "LockStatement": LockStatement,
            "ModifyStatement": ModifyStatement,
            "StoreStatement": StoreStatement,
            "StopStatement": StopStatement,
            "TransactionStatement": TransactionStatement,
            "WaitStatement": WaitStatement,
            "WriteStatement": WriteStatement,
        }

        schema = schema_dict.get(tag, Statement)
        statement = schema(**data)

        # correctly instantiate the subclass of Statement in the statement
        # cannot use **data because the type will be Statement instead of subclass of Statement
        if isinstance(statement, EvaluateStatement):
            evaluate_when_phrases = data.get("evaluateWhenPhrase", [])
            for i, phrase in enumerate(evaluate_when_phrases):
                statement_dict_list = phrase.get("statement", [])
                for j, statement_dict in enumerate(statement_dict_list):
                    statement.evaluateWhenPhrase[i].statement[j] = (
                        IBMStatementFactory.from_dict(statement_dict)
                    )

        if isinstance(statement, IfStatement):
            if_then = data.get("ifThen", [])
            for i, statement_dict in enumerate(if_then):
                statement.ifThen[i] = IBMStatementFactory.from_dict(statement_dict)
            if_else = data.get("ifElse", [])
            for i, statement_dict in enumerate(if_else):
                statement.ifElse[i] = IBMStatementFactory.from_dict(statement_dict)

        if isinstance(statement, PerformStatement):
            perform_inline = data.get("performInlineStatement", None)
            if perform_inline:
                statement.performInlineStatement = PerformInline(**perform_inline)
                perform_inline_statement = perform_inline.get("statement", [])
                for i, statement_dict in enumerate(perform_inline_statement):
                    statement.performInlineStatement.statement[i] = (
                        IBMStatementFactory.from_dict(statement_dict)
                    )

        if isinstance(statement, ReadStatement):
            invalid_key_phrase = data.get("invalid_key_phrase", [])
            for i, statement_dict in enumerate(invalid_key_phrase):
                statement.invalid_key_phrase[i] = IBMStatementFactory.from_dict(
                    statement_dict
                )
            not_invalid_key_phrase = data.get("not_invalid_key_phrase", [])
            for i, statement_dict in enumerate(not_invalid_key_phrase):
                statement.not_invalid_key_phrase[i] = IBMStatementFactory.from_dict(
                    statement_dict
                )
            at_end_phrase = data.get("at_end_phrase", [])
            for i, statement_dict in enumerate(at_end_phrase):
                statement.at_end_phrase[i] = IBMStatementFactory.from_dict(
                    statement_dict
                )
            not_at_end_phrase = data.get("not_at_end_phrase", [])
            for i, statement_dict in enumerate(not_at_end_phrase):
                statement.not_at_end_phrase[i] = IBMStatementFactory.from_dict(
                    statement_dict
                )

        if isinstance(statement, OpenStatement):
            open_files = data.get("open_files", [])
            for i, file_dict in enumerate(open_files):
                statement.open_files[i] = OpenFile(**file_dict)
                on_exception_clause = file_dict.get("on_exception_clause", [])
                for j, statement_dict in enumerate(on_exception_clause):
                    statement.open_files[i].on_exception_clause[j] = (
                        IBMStatementFactory.from_dict(statement_dict)
                    )

        if isinstance(statement, RewriteStatement):
            invalid_key_phrase = data.get("invalidKeyPhrase", [])
            for i, statement_dict in enumerate(invalid_key_phrase):
                statement.invalidKeyPhrase[i] = IBMStatementFactory.from_dict(
                    statement_dict
                )
            not_invalid_key_phrase = data.get("notInvalidKeyPhrase", [])
            for i, statement_dict in enumerate(not_invalid_key_phrase):
                statement.notInvalidKeyPhrase[i] = IBMStatementFactory.from_dict(
                    statement_dict
                )

        return statement
