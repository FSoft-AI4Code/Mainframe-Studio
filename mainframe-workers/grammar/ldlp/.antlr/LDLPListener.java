// Generated from /Users/nguyen/Work/mainframe-workers/grammar/ldlp/LDLP.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link LDLPParser}.
 */
public interface LDLPListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link LDLPParser#startRule}.
	 * @param ctx the parse tree
	 */
	void enterStartRule(LDLPParser.StartRuleContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#startRule}.
	 * @param ctx the parse tree
	 */
	void exitStartRule(LDLPParser.StartRuleContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#runtime}.
	 * @param ctx the parse tree
	 */
	void enterRuntime(LDLPParser.RuntimeContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#runtime}.
	 * @param ctx the parse tree
	 */
	void exitRuntime(LDLPParser.RuntimeContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#conditionHeader}.
	 * @param ctx the parse tree
	 */
	void enterConditionHeader(LDLPParser.ConditionHeaderContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#conditionHeader}.
	 * @param ctx the parse tree
	 */
	void exitConditionHeader(LDLPParser.ConditionHeaderContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#statements}.
	 * @param ctx the parse tree
	 */
	void enterStatements(LDLPParser.StatementsContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#statements}.
	 * @param ctx the parse tree
	 */
	void exitStatements(LDLPParser.StatementsContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(LDLPParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(LDLPParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#thisAssignStatement}.
	 * @param ctx the parse tree
	 */
	void enterThisAssignStatement(LDLPParser.ThisAssignStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#thisAssignStatement}.
	 * @param ctx the parse tree
	 */
	void exitThisAssignStatement(LDLPParser.ThisAssignStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#thisMethodCalledStatement}.
	 * @param ctx the parse tree
	 */
	void enterThisMethodCalledStatement(LDLPParser.ThisMethodCalledStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#thisMethodCalledStatement}.
	 * @param ctx the parse tree
	 */
	void exitThisMethodCalledStatement(LDLPParser.ThisMethodCalledStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#functionCallingStatement}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCallingStatement(LDLPParser.FunctionCallingStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#functionCallingStatement}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCallingStatement(LDLPParser.FunctionCallingStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#function_name}.
	 * @param ctx the parse tree
	 */
	void enterFunction_name(LDLPParser.Function_nameContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#function_name}.
	 * @param ctx the parse tree
	 */
	void exitFunction_name(LDLPParser.Function_nameContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#abortStatement}.
	 * @param ctx the parse tree
	 */
	void enterAbortStatement(LDLPParser.AbortStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#abortStatement}.
	 * @param ctx the parse tree
	 */
	void exitAbortStatement(LDLPParser.AbortStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#acceptStatement}.
	 * @param ctx the parse tree
	 */
	void enterAcceptStatement(LDLPParser.AcceptStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#acceptStatement}.
	 * @param ctx the parse tree
	 */
	void exitAcceptStatement(LDLPParser.AcceptStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#accessExtStatement}.
	 * @param ctx the parse tree
	 */
	void enterAccessExtStatement(LDLPParser.AccessExtStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#accessExtStatement}.
	 * @param ctx the parse tree
	 */
	void exitAccessExtStatement(LDLPParser.AccessExtStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#locator}.
	 * @param ctx the parse tree
	 */
	void enterLocator(LDLPParser.LocatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#locator}.
	 * @param ctx the parse tree
	 */
	void exitLocator(LDLPParser.LocatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#find}.
	 * @param ctx the parse tree
	 */
	void enterFind(LDLPParser.FindContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#find}.
	 * @param ctx the parse tree
	 */
	void exitFind(LDLPParser.FindContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#get}.
	 * @param ctx the parse tree
	 */
	void enterGet(LDLPParser.GetContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#get}.
	 * @param ctx the parse tree
	 */
	void exitGet(LDLPParser.GetContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#addStatement}.
	 * @param ctx the parse tree
	 */
	void enterAddStatement(LDLPParser.AddStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#addStatement}.
	 * @param ctx the parse tree
	 */
	void exitAddStatement(LDLPParser.AddStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#advanceStatement}.
	 * @param ctx the parse tree
	 */
	void enterAdvanceStatement(LDLPParser.AdvanceStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#advanceStatement}.
	 * @param ctx the parse tree
	 */
	void exitAdvanceStatement(LDLPParser.AdvanceStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#outputStream}.
	 * @param ctx the parse tree
	 */
	void enterOutputStream(LDLPParser.OutputStreamContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#outputStream}.
	 * @param ctx the parse tree
	 */
	void exitOutputStream(LDLPParser.OutputStreamContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(LDLPParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(LDLPParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#attachStatement}.
	 * @param ctx the parse tree
	 */
	void enterAttachStatement(LDLPParser.AttachStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#attachStatement}.
	 * @param ctx the parse tree
	 */
	void exitAttachStatement(LDLPParser.AttachStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#attachAndSpaceStatement}.
	 * @param ctx the parse tree
	 */
	void enterAttachAndSpaceStatement(LDLPParser.AttachAndSpaceStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#attachAndSpaceStatement}.
	 * @param ctx the parse tree
	 */
	void exitAttachAndSpaceStatement(LDLPParser.AttachAndSpaceStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#attributeStatement}.
	 * @param ctx the parse tree
	 */
	void enterAttributeStatement(LDLPParser.AttributeStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#attributeStatement}.
	 * @param ctx the parse tree
	 */
	void exitAttributeStatement(LDLPParser.AttributeStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#beginpageStatement}.
	 * @param ctx the parse tree
	 */
	void enterBeginpageStatement(LDLPParser.BeginpageStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#beginpageStatement}.
	 * @param ctx the parse tree
	 */
	void exitBeginpageStatement(LDLPParser.BeginpageStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#breakStatement}.
	 * @param ctx the parse tree
	 */
	void enterBreakStatement(LDLPParser.BreakStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#breakStatement}.
	 * @param ctx the parse tree
	 */
	void exitBreakStatement(LDLPParser.BreakStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#case}.
	 * @param ctx the parse tree
	 */
	void enterCase(LDLPParser.CaseContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#case}.
	 * @param ctx the parse tree
	 */
	void exitCase(LDLPParser.CaseContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#otherwise}.
	 * @param ctx the parse tree
	 */
	void enterOtherwise(LDLPParser.OtherwiseContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#otherwise}.
	 * @param ctx the parse tree
	 */
	void exitOtherwise(LDLPParser.OtherwiseContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#caseStatement}.
	 * @param ctx the parse tree
	 */
	void enterCaseStatement(LDLPParser.CaseStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#caseStatement}.
	 * @param ctx the parse tree
	 */
	void exitCaseStatement(LDLPParser.CaseStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#beginCase}.
	 * @param ctx the parse tree
	 */
	void enterBeginCase(LDLPParser.BeginCaseContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#beginCase}.
	 * @param ctx the parse tree
	 */
	void exitBeginCase(LDLPParser.BeginCaseContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#endcase}.
	 * @param ctx the parse tree
	 */
	void enterEndcase(LDLPParser.EndcaseContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#endcase}.
	 * @param ctx the parse tree
	 */
	void exitEndcase(LDLPParser.EndcaseContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#computeStatement}.
	 * @param ctx the parse tree
	 */
	void enterComputeStatement(LDLPParser.ComputeStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#computeStatement}.
	 * @param ctx the parse tree
	 */
	void exitComputeStatement(LDLPParser.ComputeStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#continueStatement}.
	 * @param ctx the parse tree
	 */
	void enterContinueStatement(LDLPParser.ContinueStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#continueStatement}.
	 * @param ctx the parse tree
	 */
	void exitContinueStatement(LDLPParser.ContinueStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#criticalpointStatement}.
	 * @param ctx the parse tree
	 */
	void enterCriticalpointStatement(LDLPParser.CriticalpointStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#criticalpointStatement}.
	 * @param ctx the parse tree
	 */
	void exitCriticalpointStatement(LDLPParser.CriticalpointStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#cursorStatement}.
	 * @param ctx the parse tree
	 */
	void enterCursorStatement(LDLPParser.CursorStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#cursorStatement}.
	 * @param ctx the parse tree
	 */
	void exitCursorStatement(LDLPParser.CursorStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#dateConvertStatement}.
	 * @param ctx the parse tree
	 */
	void enterDateConvertStatement(LDLPParser.DateConvertStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#dateConvertStatement}.
	 * @param ctx the parse tree
	 */
	void exitDateConvertStatement(LDLPParser.DateConvertStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#dateVariable}.
	 * @param ctx the parse tree
	 */
	void enterDateVariable(LDLPParser.DateVariableContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#dateVariable}.
	 * @param ctx the parse tree
	 */
	void exitDateVariable(LDLPParser.DateVariableContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#detachStatement}.
	 * @param ctx the parse tree
	 */
	void enterDetachStatement(LDLPParser.DetachStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#detachStatement}.
	 * @param ctx the parse tree
	 */
	void exitDetachStatement(LDLPParser.DetachStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#determineStatement}.
	 * @param ctx the parse tree
	 */
	void enterDetermineStatement(LDLPParser.DetermineStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#determineStatement}.
	 * @param ctx the parse tree
	 */
	void exitDetermineStatement(LDLPParser.DetermineStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#determineActualStatement}.
	 * @param ctx the parse tree
	 */
	void enterDetermineActualStatement(LDLPParser.DetermineActualStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#determineActualStatement}.
	 * @param ctx the parse tree
	 */
	void exitDetermineActualStatement(LDLPParser.DetermineActualStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#variant}.
	 * @param ctx the parse tree
	 */
	void enterVariant(LDLPParser.VariantContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#variant}.
	 * @param ctx the parse tree
	 */
	void exitVariant(LDLPParser.VariantContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#databaseVariant}.
	 * @param ctx the parse tree
	 */
	void enterDatabaseVariant(LDLPParser.DatabaseVariantContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#databaseVariant}.
	 * @param ctx the parse tree
	 */
	void exitDatabaseVariant(LDLPParser.DatabaseVariantContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#extractFileVariant}.
	 * @param ctx the parse tree
	 */
	void enterExtractFileVariant(LDLPParser.ExtractFileVariantContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#extractFileVariant}.
	 * @param ctx the parse tree
	 */
	void exitExtractFileVariant(LDLPParser.ExtractFileVariantContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#determineBackStatement}.
	 * @param ctx the parse tree
	 */
	void enterDetermineBackStatement(LDLPParser.DetermineBackStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#determineBackStatement}.
	 * @param ctx the parse tree
	 */
	void exitDetermineBackStatement(LDLPParser.DetermineBackStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#determineEveryStatement}.
	 * @param ctx the parse tree
	 */
	void enterDetermineEveryStatement(LDLPParser.DetermineEveryStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#determineEveryStatement}.
	 * @param ctx the parse tree
	 */
	void exitDetermineEveryStatement(LDLPParser.DetermineEveryStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#determineFromStatement}.
	 * @param ctx the parse tree
	 */
	void enterDetermineFromStatement(LDLPParser.DetermineFromStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#determineFromStatement}.
	 * @param ctx the parse tree
	 */
	void exitDetermineFromStatement(LDLPParser.DetermineFromStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#determineGroupStatement}.
	 * @param ctx the parse tree
	 */
	void enterDetermineGroupStatement(LDLPParser.DetermineGroupStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#determineGroupStatement}.
	 * @param ctx the parse tree
	 */
	void exitDetermineGroupStatement(LDLPParser.DetermineGroupStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#determineLastStatement}.
	 * @param ctx the parse tree
	 */
	void enterDetermineLastStatement(LDLPParser.DetermineLastStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#determineLastStatement}.
	 * @param ctx the parse tree
	 */
	void exitDetermineLastStatement(LDLPParser.DetermineLastStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#determineTotal}.
	 * @param ctx the parse tree
	 */
	void enterDetermineTotal(LDLPParser.DetermineTotalContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#determineTotal}.
	 * @param ctx the parse tree
	 */
	void exitDetermineTotal(LDLPParser.DetermineTotalContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#attributeName}.
	 * @param ctx the parse tree
	 */
	void enterAttributeName(LDLPParser.AttributeNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#attributeName}.
	 * @param ctx the parse tree
	 */
	void exitAttributeName(LDLPParser.AttributeNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#keyArguments}.
	 * @param ctx the parse tree
	 */
	void enterKeyArguments(LDLPParser.KeyArgumentsContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#keyArguments}.
	 * @param ctx the parse tree
	 */
	void exitKeyArguments(LDLPParser.KeyArgumentsContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#records}.
	 * @param ctx the parse tree
	 */
	void enterRecords(LDLPParser.RecordsContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#records}.
	 * @param ctx the parse tree
	 */
	void exitRecords(LDLPParser.RecordsContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#extractFile}.
	 * @param ctx the parse tree
	 */
	void enterExtractFile(LDLPParser.ExtractFileContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#extractFile}.
	 * @param ctx the parse tree
	 */
	void exitExtractFile(LDLPParser.ExtractFileContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#iterator}.
	 * @param ctx the parse tree
	 */
	void enterIterator(LDLPParser.IteratorContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#iterator}.
	 * @param ctx the parse tree
	 */
	void exitIterator(LDLPParser.IteratorContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#object}.
	 * @param ctx the parse tree
	 */
	void enterObject(LDLPParser.ObjectContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#object}.
	 * @param ctx the parse tree
	 */
	void exitObject(LDLPParser.ObjectContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#profile}.
	 * @param ctx the parse tree
	 */
	void enterProfile(LDLPParser.ProfileContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#profile}.
	 * @param ctx the parse tree
	 */
	void exitProfile(LDLPParser.ProfileContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#argument}.
	 * @param ctx the parse tree
	 */
	void enterArgument(LDLPParser.ArgumentContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#argument}.
	 * @param ctx the parse tree
	 */
	void exitArgument(LDLPParser.ArgumentContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#determineEnd}.
	 * @param ctx the parse tree
	 */
	void enterDetermineEnd(LDLPParser.DetermineEndContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#determineEnd}.
	 * @param ctx the parse tree
	 */
	void exitDetermineEnd(LDLPParser.DetermineEndContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#divideStatement}.
	 * @param ctx the parse tree
	 */
	void enterDivideStatement(LDLPParser.DivideStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#divideStatement}.
	 * @param ctx the parse tree
	 */
	void exitDivideStatement(LDLPParser.DivideStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#dowhenBlock}.
	 * @param ctx the parse tree
	 */
	void enterDowhenBlock(LDLPParser.DowhenBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#dowhenBlock}.
	 * @param ctx the parse tree
	 */
	void exitDowhenBlock(LDLPParser.DowhenBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#elseBlock}.
	 * @param ctx the parse tree
	 */
	void enterElseBlock(LDLPParser.ElseBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#elseBlock}.
	 * @param ctx the parse tree
	 */
	void exitElseBlock(LDLPParser.ElseBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#dowhenStatement}.
	 * @param ctx the parse tree
	 */
	void enterDowhenStatement(LDLPParser.DowhenStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#dowhenStatement}.
	 * @param ctx the parse tree
	 */
	void exitDowhenStatement(LDLPParser.DowhenStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(LDLPParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(LDLPParser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#classAttribute}.
	 * @param ctx the parse tree
	 */
	void enterClassAttribute(LDLPParser.ClassAttributeContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#classAttribute}.
	 * @param ctx the parse tree
	 */
	void exitClassAttribute(LDLPParser.ClassAttributeContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#endDowhen}.
	 * @param ctx the parse tree
	 */
	void enterEndDowhen(LDLPParser.EndDowhenContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#endDowhen}.
	 * @param ctx the parse tree
	 */
	void exitEndDowhen(LDLPParser.EndDowhenContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#enduseStatement}.
	 * @param ctx the parse tree
	 */
	void enterEnduseStatement(LDLPParser.EnduseStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#enduseStatement}.
	 * @param ctx the parse tree
	 */
	void exitEnduseStatement(LDLPParser.EnduseStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#excludeStatement}.
	 * @param ctx the parse tree
	 */
	void enterExcludeStatement(LDLPParser.ExcludeStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#excludeStatement}.
	 * @param ctx the parse tree
	 */
	void exitExcludeStatement(LDLPParser.ExcludeStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(LDLPParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(LDLPParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#endIf}.
	 * @param ctx the parse tree
	 */
	void enterEndIf(LDLPParser.EndIfContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#endIf}.
	 * @param ctx the parse tree
	 */
	void exitEndIf(LDLPParser.EndIfContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#methodCall}.
	 * @param ctx the parse tree
	 */
	void enterMethodCall(LDLPParser.MethodCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#methodCall}.
	 * @param ctx the parse tree
	 */
	void exitMethodCall(LDLPParser.MethodCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(LDLPParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(LDLPParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#conditionalExpression}.
	 * @param ctx the parse tree
	 */
	void enterConditionalExpression(LDLPParser.ConditionalExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#conditionalExpression}.
	 * @param ctx the parse tree
	 */
	void exitConditionalExpression(LDLPParser.ConditionalExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#setExpression}.
	 * @param ctx the parse tree
	 */
	void enterSetExpression(LDLPParser.SetExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#setExpression}.
	 * @param ctx the parse tree
	 */
	void exitSetExpression(LDLPParser.SetExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#stringExpression}.
	 * @param ctx the parse tree
	 */
	void enterStringExpression(LDLPParser.StringExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#stringExpression}.
	 * @param ctx the parse tree
	 */
	void exitStringExpression(LDLPParser.StringExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#paramList}.
	 * @param ctx the parse tree
	 */
	void enterParamList(LDLPParser.ParamListContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#paramList}.
	 * @param ctx the parse tree
	 */
	void exitParamList(LDLPParser.ParamListContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#param}.
	 * @param ctx the parse tree
	 */
	void enterParam(LDLPParser.ParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#param}.
	 * @param ctx the parse tree
	 */
	void exitParam(LDLPParser.ParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#extractStatement}.
	 * @param ctx the parse tree
	 */
	void enterExtractStatement(LDLPParser.ExtractStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#extractStatement}.
	 * @param ctx the parse tree
	 */
	void exitExtractStatement(LDLPParser.ExtractStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#header}.
	 * @param ctx the parse tree
	 */
	void enterHeader(LDLPParser.HeaderContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#header}.
	 * @param ctx the parse tree
	 */
	void exitHeader(LDLPParser.HeaderContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#foreachStatement}.
	 * @param ctx the parse tree
	 */
	void enterForeachStatement(LDLPParser.ForeachStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#foreachStatement}.
	 * @param ctx the parse tree
	 */
	void exitForeachStatement(LDLPParser.ForeachStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#flagStatement}.
	 * @param ctx the parse tree
	 */
	void enterFlagStatement(LDLPParser.FlagStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#flagStatement}.
	 * @param ctx the parse tree
	 */
	void exitFlagStatement(LDLPParser.FlagStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#initializeStatement}.
	 * @param ctx the parse tree
	 */
	void enterInitializeStatement(LDLPParser.InitializeStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#initializeStatement}.
	 * @param ctx the parse tree
	 */
	void exitInitializeStatement(LDLPParser.InitializeStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#initializationValue}.
	 * @param ctx the parse tree
	 */
	void enterInitializationValue(LDLPParser.InitializationValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#initializationValue}.
	 * @param ctx the parse tree
	 */
	void exitInitializationValue(LDLPParser.InitializationValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#insertStatement}.
	 * @param ctx the parse tree
	 */
	void enterInsertStatement(LDLPParser.InsertStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#insertStatement}.
	 * @param ctx the parse tree
	 */
	void exitInsertStatement(LDLPParser.InsertStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#insertable}.
	 * @param ctx the parse tree
	 */
	void enterInsertable(LDLPParser.InsertableContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#insertable}.
	 * @param ctx the parse tree
	 */
	void exitInsertable(LDLPParser.InsertableContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#mapping}.
	 * @param ctx the parse tree
	 */
	void enterMapping(LDLPParser.MappingContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#mapping}.
	 * @param ctx the parse tree
	 */
	void exitMapping(LDLPParser.MappingContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#tableName}.
	 * @param ctx the parse tree
	 */
	void enterTableName(LDLPParser.TableNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#tableName}.
	 * @param ctx the parse tree
	 */
	void exitTableName(LDLPParser.TableNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#jumptoStatement}.
	 * @param ctx the parse tree
	 */
	void enterJumptoStatement(LDLPParser.JumptoStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#jumptoStatement}.
	 * @param ctx the parse tree
	 */
	void exitJumptoStatement(LDLPParser.JumptoStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#labelStatement}.
	 * @param ctx the parse tree
	 */
	void enterLabelStatement(LDLPParser.LabelStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#labelStatement}.
	 * @param ctx the parse tree
	 */
	void exitLabelStatement(LDLPParser.LabelStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#label}.
	 * @param ctx the parse tree
	 */
	void enterLabel(LDLPParser.LabelContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#label}.
	 * @param ctx the parse tree
	 */
	void exitLabel(LDLPParser.LabelContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#loadStatement}.
	 * @param ctx the parse tree
	 */
	void enterLoadStatement(LDLPParser.LoadStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#loadStatement}.
	 * @param ctx the parse tree
	 */
	void exitLoadStatement(LDLPParser.LoadStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#ispecAttribute}.
	 * @param ctx the parse tree
	 */
	void enterIspecAttribute(LDLPParser.IspecAttributeContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#ispecAttribute}.
	 * @param ctx the parse tree
	 */
	void exitIspecAttribute(LDLPParser.IspecAttributeContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#logStatement}.
	 * @param ctx the parse tree
	 */
	void enterLogStatement(LDLPParser.LogStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#logStatement}.
	 * @param ctx the parse tree
	 */
	void exitLogStatement(LDLPParser.LogStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#lookupStatement}.
	 * @param ctx the parse tree
	 */
	void enterLookupStatement(LDLPParser.LookupStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#lookupStatement}.
	 * @param ctx the parse tree
	 */
	void exitLookupStatement(LDLPParser.LookupStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#lookupBaseStatement}.
	 * @param ctx the parse tree
	 */
	void enterLookupBaseStatement(LDLPParser.LookupBaseStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#lookupBaseStatement}.
	 * @param ctx the parse tree
	 */
	void exitLookupBaseStatement(LDLPParser.LookupBaseStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#lookupFromStatement}.
	 * @param ctx the parse tree
	 */
	void enterLookupFromStatement(LDLPParser.LookupFromStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#lookupFromStatement}.
	 * @param ctx the parse tree
	 */
	void exitLookupFromStatement(LDLPParser.LookupFromStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#lookupEveryStatement}.
	 * @param ctx the parse tree
	 */
	void enterLookupEveryStatement(LDLPParser.LookupEveryStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#lookupEveryStatement}.
	 * @param ctx the parse tree
	 */
	void exitLookupEveryStatement(LDLPParser.LookupEveryStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#lookupGroupStatement}.
	 * @param ctx the parse tree
	 */
	void enterLookupGroupStatement(LDLPParser.LookupGroupStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#lookupGroupStatement}.
	 * @param ctx the parse tree
	 */
	void exitLookupGroupStatement(LDLPParser.LookupGroupStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#loopStatement}.
	 * @param ctx the parse tree
	 */
	void enterLoopStatement(LDLPParser.LoopStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#loopStatement}.
	 * @param ctx the parse tree
	 */
	void exitLoopStatement(LDLPParser.LoopStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#loopBlock}.
	 * @param ctx the parse tree
	 */
	void enterLoopBlock(LDLPParser.LoopBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#loopBlock}.
	 * @param ctx the parse tree
	 */
	void exitLoopBlock(LDLPParser.LoopBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#compareType}.
	 * @param ctx the parse tree
	 */
	void enterCompareType(LDLPParser.CompareTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#compareType}.
	 * @param ctx the parse tree
	 */
	void exitCompareType(LDLPParser.CompareTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#matchStatement}.
	 * @param ctx the parse tree
	 */
	void enterMatchStatement(LDLPParser.MatchStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#matchStatement}.
	 * @param ctx the parse tree
	 */
	void exitMatchStatement(LDLPParser.MatchStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#messageStatement}.
	 * @param ctx the parse tree
	 */
	void enterMessageStatement(LDLPParser.MessageStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#messageStatement}.
	 * @param ctx the parse tree
	 */
	void exitMessageStatement(LDLPParser.MessageStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#moveStatement}.
	 * @param ctx the parse tree
	 */
	void enterMoveStatement(LDLPParser.MoveStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#moveStatement}.
	 * @param ctx the parse tree
	 */
	void exitMoveStatement(LDLPParser.MoveStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#length}.
	 * @param ctx the parse tree
	 */
	void enterLength(LDLPParser.LengthContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#length}.
	 * @param ctx the parse tree
	 */
	void exitLength(LDLPParser.LengthContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#pos}.
	 * @param ctx the parse tree
	 */
	void enterPos(LDLPParser.PosContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#pos}.
	 * @param ctx the parse tree
	 */
	void exitPos(LDLPParser.PosContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#movedateStatement}.
	 * @param ctx the parse tree
	 */
	void enterMovedateStatement(LDLPParser.MovedateStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#movedateStatement}.
	 * @param ctx the parse tree
	 */
	void exitMovedateStatement(LDLPParser.MovedateStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#movetimeStatement}.
	 * @param ctx the parse tree
	 */
	void enterMovetimeStatement(LDLPParser.MovetimeStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#movetimeStatement}.
	 * @param ctx the parse tree
	 */
	void exitMovetimeStatement(LDLPParser.MovetimeStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#multiplyStatement}.
	 * @param ctx the parse tree
	 */
	void enterMultiplyStatement(LDLPParser.MultiplyStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#multiplyStatement}.
	 * @param ctx the parse tree
	 */
	void exitMultiplyStatement(LDLPParser.MultiplyStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#onchangeStatement}.
	 * @param ctx the parse tree
	 */
	void enterOnchangeStatement(LDLPParser.OnchangeStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#onchangeStatement}.
	 * @param ctx the parse tree
	 */
	void exitOnchangeStatement(LDLPParser.OnchangeStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#routineCall}.
	 * @param ctx the parse tree
	 */
	void enterRoutineCall(LDLPParser.RoutineCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#routineCall}.
	 * @param ctx the parse tree
	 */
	void exitRoutineCall(LDLPParser.RoutineCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#pageStatement}.
	 * @param ctx the parse tree
	 */
	void enterPageStatement(LDLPParser.PageStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#pageStatement}.
	 * @param ctx the parse tree
	 */
	void exitPageStatement(LDLPParser.PageStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#recallStatement}.
	 * @param ctx the parse tree
	 */
	void enterRecallStatement(LDLPParser.RecallStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#recallStatement}.
	 * @param ctx the parse tree
	 */
	void exitRecallStatement(LDLPParser.RecallStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#releaseStatement}.
	 * @param ctx the parse tree
	 */
	void enterReleaseStatement(LDLPParser.ReleaseStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#releaseStatement}.
	 * @param ctx the parse tree
	 */
	void exitReleaseStatement(LDLPParser.ReleaseStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#restartStatement}.
	 * @param ctx the parse tree
	 */
	void enterRestartStatement(LDLPParser.RestartStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#restartStatement}.
	 * @param ctx the parse tree
	 */
	void exitRestartStatement(LDLPParser.RestartStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#rocStatement}.
	 * @param ctx the parse tree
	 */
	void enterRocStatement(LDLPParser.RocStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#rocStatement}.
	 * @param ctx the parse tree
	 */
	void exitRocStatement(LDLPParser.RocStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void enterReturnStatement(LDLPParser.ReturnStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void exitReturnStatement(LDLPParser.ReturnStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#instance}.
	 * @param ctx the parse tree
	 */
	void enterInstance(LDLPParser.InstanceContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#instance}.
	 * @param ctx the parse tree
	 */
	void exitInstance(LDLPParser.InstanceContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#interface}.
	 * @param ctx the parse tree
	 */
	void enterInterface(LDLPParser.InterfaceContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#interface}.
	 * @param ctx the parse tree
	 */
	void exitInterface(LDLPParser.InterfaceContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#runStatement}.
	 * @param ctx the parse tree
	 */
	void enterRunStatement(LDLPParser.RunStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#runStatement}.
	 * @param ctx the parse tree
	 */
	void exitRunStatement(LDLPParser.RunStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#device}.
	 * @param ctx the parse tree
	 */
	void enterDevice(LDLPParser.DeviceContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#device}.
	 * @param ctx the parse tree
	 */
	void exitDevice(LDLPParser.DeviceContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#sleepStatement}.
	 * @param ctx the parse tree
	 */
	void enterSleepStatement(LDLPParser.SleepStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#sleepStatement}.
	 * @param ctx the parse tree
	 */
	void exitSleepStatement(LDLPParser.SleepStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#startStatement}.
	 * @param ctx the parse tree
	 */
	void enterStartStatement(LDLPParser.StartStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#startStatement}.
	 * @param ctx the parse tree
	 */
	void exitStartStatement(LDLPParser.StartStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#sendListDynamicStatement}.
	 * @param ctx the parse tree
	 */
	void enterSendListDynamicStatement(LDLPParser.SendListDynamicStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#sendListDynamicStatement}.
	 * @param ctx the parse tree
	 */
	void exitSendListDynamicStatement(LDLPParser.SendListDynamicStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#sendListStaticStatement}.
	 * @param ctx the parse tree
	 */
	void enterSendListStaticStatement(LDLPParser.SendListStaticStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#sendListStaticStatement}.
	 * @param ctx the parse tree
	 */
	void exitSendListStaticStatement(LDLPParser.SendListStaticStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#downloadFile}.
	 * @param ctx the parse tree
	 */
	void enterDownloadFile(LDLPParser.DownloadFileContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#downloadFile}.
	 * @param ctx the parse tree
	 */
	void exitDownloadFile(LDLPParser.DownloadFileContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#sendMessageStatement}.
	 * @param ctx the parse tree
	 */
	void enterSendMessageStatement(LDLPParser.SendMessageStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#sendMessageStatement}.
	 * @param ctx the parse tree
	 */
	void exitSendMessageStatement(LDLPParser.SendMessageStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#sendPrintStatement}.
	 * @param ctx the parse tree
	 */
	void enterSendPrintStatement(LDLPParser.SendPrintStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#sendPrintStatement}.
	 * @param ctx the parse tree
	 */
	void exitSendPrintStatement(LDLPParser.SendPrintStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#setDBStatement}.
	 * @param ctx the parse tree
	 */
	void enterSetDBStatement(LDLPParser.SetDBStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#setDBStatement}.
	 * @param ctx the parse tree
	 */
	void exitSetDBStatement(LDLPParser.SetDBStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#setTitleStatement}.
	 * @param ctx the parse tree
	 */
	void enterSetTitleStatement(LDLPParser.SetTitleStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#setTitleStatement}.
	 * @param ctx the parse tree
	 */
	void exitSetTitleStatement(LDLPParser.SetTitleStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#stninfoStatement}.
	 * @param ctx the parse tree
	 */
	void enterStninfoStatement(LDLPParser.StninfoStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#stninfoStatement}.
	 * @param ctx the parse tree
	 */
	void exitStninfoStatement(LDLPParser.StninfoStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#subtractStatement}.
	 * @param ctx the parse tree
	 */
	void enterSubtractStatement(LDLPParser.SubtractStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#subtractStatement}.
	 * @param ctx the parse tree
	 */
	void exitSubtractStatement(LDLPParser.SubtractStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#switchtoStatement}.
	 * @param ctx the parse tree
	 */
	void enterSwitchtoStatement(LDLPParser.SwitchtoStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#switchtoStatement}.
	 * @param ctx the parse tree
	 */
	void exitSwitchtoStatement(LDLPParser.SwitchtoStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#wakeStatement}.
	 * @param ctx the parse tree
	 */
	void enterWakeStatement(LDLPParser.WakeStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#wakeStatement}.
	 * @param ctx the parse tree
	 */
	void exitWakeStatement(LDLPParser.WakeStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#relational_operator}.
	 * @param ctx the parse tree
	 */
	void enterRelational_operator(LDLPParser.Relational_operatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#relational_operator}.
	 * @param ctx the parse tree
	 */
	void exitRelational_operator(LDLPParser.Relational_operatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#logical_operator}.
	 * @param ctx the parse tree
	 */
	void enterLogical_operator(LDLPParser.Logical_operatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#logical_operator}.
	 * @param ctx the parse tree
	 */
	void exitLogical_operator(LDLPParser.Logical_operatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#status}.
	 * @param ctx the parse tree
	 */
	void enterStatus(LDLPParser.StatusContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#status}.
	 * @param ctx the parse tree
	 */
	void exitStatus(LDLPParser.StatusContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#dbName}.
	 * @param ctx the parse tree
	 */
	void enterDbName(LDLPParser.DbNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#dbName}.
	 * @param ctx the parse tree
	 */
	void exitDbName(LDLPParser.DbNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#fileName}.
	 * @param ctx the parse tree
	 */
	void enterFileName(LDLPParser.FileNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#fileName}.
	 * @param ctx the parse tree
	 */
	void exitFileName(LDLPParser.FileNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#dateFormat}.
	 * @param ctx the parse tree
	 */
	void enterDateFormat(LDLPParser.DateFormatContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#dateFormat}.
	 * @param ctx the parse tree
	 */
	void exitDateFormat(LDLPParser.DateFormatContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#className}.
	 * @param ctx the parse tree
	 */
	void enterClassName(LDLPParser.ClassNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#className}.
	 * @param ctx the parse tree
	 */
	void exitClassName(LDLPParser.ClassNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#varName}.
	 * @param ctx the parse tree
	 */
	void enterVarName(LDLPParser.VarNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#varName}.
	 * @param ctx the parse tree
	 */
	void exitVarName(LDLPParser.VarNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#objectName}.
	 * @param ctx the parse tree
	 */
	void enterObjectName(LDLPParser.ObjectNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#objectName}.
	 * @param ctx the parse tree
	 */
	void exitObjectName(LDLPParser.ObjectNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#userCode}.
	 * @param ctx the parse tree
	 */
	void enterUserCode(LDLPParser.UserCodeContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#userCode}.
	 * @param ctx the parse tree
	 */
	void exitUserCode(LDLPParser.UserCodeContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#frameName}.
	 * @param ctx the parse tree
	 */
	void enterFrameName(LDLPParser.FrameNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#frameName}.
	 * @param ctx the parse tree
	 */
	void exitFrameName(LDLPParser.FrameNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#lineNumber}.
	 * @param ctx the parse tree
	 */
	void enterLineNumber(LDLPParser.LineNumberContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#lineNumber}.
	 * @param ctx the parse tree
	 */
	void exitLineNumber(LDLPParser.LineNumberContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#pageNumber}.
	 * @param ctx the parse tree
	 */
	void enterPageNumber(LDLPParser.PageNumberContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#pageNumber}.
	 * @param ctx the parse tree
	 */
	void exitPageNumber(LDLPParser.PageNumberContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#reportName}.
	 * @param ctx the parse tree
	 */
	void enterReportName(LDLPParser.ReportNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#reportName}.
	 * @param ctx the parse tree
	 */
	void exitReportName(LDLPParser.ReportNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#profileName}.
	 * @param ctx the parse tree
	 */
	void enterProfileName(LDLPParser.ProfileNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#profileName}.
	 * @param ctx the parse tree
	 */
	void exitProfileName(LDLPParser.ProfileNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#deviceName}.
	 * @param ctx the parse tree
	 */
	void enterDeviceName(LDLPParser.DeviceNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#deviceName}.
	 * @param ctx the parse tree
	 */
	void exitDeviceName(LDLPParser.DeviceNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#keywords}.
	 * @param ctx the parse tree
	 */
	void enterKeywords(LDLPParser.KeywordsContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#keywords}.
	 * @param ctx the parse tree
	 */
	void exitKeywords(LDLPParser.KeywordsContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#specialName}.
	 * @param ctx the parse tree
	 */
	void enterSpecialName(LDLPParser.SpecialNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#specialName}.
	 * @param ctx the parse tree
	 */
	void exitSpecialName(LDLPParser.SpecialNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#variable}.
	 * @param ctx the parse tree
	 */
	void enterVariable(LDLPParser.VariableContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#variable}.
	 * @param ctx the parse tree
	 */
	void exitVariable(LDLPParser.VariableContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#identifier}.
	 * @param ctx the parse tree
	 */
	void enterIdentifier(LDLPParser.IdentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#identifier}.
	 * @param ctx the parse tree
	 */
	void exitIdentifier(LDLPParser.IdentifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#qualifier}.
	 * @param ctx the parse tree
	 */
	void enterQualifier(LDLPParser.QualifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#qualifier}.
	 * @param ctx the parse tree
	 */
	void exitQualifier(LDLPParser.QualifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link LDLPParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(LDLPParser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link LDLPParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(LDLPParser.LiteralContext ctx);
}