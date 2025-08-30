# Generated from ./grammar/ldlp/LDLP.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LDLPParser import LDLPParser
else:
    from LDLPParser import LDLPParser

# This class defines a complete generic visitor for a parse tree produced by LDLPParser.

class LDLPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LDLPParser#startRule.
    def visitStartRule(self, ctx:LDLPParser.StartRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#runtime.
    def visitRuntime(self, ctx:LDLPParser.RuntimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#statements.
    def visitStatements(self, ctx:LDLPParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#statement.
    def visitStatement(self, ctx:LDLPParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#functionCallingStatement.
    def visitFunctionCallingStatement(self, ctx:LDLPParser.FunctionCallingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#function_name.
    def visitFunction_name(self, ctx:LDLPParser.Function_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#abortStatement.
    def visitAbortStatement(self, ctx:LDLPParser.AbortStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#acceptStatement.
    def visitAcceptStatement(self, ctx:LDLPParser.AcceptStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#accessExtStatement.
    def visitAccessExtStatement(self, ctx:LDLPParser.AccessExtStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#locator.
    def visitLocator(self, ctx:LDLPParser.LocatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#find.
    def visitFind(self, ctx:LDLPParser.FindContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#get.
    def visitGet(self, ctx:LDLPParser.GetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#database.
    def visitDatabase(self, ctx:LDLPParser.DatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#item.
    def visitItem(self, ctx:LDLPParser.ItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#addStatement.
    def visitAddStatement(self, ctx:LDLPParser.AddStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#advanceStatement.
    def visitAdvanceStatement(self, ctx:LDLPParser.AdvanceStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#outputStream.
    def visitOutputStream(self, ctx:LDLPParser.OutputStreamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#assignment.
    def visitAssignment(self, ctx:LDLPParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#attachStatement.
    def visitAttachStatement(self, ctx:LDLPParser.AttachStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#attachAndSpaceStatement.
    def visitAttachAndSpaceStatement(self, ctx:LDLPParser.AttachAndSpaceStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#attributeStatement.
    def visitAttributeStatement(self, ctx:LDLPParser.AttributeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#beginpageStatement.
    def visitBeginpageStatement(self, ctx:LDLPParser.BeginpageStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#breakStatement.
    def visitBreakStatement(self, ctx:LDLPParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#case.
    def visitCase(self, ctx:LDLPParser.CaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#otherwise.
    def visitOtherwise(self, ctx:LDLPParser.OtherwiseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#caseStatement.
    def visitCaseStatement(self, ctx:LDLPParser.CaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#beginCase.
    def visitBeginCase(self, ctx:LDLPParser.BeginCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#endcase.
    def visitEndcase(self, ctx:LDLPParser.EndcaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#computeStatement.
    def visitComputeStatement(self, ctx:LDLPParser.ComputeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#continueStatement.
    def visitContinueStatement(self, ctx:LDLPParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#criticalpointStatement.
    def visitCriticalpointStatement(self, ctx:LDLPParser.CriticalpointStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#cursorStatement.
    def visitCursorStatement(self, ctx:LDLPParser.CursorStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#dateConvertStatement.
    def visitDateConvertStatement(self, ctx:LDLPParser.DateConvertStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#dateVariable.
    def visitDateVariable(self, ctx:LDLPParser.DateVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#detachStatement.
    def visitDetachStatement(self, ctx:LDLPParser.DetachStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#determineStatement.
    def visitDetermineStatement(self, ctx:LDLPParser.DetermineStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#determineActualStatement.
    def visitDetermineActualStatement(self, ctx:LDLPParser.DetermineActualStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#variant.
    def visitVariant(self, ctx:LDLPParser.VariantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#databaseVariant.
    def visitDatabaseVariant(self, ctx:LDLPParser.DatabaseVariantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#extractFileVariant.
    def visitExtractFileVariant(self, ctx:LDLPParser.ExtractFileVariantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#determineBackStatement.
    def visitDetermineBackStatement(self, ctx:LDLPParser.DetermineBackStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#determineEveryStatement.
    def visitDetermineEveryStatement(self, ctx:LDLPParser.DetermineEveryStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#determineFromStatement.
    def visitDetermineFromStatement(self, ctx:LDLPParser.DetermineFromStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#determineGroupStatement.
    def visitDetermineGroupStatement(self, ctx:LDLPParser.DetermineGroupStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#determineLastStatement.
    def visitDetermineLastStatement(self, ctx:LDLPParser.DetermineLastStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#determineTotalStatement.
    def visitDetermineTotalStatement(self, ctx:LDLPParser.DetermineTotalStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#attributeName.
    def visitAttributeName(self, ctx:LDLPParser.AttributeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#keyArguments.
    def visitKeyArguments(self, ctx:LDLPParser.KeyArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#records.
    def visitRecords(self, ctx:LDLPParser.RecordsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#extractFile.
    def visitExtractFile(self, ctx:LDLPParser.ExtractFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#iterator.
    def visitIterator(self, ctx:LDLPParser.IteratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#argument.
    def visitArgument(self, ctx:LDLPParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#determineEnd.
    def visitDetermineEnd(self, ctx:LDLPParser.DetermineEndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#divideStatement.
    def visitDivideStatement(self, ctx:LDLPParser.DivideStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#dowhenBlock.
    def visitDowhenBlock(self, ctx:LDLPParser.DowhenBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#elseBlock.
    def visitElseBlock(self, ctx:LDLPParser.ElseBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#dowhenStatement.
    def visitDowhenStatement(self, ctx:LDLPParser.DowhenStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#condition.
    def visitCondition(self, ctx:LDLPParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#classAttribute.
    def visitClassAttribute(self, ctx:LDLPParser.ClassAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#endDowhen.
    def visitEndDowhen(self, ctx:LDLPParser.EndDowhenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#enduseStatement.
    def visitEnduseStatement(self, ctx:LDLPParser.EnduseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#excludeStatement.
    def visitExcludeStatement(self, ctx:LDLPParser.ExcludeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#ifStatement.
    def visitIfStatement(self, ctx:LDLPParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#endIf.
    def visitEndIf(self, ctx:LDLPParser.EndIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#methodCall.
    def visitMethodCall(self, ctx:LDLPParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#expression.
    def visitExpression(self, ctx:LDLPParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#stringExpression.
    def visitStringExpression(self, ctx:LDLPParser.StringExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#paramList.
    def visitParamList(self, ctx:LDLPParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#param.
    def visitParam(self, ctx:LDLPParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#extractStatement.
    def visitExtractStatement(self, ctx:LDLPParser.ExtractStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#header.
    def visitHeader(self, ctx:LDLPParser.HeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#foreachStatement.
    def visitForeachStatement(self, ctx:LDLPParser.ForeachStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#flagStatement.
    def visitFlagStatement(self, ctx:LDLPParser.FlagStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#initializeStatement.
    def visitInitializeStatement(self, ctx:LDLPParser.InitializeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#initializationValue.
    def visitInitializationValue(self, ctx:LDLPParser.InitializationValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#insertStatement.
    def visitInsertStatement(self, ctx:LDLPParser.InsertStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#insertable.
    def visitInsertable(self, ctx:LDLPParser.InsertableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#mapping.
    def visitMapping(self, ctx:LDLPParser.MappingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#tableName.
    def visitTableName(self, ctx:LDLPParser.TableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#jumptoStatement.
    def visitJumptoStatement(self, ctx:LDLPParser.JumptoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#labelStatement.
    def visitLabelStatement(self, ctx:LDLPParser.LabelStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#label.
    def visitLabel(self, ctx:LDLPParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#loadStatement.
    def visitLoadStatement(self, ctx:LDLPParser.LoadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#ispecAttribute.
    def visitIspecAttribute(self, ctx:LDLPParser.IspecAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#logStatement.
    def visitLogStatement(self, ctx:LDLPParser.LogStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#lookupStatement.
    def visitLookupStatement(self, ctx:LDLPParser.LookupStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#lookupBaseStatement.
    def visitLookupBaseStatement(self, ctx:LDLPParser.LookupBaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#lookupFromStatement.
    def visitLookupFromStatement(self, ctx:LDLPParser.LookupFromStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#lookupEveryStatement.
    def visitLookupEveryStatement(self, ctx:LDLPParser.LookupEveryStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#lookupGroupStatement.
    def visitLookupGroupStatement(self, ctx:LDLPParser.LookupGroupStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#loopStatement.
    def visitLoopStatement(self, ctx:LDLPParser.LoopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#loopBlock.
    def visitLoopBlock(self, ctx:LDLPParser.LoopBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#compareType.
    def visitCompareType(self, ctx:LDLPParser.CompareTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#matchStatement.
    def visitMatchStatement(self, ctx:LDLPParser.MatchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#messageStatement.
    def visitMessageStatement(self, ctx:LDLPParser.MessageStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#moveStatement.
    def visitMoveStatement(self, ctx:LDLPParser.MoveStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#length.
    def visitLength(self, ctx:LDLPParser.LengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#source_variable.
    def visitSource_variable(self, ctx:LDLPParser.Source_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#target_variable.
    def visitTarget_variable(self, ctx:LDLPParser.Target_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#movedateStatement.
    def visitMovedateStatement(self, ctx:LDLPParser.MovedateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#movetimeStatement.
    def visitMovetimeStatement(self, ctx:LDLPParser.MovetimeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#multiplyStatement.
    def visitMultiplyStatement(self, ctx:LDLPParser.MultiplyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#onchangeStatement.
    def visitOnchangeStatement(self, ctx:LDLPParser.OnchangeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#routineCall.
    def visitRoutineCall(self, ctx:LDLPParser.RoutineCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#pageStatement.
    def visitPageStatement(self, ctx:LDLPParser.PageStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#recallStatement.
    def visitRecallStatement(self, ctx:LDLPParser.RecallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#releaseStatement.
    def visitReleaseStatement(self, ctx:LDLPParser.ReleaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#restartStatement.
    def visitRestartStatement(self, ctx:LDLPParser.RestartStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#rocStatement.
    def visitRocStatement(self, ctx:LDLPParser.RocStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#returnStatement.
    def visitReturnStatement(self, ctx:LDLPParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#instance.
    def visitInstance(self, ctx:LDLPParser.InstanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#interface.
    def visitInterface(self, ctx:LDLPParser.InterfaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#runStatement.
    def visitRunStatement(self, ctx:LDLPParser.RunStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#device.
    def visitDevice(self, ctx:LDLPParser.DeviceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#sleepStatement.
    def visitSleepStatement(self, ctx:LDLPParser.SleepStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#startStatement.
    def visitStartStatement(self, ctx:LDLPParser.StartStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#sendListDynamicStatement.
    def visitSendListDynamicStatement(self, ctx:LDLPParser.SendListDynamicStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#sendListStaticStatement.
    def visitSendListStaticStatement(self, ctx:LDLPParser.SendListStaticStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#downloadFile.
    def visitDownloadFile(self, ctx:LDLPParser.DownloadFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#sendMessageStatement.
    def visitSendMessageStatement(self, ctx:LDLPParser.SendMessageStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#sendPrintStatement.
    def visitSendPrintStatement(self, ctx:LDLPParser.SendPrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#setDBStatement.
    def visitSetDBStatement(self, ctx:LDLPParser.SetDBStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#setTitleStatement.
    def visitSetTitleStatement(self, ctx:LDLPParser.SetTitleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#stninfoStatement.
    def visitStninfoStatement(self, ctx:LDLPParser.StninfoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#subtractStatement.
    def visitSubtractStatement(self, ctx:LDLPParser.SubtractStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#switchtoStatement.
    def visitSwitchtoStatement(self, ctx:LDLPParser.SwitchtoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#wakeStatement.
    def visitWakeStatement(self, ctx:LDLPParser.WakeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#relational_operator.
    def visitRelational_operator(self, ctx:LDLPParser.Relational_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#logical_operator.
    def visitLogical_operator(self, ctx:LDLPParser.Logical_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#status.
    def visitStatus(self, ctx:LDLPParser.StatusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#dbName.
    def visitDbName(self, ctx:LDLPParser.DbNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#fileName.
    def visitFileName(self, ctx:LDLPParser.FileNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#dateFormat.
    def visitDateFormat(self, ctx:LDLPParser.DateFormatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#className.
    def visitClassName(self, ctx:LDLPParser.ClassNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#varName.
    def visitVarName(self, ctx:LDLPParser.VarNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#objectName.
    def visitObjectName(self, ctx:LDLPParser.ObjectNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#userCode.
    def visitUserCode(self, ctx:LDLPParser.UserCodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#frameName.
    def visitFrameName(self, ctx:LDLPParser.FrameNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#lineNumber.
    def visitLineNumber(self, ctx:LDLPParser.LineNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#pageNumber.
    def visitPageNumber(self, ctx:LDLPParser.PageNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#reportName.
    def visitReportName(self, ctx:LDLPParser.ReportNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#profileName.
    def visitProfileName(self, ctx:LDLPParser.ProfileNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#deviceName.
    def visitDeviceName(self, ctx:LDLPParser.DeviceNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#keywords.
    def visitKeywords(self, ctx:LDLPParser.KeywordsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#specialName.
    def visitSpecialName(self, ctx:LDLPParser.SpecialNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#variable.
    def visitVariable(self, ctx:LDLPParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#identifier.
    def visitIdentifier(self, ctx:LDLPParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LDLPParser#literal.
    def visitLiteral(self, ctx:LDLPParser.LiteralContext):
        return self.visitChildren(ctx)



del LDLPParser