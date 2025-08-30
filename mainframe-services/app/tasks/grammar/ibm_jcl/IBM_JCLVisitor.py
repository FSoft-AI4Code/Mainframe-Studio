# Generated from .\src\mainframe_migration\parser\grammar\ibm_jcl\IBM_JCL.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .IBM_JCLParser import IBM_JCLParser
else:
    from IBM_JCLParser import IBM_JCLParser

# This class defines a complete generic visitor for a parse tree produced by IBM_JCLParser.

class IBM_JCLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by IBM_JCLParser#program.
    def visitProgram(self, ctx:IBM_JCLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#statement.
    def visitStatement(self, ctx:IBM_JCLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#inline.
    def visitInline(self, ctx:IBM_JCLParser.InlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#inline2.
    def visitInline2(self, ctx:IBM_JCLParser.Inline2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#inlineContent.
    def visitInlineContent(self, ctx:IBM_JCLParser.InlineContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#continueStatement.
    def visitContinueStatement(self, ctx:IBM_JCLParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#jobStatement.
    def visitJobStatement(self, ctx:IBM_JCLParser.JobStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#jobParameters.
    def visitJobParameters(self, ctx:IBM_JCLParser.JobParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#jobParam.
    def visitJobParam(self, ctx:IBM_JCLParser.JobParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#jobParamName.
    def visitJobParamName(self, ctx:IBM_JCLParser.JobParamNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#jobParamValue.
    def visitJobParamValue(self, ctx:IBM_JCLParser.JobParamValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#execStatement.
    def visitExecStatement(self, ctx:IBM_JCLParser.ExecStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#execParameters.
    def visitExecParameters(self, ctx:IBM_JCLParser.ExecParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#execParam.
    def visitExecParam(self, ctx:IBM_JCLParser.ExecParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#execParamName.
    def visitExecParamName(self, ctx:IBM_JCLParser.ExecParamNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#execParamValue.
    def visitExecParamValue(self, ctx:IBM_JCLParser.ExecParamValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#jcllibStatement.
    def visitJcllibStatement(self, ctx:IBM_JCLParser.JcllibStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#setStatement.
    def visitSetStatement(self, ctx:IBM_JCLParser.SetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#procStatement.
    def visitProcStatement(self, ctx:IBM_JCLParser.ProcStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#procParameters.
    def visitProcParameters(self, ctx:IBM_JCLParser.ProcParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#procParam.
    def visitProcParam(self, ctx:IBM_JCLParser.ProcParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#ddStatement.
    def visitDdStatement(self, ctx:IBM_JCLParser.DdStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#keyword.
    def visitKeyword(self, ctx:IBM_JCLParser.KeywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#ddParameters.
    def visitDdParameters(self, ctx:IBM_JCLParser.DdParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#ddParam.
    def visitDdParam(self, ctx:IBM_JCLParser.DdParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#ddParamName.
    def visitDdParamName(self, ctx:IBM_JCLParser.DdParamNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#ddParamValue.
    def visitDdParamValue(self, ctx:IBM_JCLParser.DdParamValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#paramValueList.
    def visitParamValueList(self, ctx:IBM_JCLParser.ParamValueListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#paramValue.
    def visitParamValue(self, ctx:IBM_JCLParser.ParamValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#cname.
    def visitCname(self, ctx:IBM_JCLParser.CnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#idxNumber.
    def visitIdxNumber(self, ctx:IBM_JCLParser.IdxNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#avalue.
    def visitAvalue(self, ctx:IBM_JCLParser.AvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#value.
    def visitValue(self, ctx:IBM_JCLParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#accessName.
    def visitAccessName(self, ctx:IBM_JCLParser.AccessNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#comment.
    def visitComment(self, ctx:IBM_JCLParser.CommentContext):
        return self.visitChildren(ctx)



del IBM_JCLParser