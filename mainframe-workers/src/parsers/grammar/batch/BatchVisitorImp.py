from typing import List

from parsers.grammar.batch.batch_schemas import (
    BatchLabel,
    BsortexStatement,
    CallStatement,
    DelStatement,
    EchoStatement,
    EndlocalStatement,
    ExecStatement,
    ExitStatement,
    ForStatement,
    GotoStatement,
    IfStatement,
    MkdirStatement,
    PauseStatement,
    RemStatement,
    RmdirStatement,
    SetLocalStatement,
    SetStatement,
    TypeStatement,
    XcopyStatement,
    Z7Statement,
)
from parsers.grammar.batch.BatchParser import BatchParser
from parsers.grammar.batch.BatchVisitor import BatchVisitor
from parsers.grammar.utils import get_original_code_content


class BatchVisitorImp(BatchVisitor):
    def __init__(self):
        self.labels: List[BatchLabel] = []

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
            **kwargs
        )
        return statement

    # Visit a parse tree produced by BatchParser#startRule.
    def visitStartRule(self, ctx: BatchParser.StartRuleContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BatchParser#label.
    def visitLabel(self, ctx: BatchParser.LabelContext):
        label_name = get_original_code_content(
            ctx.parser,
            ctx.labelName().start.tokenIndex,
            ctx.labelName().stop.tokenIndex,
        )
        start_line = ctx.start.line
        stop_line = ctx.stop.line
        statements = []
        for statement_ctx in ctx.statement():
            statement = self.visit(statement_ctx)
            statements.append(statement)
        label = BatchLabel(
            label_name=label_name,
            start_line=start_line,
            stop_line=stop_line,
            statements=statements,
        )
        self.labels.append(label)
        return label

    # Visit a parse tree produced by BatchParser#labelName.
    def visitLabelName(self, ctx: BatchParser.LabelNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BatchParser#statement.
    def visitStatement(self, ctx: BatchParser.StatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BatchParser#z7Statement.
    def visitZ7Statement(self, ctx: BatchParser.Z7StatementContext):
        file_path = get_original_code_content(
            ctx.parser, ctx.filePath().start.tokenIndex, ctx.filePath().stop.tokenIndex
        )
        command = get_original_code_content(
            ctx.parser,
            ctx.z7Command().start.tokenIndex,
            ctx.z7Command().stop.tokenIndex,
        )
        switches = [
            get_original_code_content(
                ctx.parser, switch.start.tokenIndex, switch.stop.tokenIndex
            )
            for switch in ctx.z7Switches().z7Switch()
        ]
        return self.extract_statement(
            ctx, Z7Statement, file_path=file_path, command=command, switches=switches
        )

    # Visit a parse tree produced by BatchParser#echoStatement.
    def visitEchoStatement(self, ctx: BatchParser.EchoStatementContext):
        message = get_original_code_content(
            ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex
        )
        message = message.replace("echo", "").strip()
        return self.extract_statement(ctx, EchoStatement, message=message)

    # Visit a parse tree produced by BatchParser#remStatement.
    def visitRemStatement(self, ctx: BatchParser.RemStatementContext):
        comment = get_original_code_content(
            ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex
        )
        comment = comment.replace("rem", "").strip()
        return self.extract_statement(ctx, RemStatement, comment=comment)

    # Visit a parse tree produced by BatchParser#bsortexStatement.
    def visitBsortexStatement(self, ctx: BatchParser.BsortexStatementContext):
        sort_parameters = [
            get_original_code_content(
                ctx.parser, param.start.tokenIndex, param.stop.tokenIndex
            )
            for param in ctx.sortParameters().sortParameter()
        ]
        input_parameters = [
            get_original_code_content(
                ctx.parser, param.start.tokenIndex, param.stop.tokenIndex
            )
            for param in ctx.inputParameters().inputParameter()
        ]
        record_parameters = [
            get_original_code_content(
                ctx.parser, param.start.tokenIndex, param.stop.tokenIndex
            )
            for param in ctx.recordParameters().recordParameter()
        ]
        option_parameters = [
            get_original_code_content(
                ctx.parser, param.start.tokenIndex, param.stop.tokenIndex
            )
            for param in ctx.optionParameters().optionParameter()
        ]
        output_parameters = [
            get_original_code_content(
                ctx.parser, param.start.tokenIndex, param.stop.tokenIndex
            )
            for param in ctx.outputParameters().outputParameter()
        ]
        return self.extract_statement(
            ctx,
            BsortexStatement,
            sort_parameters=sort_parameters,
            input_parameters=input_parameters,
            record_parameters=record_parameters,
            option_parameters=option_parameters,
            output_parameters=output_parameters,
        )

    # Visit a parse tree produced by BatchParser#callStatement.
    def visitCallStatement(self, ctx: BatchParser.CallStatementContext):
        label = (
            get_original_code_content(
                ctx.parser,
                ctx.callWithLabel().labelName().start.tokenIndex,
                ctx.callWithLabel().labelName().stop.tokenIndex,
            )
            if ctx.callWithLabel()
            else None
        )
        file_path = (
            get_original_code_content(
                ctx.parser,
                ctx.callWithFilePath().getChild(0).start.tokenIndex,
                ctx.callWithFilePath().getChild(0).stop.tokenIndex,
            )
            if ctx.callWithFilePath()
            else None
        )

        call_with_file_path = ctx.callWithFilePath()

        if call_with_file_path:
            condition = (
                get_original_code_content(
                    ctx.parser,
                    call_with_file_path.conditionParameter().start.tokenIndex,
                    call_with_file_path.conditionParameter().stop.tokenIndex,
                )
                if call_with_file_path.conditionParameter()
                else None
            )
            parameters = (
                [
                    get_original_code_content(
                        ctx.parser, param.start.tokenIndex, param.stop.tokenIndex
                    )
                    for param in call_with_file_path.batchParameters().batchParameter()
                ]
                if call_with_file_path.batchParameters()
                else []
            )
        else:
            condition = None
            parameters = []

        return self.extract_statement(
            ctx,
            CallStatement,
            label=label,
            file_path=file_path,
            condition=condition,
            parameters=parameters,
        )

    # Visit a parse tree produced by BatchParser#delStatement.
    def visitDelStatement(self, ctx: BatchParser.DelStatementContext):
        file_path = get_original_code_content(
            ctx.parser, ctx.filePath().start.tokenIndex, ctx.filePath().stop.tokenIndex
        )
        return self.extract_statement(ctx, DelStatement, file_path=file_path)

    # Visit a parse tree produced by BatchParser#endlocalStatement.
    def visitEndlocalStatement(self, ctx: BatchParser.EndlocalStatementContext):
        return self.extract_statement(ctx, EndlocalStatement)

    # Visit a parse tree produced by BatchParser#execStatement.
    def visitExecStatement(self, ctx: BatchParser.ExecStatementContext):
        file = get_original_code_content(
            ctx.parser, ctx.execFile().start.tokenIndex, ctx.execFile().stop.tokenIndex
        )
        switches = (
            [
                get_original_code_content(
                    ctx.parser, switch.start.tokenIndex, switch.stop.tokenIndex
                )
                for switch in ctx.switches().switch()
            ]
            if ctx.switches()
            else None
        )
        parameters = (
            [
                get_original_code_content(
                    ctx.parser, param.start.tokenIndex, param.stop.tokenIndex
                )
                for param in ctx.execParameter()
            ]
            if ctx.execParameter()
            else None
        )
        return self.extract_statement(
            ctx, ExecStatement, file=file, switches=switches, parameters=parameters
        )

    # Visit a parse tree produced by BatchParser#exitStatement.
    def visitExitStatement(self, ctx: BatchParser.ExitStatementContext):
        exit_code = (
            get_original_code_content(
                ctx.parser,
                ctx.exitCode().start.tokenIndex,
                ctx.exitCode().stop.tokenIndex,
            )
            if ctx.exitCode()
            else None
        )
        is_exit_current_branch = ctx.exitCurrentBatch() is not None
        return self.extract_statement(
            ctx,
            ExitStatement,
            exit_code=exit_code,
            is_exit_current_branch=is_exit_current_branch,
        )

    # Visit a parse tree produced by BatchParser#forStatement.
    def visitForStatement(self, ctx: BatchParser.ForStatementContext):
        variable = get_original_code_content(
            ctx.parser,
            ctx.forVariable().start.tokenIndex,
            ctx.forVariable().stop.tokenIndex,
        )
        values = [
            get_original_code_content(
                ctx.parser, value.start.tokenIndex, value.stop.tokenIndex
            )
            for value in ctx.forValues().forValue()
        ]
        do_statements = [self.visit(statement) for statement in ctx.forDo().statement()]
        return self.extract_statement(
            ctx,
            ForStatement,
            variable=variable,
            values=values,
            do_statements=do_statements,
        )

    # Visit a parse tree produced by BatchParser#gotoStatement.
    def visitGotoStatement(self, ctx: BatchParser.GotoStatementContext):
        label = (
            get_original_code_content(
                ctx.parser,
                ctx.labelName().start.tokenIndex,
                ctx.labelName().stop.tokenIndex,
            )
            if ctx.labelName()
            else None
        )
        return self.extract_statement(ctx, GotoStatement, label=label)

    # Visit a parse tree produced by BatchParser#ifStatement.
    def visitIfStatement(self, ctx: BatchParser.IfStatementContext):
        condition = get_original_code_content(
            ctx.parser,
            ctx.condition().start.tokenIndex,
            ctx.condition().stop.tokenIndex,
        )
        then_statements = [
            self.visit(statement) for statement in ctx.ifThen().statement()
        ]
        else_statements = (
            [self.visit(statement) for statement in ctx.ifElse().statement()]
            if ctx.ifElse()
            else None
        )
        return self.extract_statement(
            ctx,
            IfStatement,
            condition=condition,
            then_statements=then_statements,
            else_statements=else_statements,
        )

    # Visit a parse tree produced by BatchParser#mkdirStatement.
    def visitMkdirStatement(self, ctx: BatchParser.MkdirStatementContext):
        value = get_original_code_content(
            ctx.parser, ctx.value().start.tokenIndex, ctx.value().stop.tokenIndex
        )
        return self.extract_statement(ctx, MkdirStatement, value=value)

    # Visit a parse tree produced by BatchParser#pauseStatement.
    def visitPauseStatement(self, ctx: BatchParser.PauseStatementContext):
        return self.extract_statement(ctx, PauseStatement)

    # Visit a parse tree produced by BatchParser#rmdirStatement.
    def visitRmdirStatement(self, ctx: BatchParser.RmdirStatementContext):
        value = get_original_code_content(
            ctx.parser, ctx.value().start.tokenIndex, ctx.value().stop.tokenIndex
        )
        switches = (
            [
                get_original_code_content(
                    ctx.parser, switch.start.tokenIndex, switch.stop.tokenIndex
                )
                for switch in ctx.switches().switch()
            ]
            if ctx.switches()
            else None
        )
        return self.extract_statement(
            ctx, RmdirStatement, value=value, switches=switches
        )

    # Visit a parse tree produced by BatchParser#setLocalStatement.
    def visitSetLocalStatement(self, ctx: BatchParser.SetLocalStatementContext):
        option = get_original_code_content(
            ctx.parser,
            ctx.setLocalOption().start.tokenIndex,
            ctx.setLocalOption().stop.tokenIndex,
        )
        return self.extract_statement(ctx, SetLocalStatement, option=option)

    # Visit a parse tree produced by BatchParser#setStatement.
    def visitSetStatement(self, ctx: BatchParser.SetStatementContext):
        switches = (
            [
                get_original_code_content(
                    ctx.parser, switch.start.tokenIndex, switch.stop.tokenIndex
                )
                for switch in ctx.switches().switch()
            ]
            if ctx.switches()
            else []
        )
        source = get_original_code_content(
            ctx.parser,
            ctx.variableName().start.tokenIndex,
            ctx.variableName().stop.tokenIndex,
        )
        target = (
            get_original_code_content(
                ctx.parser,
                ctx.assignmentPart().start.tokenIndex,
                ctx.assignmentPart().stop.tokenIndex,
            )
            if ctx.assignmentPart()
            else None
        )
        return self.extract_statement(
            ctx, SetStatement, switches=switches, source=source, target=target
        )

    # Visit a parse tree produced by BatchParser#typeStatement.
    def visitTypeStatement(self, ctx: BatchParser.TypeStatementContext):
        file_path = ctx.filePath() or ctx.fileName()
        file_path = get_original_code_content(
            ctx.parser, file_path.start.tokenIndex, file_path.stop.tokenIndex
        )
        return self.extract_statement(ctx, TypeStatement, file_path=file_path)

    # Visit a parse tree produced by BatchParser#xcopyStatement.
    def visitXcopyStatement(self, ctx: BatchParser.XcopyStatementContext):
        source = get_original_code_content(
            ctx.parser,
            ctx.xCopySource().start.tokenIndex,
            ctx.xCopySource().stop.tokenIndex,
        )
        destination = get_original_code_content(
            ctx.parser,
            ctx.xCopyDestination().start.tokenIndex,
            ctx.xCopyDestination().stop.tokenIndex,
        )
        switches = (
            [
                get_original_code_content(
                    ctx.parser, switch.start.tokenIndex, switch.stop.tokenIndex
                )
                for switch in ctx.switches().switch()
            ]
            if ctx.switches()
            else []
        )
        return self.extract_statement(
            ctx,
            XcopyStatement,
            source=source,
            destination=destination,
            switches=switches,
        )
