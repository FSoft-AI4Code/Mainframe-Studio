# Generated from src/parsers/grammar/panel/Panel.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PanelParser import PanelParser
else:
    from PanelParser import PanelParser

# This class defines a complete listener for a parse tree produced by PanelParser.
class PanelListener(ParseTreeListener):

    # Enter a parse tree produced by PanelParser#startRule.
    def enterStartRule(self, ctx:PanelParser.StartRuleContext):
        pass

    # Exit a parse tree produced by PanelParser#startRule.
    def exitStartRule(self, ctx:PanelParser.StartRuleContext):
        pass


    # Enter a parse tree produced by PanelParser#section.
    def enterSection(self, ctx:PanelParser.SectionContext):
        pass

    # Exit a parse tree produced by PanelParser#section.
    def exitSection(self, ctx:PanelParser.SectionContext):
        pass


    # Enter a parse tree produced by PanelParser#reinitSection.
    def enterReinitSection(self, ctx:PanelParser.ReinitSectionContext):
        pass

    # Exit a parse tree produced by PanelParser#reinitSection.
    def exitReinitSection(self, ctx:PanelParser.ReinitSectionContext):
        pass


    # Enter a parse tree produced by PanelParser#modelSection.
    def enterModelSection(self, ctx:PanelParser.ModelSectionContext):
        pass

    # Exit a parse tree produced by PanelParser#modelSection.
    def exitModelSection(self, ctx:PanelParser.ModelSectionContext):
        pass


    # Enter a parse tree produced by PanelParser#modelParam.
    def enterModelParam(self, ctx:PanelParser.ModelParamContext):
        pass

    # Exit a parse tree produced by PanelParser#modelParam.
    def exitModelParam(self, ctx:PanelParser.ModelParamContext):
        pass


    # Enter a parse tree produced by PanelParser#model.
    def enterModel(self, ctx:PanelParser.ModelContext):
        pass

    # Exit a parse tree produced by PanelParser#model.
    def exitModel(self, ctx:PanelParser.ModelContext):
        pass


    # Enter a parse tree produced by PanelParser#attributeSection.
    def enterAttributeSection(self, ctx:PanelParser.AttributeSectionContext):
        pass

    # Exit a parse tree produced by PanelParser#attributeSection.
    def exitAttributeSection(self, ctx:PanelParser.AttributeSectionContext):
        pass


    # Enter a parse tree produced by PanelParser#attributeComponent.
    def enterAttributeComponent(self, ctx:PanelParser.AttributeComponentContext):
        pass

    # Exit a parse tree produced by PanelParser#attributeComponent.
    def exitAttributeComponent(self, ctx:PanelParser.AttributeComponentContext):
        pass


    # Enter a parse tree produced by PanelParser#attrParameter.
    def enterAttrParameter(self, ctx:PanelParser.AttrParameterContext):
        pass

    # Exit a parse tree produced by PanelParser#attrParameter.
    def exitAttrParameter(self, ctx:PanelParser.AttrParameterContext):
        pass


    # Enter a parse tree produced by PanelParser#outlineParam.
    def enterOutlineParam(self, ctx:PanelParser.OutlineParamContext):
        pass

    # Exit a parse tree produced by PanelParser#outlineParam.
    def exitOutlineParam(self, ctx:PanelParser.OutlineParamContext):
        pass


    # Enter a parse tree produced by PanelParser#outlineValue.
    def enterOutlineValue(self, ctx:PanelParser.OutlineValueContext):
        pass

    # Exit a parse tree produced by PanelParser#outlineValue.
    def exitOutlineValue(self, ctx:PanelParser.OutlineValueContext):
        pass


    # Enter a parse tree produced by PanelParser#padcParam.
    def enterPadcParam(self, ctx:PanelParser.PadcParamContext):
        pass

    # Exit a parse tree produced by PanelParser#padcParam.
    def exitPadcParam(self, ctx:PanelParser.PadcParamContext):
        pass


    # Enter a parse tree produced by PanelParser#padcValue.
    def enterPadcValue(self, ctx:PanelParser.PadcValueContext):
        pass

    # Exit a parse tree produced by PanelParser#padcValue.
    def exitPadcValue(self, ctx:PanelParser.PadcValueContext):
        pass


    # Enter a parse tree produced by PanelParser#justParam.
    def enterJustParam(self, ctx:PanelParser.JustParamContext):
        pass

    # Exit a parse tree produced by PanelParser#justParam.
    def exitJustParam(self, ctx:PanelParser.JustParamContext):
        pass


    # Enter a parse tree produced by PanelParser#justValue.
    def enterJustValue(self, ctx:PanelParser.JustValueContext):
        pass

    # Exit a parse tree produced by PanelParser#justValue.
    def exitJustValue(self, ctx:PanelParser.JustValueContext):
        pass


    # Enter a parse tree produced by PanelParser#areaParam.
    def enterAreaParam(self, ctx:PanelParser.AreaParamContext):
        pass

    # Exit a parse tree produced by PanelParser#areaParam.
    def exitAreaParam(self, ctx:PanelParser.AreaParamContext):
        pass


    # Enter a parse tree produced by PanelParser#areaValue.
    def enterAreaValue(self, ctx:PanelParser.AreaValueContext):
        pass

    # Exit a parse tree produced by PanelParser#areaValue.
    def exitAreaValue(self, ctx:PanelParser.AreaValueContext):
        pass


    # Enter a parse tree produced by PanelParser#scrollParam.
    def enterScrollParam(self, ctx:PanelParser.ScrollParamContext):
        pass

    # Exit a parse tree produced by PanelParser#scrollParam.
    def exitScrollParam(self, ctx:PanelParser.ScrollParamContext):
        pass


    # Enter a parse tree produced by PanelParser#scrollValue.
    def enterScrollValue(self, ctx:PanelParser.ScrollValueContext):
        pass

    # Exit a parse tree produced by PanelParser#scrollValue.
    def exitScrollValue(self, ctx:PanelParser.ScrollValueContext):
        pass


    # Enter a parse tree produced by PanelParser#extendParam.
    def enterExtendParam(self, ctx:PanelParser.ExtendParamContext):
        pass

    # Exit a parse tree produced by PanelParser#extendParam.
    def exitExtendParam(self, ctx:PanelParser.ExtendParamContext):
        pass


    # Enter a parse tree produced by PanelParser#extendValue.
    def enterExtendValue(self, ctx:PanelParser.ExtendValueContext):
        pass

    # Exit a parse tree produced by PanelParser#extendValue.
    def exitExtendValue(self, ctx:PanelParser.ExtendValueContext):
        pass


    # Enter a parse tree produced by PanelParser#capsParam.
    def enterCapsParam(self, ctx:PanelParser.CapsParamContext):
        pass

    # Exit a parse tree produced by PanelParser#capsParam.
    def exitCapsParam(self, ctx:PanelParser.CapsParamContext):
        pass


    # Enter a parse tree produced by PanelParser#capsValue.
    def enterCapsValue(self, ctx:PanelParser.CapsValueContext):
        pass

    # Exit a parse tree produced by PanelParser#capsValue.
    def exitCapsValue(self, ctx:PanelParser.CapsValueContext):
        pass


    # Enter a parse tree produced by PanelParser#padParam.
    def enterPadParam(self, ctx:PanelParser.PadParamContext):
        pass

    # Exit a parse tree produced by PanelParser#padParam.
    def exitPadParam(self, ctx:PanelParser.PadParamContext):
        pass


    # Enter a parse tree produced by PanelParser#padValue.
    def enterPadValue(self, ctx:PanelParser.PadValueContext):
        pass

    # Exit a parse tree produced by PanelParser#padValue.
    def exitPadValue(self, ctx:PanelParser.PadValueContext):
        pass


    # Enter a parse tree produced by PanelParser#skipParam.
    def enterSkipParam(self, ctx:PanelParser.SkipParamContext):
        pass

    # Exit a parse tree produced by PanelParser#skipParam.
    def exitSkipParam(self, ctx:PanelParser.SkipParamContext):
        pass


    # Enter a parse tree produced by PanelParser#skipValue.
    def enterSkipValue(self, ctx:PanelParser.SkipValueContext):
        pass

    # Exit a parse tree produced by PanelParser#skipValue.
    def exitSkipValue(self, ctx:PanelParser.SkipValueContext):
        pass


    # Enter a parse tree produced by PanelParser#typeParam.
    def enterTypeParam(self, ctx:PanelParser.TypeParamContext):
        pass

    # Exit a parse tree produced by PanelParser#typeParam.
    def exitTypeParam(self, ctx:PanelParser.TypeParamContext):
        pass


    # Enter a parse tree produced by PanelParser#intensParam.
    def enterIntensParam(self, ctx:PanelParser.IntensParamContext):
        pass

    # Exit a parse tree produced by PanelParser#intensParam.
    def exitIntensParam(self, ctx:PanelParser.IntensParamContext):
        pass


    # Enter a parse tree produced by PanelParser#intensValue.
    def enterIntensValue(self, ctx:PanelParser.IntensValueContext):
        pass

    # Exit a parse tree produced by PanelParser#intensValue.
    def exitIntensValue(self, ctx:PanelParser.IntensValueContext):
        pass


    # Enter a parse tree produced by PanelParser#colorParam.
    def enterColorParam(self, ctx:PanelParser.ColorParamContext):
        pass

    # Exit a parse tree produced by PanelParser#colorParam.
    def exitColorParam(self, ctx:PanelParser.ColorParamContext):
        pass


    # Enter a parse tree produced by PanelParser#hiliteParam.
    def enterHiliteParam(self, ctx:PanelParser.HiliteParamContext):
        pass

    # Exit a parse tree produced by PanelParser#hiliteParam.
    def exitHiliteParam(self, ctx:PanelParser.HiliteParamContext):
        pass


    # Enter a parse tree produced by PanelParser#attrChar.
    def enterAttrChar(self, ctx:PanelParser.AttrCharContext):
        pass

    # Exit a parse tree produced by PanelParser#attrChar.
    def exitAttrChar(self, ctx:PanelParser.AttrCharContext):
        pass


    # Enter a parse tree produced by PanelParser#bodySection.
    def enterBodySection(self, ctx:PanelParser.BodySectionContext):
        pass

    # Exit a parse tree produced by PanelParser#bodySection.
    def exitBodySection(self, ctx:PanelParser.BodySectionContext):
        pass


    # Enter a parse tree produced by PanelParser#bodyParam.
    def enterBodyParam(self, ctx:PanelParser.BodyParamContext):
        pass

    # Exit a parse tree produced by PanelParser#bodyParam.
    def exitBodyParam(self, ctx:PanelParser.BodyParamContext):
        pass


    # Enter a parse tree produced by PanelParser#kanaParam.
    def enterKanaParam(self, ctx:PanelParser.KanaParamContext):
        pass

    # Exit a parse tree produced by PanelParser#kanaParam.
    def exitKanaParam(self, ctx:PanelParser.KanaParamContext):
        pass


    # Enter a parse tree produced by PanelParser#windowParam.
    def enterWindowParam(self, ctx:PanelParser.WindowParamContext):
        pass

    # Exit a parse tree produced by PanelParser#windowParam.
    def exitWindowParam(self, ctx:PanelParser.WindowParamContext):
        pass


    # Enter a parse tree produced by PanelParser#width.
    def enterWidth(self, ctx:PanelParser.WidthContext):
        pass

    # Exit a parse tree produced by PanelParser#width.
    def exitWidth(self, ctx:PanelParser.WidthContext):
        pass


    # Enter a parse tree produced by PanelParser#length.
    def enterLength(self, ctx:PanelParser.LengthContext):
        pass

    # Exit a parse tree produced by PanelParser#length.
    def exitLength(self, ctx:PanelParser.LengthContext):
        pass


    # Enter a parse tree produced by PanelParser#widthPara.
    def enterWidthPara(self, ctx:PanelParser.WidthParaContext):
        pass

    # Exit a parse tree produced by PanelParser#widthPara.
    def exitWidthPara(self, ctx:PanelParser.WidthParaContext):
        pass


    # Enter a parse tree produced by PanelParser#statement.
    def enterStatement(self, ctx:PanelParser.StatementContext):
        pass

    # Exit a parse tree produced by PanelParser#statement.
    def exitStatement(self, ctx:PanelParser.StatementContext):
        pass


    # Enter a parse tree produced by PanelParser#refreshStatement.
    def enterRefreshStatement(self, ctx:PanelParser.RefreshStatementContext):
        pass

    # Exit a parse tree produced by PanelParser#refreshStatement.
    def exitRefreshStatement(self, ctx:PanelParser.RefreshStatementContext):
        pass


    # Enter a parse tree produced by PanelParser#ifStatement.
    def enterIfStatement(self, ctx:PanelParser.IfStatementContext):
        pass

    # Exit a parse tree produced by PanelParser#ifStatement.
    def exitIfStatement(self, ctx:PanelParser.IfStatementContext):
        pass


    # Enter a parse tree produced by PanelParser#condition.
    def enterCondition(self, ctx:PanelParser.ConditionContext):
        pass

    # Exit a parse tree produced by PanelParser#condition.
    def exitCondition(self, ctx:PanelParser.ConditionContext):
        pass


    # Enter a parse tree produced by PanelParser#andOrCondition.
    def enterAndOrCondition(self, ctx:PanelParser.AndOrConditionContext):
        pass

    # Exit a parse tree produced by PanelParser#andOrCondition.
    def exitAndOrCondition(self, ctx:PanelParser.AndOrConditionContext):
        pass


    # Enter a parse tree produced by PanelParser#combinableCondition.
    def enterCombinableCondition(self, ctx:PanelParser.CombinableConditionContext):
        pass

    # Exit a parse tree produced by PanelParser#combinableCondition.
    def exitCombinableCondition(self, ctx:PanelParser.CombinableConditionContext):
        pass


    # Enter a parse tree produced by PanelParser#simpleCondition.
    def enterSimpleCondition(self, ctx:PanelParser.SimpleConditionContext):
        pass

    # Exit a parse tree produced by PanelParser#simpleCondition.
    def exitSimpleCondition(self, ctx:PanelParser.SimpleConditionContext):
        pass


    # Enter a parse tree produced by PanelParser#relationCondition.
    def enterRelationCondition(self, ctx:PanelParser.RelationConditionContext):
        pass

    # Exit a parse tree produced by PanelParser#relationCondition.
    def exitRelationCondition(self, ctx:PanelParser.RelationConditionContext):
        pass


    # Enter a parse tree produced by PanelParser#relationArithmeticComparison.
    def enterRelationArithmeticComparison(self, ctx:PanelParser.RelationArithmeticComparisonContext):
        pass

    # Exit a parse tree produced by PanelParser#relationArithmeticComparison.
    def exitRelationArithmeticComparison(self, ctx:PanelParser.RelationArithmeticComparisonContext):
        pass


    # Enter a parse tree produced by PanelParser#arithmeticExpression.
    def enterArithmeticExpression(self, ctx:PanelParser.ArithmeticExpressionContext):
        pass

    # Exit a parse tree produced by PanelParser#arithmeticExpression.
    def exitArithmeticExpression(self, ctx:PanelParser.ArithmeticExpressionContext):
        pass


    # Enter a parse tree produced by PanelParser#relationalOperator.
    def enterRelationalOperator(self, ctx:PanelParser.RelationalOperatorContext):
        pass

    # Exit a parse tree produced by PanelParser#relationalOperator.
    def exitRelationalOperator(self, ctx:PanelParser.RelationalOperatorContext):
        pass


    # Enter a parse tree produced by PanelParser#thenIf.
    def enterThenIf(self, ctx:PanelParser.ThenIfContext):
        pass

    # Exit a parse tree produced by PanelParser#thenIf.
    def exitThenIf(self, ctx:PanelParser.ThenIfContext):
        pass


    # Enter a parse tree produced by PanelParser#verStatement.
    def enterVerStatement(self, ctx:PanelParser.VerStatementContext):
        pass

    # Exit a parse tree produced by PanelParser#verStatement.
    def exitVerStatement(self, ctx:PanelParser.VerStatementContext):
        pass


    # Enter a parse tree produced by PanelParser#verMsg.
    def enterVerMsg(self, ctx:PanelParser.VerMsgContext):
        pass

    # Exit a parse tree produced by PanelParser#verMsg.
    def exitVerMsg(self, ctx:PanelParser.VerMsgContext):
        pass


    # Enter a parse tree produced by PanelParser#verCriteria.
    def enterVerCriteria(self, ctx:PanelParser.VerCriteriaContext):
        pass

    # Exit a parse tree produced by PanelParser#verCriteria.
    def exitVerCriteria(self, ctx:PanelParser.VerCriteriaContext):
        pass


    # Enter a parse tree produced by PanelParser#simpleCriteria.
    def enterSimpleCriteria(self, ctx:PanelParser.SimpleCriteriaContext):
        pass

    # Exit a parse tree produced by PanelParser#simpleCriteria.
    def exitSimpleCriteria(self, ctx:PanelParser.SimpleCriteriaContext):
        pass


    # Enter a parse tree produced by PanelParser#lengthCriteria.
    def enterLengthCriteria(self, ctx:PanelParser.LengthCriteriaContext):
        pass

    # Exit a parse tree produced by PanelParser#lengthCriteria.
    def exitLengthCriteria(self, ctx:PanelParser.LengthCriteriaContext):
        pass


    # Enter a parse tree produced by PanelParser#listCriteria.
    def enterListCriteria(self, ctx:PanelParser.ListCriteriaContext):
        pass

    # Exit a parse tree produced by PanelParser#listCriteria.
    def exitListCriteria(self, ctx:PanelParser.ListCriteriaContext):
        pass


    # Enter a parse tree produced by PanelParser#pictCriteria.
    def enterPictCriteria(self, ctx:PanelParser.PictCriteriaContext):
        pass

    # Exit a parse tree produced by PanelParser#pictCriteria.
    def exitPictCriteria(self, ctx:PanelParser.PictCriteriaContext):
        pass


    # Enter a parse tree produced by PanelParser#picValue.
    def enterPicValue(self, ctx:PanelParser.PicValueContext):
        pass

    # Exit a parse tree produced by PanelParser#picValue.
    def exitPicValue(self, ctx:PanelParser.PicValueContext):
        pass


    # Enter a parse tree produced by PanelParser#rangeCriteria.
    def enterRangeCriteria(self, ctx:PanelParser.RangeCriteriaContext):
        pass

    # Exit a parse tree produced by PanelParser#rangeCriteria.
    def exitRangeCriteria(self, ctx:PanelParser.RangeCriteriaContext):
        pass


    # Enter a parse tree produced by PanelParser#expectedLength.
    def enterExpectedLength(self, ctx:PanelParser.ExpectedLengthContext):
        pass

    # Exit a parse tree produced by PanelParser#expectedLength.
    def exitExpectedLength(self, ctx:PanelParser.ExpectedLengthContext):
        pass


    # Enter a parse tree produced by PanelParser#stringValue.
    def enterStringValue(self, ctx:PanelParser.StringValueContext):
        pass

    # Exit a parse tree produced by PanelParser#stringValue.
    def exitStringValue(self, ctx:PanelParser.StringValueContext):
        pass


    # Enter a parse tree produced by PanelParser#varlist.
    def enterVarlist(self, ctx:PanelParser.VarlistContext):
        pass

    # Exit a parse tree produced by PanelParser#varlist.
    def exitVarlist(self, ctx:PanelParser.VarlistContext):
        pass


    # Enter a parse tree produced by PanelParser#maskCharacter.
    def enterMaskCharacter(self, ctx:PanelParser.MaskCharacterContext):
        pass

    # Exit a parse tree produced by PanelParser#maskCharacter.
    def exitMaskCharacter(self, ctx:PanelParser.MaskCharacterContext):
        pass


    # Enter a parse tree produced by PanelParser#fieldMask.
    def enterFieldMask(self, ctx:PanelParser.FieldMaskContext):
        pass

    # Exit a parse tree produced by PanelParser#fieldMask.
    def exitFieldMask(self, ctx:PanelParser.FieldMaskContext):
        pass


    # Enter a parse tree produced by PanelParser#lower.
    def enterLower(self, ctx:PanelParser.LowerContext):
        pass

    # Exit a parse tree produced by PanelParser#lower.
    def exitLower(self, ctx:PanelParser.LowerContext):
        pass


    # Enter a parse tree produced by PanelParser#upper.
    def enterUpper(self, ctx:PanelParser.UpperContext):
        pass

    # Exit a parse tree produced by PanelParser#upper.
    def exitUpper(self, ctx:PanelParser.UpperContext):
        pass


    # Enter a parse tree produced by PanelParser#elseIf.
    def enterElseIf(self, ctx:PanelParser.ElseIfContext):
        pass

    # Exit a parse tree produced by PanelParser#elseIf.
    def exitElseIf(self, ctx:PanelParser.ElseIfContext):
        pass


    # Enter a parse tree produced by PanelParser#assignStatement.
    def enterAssignStatement(self, ctx:PanelParser.AssignStatementContext):
        pass

    # Exit a parse tree produced by PanelParser#assignStatement.
    def exitAssignStatement(self, ctx:PanelParser.AssignStatementContext):
        pass


    # Enter a parse tree produced by PanelParser#variable.
    def enterVariable(self, ctx:PanelParser.VariableContext):
        pass

    # Exit a parse tree produced by PanelParser#variable.
    def exitVariable(self, ctx:PanelParser.VariableContext):
        pass


    # Enter a parse tree produced by PanelParser#assignPart.
    def enterAssignPart(self, ctx:PanelParser.AssignPartContext):
        pass

    # Exit a parse tree produced by PanelParser#assignPart.
    def exitAssignPart(self, ctx:PanelParser.AssignPartContext):
        pass


    # Enter a parse tree produced by PanelParser#vgetStatement.
    def enterVgetStatement(self, ctx:PanelParser.VgetStatementContext):
        pass

    # Exit a parse tree produced by PanelParser#vgetStatement.
    def exitVgetStatement(self, ctx:PanelParser.VgetStatementContext):
        pass


    # Enter a parse tree produced by PanelParser#vputStatement.
    def enterVputStatement(self, ctx:PanelParser.VputStatementContext):
        pass

    # Exit a parse tree produced by PanelParser#vputStatement.
    def exitVputStatement(self, ctx:PanelParser.VputStatementContext):
        pass


    # Enter a parse tree produced by PanelParser#name_list.
    def enterName_list(self, ctx:PanelParser.Name_listContext):
        pass

    # Exit a parse tree produced by PanelParser#name_list.
    def exitName_list(self, ctx:PanelParser.Name_listContext):
        pass


    # Enter a parse tree produced by PanelParser#name_list_item.
    def enterName_list_item(self, ctx:PanelParser.Name_list_itemContext):
        pass

    # Exit a parse tree produced by PanelParser#name_list_item.
    def exitName_list_item(self, ctx:PanelParser.Name_list_itemContext):
        pass


    # Enter a parse tree produced by PanelParser#vgetParameter.
    def enterVgetParameter(self, ctx:PanelParser.VgetParameterContext):
        pass

    # Exit a parse tree produced by PanelParser#vgetParameter.
    def exitVgetParameter(self, ctx:PanelParser.VgetParameterContext):
        pass


    # Enter a parse tree produced by PanelParser#vputParameter.
    def enterVputParameter(self, ctx:PanelParser.VputParameterContext):
        pass

    # Exit a parse tree produced by PanelParser#vputParameter.
    def exitVputParameter(self, ctx:PanelParser.VputParameterContext):
        pass


    # Enter a parse tree produced by PanelParser#initSection.
    def enterInitSection(self, ctx:PanelParser.InitSectionContext):
        pass

    # Exit a parse tree produced by PanelParser#initSection.
    def exitInitSection(self, ctx:PanelParser.InitSectionContext):
        pass


    # Enter a parse tree produced by PanelParser#procSection.
    def enterProcSection(self, ctx:PanelParser.ProcSectionContext):
        pass

    # Exit a parse tree produced by PanelParser#procSection.
    def exitProcSection(self, ctx:PanelParser.ProcSectionContext):
        pass


    # Enter a parse tree produced by PanelParser#defaultParam.
    def enterDefaultParam(self, ctx:PanelParser.DefaultParamContext):
        pass

    # Exit a parse tree produced by PanelParser#defaultParam.
    def exitDefaultParam(self, ctx:PanelParser.DefaultParamContext):
        pass


    # Enter a parse tree produced by PanelParser#defValue.
    def enterDefValue(self, ctx:PanelParser.DefValueContext):
        pass

    # Exit a parse tree produced by PanelParser#defValue.
    def exitDefValue(self, ctx:PanelParser.DefValueContext):
        pass


    # Enter a parse tree produced by PanelParser#formatParam.
    def enterFormatParam(self, ctx:PanelParser.FormatParamContext):
        pass

    # Exit a parse tree produced by PanelParser#formatParam.
    def exitFormatParam(self, ctx:PanelParser.FormatParamContext):
        pass


    # Enter a parse tree produced by PanelParser#formatValue.
    def enterFormatValue(self, ctx:PanelParser.FormatValueContext):
        pass

    # Exit a parse tree produced by PanelParser#formatValue.
    def exitFormatValue(self, ctx:PanelParser.FormatValueContext):
        pass


    # Enter a parse tree produced by PanelParser#endSection.
    def enterEndSection(self, ctx:PanelParser.EndSectionContext):
        pass

    # Exit a parse tree produced by PanelParser#endSection.
    def exitEndSection(self, ctx:PanelParser.EndSectionContext):
        pass


    # Enter a parse tree produced by PanelParser#panelFunction.
    def enterPanelFunction(self, ctx:PanelParser.PanelFunctionContext):
        pass

    # Exit a parse tree produced by PanelParser#panelFunction.
    def exitPanelFunction(self, ctx:PanelParser.PanelFunctionContext):
        pass


    # Enter a parse tree produced by PanelParser#pfkFunc.
    def enterPfkFunc(self, ctx:PanelParser.PfkFuncContext):
        pass

    # Exit a parse tree produced by PanelParser#pfkFunc.
    def exitPfkFunc(self, ctx:PanelParser.PfkFuncContext):
        pass


    # Enter a parse tree produced by PanelParser#pfkParam.
    def enterPfkParam(self, ctx:PanelParser.PfkParamContext):
        pass

    # Exit a parse tree produced by PanelParser#pfkParam.
    def exitPfkParam(self, ctx:PanelParser.PfkParamContext):
        pass


    # Enter a parse tree produced by PanelParser#lvlineFunc.
    def enterLvlineFunc(self, ctx:PanelParser.LvlineFuncContext):
        pass

    # Exit a parse tree produced by PanelParser#lvlineFunc.
    def exitLvlineFunc(self, ctx:PanelParser.LvlineFuncContext):
        pass


    # Enter a parse tree produced by PanelParser#lvlineParam.
    def enterLvlineParam(self, ctx:PanelParser.LvlineParamContext):
        pass

    # Exit a parse tree produced by PanelParser#lvlineParam.
    def exitLvlineParam(self, ctx:PanelParser.LvlineParamContext):
        pass


    # Enter a parse tree produced by PanelParser#stringExpression.
    def enterStringExpression(self, ctx:PanelParser.StringExpressionContext):
        pass

    # Exit a parse tree produced by PanelParser#stringExpression.
    def exitStringExpression(self, ctx:PanelParser.StringExpressionContext):
        pass


    # Enter a parse tree produced by PanelParser#integerExpression.
    def enterIntegerExpression(self, ctx:PanelParser.IntegerExpressionContext):
        pass

    # Exit a parse tree produced by PanelParser#integerExpression.
    def exitIntegerExpression(self, ctx:PanelParser.IntegerExpressionContext):
        pass


    # Enter a parse tree produced by PanelParser#truncFunc.
    def enterTruncFunc(self, ctx:PanelParser.TruncFuncContext):
        pass

    # Exit a parse tree produced by PanelParser#truncFunc.
    def exitTruncFunc(self, ctx:PanelParser.TruncFuncContext):
        pass


    # Enter a parse tree produced by PanelParser#stringToTrunc.
    def enterStringToTrunc(self, ctx:PanelParser.StringToTruncContext):
        pass

    # Exit a parse tree produced by PanelParser#stringToTrunc.
    def exitStringToTrunc(self, ctx:PanelParser.StringToTruncContext):
        pass


    # Enter a parse tree produced by PanelParser#indexToTrunc.
    def enterIndexToTrunc(self, ctx:PanelParser.IndexToTruncContext):
        pass

    # Exit a parse tree produced by PanelParser#indexToTrunc.
    def exitIndexToTrunc(self, ctx:PanelParser.IndexToTruncContext):
        pass


    # Enter a parse tree produced by PanelParser#subStringToTrunc.
    def enterSubStringToTrunc(self, ctx:PanelParser.SubStringToTruncContext):
        pass

    # Exit a parse tree produced by PanelParser#subStringToTrunc.
    def exitSubStringToTrunc(self, ctx:PanelParser.SubStringToTruncContext):
        pass


    # Enter a parse tree produced by PanelParser#transFunc.
    def enterTransFunc(self, ctx:PanelParser.TransFuncContext):
        pass

    # Exit a parse tree produced by PanelParser#transFunc.
    def exitTransFunc(self, ctx:PanelParser.TransFuncContext):
        pass


    # Enter a parse tree produced by PanelParser#variable_to_trans.
    def enterVariable_to_trans(self, ctx:PanelParser.Variable_to_transContext):
        pass

    # Exit a parse tree produced by PanelParser#variable_to_trans.
    def exitVariable_to_trans(self, ctx:PanelParser.Variable_to_transContext):
        pass


    # Enter a parse tree produced by PanelParser#transParam.
    def enterTransParam(self, ctx:PanelParser.TransParamContext):
        pass

    # Exit a parse tree produced by PanelParser#transParam.
    def exitTransParam(self, ctx:PanelParser.TransParamContext):
        pass


    # Enter a parse tree produced by PanelParser#transVariable.
    def enterTransVariable(self, ctx:PanelParser.TransVariableContext):
        pass

    # Exit a parse tree produced by PanelParser#transVariable.
    def exitTransVariable(self, ctx:PanelParser.TransVariableContext):
        pass


    # Enter a parse tree produced by PanelParser#transReturn.
    def enterTransReturn(self, ctx:PanelParser.TransReturnContext):
        pass

    # Exit a parse tree produced by PanelParser#transReturn.
    def exitTransReturn(self, ctx:PanelParser.TransReturnContext):
        pass


    # Enter a parse tree produced by PanelParser#value.
    def enterValue(self, ctx:PanelParser.ValueContext):
        pass

    # Exit a parse tree produced by PanelParser#value.
    def exitValue(self, ctx:PanelParser.ValueContext):
        pass


    # Enter a parse tree produced by PanelParser#charDataKeyword.
    def enterCharDataKeyword(self, ctx:PanelParser.CharDataKeywordContext):
        pass

    # Exit a parse tree produced by PanelParser#charDataKeyword.
    def exitCharDataKeyword(self, ctx:PanelParser.CharDataKeywordContext):
        pass



del PanelParser