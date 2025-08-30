// Generated from /home/minhnl11aic/Documents/mainframe-workers/src/parsers/grammar/panel/Panel.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link PanelParser}.
 */
public interface PanelListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link PanelParser#startRule}.
	 * @param ctx the parse tree
	 */
	void enterStartRule(PanelParser.StartRuleContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#startRule}.
	 * @param ctx the parse tree
	 */
	void exitStartRule(PanelParser.StartRuleContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#section}.
	 * @param ctx the parse tree
	 */
	void enterSection(PanelParser.SectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#section}.
	 * @param ctx the parse tree
	 */
	void exitSection(PanelParser.SectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#reinitSection}.
	 * @param ctx the parse tree
	 */
	void enterReinitSection(PanelParser.ReinitSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#reinitSection}.
	 * @param ctx the parse tree
	 */
	void exitReinitSection(PanelParser.ReinitSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#modelSection}.
	 * @param ctx the parse tree
	 */
	void enterModelSection(PanelParser.ModelSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#modelSection}.
	 * @param ctx the parse tree
	 */
	void exitModelSection(PanelParser.ModelSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#modelParam}.
	 * @param ctx the parse tree
	 */
	void enterModelParam(PanelParser.ModelParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#modelParam}.
	 * @param ctx the parse tree
	 */
	void exitModelParam(PanelParser.ModelParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#model}.
	 * @param ctx the parse tree
	 */
	void enterModel(PanelParser.ModelContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#model}.
	 * @param ctx the parse tree
	 */
	void exitModel(PanelParser.ModelContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#attributeSection}.
	 * @param ctx the parse tree
	 */
	void enterAttributeSection(PanelParser.AttributeSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#attributeSection}.
	 * @param ctx the parse tree
	 */
	void exitAttributeSection(PanelParser.AttributeSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#attributeComponent}.
	 * @param ctx the parse tree
	 */
	void enterAttributeComponent(PanelParser.AttributeComponentContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#attributeComponent}.
	 * @param ctx the parse tree
	 */
	void exitAttributeComponent(PanelParser.AttributeComponentContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#attrParameter}.
	 * @param ctx the parse tree
	 */
	void enterAttrParameter(PanelParser.AttrParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#attrParameter}.
	 * @param ctx the parse tree
	 */
	void exitAttrParameter(PanelParser.AttrParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#outlineParam}.
	 * @param ctx the parse tree
	 */
	void enterOutlineParam(PanelParser.OutlineParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#outlineParam}.
	 * @param ctx the parse tree
	 */
	void exitOutlineParam(PanelParser.OutlineParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#outlineValue}.
	 * @param ctx the parse tree
	 */
	void enterOutlineValue(PanelParser.OutlineValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#outlineValue}.
	 * @param ctx the parse tree
	 */
	void exitOutlineValue(PanelParser.OutlineValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#padcParam}.
	 * @param ctx the parse tree
	 */
	void enterPadcParam(PanelParser.PadcParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#padcParam}.
	 * @param ctx the parse tree
	 */
	void exitPadcParam(PanelParser.PadcParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#padcValue}.
	 * @param ctx the parse tree
	 */
	void enterPadcValue(PanelParser.PadcValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#padcValue}.
	 * @param ctx the parse tree
	 */
	void exitPadcValue(PanelParser.PadcValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#justParam}.
	 * @param ctx the parse tree
	 */
	void enterJustParam(PanelParser.JustParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#justParam}.
	 * @param ctx the parse tree
	 */
	void exitJustParam(PanelParser.JustParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#justValue}.
	 * @param ctx the parse tree
	 */
	void enterJustValue(PanelParser.JustValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#justValue}.
	 * @param ctx the parse tree
	 */
	void exitJustValue(PanelParser.JustValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#areaParam}.
	 * @param ctx the parse tree
	 */
	void enterAreaParam(PanelParser.AreaParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#areaParam}.
	 * @param ctx the parse tree
	 */
	void exitAreaParam(PanelParser.AreaParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#areaValue}.
	 * @param ctx the parse tree
	 */
	void enterAreaValue(PanelParser.AreaValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#areaValue}.
	 * @param ctx the parse tree
	 */
	void exitAreaValue(PanelParser.AreaValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#scrollParam}.
	 * @param ctx the parse tree
	 */
	void enterScrollParam(PanelParser.ScrollParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#scrollParam}.
	 * @param ctx the parse tree
	 */
	void exitScrollParam(PanelParser.ScrollParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#scrollValue}.
	 * @param ctx the parse tree
	 */
	void enterScrollValue(PanelParser.ScrollValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#scrollValue}.
	 * @param ctx the parse tree
	 */
	void exitScrollValue(PanelParser.ScrollValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#extendParam}.
	 * @param ctx the parse tree
	 */
	void enterExtendParam(PanelParser.ExtendParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#extendParam}.
	 * @param ctx the parse tree
	 */
	void exitExtendParam(PanelParser.ExtendParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#extendValue}.
	 * @param ctx the parse tree
	 */
	void enterExtendValue(PanelParser.ExtendValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#extendValue}.
	 * @param ctx the parse tree
	 */
	void exitExtendValue(PanelParser.ExtendValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#capsParam}.
	 * @param ctx the parse tree
	 */
	void enterCapsParam(PanelParser.CapsParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#capsParam}.
	 * @param ctx the parse tree
	 */
	void exitCapsParam(PanelParser.CapsParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#capsValue}.
	 * @param ctx the parse tree
	 */
	void enterCapsValue(PanelParser.CapsValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#capsValue}.
	 * @param ctx the parse tree
	 */
	void exitCapsValue(PanelParser.CapsValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#padParam}.
	 * @param ctx the parse tree
	 */
	void enterPadParam(PanelParser.PadParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#padParam}.
	 * @param ctx the parse tree
	 */
	void exitPadParam(PanelParser.PadParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#padValue}.
	 * @param ctx the parse tree
	 */
	void enterPadValue(PanelParser.PadValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#padValue}.
	 * @param ctx the parse tree
	 */
	void exitPadValue(PanelParser.PadValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#skipParam}.
	 * @param ctx the parse tree
	 */
	void enterSkipParam(PanelParser.SkipParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#skipParam}.
	 * @param ctx the parse tree
	 */
	void exitSkipParam(PanelParser.SkipParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#skipValue}.
	 * @param ctx the parse tree
	 */
	void enterSkipValue(PanelParser.SkipValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#skipValue}.
	 * @param ctx the parse tree
	 */
	void exitSkipValue(PanelParser.SkipValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#typeParam}.
	 * @param ctx the parse tree
	 */
	void enterTypeParam(PanelParser.TypeParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#typeParam}.
	 * @param ctx the parse tree
	 */
	void exitTypeParam(PanelParser.TypeParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#intensParam}.
	 * @param ctx the parse tree
	 */
	void enterIntensParam(PanelParser.IntensParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#intensParam}.
	 * @param ctx the parse tree
	 */
	void exitIntensParam(PanelParser.IntensParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#intensValue}.
	 * @param ctx the parse tree
	 */
	void enterIntensValue(PanelParser.IntensValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#intensValue}.
	 * @param ctx the parse tree
	 */
	void exitIntensValue(PanelParser.IntensValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#colorParam}.
	 * @param ctx the parse tree
	 */
	void enterColorParam(PanelParser.ColorParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#colorParam}.
	 * @param ctx the parse tree
	 */
	void exitColorParam(PanelParser.ColorParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#hiliteParam}.
	 * @param ctx the parse tree
	 */
	void enterHiliteParam(PanelParser.HiliteParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#hiliteParam}.
	 * @param ctx the parse tree
	 */
	void exitHiliteParam(PanelParser.HiliteParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#attrChar}.
	 * @param ctx the parse tree
	 */
	void enterAttrChar(PanelParser.AttrCharContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#attrChar}.
	 * @param ctx the parse tree
	 */
	void exitAttrChar(PanelParser.AttrCharContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#bodySection}.
	 * @param ctx the parse tree
	 */
	void enterBodySection(PanelParser.BodySectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#bodySection}.
	 * @param ctx the parse tree
	 */
	void exitBodySection(PanelParser.BodySectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#bodyParam}.
	 * @param ctx the parse tree
	 */
	void enterBodyParam(PanelParser.BodyParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#bodyParam}.
	 * @param ctx the parse tree
	 */
	void exitBodyParam(PanelParser.BodyParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#kanaParam}.
	 * @param ctx the parse tree
	 */
	void enterKanaParam(PanelParser.KanaParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#kanaParam}.
	 * @param ctx the parse tree
	 */
	void exitKanaParam(PanelParser.KanaParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#windowParam}.
	 * @param ctx the parse tree
	 */
	void enterWindowParam(PanelParser.WindowParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#windowParam}.
	 * @param ctx the parse tree
	 */
	void exitWindowParam(PanelParser.WindowParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#width}.
	 * @param ctx the parse tree
	 */
	void enterWidth(PanelParser.WidthContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#width}.
	 * @param ctx the parse tree
	 */
	void exitWidth(PanelParser.WidthContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#length}.
	 * @param ctx the parse tree
	 */
	void enterLength(PanelParser.LengthContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#length}.
	 * @param ctx the parse tree
	 */
	void exitLength(PanelParser.LengthContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#widthPara}.
	 * @param ctx the parse tree
	 */
	void enterWidthPara(PanelParser.WidthParaContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#widthPara}.
	 * @param ctx the parse tree
	 */
	void exitWidthPara(PanelParser.WidthParaContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(PanelParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(PanelParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#refreshStatement}.
	 * @param ctx the parse tree
	 */
	void enterRefreshStatement(PanelParser.RefreshStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#refreshStatement}.
	 * @param ctx the parse tree
	 */
	void exitRefreshStatement(PanelParser.RefreshStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(PanelParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(PanelParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(PanelParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(PanelParser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#andOrCondition}.
	 * @param ctx the parse tree
	 */
	void enterAndOrCondition(PanelParser.AndOrConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#andOrCondition}.
	 * @param ctx the parse tree
	 */
	void exitAndOrCondition(PanelParser.AndOrConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#combinableCondition}.
	 * @param ctx the parse tree
	 */
	void enterCombinableCondition(PanelParser.CombinableConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#combinableCondition}.
	 * @param ctx the parse tree
	 */
	void exitCombinableCondition(PanelParser.CombinableConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#simpleCondition}.
	 * @param ctx the parse tree
	 */
	void enterSimpleCondition(PanelParser.SimpleConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#simpleCondition}.
	 * @param ctx the parse tree
	 */
	void exitSimpleCondition(PanelParser.SimpleConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#relationCondition}.
	 * @param ctx the parse tree
	 */
	void enterRelationCondition(PanelParser.RelationConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#relationCondition}.
	 * @param ctx the parse tree
	 */
	void exitRelationCondition(PanelParser.RelationConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#relationArithmeticComparison}.
	 * @param ctx the parse tree
	 */
	void enterRelationArithmeticComparison(PanelParser.RelationArithmeticComparisonContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#relationArithmeticComparison}.
	 * @param ctx the parse tree
	 */
	void exitRelationArithmeticComparison(PanelParser.RelationArithmeticComparisonContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#arithmeticExpression}.
	 * @param ctx the parse tree
	 */
	void enterArithmeticExpression(PanelParser.ArithmeticExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#arithmeticExpression}.
	 * @param ctx the parse tree
	 */
	void exitArithmeticExpression(PanelParser.ArithmeticExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#relationalOperator}.
	 * @param ctx the parse tree
	 */
	void enterRelationalOperator(PanelParser.RelationalOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#relationalOperator}.
	 * @param ctx the parse tree
	 */
	void exitRelationalOperator(PanelParser.RelationalOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#thenIf}.
	 * @param ctx the parse tree
	 */
	void enterThenIf(PanelParser.ThenIfContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#thenIf}.
	 * @param ctx the parse tree
	 */
	void exitThenIf(PanelParser.ThenIfContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#verStatement}.
	 * @param ctx the parse tree
	 */
	void enterVerStatement(PanelParser.VerStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#verStatement}.
	 * @param ctx the parse tree
	 */
	void exitVerStatement(PanelParser.VerStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#verMsg}.
	 * @param ctx the parse tree
	 */
	void enterVerMsg(PanelParser.VerMsgContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#verMsg}.
	 * @param ctx the parse tree
	 */
	void exitVerMsg(PanelParser.VerMsgContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#verCriteria}.
	 * @param ctx the parse tree
	 */
	void enterVerCriteria(PanelParser.VerCriteriaContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#verCriteria}.
	 * @param ctx the parse tree
	 */
	void exitVerCriteria(PanelParser.VerCriteriaContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#simpleCriteria}.
	 * @param ctx the parse tree
	 */
	void enterSimpleCriteria(PanelParser.SimpleCriteriaContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#simpleCriteria}.
	 * @param ctx the parse tree
	 */
	void exitSimpleCriteria(PanelParser.SimpleCriteriaContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#lengthCriteria}.
	 * @param ctx the parse tree
	 */
	void enterLengthCriteria(PanelParser.LengthCriteriaContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#lengthCriteria}.
	 * @param ctx the parse tree
	 */
	void exitLengthCriteria(PanelParser.LengthCriteriaContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#listCriteria}.
	 * @param ctx the parse tree
	 */
	void enterListCriteria(PanelParser.ListCriteriaContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#listCriteria}.
	 * @param ctx the parse tree
	 */
	void exitListCriteria(PanelParser.ListCriteriaContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#pictCriteria}.
	 * @param ctx the parse tree
	 */
	void enterPictCriteria(PanelParser.PictCriteriaContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#pictCriteria}.
	 * @param ctx the parse tree
	 */
	void exitPictCriteria(PanelParser.PictCriteriaContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#picValue}.
	 * @param ctx the parse tree
	 */
	void enterPicValue(PanelParser.PicValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#picValue}.
	 * @param ctx the parse tree
	 */
	void exitPicValue(PanelParser.PicValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#rangeCriteria}.
	 * @param ctx the parse tree
	 */
	void enterRangeCriteria(PanelParser.RangeCriteriaContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#rangeCriteria}.
	 * @param ctx the parse tree
	 */
	void exitRangeCriteria(PanelParser.RangeCriteriaContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#expectedLength}.
	 * @param ctx the parse tree
	 */
	void enterExpectedLength(PanelParser.ExpectedLengthContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#expectedLength}.
	 * @param ctx the parse tree
	 */
	void exitExpectedLength(PanelParser.ExpectedLengthContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#stringValue}.
	 * @param ctx the parse tree
	 */
	void enterStringValue(PanelParser.StringValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#stringValue}.
	 * @param ctx the parse tree
	 */
	void exitStringValue(PanelParser.StringValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#varlist}.
	 * @param ctx the parse tree
	 */
	void enterVarlist(PanelParser.VarlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#varlist}.
	 * @param ctx the parse tree
	 */
	void exitVarlist(PanelParser.VarlistContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#maskCharacter}.
	 * @param ctx the parse tree
	 */
	void enterMaskCharacter(PanelParser.MaskCharacterContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#maskCharacter}.
	 * @param ctx the parse tree
	 */
	void exitMaskCharacter(PanelParser.MaskCharacterContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#fieldMask}.
	 * @param ctx the parse tree
	 */
	void enterFieldMask(PanelParser.FieldMaskContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#fieldMask}.
	 * @param ctx the parse tree
	 */
	void exitFieldMask(PanelParser.FieldMaskContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#lower}.
	 * @param ctx the parse tree
	 */
	void enterLower(PanelParser.LowerContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#lower}.
	 * @param ctx the parse tree
	 */
	void exitLower(PanelParser.LowerContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#upper}.
	 * @param ctx the parse tree
	 */
	void enterUpper(PanelParser.UpperContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#upper}.
	 * @param ctx the parse tree
	 */
	void exitUpper(PanelParser.UpperContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#elseIf}.
	 * @param ctx the parse tree
	 */
	void enterElseIf(PanelParser.ElseIfContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#elseIf}.
	 * @param ctx the parse tree
	 */
	void exitElseIf(PanelParser.ElseIfContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#assignStatement}.
	 * @param ctx the parse tree
	 */
	void enterAssignStatement(PanelParser.AssignStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#assignStatement}.
	 * @param ctx the parse tree
	 */
	void exitAssignStatement(PanelParser.AssignStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#variable}.
	 * @param ctx the parse tree
	 */
	void enterVariable(PanelParser.VariableContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#variable}.
	 * @param ctx the parse tree
	 */
	void exitVariable(PanelParser.VariableContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#assignPart}.
	 * @param ctx the parse tree
	 */
	void enterAssignPart(PanelParser.AssignPartContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#assignPart}.
	 * @param ctx the parse tree
	 */
	void exitAssignPart(PanelParser.AssignPartContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#vgetStatement}.
	 * @param ctx the parse tree
	 */
	void enterVgetStatement(PanelParser.VgetStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#vgetStatement}.
	 * @param ctx the parse tree
	 */
	void exitVgetStatement(PanelParser.VgetStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#vputStatement}.
	 * @param ctx the parse tree
	 */
	void enterVputStatement(PanelParser.VputStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#vputStatement}.
	 * @param ctx the parse tree
	 */
	void exitVputStatement(PanelParser.VputStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#name_list}.
	 * @param ctx the parse tree
	 */
	void enterName_list(PanelParser.Name_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#name_list}.
	 * @param ctx the parse tree
	 */
	void exitName_list(PanelParser.Name_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#name_list_item}.
	 * @param ctx the parse tree
	 */
	void enterName_list_item(PanelParser.Name_list_itemContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#name_list_item}.
	 * @param ctx the parse tree
	 */
	void exitName_list_item(PanelParser.Name_list_itemContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#vgetParameter}.
	 * @param ctx the parse tree
	 */
	void enterVgetParameter(PanelParser.VgetParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#vgetParameter}.
	 * @param ctx the parse tree
	 */
	void exitVgetParameter(PanelParser.VgetParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#vputParameter}.
	 * @param ctx the parse tree
	 */
	void enterVputParameter(PanelParser.VputParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#vputParameter}.
	 * @param ctx the parse tree
	 */
	void exitVputParameter(PanelParser.VputParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#initSection}.
	 * @param ctx the parse tree
	 */
	void enterInitSection(PanelParser.InitSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#initSection}.
	 * @param ctx the parse tree
	 */
	void exitInitSection(PanelParser.InitSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#procSection}.
	 * @param ctx the parse tree
	 */
	void enterProcSection(PanelParser.ProcSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#procSection}.
	 * @param ctx the parse tree
	 */
	void exitProcSection(PanelParser.ProcSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#defaultParam}.
	 * @param ctx the parse tree
	 */
	void enterDefaultParam(PanelParser.DefaultParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#defaultParam}.
	 * @param ctx the parse tree
	 */
	void exitDefaultParam(PanelParser.DefaultParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#defValue}.
	 * @param ctx the parse tree
	 */
	void enterDefValue(PanelParser.DefValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#defValue}.
	 * @param ctx the parse tree
	 */
	void exitDefValue(PanelParser.DefValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#formatParam}.
	 * @param ctx the parse tree
	 */
	void enterFormatParam(PanelParser.FormatParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#formatParam}.
	 * @param ctx the parse tree
	 */
	void exitFormatParam(PanelParser.FormatParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#formatValue}.
	 * @param ctx the parse tree
	 */
	void enterFormatValue(PanelParser.FormatValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#formatValue}.
	 * @param ctx the parse tree
	 */
	void exitFormatValue(PanelParser.FormatValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#endSection}.
	 * @param ctx the parse tree
	 */
	void enterEndSection(PanelParser.EndSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#endSection}.
	 * @param ctx the parse tree
	 */
	void exitEndSection(PanelParser.EndSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#panelFunction}.
	 * @param ctx the parse tree
	 */
	void enterPanelFunction(PanelParser.PanelFunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#panelFunction}.
	 * @param ctx the parse tree
	 */
	void exitPanelFunction(PanelParser.PanelFunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#pfkFunc}.
	 * @param ctx the parse tree
	 */
	void enterPfkFunc(PanelParser.PfkFuncContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#pfkFunc}.
	 * @param ctx the parse tree
	 */
	void exitPfkFunc(PanelParser.PfkFuncContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#pfkParam}.
	 * @param ctx the parse tree
	 */
	void enterPfkParam(PanelParser.PfkParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#pfkParam}.
	 * @param ctx the parse tree
	 */
	void exitPfkParam(PanelParser.PfkParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#lvlineFunc}.
	 * @param ctx the parse tree
	 */
	void enterLvlineFunc(PanelParser.LvlineFuncContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#lvlineFunc}.
	 * @param ctx the parse tree
	 */
	void exitLvlineFunc(PanelParser.LvlineFuncContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#lvlineParam}.
	 * @param ctx the parse tree
	 */
	void enterLvlineParam(PanelParser.LvlineParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#lvlineParam}.
	 * @param ctx the parse tree
	 */
	void exitLvlineParam(PanelParser.LvlineParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#stringExpression}.
	 * @param ctx the parse tree
	 */
	void enterStringExpression(PanelParser.StringExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#stringExpression}.
	 * @param ctx the parse tree
	 */
	void exitStringExpression(PanelParser.StringExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#integerExpression}.
	 * @param ctx the parse tree
	 */
	void enterIntegerExpression(PanelParser.IntegerExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#integerExpression}.
	 * @param ctx the parse tree
	 */
	void exitIntegerExpression(PanelParser.IntegerExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#truncFunc}.
	 * @param ctx the parse tree
	 */
	void enterTruncFunc(PanelParser.TruncFuncContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#truncFunc}.
	 * @param ctx the parse tree
	 */
	void exitTruncFunc(PanelParser.TruncFuncContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#stringToTrunc}.
	 * @param ctx the parse tree
	 */
	void enterStringToTrunc(PanelParser.StringToTruncContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#stringToTrunc}.
	 * @param ctx the parse tree
	 */
	void exitStringToTrunc(PanelParser.StringToTruncContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#indexToTrunc}.
	 * @param ctx the parse tree
	 */
	void enterIndexToTrunc(PanelParser.IndexToTruncContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#indexToTrunc}.
	 * @param ctx the parse tree
	 */
	void exitIndexToTrunc(PanelParser.IndexToTruncContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#subStringToTrunc}.
	 * @param ctx the parse tree
	 */
	void enterSubStringToTrunc(PanelParser.SubStringToTruncContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#subStringToTrunc}.
	 * @param ctx the parse tree
	 */
	void exitSubStringToTrunc(PanelParser.SubStringToTruncContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#transFunc}.
	 * @param ctx the parse tree
	 */
	void enterTransFunc(PanelParser.TransFuncContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#transFunc}.
	 * @param ctx the parse tree
	 */
	void exitTransFunc(PanelParser.TransFuncContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#variable_to_trans}.
	 * @param ctx the parse tree
	 */
	void enterVariable_to_trans(PanelParser.Variable_to_transContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#variable_to_trans}.
	 * @param ctx the parse tree
	 */
	void exitVariable_to_trans(PanelParser.Variable_to_transContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#transParam}.
	 * @param ctx the parse tree
	 */
	void enterTransParam(PanelParser.TransParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#transParam}.
	 * @param ctx the parse tree
	 */
	void exitTransParam(PanelParser.TransParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#transVariable}.
	 * @param ctx the parse tree
	 */
	void enterTransVariable(PanelParser.TransVariableContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#transVariable}.
	 * @param ctx the parse tree
	 */
	void exitTransVariable(PanelParser.TransVariableContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#transReturn}.
	 * @param ctx the parse tree
	 */
	void enterTransReturn(PanelParser.TransReturnContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#transReturn}.
	 * @param ctx the parse tree
	 */
	void exitTransReturn(PanelParser.TransReturnContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#value}.
	 * @param ctx the parse tree
	 */
	void enterValue(PanelParser.ValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#value}.
	 * @param ctx the parse tree
	 */
	void exitValue(PanelParser.ValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link PanelParser#charDataKeyword}.
	 * @param ctx the parse tree
	 */
	void enterCharDataKeyword(PanelParser.CharDataKeywordContext ctx);
	/**
	 * Exit a parse tree produced by {@link PanelParser#charDataKeyword}.
	 * @param ctx the parse tree
	 */
	void exitCharDataKeyword(PanelParser.CharDataKeywordContext ctx);
}