import traceback
from typing import List

from antlr4.tree.Tree import TerminalNodeImpl
from loguru import logger

from grammar.ldlp.ldlp_schemas import (
    AbortStatement,
    AcceptStatement,
    AccessExtStatement,
    AddStatement,
    AdvanceStatement,
    Assignment,
    AttachAndSpaceStatement,
    AttachStatement,
    AttributeStatement,
    BeginPageStatement,
    BreakStatement,
    Case,
    CaseStatement,
    ComputeStatement,
    ContinueStatement,
    CriticalPointStatement,
    CursorStatement,
    DateConvertStatement,
    DetachStatement,
    DetermineActualStatement,
    DetermineBackStatement,
    DetermineEveryStatement,
    DetermineFromStatement,
    DetermineGroupStatement,
    DetermineLastStatement,
    DetermineTotalStatement,
    DivideStatement,
    DowhenStatement,
    EndUseStatement,
    ExcludeStatement,
    ExtractStatement,
    FlagStatement,
    FunctionCallingStatement,
    IfStatement,
    InitializeStatement,
    InsertStatement,
    JumpToStatement,
    LabelStatement,
    LDLPStatement,
    LoadStatement,
    LogStatement,
    LookupBaseStatement,
    LookupEveryStatement,
    LookupFromStatement,
    LookupGroupStatement,
    LoopStatement,
    MatchStatement,
    MessageStatement,
    MoveDateStatement,
    MoveStatement,
    MoveTimeStatement,
    MultiplyStatement,
    OnChangeStatement,
    PageStatement,
    RecallStatement,
    ReleaseStatement,
    RestartStatement,
    ReturnStatement,
    RocStatement,
    RunStatement,
    SendListDynamicStatement,
    SendListStaticStatement,
    SendMessageStatement,
    SendPrintStatement,
    SetDBStatement,
    SetTitleStatement,
    SleepStatement,
    StartStatement,
    StnInfoStatement,
    SubtractStatement,
    SwitchToStatement,
    WakeStatement,
)
from grammar.ldlp.LDLPParser import LDLPParser
from grammar.ldlp.LDLPVisitor import LDLPVisitor
from grammar.utils import get_original_code_content


class LDLPVisitorImp(LDLPVisitor):

    def __init__(self):
        self.statements: List[LDLPStatement] = []
        self.func = {
            "MoveStatementContext": self.assessMoveStatement,
            "AssignmentContext": self.assessAssignment,
            "DowhenStatementContext": self.assessDowhenStatement,
            "RecallStatementContext": self.assessRecallStatement,
            "AdvanceStatementContext": self.assessAdvanceStatement,
            "AddStatementContext": self.assessAddStatement,
            "DivideStatementContext": self.assessDivideStatement,
            "MultiplyStatementContext": self.assessMultiplyStatement,
            "DateConvertStatementContext": self.assessDateConvertStatement,
            "InsertStatementContext": self.assessInsertStatement,
            "CaseStatementContext": self.assessCaseStatement,
            "ComputeStatementContext": self.assessComputeStatement,
            "ContinueStatementContext": self.assessContinueStatement,
            "DetermineActualStatementContext": self.assessDetermineActualStatement,
            "DetermineBackStatementContext": self.assessDetermineBackStatement,
            "DetermineEveryStatementContext": self.assessDetermineEveryStatement,
            "DetermineFromStatementContext": self.assessDetermineFromStatement,
            "DetermineGroupStatementContext": self.assessDetermineGroupStatement,
            "DetermineLastStatementContext": self.assessDetermineLastStatement,
            "DetermineTotalStatementContext": self.assessDetermineTotalStatement,
            "BreakStatementContext": self.assessBreakStatement,
            "AccessExtStatementContext": self.assessAccessExtStatement,
            "LookupBaseStatementContext": self.assessLookupBaseStatement,
            "LookupFromStatementContext": self.assessLookupFromStatement,
            "LookupEveryStatementContext": self.assessLookupEveryStatement,
            "LookupGroupStatementContext": self.assessLookupGroupStatement,
            "AttachStatementContext": self.assessAttachStatement,
            "AttachAndSpaceStatementContext": self.assessAttachAndSpaceStatement,
            "MessageStatementContext": self.assessMessageStatement,
            "AcceptStatementContext": self.assessAcceptStatement,
            "JumptoStatementContext": self.assessJumptoStatement,
            "ExtractStatementContext": self.assessExtractStatement,
            "SleepStatementContext": self.assessSleepStatement,
            "LabelStatementContext": self.assessLabelStatement,
            "CursorStatementContext": self.assessCursorStatement,
            "FlagStatementContext": self.assessFlagStatement,
            "DetachStatementContext": self.assessDetachStatement,
            "MovedateStatementContext": self.assessMoveDateStatement,
            "InitializeStatementContext": self.assessInitializeStatement,
            "AbortStatementContext": self.assessAbortStatement,
            "IfStatementContext": self.assessIfStatement,
            "LoopStatementContext": self.assessLoopStatement,
            "ReturnStatementContext": self.assessReturnStatement,
            "RocStatementContext": self.assessRocStatement,
            "StartStatementContext": self.assessStartStatement,
            "SendListDynamicStatementContext": self.assessSendListDynamicStatement,
            "SendListStaticStatementContext": self.assessSendListStaticStatement,
            "SendMessageStatementContext": self.assessSendMessageStatement,
            "SendPrintStatementContext": self.assessSendPrintStatement,
            "SetDBStatementContext": self.assessSetDBStatement,
            "SetTitleStatementContext": self.assessSetTitleStatement,
            "StninfoStatementContext": self.assessStnInfoStatement,
            "SubtractStatementContext": self.assessSubtractStatement,
            "SwitchtoStatementContext": self.assessSwitchToStatement,
            "WakeStatementContext": self.assessWakeStatement,
            "RunStatementContext": self.assessRunStatement,
            "CriticalPointStatementContext": self.assessCriticalpointStatement,
            "EndUseStatementContext": self.assessEnduseStatement,
            "ExcludeStatementContext": self.assessExcludeStatement,
            "MatchStatementContext": self.assessMatchStatement,
            "AttributeStatementContext": self.assessAttributeStatement,
            "BeginpageStatementContext": self.assessBeginpageStatement,
            "OnchangeStatementContext": self.assessOnchangeStatement,
            "PageStatementContext": self.assessPageStatement,
            "ReleaseStatementContext": self.assessReleaseStatement,
            "RestartStatementContext": self.assessRestartStatement,
            "LogStatementContext": self.assessLogStatement,
            "MovetimeStatementContext": self.assessMovetimeStatement,
            "FunctionCallingStatementContext": self.assessFunctionCallingStatement,
        }

    def extract_statement(self, ctx, statement_class, **kwargs):
        raw = get_original_code_content(
            ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex
        )
        start_line = ctx.start.line
        stop_line = ctx.stop.line
        statement = statement_class(
            raw=raw,
            start_line=start_line,
            stop_line=stop_line,
            tag=ctx.__class__.__name__.replace("Context", ""),
            **kwargs,
        )
        return statement

    # Visit a parse tree produced by LDLPParser#startRule.
    def visitStartRule(self, ctx: LDLPParser.StartRuleContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#runtime.
    def visitRuntime(self, ctx: LDLPParser.RuntimeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#statements.
    def visitStatements(self, ctx: LDLPParser.StatementsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#statement.
    def visitStatement(self, ctx: LDLPParser.StatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#functionCallingStatement.
    def visitFunctionCallingStatement(
        self, ctx: LDLPParser.FunctionCallingStatementContext
    ):
        try:
            statement = self.assessFunctionCallingStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )

        return self.visitChildren(ctx)

    def assessFunctionCallingStatement(
        self, ctx: LDLPParser.FunctionCallingStatementContext
    ):
        function_name = get_original_code_content(
            ctx.parser,
            ctx.function_name().start.tokenIndex,
            ctx.function_name().stop.tokenIndex,
        )

        params = (
            [
                get_original_code_content(
                    ctx.parser,
                    param.start.tokenIndex,
                    param.stop.tokenIndex,
                )
                for param in ctx.paramList().param()
            ]
            if ctx.paramList()
            else []
        )

        statement = self.extract_statement(
            ctx,
            FunctionCallingStatement,
            function_name=function_name,
            params=params,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#function_name.
    def visitFunction_name(self, ctx: LDLPParser.Function_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#abortStatement.
    def visitAbortStatement(self, ctx: LDLPParser.AbortStatementContext):
        try:
            statement = self.assessAbortStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )

        return self.visitChildren(ctx)

    def assessAbortStatement(self, ctx: LDLPParser.AbortStatementContext):
        message = (
            get_original_code_content(
                ctx.parser,
                ctx.getChild(1).start.tokenIndex,
                ctx.getChild(1).stop.tokenIndex,
            )
            if ctx.getChild(1)
            else None
        )

        recall_item_name = (
            get_original_code_content(
                ctx.parser,
                ctx.getChild(2).start.tokenIndex,
                ctx.getChild(2).stop.tokenIndex,
            )
            if ctx.getChild(2)
            else None
        )

        statement = self.extract_statement(
            ctx,
            AbortStatement,
            message=message,
            recall_item_name=recall_item_name,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#acceptStatement.
    def visitAcceptStatement(self, ctx: LDLPParser.AcceptStatementContext):
        try:
            statement = self.assessAcceptStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessAcceptStatement(self, ctx: LDLPParser.AcceptStatementContext):
        object_name = get_original_code_content(
            ctx.parser,
            ctx.objectName().start.tokenIndex,
            ctx.objectName().stop.tokenIndex,
        )

        statement = self.extract_statement(
            ctx,
            AcceptStatement,
            object_name=object_name,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#accessExtStatement.
    def visitAccessExtStatement(self, ctx: LDLPParser.AccessExtStatementContext):
        try:
            statement = self.assessAccessExtStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessAccessExtStatement(self, ctx: LDLPParser.AccessExtStatementContext):
        db_name = get_original_code_content(
            ctx.parser,
            ctx.dbName().start.tokenIndex,
            ctx.dbName().stop.tokenIndex,
        )

        locator_ctx = ctx.locator()

        access_ext_type = None
        database = None
        item = None

        if locator_ctx:
            if locator_ctx.get():
                access_ext_type = "GET"
                database = get_original_code_content(
                    ctx.parser,
                    locator_ctx.get().database().start.tokenIndex,
                    locator_ctx.get().database().stop.tokenIndex,
                )

                item = get_original_code_content(
                    ctx.parser,
                    locator_ctx.get().item().start.tokenIndex,
                    locator_ctx.get().item().stop.tokenIndex,
                )
            else:
                access_ext_type = "FIND"
                database = get_original_code_content(
                    ctx.parser,
                    locator_ctx.find().database().start.tokenIndex,
                    locator_ctx.find().database().stop.tokenIndex,
                )

        statement = self.extract_statement(
            ctx,
            AccessExtStatement,
            db_name=db_name,
            access_ext_type=access_ext_type,
            database=database,
            item=item,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#locator.
    def visitLocator(self, ctx: LDLPParser.LocatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#find.
    def visitFind(self, ctx: LDLPParser.FindContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#get.
    def visitGet(self, ctx: LDLPParser.GetContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#database.
    def visitDatabase(self, ctx: LDLPParser.DatabaseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#item.
    def visitItem(self, ctx: LDLPParser.ItemContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#addStatement.
    def visitAddStatement(self, ctx: LDLPParser.AddStatementContext):
        try:
            statement = self.assessAddStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessAddStatement(self, ctx: LDLPParser.AddStatementContext):
        first_operand = get_original_code_content(
            ctx.parser,
            ctx.expression().start.tokenIndex,
            ctx.expression().stop.tokenIndex,
        )
        second_operand = get_original_code_content(
            ctx.parser,
            ctx.variable(0).start.tokenIndex,
            ctx.variable(0).stop.tokenIndex,
        )
        results = (
            get_original_code_content(
                ctx.parser,
                ctx.variable(1).start.tokenIndex,
                ctx.variable(1).stop.tokenIndex,
            )
            if len(ctx.variable()) > 1
            else second_operand
        )
        is_rounded = ctx.ROUNDED() is not None
        gs_status = (
            get_original_code_content(
                ctx.parser,
                ctx.status().start.tokenIndex,
                ctx.status().stop.tokenIndex,
            )
            if ctx.status()
            else None
        )

        statement = self.extract_statement(
            ctx,
            AddStatement,
            first_operand=first_operand,
            second_operand=second_operand,
            results=results,
            is_rounded=is_rounded,
            gs_status=gs_status,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#advanceStatement.
    def visitAdvanceStatement(self, ctx: LDLPParser.AdvanceStatementContext):
        try:
            statement = self.assessAdvanceStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessAdvanceStatement(self, ctx: LDLPParser.AdvanceStatementContext):
        number_of_lines = (
            int(ctx.NUMERIC_LITERALS().getText()) if ctx.NUMERIC_LITERALS() else None
        )
        is_to_new_page = ctx.NEW_PAGE() is not None
        channel = int(ctx.CHANNEL().getText()) if ctx.CHANNEL() else None
        output_stream = (
            get_original_code_content(
                ctx.parser,
                ctx.outputStream().start.tokenIndex,
                ctx.outputStream().stop.tokenIndex,
            )
            if ctx.outputStream()
            else None
        )

        statement = self.extract_statement(
            ctx,
            AdvanceStatement,
            number_of_lines=number_of_lines,
            is_to_new_page=is_to_new_page,
            channel=channel,
            output_stream=output_stream,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#outputStream.
    def visitOutputStream(self, ctx: LDLPParser.OutputStreamContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#assignment.
    def visitAssignment(self, ctx: LDLPParser.AssignmentContext):
        try:
            statement = self.assessAssignment(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessAssignment(self, ctx: LDLPParser.AssignmentContext):
        source = get_original_code_content(
            ctx.parser,
            ctx.expression().start.tokenIndex,
            ctx.expression().stop.tokenIndex,
        )
        target = get_original_code_content(
            ctx.parser, ctx.variable().start.tokenIndex, ctx.variable().stop.tokenIndex
        )

        statement = self.extract_statement(
            ctx,
            Assignment,
            source=source,
            target=target,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#attachStatement.
    def visitAttachStatement(self, ctx: LDLPParser.AttachStatementContext):
        try:
            statement = self.assessAttachStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessAttachStatement(self, ctx: LDLPParser.AttachStatementContext):
        value = get_original_code_content(
            ctx.parser,
            ctx.stringExpression().start.tokenIndex,
            ctx.stringExpression().stop.tokenIndex,
        )
        attach_variable = get_original_code_content(
            ctx.parser,
            ctx.variable().start.tokenIndex,
            ctx.variable().stop.tokenIndex,
        )

        statement = self.extract_statement(
            ctx,
            AttachStatement,
            value=value,
            attach_variable=attach_variable,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#attachAndSpaceStatement.
    def visitAttachAndSpaceStatement(
        self, ctx: LDLPParser.AttachAndSpaceStatementContext
    ):
        try:
            statement = self.assessAttachAndSpaceStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessAttachAndSpaceStatement(
        self, ctx: LDLPParser.AttachAndSpaceStatementContext
    ):
        value = get_original_code_content(
            ctx.parser,
            ctx.stringExpression().start.tokenIndex,
            ctx.stringExpression().stop.tokenIndex,
        )
        attach_variable = get_original_code_content(
            ctx.parser,
            ctx.variable().start.tokenIndex,
            ctx.variable().stop.tokenIndex,
        )

        statement = self.extract_statement(
            ctx,
            AttachAndSpaceStatement,
            value=value,
            attach_variable=attach_variable,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#attributeStatement.
    def visitAttributeStatement(self, ctx: LDLPParser.AttributeStatementContext):
        try:
            statement = self.assessAttributeStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )

        return self.visitChildren(ctx)

    def assessAttributeStatement(self, ctx: LDLPParser.AttributeStatementContext):
        bd_name_attribute = get_original_code_content(
            ctx.parser,
            ctx.literal().start.tokenIndex,
            ctx.literal().stop.tokenIndex,
        )

        user_code = (
            get_original_code_content(
                ctx.parser,
                ctx.userCode().start.tokenIndex,
                ctx.userCode().stop.tokenIndex,
            )
            if ctx.userCode()
            else None
        )

        gs_status = (
            get_original_code_content(
                ctx.parser,
                ctx.status().start.tokenIndex,
                ctx.status().stop.tokenIndex,
            )
            if ctx.status()
            else None
        )

        statement = self.extract_statement(
            ctx,
            AttributeStatement,
            bd_name_attribute=bd_name_attribute,
            user_code=user_code,
            gs_status=gs_status,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#beginpageStatement.
    def visitBeginpageStatement(self, ctx: LDLPParser.BeginpageStatementContext):
        try:
            statement = self.assessBeginpageStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )

        return self.visitChildren(ctx)

    def assessBeginpageStatement(self, ctx: LDLPParser.BeginpageStatementContext):
        is_clear = ctx.CLEAR() is not None

        heading_frame_name = (
            get_original_code_content(
                ctx.parser,
                ctx.frameName().start.tokenIndex,
                ctx.frameName().stop.tokenIndex,
            )
            if ctx.frameName()
            else None
        )

        output_stream = (
            get_original_code_content(
                ctx.parser,
                ctx.outputStream().start.tokenIndex,
                ctx.outputStream().stop.tokenIndex,
            )
            if ctx.outputStream()
            else None
        )

        statement = self.extract_statement(
            ctx,
            BeginPageStatement,
            is_clear=is_clear,
            heading_frame_name=heading_frame_name,
            output_stream=output_stream,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#breakStatement.
    def visitBreakStatement(self, ctx: LDLPParser.BreakStatementContext):
        try:
            statement = self.assessBreakStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessBreakStatement(self, ctx: LDLPParser.BreakStatementContext):
        is_break_all = ctx.ALL() is not None

        statement = self.extract_statement(
            ctx,
            BreakStatement,
            is_break_all=is_break_all,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#case.
    def visitCase(self, ctx: LDLPParser.CaseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#otherwise.
    def visitOtherwise(self, ctx: LDLPParser.OtherwiseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#caseStatement.
    def visitCaseStatement(self, ctx: LDLPParser.CaseStatementContext):
        try:
            statement = self.assessCaseStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessCaseStatement(self, ctx: LDLPParser.CaseStatementContext):
        control_value = get_original_code_content(
            ctx.parser,
            ctx.expression().start.tokenIndex,
            ctx.expression().stop.tokenIndex,
        )

        cases = []
        for case in ctx.case():
            values = []
            for val in case.getChildren():
                if isinstance(val, LDLPParser.LiteralContext) or isinstance(
                    val, LDLPParser.VariableContext
                ):
                    values.append(
                        get_original_code_content(
                            ctx.parser,
                            val.start.tokenIndex,
                            val.stop.tokenIndex,
                        )
                    )
            case_statements = []
            if case.statements():
                case_statements = self.assess_nested_statements(case.statements())
            cases.append(Case(values=values, statements=case_statements))

        otherwise_statements = []
        if ctx.otherwise() and ctx.otherwise().statements():
            otherwise_statements = self.assess_nested_statements(
                ctx.otherwise().statements()
            )

        statement = self.extract_statement(
            ctx,
            CaseStatement,
            control_value=control_value,
            cases=cases,
            otherwise_statements=otherwise_statements,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#beginCase.
    def visitBeginCase(self, ctx: LDLPParser.BeginCaseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#endcase.
    def visitEndcase(self, ctx: LDLPParser.EndcaseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#computeStatement.
    def visitComputeStatement(self, ctx: LDLPParser.ComputeStatementContext):
        try:
            statement = self.assessComputeStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessComputeStatement(self, ctx: LDLPParser.ComputeStatementContext):
        results = get_original_code_content(
            ctx.parser,
            ctx.variable().start.tokenIndex,
            ctx.variable().stop.tokenIndex,
        )
        evaluate_expression = get_original_code_content(
            ctx.parser,
            ctx.expression().start.tokenIndex,
            ctx.expression().stop.tokenIndex,
        )
        is_rounded = ctx.ROUNDED() is not None
        gs_status = (
            get_original_code_content(
                ctx.parser,
                ctx.status().start.tokenIndex,
                ctx.status().stop.tokenIndex,
            )
            if ctx.status()
            else None
        )

        statement = self.extract_statement(
            ctx,
            ComputeStatement,
            results=results,
            evaluate_expression=evaluate_expression,
            is_rounded=is_rounded,
            gs_status=gs_status,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#continueStatement.
    def visitContinueStatement(self, ctx: LDLPParser.ContinueStatementContext):
        try:
            statement = self.assessContinueStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessContinueStatement(self, ctx: LDLPParser.ContinueStatementContext):
        statement = self.extract_statement(ctx, ContinueStatement)
        return statement

    # Visit a parse tree produced by LDLPParser#criticalpointStatement.
    def visitCriticalpointStatement(
        self, ctx: LDLPParser.CriticalpointStatementContext
    ):
        try:
            statement = self.assessCriticalpointStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessCriticalpointStatement(
        self, ctx: LDLPParser.CriticalpointStatementContext
    ):
        suspend_time = (
            get_original_code_content(
                ctx.parser,
                ctx.expression().start.tokenIndex,
                ctx.expression().stop.tokenIndex,
            )
            if ctx.expression()
            else None
        )
        is_no_release = ctx.NO_RELEASE() is not None

        statement = self.extract_statement(
            ctx,
            CriticalPointStatement,
            suspend_time=suspend_time,
            is_no_release=is_no_release,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#cursorStatement.
    def visitCursorStatement(self, ctx: LDLPParser.CursorStatementContext):
        try:
            statement = self.assessCursorStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessCursorStatement(self, ctx: LDLPParser.CursorStatementContext):
        position = (
            ctx.getChild(1).getText()
            if isinstance(ctx.getChild(1), TerminalNodeImpl)
            else get_original_code_content(
                ctx.parser,
                ctx.getChild(1).start.tokenIndex,
                ctx.getChild(1).stop.tokenIndex,
            )
        )

        statement = self.extract_statement(
            ctx,
            CursorStatement,
            position=position,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#dateConvertStatement.
    def visitDateConvertStatement(self, ctx: LDLPParser.DateConvertStatementContext):
        try:
            statement = self.assessDateConvertStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessDateConvertStatement(self, ctx: LDLPParser.DateConvertStatementContext):
        input_date_variable = get_original_code_content(
            ctx.parser,
            ctx.dateVariable(0).start.tokenIndex,
            ctx.dateVariable(0).stop.tokenIndex,
        )
        offset = (
            get_original_code_content(
                ctx.parser,
                ctx.dateVariable(1).start.tokenIndex,
                ctx.dateVariable(1).stop.tokenIndex,
            )
            if len(ctx.dateVariable()) > 1
            else None
        )
        format = (
            get_original_code_content(
                ctx.parser,
                ctx.dateFormat(0).start.tokenIndex,
                ctx.dateFormat(0).stop.tokenIndex,
            )
            if ctx.dateFormat()
            else ctx.getChild(1).getText()
        )

        gs_status = (
            get_original_code_content(
                ctx.parser,
                ctx.status().start.tokenIndex,
                ctx.status().stop.tokenIndex,
            )
            if ctx.status()
            else None
        )

        statement = self.extract_statement(
            ctx,
            DateConvertStatement,
            input_date_variable=input_date_variable,
            offset=offset,
            format=format,
            gs_status=gs_status,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#dateVariable.
    def visitDateVariable(self, ctx: LDLPParser.DateVariableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#detachStatement.
    def visitDetachStatement(self, ctx: LDLPParser.DetachStatementContext):
        try:
            statement = self.assessDetachStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessDetachStatement(self, ctx: LDLPParser.DetachStatementContext):
        value = get_original_code_content(
            ctx.parser,
            ctx.expression(0).start.tokenIndex,
            ctx.expression(0).stop.tokenIndex,
        )
        detach_variable = get_original_code_content(
            ctx.parser,
            ctx.variable().start.tokenIndex,
            ctx.variable().stop.tokenIndex,
        )
        start_position = (
            get_original_code_content(
                ctx.parser,
                ctx.start_position.start.tokenIndex,
                ctx.start_position.stop.tokenIndex,
            )
            if ctx.start_position
            else None
        )
        delimiter = (
            get_original_code_content(
                ctx.parser,
                ctx.delimiter.start.tokenIndex,
                ctx.delimiter.stop.tokenIndex,
            )
            if ctx.delimiter
            else None
        )

        statement = self.extract_statement(
            ctx,
            DetachStatement,
            value=value,
            detach_variable=detach_variable,
            start_position=start_position,
            delimiter=delimiter,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#determineStatement.
    def visitDetermineStatement(self, ctx: LDLPParser.DetermineStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#determineActualStatement.
    def visitDetermineActualStatement(
        self, ctx: LDLPParser.DetermineActualStatementContext
    ):
        try:
            statement = self.assessDetermineActualStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessDetermineActualStatement(
        self, ctx: LDLPParser.DetermineActualStatementContext
    ):
        variant = "Database" if ctx.variant().databaseVariant() else "ExtractFile"

        variant_ctx = ctx.variant()
        iterator = (
            get_original_code_content(
                ctx.parser,
                variant_ctx.databaseVariant().iterator().start.tokenIndex,
                variant_ctx.databaseVariant().iterator().stop.tokenIndex,
            )
            if variant_ctx.databaseVariant()
            else None
        )
        extract_file = (
            get_original_code_content(
                ctx.parser,
                variant_ctx.extractFileVariant().extractFile().start.tokenIndex,
                variant_ctx.extractFileVariant().extractFile().stop.tokenIndex,
            )
            if variant_ctx.extractFileVariant()
            else None
        )

        extracted_as = (
            get_original_code_content(
                ctx.parser,
                variant_ctx.extractFileVariant().getChild(2).start.tokenIndex,
                variant_ctx.extractFileVariant().getChild(2).stop.tokenIndex,
            )
            if variant_ctx.extractFileVariant()
            else None
        )
        retained_as = (
            get_original_code_content(
                ctx.parser,
                variant_ctx.extractFileVariant().fileName().start.tokenIndex,
                variant_ctx.extractFileVariant().fileName().stop.tokenIndex,
            )
            if variant_ctx.extractFileVariant()
            and variant_ctx.extractFileVariant().fileName()
            else None
        )
        is_serial = (
            variant_ctx.databaseVariant().SERIAL() is not None
            if variant_ctx.databaseVariant()
            else False
        )
        is_secure = (
            variant_ctx.databaseVariant().SECURE() is not None
            if variant_ctx.databaseVariant()
            else False
        )
        is_key_only = (
            variant_ctx.databaseVariant().KEY_ONLY() is not None
            if variant_ctx.databaseVariant()
            else False
        )

        gs_status = (
            get_original_code_content(
                ctx.parser,
                ctx.status().start.tokenIndex,
                ctx.status().stop.tokenIndex,
            )
            if ctx.status()
            else None
        )

        multi_records = (
            get_original_code_content(
                ctx.parser,
                variant_ctx.databaseVariant().records().start.tokenIndex,
                variant_ctx.databaseVariant().records().stop.tokenIndex,
            )
            if variant_ctx.databaseVariant() and variant_ctx.databaseVariant().records()
            else None
        )

        statements = []
        if ctx.statements():
            statements = self.assess_nested_statements(ctx.statements())

        statement = self.extract_statement(
            ctx,
            DetermineActualStatement,
            variant=variant,
            iterator=iterator,
            extract_file=extract_file,
            extracted_as=extracted_as,
            retained_as=retained_as,
            is_serial=is_serial,
            is_secure=is_secure,
            is_key_only=is_key_only,
            gs_status=gs_status,
            multi_records=multi_records,
            statements=statements,
        )

        return statement

    def assess_nested_statements(
        self, statements_ctx: LDLPParser.StatementsContext
    ) -> List[LDLPStatement]:
        MULTI_TYPE_STATEMENTS = (
            LDLPParser.DetermineStatementContext,
            LDLPParser.LookupStatementContext,
        )

        statements = []

        for statement in statements_ctx.statement():
            statement = statement.getChild(0)
            if isinstance(
                statement,
                MULTI_TYPE_STATEMENTS,
            ):
                statement = statement.getChild(0)

            statement_type = type(statement).__name__

            if statement_type in self.func:
                try:
                    statement = self.func[statement_type](statement)
                    statements.append(statement)
                except Exception as e:
                    logger.error(traceback.format_exc())
                    logger.warning(
                        f"Cannot assess statement {statement_type}: {statement.getText()}, skipping"
                    )
            else:
                logger.warning(
                    f"Missing assessment for statement {statement_type}, skipping"
                )

        return statements

    # Visit a parse tree produced by LDLPParser#determineBackStatement.
    def visitDetermineBackStatement(
        self, ctx: LDLPParser.DetermineBackStatementContext
    ):
        try:
            statement = self.assessDetermineBackStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessDetermineBackStatement(
        self, ctx: LDLPParser.DetermineBackStatementContext
    ):
        iterator = get_original_code_content(
            ctx.parser,
            ctx.iterator().start.tokenIndex,
            ctx.iterator().stop.tokenIndex,
        )
        is_serial = ctx.SERIAL() is not None
        is_secure = ctx.SECURE() is not None
        is_key_only = ctx.KEY_ONLY() is not None
        gs_status = (
            get_original_code_content(
                ctx.parser,
                ctx.status().start.tokenIndex,
                ctx.status().stop.tokenIndex,
            )
            if ctx.status()
            else None
        )
        multi_records = (
            get_original_code_content(
                ctx.parser,
                ctx.records().start.tokenIndex,
                ctx.records().stop.tokenIndex,
            )
            if ctx.records()
            else None
        )

        statements = []
        if ctx.statements():
            statements = self.assess_nested_statements(ctx.statements())

        statement = self.extract_statement(
            ctx,
            DetermineBackStatement,
            iterator=iterator,
            is_serial=is_serial,
            is_secure=is_secure,
            is_key_only=is_key_only,
            gs_status=gs_status,
            multi_records=multi_records,
            statements=statements,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#determineEveryStatement.
    def visitDetermineEveryStatement(
        self, ctx: LDLPParser.DetermineEveryStatementContext
    ):
        try:
            statement = self.assessDetermineEveryStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )

        return self.visitChildren(ctx)

    def assessDetermineEveryStatement(
        self, ctx: LDLPParser.DetermineEveryStatementContext
    ):
        iterator = get_original_code_content(
            ctx.parser,
            ctx.iterator().start.tokenIndex,
            ctx.iterator().stop.tokenIndex,
        )

        is_serial = ctx.SERIAL() is not None
        is_secure = ctx.SECURE() is not None
        is_key_only = ctx.KEY_ONLY() is not None

        multi_records = (
            get_original_code_content(
                ctx.parser,
                ctx.records().start.tokenIndex,
                ctx.records().stop.tokenIndex,
            )
            if ctx.records()
            else None
        )

        statements = []
        if ctx.statements():
            statements = self.assess_nested_statements(ctx.statements())

        gs_status = (
            get_original_code_content(
                ctx.parser,
                ctx.status().start.tokenIndex,
                ctx.status().stop.tokenIndex,
            )
            if ctx.status()
            else None
        )

        statement = self.extract_statement(
            ctx,
            DetermineEveryStatement,
            iterator=iterator,
            is_serial=is_serial,
            is_secure=is_secure,
            is_key_only=is_key_only,
            multi_records=multi_records,
            gs_status=gs_status,
            statements=statements,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#determineFromStatement.
    def visitDetermineFromStatement(
        self, ctx: LDLPParser.DetermineFromStatementContext
    ):
        try:
            statement = self.assessDetermineFromStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessDetermineFromStatement(
        self, ctx: LDLPParser.DetermineFromStatementContext
    ):
        iterator = get_original_code_content(
            ctx.parser,
            ctx.iterator().start.tokenIndex,
            ctx.iterator().stop.tokenIndex,
        )
        is_serial = ctx.SERIAL() is not None
        is_secure = ctx.SECURE() is not None
        is_key_only = ctx.KEY_ONLY() is not None
        gs_status = (
            get_original_code_content(
                ctx.parser,
                ctx.status().start.tokenIndex,
                ctx.status().stop.tokenIndex,
            )
            if ctx.status()
            else None
        )
        multi_records = (
            get_original_code_content(
                ctx.parser,
                ctx.records().start.tokenIndex,
                ctx.records().stop.tokenIndex,
            )
            if ctx.records()
            else None
        )

        statements = []
        if ctx.statements():
            statements = self.assess_nested_statements(ctx.statements())

        statement = self.extract_statement(
            ctx,
            DetermineFromStatement,
            iterator=iterator,
            is_serial=is_serial,
            is_secure=is_secure,
            is_key_only=is_key_only,
            gs_status=gs_status,
            multi_records=multi_records,
            statements=statements,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#determineGroupStatement.
    def visitDetermineGroupStatement(
        self, ctx: LDLPParser.DetermineGroupStatementContext
    ):
        try:
            statement = self.assessDetermineGroupStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessDetermineGroupStatement(
        self, ctx: LDLPParser.DetermineGroupStatementContext
    ):
        iterator = get_original_code_content(
            ctx.parser,
            ctx.iterator().start.tokenIndex,
            ctx.iterator().stop.tokenIndex,
        )
        arguments = [
            get_original_code_content(
                ctx.parser,
                arg.start.tokenIndex,
                arg.stop.tokenIndex,
            )
            for arg in ctx.args
        ]
        until_arguments = (
            [
                get_original_code_content(
                    ctx.parser,
                    arg.start.tokenIndex,
                    arg.stop.tokenIndex,
                )
                for arg in ctx.until_args
            ]
            if ctx.until_args
            else []
        )

        is_serial = ctx.SERIAL() is not None
        is_secure = ctx.SECURE() is not None
        is_key_only = ctx.KEY_ONLY() is not None
        gs_status = (
            get_original_code_content(
                ctx.parser,
                ctx.status().start.tokenIndex,
                ctx.status().stop.tokenIndex,
            )
            if ctx.status()
            else None
        )
        multi_records = (
            get_original_code_content(
                ctx.parser,
                ctx.records().start.tokenIndex,
                ctx.records().stop.tokenIndex,
            )
            if ctx.records()
            else None
        )

        statements = []
        if ctx.statements():
            statements = self.assess_nested_statements(ctx.statements())

        statement = self.extract_statement(
            ctx,
            DetermineGroupStatement,
            iterator=iterator,
            arguments=arguments,
            until_arguments=until_arguments,
            is_serial=is_serial,
            is_secure=is_secure,
            is_key_only=is_key_only,
            gs_status=gs_status,
            multi_records=multi_records,
            statements=statements,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#determineLastStatement.
    def visitDetermineLastStatement(
        self, ctx: LDLPParser.DetermineLastStatementContext
    ):
        try:
            statement = self.assessDetermineLastStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessDetermineLastStatement(
        self, ctx: LDLPParser.DetermineLastStatementContext
    ):
        iterator = get_original_code_content(
            ctx.parser,
            ctx.iterator().start.tokenIndex,
            ctx.iterator().stop.tokenIndex,
        )
        is_secure = ctx.SECURE() is not None
        is_key_only = ctx.KEY_ONLY() is not None
        gs_status = (
            get_original_code_content(
                ctx.parser,
                ctx.status().start.tokenIndex,
                ctx.status().stop.tokenIndex,
            )
            if ctx.status()
            else None
        )

        statement = self.extract_statement(
            ctx,
            DetermineLastStatement,
            iterator=iterator,
            is_secure=is_secure,
            is_key_only=is_key_only,
            gs_status=gs_status,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#determineTotal.
    def visitDetermineTotalStatementContext(
        self, ctx: LDLPParser.DetermineTotalStatementContext
    ):
        try:
            statement = self.assessDetermineTotalStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessDetermineTotalStatement(
        self, ctx: LDLPParser.DetermineTotalStatementContext
    ):
        identifier = get_original_code_content(
            ctx.parser,
            ctx.identifier().start.tokenIndex,
            ctx.identifier().stop.tokenIndex,
        )
        attribute_name = get_original_code_content(
            ctx.parser,
            ctx.attributeName().start.tokenIndex,
            ctx.attributeName().stop.tokenIndex,
        )
        arguments = [
            get_original_code_content(
                ctx.parser,
                arg.start.tokenIndex,
                arg.stop.tokenIndex,
            )
            for arg in ctx.keyArguments().argument()
        ]
        gs_status = (
            get_original_code_content(
                ctx.parser,
                ctx.status().start.tokenIndex,
                ctx.status().stop.tokenIndex,
            )
            if ctx.status()
            else None
        )
        multi_records = (
            get_original_code_content(
                ctx.parser,
                ctx.records().start.tokenIndex,
                ctx.records().stop.tokenIndex,
            )
            if ctx.records()
            else None
        )

        statements = []
        if ctx.statements():
            statements = self.assess_nested_statements(ctx.statements())

        statement = self.extract_statement(
            ctx,
            DetermineTotalStatement,
            identifier=identifier,
            attribute_name=attribute_name,
            arguments=arguments,
            gs_status=gs_status,
            multi_records=multi_records,
            statements=statements,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#attributeName.
    def visitAttributeName(self, ctx: LDLPParser.AttributeNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#keyArguments.
    def visitKeyArguments(self, ctx: LDLPParser.KeyArgumentsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#records.
    def visitRecords(self, ctx: LDLPParser.RecordsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#extractFile.
    def visitExtractFile(self, ctx: LDLPParser.ExtractFileContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#iterator.
    def visitIterator(self, ctx: LDLPParser.IteratorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#argument.
    def visitArgument(self, ctx: LDLPParser.ArgumentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#determineEnd.
    def visitDetermineEnd(self, ctx: LDLPParser.DetermineEndContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#divideStatement.
    def visitDivideStatement(self, ctx: LDLPParser.DivideStatementContext):
        try:
            statement = self.assessDivideStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessDivideStatement(self, ctx: LDLPParser.DivideStatementContext):
        divisor = get_original_code_content(
            ctx.parser,
            ctx.expression().start.tokenIndex,
            ctx.expression().stop.tokenIndex,
        )
        dividend = get_original_code_content(
            ctx.parser,
            ctx.variable(0).start.tokenIndex,
            ctx.variable(0).stop.tokenIndex,
        )
        results = (
            get_original_code_content(
                ctx.parser,
                ctx.giving_variable.start.tokenIndex,
                ctx.giving_variable.stop.tokenIndex,
            )
            if ctx.giving_variable
            else divisor
        )
        is_rounded = ctx.ROUNDED() is not None
        remainder = (
            get_original_code_content(
                ctx.parser,
                ctx.remainder_variable.start.tokenIndex,
                ctx.remainder_variable.stop.tokenIndex,
            )
            if ctx.remainder_variable
            else None
        )
        gs_status = (
            get_original_code_content(
                ctx.parser,
                ctx.status().start.tokenIndex,
                ctx.status().stop.tokenIndex,
            )
            if ctx.status()
            else None
        )

        statement = self.extract_statement(
            ctx,
            DivideStatement,
            dividend=dividend,
            divisor=divisor,
            results=results,
            is_rounded=is_rounded,
            remainder=remainder,
            gs_status=gs_status,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#dowhenBlock.
    def visitDowhenBlock(self, ctx: LDLPParser.DowhenBlockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#elseBlock.
    def visitElseBlock(self, ctx: LDLPParser.ElseBlockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#dowhenStatement.
    def visitDowhenStatement(self, ctx: LDLPParser.DowhenStatementContext):
        try:
            statement = self.assessDowhenStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessDowhenStatement(self, ctx: LDLPParser.DowhenStatementContext):
        condition = get_original_code_content(
            ctx.parser,
            ctx.condition().start.tokenIndex,
            ctx.condition().stop.tokenIndex,
        )

        statements = []

        if ctx.dowhenBlock():
            statements = self.assess_nested_statements(ctx.dowhenBlock().statements())

        else_statements = []
        if ctx.elseBlock():
            else_statements = self.assess_nested_statements(
                ctx.elseBlock().statements()
            )

        statement = self.extract_statement(
            ctx,
            DowhenStatement,
            condition=condition,
            statements=statements,
            else_statements=else_statements,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#endDowhen.
    def visitEndDowhen(self, ctx: LDLPParser.EndDowhenContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#enduseStatement.
    def visitEnduseStatement(self, ctx: LDLPParser.EnduseStatementContext):
        try:
            statement = self.assessEnduseStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessEnduseStatement(self, ctx: LDLPParser.EnduseStatementContext):
        class_name = get_original_code_content(
            ctx.parser,
            ctx.className().start.tokenIndex,
            ctx.className().stop.tokenIndex,
        )

        statement = self.extract_statement(
            ctx,
            EndUseStatement,
            class_name=class_name,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#excludeStatement.
    def visitExcludeStatement(self, ctx: LDLPParser.ExcludeStatementContext):
        try:
            statement = self.assessExcludeStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessExcludeStatement(self, ctx: LDLPParser.ExcludeStatementContext):
        class_name = get_original_code_content(
            ctx.parser,
            ctx.className().start.tokenIndex,
            ctx.className().stop.tokenIndex,
        )

        statement = self.extract_statement(
            ctx,
            ExcludeStatement,
            class_name=class_name,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#ifStatement.
    def visitIfStatement(self, ctx: LDLPParser.IfStatementContext):
        try:
            statement = self.assessIfStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessIfStatement(self, ctx: LDLPParser.IfStatementContext):
        condition = get_original_code_content(
            ctx.parser,
            ctx.expression().start.tokenIndex,
            ctx.expression().stop.tokenIndex,
        )

        statements = []
        if ctx.dowhenBlock():
            statements = self.assess_nested_statements(ctx.dowhenBlock().statements())

        else_statements = []
        if ctx.elseBlock():
            else_statements = self.assess_nested_statements(
                ctx.elseBlock().statements()
            )

        statement = self.extract_statement(
            ctx,
            IfStatement,
            condition=condition,
            statements=statements,
            else_statements=else_statements,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#endIf.
    def visitEndIf(self, ctx: LDLPParser.EndIfContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#methodCall.
    def visitMethodCall(self, ctx: LDLPParser.MethodCallContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#expression.
    def visitExpression(self, ctx: LDLPParser.ExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#stringExpression.
    def visitStringExpression(self, ctx: LDLPParser.StringExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#paramList.
    def visitParamList(self, ctx: LDLPParser.ParamListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#param.
    def visitParam(self, ctx: LDLPParser.ParamContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#extractStatement.
    def visitExtractStatement(self, ctx: LDLPParser.ExtractStatementContext):
        try:
            statement = self.assessExtractStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessExtractStatement(self, ctx: LDLPParser.ExtractStatementContext):
        attribute = get_original_code_content(
            ctx.parser,
            ctx.attributeName().start.tokenIndex,
            ctx.attributeName().stop.tokenIndex,
        )
        header = (
            get_original_code_content(
                ctx.parser,
                ctx.header().start.tokenIndex,
                ctx.header().stop.tokenIndex,
            )
            if ctx.header()
            else None
        )
        extract_file = get_original_code_content(
            ctx.parser,
            ctx.extractFile().start.tokenIndex,
            ctx.extractFile().stop.tokenIndex,
        )
        retain_as = (
            get_original_code_content(
                ctx.parser,
                ctx.fileName().start.tokenIndex,
                ctx.fileName().stop.tokenIndex,
            )
            if ctx.fileName()
            else None
        )

        statement = self.extract_statement(
            ctx,
            ExtractStatement,
            attribute=attribute,
            header=header,
            extract_file=extract_file,
            retain_as=retain_as,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#header.
    def visitHeader(self, ctx: LDLPParser.HeaderContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#foreachStatement.
    def visitForeachStatement(self, ctx: LDLPParser.ForeachStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#flagStatement.
    def visitFlagStatement(self, ctx: LDLPParser.FlagStatementContext):
        try:
            statement = self.assessFlagStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessFlagStatement(self, ctx: LDLPParser.FlagStatementContext):
        source_value = get_original_code_content(
            ctx.parser,
            ctx.expression().start.tokenIndex,
            ctx.expression().stop.tokenIndex,
        )
        variable = get_original_code_content(
            ctx.parser,
            ctx.variable().start.tokenIndex,
            ctx.variable().stop.tokenIndex,
        )

        statement = self.extract_statement(
            ctx,
            FlagStatement,
            source_value=source_value,
            variable=variable,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#initializeStatement.
    def visitInitializeStatement(self, ctx: LDLPParser.InitializeStatementContext):
        try:
            statement = self.assessInitializeStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessInitializeStatement(self, ctx: LDLPParser.InitializeStatementContext):
        variable = get_original_code_content(
            ctx.parser,
            ctx.variable().start.tokenIndex,
            ctx.variable().stop.tokenIndex,
        )
        initialization_value = (
            get_original_code_content(
                ctx.parser,
                ctx.initializationValue().start.tokenIndex,
                ctx.initializationValue().stop.tokenIndex,
            )
            if ctx.initializationValue()
            else None
        )

        statement = self.extract_statement(
            ctx,
            InitializeStatement,
            variable=variable,
            initialization_value=initialization_value,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#initializationValue.
    def visitInitializationValue(self, ctx: LDLPParser.InitializationValueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#insertStatement.
    def visitInsertStatement(self, ctx: LDLPParser.InsertStatementContext):
        try:
            statement = self.assessInsertStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessInsertStatement(self, ctx: LDLPParser.InsertStatementContext):
        insertable = get_original_code_content(
            ctx.parser,
            ctx.insertable().start.tokenIndex,
            ctx.insertable().stop.tokenIndex,
        )
        mappings = [
            get_original_code_content(
                ctx.parser,
                mapping.start.tokenIndex,
                mapping.stop.tokenIndex,
            )
            for mapping in ctx.mapping()
        ]

        statement = self.extract_statement(
            ctx,
            InsertStatement,
            insertable=insertable,
            mapping=mappings,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#insertable.
    def visitInsertable(self, ctx: LDLPParser.InsertableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#mapping.
    def visitMapping(self, ctx: LDLPParser.MappingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#tableName.
    def visitTableName(self, ctx: LDLPParser.TableNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#jumptoStatement.
    def visitJumptoStatement(self, ctx: LDLPParser.JumptoStatementContext):
        try:
            statement = self.assessJumptoStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessJumptoStatement(self, ctx: LDLPParser.JumptoStatementContext):
        label = get_original_code_content(
            ctx.parser,
            ctx.label().start.tokenIndex,
            ctx.label().stop.tokenIndex,
        )

        statement = self.extract_statement(
            ctx,
            JumpToStatement,
            label=label,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#labelStatement.
    def visitLabelStatement(self, ctx: LDLPParser.LabelStatementContext):
        try:
            statement = self.assessLabelStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessLabelStatement(self, ctx: LDLPParser.LabelStatementContext):
        label = get_original_code_content(
            ctx.parser,
            ctx.label().start.tokenIndex,
            ctx.label().stop.tokenIndex,
        )

        statement = self.extract_statement(
            ctx,
            LabelStatement,
            label=label,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#label.
    def visitLabel(self, ctx: LDLPParser.LabelContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#loadStatement.
    def visitLoadStatement(self, ctx: LDLPParser.LoadStatementContext):
        try:
            statement = self.assessLoadStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )

        return self.visitChildren(ctx)

    def assessLoadStatement(self, ctx: LDLPParser.LoadStatementContext):
        length = get_original_code_content(
            ctx.parser,
            ctx.expression().start.tokenIndex,
            ctx.expression().stop.tokenIndex,
        )

        ispec_attribute = get_original_code_content(
            ctx.parser,
            ctx.ispecAttribute().start.tokenIndex,
            ctx.ispecAttribute().stop.tokenIndex,
        )

        statement = self.extract_statement(
            ctx,
            LoadStatement,
            length=length,
            ispec_attribute=ispec_attribute,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#ispecAttribute.
    def visitIspecAttribute(self, ctx: LDLPParser.IspecAttributeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#logStatement.
    def visitLogStatement(self, ctx: LDLPParser.LogStatementContext):
        try:
            statement = self.assessLogStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )

        return self.visitChildren(ctx)

    def assessLogStatement(self, ctx: LDLPParser.LogStatementContext):
        mode = ctx.getChild(1).getText()
        level = ctx.ERROR() or ctx.WARNING() or ctx.HALT()
        level = level.getText() if level else None

        messages = [
            get_original_code_content(
                ctx.parser,
                message.start.tokenIndex,
                message.stop.tokenIndex,
            )
            for message in ctx.expression()
        ]

        statement = self.extract_statement(
            ctx,
            LogStatement,
            mode=mode,
            level=level,
            messages=messages,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#lookupStatement.
    def visitLookupStatement(self, ctx: LDLPParser.LookupStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#lookupBaseStatement.
    def visitLookupBaseStatement(self, ctx: LDLPParser.LookupBaseStatementContext):
        try:
            statement = self.assessLookupBaseStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessLookupBaseStatement(self, ctx: LDLPParser.LookupBaseStatementContext):
        primary_key = get_original_code_content(
            ctx.parser,
            ctx.expression().start.tokenIndex,
            ctx.expression().stop.tokenIndex,
        )
        class_name = get_original_code_content(
            ctx.parser,
            ctx.className().start.tokenIndex,
            ctx.className().stop.tokenIndex,
        )
        is_secure = ctx.SECURE() is not None
        is_key_only = ctx.KEY_ONLY() is not None
        gs_status = (
            get_original_code_content(
                ctx.parser,
                ctx.status().start.tokenIndex,
                ctx.status().stop.tokenIndex,
            )
            if ctx.status()
            else None
        )

        statement = self.extract_statement(
            ctx,
            LookupBaseStatement,
            primary_key=primary_key,
            class_name=class_name,
            is_secure=is_secure,
            is_key_only=is_key_only,
            gs_status=gs_status,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#lookupFromStatement.
    def visitLookupFromStatement(self, ctx: LDLPParser.LookupFromStatementContext):
        try:
            statement = self.assessLookupFromStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessLookupFromStatement(self, ctx: LDLPParser.LookupFromStatementContext):
        primary_key = get_original_code_content(
            ctx.parser,
            ctx.expression(0).start.tokenIndex,
            ctx.expression(0).stop.tokenIndex,
        )
        class_name = get_original_code_content(
            ctx.parser,
            ctx.className().start.tokenIndex,
            ctx.className().stop.tokenIndex,
        )
        is_serial = ctx.SERIAL() is not None
        is_secure = ctx.SECURE() is not None
        is_key_only = ctx.KEY_ONLY() is not None
        multi_command = (
            get_original_code_content(
                ctx.parser,
                ctx.expression(1).start.tokenIndex,
                ctx.expression(1).stop.tokenIndex,
            )
            if len(ctx.expression()) > 1
            else None
        )
        gs_status = (
            get_original_code_content(
                ctx.parser,
                ctx.status().start.tokenIndex,
                ctx.status().stop.tokenIndex,
            )
            if ctx.status()
            else None
        )

        statements = []
        if ctx.statements():
            statements = self.assess_nested_statements(ctx.statements())

        statement = self.extract_statement(
            ctx,
            LookupFromStatement,
            primary_key=primary_key,
            class_name=class_name,
            is_serial=is_serial,
            is_secure=is_secure,
            is_key_only=is_key_only,
            multi_command=multi_command,
            gs_status=gs_status,
            statements=statements,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#lookupEveryStatement.
    def visitLookupEveryStatement(self, ctx: LDLPParser.LookupEveryStatementContext):
        try:
            statement = self.assessLookupEveryStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessLookupEveryStatement(self, ctx: LDLPParser.LookupEveryStatementContext):
        class_name = get_original_code_content(
            ctx.parser,
            ctx.className().start.tokenIndex,
            ctx.className().stop.tokenIndex,
        )
        is_serial = ctx.SERIAL() is not None
        is_secure = ctx.SECURE() is not None
        is_key_only = ctx.KEY_ONLY() is not None
        multi_command = (
            get_original_code_content(
                ctx.parser,
                ctx.expression().start.tokenIndex,
                ctx.expression().stop.tokenIndex,
            )
            if ctx.expression()
            else None
        )
        gs_status = (
            get_original_code_content(
                ctx.parser,
                ctx.status().start.tokenIndex,
                ctx.status().stop.tokenIndex,
            )
            if ctx.status()
            else None
        )

        statements = []
        if ctx.statements():
            statements = self.assess_nested_statements(ctx.statements())

        statement = self.extract_statement(
            ctx,
            LookupEveryStatement,
            class_name=class_name,
            is_serial=is_serial,
            is_secure=is_secure,
            is_key_only=is_key_only,
            multi_command=multi_command,
            gs_status=gs_status,
            statements=statements,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#lookupGroupStatement.
    def visitLookupGroupStatement(self, ctx: LDLPParser.LookupGroupStatementContext):
        try:
            statement = self.assessLookupGroupStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessLookupGroupStatement(self, ctx: LDLPParser.LookupGroupStatementContext):
        class_name = get_original_code_content(
            ctx.parser,
            ctx.className().start.tokenIndex,
            ctx.className().stop.tokenIndex,
        )
        read_order = "FROM" if ctx.FROM() else "BACK"
        primary_key = get_original_code_content(
            ctx.parser,
            ctx.expression(0).start.tokenIndex,
            ctx.expression(0).stop.tokenIndex,
        )
        primary_key_final_record = (
            get_original_code_content(
                ctx.parser,
                ctx.until_exp.start.tokenIndex,
                ctx.until_exp.stop.tokenIndex,
            )
            if ctx.until_exp
            else None
        )
        is_serial = ctx.SERIAL() is not None
        is_secure = ctx.SECURE() is not None
        is_key_only = ctx.KEY_ONLY() is not None
        multi_command = (
            get_original_code_content(
                ctx.parser,
                ctx.multi_exp.start.tokenIndex,
                ctx.multi_exp.stop.tokenIndex,
            )
            if ctx.multi_exp
            else None
        )
        gs_status = (
            get_original_code_content(
                ctx.parser,
                ctx.status().start.tokenIndex,
                ctx.status().stop.tokenIndex,
            )
            if ctx.status()
            else None
        )

        statements = []
        if ctx.statements():
            statements = self.assess_nested_statements(ctx.statements())

        statement = self.extract_statement(
            ctx,
            LookupGroupStatement,
            class_name=class_name,
            read_order=read_order,
            primary_key=primary_key,
            primary_key_final_record=primary_key_final_record,
            is_serial=is_serial,
            is_secure=is_secure,
            is_key_only=is_key_only,
            multi_command=multi_command,
            gs_status=gs_status,
            statements=statements,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#loopStatement.
    def visitLoopStatement(self, ctx: LDLPParser.LoopStatementContext):
        try:
            statement = self.assessLoopStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessLoopStatement(self, ctx: LDLPParser.LoopStatementContext):
        condition = (
            get_original_code_content(
                ctx.parser,
                ctx.expression().start.tokenIndex,
                ctx.expression().stop.tokenIndex,
            )
            if ctx.expression()
            else None
        )

        statements = []
        if ctx.loopBlock():
            statements = self.assess_nested_statements(ctx.loopBlock().statements())

        statement = self.extract_statement(
            ctx,
            LoopStatement,
            condition=condition,
            statements=statements,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#loopBlock.
    def visitLoopBlock(self, ctx: LDLPParser.LoopBlockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#compareType.
    def visitCompareType(self, ctx: LDLPParser.CompareTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#matchStatement.
    def visitMatchStatement(self, ctx: LDLPParser.MatchStatementContext):
        try:
            statement = self.assessMatchStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )

        return self.visitChildren(ctx)

    def assessMatchStatement(self, ctx: LDLPParser.MatchStatementContext):
        compare_type = get_original_code_content(
            ctx.parser,
            ctx.compareType().start.tokenIndex,
            ctx.compareType().stop.tokenIndex,
        )

        extract_files = [
            get_original_code_content(
                ctx.parser,
                extract_file.start.tokenIndex,
                extract_file.stop.tokenIndex,
            )
            for extract_file in ctx.extractFile()
        ]

        gs_status = (
            get_original_code_content(
                ctx.parser,
                ctx.status().start.tokenIndex,
                ctx.status().stop.tokenIndex,
            )
            if ctx.status()
            else None
        )

        statement = self.extract_statement(
            ctx,
            MatchStatement,
            compare_type=compare_type,
            extract_files=extract_files,
            gs_status=gs_status,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#messageStatement.
    def visitMessageStatement(self, ctx: LDLPParser.MessageStatementContext):
        try:
            statement = self.assessMessageStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessMessageStatement(self, ctx: LDLPParser.MessageStatementContext):
        message_type_ctx = ctx.getChild(1)

        message_type = (
            message_type_ctx.getText()
            if isinstance(message_type_ctx, TerminalNodeImpl)
            else get_original_code_content(
                ctx.parser,
                ctx.getChild(1).start.tokenIndex,
                ctx.getChild(1).stop.tokenIndex,
            )
        )

        message = (
            get_original_code_content(
                ctx.parser,
                ctx.getChild(2).start.tokenIndex,
                ctx.getChild(2).stop.tokenIndex,
            )
            if len(ctx.children) > 2
            else None
        )

        statement = self.extract_statement(
            ctx,
            MessageStatement,
            message_type=message_type,
            message=message,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#moveStatement.
    def visitMoveStatement(self, ctx: LDLPParser.MoveStatementContext):
        try:
            statement = self.assessMoveStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessMoveStatement(self, ctx: LDLPParser.MoveStatementContext):
        source = get_original_code_content(
            ctx.parser,
            ctx.expression().start.tokenIndex,
            ctx.expression().stop.tokenIndex,
        )
        source_position = (
            get_original_code_content(
                ctx.parser,
                ctx.source_variable().start.tokenIndex,
                ctx.source_variable().stop.tokenIndex,
            )
            if ctx.source_variable()
            else None
        )
        length = (
            get_original_code_content(
                ctx.parser, ctx.length().start.tokenIndex, ctx.length().stop.tokenIndex
            )
            if ctx.length()
            else None
        )
        target = get_original_code_content(
            ctx.parser, ctx.variable().start.tokenIndex, ctx.variable().stop.tokenIndex
        )
        target_position = (
            get_original_code_content(
                ctx.parser,
                ctx.target_variable().start.tokenIndex,
                ctx.target_variable().stop.tokenIndex,
            )
            if ctx.target_variable()
            else None
        )
        sort_order = (
            ctx.SORTA().getText()
            if ctx.SORTA()
            else (ctx.SORTD().getText() if ctx.SORTD() else None)
        )
        gs_status = (
            get_original_code_content(
                ctx.parser, ctx.status().start.tokenIndex, ctx.status().stop.tokenIndex
            )
            if ctx.status()
            else None
        )

        statement = self.extract_statement(
            ctx,
            MoveStatement,
            source=source,
            source_position=source_position,
            length=length,
            target=target,
            target_position=target_position,
            sort_order=sort_order,
            gs_status=gs_status,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#length.
    def visitLength(self, ctx: LDLPParser.LengthContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#source_variable.
    def visitSource_variable(self, ctx: LDLPParser.Source_variableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#target_variable.
    def visitTarget_variable(self, ctx: LDLPParser.Target_variableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#movedateStatement.
    def visitMovedateStatement(self, ctx: LDLPParser.MovedateStatementContext):
        try:
            statement = self.assessMoveDateStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessMoveDateStatement(self, ctx: LDLPParser.MovedateStatementContext):
        date_variable = get_original_code_content(
            ctx.parser,
            ctx.variable().start.tokenIndex,
            ctx.variable().stop.tokenIndex,
        )
        format = (
            get_original_code_content(
                ctx.parser,
                ctx.identifier().start.tokenIndex,
                ctx.identifier().stop.tokenIndex,
            )
            if ctx.identifier()
            else None
        )

        statement = self.extract_statement(
            ctx,
            MoveDateStatement,
            date_variable=date_variable,
            format=format,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#movetimeStatement.
    def visitMovetimeStatement(self, ctx: LDLPParser.MovetimeStatementContext):
        try:
            statement = self.assessMovetimeStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )

        return self.visitChildren(ctx)

    def assessMovetimeStatement(self, ctx: LDLPParser.MovetimeStatementContext):
        variable = get_original_code_content(
            ctx.parser,
            ctx.variable().start.tokenIndex,
            ctx.variable().stop.tokenIndex,
        )

        statement = self.extract_statement(
            ctx,
            MoveTimeStatement,
            variable=variable,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#multiplyStatement.
    def visitMultiplyStatement(self, ctx: LDLPParser.MultiplyStatementContext):
        try:
            statement = self.assessMultiplyStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessMultiplyStatement(self, ctx: LDLPParser.MultiplyStatementContext):
        multiplicand = get_original_code_content(
            ctx.parser,
            ctx.expression().start.tokenIndex,
            ctx.expression().stop.tokenIndex,
        )
        multiplier = get_original_code_content(
            ctx.parser,
            ctx.getChild(2).start.tokenIndex,
            ctx.getChild(2).stop.tokenIndex,
        )
        results = (
            get_original_code_content(
                ctx.parser,
                ctx.giving_variable.start.tokenIndex,
                ctx.giving_variable.stop.tokenIndex,
            )
            if ctx.giving_variable
            else multiplier
        )
        is_rounded = ctx.ROUNDED() is not None
        gs_status = (
            get_original_code_content(
                ctx.parser,
                ctx.status().start.tokenIndex,
                ctx.status().stop.tokenIndex,
            )
            if ctx.status()
            else None
        )

        statement = self.extract_statement(
            ctx,
            MultiplyStatement,
            multiplicand=multiplicand,
            multiplier=multiplier,
            results=results,
            is_rounded=is_rounded,
            gs_status=gs_status,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#onchangeStatement.
    def visitOnchangeStatement(self, ctx: LDLPParser.OnchangeStatementContext):
        try:
            statement = self.assessOnchangeStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )

        return self.visitChildren(ctx)

    def assessOnchangeStatement(self, ctx: LDLPParser.OnchangeStatementContext):
        controlling_variable = get_original_code_content(
            ctx.parser,
            ctx.variable().start.tokenIndex,
            ctx.variable().stop.tokenIndex,
        )

        as_literal = get_original_code_content(
            ctx.parser,
            ctx.literal().start.tokenIndex,
            ctx.literal().stop.tokenIndex,
        )

        footer_frame_name = (
            get_original_code_content(
                ctx.parser,
                ctx.footing_frame_name.start.tokenIndex,
                ctx.footing_frame_name.stop.tokenIndex,
            )
            if ctx.footing_frame_name
            else None
        )

        footer_line_number = (
            get_original_code_content(
                ctx.parser,
                ctx.footing_line_number.start.tokenIndex,
                ctx.footing_line_number.stop.tokenIndex,
            )
            if ctx.footing_line_number
            else None
        )

        header_frame_name = (
            get_original_code_content(
                ctx.parser,
                ctx.heading_frame_name.start.tokenIndex,
                ctx.heading_frame_name.stop.tokenIndex,
            )
            if ctx.heading_frame_name
            else None
        )

        header_line_number = (
            get_original_code_content(
                ctx.parser,
                ctx.heading_line_number.start.tokenIndex,
                ctx.heading_line_number.stop.tokenIndex,
            )
            if ctx.heading_line_number
            else None
        )

        routine_call = (
            get_original_code_content(
                ctx.parser,
                ctx.routineCall().start.tokenIndex,
                ctx.routineCall().stop.tokenIndex,
            )
            if ctx.routineCall()
            else None
        )

        statement = self.extract_statement(
            ctx,
            OnChangeStatement,
            controlling_variable=controlling_variable,
            as_literal=as_literal,
            footer_frame_name=footer_frame_name,
            footer_line_number=footer_line_number,
            header_frame_name=header_frame_name,
            header_line_number=header_line_number,
            routine_call=routine_call,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#routineCall.
    def visitRoutineCall(self, ctx: LDLPParser.RoutineCallContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#pageStatement.
    def visitPageStatement(self, ctx: LDLPParser.PageStatementContext):
        try:
            statement = self.assessPageStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )

        return self.visitChildren(ctx)

    def assessPageStatement(self, ctx: LDLPParser.PageStatementContext):
        destination_page_number = get_original_code_content(
            ctx.parser,
            ctx.pageNumber().start.tokenIndex,
            ctx.pageNumber().stop.tokenIndex,
        )

        variable_to_destination_page = get_original_code_content(
            ctx.parser,
            ctx.varName().start.tokenIndex,
            ctx.varName().stop.tokenIndex,
        )

        statement = self.extract_statement(
            ctx,
            PageStatement,
            destination_page_number=destination_page_number,
            variable_to_destination_page=variable_to_destination_page,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#recallStatement.
    def visitRecallStatement(self, ctx: LDLPParser.RecallStatementContext):
        try:
            statement = self.assessRecallStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessRecallStatement(self, ctx: LDLPParser.RecallStatementContext):
        object_name = (
            get_original_code_content(
                ctx.parser,
                ctx.expression(0).start.tokenIndex,
                ctx.expression(0).stop.tokenIndex,
            )
            if ctx.expression()
            else None
        )
        is_recall_bye = ctx.BYE() is not None
        is_recall_exit = ctx.EXIT() is not None
        teach_screen = (
            get_original_code_content(
                ctx.parser,
                ctx.expression(1).start.tokenIndex,
                ctx.expression(1).stop.token,
            )
            if len(ctx.expression()) > 1
            else None
        )

        statement = self.extract_statement(
            ctx,
            RecallStatement,
            object_name=object_name,
            is_recall_bye=is_recall_bye,
            is_recall_exit=is_recall_exit,
            teach_screen=teach_screen,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#releaseStatement.
    def visitReleaseStatement(self, ctx: LDLPParser.ReleaseStatementContext):
        try:
            statement = self.assessReleaseStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )

        return self.visitChildren(ctx)

    def assessReleaseStatement(self, ctx: LDLPParser.ReleaseStatementContext):
        report_name = (
            get_original_code_content(
                ctx.parser,
                ctx.reportName().start.tokenIndex,
                ctx.reportName().stop.tokenIndex,
            )
            if ctx.reportName()
            else None
        )

        statement = self.extract_statement(
            ctx,
            ReleaseStatement,
            report_name=report_name,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#restartStatement.
    def visitRestartStatement(self, ctx: LDLPParser.RestartStatementContext):
        try:
            statement = self.assessRestartStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )

        return self.visitChildren(ctx)

    def assessRestartStatement(self, ctx: LDLPParser.RestartStatementContext):
        profile_name = get_original_code_content(
            ctx.parser,
            ctx.profileName().start.tokenIndex,
            ctx.profileName().stop.tokenIndex,
        )

        statement = self.extract_statement(
            ctx,
            RestartStatement,
            profile_name=profile_name,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#rocStatement.
    def visitRocStatement(self, ctx: LDLPParser.RocStatementContext):
        try:
            statement = self.assessRocStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessRocStatement(self, ctx: LDLPParser.RocStatementContext):
        name = get_original_code_content(
            ctx.parser,
            ctx.expression(0).start.tokenIndex,
            ctx.expression(0).stop.tokenIndex,
        )
        roc_command = (
            get_original_code_content(
                ctx.parser,
                ctx.expression(1).start.tokenIndex,
                ctx.expression(1).stop.tokenIndex,
            )
            if ctx.expression(1)
            else None
        )

        statement = self.extract_statement(
            ctx,
            RocStatement,
            name=name,
            roc_command=roc_command,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#returnStatement.
    def visitReturnStatement(self, ctx: LDLPParser.ReturnStatementContext):
        try:
            statement = self.assessReturnStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessReturnStatement(self, ctx: LDLPParser.ReturnStatementContext):
        return_value = (
            get_original_code_content(
                ctx.parser,
                ctx.getChild(1).start.tokenIndex,
                ctx.getChild(1).stop.tokenIndex,
            )
            if ctx.getChild(1)
            else None
        )

        statement = self.extract_statement(
            ctx,
            ReturnStatement,
            return_value=return_value,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#instance.
    def visitInstance(self, ctx: LDLPParser.InstanceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#interface.
    def visitInterface(self, ctx: LDLPParser.InterfaceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#runStatement.
    def visitRunStatement(self, ctx: LDLPParser.RunStatementContext):
        try:
            statement = self.assessRunStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessRunStatement(self, ctx: LDLPParser.RunStatementContext):
        report_name = get_original_code_content(
            ctx.parser,
            ctx.getChild(1).start.tokenIndex,
            ctx.getChild(1).stop.tokenIndex,
        )
        output_device = (
            get_original_code_content(
                ctx.parser,
                ctx.device().start.tokenIndex,
                ctx.device().stop.tokenIndex,
            )
            if ctx.device()
            else None
        )
        is_trace = ctx.TRACE() is not None
        initial_language = (
            get_original_code_content(
                ctx.parser,
                ctx.initial_language.start.tokenIndex,
                ctx.initial_language.stop.tokenIndex,
            )
            if ctx.initial_language
            else None
        )
        parameter = (
            get_original_code_content(
                ctx.parser,
                ctx.parameter.start.tokenIndex,
                ctx.parameter.stop.tokenIndex,
            )
            if ctx.parameter
            else None
        )

        statement = self.extract_statement(
            ctx,
            RunStatement,
            report_name=report_name,
            output_device=output_device,
            is_trace=is_trace,
            initial_language=initial_language,
            parameter=parameter,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#device.
    def visitDevice(self, ctx: LDLPParser.DeviceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#sleepStatement.
    def visitSleepStatement(self, ctx: LDLPParser.SleepStatementContext):
        try:
            statement = self.assessSleepStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessSleepStatement(self, ctx: LDLPParser.SleepStatementContext):
        suspend_time = get_original_code_content(
            ctx.parser,
            ctx.getChild(1).start.tokenIndex,
            ctx.getChild(1).stop.tokenIndex,
        )

        is_no_commit = ctx.NO_COMMIT() is not None

        statement = self.extract_statement(
            ctx,
            SleepStatement,
            suspend_time=suspend_time,
            is_no_commit=is_no_commit,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#startStatement.
    def visitStartStatement(self, ctx: LDLPParser.StartStatementContext):
        try:
            statement = self.assessStartStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessStartStatement(self, ctx: LDLPParser.StartStatementContext):
        program = get_original_code_content(
            ctx.parser,
            ctx.expression(0).start.tokenIndex,
            ctx.expression(0).stop.tokenIndex,
        )
        parameter = (
            get_original_code_content(
                ctx.parser,
                ctx.expression(1).start.tokenIndex,
                ctx.expression(1).stop.tokenIndex,
            )
            if ctx.expression(1)
            else None
        )

        statement = self.extract_statement(
            ctx,
            StartStatement,
            program=program,
            parameter=parameter,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#sendListDynamicStatement.
    def visitSendListDynamicStatement(
        self, ctx: LDLPParser.SendListDynamicStatementContext
    ):
        try:
            statement = self.assessSendListDynamicStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessSendListDynamicStatement(
        self, ctx: LDLPParser.SendListDynamicStatementContext
    ):
        list_box_name = get_original_code_content(
            ctx.parser,
            ctx.expression().start.tokenIndex,
            ctx.expression().stop.tokenIndex,
        )
        variable_add_to_list_box = get_original_code_content(
            ctx.parser,
            ctx.variable().start.tokenIndex,
            ctx.variable().stop.tokenIndex,
        )

        statement = self.extract_statement(
            ctx,
            SendListDynamicStatement,
            list_box_name=list_box_name,
            variable_add_to_list_box=variable_add_to_list_box,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#sendListStaticStatement.
    def visitSendListStaticStatement(
        self, ctx: LDLPParser.SendListStaticStatementContext
    ):
        try:
            statement = self.assessSendListStaticStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessSendListStaticStatement(
        self, ctx: LDLPParser.SendListStaticStatementContext
    ):
        list_box_name = get_original_code_content(
            ctx.parser,
            ctx.expression().start.tokenIndex,
            ctx.expression().stop.tokenIndex,
        )
        download_file = (
            get_original_code_content(
                ctx.parser,
                ctx.downloadFile().start.tokenIndex,
                ctx.downloadFile().stop.tokenIndex,
            )
            if ctx.downloadFile()
            else None
        )
        pack_name = (
            get_original_code_content(
                ctx.parser,
                ctx.FILE().start.tokenIndex,
                ctx.FILE().stop.tokenIndex,
            )
            if ctx.FILE()
            else None
        )
        existing_extract_file = (
            get_original_code_content(
                ctx.parser,
                ctx.extractFile().start.tokenIndex,
                ctx.extractFile().stop.tokenIndex,
            )
            if ctx.extractFile()
            else None
        )

        statement = self.extract_statement(
            ctx,
            SendListStaticStatement,
            list_box_name=list_box_name,
            download_file=download_file,
            pack_name=pack_name,
            existing_extract_file=existing_extract_file,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#downloadFile.
    def visitDownloadFile(self, ctx: LDLPParser.DownloadFileContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#sendMessageStatement.
    def visitSendMessageStatement(self, ctx: LDLPParser.SendMessageStatementContext):
        try:
            statement = self.assessSendMessageStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessSendMessageStatement(self, ctx: LDLPParser.SendMessageStatementContext):
        receiver = get_original_code_content(
            ctx.parser,
            ctx.getChild(1).start.tokenIndex,
            ctx.getChild(1).stop.tokenIndex,
        )
        message = get_original_code_content(
            ctx.parser,
            ctx.getChild(2).start.tokenIndex,
            ctx.getChild(2).stop.tokenIndex,
        )

        statement = self.extract_statement(
            ctx,
            SendMessageStatement,
            receiver=receiver,
            message=message,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#sendPrintStatement.
    def visitSendPrintStatement(self, ctx: LDLPParser.SendPrintStatementContext):
        try:
            statement = self.assessSendPrintStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessSendPrintStatement(self, ctx: LDLPParser.SendPrintStatementContext):
        report_name = (
            get_original_code_content(
                ctx.parser,
                ctx.reportName().start.tokenIndex,
                ctx.reportName().stop.tokenIndex,
            )
            if ctx.reportName()
            else None
        )
        device = (
            get_original_code_content(
                ctx.parser,
                ctx.device().start.tokenIndex,
                ctx.device().stop.tokenIndex,
            )
            if ctx.device()
            else None
        )
        output_device = (
            get_original_code_content(
                ctx.parser,
                ctx.output_device.start.tokenIndex,
                ctx.output_device.stop.tokenIndex,
            )
            if ctx.output_device
            else None
        )
        at_expression = (
            get_original_code_content(
                ctx.parser,
                ctx.at_expr.start.tokenIndex,
                ctx.at_expr.stop.tokenIndex,
            )
            if ctx.at_expr
            else None
        )

        statement = self.extract_statement(
            ctx,
            SendPrintStatement,
            report_name=report_name,
            device=device,
            output_device=output_device,
            at_expression=at_expression,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#setDBStatement.
    def visitSetDBStatement(self, ctx: LDLPParser.SetDBStatementContext):
        try:
            statement = self.assessSetDBStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessSetDBStatement(self, ctx: LDLPParser.SetDBStatementContext):
        db_name = get_original_code_content(
            ctx.parser,
            ctx.dbName().start.tokenIndex,
            ctx.dbName().stop.tokenIndex,
        )
        class_name = (
            get_original_code_content(
                ctx.parser,
                ctx.className().start.tokenIndex,
                ctx.className().stop.tokenIndex,
            )
            if ctx.className()
            else None
        )
        is_all_classes = ctx.ALL() is not None

        statement = self.extract_statement(
            ctx,
            SetDBStatement,
            db_name=db_name,
            class_name=class_name,
            is_all_classes=is_all_classes,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#setTitleStatement.
    def visitSetTitleStatement(self, ctx: LDLPParser.SetTitleStatementContext):
        try:
            statement = self.assessSetTitleStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessSetTitleStatement(self, ctx: LDLPParser.SetTitleStatementContext):
        extract_file = get_original_code_content(
            ctx.parser,
            ctx.extractFile().start.tokenIndex,
            ctx.extractFile().stop.tokenIndex,
        )
        name_assign_to_file = get_original_code_content(
            ctx.parser,
            ctx.expression(0).start.tokenIndex,
            ctx.expression(0).stop.tokenIndex,
        )
        pack_name = (
            get_original_code_content(
                ctx.parser,
                ctx.expression(1).start.tokenIndex,
                ctx.expression(1).stop.tokenIndex,
            )
            if ctx.expression(1)
            else None
        )
        is_exist = ctx.EXIST() is not None

        statement = self.extract_statement(
            ctx,
            SetTitleStatement,
            extract_file=extract_file,
            name_assign_to_file=name_assign_to_file,
            pack_name=pack_name,
            is_exist=is_exist,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#stninfoStatement.
    def visitStninfoStatement(self, ctx: LDLPParser.StninfoStatementContext):
        try:
            statement = self.assessStnInfoStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessStnInfoStatement(self, ctx: LDLPParser.StninfoStatementContext):
        name = get_original_code_content(
            ctx.parser,
            ctx.expression().start.tokenIndex,
            ctx.expression().stop.tokenIndex,
        )
        variable_receive_request_info = get_original_code_content(
            ctx.parser,
            ctx.variable().start.tokenIndex,
            ctx.variable().stop.tokenIndex,
        )

        statement = self.extract_statement(
            ctx,
            StnInfoStatement,
            name=name,
            variable_receive_request_info=variable_receive_request_info,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#subtractStatement.
    def visitSubtractStatement(self, ctx: LDLPParser.SubtractStatementContext):
        try:
            statement = self.assessSubtractStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessSubtractStatement(self, ctx: LDLPParser.SubtractStatementContext):
        minuend = get_original_code_content(
            ctx.parser,
            ctx.expression().start.tokenIndex,
            ctx.expression().stop.tokenIndex,
        )
        subtrahend = get_original_code_content(
            ctx.parser,
            ctx.variable(0).start.tokenIndex,
            ctx.variable(0).stop.tokenIndex,
        )
        results = (
            get_original_code_content(
                ctx.parser,
                ctx.variable(1).start.tokenIndex,
                ctx.variable(1).stop.tokenIndex,
            )
            if len(ctx.variable()) > 1
            else subtrahend
        )
        is_rounded = ctx.ROUNDED() is not None
        gs_status = (
            get_original_code_content(
                ctx.parser,
                ctx.status().start.tokenIndex,
                ctx.status().stop.tokenIndex,
            )
            if ctx.status()
            else None
        )

        statement = self.extract_statement(
            ctx,
            SubtractStatement,
            minuend=minuend,
            subtrahend=subtrahend,
            results=results,
            is_rounded=is_rounded,
            gs_status=gs_status,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#switchtoStatement.
    def visitSwitchtoStatement(self, ctx: LDLPParser.SwitchtoStatementContext):
        try:
            statement = self.assessSwitchToStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessSwitchToStatement(self, ctx: LDLPParser.SwitchtoStatementContext):
        destination_system_name = get_original_code_content(
            ctx.parser,
            ctx.expression().start.tokenIndex,
            ctx.expression().stop.tokenIndex,
        )
        data_pass_to_target_system = (
            get_original_code_content(
                ctx.parser,
                ctx.data.start.tokenIndex,
                ctx.data.stop.tokenIndex,
            )
            if ctx.data
            else None
        )
        partition_name = (
            get_original_code_content(
                ctx.parser,
                ctx.partition.start.tokenIndex,
                ctx.partition.stop.tokenIndex,
            )
            if ctx.partition
            else None
        )
        is_log_off_from_origin_application = ctx.BYE() is not None
        is_clear = ctx.CLEAR() is not None
        is_inherit = ctx.INHERIT() is not None

        statement = self.extract_statement(
            ctx,
            SwitchToStatement,
            destination_system_name=destination_system_name,
            data_pass_to_target_system=data_pass_to_target_system,
            partition_name=partition_name,
            is_log_off_from_origin_application=is_log_off_from_origin_application,
            is_clear=is_clear,
            is_inherit=is_inherit,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#wakeStatement.
    def visitWakeStatement(self, ctx: LDLPParser.WakeStatementContext):
        try:
            statement = self.assessWakeStatement(ctx)
            self.statements.append(statement)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.warning(
                f"Cannot assess statement {type(ctx)}: {ctx.getText()}, skipping"
            )
        return self.visitChildren(ctx)

    def assessWakeStatement(self, ctx: LDLPParser.WakeStatementContext):
        report_name = get_original_code_content(
            ctx.parser,
            ctx.reportName().start.tokenIndex,
            ctx.reportName().stop.tokenIndex,
        )
        data_pass_to_report = (
            get_original_code_content(
                ctx.parser,
                ctx.expression().start.tokenIndex,
                ctx.expression().stop.tokenIndex,
            )
            if ctx.expression()
            else None
        )
        gs_status = (
            get_original_code_content(
                ctx.parser,
                ctx.status().start.tokenIndex,
                ctx.status().stop.tokenIndex,
            )
            if ctx.status()
            else None
        )

        statement = self.extract_statement(
            ctx,
            WakeStatement,
            report_name=report_name,
            data_pass_to_report=data_pass_to_report,
            gs_status=gs_status,
        )

        return statement

    # Visit a parse tree produced by LDLPParser#relational_operator.
    def visitRelational_operator(self, ctx: LDLPParser.Relational_operatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#logical_operator.
    def visitLogical_operator(self, ctx: LDLPParser.Logical_operatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#status.
    def visitStatus(self, ctx: LDLPParser.StatusContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#dbName.
    def visitDbName(self, ctx: LDLPParser.DbNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#fileName.
    def visitFileName(self, ctx: LDLPParser.FileNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#dateFormat.
    def visitDateFormat(self, ctx: LDLPParser.DateFormatContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#className.
    def visitClassName(self, ctx: LDLPParser.ClassNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#varName.
    def visitVarName(self, ctx: LDLPParser.VarNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#objectName.
    def visitObjectName(self, ctx: LDLPParser.ObjectNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#userCode.
    def visitUserCode(self, ctx: LDLPParser.UserCodeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#frameName.
    def visitFrameName(self, ctx: LDLPParser.FrameNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#lineNumber.
    def visitLineNumber(self, ctx: LDLPParser.LineNumberContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#pageNumber.
    def visitPageNumber(self, ctx: LDLPParser.PageNumberContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#reportName.
    def visitReportName(self, ctx: LDLPParser.ReportNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#profileName.
    def visitProfileName(self, ctx: LDLPParser.ProfileNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#deviceName.
    def visitDeviceName(self, ctx: LDLPParser.DeviceNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#keywords.
    def visitKeywords(self, ctx: LDLPParser.KeywordsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#specialName.
    def visitSpecialName(self, ctx: LDLPParser.SpecialNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#variable.
    def visitVariable(self, ctx: LDLPParser.VariableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#identifier.
    def visitIdentifier(self, ctx: LDLPParser.IdentifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LDLPParser#literal.
    def visitLiteral(self, ctx: LDLPParser.LiteralContext):
        return self.visitChildren(ctx)
