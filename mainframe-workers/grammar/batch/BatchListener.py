# Generated from ./grammar/batch/Batch.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BatchParser import BatchParser
else:
    from BatchParser import BatchParser

# This class defines a complete listener for a parse tree produced by BatchParser.
class BatchListener(ParseTreeListener):

    # Enter a parse tree produced by BatchParser#startRule.
    def enterStartRule(self, ctx:BatchParser.StartRuleContext):
        pass

    # Exit a parse tree produced by BatchParser#startRule.
    def exitStartRule(self, ctx:BatchParser.StartRuleContext):
        pass


    # Enter a parse tree produced by BatchParser#label.
    def enterLabel(self, ctx:BatchParser.LabelContext):
        pass

    # Exit a parse tree produced by BatchParser#label.
    def exitLabel(self, ctx:BatchParser.LabelContext):
        pass


    # Enter a parse tree produced by BatchParser#labelName.
    def enterLabelName(self, ctx:BatchParser.LabelNameContext):
        pass

    # Exit a parse tree produced by BatchParser#labelName.
    def exitLabelName(self, ctx:BatchParser.LabelNameContext):
        pass


    # Enter a parse tree produced by BatchParser#statement.
    def enterStatement(self, ctx:BatchParser.StatementContext):
        pass

    # Exit a parse tree produced by BatchParser#statement.
    def exitStatement(self, ctx:BatchParser.StatementContext):
        pass


    # Enter a parse tree produced by BatchParser#z7Statement.
    def enterZ7Statement(self, ctx:BatchParser.Z7StatementContext):
        pass

    # Exit a parse tree produced by BatchParser#z7Statement.
    def exitZ7Statement(self, ctx:BatchParser.Z7StatementContext):
        pass


    # Enter a parse tree produced by BatchParser#z7Command.
    def enterZ7Command(self, ctx:BatchParser.Z7CommandContext):
        pass

    # Exit a parse tree produced by BatchParser#z7Command.
    def exitZ7Command(self, ctx:BatchParser.Z7CommandContext):
        pass


    # Enter a parse tree produced by BatchParser#z7Switches.
    def enterZ7Switches(self, ctx:BatchParser.Z7SwitchesContext):
        pass

    # Exit a parse tree produced by BatchParser#z7Switches.
    def exitZ7Switches(self, ctx:BatchParser.Z7SwitchesContext):
        pass


    # Enter a parse tree produced by BatchParser#z7Switch.
    def enterZ7Switch(self, ctx:BatchParser.Z7SwitchContext):
        pass

    # Exit a parse tree produced by BatchParser#z7Switch.
    def exitZ7Switch(self, ctx:BatchParser.Z7SwitchContext):
        pass


    # Enter a parse tree produced by BatchParser#echoStatement.
    def enterEchoStatement(self, ctx:BatchParser.EchoStatementContext):
        pass

    # Exit a parse tree produced by BatchParser#echoStatement.
    def exitEchoStatement(self, ctx:BatchParser.EchoStatementContext):
        pass


    # Enter a parse tree produced by BatchParser#remStatement.
    def enterRemStatement(self, ctx:BatchParser.RemStatementContext):
        pass

    # Exit a parse tree produced by BatchParser#remStatement.
    def exitRemStatement(self, ctx:BatchParser.RemStatementContext):
        pass


    # Enter a parse tree produced by BatchParser#bsortexStatement.
    def enterBsortexStatement(self, ctx:BatchParser.BsortexStatementContext):
        pass

    # Exit a parse tree produced by BatchParser#bsortexStatement.
    def exitBsortexStatement(self, ctx:BatchParser.BsortexStatementContext):
        pass


    # Enter a parse tree produced by BatchParser#sortParameters.
    def enterSortParameters(self, ctx:BatchParser.SortParametersContext):
        pass

    # Exit a parse tree produced by BatchParser#sortParameters.
    def exitSortParameters(self, ctx:BatchParser.SortParametersContext):
        pass


    # Enter a parse tree produced by BatchParser#sortParameter.
    def enterSortParameter(self, ctx:BatchParser.SortParameterContext):
        pass

    # Exit a parse tree produced by BatchParser#sortParameter.
    def exitSortParameter(self, ctx:BatchParser.SortParameterContext):
        pass


    # Enter a parse tree produced by BatchParser#sortValue.
    def enterSortValue(self, ctx:BatchParser.SortValueContext):
        pass

    # Exit a parse tree produced by BatchParser#sortValue.
    def exitSortValue(self, ctx:BatchParser.SortValueContext):
        pass


    # Enter a parse tree produced by BatchParser#inputParameters.
    def enterInputParameters(self, ctx:BatchParser.InputParametersContext):
        pass

    # Exit a parse tree produced by BatchParser#inputParameters.
    def exitInputParameters(self, ctx:BatchParser.InputParametersContext):
        pass


    # Enter a parse tree produced by BatchParser#inputParameter.
    def enterInputParameter(self, ctx:BatchParser.InputParameterContext):
        pass

    # Exit a parse tree produced by BatchParser#inputParameter.
    def exitInputParameter(self, ctx:BatchParser.InputParameterContext):
        pass


    # Enter a parse tree produced by BatchParser#recordParameters.
    def enterRecordParameters(self, ctx:BatchParser.RecordParametersContext):
        pass

    # Exit a parse tree produced by BatchParser#recordParameters.
    def exitRecordParameters(self, ctx:BatchParser.RecordParametersContext):
        pass


    # Enter a parse tree produced by BatchParser#recordParameter.
    def enterRecordParameter(self, ctx:BatchParser.RecordParameterContext):
        pass

    # Exit a parse tree produced by BatchParser#recordParameter.
    def exitRecordParameter(self, ctx:BatchParser.RecordParameterContext):
        pass


    # Enter a parse tree produced by BatchParser#optionParameters.
    def enterOptionParameters(self, ctx:BatchParser.OptionParametersContext):
        pass

    # Exit a parse tree produced by BatchParser#optionParameters.
    def exitOptionParameters(self, ctx:BatchParser.OptionParametersContext):
        pass


    # Enter a parse tree produced by BatchParser#optionParameter.
    def enterOptionParameter(self, ctx:BatchParser.OptionParameterContext):
        pass

    # Exit a parse tree produced by BatchParser#optionParameter.
    def exitOptionParameter(self, ctx:BatchParser.OptionParameterContext):
        pass


    # Enter a parse tree produced by BatchParser#outputParameters.
    def enterOutputParameters(self, ctx:BatchParser.OutputParametersContext):
        pass

    # Exit a parse tree produced by BatchParser#outputParameters.
    def exitOutputParameters(self, ctx:BatchParser.OutputParametersContext):
        pass


    # Enter a parse tree produced by BatchParser#outputParameter.
    def enterOutputParameter(self, ctx:BatchParser.OutputParameterContext):
        pass

    # Exit a parse tree produced by BatchParser#outputParameter.
    def exitOutputParameter(self, ctx:BatchParser.OutputParameterContext):
        pass


    # Enter a parse tree produced by BatchParser#outputValue.
    def enterOutputValue(self, ctx:BatchParser.OutputValueContext):
        pass

    # Exit a parse tree produced by BatchParser#outputValue.
    def exitOutputValue(self, ctx:BatchParser.OutputValueContext):
        pass


    # Enter a parse tree produced by BatchParser#callStatement.
    def enterCallStatement(self, ctx:BatchParser.CallStatementContext):
        pass

    # Exit a parse tree produced by BatchParser#callStatement.
    def exitCallStatement(self, ctx:BatchParser.CallStatementContext):
        pass


    # Enter a parse tree produced by BatchParser#callWithLabel.
    def enterCallWithLabel(self, ctx:BatchParser.CallWithLabelContext):
        pass

    # Exit a parse tree produced by BatchParser#callWithLabel.
    def exitCallWithLabel(self, ctx:BatchParser.CallWithLabelContext):
        pass


    # Enter a parse tree produced by BatchParser#callWithFilePath.
    def enterCallWithFilePath(self, ctx:BatchParser.CallWithFilePathContext):
        pass

    # Exit a parse tree produced by BatchParser#callWithFilePath.
    def exitCallWithFilePath(self, ctx:BatchParser.CallWithFilePathContext):
        pass


    # Enter a parse tree produced by BatchParser#batchParameters.
    def enterBatchParameters(self, ctx:BatchParser.BatchParametersContext):
        pass

    # Exit a parse tree produced by BatchParser#batchParameters.
    def exitBatchParameters(self, ctx:BatchParser.BatchParametersContext):
        pass


    # Enter a parse tree produced by BatchParser#batchParameter.
    def enterBatchParameter(self, ctx:BatchParser.BatchParameterContext):
        pass

    # Exit a parse tree produced by BatchParser#batchParameter.
    def exitBatchParameter(self, ctx:BatchParser.BatchParameterContext):
        pass


    # Enter a parse tree produced by BatchParser#conditionParameter.
    def enterConditionParameter(self, ctx:BatchParser.ConditionParameterContext):
        pass

    # Exit a parse tree produced by BatchParser#conditionParameter.
    def exitConditionParameter(self, ctx:BatchParser.ConditionParameterContext):
        pass


    # Enter a parse tree produced by BatchParser#delStatement.
    def enterDelStatement(self, ctx:BatchParser.DelStatementContext):
        pass

    # Exit a parse tree produced by BatchParser#delStatement.
    def exitDelStatement(self, ctx:BatchParser.DelStatementContext):
        pass


    # Enter a parse tree produced by BatchParser#endlocalStatement.
    def enterEndlocalStatement(self, ctx:BatchParser.EndlocalStatementContext):
        pass

    # Exit a parse tree produced by BatchParser#endlocalStatement.
    def exitEndlocalStatement(self, ctx:BatchParser.EndlocalStatementContext):
        pass


    # Enter a parse tree produced by BatchParser#execStatement.
    def enterExecStatement(self, ctx:BatchParser.ExecStatementContext):
        pass

    # Exit a parse tree produced by BatchParser#execStatement.
    def exitExecStatement(self, ctx:BatchParser.ExecStatementContext):
        pass


    # Enter a parse tree produced by BatchParser#execFile.
    def enterExecFile(self, ctx:BatchParser.ExecFileContext):
        pass

    # Exit a parse tree produced by BatchParser#execFile.
    def exitExecFile(self, ctx:BatchParser.ExecFileContext):
        pass


    # Enter a parse tree produced by BatchParser#execParameter.
    def enterExecParameter(self, ctx:BatchParser.ExecParameterContext):
        pass

    # Exit a parse tree produced by BatchParser#execParameter.
    def exitExecParameter(self, ctx:BatchParser.ExecParameterContext):
        pass


    # Enter a parse tree produced by BatchParser#concatenateFileContent.
    def enterConcatenateFileContent(self, ctx:BatchParser.ConcatenateFileContentContext):
        pass

    # Exit a parse tree produced by BatchParser#concatenateFileContent.
    def exitConcatenateFileContent(self, ctx:BatchParser.ConcatenateFileContentContext):
        pass


    # Enter a parse tree produced by BatchParser#exitStatement.
    def enterExitStatement(self, ctx:BatchParser.ExitStatementContext):
        pass

    # Exit a parse tree produced by BatchParser#exitStatement.
    def exitExitStatement(self, ctx:BatchParser.ExitStatementContext):
        pass


    # Enter a parse tree produced by BatchParser#exitCurrentBatch.
    def enterExitCurrentBatch(self, ctx:BatchParser.ExitCurrentBatchContext):
        pass

    # Exit a parse tree produced by BatchParser#exitCurrentBatch.
    def exitExitCurrentBatch(self, ctx:BatchParser.ExitCurrentBatchContext):
        pass


    # Enter a parse tree produced by BatchParser#exitCode.
    def enterExitCode(self, ctx:BatchParser.ExitCodeContext):
        pass

    # Exit a parse tree produced by BatchParser#exitCode.
    def exitExitCode(self, ctx:BatchParser.ExitCodeContext):
        pass


    # Enter a parse tree produced by BatchParser#forStatement.
    def enterForStatement(self, ctx:BatchParser.ForStatementContext):
        pass

    # Exit a parse tree produced by BatchParser#forStatement.
    def exitForStatement(self, ctx:BatchParser.ForStatementContext):
        pass


    # Enter a parse tree produced by BatchParser#configurationString.
    def enterConfigurationString(self, ctx:BatchParser.ConfigurationStringContext):
        pass

    # Exit a parse tree produced by BatchParser#configurationString.
    def exitConfigurationString(self, ctx:BatchParser.ConfigurationStringContext):
        pass


    # Enter a parse tree produced by BatchParser#forValues.
    def enterForValues(self, ctx:BatchParser.ForValuesContext):
        pass

    # Exit a parse tree produced by BatchParser#forValues.
    def exitForValues(self, ctx:BatchParser.ForValuesContext):
        pass


    # Enter a parse tree produced by BatchParser#forValue.
    def enterForValue(self, ctx:BatchParser.ForValueContext):
        pass

    # Exit a parse tree produced by BatchParser#forValue.
    def exitForValue(self, ctx:BatchParser.ForValueContext):
        pass


    # Enter a parse tree produced by BatchParser#forVariable.
    def enterForVariable(self, ctx:BatchParser.ForVariableContext):
        pass

    # Exit a parse tree produced by BatchParser#forVariable.
    def exitForVariable(self, ctx:BatchParser.ForVariableContext):
        pass


    # Enter a parse tree produced by BatchParser#forVariableModifier.
    def enterForVariableModifier(self, ctx:BatchParser.ForVariableModifierContext):
        pass

    # Exit a parse tree produced by BatchParser#forVariableModifier.
    def exitForVariableModifier(self, ctx:BatchParser.ForVariableModifierContext):
        pass


    # Enter a parse tree produced by BatchParser#forDo.
    def enterForDo(self, ctx:BatchParser.ForDoContext):
        pass

    # Exit a parse tree produced by BatchParser#forDo.
    def exitForDo(self, ctx:BatchParser.ForDoContext):
        pass


    # Enter a parse tree produced by BatchParser#gotoStatement.
    def enterGotoStatement(self, ctx:BatchParser.GotoStatementContext):
        pass

    # Exit a parse tree produced by BatchParser#gotoStatement.
    def exitGotoStatement(self, ctx:BatchParser.GotoStatementContext):
        pass


    # Enter a parse tree produced by BatchParser#ifStatement.
    def enterIfStatement(self, ctx:BatchParser.IfStatementContext):
        pass

    # Exit a parse tree produced by BatchParser#ifStatement.
    def exitIfStatement(self, ctx:BatchParser.IfStatementContext):
        pass


    # Enter a parse tree produced by BatchParser#ifThen.
    def enterIfThen(self, ctx:BatchParser.IfThenContext):
        pass

    # Exit a parse tree produced by BatchParser#ifThen.
    def exitIfThen(self, ctx:BatchParser.IfThenContext):
        pass


    # Enter a parse tree produced by BatchParser#ifElse.
    def enterIfElse(self, ctx:BatchParser.IfElseContext):
        pass

    # Exit a parse tree produced by BatchParser#ifElse.
    def exitIfElse(self, ctx:BatchParser.IfElseContext):
        pass


    # Enter a parse tree produced by BatchParser#simpleIf.
    def enterSimpleIf(self, ctx:BatchParser.SimpleIfContext):
        pass

    # Exit a parse tree produced by BatchParser#simpleIf.
    def exitSimpleIf(self, ctx:BatchParser.SimpleIfContext):
        pass


    # Enter a parse tree produced by BatchParser#condition.
    def enterCondition(self, ctx:BatchParser.ConditionContext):
        pass

    # Exit a parse tree produced by BatchParser#condition.
    def exitCondition(self, ctx:BatchParser.ConditionContext):
        pass


    # Enter a parse tree produced by BatchParser#leftConditionOperator.
    def enterLeftConditionOperator(self, ctx:BatchParser.LeftConditionOperatorContext):
        pass

    # Exit a parse tree produced by BatchParser#leftConditionOperator.
    def exitLeftConditionOperator(self, ctx:BatchParser.LeftConditionOperatorContext):
        pass


    # Enter a parse tree produced by BatchParser#rightConditionOperator.
    def enterRightConditionOperator(self, ctx:BatchParser.RightConditionOperatorContext):
        pass

    # Exit a parse tree produced by BatchParser#rightConditionOperator.
    def exitRightConditionOperator(self, ctx:BatchParser.RightConditionOperatorContext):
        pass


    # Enter a parse tree produced by BatchParser#relationalOperator.
    def enterRelationalOperator(self, ctx:BatchParser.RelationalOperatorContext):
        pass

    # Exit a parse tree produced by BatchParser#relationalOperator.
    def exitRelationalOperator(self, ctx:BatchParser.RelationalOperatorContext):
        pass


    # Enter a parse tree produced by BatchParser#mkdirStatement.
    def enterMkdirStatement(self, ctx:BatchParser.MkdirStatementContext):
        pass

    # Exit a parse tree produced by BatchParser#mkdirStatement.
    def exitMkdirStatement(self, ctx:BatchParser.MkdirStatementContext):
        pass


    # Enter a parse tree produced by BatchParser#setLocalStatement.
    def enterSetLocalStatement(self, ctx:BatchParser.SetLocalStatementContext):
        pass

    # Exit a parse tree produced by BatchParser#setLocalStatement.
    def exitSetLocalStatement(self, ctx:BatchParser.SetLocalStatementContext):
        pass


    # Enter a parse tree produced by BatchParser#typeStatement.
    def enterTypeStatement(self, ctx:BatchParser.TypeStatementContext):
        pass

    # Exit a parse tree produced by BatchParser#typeStatement.
    def exitTypeStatement(self, ctx:BatchParser.TypeStatementContext):
        pass


    # Enter a parse tree produced by BatchParser#rmdirStatement.
    def enterRmdirStatement(self, ctx:BatchParser.RmdirStatementContext):
        pass

    # Exit a parse tree produced by BatchParser#rmdirStatement.
    def exitRmdirStatement(self, ctx:BatchParser.RmdirStatementContext):
        pass


    # Enter a parse tree produced by BatchParser#xcopyStatement.
    def enterXcopyStatement(self, ctx:BatchParser.XcopyStatementContext):
        pass

    # Exit a parse tree produced by BatchParser#xcopyStatement.
    def exitXcopyStatement(self, ctx:BatchParser.XcopyStatementContext):
        pass


    # Enter a parse tree produced by BatchParser#xCopySource.
    def enterXCopySource(self, ctx:BatchParser.XCopySourceContext):
        pass

    # Exit a parse tree produced by BatchParser#xCopySource.
    def exitXCopySource(self, ctx:BatchParser.XCopySourceContext):
        pass


    # Enter a parse tree produced by BatchParser#xCopyDestination.
    def enterXCopyDestination(self, ctx:BatchParser.XCopyDestinationContext):
        pass

    # Exit a parse tree produced by BatchParser#xCopyDestination.
    def exitXCopyDestination(self, ctx:BatchParser.XCopyDestinationContext):
        pass


    # Enter a parse tree produced by BatchParser#switches.
    def enterSwitches(self, ctx:BatchParser.SwitchesContext):
        pass

    # Exit a parse tree produced by BatchParser#switches.
    def exitSwitches(self, ctx:BatchParser.SwitchesContext):
        pass


    # Enter a parse tree produced by BatchParser#switch.
    def enterSwitch(self, ctx:BatchParser.SwitchContext):
        pass

    # Exit a parse tree produced by BatchParser#switch.
    def exitSwitch(self, ctx:BatchParser.SwitchContext):
        pass


    # Enter a parse tree produced by BatchParser#dateFormat.
    def enterDateFormat(self, ctx:BatchParser.DateFormatContext):
        pass

    # Exit a parse tree produced by BatchParser#dateFormat.
    def exitDateFormat(self, ctx:BatchParser.DateFormatContext):
        pass


    # Enter a parse tree produced by BatchParser#setLocalOption.
    def enterSetLocalOption(self, ctx:BatchParser.SetLocalOptionContext):
        pass

    # Exit a parse tree produced by BatchParser#setLocalOption.
    def exitSetLocalOption(self, ctx:BatchParser.SetLocalOptionContext):
        pass


    # Enter a parse tree produced by BatchParser#setStatement.
    def enterSetStatement(self, ctx:BatchParser.SetStatementContext):
        pass

    # Exit a parse tree produced by BatchParser#setStatement.
    def exitSetStatement(self, ctx:BatchParser.SetStatementContext):
        pass


    # Enter a parse tree produced by BatchParser#displayFormating.
    def enterDisplayFormating(self, ctx:BatchParser.DisplayFormatingContext):
        pass

    # Exit a parse tree produced by BatchParser#displayFormating.
    def exitDisplayFormating(self, ctx:BatchParser.DisplayFormatingContext):
        pass


    # Enter a parse tree produced by BatchParser#assignmentPart.
    def enterAssignmentPart(self, ctx:BatchParser.AssignmentPartContext):
        pass

    # Exit a parse tree produced by BatchParser#assignmentPart.
    def exitAssignmentPart(self, ctx:BatchParser.AssignmentPartContext):
        pass


    # Enter a parse tree produced by BatchParser#pauseStatement.
    def enterPauseStatement(self, ctx:BatchParser.PauseStatementContext):
        pass

    # Exit a parse tree produced by BatchParser#pauseStatement.
    def exitPauseStatement(self, ctx:BatchParser.PauseStatementContext):
        pass


    # Enter a parse tree produced by BatchParser#variableName.
    def enterVariableName(self, ctx:BatchParser.VariableNameContext):
        pass

    # Exit a parse tree produced by BatchParser#variableName.
    def exitVariableName(self, ctx:BatchParser.VariableNameContext):
        pass


    # Enter a parse tree produced by BatchParser#value.
    def enterValue(self, ctx:BatchParser.ValueContext):
        pass

    # Exit a parse tree produced by BatchParser#value.
    def exitValue(self, ctx:BatchParser.ValueContext):
        pass


    # Enter a parse tree produced by BatchParser#calcValue.
    def enterCalcValue(self, ctx:BatchParser.CalcValueContext):
        pass

    # Exit a parse tree produced by BatchParser#calcValue.
    def exitCalcValue(self, ctx:BatchParser.CalcValueContext):
        pass


    # Enter a parse tree produced by BatchParser#calcOperator.
    def enterCalcOperator(self, ctx:BatchParser.CalcOperatorContext):
        pass

    # Exit a parse tree produced by BatchParser#calcOperator.
    def exitCalcOperator(self, ctx:BatchParser.CalcOperatorContext):
        pass


    # Enter a parse tree produced by BatchParser#filePath.
    def enterFilePath(self, ctx:BatchParser.FilePathContext):
        pass

    # Exit a parse tree produced by BatchParser#filePath.
    def exitFilePath(self, ctx:BatchParser.FilePathContext):
        pass


    # Enter a parse tree produced by BatchParser#fileName.
    def enterFileName(self, ctx:BatchParser.FileNameContext):
        pass

    # Exit a parse tree produced by BatchParser#fileName.
    def exitFileName(self, ctx:BatchParser.FileNameContext):
        pass


    # Enter a parse tree produced by BatchParser#fileNameChar.
    def enterFileNameChar(self, ctx:BatchParser.FileNameCharContext):
        pass

    # Exit a parse tree produced by BatchParser#fileNameChar.
    def exitFileNameChar(self, ctx:BatchParser.FileNameCharContext):
        pass


    # Enter a parse tree produced by BatchParser#identifierCombinedWithReferencedVariable.
    def enterIdentifierCombinedWithReferencedVariable(self, ctx:BatchParser.IdentifierCombinedWithReferencedVariableContext):
        pass

    # Exit a parse tree produced by BatchParser#identifierCombinedWithReferencedVariable.
    def exitIdentifierCombinedWithReferencedVariable(self, ctx:BatchParser.IdentifierCombinedWithReferencedVariableContext):
        pass


    # Enter a parse tree produced by BatchParser#idetifierOrRerencedVariable.
    def enterIdetifierOrRerencedVariable(self, ctx:BatchParser.IdetifierOrRerencedVariableContext):
        pass

    # Exit a parse tree produced by BatchParser#idetifierOrRerencedVariable.
    def exitIdetifierOrRerencedVariable(self, ctx:BatchParser.IdetifierOrRerencedVariableContext):
        pass


    # Enter a parse tree produced by BatchParser#referencedVariable.
    def enterReferencedVariable(self, ctx:BatchParser.ReferencedVariableContext):
        pass

    # Exit a parse tree produced by BatchParser#referencedVariable.
    def exitReferencedVariable(self, ctx:BatchParser.ReferencedVariableContext):
        pass


    # Enter a parse tree produced by BatchParser#variableSubstring.
    def enterVariableSubstring(self, ctx:BatchParser.VariableSubstringContext):
        pass

    # Exit a parse tree produced by BatchParser#variableSubstring.
    def exitVariableSubstring(self, ctx:BatchParser.VariableSubstringContext):
        pass


    # Enter a parse tree produced by BatchParser#leftSubstring.
    def enterLeftSubstring(self, ctx:BatchParser.LeftSubstringContext):
        pass

    # Exit a parse tree produced by BatchParser#leftSubstring.
    def exitLeftSubstring(self, ctx:BatchParser.LeftSubstringContext):
        pass


    # Enter a parse tree produced by BatchParser#rightSubstring.
    def enterRightSubstring(self, ctx:BatchParser.RightSubstringContext):
        pass

    # Exit a parse tree produced by BatchParser#rightSubstring.
    def exitRightSubstring(self, ctx:BatchParser.RightSubstringContext):
        pass


    # Enter a parse tree produced by BatchParser#replacedOrRemovedSubstring.
    def enterReplacedOrRemovedSubstring(self, ctx:BatchParser.ReplacedOrRemovedSubstringContext):
        pass

    # Exit a parse tree produced by BatchParser#replacedOrRemovedSubstring.
    def exitReplacedOrRemovedSubstring(self, ctx:BatchParser.ReplacedOrRemovedSubstringContext):
        pass


    # Enter a parse tree produced by BatchParser#removeSubstring.
    def enterRemoveSubstring(self, ctx:BatchParser.RemoveSubstringContext):
        pass

    # Exit a parse tree produced by BatchParser#removeSubstring.
    def exitRemoveSubstring(self, ctx:BatchParser.RemoveSubstringContext):
        pass


    # Enter a parse tree produced by BatchParser#removedSubstring.
    def enterRemovedSubstring(self, ctx:BatchParser.RemovedSubstringContext):
        pass

    # Exit a parse tree produced by BatchParser#removedSubstring.
    def exitRemovedSubstring(self, ctx:BatchParser.RemovedSubstringContext):
        pass


    # Enter a parse tree produced by BatchParser#removeSpaces.
    def enterRemoveSpaces(self, ctx:BatchParser.RemoveSpacesContext):
        pass

    # Exit a parse tree produced by BatchParser#removeSpaces.
    def exitRemoveSpaces(self, ctx:BatchParser.RemoveSpacesContext):
        pass


    # Enter a parse tree produced by BatchParser#replaceSubstring.
    def enterReplaceSubstring(self, ctx:BatchParser.ReplaceSubstringContext):
        pass

    # Exit a parse tree produced by BatchParser#replaceSubstring.
    def exitReplaceSubstring(self, ctx:BatchParser.ReplaceSubstringContext):
        pass


    # Enter a parse tree produced by BatchParser#subtringRemoved.
    def enterSubtringRemoved(self, ctx:BatchParser.SubtringRemovedContext):
        pass

    # Exit a parse tree produced by BatchParser#subtringRemoved.
    def exitSubtringRemoved(self, ctx:BatchParser.SubtringRemovedContext):
        pass


    # Enter a parse tree produced by BatchParser#subStringReplaced.
    def enterSubStringReplaced(self, ctx:BatchParser.SubStringReplacedContext):
        pass

    # Exit a parse tree produced by BatchParser#subStringReplaced.
    def exitSubStringReplaced(self, ctx:BatchParser.SubStringReplacedContext):
        pass


    # Enter a parse tree produced by BatchParser#startSub.
    def enterStartSub(self, ctx:BatchParser.StartSubContext):
        pass

    # Exit a parse tree produced by BatchParser#startSub.
    def exitStartSub(self, ctx:BatchParser.StartSubContext):
        pass


    # Enter a parse tree produced by BatchParser#lengthSub.
    def enterLengthSub(self, ctx:BatchParser.LengthSubContext):
        pass

    # Exit a parse tree produced by BatchParser#lengthSub.
    def exitLengthSub(self, ctx:BatchParser.LengthSubContext):
        pass


    # Enter a parse tree produced by BatchParser#variableStart.
    def enterVariableStart(self, ctx:BatchParser.VariableStartContext):
        pass

    # Exit a parse tree produced by BatchParser#variableStart.
    def exitVariableStart(self, ctx:BatchParser.VariableStartContext):
        pass


    # Enter a parse tree produced by BatchParser#variableLength.
    def enterVariableLength(self, ctx:BatchParser.VariableLengthContext):
        pass

    # Exit a parse tree produced by BatchParser#variableLength.
    def exitVariableLength(self, ctx:BatchParser.VariableLengthContext):
        pass


    # Enter a parse tree produced by BatchParser#concatenateString.
    def enterConcatenateString(self, ctx:BatchParser.ConcatenateStringContext):
        pass

    # Exit a parse tree produced by BatchParser#concatenateString.
    def exitConcatenateString(self, ctx:BatchParser.ConcatenateStringContext):
        pass



del BatchParser