// Generated from /home/neil/Documents/mainframe-workers/grammar/clist/Clist.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ClistParser}.
 */
public interface ClistListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ClistParser#startRule}.
	 * @param ctx the parse tree
	 */
	void enterStartRule(ClistParser.StartRuleContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#startRule}.
	 * @param ctx the parse tree
	 */
	void exitStartRule(ClistParser.StartRuleContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#procedure}.
	 * @param ctx the parse tree
	 */
	void enterProcedure(ClistParser.ProcedureContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#procedure}.
	 * @param ctx the parse tree
	 */
	void exitProcedure(ClistParser.ProcedureContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#labelEnd}.
	 * @param ctx the parse tree
	 */
	void enterLabelEnd(ClistParser.LabelEndContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#labelEnd}.
	 * @param ctx the parse tree
	 */
	void exitLabelEnd(ClistParser.LabelEndContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#procOption}.
	 * @param ctx the parse tree
	 */
	void enterProcOption(ClistParser.ProcOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#procOption}.
	 * @param ctx the parse tree
	 */
	void exitProcOption(ClistParser.ProcOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#label}.
	 * @param ctx the parse tree
	 */
	void enterLabel(ClistParser.LabelContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#label}.
	 * @param ctx the parse tree
	 */
	void exitLabel(ClistParser.LabelContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#commandName}.
	 * @param ctx the parse tree
	 */
	void enterCommandName(ClistParser.CommandNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#commandName}.
	 * @param ctx the parse tree
	 */
	void exitCommandName(ClistParser.CommandNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#labelName}.
	 * @param ctx the parse tree
	 */
	void enterLabelName(ClistParser.LabelNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#labelName}.
	 * @param ctx the parse tree
	 */
	void exitLabelName(ClistParser.LabelNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(ClistParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(ClistParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#hlistStatement}.
	 * @param ctx the parse tree
	 */
	void enterHlistStatement(ClistParser.HlistStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#hlistStatement}.
	 * @param ctx the parse tree
	 */
	void exitHlistStatement(ClistParser.HlistStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#hlistParameter}.
	 * @param ctx the parse tree
	 */
	void enterHlistParameter(ClistParser.HlistParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#hlistParameter}.
	 * @param ctx the parse tree
	 */
	void exitHlistParameter(ClistParser.HlistParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#jprintrStatement}.
	 * @param ctx the parse tree
	 */
	void enterJprintrStatement(ClistParser.JprintrStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#jprintrStatement}.
	 * @param ctx the parse tree
	 */
	void exitJprintrStatement(ClistParser.JprintrStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#jprintContent}.
	 * @param ctx the parse tree
	 */
	void enterJprintContent(ClistParser.JprintContentContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#jprintContent}.
	 * @param ctx the parse tree
	 */
	void exitJprintContent(ClistParser.JprintContentContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#jprintParameter}.
	 * @param ctx the parse tree
	 */
	void enterJprintParameter(ClistParser.JprintParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#jprintParameter}.
	 * @param ctx the parse tree
	 */
	void exitJprintParameter(ClistParser.JprintParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#hrecoverStatement}.
	 * @param ctx the parse tree
	 */
	void enterHrecoverStatement(ClistParser.HrecoverStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#hrecoverStatement}.
	 * @param ctx the parse tree
	 */
	void exitHrecoverStatement(ClistParser.HrecoverStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#hrecoverParameter}.
	 * @param ctx the parse tree
	 */
	void enterHrecoverParameter(ClistParser.HrecoverParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#hrecoverParameter}.
	 * @param ctx the parse tree
	 */
	void exitHrecoverParameter(ClistParser.HrecoverParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#kdsPrintStatement}.
	 * @param ctx the parse tree
	 */
	void enterKdsPrintStatement(ClistParser.KdsPrintStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#kdsPrintStatement}.
	 * @param ctx the parse tree
	 */
	void exitKdsPrintStatement(ClistParser.KdsPrintStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#kdsPrintParamater}.
	 * @param ctx the parse tree
	 */
	void enterKdsPrintParamater(ClistParser.KdsPrintParamaterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#kdsPrintParamater}.
	 * @param ctx the parse tree
	 */
	void exitKdsPrintParamater(ClistParser.KdsPrintParamaterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#cancelStatement}.
	 * @param ctx the parse tree
	 */
	void enterCancelStatement(ClistParser.CancelStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#cancelStatement}.
	 * @param ctx the parse tree
	 */
	void exitCancelStatement(ClistParser.CancelStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#outputStatement}.
	 * @param ctx the parse tree
	 */
	void enterOutputStatement(ClistParser.OutputStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#outputStatement}.
	 * @param ctx the parse tree
	 */
	void exitOutputStatement(ClistParser.OutputStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#outputParameter}.
	 * @param ctx the parse tree
	 */
	void enterOutputParameter(ClistParser.OutputParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#outputParameter}.
	 * @param ctx the parse tree
	 */
	void exitOutputParameter(ClistParser.OutputParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#job_parameter}.
	 * @param ctx the parse tree
	 */
	void enterJob_parameter(ClistParser.Job_parameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#job_parameter}.
	 * @param ctx the parse tree
	 */
	void exitJob_parameter(ClistParser.Job_parameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#job_name}.
	 * @param ctx the parse tree
	 */
	void enterJob_name(ClistParser.Job_nameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#job_name}.
	 * @param ctx the parse tree
	 */
	void exitJob_name(ClistParser.Job_nameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#job_id}.
	 * @param ctx the parse tree
	 */
	void enterJob_id(ClistParser.Job_idContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#job_id}.
	 * @param ctx the parse tree
	 */
	void exitJob_id(ClistParser.Job_idContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#execStatement}.
	 * @param ctx the parse tree
	 */
	void enterExecStatement(ClistParser.ExecStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#execStatement}.
	 * @param ctx the parse tree
	 */
	void exitExecStatement(ClistParser.ExecStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#selectStatement}.
	 * @param ctx the parse tree
	 */
	void enterSelectStatement(ClistParser.SelectStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#selectStatement}.
	 * @param ctx the parse tree
	 */
	void exitSelectStatement(ClistParser.SelectStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#otherwiseSelect}.
	 * @param ctx the parse tree
	 */
	void enterOtherwiseSelect(ClistParser.OtherwiseSelectContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#otherwiseSelect}.
	 * @param ctx the parse tree
	 */
	void exitOtherwiseSelect(ClistParser.OtherwiseSelectContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#testExpression}.
	 * @param ctx the parse tree
	 */
	void enterTestExpression(ClistParser.TestExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#testExpression}.
	 * @param ctx the parse tree
	 */
	void exitTestExpression(ClistParser.TestExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#whenSelect}.
	 * @param ctx the parse tree
	 */
	void enterWhenSelect(ClistParser.WhenSelectContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#whenSelect}.
	 * @param ctx the parse tree
	 */
	void exitWhenSelect(ClistParser.WhenSelectContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#readdvalStatement}.
	 * @param ctx the parse tree
	 */
	void enterReaddvalStatement(ClistParser.ReaddvalStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#readdvalStatement}.
	 * @param ctx the parse tree
	 */
	void exitReaddvalStatement(ClistParser.ReaddvalStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#putfileStatement}.
	 * @param ctx the parse tree
	 */
	void enterPutfileStatement(ClistParser.PutfileStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#putfileStatement}.
	 * @param ctx the parse tree
	 */
	void exitPutfileStatement(ClistParser.PutfileStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#doWhileStatement}.
	 * @param ctx the parse tree
	 */
	void enterDoWhileStatement(ClistParser.DoWhileStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#doWhileStatement}.
	 * @param ctx the parse tree
	 */
	void exitDoWhileStatement(ClistParser.DoWhileStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void enterReturnStatement(ClistParser.ReturnStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void exitReturnStatement(ClistParser.ReturnStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#errorStatement}.
	 * @param ctx the parse tree
	 */
	void enterErrorStatement(ClistParser.ErrorStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#errorStatement}.
	 * @param ctx the parse tree
	 */
	void exitErrorStatement(ClistParser.ErrorStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#listDmsStatement}.
	 * @param ctx the parse tree
	 */
	void enterListDmsStatement(ClistParser.ListDmsStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#listDmsStatement}.
	 * @param ctx the parse tree
	 */
	void exitListDmsStatement(ClistParser.ListDmsStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#listDmsParameter}.
	 * @param ctx the parse tree
	 */
	void enterListDmsParameter(ClistParser.ListDmsParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#listDmsParameter}.
	 * @param ctx the parse tree
	 */
	void exitListDmsParameter(ClistParser.ListDmsParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#attributeStatement}.
	 * @param ctx the parse tree
	 */
	void enterAttributeStatement(ClistParser.AttributeStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#attributeStatement}.
	 * @param ctx the parse tree
	 */
	void exitAttributeStatement(ClistParser.AttributeStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#attributeStatementParameter}.
	 * @param ctx the parse tree
	 */
	void enterAttributeStatementParameter(ClistParser.AttributeStatementParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#attributeStatementParameter}.
	 * @param ctx the parse tree
	 */
	void exitAttributeStatementParameter(ClistParser.AttributeStatementParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#deleteStatement}.
	 * @param ctx the parse tree
	 */
	void enterDeleteStatement(ClistParser.DeleteStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#deleteStatement}.
	 * @param ctx the parse tree
	 */
	void exitDeleteStatement(ClistParser.DeleteStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#setStatement}.
	 * @param ctx the parse tree
	 */
	void enterSetStatement(ClistParser.SetStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#setStatement}.
	 * @param ctx the parse tree
	 */
	void exitSetStatement(ClistParser.SetStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#variableAssignment}.
	 * @param ctx the parse tree
	 */
	void enterVariableAssignment(ClistParser.VariableAssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#variableAssignment}.
	 * @param ctx the parse tree
	 */
	void exitVariableAssignment(ClistParser.VariableAssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#globalStatement}.
	 * @param ctx the parse tree
	 */
	void enterGlobalStatement(ClistParser.GlobalStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#globalStatement}.
	 * @param ctx the parse tree
	 */
	void exitGlobalStatement(ClistParser.GlobalStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#ispExecStatement}.
	 * @param ctx the parse tree
	 */
	void enterIspExecStatement(ClistParser.IspExecStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#ispExecStatement}.
	 * @param ctx the parse tree
	 */
	void exitIspExecStatement(ClistParser.IspExecStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#fenService}.
	 * @param ctx the parse tree
	 */
	void enterFenService(ClistParser.FenServiceContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#fenService}.
	 * @param ctx the parse tree
	 */
	void exitFenService(ClistParser.FenServiceContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#fenParameter}.
	 * @param ctx the parse tree
	 */
	void enterFenParameter(ClistParser.FenParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#fenParameter}.
	 * @param ctx the parse tree
	 */
	void exitFenParameter(ClistParser.FenParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#addpopService}.
	 * @param ctx the parse tree
	 */
	void enterAddpopService(ClistParser.AddpopServiceContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#addpopService}.
	 * @param ctx the parse tree
	 */
	void exitAddpopService(ClistParser.AddpopServiceContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#addpopServiceParameter}.
	 * @param ctx the parse tree
	 */
	void enterAddpopServiceParameter(ClistParser.AddpopServiceParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#addpopServiceParameter}.
	 * @param ctx the parse tree
	 */
	void exitAddpopServiceParameter(ClistParser.AddpopServiceParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#displayService}.
	 * @param ctx the parse tree
	 */
	void enterDisplayService(ClistParser.DisplayServiceContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#displayService}.
	 * @param ctx the parse tree
	 */
	void exitDisplayService(ClistParser.DisplayServiceContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#displayParameter}.
	 * @param ctx the parse tree
	 */
	void enterDisplayParameter(ClistParser.DisplayParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#displayParameter}.
	 * @param ctx the parse tree
	 */
	void exitDisplayParameter(ClistParser.DisplayParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#logService}.
	 * @param ctx the parse tree
	 */
	void enterLogService(ClistParser.LogServiceContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#logService}.
	 * @param ctx the parse tree
	 */
	void exitLogService(ClistParser.LogServiceContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#message}.
	 * @param ctx the parse tree
	 */
	void enterMessage(ClistParser.MessageContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#message}.
	 * @param ctx the parse tree
	 */
	void exitMessage(ClistParser.MessageContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#controlService}.
	 * @param ctx the parse tree
	 */
	void enterControlService(ClistParser.ControlServiceContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#controlService}.
	 * @param ctx the parse tree
	 */
	void exitControlService(ClistParser.ControlServiceContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#controlServiceParameter}.
	 * @param ctx the parse tree
	 */
	void enterControlServiceParameter(ClistParser.ControlServiceParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#controlServiceParameter}.
	 * @param ctx the parse tree
	 */
	void exitControlServiceParameter(ClistParser.ControlServiceParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#tablebService}.
	 * @param ctx the parse tree
	 */
	void enterTablebService(ClistParser.TablebServiceContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#tablebService}.
	 * @param ctx the parse tree
	 */
	void exitTablebService(ClistParser.TablebServiceContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#tableServiceName}.
	 * @param ctx the parse tree
	 */
	void enterTableServiceName(ClistParser.TableServiceNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#tableServiceName}.
	 * @param ctx the parse tree
	 */
	void exitTableServiceName(ClistParser.TableServiceNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#table_name}.
	 * @param ctx the parse tree
	 */
	void enterTable_name(ClistParser.Table_nameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#table_name}.
	 * @param ctx the parse tree
	 */
	void exitTable_name(ClistParser.Table_nameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#tableParameter}.
	 * @param ctx the parse tree
	 */
	void enterTableParameter(ClistParser.TableParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#tableParameter}.
	 * @param ctx the parse tree
	 */
	void exitTableParameter(ClistParser.TableParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#lminitService}.
	 * @param ctx the parse tree
	 */
	void enterLminitService(ClistParser.LminitServiceContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#lminitService}.
	 * @param ctx the parse tree
	 */
	void exitLminitService(ClistParser.LminitServiceContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#lmfreeService}.
	 * @param ctx the parse tree
	 */
	void enterLmfreeService(ClistParser.LmfreeServiceContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#lmfreeService}.
	 * @param ctx the parse tree
	 */
	void exitLmfreeService(ClistParser.LmfreeServiceContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#lmcopyService}.
	 * @param ctx the parse tree
	 */
	void enterLmcopyService(ClistParser.LmcopyServiceContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#lmcopyService}.
	 * @param ctx the parse tree
	 */
	void exitLmcopyService(ClistParser.LmcopyServiceContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#fromMem}.
	 * @param ctx the parse tree
	 */
	void enterFromMem(ClistParser.FromMemContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#fromMem}.
	 * @param ctx the parse tree
	 */
	void exitFromMem(ClistParser.FromMemContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#toMem}.
	 * @param ctx the parse tree
	 */
	void enterToMem(ClistParser.ToMemContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#toMem}.
	 * @param ctx the parse tree
	 */
	void exitToMem(ClistParser.ToMemContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#lmcopyParameter}.
	 * @param ctx the parse tree
	 */
	void enterLmcopyParameter(ClistParser.LmcopyParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#lmcopyParameter}.
	 * @param ctx the parse tree
	 */
	void exitLmcopyParameter(ClistParser.LmcopyParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#fromId}.
	 * @param ctx the parse tree
	 */
	void enterFromId(ClistParser.FromIdContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#fromId}.
	 * @param ctx the parse tree
	 */
	void exitFromId(ClistParser.FromIdContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#toDataId}.
	 * @param ctx the parse tree
	 */
	void enterToDataId(ClistParser.ToDataIdContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#toDataId}.
	 * @param ctx the parse tree
	 */
	void exitToDataId(ClistParser.ToDataIdContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#lminitParameter}.
	 * @param ctx the parse tree
	 */
	void enterLminitParameter(ClistParser.LminitParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#lminitParameter}.
	 * @param ctx the parse tree
	 */
	void exitLminitParameter(ClistParser.LminitParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#fteraseService}.
	 * @param ctx the parse tree
	 */
	void enterFteraseService(ClistParser.FteraseServiceContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#fteraseService}.
	 * @param ctx the parse tree
	 */
	void exitFteraseService(ClistParser.FteraseServiceContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#browseService}.
	 * @param ctx the parse tree
	 */
	void enterBrowseService(ClistParser.BrowseServiceContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#browseService}.
	 * @param ctx the parse tree
	 */
	void exitBrowseService(ClistParser.BrowseServiceContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#browseServiceParameter}.
	 * @param ctx the parse tree
	 */
	void enterBrowseServiceParameter(ClistParser.BrowseServiceParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#browseServiceParameter}.
	 * @param ctx the parse tree
	 */
	void exitBrowseServiceParameter(ClistParser.BrowseServiceParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#editService}.
	 * @param ctx the parse tree
	 */
	void enterEditService(ClistParser.EditServiceContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#editService}.
	 * @param ctx the parse tree
	 */
	void exitEditService(ClistParser.EditServiceContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#editServiceParameter}.
	 * @param ctx the parse tree
	 */
	void enterEditServiceParameter(ClistParser.EditServiceParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#editServiceParameter}.
	 * @param ctx the parse tree
	 */
	void exitEditServiceParameter(ClistParser.EditServiceParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#ftinclService}.
	 * @param ctx the parse tree
	 */
	void enterFtinclService(ClistParser.FtinclServiceContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#ftinclService}.
	 * @param ctx the parse tree
	 */
	void exitFtinclService(ClistParser.FtinclServiceContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#skel_name}.
	 * @param ctx the parse tree
	 */
	void enterSkel_name(ClistParser.Skel_nameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#skel_name}.
	 * @param ctx the parse tree
	 */
	void exitSkel_name(ClistParser.Skel_nameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#ftinclParameter}.
	 * @param ctx the parse tree
	 */
	void enterFtinclParameter(ClistParser.FtinclParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#ftinclParameter}.
	 * @param ctx the parse tree
	 */
	void exitFtinclParameter(ClistParser.FtinclParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#ftCloseService}.
	 * @param ctx the parse tree
	 */
	void enterFtCloseService(ClistParser.FtCloseServiceContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#ftCloseService}.
	 * @param ctx the parse tree
	 */
	void exitFtCloseService(ClistParser.FtCloseServiceContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#ftCloseName}.
	 * @param ctx the parse tree
	 */
	void enterFtCloseName(ClistParser.FtCloseNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#ftCloseName}.
	 * @param ctx the parse tree
	 */
	void exitFtCloseName(ClistParser.FtCloseNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#ftCloseLibrary}.
	 * @param ctx the parse tree
	 */
	void enterFtCloseLibrary(ClistParser.FtCloseLibraryContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#ftCloseLibrary}.
	 * @param ctx the parse tree
	 */
	void exitFtCloseLibrary(ClistParser.FtCloseLibraryContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#ftCloseParameter}.
	 * @param ctx the parse tree
	 */
	void enterFtCloseParameter(ClistParser.FtCloseParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#ftCloseParameter}.
	 * @param ctx the parse tree
	 */
	void exitFtCloseParameter(ClistParser.FtCloseParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#ftopenService}.
	 * @param ctx the parse tree
	 */
	void enterFtopenService(ClistParser.FtopenServiceContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#ftopenService}.
	 * @param ctx the parse tree
	 */
	void exitFtopenService(ClistParser.FtopenServiceContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#ftopenServiceParameter}.
	 * @param ctx the parse tree
	 */
	void enterFtopenServiceParameter(ClistParser.FtopenServiceParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#ftopenServiceParameter}.
	 * @param ctx the parse tree
	 */
	void exitFtopenServiceParameter(ClistParser.FtopenServiceParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#vgetService}.
	 * @param ctx the parse tree
	 */
	void enterVgetService(ClistParser.VgetServiceContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#vgetService}.
	 * @param ctx the parse tree
	 */
	void exitVgetService(ClistParser.VgetServiceContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#vputService}.
	 * @param ctx the parse tree
	 */
	void enterVputService(ClistParser.VputServiceContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#vputService}.
	 * @param ctx the parse tree
	 */
	void exitVputService(ClistParser.VputServiceContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#name_list}.
	 * @param ctx the parse tree
	 */
	void enterName_list(ClistParser.Name_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#name_list}.
	 * @param ctx the parse tree
	 */
	void exitName_list(ClistParser.Name_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#name_list_item}.
	 * @param ctx the parse tree
	 */
	void enterName_list_item(ClistParser.Name_list_itemContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#name_list_item}.
	 * @param ctx the parse tree
	 */
	void exitName_list_item(ClistParser.Name_list_itemContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#vgetParameter}.
	 * @param ctx the parse tree
	 */
	void enterVgetParameter(ClistParser.VgetParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#vgetParameter}.
	 * @param ctx the parse tree
	 */
	void exitVgetParameter(ClistParser.VgetParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#vputParameter}.
	 * @param ctx the parse tree
	 */
	void enterVputParameter(ClistParser.VputParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#vputParameter}.
	 * @param ctx the parse tree
	 */
	void exitVputParameter(ClistParser.VputParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#value}.
	 * @param ctx the parse tree
	 */
	void enterValue(ClistParser.ValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#value}.
	 * @param ctx the parse tree
	 */
	void exitValue(ClistParser.ValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#stringExpression}.
	 * @param ctx the parse tree
	 */
	void enterStringExpression(ClistParser.StringExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#stringExpression}.
	 * @param ctx the parse tree
	 */
	void exitStringExpression(ClistParser.StringExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#calcExpression}.
	 * @param ctx the parse tree
	 */
	void enterCalcExpression(ClistParser.CalcExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#calcExpression}.
	 * @param ctx the parse tree
	 */
	void exitCalcExpression(ClistParser.CalcExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ToTerm}
	 * labeled alternative in {@link ClistParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterToTerm(ClistParser.ToTermContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ToTerm}
	 * labeled alternative in {@link ClistParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitToTerm(ClistParser.ToTermContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AddSubExpr}
	 * labeled alternative in {@link ClistParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterAddSubExpr(ClistParser.AddSubExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AddSubExpr}
	 * labeled alternative in {@link ClistParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitAddSubExpr(ClistParser.AddSubExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MulDivExpr}
	 * labeled alternative in {@link ClistParser#term}.
	 * @param ctx the parse tree
	 */
	void enterMulDivExpr(ClistParser.MulDivExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MulDivExpr}
	 * labeled alternative in {@link ClistParser#term}.
	 * @param ctx the parse tree
	 */
	void exitMulDivExpr(ClistParser.MulDivExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ToFactor}
	 * labeled alternative in {@link ClistParser#term}.
	 * @param ctx the parse tree
	 */
	void enterToFactor(ClistParser.ToFactorContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ToFactor}
	 * labeled alternative in {@link ClistParser#term}.
	 * @param ctx the parse tree
	 */
	void exitToFactor(ClistParser.ToFactorContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ParenExpr}
	 * labeled alternative in {@link ClistParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterParenExpr(ClistParser.ParenExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ParenExpr}
	 * labeled alternative in {@link ClistParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitParenExpr(ClistParser.ParenExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code NumberExpr}
	 * labeled alternative in {@link ClistParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterNumberExpr(ClistParser.NumberExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code NumberExpr}
	 * labeled alternative in {@link ClistParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitNumberExpr(ClistParser.NumberExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#closefileStatement}.
	 * @param ctx the parse tree
	 */
	void enterClosefileStatement(ClistParser.ClosefileStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#closefileStatement}.
	 * @param ctx the parse tree
	 */
	void exitClosefileStatement(ClistParser.ClosefileStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#getfileStatement}.
	 * @param ctx the parse tree
	 */
	void enterGetfileStatement(ClistParser.GetfileStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#getfileStatement}.
	 * @param ctx the parse tree
	 */
	void exitGetfileStatement(ClistParser.GetfileStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#openfileStatement}.
	 * @param ctx the parse tree
	 */
	void enterOpenfileStatement(ClistParser.OpenfileStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#openfileStatement}.
	 * @param ctx the parse tree
	 */
	void exitOpenfileStatement(ClistParser.OpenfileStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#openfileOption}.
	 * @param ctx the parse tree
	 */
	void enterOpenfileOption(ClistParser.OpenfileOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#openfileOption}.
	 * @param ctx the parse tree
	 */
	void exitOpenfileOption(ClistParser.OpenfileOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#callStatement}.
	 * @param ctx the parse tree
	 */
	void enterCallStatement(ClistParser.CallStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#callStatement}.
	 * @param ctx the parse tree
	 */
	void exitCallStatement(ClistParser.CallStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#member_name}.
	 * @param ctx the parse tree
	 */
	void enterMember_name(ClistParser.Member_nameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#member_name}.
	 * @param ctx the parse tree
	 */
	void exitMember_name(ClistParser.Member_nameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#callOption}.
	 * @param ctx the parse tree
	 */
	void enterCallOption(ClistParser.CallOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#callOption}.
	 * @param ctx the parse tree
	 */
	void exitCallOption(ClistParser.CallOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#dsnEndStatement}.
	 * @param ctx the parse tree
	 */
	void enterDsnEndStatement(ClistParser.DsnEndStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#dsnEndStatement}.
	 * @param ctx the parse tree
	 */
	void exitDsnEndStatement(ClistParser.DsnEndStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#runStatement}.
	 * @param ctx the parse tree
	 */
	void enterRunStatement(ClistParser.RunStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#runStatement}.
	 * @param ctx the parse tree
	 */
	void exitRunStatement(ClistParser.RunStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#allocStatement}.
	 * @param ctx the parse tree
	 */
	void enterAllocStatement(ClistParser.AllocStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#allocStatement}.
	 * @param ctx the parse tree
	 */
	void exitAllocStatement(ClistParser.AllocStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#allocParameter}.
	 * @param ctx the parse tree
	 */
	void enterAllocParameter(ClistParser.AllocParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#allocParameter}.
	 * @param ctx the parse tree
	 */
	void exitAllocParameter(ClistParser.AllocParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#otherAllocParameter}.
	 * @param ctx the parse tree
	 */
	void enterOtherAllocParameter(ClistParser.OtherAllocParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#otherAllocParameter}.
	 * @param ctx the parse tree
	 */
	void exitOtherAllocParameter(ClistParser.OtherAllocParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#allocParameterName}.
	 * @param ctx the parse tree
	 */
	void enterAllocParameterName(ClistParser.AllocParameterNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#allocParameterName}.
	 * @param ctx the parse tree
	 */
	void exitAllocParameterName(ClistParser.AllocParameterNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#allocParameterParams}.
	 * @param ctx the parse tree
	 */
	void enterAllocParameterParams(ClistParser.AllocParameterParamsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#allocParameterParams}.
	 * @param ctx the parse tree
	 */
	void exitAllocParameterParams(ClistParser.AllocParameterParamsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#allocParameterParam}.
	 * @param ctx the parse tree
	 */
	void enterAllocParameterParam(ClistParser.AllocParameterParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#allocParameterParam}.
	 * @param ctx the parse tree
	 */
	void exitAllocParameterParam(ClistParser.AllocParameterParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#freeFileStatement}.
	 * @param ctx the parse tree
	 */
	void enterFreeFileStatement(ClistParser.FreeFileStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#freeFileStatement}.
	 * @param ctx the parse tree
	 */
	void exitFreeFileStatement(ClistParser.FreeFileStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#clist_attribute_list_presentation}.
	 * @param ctx the parse tree
	 */
	void enterClist_attribute_list_presentation(ClistParser.Clist_attribute_list_presentationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#clist_attribute_list_presentation}.
	 * @param ctx the parse tree
	 */
	void exitClist_attribute_list_presentation(ClistParser.Clist_attribute_list_presentationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#clist_attribute_presentation}.
	 * @param ctx the parse tree
	 */
	void enterClist_attribute_presentation(ClistParser.Clist_attribute_presentationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#clist_attribute_presentation}.
	 * @param ctx the parse tree
	 */
	void exitClist_attribute_presentation(ClistParser.Clist_attribute_presentationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#attribute_name}.
	 * @param ctx the parse tree
	 */
	void enterAttribute_name(ClistParser.Attribute_nameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#attribute_name}.
	 * @param ctx the parse tree
	 */
	void exitAttribute_name(ClistParser.Attribute_nameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#clist_file_presentation}.
	 * @param ctx the parse tree
	 */
	void enterClist_file_presentation(ClistParser.Clist_file_presentationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#clist_file_presentation}.
	 * @param ctx the parse tree
	 */
	void exitClist_file_presentation(ClistParser.Clist_file_presentationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#clist_dataset_presentation}.
	 * @param ctx the parse tree
	 */
	void enterClist_dataset_presentation(ClistParser.Clist_dataset_presentationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#clist_dataset_presentation}.
	 * @param ctx the parse tree
	 */
	void exitClist_dataset_presentation(ClistParser.Clist_dataset_presentationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#clist_program_presentation}.
	 * @param ctx the parse tree
	 */
	void enterClist_program_presentation(ClistParser.Clist_program_presentationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#clist_program_presentation}.
	 * @param ctx the parse tree
	 */
	void exitClist_program_presentation(ClistParser.Clist_program_presentationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#clist_plan_presentation}.
	 * @param ctx the parse tree
	 */
	void enterClist_plan_presentation(ClistParser.Clist_plan_presentationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#clist_plan_presentation}.
	 * @param ctx the parse tree
	 */
	void exitClist_plan_presentation(ClistParser.Clist_plan_presentationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#clist_library_presentation}.
	 * @param ctx the parse tree
	 */
	void enterClist_library_presentation(ClistParser.Clist_library_presentationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#clist_library_presentation}.
	 * @param ctx the parse tree
	 */
	void exitClist_library_presentation(ClistParser.Clist_library_presentationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#clist_params_presentation}.
	 * @param ctx the parse tree
	 */
	void enterClist_params_presentation(ClistParser.Clist_params_presentationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#clist_params_presentation}.
	 * @param ctx the parse tree
	 */
	void exitClist_params_presentation(ClistParser.Clist_params_presentationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#clist_system_presentation}.
	 * @param ctx the parse tree
	 */
	void enterClist_system_presentation(ClistParser.Clist_system_presentationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#clist_system_presentation}.
	 * @param ctx the parse tree
	 */
	void exitClist_system_presentation(ClistParser.Clist_system_presentationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#clist_data_id_presentation}.
	 * @param ctx the parse tree
	 */
	void enterClist_data_id_presentation(ClistParser.Clist_data_id_presentationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#clist_data_id_presentation}.
	 * @param ctx the parse tree
	 */
	void exitClist_data_id_presentation(ClistParser.Clist_data_id_presentationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#data_id}.
	 * @param ctx the parse tree
	 */
	void enterData_id(ClistParser.Data_idContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#data_id}.
	 * @param ctx the parse tree
	 */
	void exitData_id(ClistParser.Data_idContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#system_name}.
	 * @param ctx the parse tree
	 */
	void enterSystem_name(ClistParser.System_nameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#system_name}.
	 * @param ctx the parse tree
	 */
	void exitSystem_name(ClistParser.System_nameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#plan_name}.
	 * @param ctx the parse tree
	 */
	void enterPlan_name(ClistParser.Plan_nameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#plan_name}.
	 * @param ctx the parse tree
	 */
	void exitPlan_name(ClistParser.Plan_nameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#program_name}.
	 * @param ctx the parse tree
	 */
	void enterProgram_name(ClistParser.Program_nameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#program_name}.
	 * @param ctx the parse tree
	 */
	void exitProgram_name(ClistParser.Program_nameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#library_name}.
	 * @param ctx the parse tree
	 */
	void enterLibrary_name(ClistParser.Library_nameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#library_name}.
	 * @param ctx the parse tree
	 */
	void exitLibrary_name(ClistParser.Library_nameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#params_name}.
	 * @param ctx the parse tree
	 */
	void enterParams_name(ClistParser.Params_nameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#params_name}.
	 * @param ctx the parse tree
	 */
	void exitParams_name(ClistParser.Params_nameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#fileName}.
	 * @param ctx the parse tree
	 */
	void enterFileName(ClistParser.FileNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#fileName}.
	 * @param ctx the parse tree
	 */
	void exitFileName(ClistParser.FileNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#generalStatementParemeter}.
	 * @param ctx the parse tree
	 */
	void enterGeneralStatementParemeter(ClistParser.GeneralStatementParemeterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#generalStatementParemeter}.
	 * @param ctx the parse tree
	 */
	void exitGeneralStatementParemeter(ClistParser.GeneralStatementParemeterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#gotoStatement}.
	 * @param ctx the parse tree
	 */
	void enterGotoStatement(ClistParser.GotoStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#gotoStatement}.
	 * @param ctx the parse tree
	 */
	void exitGotoStatement(ClistParser.GotoStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(ClistParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(ClistParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#endIf}.
	 * @param ctx the parse tree
	 */
	void enterEndIf(ClistParser.EndIfContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#endIf}.
	 * @param ctx the parse tree
	 */
	void exitEndIf(ClistParser.EndIfContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#thenIf}.
	 * @param ctx the parse tree
	 */
	void enterThenIf(ClistParser.ThenIfContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#thenIf}.
	 * @param ctx the parse tree
	 */
	void exitThenIf(ClistParser.ThenIfContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#elseIf}.
	 * @param ctx the parse tree
	 */
	void enterElseIf(ClistParser.ElseIfContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#elseIf}.
	 * @param ctx the parse tree
	 */
	void exitElseIf(ClistParser.ElseIfContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#clistKeyword}.
	 * @param ctx the parse tree
	 */
	void enterClistKeyword(ClistParser.ClistKeywordContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#clistKeyword}.
	 * @param ctx the parse tree
	 */
	void exitClistKeyword(ClistParser.ClistKeywordContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#charDataKeyword}.
	 * @param ctx the parse tree
	 */
	void enterCharDataKeyword(ClistParser.CharDataKeywordContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#charDataKeyword}.
	 * @param ctx the parse tree
	 */
	void exitCharDataKeyword(ClistParser.CharDataKeywordContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(ClistParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(ClistParser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#andOrCondition}.
	 * @param ctx the parse tree
	 */
	void enterAndOrCondition(ClistParser.AndOrConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#andOrCondition}.
	 * @param ctx the parse tree
	 */
	void exitAndOrCondition(ClistParser.AndOrConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#combinableCondition}.
	 * @param ctx the parse tree
	 */
	void enterCombinableCondition(ClistParser.CombinableConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#combinableCondition}.
	 * @param ctx the parse tree
	 */
	void exitCombinableCondition(ClistParser.CombinableConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#simpleCondition}.
	 * @param ctx the parse tree
	 */
	void enterSimpleCondition(ClistParser.SimpleConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#simpleCondition}.
	 * @param ctx the parse tree
	 */
	void exitSimpleCondition(ClistParser.SimpleConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#relationCondition}.
	 * @param ctx the parse tree
	 */
	void enterRelationCondition(ClistParser.RelationConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#relationCondition}.
	 * @param ctx the parse tree
	 */
	void exitRelationCondition(ClistParser.RelationConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#relationArithmeticComparison}.
	 * @param ctx the parse tree
	 */
	void enterRelationArithmeticComparison(ClistParser.RelationArithmeticComparisonContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#relationArithmeticComparison}.
	 * @param ctx the parse tree
	 */
	void exitRelationArithmeticComparison(ClistParser.RelationArithmeticComparisonContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#arithmeticExpression}.
	 * @param ctx the parse tree
	 */
	void enterArithmeticExpression(ClistParser.ArithmeticExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#arithmeticExpression}.
	 * @param ctx the parse tree
	 */
	void exitArithmeticExpression(ClistParser.ArithmeticExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#relationalOperator}.
	 * @param ctx the parse tree
	 */
	void enterRelationalOperator(ClistParser.RelationalOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#relationalOperator}.
	 * @param ctx the parse tree
	 */
	void exitRelationalOperator(ClistParser.RelationalOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#insertStatement}.
	 * @param ctx the parse tree
	 */
	void enterInsertStatement(ClistParser.InsertStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#insertStatement}.
	 * @param ctx the parse tree
	 */
	void exitInsertStatement(ClistParser.InsertStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#exitStatement}.
	 * @param ctx the parse tree
	 */
	void enterExitStatement(ClistParser.ExitStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#exitStatement}.
	 * @param ctx the parse tree
	 */
	void exitExitStatement(ClistParser.ExitStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#exitParameters}.
	 * @param ctx the parse tree
	 */
	void enterExitParameters(ClistParser.ExitParametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#exitParameters}.
	 * @param ctx the parse tree
	 */
	void exitExitParameters(ClistParser.ExitParametersContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#submitStatement}.
	 * @param ctx the parse tree
	 */
	void enterSubmitStatement(ClistParser.SubmitStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#submitStatement}.
	 * @param ctx the parse tree
	 */
	void exitSubmitStatement(ClistParser.SubmitStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#jcl_code_submited}.
	 * @param ctx the parse tree
	 */
	void enterJcl_code_submited(ClistParser.Jcl_code_submitedContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#jcl_code_submited}.
	 * @param ctx the parse tree
	 */
	void exitJcl_code_submited(ClistParser.Jcl_code_submitedContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#jcl_code}.
	 * @param ctx the parse tree
	 */
	void enterJcl_code(ClistParser.Jcl_codeContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#jcl_code}.
	 * @param ctx the parse tree
	 */
	void exitJcl_code(ClistParser.Jcl_codeContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#jcl_code_start_and_end_symbol}.
	 * @param ctx the parse tree
	 */
	void enterJcl_code_start_and_end_symbol(ClistParser.Jcl_code_start_and_end_symbolContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#jcl_code_start_and_end_symbol}.
	 * @param ctx the parse tree
	 */
	void exitJcl_code_start_and_end_symbol(ClistParser.Jcl_code_start_and_end_symbolContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#inlineStatement}.
	 * @param ctx the parse tree
	 */
	void enterInlineStatement(ClistParser.InlineStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#inlineStatement}.
	 * @param ctx the parse tree
	 */
	void exitInlineStatement(ClistParser.InlineStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#changeStatement}.
	 * @param ctx the parse tree
	 */
	void enterChangeStatement(ClistParser.ChangeStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#changeStatement}.
	 * @param ctx the parse tree
	 */
	void exitChangeStatement(ClistParser.ChangeStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#changeParameter}.
	 * @param ctx the parse tree
	 */
	void enterChangeParameter(ClistParser.ChangeParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#changeParameter}.
	 * @param ctx the parse tree
	 */
	void exitChangeParameter(ClistParser.ChangeParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#changeString}.
	 * @param ctx the parse tree
	 */
	void enterChangeString(ClistParser.ChangeStringContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#changeString}.
	 * @param ctx the parse tree
	 */
	void exitChangeString(ClistParser.ChangeStringContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#orignalString}.
	 * @param ctx the parse tree
	 */
	void enterOrignalString(ClistParser.OrignalStringContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#orignalString}.
	 * @param ctx the parse tree
	 */
	void exitOrignalString(ClistParser.OrignalStringContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#findStatement}.
	 * @param ctx the parse tree
	 */
	void enterFindStatement(ClistParser.FindStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#findStatement}.
	 * @param ctx the parse tree
	 */
	void exitFindStatement(ClistParser.FindStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#findString}.
	 * @param ctx the parse tree
	 */
	void enterFindString(ClistParser.FindStringContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#findString}.
	 * @param ctx the parse tree
	 */
	void exitFindString(ClistParser.FindStringContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#editStatement}.
	 * @param ctx the parse tree
	 */
	void enterEditStatement(ClistParser.EditStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#editStatement}.
	 * @param ctx the parse tree
	 */
	void exitEditStatement(ClistParser.EditStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#editOption}.
	 * @param ctx the parse tree
	 */
	void enterEditOption(ClistParser.EditOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#editOption}.
	 * @param ctx the parse tree
	 */
	void exitEditOption(ClistParser.EditOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#smCopyStatement}.
	 * @param ctx the parse tree
	 */
	void enterSmCopyStatement(ClistParser.SmCopyStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#smCopyStatement}.
	 * @param ctx the parse tree
	 */
	void exitSmCopyStatement(ClistParser.SmCopyStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#smCopyFrom}.
	 * @param ctx the parse tree
	 */
	void enterSmCopyFrom(ClistParser.SmCopyFromContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#smCopyFrom}.
	 * @param ctx the parse tree
	 */
	void exitSmCopyFrom(ClistParser.SmCopyFromContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#fromDataset}.
	 * @param ctx the parse tree
	 */
	void enterFromDataset(ClistParser.FromDatasetContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#fromDataset}.
	 * @param ctx the parse tree
	 */
	void exitFromDataset(ClistParser.FromDatasetContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#smCopyTo}.
	 * @param ctx the parse tree
	 */
	void enterSmCopyTo(ClistParser.SmCopyToContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#smCopyTo}.
	 * @param ctx the parse tree
	 */
	void exitSmCopyTo(ClistParser.SmCopyToContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#toDataset}.
	 * @param ctx the parse tree
	 */
	void enterToDataset(ClistParser.ToDatasetContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#toDataset}.
	 * @param ctx the parse tree
	 */
	void exitToDataset(ClistParser.ToDatasetContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#smCopyOption}.
	 * @param ctx the parse tree
	 */
	void enterSmCopyOption(ClistParser.SmCopyOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#smCopyOption}.
	 * @param ctx the parse tree
	 */
	void exitSmCopyOption(ClistParser.SmCopyOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#readStatement}.
	 * @param ctx the parse tree
	 */
	void enterReadStatement(ClistParser.ReadStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#readStatement}.
	 * @param ctx the parse tree
	 */
	void exitReadStatement(ClistParser.ReadStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#variable}.
	 * @param ctx the parse tree
	 */
	void enterVariable(ClistParser.VariableContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#variable}.
	 * @param ctx the parse tree
	 */
	void exitVariable(ClistParser.VariableContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#normalVariableCombineWithReferenced}.
	 * @param ctx the parse tree
	 */
	void enterNormalVariableCombineWithReferenced(ClistParser.NormalVariableCombineWithReferencedContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#normalVariableCombineWithReferenced}.
	 * @param ctx the parse tree
	 */
	void exitNormalVariableCombineWithReferenced(ClistParser.NormalVariableCombineWithReferencedContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#referencedVariable}.
	 * @param ctx the parse tree
	 */
	void enterReferencedVariable(ClistParser.ReferencedVariableContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#referencedVariable}.
	 * @param ctx the parse tree
	 */
	void exitReferencedVariable(ClistParser.ReferencedVariableContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#writeNrStatement}.
	 * @param ctx the parse tree
	 */
	void enterWriteNrStatement(ClistParser.WriteNrStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#writeNrStatement}.
	 * @param ctx the parse tree
	 */
	void exitWriteNrStatement(ClistParser.WriteNrStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#writeStatement}.
	 * @param ctx the parse tree
	 */
	void enterWriteStatement(ClistParser.WriteStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#writeStatement}.
	 * @param ctx the parse tree
	 */
	void exitWriteStatement(ClistParser.WriteStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#attnStatement}.
	 * @param ctx the parse tree
	 */
	void enterAttnStatement(ClistParser.AttnStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#attnStatement}.
	 * @param ctx the parse tree
	 */
	void exitAttnStatement(ClistParser.AttnStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#controlStatement}.
	 * @param ctx the parse tree
	 */
	void enterControlStatement(ClistParser.ControlStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#controlStatement}.
	 * @param ctx the parse tree
	 */
	void exitControlStatement(ClistParser.ControlStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#controlOption}.
	 * @param ctx the parse tree
	 */
	void enterControlOption(ClistParser.ControlOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#controlOption}.
	 * @param ctx the parse tree
	 */
	void exitControlOption(ClistParser.ControlOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#doEndStatement}.
	 * @param ctx the parse tree
	 */
	void enterDoEndStatement(ClistParser.DoEndStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#doEndStatement}.
	 * @param ctx the parse tree
	 */
	void exitDoEndStatement(ClistParser.DoEndStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#clist_file_name}.
	 * @param ctx the parse tree
	 */
	void enterClist_file_name(ClistParser.Clist_file_nameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#clist_file_name}.
	 * @param ctx the parse tree
	 */
	void exitClist_file_name(ClistParser.Clist_file_nameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#buildInFuntion}.
	 * @param ctx the parse tree
	 */
	void enterBuildInFuntion(ClistParser.BuildInFuntionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#buildInFuntion}.
	 * @param ctx the parse tree
	 */
	void exitBuildInFuntion(ClistParser.BuildInFuntionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#otherBuildInFunction}.
	 * @param ctx the parse tree
	 */
	void enterOtherBuildInFunction(ClistParser.OtherBuildInFunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#otherBuildInFunction}.
	 * @param ctx the parse tree
	 */
	void exitOtherBuildInFunction(ClistParser.OtherBuildInFunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#function_name}.
	 * @param ctx the parse tree
	 */
	void enterFunction_name(ClistParser.Function_nameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#function_name}.
	 * @param ctx the parse tree
	 */
	void exitFunction_name(ClistParser.Function_nameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#function_parameter}.
	 * @param ctx the parse tree
	 */
	void enterFunction_parameter(ClistParser.Function_parameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#function_parameter}.
	 * @param ctx the parse tree
	 */
	void exitFunction_parameter(ClistParser.Function_parameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#lengthFunction}.
	 * @param ctx the parse tree
	 */
	void enterLengthFunction(ClistParser.LengthFunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#lengthFunction}.
	 * @param ctx the parse tree
	 */
	void exitLengthFunction(ClistParser.LengthFunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#subStringFunction}.
	 * @param ctx the parse tree
	 */
	void enterSubStringFunction(ClistParser.SubStringFunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#subStringFunction}.
	 * @param ctx the parse tree
	 */
	void exitSubStringFunction(ClistParser.SubStringFunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#partToSubString}.
	 * @param ctx the parse tree
	 */
	void enterPartToSubString(ClistParser.PartToSubStringContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#partToSubString}.
	 * @param ctx the parse tree
	 */
	void exitPartToSubString(ClistParser.PartToSubStringContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#startIndex}.
	 * @param ctx the parse tree
	 */
	void enterStartIndex(ClistParser.StartIndexContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#startIndex}.
	 * @param ctx the parse tree
	 */
	void exitStartIndex(ClistParser.StartIndexContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#endIndex}.
	 * @param ctx the parse tree
	 */
	void enterEndIndex(ClistParser.EndIndexContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#endIndex}.
	 * @param ctx the parse tree
	 */
	void exitEndIndex(ClistParser.EndIndexContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#intergerLiteral}.
	 * @param ctx the parse tree
	 */
	void enterIntergerLiteral(ClistParser.IntergerLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#intergerLiteral}.
	 * @param ctx the parse tree
	 */
	void exitIntergerLiteral(ClistParser.IntergerLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#stringToSubString}.
	 * @param ctx the parse tree
	 */
	void enterStringToSubString(ClistParser.StringToSubStringContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#stringToSubString}.
	 * @param ctx the parse tree
	 */
	void exitStringToSubString(ClistParser.StringToSubStringContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#stringFuntion}.
	 * @param ctx the parse tree
	 */
	void enterStringFuntion(ClistParser.StringFuntionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#stringFuntion}.
	 * @param ctx the parse tree
	 */
	void exitStringFuntion(ClistParser.StringFuntionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#dataset_name}.
	 * @param ctx the parse tree
	 */
	void enterDataset_name(ClistParser.Dataset_nameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#dataset_name}.
	 * @param ctx the parse tree
	 */
	void exitDataset_name(ClistParser.Dataset_nameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#dataset_part}.
	 * @param ctx the parse tree
	 */
	void enterDataset_part(ClistParser.Dataset_partContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#dataset_part}.
	 * @param ctx the parse tree
	 */
	void exitDataset_part(ClistParser.Dataset_partContext ctx);
	/**
	 * Enter a parse tree produced by {@link ClistParser#signed_number}.
	 * @param ctx the parse tree
	 */
	void enterSigned_number(ClistParser.Signed_numberContext ctx);
	/**
	 * Exit a parse tree produced by {@link ClistParser#signed_number}.
	 * @param ctx the parse tree
	 */
	void exitSigned_number(ClistParser.Signed_numberContext ctx);
}