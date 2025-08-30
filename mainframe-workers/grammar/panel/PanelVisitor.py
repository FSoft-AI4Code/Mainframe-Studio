# Generated from grammar/panel/Panel.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PanelParser import PanelParser
else:
    from PanelParser import PanelParser

# This class defines a complete generic visitor for a parse tree produced by PanelParser.

class PanelVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PanelParser#startRule.
    def visitStartRule(self, ctx:PanelParser.StartRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#section.
    def visitSection(self, ctx:PanelParser.SectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#reinitSection.
    def visitReinitSection(self, ctx:PanelParser.ReinitSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#modelSection.
    def visitModelSection(self, ctx:PanelParser.ModelSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#modelParam.
    def visitModelParam(self, ctx:PanelParser.ModelParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#model.
    def visitModel(self, ctx:PanelParser.ModelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#attributeSection.
    def visitAttributeSection(self, ctx:PanelParser.AttributeSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#attributeComponent.
    def visitAttributeComponent(self, ctx:PanelParser.AttributeComponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#attrParameter.
    def visitAttrParameter(self, ctx:PanelParser.AttrParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#outlineParam.
    def visitOutlineParam(self, ctx:PanelParser.OutlineParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#outlineValue.
    def visitOutlineValue(self, ctx:PanelParser.OutlineValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#padcParam.
    def visitPadcParam(self, ctx:PanelParser.PadcParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#padcValue.
    def visitPadcValue(self, ctx:PanelParser.PadcValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#justParam.
    def visitJustParam(self, ctx:PanelParser.JustParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#justValue.
    def visitJustValue(self, ctx:PanelParser.JustValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#areaParam.
    def visitAreaParam(self, ctx:PanelParser.AreaParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#areaValue.
    def visitAreaValue(self, ctx:PanelParser.AreaValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#scrollParam.
    def visitScrollParam(self, ctx:PanelParser.ScrollParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#scrollValue.
    def visitScrollValue(self, ctx:PanelParser.ScrollValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#extendParam.
    def visitExtendParam(self, ctx:PanelParser.ExtendParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#extendValue.
    def visitExtendValue(self, ctx:PanelParser.ExtendValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#capsParam.
    def visitCapsParam(self, ctx:PanelParser.CapsParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#capsValue.
    def visitCapsValue(self, ctx:PanelParser.CapsValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#padParam.
    def visitPadParam(self, ctx:PanelParser.PadParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#padValue.
    def visitPadValue(self, ctx:PanelParser.PadValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#skipParam.
    def visitSkipParam(self, ctx:PanelParser.SkipParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#skipValue.
    def visitSkipValue(self, ctx:PanelParser.SkipValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#typeParam.
    def visitTypeParam(self, ctx:PanelParser.TypeParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#intensParam.
    def visitIntensParam(self, ctx:PanelParser.IntensParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#intensValue.
    def visitIntensValue(self, ctx:PanelParser.IntensValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#colorParam.
    def visitColorParam(self, ctx:PanelParser.ColorParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#hiliteParam.
    def visitHiliteParam(self, ctx:PanelParser.HiliteParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#attrChar.
    def visitAttrChar(self, ctx:PanelParser.AttrCharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#bodySection.
    def visitBodySection(self, ctx:PanelParser.BodySectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#bodyParam.
    def visitBodyParam(self, ctx:PanelParser.BodyParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#kanaParam.
    def visitKanaParam(self, ctx:PanelParser.KanaParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#windowParam.
    def visitWindowParam(self, ctx:PanelParser.WindowParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#width.
    def visitWidth(self, ctx:PanelParser.WidthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#length.
    def visitLength(self, ctx:PanelParser.LengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#widthPara.
    def visitWidthPara(self, ctx:PanelParser.WidthParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#statement.
    def visitStatement(self, ctx:PanelParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#refreshStatement.
    def visitRefreshStatement(self, ctx:PanelParser.RefreshStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#ifStatement.
    def visitIfStatement(self, ctx:PanelParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#condition.
    def visitCondition(self, ctx:PanelParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#andOrCondition.
    def visitAndOrCondition(self, ctx:PanelParser.AndOrConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#combinableCondition.
    def visitCombinableCondition(self, ctx:PanelParser.CombinableConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#simpleCondition.
    def visitSimpleCondition(self, ctx:PanelParser.SimpleConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#relationCondition.
    def visitRelationCondition(self, ctx:PanelParser.RelationConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#relationArithmeticComparison.
    def visitRelationArithmeticComparison(self, ctx:PanelParser.RelationArithmeticComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#arithmeticExpression.
    def visitArithmeticExpression(self, ctx:PanelParser.ArithmeticExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#relationalOperator.
    def visitRelationalOperator(self, ctx:PanelParser.RelationalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#thenIf.
    def visitThenIf(self, ctx:PanelParser.ThenIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#verStatement.
    def visitVerStatement(self, ctx:PanelParser.VerStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#verMsg.
    def visitVerMsg(self, ctx:PanelParser.VerMsgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#verCriteria.
    def visitVerCriteria(self, ctx:PanelParser.VerCriteriaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#simpleCriteria.
    def visitSimpleCriteria(self, ctx:PanelParser.SimpleCriteriaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#lengthCriteria.
    def visitLengthCriteria(self, ctx:PanelParser.LengthCriteriaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#listCriteria.
    def visitListCriteria(self, ctx:PanelParser.ListCriteriaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#pictCriteria.
    def visitPictCriteria(self, ctx:PanelParser.PictCriteriaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#picValue.
    def visitPicValue(self, ctx:PanelParser.PicValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#rangeCriteria.
    def visitRangeCriteria(self, ctx:PanelParser.RangeCriteriaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#expectedLength.
    def visitExpectedLength(self, ctx:PanelParser.ExpectedLengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#stringValue.
    def visitStringValue(self, ctx:PanelParser.StringValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#varlist.
    def visitVarlist(self, ctx:PanelParser.VarlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#maskCharacter.
    def visitMaskCharacter(self, ctx:PanelParser.MaskCharacterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#fieldMask.
    def visitFieldMask(self, ctx:PanelParser.FieldMaskContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#lower.
    def visitLower(self, ctx:PanelParser.LowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#upper.
    def visitUpper(self, ctx:PanelParser.UpperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#elseIf.
    def visitElseIf(self, ctx:PanelParser.ElseIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#assignStatement.
    def visitAssignStatement(self, ctx:PanelParser.AssignStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#variable.
    def visitVariable(self, ctx:PanelParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#assignPart.
    def visitAssignPart(self, ctx:PanelParser.AssignPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#vgetStatement.
    def visitVgetStatement(self, ctx:PanelParser.VgetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#vputStatement.
    def visitVputStatement(self, ctx:PanelParser.VputStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#name_list.
    def visitName_list(self, ctx:PanelParser.Name_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#name_list_item.
    def visitName_list_item(self, ctx:PanelParser.Name_list_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#vgetParameter.
    def visitVgetParameter(self, ctx:PanelParser.VgetParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#vputParameter.
    def visitVputParameter(self, ctx:PanelParser.VputParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#initSection.
    def visitInitSection(self, ctx:PanelParser.InitSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#procSection.
    def visitProcSection(self, ctx:PanelParser.ProcSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#defaultParam.
    def visitDefaultParam(self, ctx:PanelParser.DefaultParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#defValue.
    def visitDefValue(self, ctx:PanelParser.DefValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#formatParam.
    def visitFormatParam(self, ctx:PanelParser.FormatParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#formatValue.
    def visitFormatValue(self, ctx:PanelParser.FormatValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#endSection.
    def visitEndSection(self, ctx:PanelParser.EndSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#panelFunction.
    def visitPanelFunction(self, ctx:PanelParser.PanelFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#pfkFunc.
    def visitPfkFunc(self, ctx:PanelParser.PfkFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#pfkParam.
    def visitPfkParam(self, ctx:PanelParser.PfkParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#lvlineFunc.
    def visitLvlineFunc(self, ctx:PanelParser.LvlineFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#lvlineParam.
    def visitLvlineParam(self, ctx:PanelParser.LvlineParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#stringExpression.
    def visitStringExpression(self, ctx:PanelParser.StringExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#integerExpression.
    def visitIntegerExpression(self, ctx:PanelParser.IntegerExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#truncFunc.
    def visitTruncFunc(self, ctx:PanelParser.TruncFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#stringToTrunc.
    def visitStringToTrunc(self, ctx:PanelParser.StringToTruncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#indexToTrunc.
    def visitIndexToTrunc(self, ctx:PanelParser.IndexToTruncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#subStringToTrunc.
    def visitSubStringToTrunc(self, ctx:PanelParser.SubStringToTruncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#transFunc.
    def visitTransFunc(self, ctx:PanelParser.TransFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#transDefaultOutput.
    def visitTransDefaultOutput(self, ctx:PanelParser.TransDefaultOutputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#transParam.
    def visitTransParam(self, ctx:PanelParser.TransParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#transVariable.
    def visitTransVariable(self, ctx:PanelParser.TransVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#transReturn.
    def visitTransReturn(self, ctx:PanelParser.TransReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#value.
    def visitValue(self, ctx:PanelParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PanelParser#charDataKeyword.
    def visitCharDataKeyword(self, ctx:PanelParser.CharDataKeywordContext):
        return self.visitChildren(ctx)



del PanelParser