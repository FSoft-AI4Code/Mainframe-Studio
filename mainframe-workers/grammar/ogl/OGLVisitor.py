# Generated from grammar/ogl/OGL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .OGLParser import OGLParser
else:
    from OGLParser import OGLParser

# This class defines a complete generic visitor for a parse tree produced by OGLParser.

class OGLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by OGLParser#startRule.
    def visitStartRule(self, ctx:OGLParser.StartRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#command.
    def visitCommand(self, ctx:OGLParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#segmentCommand.
    def visitSegmentCommand(self, ctx:OGLParser.SegmentCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#segmentName.
    def visitSegmentName(self, ctx:OGLParser.SegmentNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#segmentDDName.
    def visitSegmentDDName(self, ctx:OGLParser.SegmentDDNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#segmentDDNameName.
    def visitSegmentDDNameName(self, ctx:OGLParser.SegmentDDNameNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#segmentFileType.
    def visitSegmentFileType(self, ctx:OGLParser.SegmentFileTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#placePatternCommand.
    def visitPlacePatternCommand(self, ctx:OGLParser.PlacePatternCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#patternColor.
    def visitPatternColor(self, ctx:OGLParser.PatternColorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#patternColorName.
    def visitPatternColorName(self, ctx:OGLParser.PatternColorNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#mirrorOption.
    def visitMirrorOption(self, ctx:OGLParser.MirrorOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#negativeOption.
    def visitNegativeOption(self, ctx:OGLParser.NegativeOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#patternShade.
    def visitPatternShade(self, ctx:OGLParser.PatternShadeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#definepatternCommand.
    def visitDefinepatternCommand(self, ctx:OGLParser.DefinepatternCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#lineCoding.
    def visitLineCoding(self, ctx:OGLParser.LineCodingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#lineCodingPels.
    def visitLineCodingPels(self, ctx:OGLParser.LineCodingPelsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#lineCodingEncoded.
    def visitLineCodingEncoded(self, ctx:OGLParser.LineCodingEncodedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#coded_line.
    def visitCoded_line(self, ctx:OGLParser.Coded_lineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#patternName.
    def visitPatternName(self, ctx:OGLParser.PatternNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#settextCommand.
    def visitSettextCommand(self, ctx:OGLParser.SettextCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#settextFormat.
    def visitSettextFormat(self, ctx:OGLParser.SettextFormatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#settextFormatModern.
    def visitSettextFormatModern(self, ctx:OGLParser.SettextFormatModernContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#settextFormatPlacement.
    def visitSettextFormatPlacement(self, ctx:OGLParser.SettextFormatPlacementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#settextFormatColumn.
    def visitSettextFormatColumn(self, ctx:OGLParser.SettextFormatColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#settextAlignment.
    def visitSettextAlignment(self, ctx:OGLParser.SettextAlignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#settextAlignmentAuto.
    def visitSettextAlignmentAuto(self, ctx:OGLParser.SettextAlignmentAutoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#settextAlignmentSpaced.
    def visitSettextAlignmentSpaced(self, ctx:OGLParser.SettextAlignmentSpacedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#settextAlignmentValue.
    def visitSettextAlignmentValue(self, ctx:OGLParser.SettextAlignmentValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#setunitsCommand.
    def visitSetunitsCommand(self, ctx:OGLParser.SetunitsCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#setunitsDefault.
    def visitSetunitsDefault(self, ctx:OGLParser.SetunitsDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#primaryDefault.
    def visitPrimaryDefault(self, ctx:OGLParser.PrimaryDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#secondaryDefault.
    def visitSecondaryDefault(self, ctx:OGLParser.SecondaryDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#setunitsLineSp.
    def visitSetunitsLineSp(self, ctx:OGLParser.SetunitsLineSpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#setunitsCornerLength.
    def visitSetunitsCornerLength(self, ctx:OGLParser.SetunitsCornerLengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#conrnerLengthValue.
    def visitConrnerLengthValue(self, ctx:OGLParser.ConrnerLengthValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#setunitsTextMargin.
    def visitSetunitsTextMargin(self, ctx:OGLParser.SetunitsTextMarginContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#textMarginValue.
    def visitTextMarginValue(self, ctx:OGLParser.TextMarginValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#setUnitsPositioning.
    def visitSetUnitsPositioning(self, ctx:OGLParser.SetUnitsPositioningContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#positionValue.
    def visitPositionValue(self, ctx:OGLParser.PositionValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#placeCommand.
    def visitPlaceCommand(self, ctx:OGLParser.PlaceCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#drawruleCommand.
    def visitDrawruleCommand(self, ctx:OGLParser.DrawruleCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#ruleDirection.
    def visitRuleDirection(self, ctx:OGLParser.RuleDirectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#ruleLength.
    def visitRuleLength(self, ctx:OGLParser.RuleLengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#ruleThickness.
    def visitRuleThickness(self, ctx:OGLParser.RuleThicknessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#ruleType.
    def visitRuleType(self, ctx:OGLParser.RuleTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#ruleRepeated.
    def visitRuleRepeated(self, ctx:OGLParser.RuleRepeatedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#ruleRepeatAcross.
    def visitRuleRepeatAcross(self, ctx:OGLParser.RuleRepeatAcrossContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#ruleRepetition.
    def visitRuleRepetition(self, ctx:OGLParser.RuleRepetitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#ruleRepeatLocation.
    def visitRuleRepeatLocation(self, ctx:OGLParser.RuleRepeatLocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#ruleRepeatVerticalCoordinate.
    def visitRuleRepeatVerticalCoordinate(self, ctx:OGLParser.RuleRepeatVerticalCoordinateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#ruleRepeatHorizonalCoordinate.
    def visitRuleRepeatHorizonalCoordinate(self, ctx:OGLParser.RuleRepeatHorizonalCoordinateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#drawboxCommand.
    def visitDrawboxCommand(self, ctx:OGLParser.DrawboxCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#boxWidth.
    def visitBoxWidth(self, ctx:OGLParser.BoxWidthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#boxHeight.
    def visitBoxHeight(self, ctx:OGLParser.BoxHeightContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#boxBorderThickness.
    def visitBoxBorderThickness(self, ctx:OGLParser.BoxBorderThicknessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#boxBorderType.
    def visitBoxBorderType(self, ctx:OGLParser.BoxBorderTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#boxRounded.
    def visitBoxRounded(self, ctx:OGLParser.BoxRoundedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#boxRoundedOption.
    def visitBoxRoundedOption(self, ctx:OGLParser.BoxRoundedOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#boxDiagonal.
    def visitBoxDiagonal(self, ctx:OGLParser.BoxDiagonalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#boxDiagonalOption.
    def visitBoxDiagonalOption(self, ctx:OGLParser.BoxDiagonalOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#boxRepeat.
    def visitBoxRepeat(self, ctx:OGLParser.BoxRepeatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#boxRepeatLocation.
    def visitBoxRepeatLocation(self, ctx:OGLParser.BoxRepeatLocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#boxRepeatVerticalCoordinate.
    def visitBoxRepeatVerticalCoordinate(self, ctx:OGLParser.BoxRepeatVerticalCoordinateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#boxRepeatHorizonalCoordinate.
    def visitBoxRepeatHorizonalCoordinate(self, ctx:OGLParser.BoxRepeatHorizonalCoordinateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#boxRepeatAcrossDown.
    def visitBoxRepeatAcrossDown(self, ctx:OGLParser.BoxRepeatAcrossDownContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#boxRepetition.
    def visitBoxRepetition(self, ctx:OGLParser.BoxRepetitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#boxRepeatSpaced.
    def visitBoxRepeatSpaced(self, ctx:OGLParser.BoxRepeatSpacedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#spacedValue.
    def visitSpacedValue(self, ctx:OGLParser.SpacedValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#boxShade.
    def visitBoxShade(self, ctx:OGLParser.BoxShadeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#box.
    def visitBox(self, ctx:OGLParser.BoxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#shadeArea.
    def visitShadeArea(self, ctx:OGLParser.ShadeAreaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#shadePattern.
    def visitShadePattern(self, ctx:OGLParser.ShadePatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#shadeType.
    def visitShadeType(self, ctx:OGLParser.ShadeTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#boxColor.
    def visitBoxColor(self, ctx:OGLParser.BoxColorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#boxColorName.
    def visitBoxColorName(self, ctx:OGLParser.BoxColorNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#boxWithtext.
    def visitBoxWithtext(self, ctx:OGLParser.BoxWithtextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#boxWithtextOrient.
    def visitBoxWithtextOrient(self, ctx:OGLParser.BoxWithtextOrientContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#boxWithtextLineSpacing.
    def visitBoxWithtextLineSpacing(self, ctx:OGLParser.BoxWithtextLineSpacingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#line.
    def visitLine(self, ctx:OGLParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#line_part.
    def visitLine_part(self, ctx:OGLParser.Line_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#text.
    def visitText(self, ctx:OGLParser.TextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#lineSosiMode.
    def visitLineSosiMode(self, ctx:OGLParser.LineSosiModeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#lineUnderlying.
    def visitLineUnderlying(self, ctx:OGLParser.LineUnderlyingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#lineTextType.
    def visitLineTextType(self, ctx:OGLParser.LineTextTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#boxWithtextFormat.
    def visitBoxWithtextFormat(self, ctx:OGLParser.BoxWithtextFormatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#boxWithtextFormatModern.
    def visitBoxWithtextFormatModern(self, ctx:OGLParser.BoxWithtextFormatModernContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#boxWithtextFormatPlacement.
    def visitBoxWithtextFormatPlacement(self, ctx:OGLParser.BoxWithtextFormatPlacementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#boxWithtextFormatColumn.
    def visitBoxWithtextFormatColumn(self, ctx:OGLParser.BoxWithtextFormatColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#positionCommand.
    def visitPositionCommand(self, ctx:OGLParser.PositionCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#positionX.
    def visitPositionX(self, ctx:OGLParser.PositionXContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#positionY.
    def visitPositionY(self, ctx:OGLParser.PositionYContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#controlCommand.
    def visitControlCommand(self, ctx:OGLParser.ControlCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#controlStorage.
    def visitControlStorage(self, ctx:OGLParser.ControlStorageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#controlMessage.
    def visitControlMessage(self, ctx:OGLParser.ControlMessageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#controlSummary.
    def visitControlSummary(self, ctx:OGLParser.ControlSummaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#controlSosiOption.
    def visitControlSosiOption(self, ctx:OGLParser.ControlSosiOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#overlayCommand.
    def visitOverlayCommand(self, ctx:OGLParser.OverlayCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#overlayName.
    def visitOverlayName(self, ctx:OGLParser.OverlayNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#overlayWidth.
    def visitOverlayWidth(self, ctx:OGLParser.OverlayWidthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#overlayHeight.
    def visitOverlayHeight(self, ctx:OGLParser.OverlayHeightContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#overlayHorizonalCoordinate.
    def visitOverlayHorizonalCoordinate(self, ctx:OGLParser.OverlayHorizonalCoordinateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#overlayVerticalCoordinate.
    def visitOverlayVerticalCoordinate(self, ctx:OGLParser.OverlayVerticalCoordinateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#orientCommand.
    def visitOrientCommand(self, ctx:OGLParser.OrientCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#orientRotatedDegree.
    def visitOrientRotatedDegree(self, ctx:OGLParser.OrientRotatedDegreeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#fontCommand.
    def visitFontCommand(self, ctx:OGLParser.FontCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#fontCommandMVS.
    def visitFontCommandMVS(self, ctx:OGLParser.FontCommandMVSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#fontCommandVM.
    def visitFontCommandVM(self, ctx:OGLParser.FontCommandVMContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#fontFileType.
    def visitFontFileType(self, ctx:OGLParser.FontFileTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#fileTypeName.
    def visitFileTypeName(self, ctx:OGLParser.FileTypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#fontWithMemID.
    def visitFontWithMemID(self, ctx:OGLParser.FontWithMemIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#fontWithCharSet.
    def visitFontWithCharSet(self, ctx:OGLParser.FontWithCharSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#fontDDName.
    def visitFontDDName(self, ctx:OGLParser.FontDDNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#ddNameName.
    def visitDdNameName(self, ctx:OGLParser.DdNameNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#fontHeight.
    def visitFontHeight(self, ctx:OGLParser.FontHeightContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#fontScale.
    def visitFontScale(self, ctx:OGLParser.FontScaleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#fontColor.
    def visitFontColor(self, ctx:OGLParser.FontColorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#fontUColor.
    def visitFontUColor(self, ctx:OGLParser.FontUColorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#fontColorName.
    def visitFontColorName(self, ctx:OGLParser.FontColorNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#fontName.
    def visitFontName(self, ctx:OGLParser.FontNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#memId.
    def visitMemId(self, ctx:OGLParser.MemIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#charSetName.
    def visitCharSetName(self, ctx:OGLParser.CharSetNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#codePageName.
    def visitCodePageName(self, ctx:OGLParser.CodePageNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#defineGroupCommand.
    def visitDefineGroupCommand(self, ctx:OGLParser.DefineGroupCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#groupName.
    def visitGroupName(self, ctx:OGLParser.GroupNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OGLParser#oglMeasurement.
    def visitOglMeasurement(self, ctx:OGLParser.OglMeasurementContext):
        return self.visitChildren(ctx)



del OGLParser