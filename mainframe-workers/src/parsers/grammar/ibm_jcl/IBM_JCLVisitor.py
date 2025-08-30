# Generated from src/parsers/grammar/ibm_jcl/IBM_JCL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .IBM_JCLParser import IBM_JCLParser
else:
    from IBM_JCLParser import IBM_JCLParser

# This class defines a complete generic visitor for a parse tree produced by IBM_JCLParser.

class IBM_JCLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by IBM_JCLParser#startRule.
    def visitStartRule(self, ctx:IBM_JCLParser.StartRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#statement.
    def visitStatement(self, ctx:IBM_JCLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#inlineContent.
    def visitInlineContent(self, ctx:IBM_JCLParser.InlineContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#recordFieldContent.
    def visitRecordFieldContent(self, ctx:IBM_JCLParser.RecordFieldContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#recordField.
    def visitRecordField(self, ctx:IBM_JCLParser.RecordFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#recordFieldParam.
    def visitRecordFieldParam(self, ctx:IBM_JCLParser.RecordFieldParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#generateContent.
    def visitGenerateContent(self, ctx:IBM_JCLParser.GenerateContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#generateParam.
    def visitGenerateParam(self, ctx:IBM_JCLParser.GenerateParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#generateParaName.
    def visitGenerateParaName(self, ctx:IBM_JCLParser.GenerateParaNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#generateParaValue.
    def visitGenerateParaValue(self, ctx:IBM_JCLParser.GenerateParaValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#inlineParameters.
    def visitInlineParameters(self, ctx:IBM_JCLParser.InlineParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#inlineParam.
    def visitInlineParam(self, ctx:IBM_JCLParser.InlineParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#inlineParaName.
    def visitInlineParaName(self, ctx:IBM_JCLParser.InlineParaNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#inlineParaValue.
    def visitInlineParaValue(self, ctx:IBM_JCLParser.InlineParaValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#extentContent.
    def visitExtentContent(self, ctx:IBM_JCLParser.ExtentContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#extentParam.
    def visitExtentParam(self, ctx:IBM_JCLParser.ExtentParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#extentParaName.
    def visitExtentParaName(self, ctx:IBM_JCLParser.ExtentParaNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#extentParaValue.
    def visitExtentParaValue(self, ctx:IBM_JCLParser.ExtentParaValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#tdumpContent.
    def visitTdumpContent(self, ctx:IBM_JCLParser.TdumpContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#processedData.
    def visitProcessedData(self, ctx:IBM_JCLParser.ProcessedDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#systemIdentifier.
    def visitSystemIdentifier(self, ctx:IBM_JCLParser.SystemIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#sortContent.
    def visitSortContent(self, ctx:IBM_JCLParser.SortContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#sortOption.
    def visitSortOption(self, ctx:IBM_JCLParser.SortOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#formatOption.
    def visitFormatOption(self, ctx:IBM_JCLParser.FormatOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#sortFields.
    def visitSortFields(self, ctx:IBM_JCLParser.SortFieldsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#sortField.
    def visitSortField(self, ctx:IBM_JCLParser.SortFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#prtfileContent.
    def visitPrtfileContent(self, ctx:IBM_JCLParser.PrtfileContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#prtFileParameter.
    def visitPrtFileParameter(self, ctx:IBM_JCLParser.PrtFileParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#backUpDatasetContent.
    def visitBackUpDatasetContent(self, ctx:IBM_JCLParser.BackUpDatasetContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#backUpFrom.
    def visitBackUpFrom(self, ctx:IBM_JCLParser.BackUpFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#backUpTo.
    def visitBackUpTo(self, ctx:IBM_JCLParser.BackUpToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#datasetContent.
    def visitDatasetContent(self, ctx:IBM_JCLParser.DatasetContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#datasetOptions.
    def visitDatasetOptions(self, ctx:IBM_JCLParser.DatasetOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#datasetOption.
    def visitDatasetOption(self, ctx:IBM_JCLParser.DatasetOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#datasetList.
    def visitDatasetList(self, ctx:IBM_JCLParser.DatasetListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#datasetName.
    def visitDatasetName(self, ctx:IBM_JCLParser.DatasetNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#ifStatement.
    def visitIfStatement(self, ctx:IBM_JCLParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#thenIf.
    def visitThenIf(self, ctx:IBM_JCLParser.ThenIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#elseIf.
    def visitElseIf(self, ctx:IBM_JCLParser.ElseIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#condition.
    def visitCondition(self, ctx:IBM_JCLParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#andOrCondition.
    def visitAndOrCondition(self, ctx:IBM_JCLParser.AndOrConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#combinableCondition.
    def visitCombinableCondition(self, ctx:IBM_JCLParser.CombinableConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#simpleCondition.
    def visitSimpleCondition(self, ctx:IBM_JCLParser.SimpleConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#conditionOperator.
    def visitConditionOperator(self, ctx:IBM_JCLParser.ConditionOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#calcOperator.
    def visitCalcOperator(self, ctx:IBM_JCLParser.CalcOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#endIf.
    def visitEndIf(self, ctx:IBM_JCLParser.EndIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#joblibStatement.
    def visitJoblibStatement(self, ctx:IBM_JCLParser.JoblibStatementContext):
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


    # Visit a parse tree produced by IBM_JCLParser#includeStatement.
    def visitIncludeStatement(self, ctx:IBM_JCLParser.IncludeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#memberName.
    def visitMemberName(self, ctx:IBM_JCLParser.MemberNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#outputStatement.
    def visitOutputStatement(self, ctx:IBM_JCLParser.OutputStatementContext):
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


    # Visit a parse tree produced by IBM_JCLParser#procEnd.
    def visitProcEnd(self, ctx:IBM_JCLParser.ProcEndContext):
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


    # Visit a parse tree produced by IBM_JCLParser#charDataKeyword.
    def visitCharDataKeyword(self, ctx:IBM_JCLParser.CharDataKeywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#inline.
    def visitInline(self, ctx:IBM_JCLParser.InlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IBM_JCLParser#inline2.
    def visitInline2(self, ctx:IBM_JCLParser.Inline2Context):
        return self.visitChildren(ctx)



del IBM_JCLParser