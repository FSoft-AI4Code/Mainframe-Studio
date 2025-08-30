from typing import Optional, Type, TypeVar

from antlr4 import ParserRuleContext, TerminalNode

from .IBM_JCLParser import IBM_JCLParser
from .IBM_JCLVisitor import IBM_JCLVisitor
from .jcl_schema import (
    DdStatement,
    ExecStatement,
)
from ..utils import get_original_code_content
from ...utils import CodeBlock

T = TypeVar("T", bound=ParserRuleContext)


class MyIBM_JCLVisitor(IBM_JCLVisitor):

    def __init__(self, parser: IBM_JCLParser) -> None:
        super().__init__()

        self.parser = parser

        self.num_conditions = 0
        self.is_vsam = False
        self.params_list: list[str] = []
        self.dataset_list: list[dict[str, str]] = []
        self.exec_statement_list: list[CodeBlock] = []
        self.job_statement_list: list[CodeBlock] = []
        self.proc_statement_list: list[CodeBlock] = []
        self.jcl_lib_statement_list: list[CodeBlock] = []
        self.set_statement_list: list[CodeBlock] = []
        self.exec_statement_map: dict[str, ExecStatement] = {}

    # Visit a parse tree produced by IBM_JCLParser#program.
    def visitProgram(self, ctx: IBM_JCLParser.ProgramContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#statement.
    def visitStatement(self, ctx: IBM_JCLParser.StatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#inline.
    def visitInline(self, ctx: IBM_JCLParser.InlineContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#inline2.
    def visitInline2(self, ctx: IBM_JCLParser.Inline2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#inlineContent.
    def visitInlineContent(self, ctx: IBM_JCLParser.InlineContentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#continueStatement.
    def visitContinueStatement(self, ctx: IBM_JCLParser.ContinueStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#jobStatement.
    def visitJobStatement(self, ctx: IBM_JCLParser.JobStatementContext):
        self.job_statement_list.append(
            CodeBlock(
                content=ctx.getText(),
                start_line=ctx.start.line,
                end_line=ctx.stop.line,
            )
        )
        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#jobParameters.
    def visitJobParameters(self, ctx: IBM_JCLParser.JobParametersContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#jobParam.
    def visitJobParam(self, ctx: IBM_JCLParser.JobParamContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#jobParamName.
    def visitJobParamName(self, ctx: IBM_JCLParser.JobParamNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#jobParamValue.
    def visitJobParamValue(self, ctx: IBM_JCLParser.JobParamValueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#execStatement.
    def visitExecStatement(self, ctx: IBM_JCLParser.ExecStatementContext):
        code = CodeBlock(
            content=ctx.getText(),
            start_line=ctx.start.line,
            end_line=ctx.stop.line,
        )
        self.exec_statement_list.append(code)

        step_name = ctx.getChild(1).getText()

        # parameter dictionary with keys are the parameter names, values are parameter values
        param_map: dict[str, str] = {}

        for child in ctx.getChildren():
            if not isinstance(child, IBM_JCLParser.ExecParametersContext):
                continue
            for grandchild in child.getChildren():
                if not isinstance(grandchild, IBM_JCLParser.ExecParamContext):
                    continue
                program_found = False

                for great_grandchild in grandchild.getChildren():
                    if isinstance(great_grandchild, IBM_JCLParser.ExecParamNameContext):
                        if great_grandchild.getText().strip() == "PGM":
                            program_found = True
                    elif isinstance(
                        great_grandchild, IBM_JCLParser.ExecParamValueContext
                    ):
                        if (
                            program_found
                            and great_grandchild.getText().strip() == "IDCAMS"
                        ):
                            self.is_vsam = True
                param: str = grandchild.getText()
                self.params_list.append(param)

                # extract exec parameter key and value
                param_name_value = param.split("=")

                if len(param_name_value) == 1:
                    # if the parameter name is omit, the compiler will refer it to PROC
                    # https://www.ibm.com/docs/en/zos-basic-skills?topic=do-jcl-exec-statements-positional-frequently-used-parameters#:~:text=If%20you%20omit%20the%20PGM%20or%20PROC%20parameter%2C%20z/OS%20automatically%20assumes%20that%20you%20are%20specifying%20a%20procedure%20that%20you%20want%20to%20run.
                    param_map["PROC"] = param_name_value[0]
                else:
                    for i in range(0, len(param_name_value), 2):
                        if i + 1 >= len(param_name_value):
                            # Handle cases where there's a parameter name without a value
                            param_name = param_name_value[i]
                            param_value = ""
                        else:
                            param_name = param_name_value[i]
                            param_value = param_name_value[i + 1]

                        param_map[param_name] = param_value

                if "COND" in param:
                    self.num_conditions += 1

        exec_statement = ExecStatement(
            step_name=step_name, parameters_map=param_map, code=code, statements=[]
        )
        self.exec_statement_map[step_name] = exec_statement

        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#execParameters.
    def visitExecParameters(self, ctx: IBM_JCLParser.ExecParametersContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#execParam.
    def visitExecParam(self, ctx: IBM_JCLParser.ExecParamContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#execParamName.
    def visitExecParamName(self, ctx: IBM_JCLParser.ExecParamNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#execParamValue.
    def visitExecParamValue(self, ctx: IBM_JCLParser.ExecParamValueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#jcllibStatement.
    def visitJcllibStatement(self, ctx: IBM_JCLParser.JcllibStatementContext):
        self.jcl_lib_statement_list.append(
            CodeBlock(
                content=ctx.getText(),
                start_line=ctx.start.line,
                end_line=ctx.stop.line,
            )
        )
        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#setStatement.
    def visitSetStatement(self, ctx: IBM_JCLParser.SetStatementContext):
        self.set_statement_list.append(
            CodeBlock(
                content=ctx.getText(),
                start_line=ctx.start.line,
                end_line=ctx.stop.line,
            )
        )
        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#procStatement.
    def visitProcStatement(self, ctx: IBM_JCLParser.ProcStatementContext):
        self.proc_statement_list.append(
            CodeBlock(
                content=ctx.getText(),
                start_line=ctx.start.line,
                end_line=ctx.stop.line,
            )
        )
        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#procParameters.
    def visitProcParameters(self, ctx: IBM_JCLParser.ProcParametersContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#procParam.
    def visitProcParam(self, ctx: IBM_JCLParser.ProcParamContext):
        return self.visitChildren(ctx)

    def recursive_find_first_child_by_type(
        self, current: ParserRuleContext, type: Type[T]
    ) -> Optional[T]:
        if isinstance(current, TerminalNode):
            return None

        if isinstance(current, type):
            return current

        for child in current.getChildren():
            match = self.recursive_find_first_child_by_type(child, type)

            if match:
                return match

        return None

    def find_all_child_by_type(
        self, current: ParserRuleContext, type: Type[T]
    ) -> list[T]:
        result: list[T] = []

        if isinstance(current, TerminalNode):
            return result

        if isinstance(current, type):
            result.append(current)
        for child in current.getChildren():
            result.extend(self.find_all_child_by_type(child, type))
        return result

    def find_parent_by_type(
        self, node: ParserRuleContext, type: Type[T]
    ) -> Optional[T]:
        current = node

        while True:
            if isinstance(current, type):
                return current

            if current.parentCtx:
                current = current.parentCtx
            else:
                return None

    # Visit a parse tree produced by IBM_JCLParser#ddStatement.
    def visitDdStatement(self, ctx: IBM_JCLParser.DdStatementContext):
        dd_param_list = self.find_all_child_by_type(
            ctx, IBM_JCLParser.DdParametersContext
        )
        # TODO fix parameters context

        param_map: dict[str, str] = {}

        dd_name = self.recursive_find_first_child_by_type(
            ctx, IBM_JCLParser.CnameContext
        )

        dd_dataset_map_list: list[dict[str, str]] = []

        unnamed_parameter_count = 0
        unnamed_parameter_name = "UNNAMED"

        for dd_param in dd_param_list:
            # lines that only have '//'
            if dd_param.getText() == "//":
                continue

            for i, child in enumerate(dd_param.getChildren()):
                if (
                    i == 0
                    and isinstance(child, TerminalNode)
                    and child.getText() == "*"
                ):
                    # The '*' parameter value does not have parameter name
                    unnamed_parameter_count += 1
                    param_map[f"{unnamed_parameter_name}_{unnamed_parameter_count}"] = (
                        "*"
                    )

                elif isinstance(child, IBM_JCLParser.DdParamContext):
                    # The paramter with name and value
                    dd_param_name = self.recursive_find_first_child_by_type(
                        child, IBM_JCLParser.DdParamNameContext
                    )

                    dd_param_value = self.recursive_find_first_child_by_type(
                        dd_param, IBM_JCLParser.ParamValueContext
                    )

                    if dd_param_name:
                        param_map[dd_param_name.getText(
                        )] = dd_param_value.getText()
                    else:
                        unnamed_parameter_count += 1

                        param_map[
                            f"{unnamed_parameter_name}_{unnamed_parameter_count}"
                        ] = dd_param_value.getText()

                    if not dd_param_name or dd_param_name.getText().upper() != "DSN":
                        continue

                    if not dd_param_value:
                        raise RuntimeError(
                            f"The syntax for the DD statement is invalid. The DSN parameter value is missing for statement {ctx.getText()}"
                        )

                    if not dd_name:
                        # raise ValueError(
                        #     f"The syntax for the DD statement is invalid. The variable name of the dataset {dd_param_value.getText()} is missing for statement {ctx.getText()}"
                        # )
                        variable_name = "UNKNOWN"
                    else:
                        variable_name = dd_name.getText()

                    # if variable_name.upper() == "STEPLIB":
                    #     continue

                    exec_statement_context = self.find_parent_by_type(
                        ctx, IBM_JCLParser.ExecStatementContext
                    )

                    if not exec_statement_context:
                        raise ValueError(
                            f"The syntax for the DD statement is invalid. The exec statement for statement '{ctx.getText()}' is missing"
                        )

                    exec_param_value = self.recursive_find_first_child_by_type(
                        exec_statement_context, IBM_JCLParser.ExecParamValueContext
                    )

                    if not exec_param_value:
                        raise ValueError(
                            f"The program name is missing in the exec statement '{exec_statement_context.getText()}'"
                        )

                    dataset_name = dd_param_value.getText()
                    dd_statement = child.getText()
                    program_id = exec_param_value.getText()

                    dataset = {
                        "dataset_name": dataset_name,
                        "variable_name": variable_name,
                        "dd_statement": dd_statement,
                        "program_id": program_id,
                    }

                    dd_dataset_map_list.append(dataset)
                    self.dataset_list.append(dataset)

        logic = None
        inline_context_list = self.find_all_child_by_type(
            ctx, IBM_JCLParser.InlineContext
        )
        for inline_context in inline_context_list:
            if logic is None:
                logic = ""
            logic += get_original_code_content(
                self.parser,
                inline_context.start.tokenIndex,
                inline_context.stop.tokenIndex,
            )

        dd_statement = DdStatement(
            ddname=dd_name.getText() if dd_name else "",
            parameters_map=param_map,
            dataset_map_list=dd_dataset_map_list,
            logic=logic,
        )

        exec_statement_context = self.find_parent_by_type(
            ctx, IBM_JCLParser.ExecStatementContext
        )

        if exec_statement_context is None:
            raise ValueError(
                f"The exec statement of the DD statement '{ctx.getText()}' is missing"
            )

        step_name = exec_statement_context.getChild(1).getText()
        exec_statement = self.exec_statement_map.get(step_name)

        if exec_statement is None:
            raise ValueError(
                f"The record of the exec statement '{exec_statement_context.getText()}' in exec_statement_map is missing"
            )

        exec_statement.statements.append(dd_statement)

        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#keyword.
    def visitKeyword(self, ctx: IBM_JCLParser.KeywordContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#ddParameters.
    def visitDdParameters(self, ctx: IBM_JCLParser.DdParametersContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#ddParam.
    def visitDdParam(self, ctx: IBM_JCLParser.DdParamContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#ddParamName.
    def visitDdParamName(self, ctx: IBM_JCLParser.DdParamNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#ddParamValue.
    def visitDdParamValue(self, ctx: IBM_JCLParser.DdParamValueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#paramValueList.
    def visitParamValueList(self, ctx: IBM_JCLParser.ParamValueListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#paramValue.
    def visitParamValue(self, ctx: IBM_JCLParser.ParamValueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#cname.
    def visitCname(self, ctx: IBM_JCLParser.CnameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#idxNumber.
    def visitIdxNumber(self, ctx: IBM_JCLParser.IdxNumberContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#avalue.
    def visitAvalue(self, ctx: IBM_JCLParser.AvalueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#value.
    def visitValue(self, ctx: IBM_JCLParser.ValueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#accessName.
    def visitAccessName(self, ctx: IBM_JCLParser.AccessNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by IBM_JCLParser#comment.
    def visitComment(self, ctx: IBM_JCLParser.CommentContext):
        return self.visitChildren(ctx)
