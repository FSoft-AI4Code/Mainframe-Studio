# Generated from ./grammar/ldlp/LDLP.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LDLPParser import LDLPParser
else:
    from LDLPParser import LDLPParser

# This class defines a complete listener for a parse tree produced by LDLPParser.
class LDLPListener(ParseTreeListener):

    # Enter a parse tree produced by LDLPParser#startRule.
    def enterStartRule(self, ctx:LDLPParser.StartRuleContext):
        pass

    # Exit a parse tree produced by LDLPParser#startRule.
    def exitStartRule(self, ctx:LDLPParser.StartRuleContext):
        pass


    # Enter a parse tree produced by LDLPParser#runtime.
    def enterRuntime(self, ctx:LDLPParser.RuntimeContext):
        pass

    # Exit a parse tree produced by LDLPParser#runtime.
    def exitRuntime(self, ctx:LDLPParser.RuntimeContext):
        pass


    # Enter a parse tree produced by LDLPParser#statements.
    def enterStatements(self, ctx:LDLPParser.StatementsContext):
        pass

    # Exit a parse tree produced by LDLPParser#statements.
    def exitStatements(self, ctx:LDLPParser.StatementsContext):
        pass


    # Enter a parse tree produced by LDLPParser#statement.
    def enterStatement(self, ctx:LDLPParser.StatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#statement.
    def exitStatement(self, ctx:LDLPParser.StatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#functionCallingStatement.
    def enterFunctionCallingStatement(self, ctx:LDLPParser.FunctionCallingStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#functionCallingStatement.
    def exitFunctionCallingStatement(self, ctx:LDLPParser.FunctionCallingStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#function_name.
    def enterFunction_name(self, ctx:LDLPParser.Function_nameContext):
        pass

    # Exit a parse tree produced by LDLPParser#function_name.
    def exitFunction_name(self, ctx:LDLPParser.Function_nameContext):
        pass


    # Enter a parse tree produced by LDLPParser#abortStatement.
    def enterAbortStatement(self, ctx:LDLPParser.AbortStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#abortStatement.
    def exitAbortStatement(self, ctx:LDLPParser.AbortStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#acceptStatement.
    def enterAcceptStatement(self, ctx:LDLPParser.AcceptStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#acceptStatement.
    def exitAcceptStatement(self, ctx:LDLPParser.AcceptStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#accessExtStatement.
    def enterAccessExtStatement(self, ctx:LDLPParser.AccessExtStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#accessExtStatement.
    def exitAccessExtStatement(self, ctx:LDLPParser.AccessExtStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#locator.
    def enterLocator(self, ctx:LDLPParser.LocatorContext):
        pass

    # Exit a parse tree produced by LDLPParser#locator.
    def exitLocator(self, ctx:LDLPParser.LocatorContext):
        pass


    # Enter a parse tree produced by LDLPParser#find.
    def enterFind(self, ctx:LDLPParser.FindContext):
        pass

    # Exit a parse tree produced by LDLPParser#find.
    def exitFind(self, ctx:LDLPParser.FindContext):
        pass


    # Enter a parse tree produced by LDLPParser#get.
    def enterGet(self, ctx:LDLPParser.GetContext):
        pass

    # Exit a parse tree produced by LDLPParser#get.
    def exitGet(self, ctx:LDLPParser.GetContext):
        pass


    # Enter a parse tree produced by LDLPParser#database.
    def enterDatabase(self, ctx:LDLPParser.DatabaseContext):
        pass

    # Exit a parse tree produced by LDLPParser#database.
    def exitDatabase(self, ctx:LDLPParser.DatabaseContext):
        pass


    # Enter a parse tree produced by LDLPParser#item.
    def enterItem(self, ctx:LDLPParser.ItemContext):
        pass

    # Exit a parse tree produced by LDLPParser#item.
    def exitItem(self, ctx:LDLPParser.ItemContext):
        pass


    # Enter a parse tree produced by LDLPParser#addStatement.
    def enterAddStatement(self, ctx:LDLPParser.AddStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#addStatement.
    def exitAddStatement(self, ctx:LDLPParser.AddStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#advanceStatement.
    def enterAdvanceStatement(self, ctx:LDLPParser.AdvanceStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#advanceStatement.
    def exitAdvanceStatement(self, ctx:LDLPParser.AdvanceStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#outputStream.
    def enterOutputStream(self, ctx:LDLPParser.OutputStreamContext):
        pass

    # Exit a parse tree produced by LDLPParser#outputStream.
    def exitOutputStream(self, ctx:LDLPParser.OutputStreamContext):
        pass


    # Enter a parse tree produced by LDLPParser#assignment.
    def enterAssignment(self, ctx:LDLPParser.AssignmentContext):
        pass

    # Exit a parse tree produced by LDLPParser#assignment.
    def exitAssignment(self, ctx:LDLPParser.AssignmentContext):
        pass


    # Enter a parse tree produced by LDLPParser#attachStatement.
    def enterAttachStatement(self, ctx:LDLPParser.AttachStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#attachStatement.
    def exitAttachStatement(self, ctx:LDLPParser.AttachStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#attachAndSpaceStatement.
    def enterAttachAndSpaceStatement(self, ctx:LDLPParser.AttachAndSpaceStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#attachAndSpaceStatement.
    def exitAttachAndSpaceStatement(self, ctx:LDLPParser.AttachAndSpaceStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#attributeStatement.
    def enterAttributeStatement(self, ctx:LDLPParser.AttributeStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#attributeStatement.
    def exitAttributeStatement(self, ctx:LDLPParser.AttributeStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#beginpageStatement.
    def enterBeginpageStatement(self, ctx:LDLPParser.BeginpageStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#beginpageStatement.
    def exitBeginpageStatement(self, ctx:LDLPParser.BeginpageStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#breakStatement.
    def enterBreakStatement(self, ctx:LDLPParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#breakStatement.
    def exitBreakStatement(self, ctx:LDLPParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#case.
    def enterCase(self, ctx:LDLPParser.CaseContext):
        pass

    # Exit a parse tree produced by LDLPParser#case.
    def exitCase(self, ctx:LDLPParser.CaseContext):
        pass


    # Enter a parse tree produced by LDLPParser#otherwise.
    def enterOtherwise(self, ctx:LDLPParser.OtherwiseContext):
        pass

    # Exit a parse tree produced by LDLPParser#otherwise.
    def exitOtherwise(self, ctx:LDLPParser.OtherwiseContext):
        pass


    # Enter a parse tree produced by LDLPParser#caseStatement.
    def enterCaseStatement(self, ctx:LDLPParser.CaseStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#caseStatement.
    def exitCaseStatement(self, ctx:LDLPParser.CaseStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#beginCase.
    def enterBeginCase(self, ctx:LDLPParser.BeginCaseContext):
        pass

    # Exit a parse tree produced by LDLPParser#beginCase.
    def exitBeginCase(self, ctx:LDLPParser.BeginCaseContext):
        pass


    # Enter a parse tree produced by LDLPParser#endcase.
    def enterEndcase(self, ctx:LDLPParser.EndcaseContext):
        pass

    # Exit a parse tree produced by LDLPParser#endcase.
    def exitEndcase(self, ctx:LDLPParser.EndcaseContext):
        pass


    # Enter a parse tree produced by LDLPParser#computeStatement.
    def enterComputeStatement(self, ctx:LDLPParser.ComputeStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#computeStatement.
    def exitComputeStatement(self, ctx:LDLPParser.ComputeStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#continueStatement.
    def enterContinueStatement(self, ctx:LDLPParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#continueStatement.
    def exitContinueStatement(self, ctx:LDLPParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#criticalpointStatement.
    def enterCriticalpointStatement(self, ctx:LDLPParser.CriticalpointStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#criticalpointStatement.
    def exitCriticalpointStatement(self, ctx:LDLPParser.CriticalpointStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#cursorStatement.
    def enterCursorStatement(self, ctx:LDLPParser.CursorStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#cursorStatement.
    def exitCursorStatement(self, ctx:LDLPParser.CursorStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#dateConvertStatement.
    def enterDateConvertStatement(self, ctx:LDLPParser.DateConvertStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#dateConvertStatement.
    def exitDateConvertStatement(self, ctx:LDLPParser.DateConvertStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#dateVariable.
    def enterDateVariable(self, ctx:LDLPParser.DateVariableContext):
        pass

    # Exit a parse tree produced by LDLPParser#dateVariable.
    def exitDateVariable(self, ctx:LDLPParser.DateVariableContext):
        pass


    # Enter a parse tree produced by LDLPParser#detachStatement.
    def enterDetachStatement(self, ctx:LDLPParser.DetachStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#detachStatement.
    def exitDetachStatement(self, ctx:LDLPParser.DetachStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#determineStatement.
    def enterDetermineStatement(self, ctx:LDLPParser.DetermineStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#determineStatement.
    def exitDetermineStatement(self, ctx:LDLPParser.DetermineStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#determineActualStatement.
    def enterDetermineActualStatement(self, ctx:LDLPParser.DetermineActualStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#determineActualStatement.
    def exitDetermineActualStatement(self, ctx:LDLPParser.DetermineActualStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#variant.
    def enterVariant(self, ctx:LDLPParser.VariantContext):
        pass

    # Exit a parse tree produced by LDLPParser#variant.
    def exitVariant(self, ctx:LDLPParser.VariantContext):
        pass


    # Enter a parse tree produced by LDLPParser#databaseVariant.
    def enterDatabaseVariant(self, ctx:LDLPParser.DatabaseVariantContext):
        pass

    # Exit a parse tree produced by LDLPParser#databaseVariant.
    def exitDatabaseVariant(self, ctx:LDLPParser.DatabaseVariantContext):
        pass


    # Enter a parse tree produced by LDLPParser#extractFileVariant.
    def enterExtractFileVariant(self, ctx:LDLPParser.ExtractFileVariantContext):
        pass

    # Exit a parse tree produced by LDLPParser#extractFileVariant.
    def exitExtractFileVariant(self, ctx:LDLPParser.ExtractFileVariantContext):
        pass


    # Enter a parse tree produced by LDLPParser#determineBackStatement.
    def enterDetermineBackStatement(self, ctx:LDLPParser.DetermineBackStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#determineBackStatement.
    def exitDetermineBackStatement(self, ctx:LDLPParser.DetermineBackStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#determineEveryStatement.
    def enterDetermineEveryStatement(self, ctx:LDLPParser.DetermineEveryStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#determineEveryStatement.
    def exitDetermineEveryStatement(self, ctx:LDLPParser.DetermineEveryStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#determineFromStatement.
    def enterDetermineFromStatement(self, ctx:LDLPParser.DetermineFromStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#determineFromStatement.
    def exitDetermineFromStatement(self, ctx:LDLPParser.DetermineFromStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#determineGroupStatement.
    def enterDetermineGroupStatement(self, ctx:LDLPParser.DetermineGroupStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#determineGroupStatement.
    def exitDetermineGroupStatement(self, ctx:LDLPParser.DetermineGroupStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#determineLastStatement.
    def enterDetermineLastStatement(self, ctx:LDLPParser.DetermineLastStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#determineLastStatement.
    def exitDetermineLastStatement(self, ctx:LDLPParser.DetermineLastStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#determineTotalStatement.
    def enterDetermineTotalStatement(self, ctx:LDLPParser.DetermineTotalStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#determineTotalStatement.
    def exitDetermineTotalStatement(self, ctx:LDLPParser.DetermineTotalStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#attributeName.
    def enterAttributeName(self, ctx:LDLPParser.AttributeNameContext):
        pass

    # Exit a parse tree produced by LDLPParser#attributeName.
    def exitAttributeName(self, ctx:LDLPParser.AttributeNameContext):
        pass


    # Enter a parse tree produced by LDLPParser#keyArguments.
    def enterKeyArguments(self, ctx:LDLPParser.KeyArgumentsContext):
        pass

    # Exit a parse tree produced by LDLPParser#keyArguments.
    def exitKeyArguments(self, ctx:LDLPParser.KeyArgumentsContext):
        pass


    # Enter a parse tree produced by LDLPParser#records.
    def enterRecords(self, ctx:LDLPParser.RecordsContext):
        pass

    # Exit a parse tree produced by LDLPParser#records.
    def exitRecords(self, ctx:LDLPParser.RecordsContext):
        pass


    # Enter a parse tree produced by LDLPParser#extractFile.
    def enterExtractFile(self, ctx:LDLPParser.ExtractFileContext):
        pass

    # Exit a parse tree produced by LDLPParser#extractFile.
    def exitExtractFile(self, ctx:LDLPParser.ExtractFileContext):
        pass


    # Enter a parse tree produced by LDLPParser#iterator.
    def enterIterator(self, ctx:LDLPParser.IteratorContext):
        pass

    # Exit a parse tree produced by LDLPParser#iterator.
    def exitIterator(self, ctx:LDLPParser.IteratorContext):
        pass


    # Enter a parse tree produced by LDLPParser#argument.
    def enterArgument(self, ctx:LDLPParser.ArgumentContext):
        pass

    # Exit a parse tree produced by LDLPParser#argument.
    def exitArgument(self, ctx:LDLPParser.ArgumentContext):
        pass


    # Enter a parse tree produced by LDLPParser#determineEnd.
    def enterDetermineEnd(self, ctx:LDLPParser.DetermineEndContext):
        pass

    # Exit a parse tree produced by LDLPParser#determineEnd.
    def exitDetermineEnd(self, ctx:LDLPParser.DetermineEndContext):
        pass


    # Enter a parse tree produced by LDLPParser#divideStatement.
    def enterDivideStatement(self, ctx:LDLPParser.DivideStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#divideStatement.
    def exitDivideStatement(self, ctx:LDLPParser.DivideStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#dowhenBlock.
    def enterDowhenBlock(self, ctx:LDLPParser.DowhenBlockContext):
        pass

    # Exit a parse tree produced by LDLPParser#dowhenBlock.
    def exitDowhenBlock(self, ctx:LDLPParser.DowhenBlockContext):
        pass


    # Enter a parse tree produced by LDLPParser#elseBlock.
    def enterElseBlock(self, ctx:LDLPParser.ElseBlockContext):
        pass

    # Exit a parse tree produced by LDLPParser#elseBlock.
    def exitElseBlock(self, ctx:LDLPParser.ElseBlockContext):
        pass


    # Enter a parse tree produced by LDLPParser#dowhenStatement.
    def enterDowhenStatement(self, ctx:LDLPParser.DowhenStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#dowhenStatement.
    def exitDowhenStatement(self, ctx:LDLPParser.DowhenStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#condition.
    def enterCondition(self, ctx:LDLPParser.ConditionContext):
        pass

    # Exit a parse tree produced by LDLPParser#condition.
    def exitCondition(self, ctx:LDLPParser.ConditionContext):
        pass


    # Enter a parse tree produced by LDLPParser#classAttribute.
    def enterClassAttribute(self, ctx:LDLPParser.ClassAttributeContext):
        pass

    # Exit a parse tree produced by LDLPParser#classAttribute.
    def exitClassAttribute(self, ctx:LDLPParser.ClassAttributeContext):
        pass


    # Enter a parse tree produced by LDLPParser#endDowhen.
    def enterEndDowhen(self, ctx:LDLPParser.EndDowhenContext):
        pass

    # Exit a parse tree produced by LDLPParser#endDowhen.
    def exitEndDowhen(self, ctx:LDLPParser.EndDowhenContext):
        pass


    # Enter a parse tree produced by LDLPParser#enduseStatement.
    def enterEnduseStatement(self, ctx:LDLPParser.EnduseStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#enduseStatement.
    def exitEnduseStatement(self, ctx:LDLPParser.EnduseStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#excludeStatement.
    def enterExcludeStatement(self, ctx:LDLPParser.ExcludeStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#excludeStatement.
    def exitExcludeStatement(self, ctx:LDLPParser.ExcludeStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#ifStatement.
    def enterIfStatement(self, ctx:LDLPParser.IfStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#ifStatement.
    def exitIfStatement(self, ctx:LDLPParser.IfStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#endIf.
    def enterEndIf(self, ctx:LDLPParser.EndIfContext):
        pass

    # Exit a parse tree produced by LDLPParser#endIf.
    def exitEndIf(self, ctx:LDLPParser.EndIfContext):
        pass


    # Enter a parse tree produced by LDLPParser#methodCall.
    def enterMethodCall(self, ctx:LDLPParser.MethodCallContext):
        pass

    # Exit a parse tree produced by LDLPParser#methodCall.
    def exitMethodCall(self, ctx:LDLPParser.MethodCallContext):
        pass


    # Enter a parse tree produced by LDLPParser#expression.
    def enterExpression(self, ctx:LDLPParser.ExpressionContext):
        pass

    # Exit a parse tree produced by LDLPParser#expression.
    def exitExpression(self, ctx:LDLPParser.ExpressionContext):
        pass


    # Enter a parse tree produced by LDLPParser#stringExpression.
    def enterStringExpression(self, ctx:LDLPParser.StringExpressionContext):
        pass

    # Exit a parse tree produced by LDLPParser#stringExpression.
    def exitStringExpression(self, ctx:LDLPParser.StringExpressionContext):
        pass


    # Enter a parse tree produced by LDLPParser#paramList.
    def enterParamList(self, ctx:LDLPParser.ParamListContext):
        pass

    # Exit a parse tree produced by LDLPParser#paramList.
    def exitParamList(self, ctx:LDLPParser.ParamListContext):
        pass


    # Enter a parse tree produced by LDLPParser#param.
    def enterParam(self, ctx:LDLPParser.ParamContext):
        pass

    # Exit a parse tree produced by LDLPParser#param.
    def exitParam(self, ctx:LDLPParser.ParamContext):
        pass


    # Enter a parse tree produced by LDLPParser#extractStatement.
    def enterExtractStatement(self, ctx:LDLPParser.ExtractStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#extractStatement.
    def exitExtractStatement(self, ctx:LDLPParser.ExtractStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#header.
    def enterHeader(self, ctx:LDLPParser.HeaderContext):
        pass

    # Exit a parse tree produced by LDLPParser#header.
    def exitHeader(self, ctx:LDLPParser.HeaderContext):
        pass


    # Enter a parse tree produced by LDLPParser#foreachStatement.
    def enterForeachStatement(self, ctx:LDLPParser.ForeachStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#foreachStatement.
    def exitForeachStatement(self, ctx:LDLPParser.ForeachStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#flagStatement.
    def enterFlagStatement(self, ctx:LDLPParser.FlagStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#flagStatement.
    def exitFlagStatement(self, ctx:LDLPParser.FlagStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#initializeStatement.
    def enterInitializeStatement(self, ctx:LDLPParser.InitializeStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#initializeStatement.
    def exitInitializeStatement(self, ctx:LDLPParser.InitializeStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#initializationValue.
    def enterInitializationValue(self, ctx:LDLPParser.InitializationValueContext):
        pass

    # Exit a parse tree produced by LDLPParser#initializationValue.
    def exitInitializationValue(self, ctx:LDLPParser.InitializationValueContext):
        pass


    # Enter a parse tree produced by LDLPParser#insertStatement.
    def enterInsertStatement(self, ctx:LDLPParser.InsertStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#insertStatement.
    def exitInsertStatement(self, ctx:LDLPParser.InsertStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#insertable.
    def enterInsertable(self, ctx:LDLPParser.InsertableContext):
        pass

    # Exit a parse tree produced by LDLPParser#insertable.
    def exitInsertable(self, ctx:LDLPParser.InsertableContext):
        pass


    # Enter a parse tree produced by LDLPParser#mapping.
    def enterMapping(self, ctx:LDLPParser.MappingContext):
        pass

    # Exit a parse tree produced by LDLPParser#mapping.
    def exitMapping(self, ctx:LDLPParser.MappingContext):
        pass


    # Enter a parse tree produced by LDLPParser#tableName.
    def enterTableName(self, ctx:LDLPParser.TableNameContext):
        pass

    # Exit a parse tree produced by LDLPParser#tableName.
    def exitTableName(self, ctx:LDLPParser.TableNameContext):
        pass


    # Enter a parse tree produced by LDLPParser#jumptoStatement.
    def enterJumptoStatement(self, ctx:LDLPParser.JumptoStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#jumptoStatement.
    def exitJumptoStatement(self, ctx:LDLPParser.JumptoStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#labelStatement.
    def enterLabelStatement(self, ctx:LDLPParser.LabelStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#labelStatement.
    def exitLabelStatement(self, ctx:LDLPParser.LabelStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#label.
    def enterLabel(self, ctx:LDLPParser.LabelContext):
        pass

    # Exit a parse tree produced by LDLPParser#label.
    def exitLabel(self, ctx:LDLPParser.LabelContext):
        pass


    # Enter a parse tree produced by LDLPParser#loadStatement.
    def enterLoadStatement(self, ctx:LDLPParser.LoadStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#loadStatement.
    def exitLoadStatement(self, ctx:LDLPParser.LoadStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#ispecAttribute.
    def enterIspecAttribute(self, ctx:LDLPParser.IspecAttributeContext):
        pass

    # Exit a parse tree produced by LDLPParser#ispecAttribute.
    def exitIspecAttribute(self, ctx:LDLPParser.IspecAttributeContext):
        pass


    # Enter a parse tree produced by LDLPParser#logStatement.
    def enterLogStatement(self, ctx:LDLPParser.LogStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#logStatement.
    def exitLogStatement(self, ctx:LDLPParser.LogStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#lookupStatement.
    def enterLookupStatement(self, ctx:LDLPParser.LookupStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#lookupStatement.
    def exitLookupStatement(self, ctx:LDLPParser.LookupStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#lookupBaseStatement.
    def enterLookupBaseStatement(self, ctx:LDLPParser.LookupBaseStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#lookupBaseStatement.
    def exitLookupBaseStatement(self, ctx:LDLPParser.LookupBaseStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#lookupFromStatement.
    def enterLookupFromStatement(self, ctx:LDLPParser.LookupFromStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#lookupFromStatement.
    def exitLookupFromStatement(self, ctx:LDLPParser.LookupFromStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#lookupEveryStatement.
    def enterLookupEveryStatement(self, ctx:LDLPParser.LookupEveryStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#lookupEveryStatement.
    def exitLookupEveryStatement(self, ctx:LDLPParser.LookupEveryStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#lookupGroupStatement.
    def enterLookupGroupStatement(self, ctx:LDLPParser.LookupGroupStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#lookupGroupStatement.
    def exitLookupGroupStatement(self, ctx:LDLPParser.LookupGroupStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#loopStatement.
    def enterLoopStatement(self, ctx:LDLPParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#loopStatement.
    def exitLoopStatement(self, ctx:LDLPParser.LoopStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#loopBlock.
    def enterLoopBlock(self, ctx:LDLPParser.LoopBlockContext):
        pass

    # Exit a parse tree produced by LDLPParser#loopBlock.
    def exitLoopBlock(self, ctx:LDLPParser.LoopBlockContext):
        pass


    # Enter a parse tree produced by LDLPParser#compareType.
    def enterCompareType(self, ctx:LDLPParser.CompareTypeContext):
        pass

    # Exit a parse tree produced by LDLPParser#compareType.
    def exitCompareType(self, ctx:LDLPParser.CompareTypeContext):
        pass


    # Enter a parse tree produced by LDLPParser#matchStatement.
    def enterMatchStatement(self, ctx:LDLPParser.MatchStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#matchStatement.
    def exitMatchStatement(self, ctx:LDLPParser.MatchStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#messageStatement.
    def enterMessageStatement(self, ctx:LDLPParser.MessageStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#messageStatement.
    def exitMessageStatement(self, ctx:LDLPParser.MessageStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#moveStatement.
    def enterMoveStatement(self, ctx:LDLPParser.MoveStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#moveStatement.
    def exitMoveStatement(self, ctx:LDLPParser.MoveStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#length.
    def enterLength(self, ctx:LDLPParser.LengthContext):
        pass

    # Exit a parse tree produced by LDLPParser#length.
    def exitLength(self, ctx:LDLPParser.LengthContext):
        pass


    # Enter a parse tree produced by LDLPParser#source_variable.
    def enterSource_variable(self, ctx:LDLPParser.Source_variableContext):
        pass

    # Exit a parse tree produced by LDLPParser#source_variable.
    def exitSource_variable(self, ctx:LDLPParser.Source_variableContext):
        pass


    # Enter a parse tree produced by LDLPParser#target_variable.
    def enterTarget_variable(self, ctx:LDLPParser.Target_variableContext):
        pass

    # Exit a parse tree produced by LDLPParser#target_variable.
    def exitTarget_variable(self, ctx:LDLPParser.Target_variableContext):
        pass


    # Enter a parse tree produced by LDLPParser#movedateStatement.
    def enterMovedateStatement(self, ctx:LDLPParser.MovedateStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#movedateStatement.
    def exitMovedateStatement(self, ctx:LDLPParser.MovedateStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#movetimeStatement.
    def enterMovetimeStatement(self, ctx:LDLPParser.MovetimeStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#movetimeStatement.
    def exitMovetimeStatement(self, ctx:LDLPParser.MovetimeStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#multiplyStatement.
    def enterMultiplyStatement(self, ctx:LDLPParser.MultiplyStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#multiplyStatement.
    def exitMultiplyStatement(self, ctx:LDLPParser.MultiplyStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#onchangeStatement.
    def enterOnchangeStatement(self, ctx:LDLPParser.OnchangeStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#onchangeStatement.
    def exitOnchangeStatement(self, ctx:LDLPParser.OnchangeStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#routineCall.
    def enterRoutineCall(self, ctx:LDLPParser.RoutineCallContext):
        pass

    # Exit a parse tree produced by LDLPParser#routineCall.
    def exitRoutineCall(self, ctx:LDLPParser.RoutineCallContext):
        pass


    # Enter a parse tree produced by LDLPParser#pageStatement.
    def enterPageStatement(self, ctx:LDLPParser.PageStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#pageStatement.
    def exitPageStatement(self, ctx:LDLPParser.PageStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#recallStatement.
    def enterRecallStatement(self, ctx:LDLPParser.RecallStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#recallStatement.
    def exitRecallStatement(self, ctx:LDLPParser.RecallStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#releaseStatement.
    def enterReleaseStatement(self, ctx:LDLPParser.ReleaseStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#releaseStatement.
    def exitReleaseStatement(self, ctx:LDLPParser.ReleaseStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#restartStatement.
    def enterRestartStatement(self, ctx:LDLPParser.RestartStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#restartStatement.
    def exitRestartStatement(self, ctx:LDLPParser.RestartStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#rocStatement.
    def enterRocStatement(self, ctx:LDLPParser.RocStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#rocStatement.
    def exitRocStatement(self, ctx:LDLPParser.RocStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#returnStatement.
    def enterReturnStatement(self, ctx:LDLPParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#returnStatement.
    def exitReturnStatement(self, ctx:LDLPParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#instance.
    def enterInstance(self, ctx:LDLPParser.InstanceContext):
        pass

    # Exit a parse tree produced by LDLPParser#instance.
    def exitInstance(self, ctx:LDLPParser.InstanceContext):
        pass


    # Enter a parse tree produced by LDLPParser#interface.
    def enterInterface(self, ctx:LDLPParser.InterfaceContext):
        pass

    # Exit a parse tree produced by LDLPParser#interface.
    def exitInterface(self, ctx:LDLPParser.InterfaceContext):
        pass


    # Enter a parse tree produced by LDLPParser#runStatement.
    def enterRunStatement(self, ctx:LDLPParser.RunStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#runStatement.
    def exitRunStatement(self, ctx:LDLPParser.RunStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#device.
    def enterDevice(self, ctx:LDLPParser.DeviceContext):
        pass

    # Exit a parse tree produced by LDLPParser#device.
    def exitDevice(self, ctx:LDLPParser.DeviceContext):
        pass


    # Enter a parse tree produced by LDLPParser#sleepStatement.
    def enterSleepStatement(self, ctx:LDLPParser.SleepStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#sleepStatement.
    def exitSleepStatement(self, ctx:LDLPParser.SleepStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#startStatement.
    def enterStartStatement(self, ctx:LDLPParser.StartStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#startStatement.
    def exitStartStatement(self, ctx:LDLPParser.StartStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#sendListDynamicStatement.
    def enterSendListDynamicStatement(self, ctx:LDLPParser.SendListDynamicStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#sendListDynamicStatement.
    def exitSendListDynamicStatement(self, ctx:LDLPParser.SendListDynamicStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#sendListStaticStatement.
    def enterSendListStaticStatement(self, ctx:LDLPParser.SendListStaticStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#sendListStaticStatement.
    def exitSendListStaticStatement(self, ctx:LDLPParser.SendListStaticStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#downloadFile.
    def enterDownloadFile(self, ctx:LDLPParser.DownloadFileContext):
        pass

    # Exit a parse tree produced by LDLPParser#downloadFile.
    def exitDownloadFile(self, ctx:LDLPParser.DownloadFileContext):
        pass


    # Enter a parse tree produced by LDLPParser#sendMessageStatement.
    def enterSendMessageStatement(self, ctx:LDLPParser.SendMessageStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#sendMessageStatement.
    def exitSendMessageStatement(self, ctx:LDLPParser.SendMessageStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#sendPrintStatement.
    def enterSendPrintStatement(self, ctx:LDLPParser.SendPrintStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#sendPrintStatement.
    def exitSendPrintStatement(self, ctx:LDLPParser.SendPrintStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#setDBStatement.
    def enterSetDBStatement(self, ctx:LDLPParser.SetDBStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#setDBStatement.
    def exitSetDBStatement(self, ctx:LDLPParser.SetDBStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#setTitleStatement.
    def enterSetTitleStatement(self, ctx:LDLPParser.SetTitleStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#setTitleStatement.
    def exitSetTitleStatement(self, ctx:LDLPParser.SetTitleStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#stninfoStatement.
    def enterStninfoStatement(self, ctx:LDLPParser.StninfoStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#stninfoStatement.
    def exitStninfoStatement(self, ctx:LDLPParser.StninfoStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#subtractStatement.
    def enterSubtractStatement(self, ctx:LDLPParser.SubtractStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#subtractStatement.
    def exitSubtractStatement(self, ctx:LDLPParser.SubtractStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#switchtoStatement.
    def enterSwitchtoStatement(self, ctx:LDLPParser.SwitchtoStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#switchtoStatement.
    def exitSwitchtoStatement(self, ctx:LDLPParser.SwitchtoStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#wakeStatement.
    def enterWakeStatement(self, ctx:LDLPParser.WakeStatementContext):
        pass

    # Exit a parse tree produced by LDLPParser#wakeStatement.
    def exitWakeStatement(self, ctx:LDLPParser.WakeStatementContext):
        pass


    # Enter a parse tree produced by LDLPParser#relational_operator.
    def enterRelational_operator(self, ctx:LDLPParser.Relational_operatorContext):
        pass

    # Exit a parse tree produced by LDLPParser#relational_operator.
    def exitRelational_operator(self, ctx:LDLPParser.Relational_operatorContext):
        pass


    # Enter a parse tree produced by LDLPParser#logical_operator.
    def enterLogical_operator(self, ctx:LDLPParser.Logical_operatorContext):
        pass

    # Exit a parse tree produced by LDLPParser#logical_operator.
    def exitLogical_operator(self, ctx:LDLPParser.Logical_operatorContext):
        pass


    # Enter a parse tree produced by LDLPParser#status.
    def enterStatus(self, ctx:LDLPParser.StatusContext):
        pass

    # Exit a parse tree produced by LDLPParser#status.
    def exitStatus(self, ctx:LDLPParser.StatusContext):
        pass


    # Enter a parse tree produced by LDLPParser#dbName.
    def enterDbName(self, ctx:LDLPParser.DbNameContext):
        pass

    # Exit a parse tree produced by LDLPParser#dbName.
    def exitDbName(self, ctx:LDLPParser.DbNameContext):
        pass


    # Enter a parse tree produced by LDLPParser#fileName.
    def enterFileName(self, ctx:LDLPParser.FileNameContext):
        pass

    # Exit a parse tree produced by LDLPParser#fileName.
    def exitFileName(self, ctx:LDLPParser.FileNameContext):
        pass


    # Enter a parse tree produced by LDLPParser#dateFormat.
    def enterDateFormat(self, ctx:LDLPParser.DateFormatContext):
        pass

    # Exit a parse tree produced by LDLPParser#dateFormat.
    def exitDateFormat(self, ctx:LDLPParser.DateFormatContext):
        pass


    # Enter a parse tree produced by LDLPParser#className.
    def enterClassName(self, ctx:LDLPParser.ClassNameContext):
        pass

    # Exit a parse tree produced by LDLPParser#className.
    def exitClassName(self, ctx:LDLPParser.ClassNameContext):
        pass


    # Enter a parse tree produced by LDLPParser#varName.
    def enterVarName(self, ctx:LDLPParser.VarNameContext):
        pass

    # Exit a parse tree produced by LDLPParser#varName.
    def exitVarName(self, ctx:LDLPParser.VarNameContext):
        pass


    # Enter a parse tree produced by LDLPParser#objectName.
    def enterObjectName(self, ctx:LDLPParser.ObjectNameContext):
        pass

    # Exit a parse tree produced by LDLPParser#objectName.
    def exitObjectName(self, ctx:LDLPParser.ObjectNameContext):
        pass


    # Enter a parse tree produced by LDLPParser#userCode.
    def enterUserCode(self, ctx:LDLPParser.UserCodeContext):
        pass

    # Exit a parse tree produced by LDLPParser#userCode.
    def exitUserCode(self, ctx:LDLPParser.UserCodeContext):
        pass


    # Enter a parse tree produced by LDLPParser#frameName.
    def enterFrameName(self, ctx:LDLPParser.FrameNameContext):
        pass

    # Exit a parse tree produced by LDLPParser#frameName.
    def exitFrameName(self, ctx:LDLPParser.FrameNameContext):
        pass


    # Enter a parse tree produced by LDLPParser#lineNumber.
    def enterLineNumber(self, ctx:LDLPParser.LineNumberContext):
        pass

    # Exit a parse tree produced by LDLPParser#lineNumber.
    def exitLineNumber(self, ctx:LDLPParser.LineNumberContext):
        pass


    # Enter a parse tree produced by LDLPParser#pageNumber.
    def enterPageNumber(self, ctx:LDLPParser.PageNumberContext):
        pass

    # Exit a parse tree produced by LDLPParser#pageNumber.
    def exitPageNumber(self, ctx:LDLPParser.PageNumberContext):
        pass


    # Enter a parse tree produced by LDLPParser#reportName.
    def enterReportName(self, ctx:LDLPParser.ReportNameContext):
        pass

    # Exit a parse tree produced by LDLPParser#reportName.
    def exitReportName(self, ctx:LDLPParser.ReportNameContext):
        pass


    # Enter a parse tree produced by LDLPParser#profileName.
    def enterProfileName(self, ctx:LDLPParser.ProfileNameContext):
        pass

    # Exit a parse tree produced by LDLPParser#profileName.
    def exitProfileName(self, ctx:LDLPParser.ProfileNameContext):
        pass


    # Enter a parse tree produced by LDLPParser#deviceName.
    def enterDeviceName(self, ctx:LDLPParser.DeviceNameContext):
        pass

    # Exit a parse tree produced by LDLPParser#deviceName.
    def exitDeviceName(self, ctx:LDLPParser.DeviceNameContext):
        pass


    # Enter a parse tree produced by LDLPParser#keywords.
    def enterKeywords(self, ctx:LDLPParser.KeywordsContext):
        pass

    # Exit a parse tree produced by LDLPParser#keywords.
    def exitKeywords(self, ctx:LDLPParser.KeywordsContext):
        pass


    # Enter a parse tree produced by LDLPParser#specialName.
    def enterSpecialName(self, ctx:LDLPParser.SpecialNameContext):
        pass

    # Exit a parse tree produced by LDLPParser#specialName.
    def exitSpecialName(self, ctx:LDLPParser.SpecialNameContext):
        pass


    # Enter a parse tree produced by LDLPParser#variable.
    def enterVariable(self, ctx:LDLPParser.VariableContext):
        pass

    # Exit a parse tree produced by LDLPParser#variable.
    def exitVariable(self, ctx:LDLPParser.VariableContext):
        pass


    # Enter a parse tree produced by LDLPParser#identifier.
    def enterIdentifier(self, ctx:LDLPParser.IdentifierContext):
        pass

    # Exit a parse tree produced by LDLPParser#identifier.
    def exitIdentifier(self, ctx:LDLPParser.IdentifierContext):
        pass


    # Enter a parse tree produced by LDLPParser#literal.
    def enterLiteral(self, ctx:LDLPParser.LiteralContext):
        pass

    # Exit a parse tree produced by LDLPParser#literal.
    def exitLiteral(self, ctx:LDLPParser.LiteralContext):
        pass



del LDLPParser