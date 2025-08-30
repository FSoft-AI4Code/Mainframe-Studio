# Generated from grammar/ogl/OGL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .OGLParser import OGLParser
else:
    from OGLParser import OGLParser

# This class defines a complete listener for a parse tree produced by OGLParser.
class OGLListener(ParseTreeListener):

    # Enter a parse tree produced by OGLParser#startRule.
    def enterStartRule(self, ctx:OGLParser.StartRuleContext):
        pass

    # Exit a parse tree produced by OGLParser#startRule.
    def exitStartRule(self, ctx:OGLParser.StartRuleContext):
        pass


    # Enter a parse tree produced by OGLParser#command.
    def enterCommand(self, ctx:OGLParser.CommandContext):
        pass

    # Exit a parse tree produced by OGLParser#command.
    def exitCommand(self, ctx:OGLParser.CommandContext):
        pass


    # Enter a parse tree produced by OGLParser#segmentCommand.
    def enterSegmentCommand(self, ctx:OGLParser.SegmentCommandContext):
        pass

    # Exit a parse tree produced by OGLParser#segmentCommand.
    def exitSegmentCommand(self, ctx:OGLParser.SegmentCommandContext):
        pass


    # Enter a parse tree produced by OGLParser#segmentName.
    def enterSegmentName(self, ctx:OGLParser.SegmentNameContext):
        pass

    # Exit a parse tree produced by OGLParser#segmentName.
    def exitSegmentName(self, ctx:OGLParser.SegmentNameContext):
        pass


    # Enter a parse tree produced by OGLParser#segmentDDName.
    def enterSegmentDDName(self, ctx:OGLParser.SegmentDDNameContext):
        pass

    # Exit a parse tree produced by OGLParser#segmentDDName.
    def exitSegmentDDName(self, ctx:OGLParser.SegmentDDNameContext):
        pass


    # Enter a parse tree produced by OGLParser#segmentDDNameName.
    def enterSegmentDDNameName(self, ctx:OGLParser.SegmentDDNameNameContext):
        pass

    # Exit a parse tree produced by OGLParser#segmentDDNameName.
    def exitSegmentDDNameName(self, ctx:OGLParser.SegmentDDNameNameContext):
        pass


    # Enter a parse tree produced by OGLParser#segmentFileType.
    def enterSegmentFileType(self, ctx:OGLParser.SegmentFileTypeContext):
        pass

    # Exit a parse tree produced by OGLParser#segmentFileType.
    def exitSegmentFileType(self, ctx:OGLParser.SegmentFileTypeContext):
        pass


    # Enter a parse tree produced by OGLParser#placePatternCommand.
    def enterPlacePatternCommand(self, ctx:OGLParser.PlacePatternCommandContext):
        pass

    # Exit a parse tree produced by OGLParser#placePatternCommand.
    def exitPlacePatternCommand(self, ctx:OGLParser.PlacePatternCommandContext):
        pass


    # Enter a parse tree produced by OGLParser#patternColor.
    def enterPatternColor(self, ctx:OGLParser.PatternColorContext):
        pass

    # Exit a parse tree produced by OGLParser#patternColor.
    def exitPatternColor(self, ctx:OGLParser.PatternColorContext):
        pass


    # Enter a parse tree produced by OGLParser#patternColorName.
    def enterPatternColorName(self, ctx:OGLParser.PatternColorNameContext):
        pass

    # Exit a parse tree produced by OGLParser#patternColorName.
    def exitPatternColorName(self, ctx:OGLParser.PatternColorNameContext):
        pass


    # Enter a parse tree produced by OGLParser#mirrorOption.
    def enterMirrorOption(self, ctx:OGLParser.MirrorOptionContext):
        pass

    # Exit a parse tree produced by OGLParser#mirrorOption.
    def exitMirrorOption(self, ctx:OGLParser.MirrorOptionContext):
        pass


    # Enter a parse tree produced by OGLParser#negativeOption.
    def enterNegativeOption(self, ctx:OGLParser.NegativeOptionContext):
        pass

    # Exit a parse tree produced by OGLParser#negativeOption.
    def exitNegativeOption(self, ctx:OGLParser.NegativeOptionContext):
        pass


    # Enter a parse tree produced by OGLParser#patternShade.
    def enterPatternShade(self, ctx:OGLParser.PatternShadeContext):
        pass

    # Exit a parse tree produced by OGLParser#patternShade.
    def exitPatternShade(self, ctx:OGLParser.PatternShadeContext):
        pass


    # Enter a parse tree produced by OGLParser#definepatternCommand.
    def enterDefinepatternCommand(self, ctx:OGLParser.DefinepatternCommandContext):
        pass

    # Exit a parse tree produced by OGLParser#definepatternCommand.
    def exitDefinepatternCommand(self, ctx:OGLParser.DefinepatternCommandContext):
        pass


    # Enter a parse tree produced by OGLParser#lineCoding.
    def enterLineCoding(self, ctx:OGLParser.LineCodingContext):
        pass

    # Exit a parse tree produced by OGLParser#lineCoding.
    def exitLineCoding(self, ctx:OGLParser.LineCodingContext):
        pass


    # Enter a parse tree produced by OGLParser#lineCodingPels.
    def enterLineCodingPels(self, ctx:OGLParser.LineCodingPelsContext):
        pass

    # Exit a parse tree produced by OGLParser#lineCodingPels.
    def exitLineCodingPels(self, ctx:OGLParser.LineCodingPelsContext):
        pass


    # Enter a parse tree produced by OGLParser#lineCodingEncoded.
    def enterLineCodingEncoded(self, ctx:OGLParser.LineCodingEncodedContext):
        pass

    # Exit a parse tree produced by OGLParser#lineCodingEncoded.
    def exitLineCodingEncoded(self, ctx:OGLParser.LineCodingEncodedContext):
        pass


    # Enter a parse tree produced by OGLParser#coded_line.
    def enterCoded_line(self, ctx:OGLParser.Coded_lineContext):
        pass

    # Exit a parse tree produced by OGLParser#coded_line.
    def exitCoded_line(self, ctx:OGLParser.Coded_lineContext):
        pass


    # Enter a parse tree produced by OGLParser#patternName.
    def enterPatternName(self, ctx:OGLParser.PatternNameContext):
        pass

    # Exit a parse tree produced by OGLParser#patternName.
    def exitPatternName(self, ctx:OGLParser.PatternNameContext):
        pass


    # Enter a parse tree produced by OGLParser#settextCommand.
    def enterSettextCommand(self, ctx:OGLParser.SettextCommandContext):
        pass

    # Exit a parse tree produced by OGLParser#settextCommand.
    def exitSettextCommand(self, ctx:OGLParser.SettextCommandContext):
        pass


    # Enter a parse tree produced by OGLParser#settextFormat.
    def enterSettextFormat(self, ctx:OGLParser.SettextFormatContext):
        pass

    # Exit a parse tree produced by OGLParser#settextFormat.
    def exitSettextFormat(self, ctx:OGLParser.SettextFormatContext):
        pass


    # Enter a parse tree produced by OGLParser#settextFormatModern.
    def enterSettextFormatModern(self, ctx:OGLParser.SettextFormatModernContext):
        pass

    # Exit a parse tree produced by OGLParser#settextFormatModern.
    def exitSettextFormatModern(self, ctx:OGLParser.SettextFormatModernContext):
        pass


    # Enter a parse tree produced by OGLParser#settextFormatPlacement.
    def enterSettextFormatPlacement(self, ctx:OGLParser.SettextFormatPlacementContext):
        pass

    # Exit a parse tree produced by OGLParser#settextFormatPlacement.
    def exitSettextFormatPlacement(self, ctx:OGLParser.SettextFormatPlacementContext):
        pass


    # Enter a parse tree produced by OGLParser#settextFormatColumn.
    def enterSettextFormatColumn(self, ctx:OGLParser.SettextFormatColumnContext):
        pass

    # Exit a parse tree produced by OGLParser#settextFormatColumn.
    def exitSettextFormatColumn(self, ctx:OGLParser.SettextFormatColumnContext):
        pass


    # Enter a parse tree produced by OGLParser#settextAlignment.
    def enterSettextAlignment(self, ctx:OGLParser.SettextAlignmentContext):
        pass

    # Exit a parse tree produced by OGLParser#settextAlignment.
    def exitSettextAlignment(self, ctx:OGLParser.SettextAlignmentContext):
        pass


    # Enter a parse tree produced by OGLParser#settextAlignmentAuto.
    def enterSettextAlignmentAuto(self, ctx:OGLParser.SettextAlignmentAutoContext):
        pass

    # Exit a parse tree produced by OGLParser#settextAlignmentAuto.
    def exitSettextAlignmentAuto(self, ctx:OGLParser.SettextAlignmentAutoContext):
        pass


    # Enter a parse tree produced by OGLParser#settextAlignmentSpaced.
    def enterSettextAlignmentSpaced(self, ctx:OGLParser.SettextAlignmentSpacedContext):
        pass

    # Exit a parse tree produced by OGLParser#settextAlignmentSpaced.
    def exitSettextAlignmentSpaced(self, ctx:OGLParser.SettextAlignmentSpacedContext):
        pass


    # Enter a parse tree produced by OGLParser#settextAlignmentValue.
    def enterSettextAlignmentValue(self, ctx:OGLParser.SettextAlignmentValueContext):
        pass

    # Exit a parse tree produced by OGLParser#settextAlignmentValue.
    def exitSettextAlignmentValue(self, ctx:OGLParser.SettextAlignmentValueContext):
        pass


    # Enter a parse tree produced by OGLParser#setunitsCommand.
    def enterSetunitsCommand(self, ctx:OGLParser.SetunitsCommandContext):
        pass

    # Exit a parse tree produced by OGLParser#setunitsCommand.
    def exitSetunitsCommand(self, ctx:OGLParser.SetunitsCommandContext):
        pass


    # Enter a parse tree produced by OGLParser#setunitsDefault.
    def enterSetunitsDefault(self, ctx:OGLParser.SetunitsDefaultContext):
        pass

    # Exit a parse tree produced by OGLParser#setunitsDefault.
    def exitSetunitsDefault(self, ctx:OGLParser.SetunitsDefaultContext):
        pass


    # Enter a parse tree produced by OGLParser#primaryDefault.
    def enterPrimaryDefault(self, ctx:OGLParser.PrimaryDefaultContext):
        pass

    # Exit a parse tree produced by OGLParser#primaryDefault.
    def exitPrimaryDefault(self, ctx:OGLParser.PrimaryDefaultContext):
        pass


    # Enter a parse tree produced by OGLParser#secondaryDefault.
    def enterSecondaryDefault(self, ctx:OGLParser.SecondaryDefaultContext):
        pass

    # Exit a parse tree produced by OGLParser#secondaryDefault.
    def exitSecondaryDefault(self, ctx:OGLParser.SecondaryDefaultContext):
        pass


    # Enter a parse tree produced by OGLParser#setunitsLineSp.
    def enterSetunitsLineSp(self, ctx:OGLParser.SetunitsLineSpContext):
        pass

    # Exit a parse tree produced by OGLParser#setunitsLineSp.
    def exitSetunitsLineSp(self, ctx:OGLParser.SetunitsLineSpContext):
        pass


    # Enter a parse tree produced by OGLParser#setunitsCornerLength.
    def enterSetunitsCornerLength(self, ctx:OGLParser.SetunitsCornerLengthContext):
        pass

    # Exit a parse tree produced by OGLParser#setunitsCornerLength.
    def exitSetunitsCornerLength(self, ctx:OGLParser.SetunitsCornerLengthContext):
        pass


    # Enter a parse tree produced by OGLParser#conrnerLengthValue.
    def enterConrnerLengthValue(self, ctx:OGLParser.ConrnerLengthValueContext):
        pass

    # Exit a parse tree produced by OGLParser#conrnerLengthValue.
    def exitConrnerLengthValue(self, ctx:OGLParser.ConrnerLengthValueContext):
        pass


    # Enter a parse tree produced by OGLParser#setunitsTextMargin.
    def enterSetunitsTextMargin(self, ctx:OGLParser.SetunitsTextMarginContext):
        pass

    # Exit a parse tree produced by OGLParser#setunitsTextMargin.
    def exitSetunitsTextMargin(self, ctx:OGLParser.SetunitsTextMarginContext):
        pass


    # Enter a parse tree produced by OGLParser#textMarginValue.
    def enterTextMarginValue(self, ctx:OGLParser.TextMarginValueContext):
        pass

    # Exit a parse tree produced by OGLParser#textMarginValue.
    def exitTextMarginValue(self, ctx:OGLParser.TextMarginValueContext):
        pass


    # Enter a parse tree produced by OGLParser#setUnitsPositioning.
    def enterSetUnitsPositioning(self, ctx:OGLParser.SetUnitsPositioningContext):
        pass

    # Exit a parse tree produced by OGLParser#setUnitsPositioning.
    def exitSetUnitsPositioning(self, ctx:OGLParser.SetUnitsPositioningContext):
        pass


    # Enter a parse tree produced by OGLParser#positionValue.
    def enterPositionValue(self, ctx:OGLParser.PositionValueContext):
        pass

    # Exit a parse tree produced by OGLParser#positionValue.
    def exitPositionValue(self, ctx:OGLParser.PositionValueContext):
        pass


    # Enter a parse tree produced by OGLParser#placeCommand.
    def enterPlaceCommand(self, ctx:OGLParser.PlaceCommandContext):
        pass

    # Exit a parse tree produced by OGLParser#placeCommand.
    def exitPlaceCommand(self, ctx:OGLParser.PlaceCommandContext):
        pass


    # Enter a parse tree produced by OGLParser#drawruleCommand.
    def enterDrawruleCommand(self, ctx:OGLParser.DrawruleCommandContext):
        pass

    # Exit a parse tree produced by OGLParser#drawruleCommand.
    def exitDrawruleCommand(self, ctx:OGLParser.DrawruleCommandContext):
        pass


    # Enter a parse tree produced by OGLParser#ruleDirection.
    def enterRuleDirection(self, ctx:OGLParser.RuleDirectionContext):
        pass

    # Exit a parse tree produced by OGLParser#ruleDirection.
    def exitRuleDirection(self, ctx:OGLParser.RuleDirectionContext):
        pass


    # Enter a parse tree produced by OGLParser#ruleLength.
    def enterRuleLength(self, ctx:OGLParser.RuleLengthContext):
        pass

    # Exit a parse tree produced by OGLParser#ruleLength.
    def exitRuleLength(self, ctx:OGLParser.RuleLengthContext):
        pass


    # Enter a parse tree produced by OGLParser#ruleThickness.
    def enterRuleThickness(self, ctx:OGLParser.RuleThicknessContext):
        pass

    # Exit a parse tree produced by OGLParser#ruleThickness.
    def exitRuleThickness(self, ctx:OGLParser.RuleThicknessContext):
        pass


    # Enter a parse tree produced by OGLParser#ruleType.
    def enterRuleType(self, ctx:OGLParser.RuleTypeContext):
        pass

    # Exit a parse tree produced by OGLParser#ruleType.
    def exitRuleType(self, ctx:OGLParser.RuleTypeContext):
        pass


    # Enter a parse tree produced by OGLParser#ruleRepeated.
    def enterRuleRepeated(self, ctx:OGLParser.RuleRepeatedContext):
        pass

    # Exit a parse tree produced by OGLParser#ruleRepeated.
    def exitRuleRepeated(self, ctx:OGLParser.RuleRepeatedContext):
        pass


    # Enter a parse tree produced by OGLParser#ruleRepeatAcross.
    def enterRuleRepeatAcross(self, ctx:OGLParser.RuleRepeatAcrossContext):
        pass

    # Exit a parse tree produced by OGLParser#ruleRepeatAcross.
    def exitRuleRepeatAcross(self, ctx:OGLParser.RuleRepeatAcrossContext):
        pass


    # Enter a parse tree produced by OGLParser#ruleRepetition.
    def enterRuleRepetition(self, ctx:OGLParser.RuleRepetitionContext):
        pass

    # Exit a parse tree produced by OGLParser#ruleRepetition.
    def exitRuleRepetition(self, ctx:OGLParser.RuleRepetitionContext):
        pass


    # Enter a parse tree produced by OGLParser#ruleRepeatLocation.
    def enterRuleRepeatLocation(self, ctx:OGLParser.RuleRepeatLocationContext):
        pass

    # Exit a parse tree produced by OGLParser#ruleRepeatLocation.
    def exitRuleRepeatLocation(self, ctx:OGLParser.RuleRepeatLocationContext):
        pass


    # Enter a parse tree produced by OGLParser#ruleRepeatVerticalCoordinate.
    def enterRuleRepeatVerticalCoordinate(self, ctx:OGLParser.RuleRepeatVerticalCoordinateContext):
        pass

    # Exit a parse tree produced by OGLParser#ruleRepeatVerticalCoordinate.
    def exitRuleRepeatVerticalCoordinate(self, ctx:OGLParser.RuleRepeatVerticalCoordinateContext):
        pass


    # Enter a parse tree produced by OGLParser#ruleRepeatHorizonalCoordinate.
    def enterRuleRepeatHorizonalCoordinate(self, ctx:OGLParser.RuleRepeatHorizonalCoordinateContext):
        pass

    # Exit a parse tree produced by OGLParser#ruleRepeatHorizonalCoordinate.
    def exitRuleRepeatHorizonalCoordinate(self, ctx:OGLParser.RuleRepeatHorizonalCoordinateContext):
        pass


    # Enter a parse tree produced by OGLParser#drawboxCommand.
    def enterDrawboxCommand(self, ctx:OGLParser.DrawboxCommandContext):
        pass

    # Exit a parse tree produced by OGLParser#drawboxCommand.
    def exitDrawboxCommand(self, ctx:OGLParser.DrawboxCommandContext):
        pass


    # Enter a parse tree produced by OGLParser#boxWidth.
    def enterBoxWidth(self, ctx:OGLParser.BoxWidthContext):
        pass

    # Exit a parse tree produced by OGLParser#boxWidth.
    def exitBoxWidth(self, ctx:OGLParser.BoxWidthContext):
        pass


    # Enter a parse tree produced by OGLParser#boxHeight.
    def enterBoxHeight(self, ctx:OGLParser.BoxHeightContext):
        pass

    # Exit a parse tree produced by OGLParser#boxHeight.
    def exitBoxHeight(self, ctx:OGLParser.BoxHeightContext):
        pass


    # Enter a parse tree produced by OGLParser#boxBorderThickness.
    def enterBoxBorderThickness(self, ctx:OGLParser.BoxBorderThicknessContext):
        pass

    # Exit a parse tree produced by OGLParser#boxBorderThickness.
    def exitBoxBorderThickness(self, ctx:OGLParser.BoxBorderThicknessContext):
        pass


    # Enter a parse tree produced by OGLParser#boxBorderType.
    def enterBoxBorderType(self, ctx:OGLParser.BoxBorderTypeContext):
        pass

    # Exit a parse tree produced by OGLParser#boxBorderType.
    def exitBoxBorderType(self, ctx:OGLParser.BoxBorderTypeContext):
        pass


    # Enter a parse tree produced by OGLParser#boxRounded.
    def enterBoxRounded(self, ctx:OGLParser.BoxRoundedContext):
        pass

    # Exit a parse tree produced by OGLParser#boxRounded.
    def exitBoxRounded(self, ctx:OGLParser.BoxRoundedContext):
        pass


    # Enter a parse tree produced by OGLParser#boxRoundedOption.
    def enterBoxRoundedOption(self, ctx:OGLParser.BoxRoundedOptionContext):
        pass

    # Exit a parse tree produced by OGLParser#boxRoundedOption.
    def exitBoxRoundedOption(self, ctx:OGLParser.BoxRoundedOptionContext):
        pass


    # Enter a parse tree produced by OGLParser#boxDiagonal.
    def enterBoxDiagonal(self, ctx:OGLParser.BoxDiagonalContext):
        pass

    # Exit a parse tree produced by OGLParser#boxDiagonal.
    def exitBoxDiagonal(self, ctx:OGLParser.BoxDiagonalContext):
        pass


    # Enter a parse tree produced by OGLParser#boxDiagonalOption.
    def enterBoxDiagonalOption(self, ctx:OGLParser.BoxDiagonalOptionContext):
        pass

    # Exit a parse tree produced by OGLParser#boxDiagonalOption.
    def exitBoxDiagonalOption(self, ctx:OGLParser.BoxDiagonalOptionContext):
        pass


    # Enter a parse tree produced by OGLParser#boxRepeat.
    def enterBoxRepeat(self, ctx:OGLParser.BoxRepeatContext):
        pass

    # Exit a parse tree produced by OGLParser#boxRepeat.
    def exitBoxRepeat(self, ctx:OGLParser.BoxRepeatContext):
        pass


    # Enter a parse tree produced by OGLParser#boxRepeatLocation.
    def enterBoxRepeatLocation(self, ctx:OGLParser.BoxRepeatLocationContext):
        pass

    # Exit a parse tree produced by OGLParser#boxRepeatLocation.
    def exitBoxRepeatLocation(self, ctx:OGLParser.BoxRepeatLocationContext):
        pass


    # Enter a parse tree produced by OGLParser#boxRepeatVerticalCoordinate.
    def enterBoxRepeatVerticalCoordinate(self, ctx:OGLParser.BoxRepeatVerticalCoordinateContext):
        pass

    # Exit a parse tree produced by OGLParser#boxRepeatVerticalCoordinate.
    def exitBoxRepeatVerticalCoordinate(self, ctx:OGLParser.BoxRepeatVerticalCoordinateContext):
        pass


    # Enter a parse tree produced by OGLParser#boxRepeatHorizonalCoordinate.
    def enterBoxRepeatHorizonalCoordinate(self, ctx:OGLParser.BoxRepeatHorizonalCoordinateContext):
        pass

    # Exit a parse tree produced by OGLParser#boxRepeatHorizonalCoordinate.
    def exitBoxRepeatHorizonalCoordinate(self, ctx:OGLParser.BoxRepeatHorizonalCoordinateContext):
        pass


    # Enter a parse tree produced by OGLParser#boxRepeatAcrossDown.
    def enterBoxRepeatAcrossDown(self, ctx:OGLParser.BoxRepeatAcrossDownContext):
        pass

    # Exit a parse tree produced by OGLParser#boxRepeatAcrossDown.
    def exitBoxRepeatAcrossDown(self, ctx:OGLParser.BoxRepeatAcrossDownContext):
        pass


    # Enter a parse tree produced by OGLParser#boxRepetition.
    def enterBoxRepetition(self, ctx:OGLParser.BoxRepetitionContext):
        pass

    # Exit a parse tree produced by OGLParser#boxRepetition.
    def exitBoxRepetition(self, ctx:OGLParser.BoxRepetitionContext):
        pass


    # Enter a parse tree produced by OGLParser#boxRepeatSpaced.
    def enterBoxRepeatSpaced(self, ctx:OGLParser.BoxRepeatSpacedContext):
        pass

    # Exit a parse tree produced by OGLParser#boxRepeatSpaced.
    def exitBoxRepeatSpaced(self, ctx:OGLParser.BoxRepeatSpacedContext):
        pass


    # Enter a parse tree produced by OGLParser#spacedValue.
    def enterSpacedValue(self, ctx:OGLParser.SpacedValueContext):
        pass

    # Exit a parse tree produced by OGLParser#spacedValue.
    def exitSpacedValue(self, ctx:OGLParser.SpacedValueContext):
        pass


    # Enter a parse tree produced by OGLParser#boxShade.
    def enterBoxShade(self, ctx:OGLParser.BoxShadeContext):
        pass

    # Exit a parse tree produced by OGLParser#boxShade.
    def exitBoxShade(self, ctx:OGLParser.BoxShadeContext):
        pass


    # Enter a parse tree produced by OGLParser#box.
    def enterBox(self, ctx:OGLParser.BoxContext):
        pass

    # Exit a parse tree produced by OGLParser#box.
    def exitBox(self, ctx:OGLParser.BoxContext):
        pass


    # Enter a parse tree produced by OGLParser#shadeArea.
    def enterShadeArea(self, ctx:OGLParser.ShadeAreaContext):
        pass

    # Exit a parse tree produced by OGLParser#shadeArea.
    def exitShadeArea(self, ctx:OGLParser.ShadeAreaContext):
        pass


    # Enter a parse tree produced by OGLParser#shadePattern.
    def enterShadePattern(self, ctx:OGLParser.ShadePatternContext):
        pass

    # Exit a parse tree produced by OGLParser#shadePattern.
    def exitShadePattern(self, ctx:OGLParser.ShadePatternContext):
        pass


    # Enter a parse tree produced by OGLParser#shadeType.
    def enterShadeType(self, ctx:OGLParser.ShadeTypeContext):
        pass

    # Exit a parse tree produced by OGLParser#shadeType.
    def exitShadeType(self, ctx:OGLParser.ShadeTypeContext):
        pass


    # Enter a parse tree produced by OGLParser#boxColor.
    def enterBoxColor(self, ctx:OGLParser.BoxColorContext):
        pass

    # Exit a parse tree produced by OGLParser#boxColor.
    def exitBoxColor(self, ctx:OGLParser.BoxColorContext):
        pass


    # Enter a parse tree produced by OGLParser#boxColorName.
    def enterBoxColorName(self, ctx:OGLParser.BoxColorNameContext):
        pass

    # Exit a parse tree produced by OGLParser#boxColorName.
    def exitBoxColorName(self, ctx:OGLParser.BoxColorNameContext):
        pass


    # Enter a parse tree produced by OGLParser#boxWithtext.
    def enterBoxWithtext(self, ctx:OGLParser.BoxWithtextContext):
        pass

    # Exit a parse tree produced by OGLParser#boxWithtext.
    def exitBoxWithtext(self, ctx:OGLParser.BoxWithtextContext):
        pass


    # Enter a parse tree produced by OGLParser#boxWithtextOrient.
    def enterBoxWithtextOrient(self, ctx:OGLParser.BoxWithtextOrientContext):
        pass

    # Exit a parse tree produced by OGLParser#boxWithtextOrient.
    def exitBoxWithtextOrient(self, ctx:OGLParser.BoxWithtextOrientContext):
        pass


    # Enter a parse tree produced by OGLParser#boxWithtextLineSpacing.
    def enterBoxWithtextLineSpacing(self, ctx:OGLParser.BoxWithtextLineSpacingContext):
        pass

    # Exit a parse tree produced by OGLParser#boxWithtextLineSpacing.
    def exitBoxWithtextLineSpacing(self, ctx:OGLParser.BoxWithtextLineSpacingContext):
        pass


    # Enter a parse tree produced by OGLParser#line.
    def enterLine(self, ctx:OGLParser.LineContext):
        pass

    # Exit a parse tree produced by OGLParser#line.
    def exitLine(self, ctx:OGLParser.LineContext):
        pass


    # Enter a parse tree produced by OGLParser#line_part.
    def enterLine_part(self, ctx:OGLParser.Line_partContext):
        pass

    # Exit a parse tree produced by OGLParser#line_part.
    def exitLine_part(self, ctx:OGLParser.Line_partContext):
        pass


    # Enter a parse tree produced by OGLParser#text.
    def enterText(self, ctx:OGLParser.TextContext):
        pass

    # Exit a parse tree produced by OGLParser#text.
    def exitText(self, ctx:OGLParser.TextContext):
        pass


    # Enter a parse tree produced by OGLParser#lineSosiMode.
    def enterLineSosiMode(self, ctx:OGLParser.LineSosiModeContext):
        pass

    # Exit a parse tree produced by OGLParser#lineSosiMode.
    def exitLineSosiMode(self, ctx:OGLParser.LineSosiModeContext):
        pass


    # Enter a parse tree produced by OGLParser#lineUnderlying.
    def enterLineUnderlying(self, ctx:OGLParser.LineUnderlyingContext):
        pass

    # Exit a parse tree produced by OGLParser#lineUnderlying.
    def exitLineUnderlying(self, ctx:OGLParser.LineUnderlyingContext):
        pass


    # Enter a parse tree produced by OGLParser#lineTextType.
    def enterLineTextType(self, ctx:OGLParser.LineTextTypeContext):
        pass

    # Exit a parse tree produced by OGLParser#lineTextType.
    def exitLineTextType(self, ctx:OGLParser.LineTextTypeContext):
        pass


    # Enter a parse tree produced by OGLParser#boxWithtextFormat.
    def enterBoxWithtextFormat(self, ctx:OGLParser.BoxWithtextFormatContext):
        pass

    # Exit a parse tree produced by OGLParser#boxWithtextFormat.
    def exitBoxWithtextFormat(self, ctx:OGLParser.BoxWithtextFormatContext):
        pass


    # Enter a parse tree produced by OGLParser#boxWithtextFormatModern.
    def enterBoxWithtextFormatModern(self, ctx:OGLParser.BoxWithtextFormatModernContext):
        pass

    # Exit a parse tree produced by OGLParser#boxWithtextFormatModern.
    def exitBoxWithtextFormatModern(self, ctx:OGLParser.BoxWithtextFormatModernContext):
        pass


    # Enter a parse tree produced by OGLParser#boxWithtextFormatPlacement.
    def enterBoxWithtextFormatPlacement(self, ctx:OGLParser.BoxWithtextFormatPlacementContext):
        pass

    # Exit a parse tree produced by OGLParser#boxWithtextFormatPlacement.
    def exitBoxWithtextFormatPlacement(self, ctx:OGLParser.BoxWithtextFormatPlacementContext):
        pass


    # Enter a parse tree produced by OGLParser#boxWithtextFormatColumn.
    def enterBoxWithtextFormatColumn(self, ctx:OGLParser.BoxWithtextFormatColumnContext):
        pass

    # Exit a parse tree produced by OGLParser#boxWithtextFormatColumn.
    def exitBoxWithtextFormatColumn(self, ctx:OGLParser.BoxWithtextFormatColumnContext):
        pass


    # Enter a parse tree produced by OGLParser#positionCommand.
    def enterPositionCommand(self, ctx:OGLParser.PositionCommandContext):
        pass

    # Exit a parse tree produced by OGLParser#positionCommand.
    def exitPositionCommand(self, ctx:OGLParser.PositionCommandContext):
        pass


    # Enter a parse tree produced by OGLParser#positionX.
    def enterPositionX(self, ctx:OGLParser.PositionXContext):
        pass

    # Exit a parse tree produced by OGLParser#positionX.
    def exitPositionX(self, ctx:OGLParser.PositionXContext):
        pass


    # Enter a parse tree produced by OGLParser#positionY.
    def enterPositionY(self, ctx:OGLParser.PositionYContext):
        pass

    # Exit a parse tree produced by OGLParser#positionY.
    def exitPositionY(self, ctx:OGLParser.PositionYContext):
        pass


    # Enter a parse tree produced by OGLParser#controlCommand.
    def enterControlCommand(self, ctx:OGLParser.ControlCommandContext):
        pass

    # Exit a parse tree produced by OGLParser#controlCommand.
    def exitControlCommand(self, ctx:OGLParser.ControlCommandContext):
        pass


    # Enter a parse tree produced by OGLParser#controlStorage.
    def enterControlStorage(self, ctx:OGLParser.ControlStorageContext):
        pass

    # Exit a parse tree produced by OGLParser#controlStorage.
    def exitControlStorage(self, ctx:OGLParser.ControlStorageContext):
        pass


    # Enter a parse tree produced by OGLParser#controlMessage.
    def enterControlMessage(self, ctx:OGLParser.ControlMessageContext):
        pass

    # Exit a parse tree produced by OGLParser#controlMessage.
    def exitControlMessage(self, ctx:OGLParser.ControlMessageContext):
        pass


    # Enter a parse tree produced by OGLParser#controlSummary.
    def enterControlSummary(self, ctx:OGLParser.ControlSummaryContext):
        pass

    # Exit a parse tree produced by OGLParser#controlSummary.
    def exitControlSummary(self, ctx:OGLParser.ControlSummaryContext):
        pass


    # Enter a parse tree produced by OGLParser#controlSosiOption.
    def enterControlSosiOption(self, ctx:OGLParser.ControlSosiOptionContext):
        pass

    # Exit a parse tree produced by OGLParser#controlSosiOption.
    def exitControlSosiOption(self, ctx:OGLParser.ControlSosiOptionContext):
        pass


    # Enter a parse tree produced by OGLParser#overlayCommand.
    def enterOverlayCommand(self, ctx:OGLParser.OverlayCommandContext):
        pass

    # Exit a parse tree produced by OGLParser#overlayCommand.
    def exitOverlayCommand(self, ctx:OGLParser.OverlayCommandContext):
        pass


    # Enter a parse tree produced by OGLParser#overlayName.
    def enterOverlayName(self, ctx:OGLParser.OverlayNameContext):
        pass

    # Exit a parse tree produced by OGLParser#overlayName.
    def exitOverlayName(self, ctx:OGLParser.OverlayNameContext):
        pass


    # Enter a parse tree produced by OGLParser#overlayWidth.
    def enterOverlayWidth(self, ctx:OGLParser.OverlayWidthContext):
        pass

    # Exit a parse tree produced by OGLParser#overlayWidth.
    def exitOverlayWidth(self, ctx:OGLParser.OverlayWidthContext):
        pass


    # Enter a parse tree produced by OGLParser#overlayHeight.
    def enterOverlayHeight(self, ctx:OGLParser.OverlayHeightContext):
        pass

    # Exit a parse tree produced by OGLParser#overlayHeight.
    def exitOverlayHeight(self, ctx:OGLParser.OverlayHeightContext):
        pass


    # Enter a parse tree produced by OGLParser#overlayHorizonalCoordinate.
    def enterOverlayHorizonalCoordinate(self, ctx:OGLParser.OverlayHorizonalCoordinateContext):
        pass

    # Exit a parse tree produced by OGLParser#overlayHorizonalCoordinate.
    def exitOverlayHorizonalCoordinate(self, ctx:OGLParser.OverlayHorizonalCoordinateContext):
        pass


    # Enter a parse tree produced by OGLParser#overlayVerticalCoordinate.
    def enterOverlayVerticalCoordinate(self, ctx:OGLParser.OverlayVerticalCoordinateContext):
        pass

    # Exit a parse tree produced by OGLParser#overlayVerticalCoordinate.
    def exitOverlayVerticalCoordinate(self, ctx:OGLParser.OverlayVerticalCoordinateContext):
        pass


    # Enter a parse tree produced by OGLParser#orientCommand.
    def enterOrientCommand(self, ctx:OGLParser.OrientCommandContext):
        pass

    # Exit a parse tree produced by OGLParser#orientCommand.
    def exitOrientCommand(self, ctx:OGLParser.OrientCommandContext):
        pass


    # Enter a parse tree produced by OGLParser#orientRotatedDegree.
    def enterOrientRotatedDegree(self, ctx:OGLParser.OrientRotatedDegreeContext):
        pass

    # Exit a parse tree produced by OGLParser#orientRotatedDegree.
    def exitOrientRotatedDegree(self, ctx:OGLParser.OrientRotatedDegreeContext):
        pass


    # Enter a parse tree produced by OGLParser#fontCommand.
    def enterFontCommand(self, ctx:OGLParser.FontCommandContext):
        pass

    # Exit a parse tree produced by OGLParser#fontCommand.
    def exitFontCommand(self, ctx:OGLParser.FontCommandContext):
        pass


    # Enter a parse tree produced by OGLParser#fontCommandMVS.
    def enterFontCommandMVS(self, ctx:OGLParser.FontCommandMVSContext):
        pass

    # Exit a parse tree produced by OGLParser#fontCommandMVS.
    def exitFontCommandMVS(self, ctx:OGLParser.FontCommandMVSContext):
        pass


    # Enter a parse tree produced by OGLParser#fontCommandVM.
    def enterFontCommandVM(self, ctx:OGLParser.FontCommandVMContext):
        pass

    # Exit a parse tree produced by OGLParser#fontCommandVM.
    def exitFontCommandVM(self, ctx:OGLParser.FontCommandVMContext):
        pass


    # Enter a parse tree produced by OGLParser#fontFileType.
    def enterFontFileType(self, ctx:OGLParser.FontFileTypeContext):
        pass

    # Exit a parse tree produced by OGLParser#fontFileType.
    def exitFontFileType(self, ctx:OGLParser.FontFileTypeContext):
        pass


    # Enter a parse tree produced by OGLParser#fileTypeName.
    def enterFileTypeName(self, ctx:OGLParser.FileTypeNameContext):
        pass

    # Exit a parse tree produced by OGLParser#fileTypeName.
    def exitFileTypeName(self, ctx:OGLParser.FileTypeNameContext):
        pass


    # Enter a parse tree produced by OGLParser#fontWithMemID.
    def enterFontWithMemID(self, ctx:OGLParser.FontWithMemIDContext):
        pass

    # Exit a parse tree produced by OGLParser#fontWithMemID.
    def exitFontWithMemID(self, ctx:OGLParser.FontWithMemIDContext):
        pass


    # Enter a parse tree produced by OGLParser#fontWithCharSet.
    def enterFontWithCharSet(self, ctx:OGLParser.FontWithCharSetContext):
        pass

    # Exit a parse tree produced by OGLParser#fontWithCharSet.
    def exitFontWithCharSet(self, ctx:OGLParser.FontWithCharSetContext):
        pass


    # Enter a parse tree produced by OGLParser#fontDDName.
    def enterFontDDName(self, ctx:OGLParser.FontDDNameContext):
        pass

    # Exit a parse tree produced by OGLParser#fontDDName.
    def exitFontDDName(self, ctx:OGLParser.FontDDNameContext):
        pass


    # Enter a parse tree produced by OGLParser#ddNameName.
    def enterDdNameName(self, ctx:OGLParser.DdNameNameContext):
        pass

    # Exit a parse tree produced by OGLParser#ddNameName.
    def exitDdNameName(self, ctx:OGLParser.DdNameNameContext):
        pass


    # Enter a parse tree produced by OGLParser#fontHeight.
    def enterFontHeight(self, ctx:OGLParser.FontHeightContext):
        pass

    # Exit a parse tree produced by OGLParser#fontHeight.
    def exitFontHeight(self, ctx:OGLParser.FontHeightContext):
        pass


    # Enter a parse tree produced by OGLParser#fontScale.
    def enterFontScale(self, ctx:OGLParser.FontScaleContext):
        pass

    # Exit a parse tree produced by OGLParser#fontScale.
    def exitFontScale(self, ctx:OGLParser.FontScaleContext):
        pass


    # Enter a parse tree produced by OGLParser#fontColor.
    def enterFontColor(self, ctx:OGLParser.FontColorContext):
        pass

    # Exit a parse tree produced by OGLParser#fontColor.
    def exitFontColor(self, ctx:OGLParser.FontColorContext):
        pass


    # Enter a parse tree produced by OGLParser#fontUColor.
    def enterFontUColor(self, ctx:OGLParser.FontUColorContext):
        pass

    # Exit a parse tree produced by OGLParser#fontUColor.
    def exitFontUColor(self, ctx:OGLParser.FontUColorContext):
        pass


    # Enter a parse tree produced by OGLParser#fontColorName.
    def enterFontColorName(self, ctx:OGLParser.FontColorNameContext):
        pass

    # Exit a parse tree produced by OGLParser#fontColorName.
    def exitFontColorName(self, ctx:OGLParser.FontColorNameContext):
        pass


    # Enter a parse tree produced by OGLParser#fontName.
    def enterFontName(self, ctx:OGLParser.FontNameContext):
        pass

    # Exit a parse tree produced by OGLParser#fontName.
    def exitFontName(self, ctx:OGLParser.FontNameContext):
        pass


    # Enter a parse tree produced by OGLParser#memId.
    def enterMemId(self, ctx:OGLParser.MemIdContext):
        pass

    # Exit a parse tree produced by OGLParser#memId.
    def exitMemId(self, ctx:OGLParser.MemIdContext):
        pass


    # Enter a parse tree produced by OGLParser#charSetName.
    def enterCharSetName(self, ctx:OGLParser.CharSetNameContext):
        pass

    # Exit a parse tree produced by OGLParser#charSetName.
    def exitCharSetName(self, ctx:OGLParser.CharSetNameContext):
        pass


    # Enter a parse tree produced by OGLParser#codePageName.
    def enterCodePageName(self, ctx:OGLParser.CodePageNameContext):
        pass

    # Exit a parse tree produced by OGLParser#codePageName.
    def exitCodePageName(self, ctx:OGLParser.CodePageNameContext):
        pass


    # Enter a parse tree produced by OGLParser#defineGroupCommand.
    def enterDefineGroupCommand(self, ctx:OGLParser.DefineGroupCommandContext):
        pass

    # Exit a parse tree produced by OGLParser#defineGroupCommand.
    def exitDefineGroupCommand(self, ctx:OGLParser.DefineGroupCommandContext):
        pass


    # Enter a parse tree produced by OGLParser#groupName.
    def enterGroupName(self, ctx:OGLParser.GroupNameContext):
        pass

    # Exit a parse tree produced by OGLParser#groupName.
    def exitGroupName(self, ctx:OGLParser.GroupNameContext):
        pass


    # Enter a parse tree produced by OGLParser#oglMeasurement.
    def enterOglMeasurement(self, ctx:OGLParser.OglMeasurementContext):
        pass

    # Exit a parse tree produced by OGLParser#oglMeasurement.
    def exitOglMeasurement(self, ctx:OGLParser.OglMeasurementContext):
        pass



del OGLParser