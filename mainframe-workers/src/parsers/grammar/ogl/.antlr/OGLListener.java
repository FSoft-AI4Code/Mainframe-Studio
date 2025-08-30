// Generated from /home/minhnl11aic/Documents/mainframe-workers/grammar/ogl/OGL.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link OGLParser}.
 */
public interface OGLListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link OGLParser#startRule}.
	 * @param ctx the parse tree
	 */
	void enterStartRule(OGLParser.StartRuleContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#startRule}.
	 * @param ctx the parse tree
	 */
	void exitStartRule(OGLParser.StartRuleContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#command}.
	 * @param ctx the parse tree
	 */
	void enterCommand(OGLParser.CommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#command}.
	 * @param ctx the parse tree
	 */
	void exitCommand(OGLParser.CommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#segmentCommand}.
	 * @param ctx the parse tree
	 */
	void enterSegmentCommand(OGLParser.SegmentCommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#segmentCommand}.
	 * @param ctx the parse tree
	 */
	void exitSegmentCommand(OGLParser.SegmentCommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#segmentName}.
	 * @param ctx the parse tree
	 */
	void enterSegmentName(OGLParser.SegmentNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#segmentName}.
	 * @param ctx the parse tree
	 */
	void exitSegmentName(OGLParser.SegmentNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#segmentDDName}.
	 * @param ctx the parse tree
	 */
	void enterSegmentDDName(OGLParser.SegmentDDNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#segmentDDName}.
	 * @param ctx the parse tree
	 */
	void exitSegmentDDName(OGLParser.SegmentDDNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#segmentDDNameName}.
	 * @param ctx the parse tree
	 */
	void enterSegmentDDNameName(OGLParser.SegmentDDNameNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#segmentDDNameName}.
	 * @param ctx the parse tree
	 */
	void exitSegmentDDNameName(OGLParser.SegmentDDNameNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#segmentFileType}.
	 * @param ctx the parse tree
	 */
	void enterSegmentFileType(OGLParser.SegmentFileTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#segmentFileType}.
	 * @param ctx the parse tree
	 */
	void exitSegmentFileType(OGLParser.SegmentFileTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#placePatternCommand}.
	 * @param ctx the parse tree
	 */
	void enterPlacePatternCommand(OGLParser.PlacePatternCommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#placePatternCommand}.
	 * @param ctx the parse tree
	 */
	void exitPlacePatternCommand(OGLParser.PlacePatternCommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#patternColor}.
	 * @param ctx the parse tree
	 */
	void enterPatternColor(OGLParser.PatternColorContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#patternColor}.
	 * @param ctx the parse tree
	 */
	void exitPatternColor(OGLParser.PatternColorContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#patternColorName}.
	 * @param ctx the parse tree
	 */
	void enterPatternColorName(OGLParser.PatternColorNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#patternColorName}.
	 * @param ctx the parse tree
	 */
	void exitPatternColorName(OGLParser.PatternColorNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#mirrorOption}.
	 * @param ctx the parse tree
	 */
	void enterMirrorOption(OGLParser.MirrorOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#mirrorOption}.
	 * @param ctx the parse tree
	 */
	void exitMirrorOption(OGLParser.MirrorOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#negativeOption}.
	 * @param ctx the parse tree
	 */
	void enterNegativeOption(OGLParser.NegativeOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#negativeOption}.
	 * @param ctx the parse tree
	 */
	void exitNegativeOption(OGLParser.NegativeOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#patternShade}.
	 * @param ctx the parse tree
	 */
	void enterPatternShade(OGLParser.PatternShadeContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#patternShade}.
	 * @param ctx the parse tree
	 */
	void exitPatternShade(OGLParser.PatternShadeContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#definepatternCommand}.
	 * @param ctx the parse tree
	 */
	void enterDefinepatternCommand(OGLParser.DefinepatternCommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#definepatternCommand}.
	 * @param ctx the parse tree
	 */
	void exitDefinepatternCommand(OGLParser.DefinepatternCommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#lineCoding}.
	 * @param ctx the parse tree
	 */
	void enterLineCoding(OGLParser.LineCodingContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#lineCoding}.
	 * @param ctx the parse tree
	 */
	void exitLineCoding(OGLParser.LineCodingContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#lineCodingPels}.
	 * @param ctx the parse tree
	 */
	void enterLineCodingPels(OGLParser.LineCodingPelsContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#lineCodingPels}.
	 * @param ctx the parse tree
	 */
	void exitLineCodingPels(OGLParser.LineCodingPelsContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#lineCodingEncoded}.
	 * @param ctx the parse tree
	 */
	void enterLineCodingEncoded(OGLParser.LineCodingEncodedContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#lineCodingEncoded}.
	 * @param ctx the parse tree
	 */
	void exitLineCodingEncoded(OGLParser.LineCodingEncodedContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#coded_line}.
	 * @param ctx the parse tree
	 */
	void enterCoded_line(OGLParser.Coded_lineContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#coded_line}.
	 * @param ctx the parse tree
	 */
	void exitCoded_line(OGLParser.Coded_lineContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#patternName}.
	 * @param ctx the parse tree
	 */
	void enterPatternName(OGLParser.PatternNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#patternName}.
	 * @param ctx the parse tree
	 */
	void exitPatternName(OGLParser.PatternNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#settextCommand}.
	 * @param ctx the parse tree
	 */
	void enterSettextCommand(OGLParser.SettextCommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#settextCommand}.
	 * @param ctx the parse tree
	 */
	void exitSettextCommand(OGLParser.SettextCommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#settextFormat}.
	 * @param ctx the parse tree
	 */
	void enterSettextFormat(OGLParser.SettextFormatContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#settextFormat}.
	 * @param ctx the parse tree
	 */
	void exitSettextFormat(OGLParser.SettextFormatContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#settextFormatModern}.
	 * @param ctx the parse tree
	 */
	void enterSettextFormatModern(OGLParser.SettextFormatModernContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#settextFormatModern}.
	 * @param ctx the parse tree
	 */
	void exitSettextFormatModern(OGLParser.SettextFormatModernContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#settextFormatPlacement}.
	 * @param ctx the parse tree
	 */
	void enterSettextFormatPlacement(OGLParser.SettextFormatPlacementContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#settextFormatPlacement}.
	 * @param ctx the parse tree
	 */
	void exitSettextFormatPlacement(OGLParser.SettextFormatPlacementContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#settextFormatColumn}.
	 * @param ctx the parse tree
	 */
	void enterSettextFormatColumn(OGLParser.SettextFormatColumnContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#settextFormatColumn}.
	 * @param ctx the parse tree
	 */
	void exitSettextFormatColumn(OGLParser.SettextFormatColumnContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#settextAlignment}.
	 * @param ctx the parse tree
	 */
	void enterSettextAlignment(OGLParser.SettextAlignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#settextAlignment}.
	 * @param ctx the parse tree
	 */
	void exitSettextAlignment(OGLParser.SettextAlignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#settextAlignmentAuto}.
	 * @param ctx the parse tree
	 */
	void enterSettextAlignmentAuto(OGLParser.SettextAlignmentAutoContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#settextAlignmentAuto}.
	 * @param ctx the parse tree
	 */
	void exitSettextAlignmentAuto(OGLParser.SettextAlignmentAutoContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#settextAlignmentSpaced}.
	 * @param ctx the parse tree
	 */
	void enterSettextAlignmentSpaced(OGLParser.SettextAlignmentSpacedContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#settextAlignmentSpaced}.
	 * @param ctx the parse tree
	 */
	void exitSettextAlignmentSpaced(OGLParser.SettextAlignmentSpacedContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#settextAlignmentValue}.
	 * @param ctx the parse tree
	 */
	void enterSettextAlignmentValue(OGLParser.SettextAlignmentValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#settextAlignmentValue}.
	 * @param ctx the parse tree
	 */
	void exitSettextAlignmentValue(OGLParser.SettextAlignmentValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#setunitsCommand}.
	 * @param ctx the parse tree
	 */
	void enterSetunitsCommand(OGLParser.SetunitsCommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#setunitsCommand}.
	 * @param ctx the parse tree
	 */
	void exitSetunitsCommand(OGLParser.SetunitsCommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#setunitsDefault}.
	 * @param ctx the parse tree
	 */
	void enterSetunitsDefault(OGLParser.SetunitsDefaultContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#setunitsDefault}.
	 * @param ctx the parse tree
	 */
	void exitSetunitsDefault(OGLParser.SetunitsDefaultContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#primaryDefault}.
	 * @param ctx the parse tree
	 */
	void enterPrimaryDefault(OGLParser.PrimaryDefaultContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#primaryDefault}.
	 * @param ctx the parse tree
	 */
	void exitPrimaryDefault(OGLParser.PrimaryDefaultContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#secondaryDefault}.
	 * @param ctx the parse tree
	 */
	void enterSecondaryDefault(OGLParser.SecondaryDefaultContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#secondaryDefault}.
	 * @param ctx the parse tree
	 */
	void exitSecondaryDefault(OGLParser.SecondaryDefaultContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#setunitsLineSp}.
	 * @param ctx the parse tree
	 */
	void enterSetunitsLineSp(OGLParser.SetunitsLineSpContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#setunitsLineSp}.
	 * @param ctx the parse tree
	 */
	void exitSetunitsLineSp(OGLParser.SetunitsLineSpContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#setunitsCornerLength}.
	 * @param ctx the parse tree
	 */
	void enterSetunitsCornerLength(OGLParser.SetunitsCornerLengthContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#setunitsCornerLength}.
	 * @param ctx the parse tree
	 */
	void exitSetunitsCornerLength(OGLParser.SetunitsCornerLengthContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#conrnerLengthValue}.
	 * @param ctx the parse tree
	 */
	void enterConrnerLengthValue(OGLParser.ConrnerLengthValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#conrnerLengthValue}.
	 * @param ctx the parse tree
	 */
	void exitConrnerLengthValue(OGLParser.ConrnerLengthValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#setunitsTextMargin}.
	 * @param ctx the parse tree
	 */
	void enterSetunitsTextMargin(OGLParser.SetunitsTextMarginContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#setunitsTextMargin}.
	 * @param ctx the parse tree
	 */
	void exitSetunitsTextMargin(OGLParser.SetunitsTextMarginContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#textMarginValue}.
	 * @param ctx the parse tree
	 */
	void enterTextMarginValue(OGLParser.TextMarginValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#textMarginValue}.
	 * @param ctx the parse tree
	 */
	void exitTextMarginValue(OGLParser.TextMarginValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#setUnitsPositioning}.
	 * @param ctx the parse tree
	 */
	void enterSetUnitsPositioning(OGLParser.SetUnitsPositioningContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#setUnitsPositioning}.
	 * @param ctx the parse tree
	 */
	void exitSetUnitsPositioning(OGLParser.SetUnitsPositioningContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#positionValue}.
	 * @param ctx the parse tree
	 */
	void enterPositionValue(OGLParser.PositionValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#positionValue}.
	 * @param ctx the parse tree
	 */
	void exitPositionValue(OGLParser.PositionValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#placeCommand}.
	 * @param ctx the parse tree
	 */
	void enterPlaceCommand(OGLParser.PlaceCommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#placeCommand}.
	 * @param ctx the parse tree
	 */
	void exitPlaceCommand(OGLParser.PlaceCommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#drawruleCommand}.
	 * @param ctx the parse tree
	 */
	void enterDrawruleCommand(OGLParser.DrawruleCommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#drawruleCommand}.
	 * @param ctx the parse tree
	 */
	void exitDrawruleCommand(OGLParser.DrawruleCommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#ruleDirection}.
	 * @param ctx the parse tree
	 */
	void enterRuleDirection(OGLParser.RuleDirectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#ruleDirection}.
	 * @param ctx the parse tree
	 */
	void exitRuleDirection(OGLParser.RuleDirectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#ruleLength}.
	 * @param ctx the parse tree
	 */
	void enterRuleLength(OGLParser.RuleLengthContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#ruleLength}.
	 * @param ctx the parse tree
	 */
	void exitRuleLength(OGLParser.RuleLengthContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#ruleThickness}.
	 * @param ctx the parse tree
	 */
	void enterRuleThickness(OGLParser.RuleThicknessContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#ruleThickness}.
	 * @param ctx the parse tree
	 */
	void exitRuleThickness(OGLParser.RuleThicknessContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#ruleType}.
	 * @param ctx the parse tree
	 */
	void enterRuleType(OGLParser.RuleTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#ruleType}.
	 * @param ctx the parse tree
	 */
	void exitRuleType(OGLParser.RuleTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#ruleRepeated}.
	 * @param ctx the parse tree
	 */
	void enterRuleRepeated(OGLParser.RuleRepeatedContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#ruleRepeated}.
	 * @param ctx the parse tree
	 */
	void exitRuleRepeated(OGLParser.RuleRepeatedContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#ruleRepeatAcross}.
	 * @param ctx the parse tree
	 */
	void enterRuleRepeatAcross(OGLParser.RuleRepeatAcrossContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#ruleRepeatAcross}.
	 * @param ctx the parse tree
	 */
	void exitRuleRepeatAcross(OGLParser.RuleRepeatAcrossContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#ruleRepetition}.
	 * @param ctx the parse tree
	 */
	void enterRuleRepetition(OGLParser.RuleRepetitionContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#ruleRepetition}.
	 * @param ctx the parse tree
	 */
	void exitRuleRepetition(OGLParser.RuleRepetitionContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#ruleRepeatLocation}.
	 * @param ctx the parse tree
	 */
	void enterRuleRepeatLocation(OGLParser.RuleRepeatLocationContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#ruleRepeatLocation}.
	 * @param ctx the parse tree
	 */
	void exitRuleRepeatLocation(OGLParser.RuleRepeatLocationContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#ruleRepeatVerticalCoordinate}.
	 * @param ctx the parse tree
	 */
	void enterRuleRepeatVerticalCoordinate(OGLParser.RuleRepeatVerticalCoordinateContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#ruleRepeatVerticalCoordinate}.
	 * @param ctx the parse tree
	 */
	void exitRuleRepeatVerticalCoordinate(OGLParser.RuleRepeatVerticalCoordinateContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#ruleRepeatHorizonalCoordinate}.
	 * @param ctx the parse tree
	 */
	void enterRuleRepeatHorizonalCoordinate(OGLParser.RuleRepeatHorizonalCoordinateContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#ruleRepeatHorizonalCoordinate}.
	 * @param ctx the parse tree
	 */
	void exitRuleRepeatHorizonalCoordinate(OGLParser.RuleRepeatHorizonalCoordinateContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#drawboxCommand}.
	 * @param ctx the parse tree
	 */
	void enterDrawboxCommand(OGLParser.DrawboxCommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#drawboxCommand}.
	 * @param ctx the parse tree
	 */
	void exitDrawboxCommand(OGLParser.DrawboxCommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#boxWidth}.
	 * @param ctx the parse tree
	 */
	void enterBoxWidth(OGLParser.BoxWidthContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#boxWidth}.
	 * @param ctx the parse tree
	 */
	void exitBoxWidth(OGLParser.BoxWidthContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#boxHeight}.
	 * @param ctx the parse tree
	 */
	void enterBoxHeight(OGLParser.BoxHeightContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#boxHeight}.
	 * @param ctx the parse tree
	 */
	void exitBoxHeight(OGLParser.BoxHeightContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#boxBorderThickness}.
	 * @param ctx the parse tree
	 */
	void enterBoxBorderThickness(OGLParser.BoxBorderThicknessContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#boxBorderThickness}.
	 * @param ctx the parse tree
	 */
	void exitBoxBorderThickness(OGLParser.BoxBorderThicknessContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#boxBorderType}.
	 * @param ctx the parse tree
	 */
	void enterBoxBorderType(OGLParser.BoxBorderTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#boxBorderType}.
	 * @param ctx the parse tree
	 */
	void exitBoxBorderType(OGLParser.BoxBorderTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#boxRounded}.
	 * @param ctx the parse tree
	 */
	void enterBoxRounded(OGLParser.BoxRoundedContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#boxRounded}.
	 * @param ctx the parse tree
	 */
	void exitBoxRounded(OGLParser.BoxRoundedContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#boxRoundedOption}.
	 * @param ctx the parse tree
	 */
	void enterBoxRoundedOption(OGLParser.BoxRoundedOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#boxRoundedOption}.
	 * @param ctx the parse tree
	 */
	void exitBoxRoundedOption(OGLParser.BoxRoundedOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#boxDiagonal}.
	 * @param ctx the parse tree
	 */
	void enterBoxDiagonal(OGLParser.BoxDiagonalContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#boxDiagonal}.
	 * @param ctx the parse tree
	 */
	void exitBoxDiagonal(OGLParser.BoxDiagonalContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#boxDiagonalOption}.
	 * @param ctx the parse tree
	 */
	void enterBoxDiagonalOption(OGLParser.BoxDiagonalOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#boxDiagonalOption}.
	 * @param ctx the parse tree
	 */
	void exitBoxDiagonalOption(OGLParser.BoxDiagonalOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#boxRepeat}.
	 * @param ctx the parse tree
	 */
	void enterBoxRepeat(OGLParser.BoxRepeatContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#boxRepeat}.
	 * @param ctx the parse tree
	 */
	void exitBoxRepeat(OGLParser.BoxRepeatContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#boxRepeatLocation}.
	 * @param ctx the parse tree
	 */
	void enterBoxRepeatLocation(OGLParser.BoxRepeatLocationContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#boxRepeatLocation}.
	 * @param ctx the parse tree
	 */
	void exitBoxRepeatLocation(OGLParser.BoxRepeatLocationContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#boxRepeatVerticalCoordinate}.
	 * @param ctx the parse tree
	 */
	void enterBoxRepeatVerticalCoordinate(OGLParser.BoxRepeatVerticalCoordinateContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#boxRepeatVerticalCoordinate}.
	 * @param ctx the parse tree
	 */
	void exitBoxRepeatVerticalCoordinate(OGLParser.BoxRepeatVerticalCoordinateContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#boxRepeatHorizonalCoordinate}.
	 * @param ctx the parse tree
	 */
	void enterBoxRepeatHorizonalCoordinate(OGLParser.BoxRepeatHorizonalCoordinateContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#boxRepeatHorizonalCoordinate}.
	 * @param ctx the parse tree
	 */
	void exitBoxRepeatHorizonalCoordinate(OGLParser.BoxRepeatHorizonalCoordinateContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#boxRepeatAcrossDown}.
	 * @param ctx the parse tree
	 */
	void enterBoxRepeatAcrossDown(OGLParser.BoxRepeatAcrossDownContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#boxRepeatAcrossDown}.
	 * @param ctx the parse tree
	 */
	void exitBoxRepeatAcrossDown(OGLParser.BoxRepeatAcrossDownContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#boxRepetition}.
	 * @param ctx the parse tree
	 */
	void enterBoxRepetition(OGLParser.BoxRepetitionContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#boxRepetition}.
	 * @param ctx the parse tree
	 */
	void exitBoxRepetition(OGLParser.BoxRepetitionContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#boxRepeatSpaced}.
	 * @param ctx the parse tree
	 */
	void enterBoxRepeatSpaced(OGLParser.BoxRepeatSpacedContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#boxRepeatSpaced}.
	 * @param ctx the parse tree
	 */
	void exitBoxRepeatSpaced(OGLParser.BoxRepeatSpacedContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#spacedValue}.
	 * @param ctx the parse tree
	 */
	void enterSpacedValue(OGLParser.SpacedValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#spacedValue}.
	 * @param ctx the parse tree
	 */
	void exitSpacedValue(OGLParser.SpacedValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#boxShade}.
	 * @param ctx the parse tree
	 */
	void enterBoxShade(OGLParser.BoxShadeContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#boxShade}.
	 * @param ctx the parse tree
	 */
	void exitBoxShade(OGLParser.BoxShadeContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#box}.
	 * @param ctx the parse tree
	 */
	void enterBox(OGLParser.BoxContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#box}.
	 * @param ctx the parse tree
	 */
	void exitBox(OGLParser.BoxContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#shadeArea}.
	 * @param ctx the parse tree
	 */
	void enterShadeArea(OGLParser.ShadeAreaContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#shadeArea}.
	 * @param ctx the parse tree
	 */
	void exitShadeArea(OGLParser.ShadeAreaContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#shadePattern}.
	 * @param ctx the parse tree
	 */
	void enterShadePattern(OGLParser.ShadePatternContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#shadePattern}.
	 * @param ctx the parse tree
	 */
	void exitShadePattern(OGLParser.ShadePatternContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#shadeType}.
	 * @param ctx the parse tree
	 */
	void enterShadeType(OGLParser.ShadeTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#shadeType}.
	 * @param ctx the parse tree
	 */
	void exitShadeType(OGLParser.ShadeTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#boxColor}.
	 * @param ctx the parse tree
	 */
	void enterBoxColor(OGLParser.BoxColorContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#boxColor}.
	 * @param ctx the parse tree
	 */
	void exitBoxColor(OGLParser.BoxColorContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#boxColorName}.
	 * @param ctx the parse tree
	 */
	void enterBoxColorName(OGLParser.BoxColorNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#boxColorName}.
	 * @param ctx the parse tree
	 */
	void exitBoxColorName(OGLParser.BoxColorNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#boxWithtext}.
	 * @param ctx the parse tree
	 */
	void enterBoxWithtext(OGLParser.BoxWithtextContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#boxWithtext}.
	 * @param ctx the parse tree
	 */
	void exitBoxWithtext(OGLParser.BoxWithtextContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#boxWithtextOrient}.
	 * @param ctx the parse tree
	 */
	void enterBoxWithtextOrient(OGLParser.BoxWithtextOrientContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#boxWithtextOrient}.
	 * @param ctx the parse tree
	 */
	void exitBoxWithtextOrient(OGLParser.BoxWithtextOrientContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#boxWithtextLineSpacing}.
	 * @param ctx the parse tree
	 */
	void enterBoxWithtextLineSpacing(OGLParser.BoxWithtextLineSpacingContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#boxWithtextLineSpacing}.
	 * @param ctx the parse tree
	 */
	void exitBoxWithtextLineSpacing(OGLParser.BoxWithtextLineSpacingContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#line}.
	 * @param ctx the parse tree
	 */
	void enterLine(OGLParser.LineContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#line}.
	 * @param ctx the parse tree
	 */
	void exitLine(OGLParser.LineContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#line_part}.
	 * @param ctx the parse tree
	 */
	void enterLine_part(OGLParser.Line_partContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#line_part}.
	 * @param ctx the parse tree
	 */
	void exitLine_part(OGLParser.Line_partContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#text}.
	 * @param ctx the parse tree
	 */
	void enterText(OGLParser.TextContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#text}.
	 * @param ctx the parse tree
	 */
	void exitText(OGLParser.TextContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#lineSosiMode}.
	 * @param ctx the parse tree
	 */
	void enterLineSosiMode(OGLParser.LineSosiModeContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#lineSosiMode}.
	 * @param ctx the parse tree
	 */
	void exitLineSosiMode(OGLParser.LineSosiModeContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#lineUnderlying}.
	 * @param ctx the parse tree
	 */
	void enterLineUnderlying(OGLParser.LineUnderlyingContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#lineUnderlying}.
	 * @param ctx the parse tree
	 */
	void exitLineUnderlying(OGLParser.LineUnderlyingContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#lineTextType}.
	 * @param ctx the parse tree
	 */
	void enterLineTextType(OGLParser.LineTextTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#lineTextType}.
	 * @param ctx the parse tree
	 */
	void exitLineTextType(OGLParser.LineTextTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#boxWithtextFormat}.
	 * @param ctx the parse tree
	 */
	void enterBoxWithtextFormat(OGLParser.BoxWithtextFormatContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#boxWithtextFormat}.
	 * @param ctx the parse tree
	 */
	void exitBoxWithtextFormat(OGLParser.BoxWithtextFormatContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#boxWithtextFormatModern}.
	 * @param ctx the parse tree
	 */
	void enterBoxWithtextFormatModern(OGLParser.BoxWithtextFormatModernContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#boxWithtextFormatModern}.
	 * @param ctx the parse tree
	 */
	void exitBoxWithtextFormatModern(OGLParser.BoxWithtextFormatModernContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#boxWithtextFormatPlacement}.
	 * @param ctx the parse tree
	 */
	void enterBoxWithtextFormatPlacement(OGLParser.BoxWithtextFormatPlacementContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#boxWithtextFormatPlacement}.
	 * @param ctx the parse tree
	 */
	void exitBoxWithtextFormatPlacement(OGLParser.BoxWithtextFormatPlacementContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#boxWithtextFormatColumn}.
	 * @param ctx the parse tree
	 */
	void enterBoxWithtextFormatColumn(OGLParser.BoxWithtextFormatColumnContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#boxWithtextFormatColumn}.
	 * @param ctx the parse tree
	 */
	void exitBoxWithtextFormatColumn(OGLParser.BoxWithtextFormatColumnContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#positionCommand}.
	 * @param ctx the parse tree
	 */
	void enterPositionCommand(OGLParser.PositionCommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#positionCommand}.
	 * @param ctx the parse tree
	 */
	void exitPositionCommand(OGLParser.PositionCommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#positionX}.
	 * @param ctx the parse tree
	 */
	void enterPositionX(OGLParser.PositionXContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#positionX}.
	 * @param ctx the parse tree
	 */
	void exitPositionX(OGLParser.PositionXContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#positionY}.
	 * @param ctx the parse tree
	 */
	void enterPositionY(OGLParser.PositionYContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#positionY}.
	 * @param ctx the parse tree
	 */
	void exitPositionY(OGLParser.PositionYContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#controlCommand}.
	 * @param ctx the parse tree
	 */
	void enterControlCommand(OGLParser.ControlCommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#controlCommand}.
	 * @param ctx the parse tree
	 */
	void exitControlCommand(OGLParser.ControlCommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#controlStorage}.
	 * @param ctx the parse tree
	 */
	void enterControlStorage(OGLParser.ControlStorageContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#controlStorage}.
	 * @param ctx the parse tree
	 */
	void exitControlStorage(OGLParser.ControlStorageContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#controlMessage}.
	 * @param ctx the parse tree
	 */
	void enterControlMessage(OGLParser.ControlMessageContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#controlMessage}.
	 * @param ctx the parse tree
	 */
	void exitControlMessage(OGLParser.ControlMessageContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#controlSummary}.
	 * @param ctx the parse tree
	 */
	void enterControlSummary(OGLParser.ControlSummaryContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#controlSummary}.
	 * @param ctx the parse tree
	 */
	void exitControlSummary(OGLParser.ControlSummaryContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#controlSosiOption}.
	 * @param ctx the parse tree
	 */
	void enterControlSosiOption(OGLParser.ControlSosiOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#controlSosiOption}.
	 * @param ctx the parse tree
	 */
	void exitControlSosiOption(OGLParser.ControlSosiOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#overlayCommand}.
	 * @param ctx the parse tree
	 */
	void enterOverlayCommand(OGLParser.OverlayCommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#overlayCommand}.
	 * @param ctx the parse tree
	 */
	void exitOverlayCommand(OGLParser.OverlayCommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#overlayName}.
	 * @param ctx the parse tree
	 */
	void enterOverlayName(OGLParser.OverlayNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#overlayName}.
	 * @param ctx the parse tree
	 */
	void exitOverlayName(OGLParser.OverlayNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#overlayWidth}.
	 * @param ctx the parse tree
	 */
	void enterOverlayWidth(OGLParser.OverlayWidthContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#overlayWidth}.
	 * @param ctx the parse tree
	 */
	void exitOverlayWidth(OGLParser.OverlayWidthContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#overlayHeight}.
	 * @param ctx the parse tree
	 */
	void enterOverlayHeight(OGLParser.OverlayHeightContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#overlayHeight}.
	 * @param ctx the parse tree
	 */
	void exitOverlayHeight(OGLParser.OverlayHeightContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#overlayHorizonalCoordinate}.
	 * @param ctx the parse tree
	 */
	void enterOverlayHorizonalCoordinate(OGLParser.OverlayHorizonalCoordinateContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#overlayHorizonalCoordinate}.
	 * @param ctx the parse tree
	 */
	void exitOverlayHorizonalCoordinate(OGLParser.OverlayHorizonalCoordinateContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#overlayVerticalCoordinate}.
	 * @param ctx the parse tree
	 */
	void enterOverlayVerticalCoordinate(OGLParser.OverlayVerticalCoordinateContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#overlayVerticalCoordinate}.
	 * @param ctx the parse tree
	 */
	void exitOverlayVerticalCoordinate(OGLParser.OverlayVerticalCoordinateContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#orientCommand}.
	 * @param ctx the parse tree
	 */
	void enterOrientCommand(OGLParser.OrientCommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#orientCommand}.
	 * @param ctx the parse tree
	 */
	void exitOrientCommand(OGLParser.OrientCommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#orientRotatedDegree}.
	 * @param ctx the parse tree
	 */
	void enterOrientRotatedDegree(OGLParser.OrientRotatedDegreeContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#orientRotatedDegree}.
	 * @param ctx the parse tree
	 */
	void exitOrientRotatedDegree(OGLParser.OrientRotatedDegreeContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#fontCommand}.
	 * @param ctx the parse tree
	 */
	void enterFontCommand(OGLParser.FontCommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#fontCommand}.
	 * @param ctx the parse tree
	 */
	void exitFontCommand(OGLParser.FontCommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#fontCommandMVS}.
	 * @param ctx the parse tree
	 */
	void enterFontCommandMVS(OGLParser.FontCommandMVSContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#fontCommandMVS}.
	 * @param ctx the parse tree
	 */
	void exitFontCommandMVS(OGLParser.FontCommandMVSContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#fontCommandVM}.
	 * @param ctx the parse tree
	 */
	void enterFontCommandVM(OGLParser.FontCommandVMContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#fontCommandVM}.
	 * @param ctx the parse tree
	 */
	void exitFontCommandVM(OGLParser.FontCommandVMContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#fontFileType}.
	 * @param ctx the parse tree
	 */
	void enterFontFileType(OGLParser.FontFileTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#fontFileType}.
	 * @param ctx the parse tree
	 */
	void exitFontFileType(OGLParser.FontFileTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#fileTypeName}.
	 * @param ctx the parse tree
	 */
	void enterFileTypeName(OGLParser.FileTypeNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#fileTypeName}.
	 * @param ctx the parse tree
	 */
	void exitFileTypeName(OGLParser.FileTypeNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#fontWithMemID}.
	 * @param ctx the parse tree
	 */
	void enterFontWithMemID(OGLParser.FontWithMemIDContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#fontWithMemID}.
	 * @param ctx the parse tree
	 */
	void exitFontWithMemID(OGLParser.FontWithMemIDContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#fontWithCharSet}.
	 * @param ctx the parse tree
	 */
	void enterFontWithCharSet(OGLParser.FontWithCharSetContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#fontWithCharSet}.
	 * @param ctx the parse tree
	 */
	void exitFontWithCharSet(OGLParser.FontWithCharSetContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#fontDDName}.
	 * @param ctx the parse tree
	 */
	void enterFontDDName(OGLParser.FontDDNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#fontDDName}.
	 * @param ctx the parse tree
	 */
	void exitFontDDName(OGLParser.FontDDNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#ddNameName}.
	 * @param ctx the parse tree
	 */
	void enterDdNameName(OGLParser.DdNameNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#ddNameName}.
	 * @param ctx the parse tree
	 */
	void exitDdNameName(OGLParser.DdNameNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#fontHeight}.
	 * @param ctx the parse tree
	 */
	void enterFontHeight(OGLParser.FontHeightContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#fontHeight}.
	 * @param ctx the parse tree
	 */
	void exitFontHeight(OGLParser.FontHeightContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#fontScale}.
	 * @param ctx the parse tree
	 */
	void enterFontScale(OGLParser.FontScaleContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#fontScale}.
	 * @param ctx the parse tree
	 */
	void exitFontScale(OGLParser.FontScaleContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#fontColor}.
	 * @param ctx the parse tree
	 */
	void enterFontColor(OGLParser.FontColorContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#fontColor}.
	 * @param ctx the parse tree
	 */
	void exitFontColor(OGLParser.FontColorContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#fontUColor}.
	 * @param ctx the parse tree
	 */
	void enterFontUColor(OGLParser.FontUColorContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#fontUColor}.
	 * @param ctx the parse tree
	 */
	void exitFontUColor(OGLParser.FontUColorContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#fontColorName}.
	 * @param ctx the parse tree
	 */
	void enterFontColorName(OGLParser.FontColorNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#fontColorName}.
	 * @param ctx the parse tree
	 */
	void exitFontColorName(OGLParser.FontColorNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#fontName}.
	 * @param ctx the parse tree
	 */
	void enterFontName(OGLParser.FontNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#fontName}.
	 * @param ctx the parse tree
	 */
	void exitFontName(OGLParser.FontNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#memId}.
	 * @param ctx the parse tree
	 */
	void enterMemId(OGLParser.MemIdContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#memId}.
	 * @param ctx the parse tree
	 */
	void exitMemId(OGLParser.MemIdContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#charSetName}.
	 * @param ctx the parse tree
	 */
	void enterCharSetName(OGLParser.CharSetNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#charSetName}.
	 * @param ctx the parse tree
	 */
	void exitCharSetName(OGLParser.CharSetNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#codePageName}.
	 * @param ctx the parse tree
	 */
	void enterCodePageName(OGLParser.CodePageNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#codePageName}.
	 * @param ctx the parse tree
	 */
	void exitCodePageName(OGLParser.CodePageNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#defineGroupCommand}.
	 * @param ctx the parse tree
	 */
	void enterDefineGroupCommand(OGLParser.DefineGroupCommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#defineGroupCommand}.
	 * @param ctx the parse tree
	 */
	void exitDefineGroupCommand(OGLParser.DefineGroupCommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#groupName}.
	 * @param ctx the parse tree
	 */
	void enterGroupName(OGLParser.GroupNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#groupName}.
	 * @param ctx the parse tree
	 */
	void exitGroupName(OGLParser.GroupNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link OGLParser#oglMeasurement}.
	 * @param ctx the parse tree
	 */
	void enterOglMeasurement(OGLParser.OglMeasurementContext ctx);
	/**
	 * Exit a parse tree produced by {@link OGLParser#oglMeasurement}.
	 * @param ctx the parse tree
	 */
	void exitOglMeasurement(OGLParser.OglMeasurementContext ctx);
}