# Generated from ./grammar/batch/Batch.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BatchParser import BatchParser
else:
    from BatchParser import BatchParser

# This class defines a complete generic visitor for a parse tree produced by BatchParser.

class BatchVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BatchParser#startRule.
    def visitStartRule(self, ctx:BatchParser.StartRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#label.
    def visitLabel(self, ctx:BatchParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#labelName.
    def visitLabelName(self, ctx:BatchParser.LabelNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#statement.
    def visitStatement(self, ctx:BatchParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#z7Statement.
    def visitZ7Statement(self, ctx:BatchParser.Z7StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#z7Command.
    def visitZ7Command(self, ctx:BatchParser.Z7CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#z7Switches.
    def visitZ7Switches(self, ctx:BatchParser.Z7SwitchesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#z7Switch.
    def visitZ7Switch(self, ctx:BatchParser.Z7SwitchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#echoStatement.
    def visitEchoStatement(self, ctx:BatchParser.EchoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#remStatement.
    def visitRemStatement(self, ctx:BatchParser.RemStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#bsortexStatement.
    def visitBsortexStatement(self, ctx:BatchParser.BsortexStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#sortParameters.
    def visitSortParameters(self, ctx:BatchParser.SortParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#sortParameter.
    def visitSortParameter(self, ctx:BatchParser.SortParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#sortValue.
    def visitSortValue(self, ctx:BatchParser.SortValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#inputParameters.
    def visitInputParameters(self, ctx:BatchParser.InputParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#inputParameter.
    def visitInputParameter(self, ctx:BatchParser.InputParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#recordParameters.
    def visitRecordParameters(self, ctx:BatchParser.RecordParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#recordParameter.
    def visitRecordParameter(self, ctx:BatchParser.RecordParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#optionParameters.
    def visitOptionParameters(self, ctx:BatchParser.OptionParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#optionParameter.
    def visitOptionParameter(self, ctx:BatchParser.OptionParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#outputParameters.
    def visitOutputParameters(self, ctx:BatchParser.OutputParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#outputParameter.
    def visitOutputParameter(self, ctx:BatchParser.OutputParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#outputValue.
    def visitOutputValue(self, ctx:BatchParser.OutputValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#callStatement.
    def visitCallStatement(self, ctx:BatchParser.CallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#callWithLabel.
    def visitCallWithLabel(self, ctx:BatchParser.CallWithLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#callWithFilePath.
    def visitCallWithFilePath(self, ctx:BatchParser.CallWithFilePathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#batchParameters.
    def visitBatchParameters(self, ctx:BatchParser.BatchParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#batchParameter.
    def visitBatchParameter(self, ctx:BatchParser.BatchParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#conditionParameter.
    def visitConditionParameter(self, ctx:BatchParser.ConditionParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#delStatement.
    def visitDelStatement(self, ctx:BatchParser.DelStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#endlocalStatement.
    def visitEndlocalStatement(self, ctx:BatchParser.EndlocalStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#execStatement.
    def visitExecStatement(self, ctx:BatchParser.ExecStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#execFile.
    def visitExecFile(self, ctx:BatchParser.ExecFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#execParameter.
    def visitExecParameter(self, ctx:BatchParser.ExecParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#concatenateFileContent.
    def visitConcatenateFileContent(self, ctx:BatchParser.ConcatenateFileContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#exitStatement.
    def visitExitStatement(self, ctx:BatchParser.ExitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#exitCurrentBatch.
    def visitExitCurrentBatch(self, ctx:BatchParser.ExitCurrentBatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#exitCode.
    def visitExitCode(self, ctx:BatchParser.ExitCodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#forStatement.
    def visitForStatement(self, ctx:BatchParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#configurationString.
    def visitConfigurationString(self, ctx:BatchParser.ConfigurationStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#forValues.
    def visitForValues(self, ctx:BatchParser.ForValuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#forValue.
    def visitForValue(self, ctx:BatchParser.ForValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#forVariable.
    def visitForVariable(self, ctx:BatchParser.ForVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#forVariableModifier.
    def visitForVariableModifier(self, ctx:BatchParser.ForVariableModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#forDo.
    def visitForDo(self, ctx:BatchParser.ForDoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#gotoStatement.
    def visitGotoStatement(self, ctx:BatchParser.GotoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#ifStatement.
    def visitIfStatement(self, ctx:BatchParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#ifThen.
    def visitIfThen(self, ctx:BatchParser.IfThenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#ifElse.
    def visitIfElse(self, ctx:BatchParser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#simpleIf.
    def visitSimpleIf(self, ctx:BatchParser.SimpleIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#condition.
    def visitCondition(self, ctx:BatchParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#leftConditionOperator.
    def visitLeftConditionOperator(self, ctx:BatchParser.LeftConditionOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#rightConditionOperator.
    def visitRightConditionOperator(self, ctx:BatchParser.RightConditionOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#relationalOperator.
    def visitRelationalOperator(self, ctx:BatchParser.RelationalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#mkdirStatement.
    def visitMkdirStatement(self, ctx:BatchParser.MkdirStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#setLocalStatement.
    def visitSetLocalStatement(self, ctx:BatchParser.SetLocalStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#typeStatement.
    def visitTypeStatement(self, ctx:BatchParser.TypeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#rmdirStatement.
    def visitRmdirStatement(self, ctx:BatchParser.RmdirStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#xcopyStatement.
    def visitXcopyStatement(self, ctx:BatchParser.XcopyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#xCopySource.
    def visitXCopySource(self, ctx:BatchParser.XCopySourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#xCopyDestination.
    def visitXCopyDestination(self, ctx:BatchParser.XCopyDestinationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#switches.
    def visitSwitches(self, ctx:BatchParser.SwitchesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#switch.
    def visitSwitch(self, ctx:BatchParser.SwitchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#dateFormat.
    def visitDateFormat(self, ctx:BatchParser.DateFormatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#setLocalOption.
    def visitSetLocalOption(self, ctx:BatchParser.SetLocalOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#setStatement.
    def visitSetStatement(self, ctx:BatchParser.SetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#displayFormating.
    def visitDisplayFormating(self, ctx:BatchParser.DisplayFormatingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#assignmentPart.
    def visitAssignmentPart(self, ctx:BatchParser.AssignmentPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#pauseStatement.
    def visitPauseStatement(self, ctx:BatchParser.PauseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#variableName.
    def visitVariableName(self, ctx:BatchParser.VariableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#value.
    def visitValue(self, ctx:BatchParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#calcValue.
    def visitCalcValue(self, ctx:BatchParser.CalcValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#calcOperator.
    def visitCalcOperator(self, ctx:BatchParser.CalcOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#filePath.
    def visitFilePath(self, ctx:BatchParser.FilePathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#fileName.
    def visitFileName(self, ctx:BatchParser.FileNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#fileNameChar.
    def visitFileNameChar(self, ctx:BatchParser.FileNameCharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#identifierCombinedWithReferencedVariable.
    def visitIdentifierCombinedWithReferencedVariable(self, ctx:BatchParser.IdentifierCombinedWithReferencedVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#idetifierOrRerencedVariable.
    def visitIdetifierOrRerencedVariable(self, ctx:BatchParser.IdetifierOrRerencedVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#referencedVariable.
    def visitReferencedVariable(self, ctx:BatchParser.ReferencedVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#variableSubstring.
    def visitVariableSubstring(self, ctx:BatchParser.VariableSubstringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#leftSubstring.
    def visitLeftSubstring(self, ctx:BatchParser.LeftSubstringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#rightSubstring.
    def visitRightSubstring(self, ctx:BatchParser.RightSubstringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#replacedOrRemovedSubstring.
    def visitReplacedOrRemovedSubstring(self, ctx:BatchParser.ReplacedOrRemovedSubstringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#removeSubstring.
    def visitRemoveSubstring(self, ctx:BatchParser.RemoveSubstringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#removedSubstring.
    def visitRemovedSubstring(self, ctx:BatchParser.RemovedSubstringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#removeSpaces.
    def visitRemoveSpaces(self, ctx:BatchParser.RemoveSpacesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#replaceSubstring.
    def visitReplaceSubstring(self, ctx:BatchParser.ReplaceSubstringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#subtringRemoved.
    def visitSubtringRemoved(self, ctx:BatchParser.SubtringRemovedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#subStringReplaced.
    def visitSubStringReplaced(self, ctx:BatchParser.SubStringReplacedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#startSub.
    def visitStartSub(self, ctx:BatchParser.StartSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#lengthSub.
    def visitLengthSub(self, ctx:BatchParser.LengthSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#variableStart.
    def visitVariableStart(self, ctx:BatchParser.VariableStartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#variableLength.
    def visitVariableLength(self, ctx:BatchParser.VariableLengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BatchParser#concatenateString.
    def visitConcatenateString(self, ctx:BatchParser.ConcatenateStringContext):
        return self.visitChildren(ctx)



del BatchParser