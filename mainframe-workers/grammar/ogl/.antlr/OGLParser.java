// Generated from /home/minhnl11aic/Documents/mainframe-workers/grammar/ogl/OGL.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class OGLParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		DOT=1, LPAREN=2, RPAREN=3, ABSOLUTE=4, ACROSS=5, ALL=6, AUTO=7, BALANCE=8, 
		BOLD=9, BOTH=10, BOTTOM=11, BOTTOMLEFT=12, BOTTOMRIGHT=13, BOX=14, CENTER=15, 
		CHAR=16, CHARSET=17, CODEPAGE=18, COLOR=19, COLUMN=20, CONTROL=21, CORNERLENGTH=22, 
		CPI=23, DARK=24, DASHED=25, DDNAME=26, DEFINE=27, DIAGONAL=28, DIAMETER=29, 
		DOTTED=30, DRAWBOX=31, DRAWRULE=32, DOWN=33, ENCODED=34, ENDDEF=35, ERROR=36, 
		FILETYPE=37, FONT=38, FONT38PP=39, FONTDD=40, GROUP=41, HALF=42, HEIGHT=43, 
		HEX=44, IN=45, JUSTIFY=46, LARGE=47, LASTNO=48, LEFT=49, LIGHT=50, LINE=51, 
		LINESP=52, LOCATION=53, LPI=54, MAX=55, MM=56, MEDIUM=57, MIRROR=58, MODERN=59, 
		NEGATIVE=60, NOMIRROR=61, NONEGATIVE=62, NOSTORE=63, NOSOSI=64, NOSUMMARY=65, 
		NOUNDERLINE=66, OFFSET=67, ORIENT=68, OVERLAY=69, PATTERN=70, PELS=71, 
		PLACE=72, POINTS=73, POSITION=74, POSITIONING=75, PSEG38PP=76, REPEAT=77, 
		REPLACE=78, RIGHT=79, ROUNDED=80, SCALE=81, SCREEN=82, SEGDD=83, SEGID=84, 
		SEGMENT=85, SETTEXT=86, SETUNITS=87, SHADE=88, SIZE=89, SMALL=90, SOLID=91, 
		SOSI=92, SOSI1=93, SOSI2=94, SPACED=95, SQUARE=96, STANDARD=97, STORE=98, 
		SUMMARY=99, TATE=100, TEXTMARGIN=101, TOP=102, TOPLEFT=103, TOPRIGHT=104, 
		UCOLOR=105, UNDERLINE=106, UP=107, WARN=108, WHOLE=109, WITHTEXT=110, 
		XDARK=111, XLIGHT=112, STRINGLITERAL=113, INTEGERLITERAL=114, COMMENT=115, 
		NEWLINE=116, WS=117, IDENTIFIER=118;
	public static final int
		RULE_startRule = 0, RULE_command = 1, RULE_segmentCommand = 2, RULE_segmentName = 3, 
		RULE_segmentDDName = 4, RULE_segmentDDNameName = 5, RULE_segmentFileType = 6, 
		RULE_placePatternCommand = 7, RULE_patternColor = 8, RULE_patternColorName = 9, 
		RULE_mirrorOption = 10, RULE_negativeOption = 11, RULE_patternShade = 12, 
		RULE_definepatternCommand = 13, RULE_lineCoding = 14, RULE_lineCodingPels = 15, 
		RULE_lineCodingEncoded = 16, RULE_coded_line = 17, RULE_patternName = 18, 
		RULE_settextCommand = 19, RULE_settextFormat = 20, RULE_settextFormatModern = 21, 
		RULE_settextFormatPlacement = 22, RULE_settextFormatColumn = 23, RULE_settextAlignment = 24, 
		RULE_settextAlignmentAuto = 25, RULE_settextAlignmentSpaced = 26, RULE_settextAlignmentValue = 27, 
		RULE_setunitsCommand = 28, RULE_setunitsDefault = 29, RULE_primaryDefault = 30, 
		RULE_secondaryDefault = 31, RULE_setunitsLineSp = 32, RULE_setunitsCornerLength = 33, 
		RULE_conrnerLengthValue = 34, RULE_setunitsTextMargin = 35, RULE_textMarginValue = 36, 
		RULE_setUnitsPositioning = 37, RULE_positionValue = 38, RULE_placeCommand = 39, 
		RULE_drawruleCommand = 40, RULE_ruleDirection = 41, RULE_ruleLength = 42, 
		RULE_ruleThickness = 43, RULE_ruleType = 44, RULE_ruleRepeated = 45, RULE_ruleRepeatAcross = 46, 
		RULE_ruleRepetition = 47, RULE_ruleRepeatLocation = 48, RULE_ruleRepeatVerticalCoordinate = 49, 
		RULE_ruleRepeatHorizonalCoordinate = 50, RULE_drawboxCommand = 51, RULE_boxWidth = 52, 
		RULE_boxHeight = 53, RULE_boxBorderThickness = 54, RULE_boxBorderType = 55, 
		RULE_boxRounded = 56, RULE_boxRoundedOption = 57, RULE_boxDiagonal = 58, 
		RULE_boxDiagonalOption = 59, RULE_boxRepeat = 60, RULE_boxRepeatLocation = 61, 
		RULE_boxRepeatVerticalCoordinate = 62, RULE_boxRepeatHorizonalCoordinate = 63, 
		RULE_boxRepeatAcrossDown = 64, RULE_boxRepetition = 65, RULE_boxRepeatSpaced = 66, 
		RULE_spacedValue = 67, RULE_boxShade = 68, RULE_box = 69, RULE_shadeArea = 70, 
		RULE_shadePattern = 71, RULE_shadeType = 72, RULE_boxColor = 73, RULE_boxColorName = 74, 
		RULE_boxWithtext = 75, RULE_boxWithtextOrient = 76, RULE_boxWithtextLineSpacing = 77, 
		RULE_line = 78, RULE_line_part = 79, RULE_text = 80, RULE_lineSosiMode = 81, 
		RULE_lineUnderlying = 82, RULE_lineTextType = 83, RULE_boxWithtextFormat = 84, 
		RULE_boxWithtextFormatModern = 85, RULE_boxWithtextFormatPlacement = 86, 
		RULE_boxWithtextFormatColumn = 87, RULE_positionCommand = 88, RULE_positionX = 89, 
		RULE_positionY = 90, RULE_controlCommand = 91, RULE_controlStorage = 92, 
		RULE_controlMessage = 93, RULE_controlSummary = 94, RULE_controlSosiOption = 95, 
		RULE_overlayCommand = 96, RULE_overlayName = 97, RULE_overlayWidth = 98, 
		RULE_overlayHeight = 99, RULE_overlayHorizonalCoordinate = 100, RULE_overlayVerticalCoordinate = 101, 
		RULE_orientCommand = 102, RULE_orientRotatedDegree = 103, RULE_fontCommand = 104, 
		RULE_fontCommandMVS = 105, RULE_fontCommandVM = 106, RULE_fontFileType = 107, 
		RULE_fileTypeName = 108, RULE_fontWithMemID = 109, RULE_fontWithCharSet = 110, 
		RULE_fontDDName = 111, RULE_ddNameName = 112, RULE_fontHeight = 113, RULE_fontScale = 114, 
		RULE_fontColor = 115, RULE_fontUColor = 116, RULE_fontColorName = 117, 
		RULE_fontName = 118, RULE_memId = 119, RULE_charSetName = 120, RULE_codePageName = 121, 
		RULE_defineGroupCommand = 122, RULE_groupName = 123, RULE_oglMeasurement = 124;
	private static String[] makeRuleNames() {
		return new String[] {
			"startRule", "command", "segmentCommand", "segmentName", "segmentDDName", 
			"segmentDDNameName", "segmentFileType", "placePatternCommand", "patternColor", 
			"patternColorName", "mirrorOption", "negativeOption", "patternShade", 
			"definepatternCommand", "lineCoding", "lineCodingPels", "lineCodingEncoded", 
			"coded_line", "patternName", "settextCommand", "settextFormat", "settextFormatModern", 
			"settextFormatPlacement", "settextFormatColumn", "settextAlignment", 
			"settextAlignmentAuto", "settextAlignmentSpaced", "settextAlignmentValue", 
			"setunitsCommand", "setunitsDefault", "primaryDefault", "secondaryDefault", 
			"setunitsLineSp", "setunitsCornerLength", "conrnerLengthValue", "setunitsTextMargin", 
			"textMarginValue", "setUnitsPositioning", "positionValue", "placeCommand", 
			"drawruleCommand", "ruleDirection", "ruleLength", "ruleThickness", "ruleType", 
			"ruleRepeated", "ruleRepeatAcross", "ruleRepetition", "ruleRepeatLocation", 
			"ruleRepeatVerticalCoordinate", "ruleRepeatHorizonalCoordinate", "drawboxCommand", 
			"boxWidth", "boxHeight", "boxBorderThickness", "boxBorderType", "boxRounded", 
			"boxRoundedOption", "boxDiagonal", "boxDiagonalOption", "boxRepeat", 
			"boxRepeatLocation", "boxRepeatVerticalCoordinate", "boxRepeatHorizonalCoordinate", 
			"boxRepeatAcrossDown", "boxRepetition", "boxRepeatSpaced", "spacedValue", 
			"boxShade", "box", "shadeArea", "shadePattern", "shadeType", "boxColor", 
			"boxColorName", "boxWithtext", "boxWithtextOrient", "boxWithtextLineSpacing", 
			"line", "line_part", "text", "lineSosiMode", "lineUnderlying", "lineTextType", 
			"boxWithtextFormat", "boxWithtextFormatModern", "boxWithtextFormatPlacement", 
			"boxWithtextFormatColumn", "positionCommand", "positionX", "positionY", 
			"controlCommand", "controlStorage", "controlMessage", "controlSummary", 
			"controlSosiOption", "overlayCommand", "overlayName", "overlayWidth", 
			"overlayHeight", "overlayHorizonalCoordinate", "overlayVerticalCoordinate", 
			"orientCommand", "orientRotatedDegree", "fontCommand", "fontCommandMVS", 
			"fontCommandVM", "fontFileType", "fileTypeName", "fontWithMemID", "fontWithCharSet", 
			"fontDDName", "ddNameName", "fontHeight", "fontScale", "fontColor", "fontUColor", 
			"fontColorName", "fontName", "memId", "charSetName", "codePageName", 
			"defineGroupCommand", "groupName", "oglMeasurement"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'.'", "'('", "')'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "DOT", "LPAREN", "RPAREN", "ABSOLUTE", "ACROSS", "ALL", "AUTO", 
			"BALANCE", "BOLD", "BOTH", "BOTTOM", "BOTTOMLEFT", "BOTTOMRIGHT", "BOX", 
			"CENTER", "CHAR", "CHARSET", "CODEPAGE", "COLOR", "COLUMN", "CONTROL", 
			"CORNERLENGTH", "CPI", "DARK", "DASHED", "DDNAME", "DEFINE", "DIAGONAL", 
			"DIAMETER", "DOTTED", "DRAWBOX", "DRAWRULE", "DOWN", "ENCODED", "ENDDEF", 
			"ERROR", "FILETYPE", "FONT", "FONT38PP", "FONTDD", "GROUP", "HALF", "HEIGHT", 
			"HEX", "IN", "JUSTIFY", "LARGE", "LASTNO", "LEFT", "LIGHT", "LINE", "LINESP", 
			"LOCATION", "LPI", "MAX", "MM", "MEDIUM", "MIRROR", "MODERN", "NEGATIVE", 
			"NOMIRROR", "NONEGATIVE", "NOSTORE", "NOSOSI", "NOSUMMARY", "NOUNDERLINE", 
			"OFFSET", "ORIENT", "OVERLAY", "PATTERN", "PELS", "PLACE", "POINTS", 
			"POSITION", "POSITIONING", "PSEG38PP", "REPEAT", "REPLACE", "RIGHT", 
			"ROUNDED", "SCALE", "SCREEN", "SEGDD", "SEGID", "SEGMENT", "SETTEXT", 
			"SETUNITS", "SHADE", "SIZE", "SMALL", "SOLID", "SOSI", "SOSI1", "SOSI2", 
			"SPACED", "SQUARE", "STANDARD", "STORE", "SUMMARY", "TATE", "TEXTMARGIN", 
			"TOP", "TOPLEFT", "TOPRIGHT", "UCOLOR", "UNDERLINE", "UP", "WARN", "WHOLE", 
			"WITHTEXT", "XDARK", "XLIGHT", "STRINGLITERAL", "INTEGERLITERAL", "COMMENT", 
			"NEWLINE", "WS", "IDENTIFIER"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "OGL.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public OGLParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StartRuleContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(OGLParser.EOF, 0); }
		public List<CommandContext> command() {
			return getRuleContexts(CommandContext.class);
		}
		public CommandContext command(int i) {
			return getRuleContext(CommandContext.class,i);
		}
		public StartRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_startRule; }
	}

	public final StartRuleContext startRule() throws RecognitionException {
		StartRuleContext _localctx = new StartRuleContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_startRule);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(253);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 281456672768L) != 0) || ((((_la - 68)) & ~0x3f) == 0 && ((1L << (_la - 68)) & 917587L) != 0)) {
				{
				{
				setState(250);
				command();
				}
				}
				setState(255);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(256);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CommandContext extends ParserRuleContext {
		public ControlCommandContext controlCommand() {
			return getRuleContext(ControlCommandContext.class,0);
		}
		public OverlayCommandContext overlayCommand() {
			return getRuleContext(OverlayCommandContext.class,0);
		}
		public OrientCommandContext orientCommand() {
			return getRuleContext(OrientCommandContext.class,0);
		}
		public FontCommandContext fontCommand() {
			return getRuleContext(FontCommandContext.class,0);
		}
		public DefineGroupCommandContext defineGroupCommand() {
			return getRuleContext(DefineGroupCommandContext.class,0);
		}
		public PositionCommandContext positionCommand() {
			return getRuleContext(PositionCommandContext.class,0);
		}
		public DrawboxCommandContext drawboxCommand() {
			return getRuleContext(DrawboxCommandContext.class,0);
		}
		public DrawruleCommandContext drawruleCommand() {
			return getRuleContext(DrawruleCommandContext.class,0);
		}
		public PlaceCommandContext placeCommand() {
			return getRuleContext(PlaceCommandContext.class,0);
		}
		public SetunitsCommandContext setunitsCommand() {
			return getRuleContext(SetunitsCommandContext.class,0);
		}
		public SettextCommandContext settextCommand() {
			return getRuleContext(SettextCommandContext.class,0);
		}
		public DefinepatternCommandContext definepatternCommand() {
			return getRuleContext(DefinepatternCommandContext.class,0);
		}
		public PlacePatternCommandContext placePatternCommand() {
			return getRuleContext(PlacePatternCommandContext.class,0);
		}
		public SegmentCommandContext segmentCommand() {
			return getRuleContext(SegmentCommandContext.class,0);
		}
		public CommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_command; }
	}

	public final CommandContext command() throws RecognitionException {
		CommandContext _localctx = new CommandContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_command);
		try {
			setState(272);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(258);
				controlCommand();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(259);
				overlayCommand();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(260);
				orientCommand();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(261);
				fontCommand();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(262);
				defineGroupCommand();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(263);
				positionCommand();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(264);
				drawboxCommand();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(265);
				drawruleCommand();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(266);
				placeCommand();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(267);
				setunitsCommand();
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(268);
				settextCommand();
				}
				break;
			case 12:
				enterOuterAlt(_localctx, 12);
				{
				setState(269);
				definepatternCommand();
				}
				break;
			case 13:
				enterOuterAlt(_localctx, 13);
				{
				setState(270);
				placePatternCommand();
				}
				break;
			case 14:
				enterOuterAlt(_localctx, 14);
				{
				setState(271);
				segmentCommand();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SegmentCommandContext extends ParserRuleContext {
		public TerminalNode SEGMENT() { return getToken(OGLParser.SEGMENT, 0); }
		public MemIdContext memId() {
			return getRuleContext(MemIdContext.class,0);
		}
		public SegmentNameContext segmentName() {
			return getRuleContext(SegmentNameContext.class,0);
		}
		public SegmentDDNameContext segmentDDName() {
			return getRuleContext(SegmentDDNameContext.class,0);
		}
		public SegmentFileTypeContext segmentFileType() {
			return getRuleContext(SegmentFileTypeContext.class,0);
		}
		public SegmentCommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_segmentCommand; }
	}

	public final SegmentCommandContext segmentCommand() throws RecognitionException {
		SegmentCommandContext _localctx = new SegmentCommandContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_segmentCommand);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(274);
			match(SEGMENT);
			setState(276);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				{
				setState(275);
				segmentName();
				}
				break;
			}
			setState(278);
			memId();
			setState(281);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case DDNAME:
				{
				setState(279);
				segmentDDName();
				}
				break;
			case FILETYPE:
				{
				setState(280);
				segmentFileType();
				}
				break;
			case EOF:
			case CONTROL:
			case DEFINE:
			case DRAWBOX:
			case DRAWRULE:
			case ENDDEF:
			case FONT:
			case ORIENT:
			case OVERLAY:
			case PLACE:
			case POSITION:
			case SEGMENT:
			case SETTEXT:
			case SETUNITS:
				break;
			default:
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SegmentNameContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(OGLParser.IDENTIFIER, 0); }
		public SegmentNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_segmentName; }
	}

	public final SegmentNameContext segmentName() throws RecognitionException {
		SegmentNameContext _localctx = new SegmentNameContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_segmentName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(283);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SegmentDDNameContext extends ParserRuleContext {
		public TerminalNode DDNAME() { return getToken(OGLParser.DDNAME, 0); }
		public SegmentDDNameNameContext segmentDDNameName() {
			return getRuleContext(SegmentDDNameNameContext.class,0);
		}
		public SegmentDDNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_segmentDDName; }
	}

	public final SegmentDDNameContext segmentDDName() throws RecognitionException {
		SegmentDDNameContext _localctx = new SegmentDDNameContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_segmentDDName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(285);
			match(DDNAME);
			setState(286);
			segmentDDNameName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SegmentDDNameNameContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(OGLParser.IDENTIFIER, 0); }
		public TerminalNode SEGDD() { return getToken(OGLParser.SEGDD, 0); }
		public SegmentDDNameNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_segmentDDNameName; }
	}

	public final SegmentDDNameNameContext segmentDDNameName() throws RecognitionException {
		SegmentDDNameNameContext _localctx = new SegmentDDNameNameContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_segmentDDNameName);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(288);
			_la = _input.LA(1);
			if ( !(_la==SEGDD || _la==IDENTIFIER) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SegmentFileTypeContext extends ParserRuleContext {
		public TerminalNode FILETYPE() { return getToken(OGLParser.FILETYPE, 0); }
		public FileTypeNameContext fileTypeName() {
			return getRuleContext(FileTypeNameContext.class,0);
		}
		public SegmentFileTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_segmentFileType; }
	}

	public final SegmentFileTypeContext segmentFileType() throws RecognitionException {
		SegmentFileTypeContext _localctx = new SegmentFileTypeContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_segmentFileType);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(290);
			match(FILETYPE);
			setState(291);
			fileTypeName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PlacePatternCommandContext extends ParserRuleContext {
		public TerminalNode PLACE() { return getToken(OGLParser.PLACE, 0); }
		public TerminalNode PATTERN() { return getToken(OGLParser.PATTERN, 0); }
		public PatternNameContext patternName() {
			return getRuleContext(PatternNameContext.class,0);
		}
		public OrientRotatedDegreeContext orientRotatedDegree() {
			return getRuleContext(OrientRotatedDegreeContext.class,0);
		}
		public PatternShadeContext patternShade() {
			return getRuleContext(PatternShadeContext.class,0);
		}
		public MirrorOptionContext mirrorOption() {
			return getRuleContext(MirrorOptionContext.class,0);
		}
		public NegativeOptionContext negativeOption() {
			return getRuleContext(NegativeOptionContext.class,0);
		}
		public PatternColorContext patternColor() {
			return getRuleContext(PatternColorContext.class,0);
		}
		public PlacePatternCommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_placePatternCommand; }
	}

	public final PlacePatternCommandContext placePatternCommand() throws RecognitionException {
		PlacePatternCommandContext _localctx = new PlacePatternCommandContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_placePatternCommand);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(293);
			match(PLACE);
			setState(294);
			match(PATTERN);
			setState(295);
			patternName();
			setState(297);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				{
				setState(296);
				orientRotatedDegree();
				}
				break;
			}
			setState(300);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 145241087999475712L) != 0) || ((((_la - 82)) & ~0x3f) == 0 && ((1L << (_la - 82)) & 5905612801L) != 0)) {
				{
				setState(299);
				patternShade();
				}
			}

			setState(303);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==MIRROR || _la==NOMIRROR) {
				{
				setState(302);
				mirrorOption();
				}
			}

			setState(306);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NEGATIVE || _la==NONEGATIVE) {
				{
				setState(305);
				negativeOption();
				}
			}

			setState(309);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COLOR) {
				{
				setState(308);
				patternColor();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PatternColorContext extends ParserRuleContext {
		public TerminalNode COLOR() { return getToken(OGLParser.COLOR, 0); }
		public PatternColorNameContext patternColorName() {
			return getRuleContext(PatternColorNameContext.class,0);
		}
		public PatternColorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_patternColor; }
	}

	public final PatternColorContext patternColor() throws RecognitionException {
		PatternColorContext _localctx = new PatternColorContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_patternColor);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(311);
			match(COLOR);
			setState(312);
			patternColorName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PatternColorNameContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(OGLParser.IDENTIFIER, 0); }
		public PatternColorNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_patternColorName; }
	}

	public final PatternColorNameContext patternColorName() throws RecognitionException {
		PatternColorNameContext _localctx = new PatternColorNameContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_patternColorName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(314);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MirrorOptionContext extends ParserRuleContext {
		public TerminalNode NOMIRROR() { return getToken(OGLParser.NOMIRROR, 0); }
		public TerminalNode MIRROR() { return getToken(OGLParser.MIRROR, 0); }
		public MirrorOptionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mirrorOption; }
	}

	public final MirrorOptionContext mirrorOption() throws RecognitionException {
		MirrorOptionContext _localctx = new MirrorOptionContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_mirrorOption);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(316);
			_la = _input.LA(1);
			if ( !(_la==MIRROR || _la==NOMIRROR) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NegativeOptionContext extends ParserRuleContext {
		public TerminalNode NEGATIVE() { return getToken(OGLParser.NEGATIVE, 0); }
		public TerminalNode NONEGATIVE() { return getToken(OGLParser.NONEGATIVE, 0); }
		public NegativeOptionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_negativeOption; }
	}

	public final NegativeOptionContext negativeOption() throws RecognitionException {
		NegativeOptionContext _localctx = new NegativeOptionContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_negativeOption);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(318);
			_la = _input.LA(1);
			if ( !(_la==NEGATIVE || _la==NONEGATIVE) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PatternShadeContext extends ParserRuleContext {
		public List<ShadePatternContext> shadePattern() {
			return getRuleContexts(ShadePatternContext.class);
		}
		public ShadePatternContext shadePattern(int i) {
			return getRuleContext(ShadePatternContext.class,i);
		}
		public List<ShadeTypeContext> shadeType() {
			return getRuleContexts(ShadeTypeContext.class);
		}
		public ShadeTypeContext shadeType(int i) {
			return getRuleContext(ShadeTypeContext.class,i);
		}
		public PatternShadeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_patternShade; }
	}

	public final PatternShadeContext patternShade() throws RecognitionException {
		PatternShadeContext _localctx = new PatternShadeContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_patternShade);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(322); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(322);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case SCREEN:
				case STANDARD:
					{
					setState(320);
					shadePattern();
					}
					break;
				case DARK:
				case LIGHT:
				case MEDIUM:
				case XDARK:
				case XLIGHT:
				case INTEGERLITERAL:
					{
					setState(321);
					shadeType();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(324); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 145241087999475712L) != 0) || ((((_la - 82)) & ~0x3f) == 0 && ((1L << (_la - 82)) & 5905612801L) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DefinepatternCommandContext extends ParserRuleContext {
		public TerminalNode DEFINE() { return getToken(OGLParser.DEFINE, 0); }
		public PatternNameContext patternName() {
			return getRuleContext(PatternNameContext.class,0);
		}
		public TerminalNode PATTERN() { return getToken(OGLParser.PATTERN, 0); }
		public LineCodingContext lineCoding() {
			return getRuleContext(LineCodingContext.class,0);
		}
		public TerminalNode ENDDEF() { return getToken(OGLParser.ENDDEF, 0); }
		public DefinepatternCommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_definepatternCommand; }
	}

	public final DefinepatternCommandContext definepatternCommand() throws RecognitionException {
		DefinepatternCommandContext _localctx = new DefinepatternCommandContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_definepatternCommand);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(326);
			match(DEFINE);
			setState(327);
			patternName();
			setState(328);
			match(PATTERN);
			setState(329);
			lineCoding();
			setState(331);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				setState(330);
				match(ENDDEF);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LineCodingContext extends ParserRuleContext {
		public LineCodingPelsContext lineCodingPels() {
			return getRuleContext(LineCodingPelsContext.class,0);
		}
		public LineCodingEncodedContext lineCodingEncoded() {
			return getRuleContext(LineCodingEncodedContext.class,0);
		}
		public LineCodingContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lineCoding; }
	}

	public final LineCodingContext lineCoding() throws RecognitionException {
		LineCodingContext _localctx = new LineCodingContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_lineCoding);
		try {
			setState(335);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PELS:
				enterOuterAlt(_localctx, 1);
				{
				setState(333);
				lineCodingPels();
				}
				break;
			case ENCODED:
				enterOuterAlt(_localctx, 2);
				{
				setState(334);
				lineCodingEncoded();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LineCodingPelsContext extends ParserRuleContext {
		public TerminalNode PELS() { return getToken(OGLParser.PELS, 0); }
		public List<Coded_lineContext> coded_line() {
			return getRuleContexts(Coded_lineContext.class);
		}
		public Coded_lineContext coded_line(int i) {
			return getRuleContext(Coded_lineContext.class,i);
		}
		public LineCodingPelsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lineCodingPels; }
	}

	public final LineCodingPelsContext lineCodingPels() throws RecognitionException {
		LineCodingPelsContext _localctx = new LineCodingPelsContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_lineCodingPels);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(337);
			match(PELS);
			setState(339); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(338);
				coded_line();
				}
				}
				setState(341); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LPAREN );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LineCodingEncodedContext extends ParserRuleContext {
		public TerminalNode ENCODED() { return getToken(OGLParser.ENCODED, 0); }
		public List<Coded_lineContext> coded_line() {
			return getRuleContexts(Coded_lineContext.class);
		}
		public Coded_lineContext coded_line(int i) {
			return getRuleContext(Coded_lineContext.class,i);
		}
		public LineCodingEncodedContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lineCodingEncoded; }
	}

	public final LineCodingEncodedContext lineCodingEncoded() throws RecognitionException {
		LineCodingEncodedContext _localctx = new LineCodingEncodedContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_lineCodingEncoded);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(343);
			match(ENCODED);
			setState(345); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(344);
				coded_line();
				}
				}
				setState(347); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LPAREN );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Coded_lineContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(OGLParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(OGLParser.RPAREN, 0); }
		public List<TerminalNode> INTEGERLITERAL() { return getTokens(OGLParser.INTEGERLITERAL); }
		public TerminalNode INTEGERLITERAL(int i) {
			return getToken(OGLParser.INTEGERLITERAL, i);
		}
		public Coded_lineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_coded_line; }
	}

	public final Coded_lineContext coded_line() throws RecognitionException {
		Coded_lineContext _localctx = new Coded_lineContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_coded_line);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(349);
			match(LPAREN);
			setState(351); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(350);
				match(INTEGERLITERAL);
				}
				}
				setState(353); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==INTEGERLITERAL );
			setState(355);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PatternNameContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(OGLParser.IDENTIFIER, 0); }
		public PatternNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_patternName; }
	}

	public final PatternNameContext patternName() throws RecognitionException {
		PatternNameContext _localctx = new PatternNameContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_patternName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(357);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SettextCommandContext extends ParserRuleContext {
		public TerminalNode SETTEXT() { return getToken(OGLParser.SETTEXT, 0); }
		public OrientRotatedDegreeContext orientRotatedDegree() {
			return getRuleContext(OrientRotatedDegreeContext.class,0);
		}
		public SettextFormatContext settextFormat() {
			return getRuleContext(SettextFormatContext.class,0);
		}
		public SettextAlignmentContext settextAlignment() {
			return getRuleContext(SettextAlignmentContext.class,0);
		}
		public List<LineContext> line() {
			return getRuleContexts(LineContext.class);
		}
		public LineContext line(int i) {
			return getRuleContext(LineContext.class,i);
		}
		public SettextCommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_settextCommand; }
	}

	public final SettextCommandContext settextCommand() throws RecognitionException {
		SettextCommandContext _localctx = new SettextCommandContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_settextCommand);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(359);
			match(SETTEXT);
			setState(361);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INTEGERLITERAL) {
				{
				setState(360);
				orientRotatedDegree();
				}
			}

			setState(364);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COLUMN || _la==MODERN || _la==TATE) {
				{
				setState(363);
				settextFormat();
				}
			}

			setState(367);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==AUTO || _la==SPACED) {
				{
				setState(366);
				settextAlignment();
				}
			}

			setState(370); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(369);
				line();
				}
				}
				setState(372); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LINE );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SettextFormatContext extends ParserRuleContext {
		public SettextFormatModernContext settextFormatModern() {
			return getRuleContext(SettextFormatModernContext.class,0);
		}
		public SettextFormatColumnContext settextFormatColumn() {
			return getRuleContext(SettextFormatColumnContext.class,0);
		}
		public SettextFormatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_settextFormat; }
	}

	public final SettextFormatContext settextFormat() throws RecognitionException {
		SettextFormatContext _localctx = new SettextFormatContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_settextFormat);
		try {
			setState(376);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case MODERN:
				enterOuterAlt(_localctx, 1);
				{
				setState(374);
				settextFormatModern();
				}
				break;
			case COLUMN:
			case TATE:
				enterOuterAlt(_localctx, 2);
				{
				setState(375);
				settextFormatColumn();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SettextFormatModernContext extends ParserRuleContext {
		public TerminalNode MODERN() { return getToken(OGLParser.MODERN, 0); }
		public SettextFormatPlacementContext settextFormatPlacement() {
			return getRuleContext(SettextFormatPlacementContext.class,0);
		}
		public SettextFormatModernContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_settextFormatModern; }
	}

	public final SettextFormatModernContext settextFormatModern() throws RecognitionException {
		SettextFormatModernContext _localctx = new SettextFormatModernContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_settextFormatModern);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(378);
			match(MODERN);
			setState(380);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 562949953456128L) != 0) || _la==RIGHT || _la==TOP) {
				{
				setState(379);
				settextFormatPlacement();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SettextFormatPlacementContext extends ParserRuleContext {
		public TerminalNode CENTER() { return getToken(OGLParser.CENTER, 0); }
		public TerminalNode TOP() { return getToken(OGLParser.TOP, 0); }
		public TerminalNode LEFT() { return getToken(OGLParser.LEFT, 0); }
		public TerminalNode RIGHT() { return getToken(OGLParser.RIGHT, 0); }
		public TerminalNode BOTTOM() { return getToken(OGLParser.BOTTOM, 0); }
		public SettextFormatPlacementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_settextFormatPlacement; }
	}

	public final SettextFormatPlacementContext settextFormatPlacement() throws RecognitionException {
		SettextFormatPlacementContext _localctx = new SettextFormatPlacementContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_settextFormatPlacement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(382);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 562949953456128L) != 0) || _la==RIGHT || _la==TOP) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SettextFormatColumnContext extends ParserRuleContext {
		public TerminalNode COLUMN() { return getToken(OGLParser.COLUMN, 0); }
		public TerminalNode TATE() { return getToken(OGLParser.TATE, 0); }
		public SettextFormatPlacementContext settextFormatPlacement() {
			return getRuleContext(SettextFormatPlacementContext.class,0);
		}
		public SettextFormatColumnContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_settextFormatColumn; }
	}

	public final SettextFormatColumnContext settextFormatColumn() throws RecognitionException {
		SettextFormatColumnContext _localctx = new SettextFormatColumnContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_settextFormatColumn);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(384);
			_la = _input.LA(1);
			if ( !(_la==COLUMN || _la==TATE) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(386);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 562949953456128L) != 0) || _la==RIGHT || _la==TOP) {
				{
				setState(385);
				settextFormatPlacement();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SettextAlignmentContext extends ParserRuleContext {
		public SettextAlignmentAutoContext settextAlignmentAuto() {
			return getRuleContext(SettextAlignmentAutoContext.class,0);
		}
		public SettextAlignmentSpacedContext settextAlignmentSpaced() {
			return getRuleContext(SettextAlignmentSpacedContext.class,0);
		}
		public SettextAlignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_settextAlignment; }
	}

	public final SettextAlignmentContext settextAlignment() throws RecognitionException {
		SettextAlignmentContext _localctx = new SettextAlignmentContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_settextAlignment);
		try {
			setState(390);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case AUTO:
				enterOuterAlt(_localctx, 1);
				{
				setState(388);
				settextAlignmentAuto();
				}
				break;
			case SPACED:
				enterOuterAlt(_localctx, 2);
				{
				setState(389);
				settextAlignmentSpaced();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SettextAlignmentAutoContext extends ParserRuleContext {
		public TerminalNode AUTO() { return getToken(OGLParser.AUTO, 0); }
		public SettextAlignmentAutoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_settextAlignmentAuto; }
	}

	public final SettextAlignmentAutoContext settextAlignmentAuto() throws RecognitionException {
		SettextAlignmentAutoContext _localctx = new SettextAlignmentAutoContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_settextAlignmentAuto);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(392);
			match(AUTO);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SettextAlignmentSpacedContext extends ParserRuleContext {
		public TerminalNode SPACED() { return getToken(OGLParser.SPACED, 0); }
		public SettextAlignmentValueContext settextAlignmentValue() {
			return getRuleContext(SettextAlignmentValueContext.class,0);
		}
		public SettextAlignmentSpacedContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_settextAlignmentSpaced; }
	}

	public final SettextAlignmentSpacedContext settextAlignmentSpaced() throws RecognitionException {
		SettextAlignmentSpacedContext _localctx = new SettextAlignmentSpacedContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_settextAlignmentSpaced);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(394);
			match(SPACED);
			setState(395);
			settextAlignmentValue();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SettextAlignmentValueContext extends ParserRuleContext {
		public OglMeasurementContext oglMeasurement() {
			return getRuleContext(OglMeasurementContext.class,0);
		}
		public SettextAlignmentValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_settextAlignmentValue; }
	}

	public final SettextAlignmentValueContext settextAlignmentValue() throws RecognitionException {
		SettextAlignmentValueContext _localctx = new SettextAlignmentValueContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_settextAlignmentValue);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(397);
			oglMeasurement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SetunitsCommandContext extends ParserRuleContext {
		public TerminalNode SETUNITS() { return getToken(OGLParser.SETUNITS, 0); }
		public SetunitsDefaultContext setunitsDefault() {
			return getRuleContext(SetunitsDefaultContext.class,0);
		}
		public SetunitsLineSpContext setunitsLineSp() {
			return getRuleContext(SetunitsLineSpContext.class,0);
		}
		public SetunitsCornerLengthContext setunitsCornerLength() {
			return getRuleContext(SetunitsCornerLengthContext.class,0);
		}
		public SetunitsTextMarginContext setunitsTextMargin() {
			return getRuleContext(SetunitsTextMarginContext.class,0);
		}
		public SetUnitsPositioningContext setUnitsPositioning() {
			return getRuleContext(SetUnitsPositioningContext.class,0);
		}
		public SetunitsCommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_setunitsCommand; }
	}

	public final SetunitsCommandContext setunitsCommand() throws RecognitionException {
		SetunitsCommandContext _localctx = new SetunitsCommandContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_setunitsCommand);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(399);
			match(SETUNITS);
			setState(401);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INTEGERLITERAL) {
				{
				setState(400);
				setunitsDefault();
				}
			}

			setState(404);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LINESP) {
				{
				setState(403);
				setunitsLineSp();
				}
			}

			setState(407);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==CORNERLENGTH) {
				{
				setState(406);
				setunitsCornerLength();
				}
			}

			setState(410);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==TEXTMARGIN) {
				{
				setState(409);
				setunitsTextMargin();
				}
			}

			setState(413);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==POSITIONING) {
				{
				setState(412);
				setUnitsPositioning();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SetunitsDefaultContext extends ParserRuleContext {
		public PrimaryDefaultContext primaryDefault() {
			return getRuleContext(PrimaryDefaultContext.class,0);
		}
		public SecondaryDefaultContext secondaryDefault() {
			return getRuleContext(SecondaryDefaultContext.class,0);
		}
		public SetunitsDefaultContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_setunitsDefault; }
	}

	public final SetunitsDefaultContext setunitsDefault() throws RecognitionException {
		SetunitsDefaultContext _localctx = new SetunitsDefaultContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_setunitsDefault);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(415);
			primaryDefault();
			setState(417);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INTEGERLITERAL) {
				{
				setState(416);
				secondaryDefault();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrimaryDefaultContext extends ParserRuleContext {
		public OglMeasurementContext oglMeasurement() {
			return getRuleContext(OglMeasurementContext.class,0);
		}
		public PrimaryDefaultContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primaryDefault; }
	}

	public final PrimaryDefaultContext primaryDefault() throws RecognitionException {
		PrimaryDefaultContext _localctx = new PrimaryDefaultContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_primaryDefault);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(419);
			oglMeasurement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SecondaryDefaultContext extends ParserRuleContext {
		public OglMeasurementContext oglMeasurement() {
			return getRuleContext(OglMeasurementContext.class,0);
		}
		public SecondaryDefaultContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_secondaryDefault; }
	}

	public final SecondaryDefaultContext secondaryDefault() throws RecognitionException {
		SecondaryDefaultContext _localctx = new SecondaryDefaultContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_secondaryDefault);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(421);
			oglMeasurement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SetunitsLineSpContext extends ParserRuleContext {
		public TerminalNode LINESP() { return getToken(OGLParser.LINESP, 0); }
		public OglMeasurementContext oglMeasurement() {
			return getRuleContext(OglMeasurementContext.class,0);
		}
		public SetunitsLineSpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_setunitsLineSp; }
	}

	public final SetunitsLineSpContext setunitsLineSp() throws RecognitionException {
		SetunitsLineSpContext _localctx = new SetunitsLineSpContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_setunitsLineSp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(423);
			match(LINESP);
			setState(424);
			oglMeasurement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SetunitsCornerLengthContext extends ParserRuleContext {
		public TerminalNode CORNERLENGTH() { return getToken(OGLParser.CORNERLENGTH, 0); }
		public ConrnerLengthValueContext conrnerLengthValue() {
			return getRuleContext(ConrnerLengthValueContext.class,0);
		}
		public SetunitsCornerLengthContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_setunitsCornerLength; }
	}

	public final SetunitsCornerLengthContext setunitsCornerLength() throws RecognitionException {
		SetunitsCornerLengthContext _localctx = new SetunitsCornerLengthContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_setunitsCornerLength);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(426);
			match(CORNERLENGTH);
			setState(427);
			conrnerLengthValue();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConrnerLengthValueContext extends ParserRuleContext {
		public OglMeasurementContext oglMeasurement() {
			return getRuleContext(OglMeasurementContext.class,0);
		}
		public TerminalNode MEDIUM() { return getToken(OGLParser.MEDIUM, 0); }
		public TerminalNode SMALL() { return getToken(OGLParser.SMALL, 0); }
		public TerminalNode LARGE() { return getToken(OGLParser.LARGE, 0); }
		public TerminalNode HALF() { return getToken(OGLParser.HALF, 0); }
		public TerminalNode MAX() { return getToken(OGLParser.MAX, 0); }
		public ConrnerLengthValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conrnerLengthValue; }
	}

	public final ConrnerLengthValueContext conrnerLengthValue() throws RecognitionException {
		ConrnerLengthValueContext _localctx = new ConrnerLengthValueContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_conrnerLengthValue);
		try {
			setState(435);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INTEGERLITERAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(429);
				oglMeasurement();
				}
				break;
			case MEDIUM:
				enterOuterAlt(_localctx, 2);
				{
				setState(430);
				match(MEDIUM);
				}
				break;
			case SMALL:
				enterOuterAlt(_localctx, 3);
				{
				setState(431);
				match(SMALL);
				}
				break;
			case LARGE:
				enterOuterAlt(_localctx, 4);
				{
				setState(432);
				match(LARGE);
				}
				break;
			case HALF:
				enterOuterAlt(_localctx, 5);
				{
				setState(433);
				match(HALF);
				}
				break;
			case MAX:
				enterOuterAlt(_localctx, 6);
				{
				setState(434);
				match(MAX);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SetunitsTextMarginContext extends ParserRuleContext {
		public TerminalNode TEXTMARGIN() { return getToken(OGLParser.TEXTMARGIN, 0); }
		public TextMarginValueContext textMarginValue() {
			return getRuleContext(TextMarginValueContext.class,0);
		}
		public SetunitsTextMarginContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_setunitsTextMargin; }
	}

	public final SetunitsTextMarginContext setunitsTextMargin() throws RecognitionException {
		SetunitsTextMarginContext _localctx = new SetunitsTextMarginContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_setunitsTextMargin);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(437);
			match(TEXTMARGIN);
			setState(438);
			textMarginValue();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TextMarginValueContext extends ParserRuleContext {
		public TerminalNode ROUNDED() { return getToken(OGLParser.ROUNDED, 0); }
		public TerminalNode SQUARE() { return getToken(OGLParser.SQUARE, 0); }
		public TextMarginValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_textMarginValue; }
	}

	public final TextMarginValueContext textMarginValue() throws RecognitionException {
		TextMarginValueContext _localctx = new TextMarginValueContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_textMarginValue);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(440);
			_la = _input.LA(1);
			if ( !(_la==ROUNDED || _la==SQUARE) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SetUnitsPositioningContext extends ParserRuleContext {
		public TerminalNode POSITIONING() { return getToken(OGLParser.POSITIONING, 0); }
		public PositionValueContext positionValue() {
			return getRuleContext(PositionValueContext.class,0);
		}
		public SetUnitsPositioningContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_setUnitsPositioning; }
	}

	public final SetUnitsPositioningContext setUnitsPositioning() throws RecognitionException {
		SetUnitsPositioningContext _localctx = new SetUnitsPositioningContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_setUnitsPositioning);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(442);
			match(POSITIONING);
			setState(443);
			positionValue();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PositionValueContext extends ParserRuleContext {
		public TerminalNode TOPLEFT() { return getToken(OGLParser.TOPLEFT, 0); }
		public TerminalNode CENTER() { return getToken(OGLParser.CENTER, 0); }
		public PositionValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_positionValue; }
	}

	public final PositionValueContext positionValue() throws RecognitionException {
		PositionValueContext _localctx = new PositionValueContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_positionValue);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(445);
			_la = _input.LA(1);
			if ( !(_la==CENTER || _la==TOPLEFT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PlaceCommandContext extends ParserRuleContext {
		public TerminalNode PLACE() { return getToken(OGLParser.PLACE, 0); }
		public GroupNameContext groupName() {
			return getRuleContext(GroupNameContext.class,0);
		}
		public TerminalNode SEGID() { return getToken(OGLParser.SEGID, 0); }
		public TerminalNode GROUP() { return getToken(OGLParser.GROUP, 0); }
		public PlaceCommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_placeCommand; }
	}

	public final PlaceCommandContext placeCommand() throws RecognitionException {
		PlaceCommandContext _localctx = new PlaceCommandContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_placeCommand);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(447);
			match(PLACE);
			setState(448);
			_la = _input.LA(1);
			if ( !(_la==GROUP || _la==SEGID) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(449);
			groupName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DrawruleCommandContext extends ParserRuleContext {
		public TerminalNode DRAWRULE() { return getToken(OGLParser.DRAWRULE, 0); }
		public RuleLengthContext ruleLength() {
			return getRuleContext(RuleLengthContext.class,0);
		}
		public RuleDirectionContext ruleDirection() {
			return getRuleContext(RuleDirectionContext.class,0);
		}
		public RuleThicknessContext ruleThickness() {
			return getRuleContext(RuleThicknessContext.class,0);
		}
		public RuleTypeContext ruleType() {
			return getRuleContext(RuleTypeContext.class,0);
		}
		public RuleRepeatedContext ruleRepeated() {
			return getRuleContext(RuleRepeatedContext.class,0);
		}
		public DrawruleCommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_drawruleCommand; }
	}

	public final DrawruleCommandContext drawruleCommand() throws RecognitionException {
		DrawruleCommandContext _localctx = new DrawruleCommandContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_drawruleCommand);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(451);
			match(DRAWRULE);
			setState(453);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ACROSS || _la==DOWN) {
				{
				setState(452);
				ruleDirection();
				}
			}

			setState(455);
			ruleLength();
			setState(457);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 145241087982699008L) != 0) || _la==INTEGERLITERAL) {
				{
				setState(456);
				ruleThickness();
				}
			}

			setState(460);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==DASHED || _la==DOTTED || _la==SOLID) {
				{
				setState(459);
				ruleType();
				}
			}

			setState(463);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==REPEAT) {
				{
				setState(462);
				ruleRepeated();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RuleDirectionContext extends ParserRuleContext {
		public TerminalNode ACROSS() { return getToken(OGLParser.ACROSS, 0); }
		public TerminalNode DOWN() { return getToken(OGLParser.DOWN, 0); }
		public RuleDirectionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ruleDirection; }
	}

	public final RuleDirectionContext ruleDirection() throws RecognitionException {
		RuleDirectionContext _localctx = new RuleDirectionContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_ruleDirection);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(465);
			_la = _input.LA(1);
			if ( !(_la==ACROSS || _la==DOWN) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RuleLengthContext extends ParserRuleContext {
		public OglMeasurementContext oglMeasurement() {
			return getRuleContext(OglMeasurementContext.class,0);
		}
		public RuleLengthContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ruleLength; }
	}

	public final RuleLengthContext ruleLength() throws RecognitionException {
		RuleLengthContext _localctx = new RuleLengthContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_ruleLength);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(467);
			oglMeasurement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RuleThicknessContext extends ParserRuleContext {
		public TerminalNode MEDIUM() { return getToken(OGLParser.MEDIUM, 0); }
		public TerminalNode LIGHT() { return getToken(OGLParser.LIGHT, 0); }
		public TerminalNode BOLD() { return getToken(OGLParser.BOLD, 0); }
		public TerminalNode INTEGERLITERAL() { return getToken(OGLParser.INTEGERLITERAL, 0); }
		public RuleThicknessContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ruleThickness; }
	}

	public final RuleThicknessContext ruleThickness() throws RecognitionException {
		RuleThicknessContext _localctx = new RuleThicknessContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_ruleThickness);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(469);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 145241087982699008L) != 0) || _la==INTEGERLITERAL) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RuleTypeContext extends ParserRuleContext {
		public TerminalNode SOLID() { return getToken(OGLParser.SOLID, 0); }
		public TerminalNode DASHED() { return getToken(OGLParser.DASHED, 0); }
		public TerminalNode DOTTED() { return getToken(OGLParser.DOTTED, 0); }
		public RuleTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ruleType; }
	}

	public final RuleTypeContext ruleType() throws RecognitionException {
		RuleTypeContext _localctx = new RuleTypeContext(_ctx, getState());
		enterRule(_localctx, 88, RULE_ruleType);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(471);
			_la = _input.LA(1);
			if ( !(_la==DASHED || _la==DOTTED || _la==SOLID) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RuleRepeatedContext extends ParserRuleContext {
		public TerminalNode REPEAT() { return getToken(OGLParser.REPEAT, 0); }
		public List<RuleRepeatAcrossContext> ruleRepeatAcross() {
			return getRuleContexts(RuleRepeatAcrossContext.class);
		}
		public RuleRepeatAcrossContext ruleRepeatAcross(int i) {
			return getRuleContext(RuleRepeatAcrossContext.class,i);
		}
		public List<RuleRepeatLocationContext> ruleRepeatLocation() {
			return getRuleContexts(RuleRepeatLocationContext.class);
		}
		public RuleRepeatLocationContext ruleRepeatLocation(int i) {
			return getRuleContext(RuleRepeatLocationContext.class,i);
		}
		public RuleRepeatedContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ruleRepeated; }
	}

	public final RuleRepeatedContext ruleRepeated() throws RecognitionException {
		RuleRepeatedContext _localctx = new RuleRepeatedContext(_ctx, getState());
		enterRule(_localctx, 90, RULE_ruleRepeated);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(473);
			match(REPEAT);
			setState(476); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(476);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case ACROSS:
				case DOWN:
				case INTEGERLITERAL:
					{
					setState(474);
					ruleRepeatAcross();
					}
					break;
				case LOCATION:
					{
					setState(475);
					ruleRepeatLocation();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(478); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 9007207844675616L) != 0) || _la==INTEGERLITERAL );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RuleRepeatAcrossContext extends ParserRuleContext {
		public RuleRepetitionContext ruleRepetition() {
			return getRuleContext(RuleRepetitionContext.class,0);
		}
		public TerminalNode SPACED() { return getToken(OGLParser.SPACED, 0); }
		public SpacedValueContext spacedValue() {
			return getRuleContext(SpacedValueContext.class,0);
		}
		public TerminalNode ACROSS() { return getToken(OGLParser.ACROSS, 0); }
		public TerminalNode DOWN() { return getToken(OGLParser.DOWN, 0); }
		public RuleRepeatAcrossContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ruleRepeatAcross; }
	}

	public final RuleRepeatAcrossContext ruleRepeatAcross() throws RecognitionException {
		RuleRepeatAcrossContext _localctx = new RuleRepeatAcrossContext(_ctx, getState());
		enterRule(_localctx, 92, RULE_ruleRepeatAcross);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(481);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ACROSS || _la==DOWN) {
				{
				setState(480);
				_la = _input.LA(1);
				if ( !(_la==ACROSS || _la==DOWN) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
			}

			setState(483);
			ruleRepetition();
			setState(484);
			match(SPACED);
			setState(485);
			spacedValue();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RuleRepetitionContext extends ParserRuleContext {
		public TerminalNode INTEGERLITERAL() { return getToken(OGLParser.INTEGERLITERAL, 0); }
		public RuleRepetitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ruleRepetition; }
	}

	public final RuleRepetitionContext ruleRepetition() throws RecognitionException {
		RuleRepetitionContext _localctx = new RuleRepetitionContext(_ctx, getState());
		enterRule(_localctx, 94, RULE_ruleRepetition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(487);
			match(INTEGERLITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RuleRepeatLocationContext extends ParserRuleContext {
		public TerminalNode LOCATION() { return getToken(OGLParser.LOCATION, 0); }
		public RuleRepeatHorizonalCoordinateContext ruleRepeatHorizonalCoordinate() {
			return getRuleContext(RuleRepeatHorizonalCoordinateContext.class,0);
		}
		public RuleRepeatVerticalCoordinateContext ruleRepeatVerticalCoordinate() {
			return getRuleContext(RuleRepeatVerticalCoordinateContext.class,0);
		}
		public RuleRepeatLocationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ruleRepeatLocation; }
	}

	public final RuleRepeatLocationContext ruleRepeatLocation() throws RecognitionException {
		RuleRepeatLocationContext _localctx = new RuleRepeatLocationContext(_ctx, getState());
		enterRule(_localctx, 96, RULE_ruleRepeatLocation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(489);
			match(LOCATION);
			setState(490);
			ruleRepeatHorizonalCoordinate();
			setState(491);
			ruleRepeatVerticalCoordinate();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RuleRepeatVerticalCoordinateContext extends ParserRuleContext {
		public OglMeasurementContext oglMeasurement() {
			return getRuleContext(OglMeasurementContext.class,0);
		}
		public RuleRepeatVerticalCoordinateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ruleRepeatVerticalCoordinate; }
	}

	public final RuleRepeatVerticalCoordinateContext ruleRepeatVerticalCoordinate() throws RecognitionException {
		RuleRepeatVerticalCoordinateContext _localctx = new RuleRepeatVerticalCoordinateContext(_ctx, getState());
		enterRule(_localctx, 98, RULE_ruleRepeatVerticalCoordinate);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(493);
			oglMeasurement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RuleRepeatHorizonalCoordinateContext extends ParserRuleContext {
		public OglMeasurementContext oglMeasurement() {
			return getRuleContext(OglMeasurementContext.class,0);
		}
		public RuleRepeatHorizonalCoordinateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ruleRepeatHorizonalCoordinate; }
	}

	public final RuleRepeatHorizonalCoordinateContext ruleRepeatHorizonalCoordinate() throws RecognitionException {
		RuleRepeatHorizonalCoordinateContext _localctx = new RuleRepeatHorizonalCoordinateContext(_ctx, getState());
		enterRule(_localctx, 100, RULE_ruleRepeatHorizonalCoordinate);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(495);
			oglMeasurement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DrawboxCommandContext extends ParserRuleContext {
		public TerminalNode DRAWBOX() { return getToken(OGLParser.DRAWBOX, 0); }
		public BoxWidthContext boxWidth() {
			return getRuleContext(BoxWidthContext.class,0);
		}
		public BoxHeightContext boxHeight() {
			return getRuleContext(BoxHeightContext.class,0);
		}
		public List<BoxBorderThicknessContext> boxBorderThickness() {
			return getRuleContexts(BoxBorderThicknessContext.class);
		}
		public BoxBorderThicknessContext boxBorderThickness(int i) {
			return getRuleContext(BoxBorderThicknessContext.class,i);
		}
		public List<BoxBorderTypeContext> boxBorderType() {
			return getRuleContexts(BoxBorderTypeContext.class);
		}
		public BoxBorderTypeContext boxBorderType(int i) {
			return getRuleContext(BoxBorderTypeContext.class,i);
		}
		public List<BoxRoundedContext> boxRounded() {
			return getRuleContexts(BoxRoundedContext.class);
		}
		public BoxRoundedContext boxRounded(int i) {
			return getRuleContext(BoxRoundedContext.class,i);
		}
		public List<BoxDiagonalContext> boxDiagonal() {
			return getRuleContexts(BoxDiagonalContext.class);
		}
		public BoxDiagonalContext boxDiagonal(int i) {
			return getRuleContext(BoxDiagonalContext.class,i);
		}
		public List<BoxRepeatContext> boxRepeat() {
			return getRuleContexts(BoxRepeatContext.class);
		}
		public BoxRepeatContext boxRepeat(int i) {
			return getRuleContext(BoxRepeatContext.class,i);
		}
		public List<BoxShadeContext> boxShade() {
			return getRuleContexts(BoxShadeContext.class);
		}
		public BoxShadeContext boxShade(int i) {
			return getRuleContext(BoxShadeContext.class,i);
		}
		public List<BoxColorContext> boxColor() {
			return getRuleContexts(BoxColorContext.class);
		}
		public BoxColorContext boxColor(int i) {
			return getRuleContext(BoxColorContext.class,i);
		}
		public List<BoxWithtextContext> boxWithtext() {
			return getRuleContexts(BoxWithtextContext.class);
		}
		public BoxWithtextContext boxWithtext(int i) {
			return getRuleContext(BoxWithtextContext.class,i);
		}
		public DrawboxCommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_drawboxCommand; }
	}

	public final DrawboxCommandContext drawboxCommand() throws RecognitionException {
		DrawboxCommandContext _localctx = new DrawboxCommandContext(_ctx, getState());
		enterRule(_localctx, 102, RULE_drawboxCommand);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(497);
			match(DRAWBOX);
			setState(498);
			boxWidth();
			setState(499);
			boxHeight();
			setState(510);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 145241089358955008L) != 0) || ((((_la - 77)) & ~0x3f) == 0 && ((1L << (_la - 77)) & 146028906505L) != 0)) {
				{
				setState(508);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case BOLD:
				case LIGHT:
				case MEDIUM:
				case INTEGERLITERAL:
					{
					setState(500);
					boxBorderThickness();
					}
					break;
				case DASHED:
				case DOTTED:
				case SOLID:
					{
					setState(501);
					boxBorderType();
					}
					break;
				case ROUNDED:
					{
					setState(502);
					boxRounded();
					}
					break;
				case DIAGONAL:
					{
					setState(503);
					boxDiagonal();
					}
					break;
				case REPEAT:
					{
					setState(504);
					boxRepeat();
					}
					break;
				case SHADE:
					{
					setState(505);
					boxShade();
					}
					break;
				case COLOR:
					{
					setState(506);
					boxColor();
					}
					break;
				case WITHTEXT:
					{
					setState(507);
					boxWithtext();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(512);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BoxWidthContext extends ParserRuleContext {
		public OglMeasurementContext oglMeasurement() {
			return getRuleContext(OglMeasurementContext.class,0);
		}
		public BoxWidthContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boxWidth; }
	}

	public final BoxWidthContext boxWidth() throws RecognitionException {
		BoxWidthContext _localctx = new BoxWidthContext(_ctx, getState());
		enterRule(_localctx, 104, RULE_boxWidth);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(513);
			oglMeasurement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BoxHeightContext extends ParserRuleContext {
		public OglMeasurementContext oglMeasurement() {
			return getRuleContext(OglMeasurementContext.class,0);
		}
		public BoxHeightContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boxHeight; }
	}

	public final BoxHeightContext boxHeight() throws RecognitionException {
		BoxHeightContext _localctx = new BoxHeightContext(_ctx, getState());
		enterRule(_localctx, 106, RULE_boxHeight);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(515);
			oglMeasurement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BoxBorderThicknessContext extends ParserRuleContext {
		public TerminalNode MEDIUM() { return getToken(OGLParser.MEDIUM, 0); }
		public TerminalNode LIGHT() { return getToken(OGLParser.LIGHT, 0); }
		public TerminalNode BOLD() { return getToken(OGLParser.BOLD, 0); }
		public TerminalNode INTEGERLITERAL() { return getToken(OGLParser.INTEGERLITERAL, 0); }
		public BoxBorderThicknessContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boxBorderThickness; }
	}

	public final BoxBorderThicknessContext boxBorderThickness() throws RecognitionException {
		BoxBorderThicknessContext _localctx = new BoxBorderThicknessContext(_ctx, getState());
		enterRule(_localctx, 108, RULE_boxBorderThickness);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(517);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 145241087982699008L) != 0) || _la==INTEGERLITERAL) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BoxBorderTypeContext extends ParserRuleContext {
		public TerminalNode SOLID() { return getToken(OGLParser.SOLID, 0); }
		public TerminalNode DASHED() { return getToken(OGLParser.DASHED, 0); }
		public TerminalNode DOTTED() { return getToken(OGLParser.DOTTED, 0); }
		public BoxBorderTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boxBorderType; }
	}

	public final BoxBorderTypeContext boxBorderType() throws RecognitionException {
		BoxBorderTypeContext _localctx = new BoxBorderTypeContext(_ctx, getState());
		enterRule(_localctx, 110, RULE_boxBorderType);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(519);
			_la = _input.LA(1);
			if ( !(_la==DASHED || _la==DOTTED || _la==SOLID) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BoxRoundedContext extends ParserRuleContext {
		public TerminalNode ROUNDED() { return getToken(OGLParser.ROUNDED, 0); }
		public BoxRoundedOptionContext boxRoundedOption() {
			return getRuleContext(BoxRoundedOptionContext.class,0);
		}
		public BoxRoundedContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boxRounded; }
	}

	public final BoxRoundedContext boxRounded() throws RecognitionException {
		BoxRoundedContext _localctx = new BoxRoundedContext(_ctx, getState());
		enterRule(_localctx, 112, RULE_boxRounded);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(521);
			match(ROUNDED);
			setState(523);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 12352L) != 0) || _la==TOPLEFT || _la==TOPRIGHT) {
				{
				setState(522);
				boxRoundedOption();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BoxRoundedOptionContext extends ParserRuleContext {
		public TerminalNode ALL() { return getToken(OGLParser.ALL, 0); }
		public List<TerminalNode> TOPLEFT() { return getTokens(OGLParser.TOPLEFT); }
		public TerminalNode TOPLEFT(int i) {
			return getToken(OGLParser.TOPLEFT, i);
		}
		public List<TerminalNode> TOPRIGHT() { return getTokens(OGLParser.TOPRIGHT); }
		public TerminalNode TOPRIGHT(int i) {
			return getToken(OGLParser.TOPRIGHT, i);
		}
		public List<TerminalNode> BOTTOMLEFT() { return getTokens(OGLParser.BOTTOMLEFT); }
		public TerminalNode BOTTOMLEFT(int i) {
			return getToken(OGLParser.BOTTOMLEFT, i);
		}
		public List<TerminalNode> BOTTOMRIGHT() { return getTokens(OGLParser.BOTTOMRIGHT); }
		public TerminalNode BOTTOMRIGHT(int i) {
			return getToken(OGLParser.BOTTOMRIGHT, i);
		}
		public BoxRoundedOptionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boxRoundedOption; }
	}

	public final BoxRoundedOptionContext boxRoundedOption() throws RecognitionException {
		BoxRoundedOptionContext _localctx = new BoxRoundedOptionContext(_ctx, getState());
		enterRule(_localctx, 114, RULE_boxRoundedOption);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(531);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ALL:
				{
				setState(525);
				match(ALL);
				}
				break;
			case BOTTOMLEFT:
			case BOTTOMRIGHT:
			case TOPLEFT:
			case TOPRIGHT:
				{
				setState(527); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(526);
					_la = _input.LA(1);
					if ( !(_la==BOTTOMLEFT || _la==BOTTOMRIGHT || _la==TOPLEFT || _la==TOPRIGHT) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
					}
					setState(529); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==BOTTOMLEFT || _la==BOTTOMRIGHT || _la==TOPLEFT || _la==TOPRIGHT );
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BoxDiagonalContext extends ParserRuleContext {
		public TerminalNode DIAGONAL() { return getToken(OGLParser.DIAGONAL, 0); }
		public BoxDiagonalOptionContext boxDiagonalOption() {
			return getRuleContext(BoxDiagonalOptionContext.class,0);
		}
		public BoxDiagonalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boxDiagonal; }
	}

	public final BoxDiagonalContext boxDiagonal() throws RecognitionException {
		BoxDiagonalContext _localctx = new BoxDiagonalContext(_ctx, getState());
		enterRule(_localctx, 116, RULE_boxDiagonal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(533);
			match(DIAGONAL);
			setState(534);
			boxDiagonalOption();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BoxDiagonalOptionContext extends ParserRuleContext {
		public TerminalNode LEFT() { return getToken(OGLParser.LEFT, 0); }
		public TerminalNode RIGHT() { return getToken(OGLParser.RIGHT, 0); }
		public TerminalNode BOTH() { return getToken(OGLParser.BOTH, 0); }
		public BoxDiagonalOptionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boxDiagonalOption; }
	}

	public final BoxDiagonalOptionContext boxDiagonalOption() throws RecognitionException {
		BoxDiagonalOptionContext _localctx = new BoxDiagonalOptionContext(_ctx, getState());
		enterRule(_localctx, 118, RULE_boxDiagonalOption);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(536);
			_la = _input.LA(1);
			if ( !(_la==BOTH || _la==LEFT || _la==RIGHT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BoxRepeatContext extends ParserRuleContext {
		public TerminalNode REPEAT() { return getToken(OGLParser.REPEAT, 0); }
		public List<BoxRepeatAcrossDownContext> boxRepeatAcrossDown() {
			return getRuleContexts(BoxRepeatAcrossDownContext.class);
		}
		public BoxRepeatAcrossDownContext boxRepeatAcrossDown(int i) {
			return getRuleContext(BoxRepeatAcrossDownContext.class,i);
		}
		public List<BoxRepeatSpacedContext> boxRepeatSpaced() {
			return getRuleContexts(BoxRepeatSpacedContext.class);
		}
		public BoxRepeatSpacedContext boxRepeatSpaced(int i) {
			return getRuleContext(BoxRepeatSpacedContext.class,i);
		}
		public BoxRepeatLocationContext boxRepeatLocation() {
			return getRuleContext(BoxRepeatLocationContext.class,0);
		}
		public BoxRepeatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boxRepeat; }
	}

	public final BoxRepeatContext boxRepeat() throws RecognitionException {
		BoxRepeatContext _localctx = new BoxRepeatContext(_ctx, getState());
		enterRule(_localctx, 120, RULE_boxRepeat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(538);
			match(REPEAT);
			setState(541); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(541);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case ACROSS:
				case DOWN:
					{
					setState(539);
					boxRepeatAcrossDown();
					}
					break;
				case SPACED:
					{
					setState(540);
					boxRepeatSpaced();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(543); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ACROSS || _la==DOWN || _la==SPACED );
			setState(546);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LOCATION) {
				{
				setState(545);
				boxRepeatLocation();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BoxRepeatLocationContext extends ParserRuleContext {
		public TerminalNode LOCATION() { return getToken(OGLParser.LOCATION, 0); }
		public BoxRepeatHorizonalCoordinateContext boxRepeatHorizonalCoordinate() {
			return getRuleContext(BoxRepeatHorizonalCoordinateContext.class,0);
		}
		public BoxRepeatVerticalCoordinateContext boxRepeatVerticalCoordinate() {
			return getRuleContext(BoxRepeatVerticalCoordinateContext.class,0);
		}
		public BoxRepeatLocationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boxRepeatLocation; }
	}

	public final BoxRepeatLocationContext boxRepeatLocation() throws RecognitionException {
		BoxRepeatLocationContext _localctx = new BoxRepeatLocationContext(_ctx, getState());
		enterRule(_localctx, 122, RULE_boxRepeatLocation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(548);
			match(LOCATION);
			setState(549);
			boxRepeatHorizonalCoordinate();
			setState(550);
			boxRepeatVerticalCoordinate();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BoxRepeatVerticalCoordinateContext extends ParserRuleContext {
		public OglMeasurementContext oglMeasurement() {
			return getRuleContext(OglMeasurementContext.class,0);
		}
		public BoxRepeatVerticalCoordinateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boxRepeatVerticalCoordinate; }
	}

	public final BoxRepeatVerticalCoordinateContext boxRepeatVerticalCoordinate() throws RecognitionException {
		BoxRepeatVerticalCoordinateContext _localctx = new BoxRepeatVerticalCoordinateContext(_ctx, getState());
		enterRule(_localctx, 124, RULE_boxRepeatVerticalCoordinate);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(552);
			oglMeasurement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BoxRepeatHorizonalCoordinateContext extends ParserRuleContext {
		public OglMeasurementContext oglMeasurement() {
			return getRuleContext(OglMeasurementContext.class,0);
		}
		public BoxRepeatHorizonalCoordinateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boxRepeatHorizonalCoordinate; }
	}

	public final BoxRepeatHorizonalCoordinateContext boxRepeatHorizonalCoordinate() throws RecognitionException {
		BoxRepeatHorizonalCoordinateContext _localctx = new BoxRepeatHorizonalCoordinateContext(_ctx, getState());
		enterRule(_localctx, 126, RULE_boxRepeatHorizonalCoordinate);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(554);
			oglMeasurement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BoxRepeatAcrossDownContext extends ParserRuleContext {
		public BoxRepetitionContext boxRepetition() {
			return getRuleContext(BoxRepetitionContext.class,0);
		}
		public TerminalNode ACROSS() { return getToken(OGLParser.ACROSS, 0); }
		public TerminalNode DOWN() { return getToken(OGLParser.DOWN, 0); }
		public BoxRepeatAcrossDownContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boxRepeatAcrossDown; }
	}

	public final BoxRepeatAcrossDownContext boxRepeatAcrossDown() throws RecognitionException {
		BoxRepeatAcrossDownContext _localctx = new BoxRepeatAcrossDownContext(_ctx, getState());
		enterRule(_localctx, 128, RULE_boxRepeatAcrossDown);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(556);
			_la = _input.LA(1);
			if ( !(_la==ACROSS || _la==DOWN) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(557);
			boxRepetition();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BoxRepetitionContext extends ParserRuleContext {
		public TerminalNode INTEGERLITERAL() { return getToken(OGLParser.INTEGERLITERAL, 0); }
		public BoxRepetitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boxRepetition; }
	}

	public final BoxRepetitionContext boxRepetition() throws RecognitionException {
		BoxRepetitionContext _localctx = new BoxRepetitionContext(_ctx, getState());
		enterRule(_localctx, 130, RULE_boxRepetition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(559);
			match(INTEGERLITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BoxRepeatSpacedContext extends ParserRuleContext {
		public TerminalNode SPACED() { return getToken(OGLParser.SPACED, 0); }
		public SpacedValueContext spacedValue() {
			return getRuleContext(SpacedValueContext.class,0);
		}
		public BoxRepeatSpacedContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boxRepeatSpaced; }
	}

	public final BoxRepeatSpacedContext boxRepeatSpaced() throws RecognitionException {
		BoxRepeatSpacedContext _localctx = new BoxRepeatSpacedContext(_ctx, getState());
		enterRule(_localctx, 132, RULE_boxRepeatSpaced);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(561);
			match(SPACED);
			setState(562);
			spacedValue();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SpacedValueContext extends ParserRuleContext {
		public TerminalNode DIAMETER() { return getToken(OGLParser.DIAMETER, 0); }
		public OglMeasurementContext oglMeasurement() {
			return getRuleContext(OglMeasurementContext.class,0);
		}
		public SpacedValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_spacedValue; }
	}

	public final SpacedValueContext spacedValue() throws RecognitionException {
		SpacedValueContext _localctx = new SpacedValueContext(_ctx, getState());
		enterRule(_localctx, 134, RULE_spacedValue);
		try {
			setState(566);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case DIAMETER:
				enterOuterAlt(_localctx, 1);
				{
				setState(564);
				match(DIAMETER);
				}
				break;
			case INTEGERLITERAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(565);
				oglMeasurement();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BoxShadeContext extends ParserRuleContext {
		public TerminalNode SHADE() { return getToken(OGLParser.SHADE, 0); }
		public BoxContext box() {
			return getRuleContext(BoxContext.class,0);
		}
		public ShadeAreaContext shadeArea() {
			return getRuleContext(ShadeAreaContext.class,0);
		}
		public ShadePatternContext shadePattern() {
			return getRuleContext(ShadePatternContext.class,0);
		}
		public ShadeTypeContext shadeType() {
			return getRuleContext(ShadeTypeContext.class,0);
		}
		public BoxShadeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boxShade; }
	}

	public final BoxShadeContext boxShade() throws RecognitionException {
		BoxShadeContext _localctx = new BoxShadeContext(_ctx, getState());
		enterRule(_localctx, 136, RULE_boxShade);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(568);
			match(SHADE);
			setState(570);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ALL || _la==BOX) {
				{
				setState(569);
				box();
				}
			}

			setState(573);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==BOTTOM || _la==LEFT || ((((_la - 79)) & ~0x3f) == 0 && ((1L << (_la - 79)) & 1082130433L) != 0)) {
				{
				setState(572);
				shadeArea();
				}
			}

			setState(576);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SCREEN || _la==STANDARD) {
				{
				setState(575);
				shadePattern();
				}
			}

			setState(579);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,50,_ctx) ) {
			case 1:
				{
				setState(578);
				shadeType();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BoxContext extends ParserRuleContext {
		public TerminalNode ALL() { return getToken(OGLParser.ALL, 0); }
		public TerminalNode BOX() { return getToken(OGLParser.BOX, 0); }
		public TerminalNode INTEGERLITERAL() { return getToken(OGLParser.INTEGERLITERAL, 0); }
		public BoxContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_box; }
	}

	public final BoxContext box() throws RecognitionException {
		BoxContext _localctx = new BoxContext(_ctx, getState());
		enterRule(_localctx, 138, RULE_box);
		try {
			setState(584);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ALL:
				enterOuterAlt(_localctx, 1);
				{
				setState(581);
				match(ALL);
				}
				break;
			case BOX:
				enterOuterAlt(_localctx, 2);
				{
				setState(582);
				match(BOX);
				setState(583);
				match(INTEGERLITERAL);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ShadeAreaContext extends ParserRuleContext {
		public TerminalNode WHOLE() { return getToken(OGLParser.WHOLE, 0); }
		public TerminalNode LEFT() { return getToken(OGLParser.LEFT, 0); }
		public TerminalNode RIGHT() { return getToken(OGLParser.RIGHT, 0); }
		public TerminalNode TOP() { return getToken(OGLParser.TOP, 0); }
		public TerminalNode BOTTOM() { return getToken(OGLParser.BOTTOM, 0); }
		public ShadeAreaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_shadeArea; }
	}

	public final ShadeAreaContext shadeArea() throws RecognitionException {
		ShadeAreaContext _localctx = new ShadeAreaContext(_ctx, getState());
		enterRule(_localctx, 140, RULE_shadeArea);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(586);
			_la = _input.LA(1);
			if ( !(_la==BOTTOM || _la==LEFT || ((((_la - 79)) & ~0x3f) == 0 && ((1L << (_la - 79)) & 1082130433L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ShadePatternContext extends ParserRuleContext {
		public TerminalNode STANDARD() { return getToken(OGLParser.STANDARD, 0); }
		public TerminalNode SCREEN() { return getToken(OGLParser.SCREEN, 0); }
		public ShadePatternContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_shadePattern; }
	}

	public final ShadePatternContext shadePattern() throws RecognitionException {
		ShadePatternContext _localctx = new ShadePatternContext(_ctx, getState());
		enterRule(_localctx, 142, RULE_shadePattern);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(588);
			_la = _input.LA(1);
			if ( !(_la==SCREEN || _la==STANDARD) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ShadeTypeContext extends ParserRuleContext {
		public TerminalNode MEDIUM() { return getToken(OGLParser.MEDIUM, 0); }
		public TerminalNode XLIGHT() { return getToken(OGLParser.XLIGHT, 0); }
		public TerminalNode LIGHT() { return getToken(OGLParser.LIGHT, 0); }
		public TerminalNode DARK() { return getToken(OGLParser.DARK, 0); }
		public TerminalNode XDARK() { return getToken(OGLParser.XDARK, 0); }
		public TerminalNode INTEGERLITERAL() { return getToken(OGLParser.INTEGERLITERAL, 0); }
		public ShadeTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_shadeType; }
	}

	public final ShadeTypeContext shadeType() throws RecognitionException {
		ShadeTypeContext _localctx = new ShadeTypeContext(_ctx, getState());
		enterRule(_localctx, 144, RULE_shadeType);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(590);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 145241087999475712L) != 0) || ((((_la - 111)) & ~0x3f) == 0 && ((1L << (_la - 111)) & 11L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BoxColorContext extends ParserRuleContext {
		public TerminalNode COLOR() { return getToken(OGLParser.COLOR, 0); }
		public BoxContext box() {
			return getRuleContext(BoxContext.class,0);
		}
		public BoxColorNameContext boxColorName() {
			return getRuleContext(BoxColorNameContext.class,0);
		}
		public BoxColorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boxColor; }
	}

	public final BoxColorContext boxColor() throws RecognitionException {
		BoxColorContext _localctx = new BoxColorContext(_ctx, getState());
		enterRule(_localctx, 146, RULE_boxColor);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(592);
			match(COLOR);
			setState(593);
			box();
			setState(594);
			boxColorName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BoxColorNameContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(OGLParser.IDENTIFIER, 0); }
		public BoxColorNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boxColorName; }
	}

	public final BoxColorNameContext boxColorName() throws RecognitionException {
		BoxColorNameContext _localctx = new BoxColorNameContext(_ctx, getState());
		enterRule(_localctx, 148, RULE_boxColorName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(596);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BoxWithtextContext extends ParserRuleContext {
		public TerminalNode WITHTEXT() { return getToken(OGLParser.WITHTEXT, 0); }
		public LineContext line() {
			return getRuleContext(LineContext.class,0);
		}
		public BoxContext box() {
			return getRuleContext(BoxContext.class,0);
		}
		public BoxWithtextOrientContext boxWithtextOrient() {
			return getRuleContext(BoxWithtextOrientContext.class,0);
		}
		public BoxWithtextFormatContext boxWithtextFormat() {
			return getRuleContext(BoxWithtextFormatContext.class,0);
		}
		public BoxWithtextLineSpacingContext boxWithtextLineSpacing() {
			return getRuleContext(BoxWithtextLineSpacingContext.class,0);
		}
		public BoxWithtextContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boxWithtext; }
	}

	public final BoxWithtextContext boxWithtext() throws RecognitionException {
		BoxWithtextContext _localctx = new BoxWithtextContext(_ctx, getState());
		enterRule(_localctx, 150, RULE_boxWithtext);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(598);
			match(WITHTEXT);
			setState(600);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ALL || _la==BOX) {
				{
				setState(599);
				box();
				}
			}

			setState(603);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INTEGERLITERAL) {
				{
				setState(602);
				boxWithtextOrient();
				}
			}

			setState(606);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 577094071002106112L) != 0) || ((((_la - 79)) & ~0x3f) == 0 && ((1L << (_la - 79)) & 10485761L) != 0)) {
				{
				setState(605);
				boxWithtextFormat();
				}
			}

			setState(609);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==AUTO || _la==SPACED) {
				{
				setState(608);
				boxWithtextLineSpacing();
				}
			}

			setState(611);
			line();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BoxWithtextOrientContext extends ParserRuleContext {
		public TerminalNode INTEGERLITERAL() { return getToken(OGLParser.INTEGERLITERAL, 0); }
		public BoxWithtextOrientContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boxWithtextOrient; }
	}

	public final BoxWithtextOrientContext boxWithtextOrient() throws RecognitionException {
		BoxWithtextOrientContext _localctx = new BoxWithtextOrientContext(_ctx, getState());
		enterRule(_localctx, 152, RULE_boxWithtextOrient);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(613);
			match(INTEGERLITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BoxWithtextLineSpacingContext extends ParserRuleContext {
		public TerminalNode AUTO() { return getToken(OGLParser.AUTO, 0); }
		public TerminalNode SPACED() { return getToken(OGLParser.SPACED, 0); }
		public OglMeasurementContext oglMeasurement() {
			return getRuleContext(OglMeasurementContext.class,0);
		}
		public BoxWithtextLineSpacingContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boxWithtextLineSpacing; }
	}

	public final BoxWithtextLineSpacingContext boxWithtextLineSpacing() throws RecognitionException {
		BoxWithtextLineSpacingContext _localctx = new BoxWithtextLineSpacingContext(_ctx, getState());
		enterRule(_localctx, 154, RULE_boxWithtextLineSpacing);
		try {
			setState(618);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case AUTO:
				enterOuterAlt(_localctx, 1);
				{
				setState(615);
				match(AUTO);
				}
				break;
			case SPACED:
				enterOuterAlt(_localctx, 2);
				{
				setState(616);
				match(SPACED);
				setState(617);
				oglMeasurement();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LineContext extends ParserRuleContext {
		public TerminalNode LINE() { return getToken(OGLParser.LINE, 0); }
		public List<Line_partContext> line_part() {
			return getRuleContexts(Line_partContext.class);
		}
		public Line_partContext line_part(int i) {
			return getRuleContext(Line_partContext.class,i);
		}
		public LineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_line; }
	}

	public final LineContext line() throws RecognitionException {
		LineContext _localctx = new LineContext(_ctx, getState());
		enterRule(_localctx, 156, RULE_line);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(620);
			match(LINE);
			setState(622); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(621);
				line_part();
				}
				}
				setState(624); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==IDENTIFIER );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Line_partContext extends ParserRuleContext {
		public List<FontNameContext> fontName() {
			return getRuleContexts(FontNameContext.class);
		}
		public FontNameContext fontName(int i) {
			return getRuleContext(FontNameContext.class,i);
		}
		public LineSosiModeContext lineSosiMode() {
			return getRuleContext(LineSosiModeContext.class,0);
		}
		public LineUnderlyingContext lineUnderlying() {
			return getRuleContext(LineUnderlyingContext.class,0);
		}
		public LineTextTypeContext lineTextType() {
			return getRuleContext(LineTextTypeContext.class,0);
		}
		public List<TextContext> text() {
			return getRuleContexts(TextContext.class);
		}
		public TextContext text(int i) {
			return getRuleContext(TextContext.class,i);
		}
		public Line_partContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_line_part; }
	}

	public final Line_partContext line_part() throws RecognitionException {
		Line_partContext _localctx = new Line_partContext(_ctx, getState());
		enterRule(_localctx, 158, RULE_line_part);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(627); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(626);
				fontName();
				}
				}
				setState(629); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==IDENTIFIER );
			setState(632);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SOSI1 || _la==SOSI2) {
				{
				setState(631);
				lineSosiMode();
				}
			}

			setState(635);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NOUNDERLINE || _la==UNDERLINE) {
				{
				setState(634);
				lineUnderlying();
				}
			}

			setState(638);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==CHAR || _la==HEX) {
				{
				setState(637);
				lineTextType();
				}
			}

			setState(641); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(640);
				text();
				}
				}
				setState(643); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==STRINGLITERAL );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TextContext extends ParserRuleContext {
		public TerminalNode STRINGLITERAL() { return getToken(OGLParser.STRINGLITERAL, 0); }
		public TextContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_text; }
	}

	public final TextContext text() throws RecognitionException {
		TextContext _localctx = new TextContext(_ctx, getState());
		enterRule(_localctx, 160, RULE_text);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(645);
			match(STRINGLITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LineSosiModeContext extends ParserRuleContext {
		public TerminalNode SOSI1() { return getToken(OGLParser.SOSI1, 0); }
		public TerminalNode SOSI2() { return getToken(OGLParser.SOSI2, 0); }
		public LineSosiModeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lineSosiMode; }
	}

	public final LineSosiModeContext lineSosiMode() throws RecognitionException {
		LineSosiModeContext _localctx = new LineSosiModeContext(_ctx, getState());
		enterRule(_localctx, 162, RULE_lineSosiMode);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(647);
			_la = _input.LA(1);
			if ( !(_la==SOSI1 || _la==SOSI2) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LineUnderlyingContext extends ParserRuleContext {
		public TerminalNode NOUNDERLINE() { return getToken(OGLParser.NOUNDERLINE, 0); }
		public TerminalNode UNDERLINE() { return getToken(OGLParser.UNDERLINE, 0); }
		public LineUnderlyingContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lineUnderlying; }
	}

	public final LineUnderlyingContext lineUnderlying() throws RecognitionException {
		LineUnderlyingContext _localctx = new LineUnderlyingContext(_ctx, getState());
		enterRule(_localctx, 164, RULE_lineUnderlying);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(649);
			_la = _input.LA(1);
			if ( !(_la==NOUNDERLINE || _la==UNDERLINE) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LineTextTypeContext extends ParserRuleContext {
		public TerminalNode CHAR() { return getToken(OGLParser.CHAR, 0); }
		public TerminalNode HEX() { return getToken(OGLParser.HEX, 0); }
		public LineTextTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lineTextType; }
	}

	public final LineTextTypeContext lineTextType() throws RecognitionException {
		LineTextTypeContext _localctx = new LineTextTypeContext(_ctx, getState());
		enterRule(_localctx, 166, RULE_lineTextType);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(651);
			_la = _input.LA(1);
			if ( !(_la==CHAR || _la==HEX) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BoxWithtextFormatContext extends ParserRuleContext {
		public BoxWithtextFormatModernContext boxWithtextFormatModern() {
			return getRuleContext(BoxWithtextFormatModernContext.class,0);
		}
		public BoxWithtextFormatColumnContext boxWithtextFormatColumn() {
			return getRuleContext(BoxWithtextFormatColumnContext.class,0);
		}
		public BoxWithtextFormatPlacementContext boxWithtextFormatPlacement() {
			return getRuleContext(BoxWithtextFormatPlacementContext.class,0);
		}
		public BoxWithtextFormatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boxWithtextFormat; }
	}

	public final BoxWithtextFormatContext boxWithtextFormat() throws RecognitionException {
		BoxWithtextFormatContext _localctx = new BoxWithtextFormatContext(_ctx, getState());
		enterRule(_localctx, 168, RULE_boxWithtextFormat);
		try {
			setState(656);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case MODERN:
				enterOuterAlt(_localctx, 1);
				{
				setState(653);
				boxWithtextFormatModern();
				}
				break;
			case COLUMN:
			case TATE:
				enterOuterAlt(_localctx, 2);
				{
				setState(654);
				boxWithtextFormatColumn();
				}
				break;
			case BALANCE:
			case BOTTOM:
			case CENTER:
			case JUSTIFY:
			case LEFT:
			case RIGHT:
			case TOP:
				enterOuterAlt(_localctx, 3);
				{
				setState(655);
				boxWithtextFormatPlacement();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BoxWithtextFormatModernContext extends ParserRuleContext {
		public TerminalNode MODERN() { return getToken(OGLParser.MODERN, 0); }
		public BoxWithtextFormatPlacementContext boxWithtextFormatPlacement() {
			return getRuleContext(BoxWithtextFormatPlacementContext.class,0);
		}
		public BoxWithtextFormatModernContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boxWithtextFormatModern; }
	}

	public final BoxWithtextFormatModernContext boxWithtextFormatModern() throws RecognitionException {
		BoxWithtextFormatModernContext _localctx = new BoxWithtextFormatModernContext(_ctx, getState());
		enterRule(_localctx, 170, RULE_boxWithtextFormatModern);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(658);
			match(MODERN);
			setState(660);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 633318697634048L) != 0) || _la==RIGHT || _la==TOP) {
				{
				setState(659);
				boxWithtextFormatPlacement();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BoxWithtextFormatPlacementContext extends ParserRuleContext {
		public List<TerminalNode> CENTER() { return getTokens(OGLParser.CENTER); }
		public TerminalNode CENTER(int i) {
			return getToken(OGLParser.CENTER, i);
		}
		public List<TerminalNode> TOP() { return getTokens(OGLParser.TOP); }
		public TerminalNode TOP(int i) {
			return getToken(OGLParser.TOP, i);
		}
		public List<TerminalNode> BOTTOM() { return getTokens(OGLParser.BOTTOM); }
		public TerminalNode BOTTOM(int i) {
			return getToken(OGLParser.BOTTOM, i);
		}
		public List<TerminalNode> LEFT() { return getTokens(OGLParser.LEFT); }
		public TerminalNode LEFT(int i) {
			return getToken(OGLParser.LEFT, i);
		}
		public List<TerminalNode> RIGHT() { return getTokens(OGLParser.RIGHT); }
		public TerminalNode RIGHT(int i) {
			return getToken(OGLParser.RIGHT, i);
		}
		public List<TerminalNode> BALANCE() { return getTokens(OGLParser.BALANCE); }
		public TerminalNode BALANCE(int i) {
			return getToken(OGLParser.BALANCE, i);
		}
		public List<TerminalNode> JUSTIFY() { return getTokens(OGLParser.JUSTIFY); }
		public TerminalNode JUSTIFY(int i) {
			return getToken(OGLParser.JUSTIFY, i);
		}
		public List<TerminalNode> LASTNO() { return getTokens(OGLParser.LASTNO); }
		public TerminalNode LASTNO(int i) {
			return getToken(OGLParser.LASTNO, i);
		}
		public BoxWithtextFormatPlacementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boxWithtextFormatPlacement; }
	}

	public final BoxWithtextFormatPlacementContext boxWithtextFormatPlacement() throws RecognitionException {
		BoxWithtextFormatPlacementContext _localctx = new BoxWithtextFormatPlacementContext(_ctx, getState());
		enterRule(_localctx, 172, RULE_boxWithtextFormatPlacement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(672); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(672);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case CENTER:
					{
					setState(662);
					match(CENTER);
					}
					break;
				case TOP:
					{
					setState(663);
					match(TOP);
					}
					break;
				case BOTTOM:
					{
					setState(664);
					match(BOTTOM);
					}
					break;
				case LEFT:
					{
					setState(665);
					match(LEFT);
					}
					break;
				case RIGHT:
					{
					setState(666);
					match(RIGHT);
					}
					break;
				case BALANCE:
					{
					setState(667);
					match(BALANCE);
					}
					break;
				case JUSTIFY:
					{
					setState(668);
					match(JUSTIFY);
					setState(670);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==LASTNO) {
						{
						setState(669);
						match(LASTNO);
						}
					}

					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(674); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 633318697634048L) != 0) || _la==RIGHT || _la==TOP );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BoxWithtextFormatColumnContext extends ParserRuleContext {
		public TerminalNode COLUMN() { return getToken(OGLParser.COLUMN, 0); }
		public TerminalNode TATE() { return getToken(OGLParser.TATE, 0); }
		public BoxWithtextFormatPlacementContext boxWithtextFormatPlacement() {
			return getRuleContext(BoxWithtextFormatPlacementContext.class,0);
		}
		public BoxWithtextFormatColumnContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boxWithtextFormatColumn; }
	}

	public final BoxWithtextFormatColumnContext boxWithtextFormatColumn() throws RecognitionException {
		BoxWithtextFormatColumnContext _localctx = new BoxWithtextFormatColumnContext(_ctx, getState());
		enterRule(_localctx, 174, RULE_boxWithtextFormatColumn);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(676);
			_la = _input.LA(1);
			if ( !(_la==COLUMN || _la==TATE) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(678);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 633318697634048L) != 0) || _la==RIGHT || _la==TOP) {
				{
				setState(677);
				boxWithtextFormatPlacement();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PositionCommandContext extends ParserRuleContext {
		public TerminalNode POSITION() { return getToken(OGLParser.POSITION, 0); }
		public PositionXContext positionX() {
			return getRuleContext(PositionXContext.class,0);
		}
		public PositionYContext positionY() {
			return getRuleContext(PositionYContext.class,0);
		}
		public PositionCommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_positionCommand; }
	}

	public final PositionCommandContext positionCommand() throws RecognitionException {
		PositionCommandContext _localctx = new PositionCommandContext(_ctx, getState());
		enterRule(_localctx, 176, RULE_positionCommand);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(680);
			match(POSITION);
			setState(681);
			positionX();
			setState(682);
			positionY();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PositionXContext extends ParserRuleContext {
		public OglMeasurementContext oglMeasurement() {
			return getRuleContext(OglMeasurementContext.class,0);
		}
		public TerminalNode ABSOLUTE() { return getToken(OGLParser.ABSOLUTE, 0); }
		public TerminalNode LEFT() { return getToken(OGLParser.LEFT, 0); }
		public TerminalNode RIGHT() { return getToken(OGLParser.RIGHT, 0); }
		public TerminalNode UP() { return getToken(OGLParser.UP, 0); }
		public TerminalNode DOWN() { return getToken(OGLParser.DOWN, 0); }
		public PositionXContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_positionX; }
	}

	public final PositionXContext positionX() throws RecognitionException {
		PositionXContext _localctx = new PositionXContext(_ctx, getState());
		enterRule(_localctx, 178, RULE_positionX);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(685);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 562958543355920L) != 0) || _la==RIGHT || _la==UP) {
				{
				setState(684);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 562958543355920L) != 0) || _la==RIGHT || _la==UP) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
			}

			setState(687);
			oglMeasurement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PositionYContext extends ParserRuleContext {
		public OglMeasurementContext oglMeasurement() {
			return getRuleContext(OglMeasurementContext.class,0);
		}
		public TerminalNode ABSOLUTE() { return getToken(OGLParser.ABSOLUTE, 0); }
		public TerminalNode LEFT() { return getToken(OGLParser.LEFT, 0); }
		public TerminalNode RIGHT() { return getToken(OGLParser.RIGHT, 0); }
		public TerminalNode UP() { return getToken(OGLParser.UP, 0); }
		public TerminalNode DOWN() { return getToken(OGLParser.DOWN, 0); }
		public PositionYContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_positionY; }
	}

	public final PositionYContext positionY() throws RecognitionException {
		PositionYContext _localctx = new PositionYContext(_ctx, getState());
		enterRule(_localctx, 180, RULE_positionY);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(690);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 562958543355920L) != 0) || _la==RIGHT || _la==UP) {
				{
				setState(689);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 562958543355920L) != 0) || _la==RIGHT || _la==UP) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
			}

			setState(692);
			oglMeasurement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ControlCommandContext extends ParserRuleContext {
		public TerminalNode CONTROL() { return getToken(OGLParser.CONTROL, 0); }
		public List<ControlStorageContext> controlStorage() {
			return getRuleContexts(ControlStorageContext.class);
		}
		public ControlStorageContext controlStorage(int i) {
			return getRuleContext(ControlStorageContext.class,i);
		}
		public List<ControlMessageContext> controlMessage() {
			return getRuleContexts(ControlMessageContext.class);
		}
		public ControlMessageContext controlMessage(int i) {
			return getRuleContext(ControlMessageContext.class,i);
		}
		public List<ControlSummaryContext> controlSummary() {
			return getRuleContexts(ControlSummaryContext.class);
		}
		public ControlSummaryContext controlSummary(int i) {
			return getRuleContext(ControlSummaryContext.class,i);
		}
		public List<ControlSosiOptionContext> controlSosiOption() {
			return getRuleContexts(ControlSosiOptionContext.class);
		}
		public ControlSosiOptionContext controlSosiOption(int i) {
			return getRuleContext(ControlSosiOptionContext.class,i);
		}
		public ControlCommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_controlCommand; }
	}

	public final ControlCommandContext controlCommand() throws RecognitionException {
		ControlCommandContext _localctx = new ControlCommandContext(_ctx, getState());
		enterRule(_localctx, 182, RULE_controlCommand);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(694);
			match(CONTROL);
			setState(698);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 63)) & ~0x3f) == 0 && ((1L << (_la - 63)) & 34359771137L) != 0)) {
				{
				{
				setState(695);
				controlStorage();
				}
				}
				setState(700);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(704);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ALL || _la==ERROR || _la==WARN) {
				{
				{
				setState(701);
				controlMessage();
				}
				}
				setState(706);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(710);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NOSUMMARY || _la==SUMMARY) {
				{
				{
				setState(707);
				controlSummary();
				}
				}
				setState(712);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(716);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NOSOSI || _la==SOSI) {
				{
				{
				setState(713);
				controlSosiOption();
				}
				}
				setState(718);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ControlStorageContext extends ParserRuleContext {
		public TerminalNode NOSTORE() { return getToken(OGLParser.NOSTORE, 0); }
		public TerminalNode STORE() { return getToken(OGLParser.STORE, 0); }
		public TerminalNode REPLACE() { return getToken(OGLParser.REPLACE, 0); }
		public ControlStorageContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_controlStorage; }
	}

	public final ControlStorageContext controlStorage() throws RecognitionException {
		ControlStorageContext _localctx = new ControlStorageContext(_ctx, getState());
		enterRule(_localctx, 184, RULE_controlStorage);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(719);
			_la = _input.LA(1);
			if ( !(((((_la - 63)) & ~0x3f) == 0 && ((1L << (_la - 63)) & 34359771137L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ControlMessageContext extends ParserRuleContext {
		public TerminalNode ALL() { return getToken(OGLParser.ALL, 0); }
		public TerminalNode WARN() { return getToken(OGLParser.WARN, 0); }
		public TerminalNode ERROR() { return getToken(OGLParser.ERROR, 0); }
		public ControlMessageContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_controlMessage; }
	}

	public final ControlMessageContext controlMessage() throws RecognitionException {
		ControlMessageContext _localctx = new ControlMessageContext(_ctx, getState());
		enterRule(_localctx, 186, RULE_controlMessage);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(721);
			_la = _input.LA(1);
			if ( !(_la==ALL || _la==ERROR || _la==WARN) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ControlSummaryContext extends ParserRuleContext {
		public TerminalNode NOSUMMARY() { return getToken(OGLParser.NOSUMMARY, 0); }
		public TerminalNode SUMMARY() { return getToken(OGLParser.SUMMARY, 0); }
		public ControlSummaryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_controlSummary; }
	}

	public final ControlSummaryContext controlSummary() throws RecognitionException {
		ControlSummaryContext _localctx = new ControlSummaryContext(_ctx, getState());
		enterRule(_localctx, 188, RULE_controlSummary);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(723);
			_la = _input.LA(1);
			if ( !(_la==NOSUMMARY || _la==SUMMARY) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ControlSosiOptionContext extends ParserRuleContext {
		public TerminalNode SOSI() { return getToken(OGLParser.SOSI, 0); }
		public TerminalNode NOSOSI() { return getToken(OGLParser.NOSOSI, 0); }
		public ControlSosiOptionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_controlSosiOption; }
	}

	public final ControlSosiOptionContext controlSosiOption() throws RecognitionException {
		ControlSosiOptionContext _localctx = new ControlSosiOptionContext(_ctx, getState());
		enterRule(_localctx, 190, RULE_controlSosiOption);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(725);
			_la = _input.LA(1);
			if ( !(_la==NOSOSI || _la==SOSI) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OverlayCommandContext extends ParserRuleContext {
		public TerminalNode OVERLAY() { return getToken(OGLParser.OVERLAY, 0); }
		public OverlayNameContext overlayName() {
			return getRuleContext(OverlayNameContext.class,0);
		}
		public TerminalNode SIZE() { return getToken(OGLParser.SIZE, 0); }
		public OverlayWidthContext overlayWidth() {
			return getRuleContext(OverlayWidthContext.class,0);
		}
		public OverlayHeightContext overlayHeight() {
			return getRuleContext(OverlayHeightContext.class,0);
		}
		public TerminalNode OFFSET() { return getToken(OGLParser.OFFSET, 0); }
		public OverlayHorizonalCoordinateContext overlayHorizonalCoordinate() {
			return getRuleContext(OverlayHorizonalCoordinateContext.class,0);
		}
		public OverlayVerticalCoordinateContext overlayVerticalCoordinate() {
			return getRuleContext(OverlayVerticalCoordinateContext.class,0);
		}
		public OverlayCommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_overlayCommand; }
	}

	public final OverlayCommandContext overlayCommand() throws RecognitionException {
		OverlayCommandContext _localctx = new OverlayCommandContext(_ctx, getState());
		enterRule(_localctx, 192, RULE_overlayCommand);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(727);
			match(OVERLAY);
			setState(728);
			overlayName();
			setState(729);
			match(SIZE);
			setState(730);
			overlayWidth();
			setState(731);
			overlayHeight();
			setState(732);
			match(OFFSET);
			setState(733);
			overlayHorizonalCoordinate();
			setState(734);
			overlayVerticalCoordinate();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OverlayNameContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(OGLParser.IDENTIFIER, 0); }
		public OverlayNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_overlayName; }
	}

	public final OverlayNameContext overlayName() throws RecognitionException {
		OverlayNameContext _localctx = new OverlayNameContext(_ctx, getState());
		enterRule(_localctx, 194, RULE_overlayName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(736);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OverlayWidthContext extends ParserRuleContext {
		public OglMeasurementContext oglMeasurement() {
			return getRuleContext(OglMeasurementContext.class,0);
		}
		public OverlayWidthContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_overlayWidth; }
	}

	public final OverlayWidthContext overlayWidth() throws RecognitionException {
		OverlayWidthContext _localctx = new OverlayWidthContext(_ctx, getState());
		enterRule(_localctx, 196, RULE_overlayWidth);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(738);
			oglMeasurement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OverlayHeightContext extends ParserRuleContext {
		public OglMeasurementContext oglMeasurement() {
			return getRuleContext(OglMeasurementContext.class,0);
		}
		public OverlayHeightContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_overlayHeight; }
	}

	public final OverlayHeightContext overlayHeight() throws RecognitionException {
		OverlayHeightContext _localctx = new OverlayHeightContext(_ctx, getState());
		enterRule(_localctx, 198, RULE_overlayHeight);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(740);
			oglMeasurement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OverlayHorizonalCoordinateContext extends ParserRuleContext {
		public OglMeasurementContext oglMeasurement() {
			return getRuleContext(OglMeasurementContext.class,0);
		}
		public OverlayHorizonalCoordinateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_overlayHorizonalCoordinate; }
	}

	public final OverlayHorizonalCoordinateContext overlayHorizonalCoordinate() throws RecognitionException {
		OverlayHorizonalCoordinateContext _localctx = new OverlayHorizonalCoordinateContext(_ctx, getState());
		enterRule(_localctx, 200, RULE_overlayHorizonalCoordinate);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(742);
			oglMeasurement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OverlayVerticalCoordinateContext extends ParserRuleContext {
		public OglMeasurementContext oglMeasurement() {
			return getRuleContext(OglMeasurementContext.class,0);
		}
		public OverlayVerticalCoordinateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_overlayVerticalCoordinate; }
	}

	public final OverlayVerticalCoordinateContext overlayVerticalCoordinate() throws RecognitionException {
		OverlayVerticalCoordinateContext _localctx = new OverlayVerticalCoordinateContext(_ctx, getState());
		enterRule(_localctx, 202, RULE_overlayVerticalCoordinate);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(744);
			oglMeasurement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OrientCommandContext extends ParserRuleContext {
		public TerminalNode ORIENT() { return getToken(OGLParser.ORIENT, 0); }
		public OrientRotatedDegreeContext orientRotatedDegree() {
			return getRuleContext(OrientRotatedDegreeContext.class,0);
		}
		public OrientCommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_orientCommand; }
	}

	public final OrientCommandContext orientCommand() throws RecognitionException {
		OrientCommandContext _localctx = new OrientCommandContext(_ctx, getState());
		enterRule(_localctx, 204, RULE_orientCommand);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(746);
			match(ORIENT);
			setState(747);
			orientRotatedDegree();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OrientRotatedDegreeContext extends ParserRuleContext {
		public TerminalNode INTEGERLITERAL() { return getToken(OGLParser.INTEGERLITERAL, 0); }
		public OrientRotatedDegreeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_orientRotatedDegree; }
	}

	public final OrientRotatedDegreeContext orientRotatedDegree() throws RecognitionException {
		OrientRotatedDegreeContext _localctx = new OrientRotatedDegreeContext(_ctx, getState());
		enterRule(_localctx, 206, RULE_orientRotatedDegree);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(749);
			match(INTEGERLITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FontCommandContext extends ParserRuleContext {
		public FontCommandMVSContext fontCommandMVS() {
			return getRuleContext(FontCommandMVSContext.class,0);
		}
		public FontCommandVMContext fontCommandVM() {
			return getRuleContext(FontCommandVMContext.class,0);
		}
		public FontCommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fontCommand; }
	}

	public final FontCommandContext fontCommand() throws RecognitionException {
		FontCommandContext _localctx = new FontCommandContext(_ctx, getState());
		enterRule(_localctx, 208, RULE_fontCommand);
		try {
			setState(753);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,75,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(751);
				fontCommandMVS();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(752);
				fontCommandVM();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FontCommandMVSContext extends ParserRuleContext {
		public TerminalNode FONT() { return getToken(OGLParser.FONT, 0); }
		public FontWithMemIDContext fontWithMemID() {
			return getRuleContext(FontWithMemIDContext.class,0);
		}
		public FontWithCharSetContext fontWithCharSet() {
			return getRuleContext(FontWithCharSetContext.class,0);
		}
		public FontDDNameContext fontDDName() {
			return getRuleContext(FontDDNameContext.class,0);
		}
		public FontHeightContext fontHeight() {
			return getRuleContext(FontHeightContext.class,0);
		}
		public FontScaleContext fontScale() {
			return getRuleContext(FontScaleContext.class,0);
		}
		public FontColorContext fontColor() {
			return getRuleContext(FontColorContext.class,0);
		}
		public FontUColorContext fontUColor() {
			return getRuleContext(FontUColorContext.class,0);
		}
		public FontCommandMVSContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fontCommandMVS; }
	}

	public final FontCommandMVSContext fontCommandMVS() throws RecognitionException {
		FontCommandMVSContext _localctx = new FontCommandMVSContext(_ctx, getState());
		enterRule(_localctx, 210, RULE_fontCommandMVS);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(755);
			match(FONT);
			setState(758);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,76,_ctx) ) {
			case 1:
				{
				setState(756);
				fontWithMemID();
				}
				break;
			case 2:
				{
				setState(757);
				fontWithCharSet();
				}
				break;
			}
			setState(761);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==DDNAME) {
				{
				setState(760);
				fontDDName();
				}
			}

			setState(764);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==HEIGHT) {
				{
				setState(763);
				fontHeight();
				}
			}

			setState(767);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SCALE) {
				{
				setState(766);
				fontScale();
				}
			}

			setState(770);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COLOR) {
				{
				setState(769);
				fontColor();
				}
			}

			setState(773);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==UCOLOR) {
				{
				setState(772);
				fontUColor();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FontCommandVMContext extends ParserRuleContext {
		public TerminalNode FONT() { return getToken(OGLParser.FONT, 0); }
		public FontWithMemIDContext fontWithMemID() {
			return getRuleContext(FontWithMemIDContext.class,0);
		}
		public FontWithCharSetContext fontWithCharSet() {
			return getRuleContext(FontWithCharSetContext.class,0);
		}
		public FontFileTypeContext fontFileType() {
			return getRuleContext(FontFileTypeContext.class,0);
		}
		public FontHeightContext fontHeight() {
			return getRuleContext(FontHeightContext.class,0);
		}
		public FontScaleContext fontScale() {
			return getRuleContext(FontScaleContext.class,0);
		}
		public FontColorContext fontColor() {
			return getRuleContext(FontColorContext.class,0);
		}
		public FontUColorContext fontUColor() {
			return getRuleContext(FontUColorContext.class,0);
		}
		public FontCommandVMContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fontCommandVM; }
	}

	public final FontCommandVMContext fontCommandVM() throws RecognitionException {
		FontCommandVMContext _localctx = new FontCommandVMContext(_ctx, getState());
		enterRule(_localctx, 212, RULE_fontCommandVM);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(775);
			match(FONT);
			setState(778);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,82,_ctx) ) {
			case 1:
				{
				setState(776);
				fontWithMemID();
				}
				break;
			case 2:
				{
				setState(777);
				fontWithCharSet();
				}
				break;
			}
			setState(781);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==FILETYPE) {
				{
				setState(780);
				fontFileType();
				}
			}

			setState(784);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==HEIGHT) {
				{
				setState(783);
				fontHeight();
				}
			}

			setState(787);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SCALE) {
				{
				setState(786);
				fontScale();
				}
			}

			setState(790);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COLOR) {
				{
				setState(789);
				fontColor();
				}
			}

			setState(793);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==UCOLOR) {
				{
				setState(792);
				fontUColor();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FontFileTypeContext extends ParserRuleContext {
		public TerminalNode FILETYPE() { return getToken(OGLParser.FILETYPE, 0); }
		public FileTypeNameContext fileTypeName() {
			return getRuleContext(FileTypeNameContext.class,0);
		}
		public FontFileTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fontFileType; }
	}

	public final FontFileTypeContext fontFileType() throws RecognitionException {
		FontFileTypeContext _localctx = new FontFileTypeContext(_ctx, getState());
		enterRule(_localctx, 214, RULE_fontFileType);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(795);
			match(FILETYPE);
			setState(796);
			fileTypeName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FileTypeNameContext extends ParserRuleContext {
		public TerminalNode FONT38PP() { return getToken(OGLParser.FONT38PP, 0); }
		public TerminalNode IDENTIFIER() { return getToken(OGLParser.IDENTIFIER, 0); }
		public TerminalNode PSEG38PP() { return getToken(OGLParser.PSEG38PP, 0); }
		public FileTypeNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fileTypeName; }
	}

	public final FileTypeNameContext fileTypeName() throws RecognitionException {
		FileTypeNameContext _localctx = new FileTypeNameContext(_ctx, getState());
		enterRule(_localctx, 216, RULE_fileTypeName);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(798);
			_la = _input.LA(1);
			if ( !(_la==FONT38PP || _la==PSEG38PP || _la==IDENTIFIER) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FontWithMemIDContext extends ParserRuleContext {
		public MemIdContext memId() {
			return getRuleContext(MemIdContext.class,0);
		}
		public FontNameContext fontName() {
			return getRuleContext(FontNameContext.class,0);
		}
		public FontWithMemIDContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fontWithMemID; }
	}

	public final FontWithMemIDContext fontWithMemID() throws RecognitionException {
		FontWithMemIDContext _localctx = new FontWithMemIDContext(_ctx, getState());
		enterRule(_localctx, 218, RULE_fontWithMemID);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(801);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,88,_ctx) ) {
			case 1:
				{
				setState(800);
				fontName();
				}
				break;
			}
			setState(803);
			memId();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FontWithCharSetContext extends ParserRuleContext {
		public FontNameContext fontName() {
			return getRuleContext(FontNameContext.class,0);
		}
		public TerminalNode CHARSET() { return getToken(OGLParser.CHARSET, 0); }
		public CharSetNameContext charSetName() {
			return getRuleContext(CharSetNameContext.class,0);
		}
		public TerminalNode CODEPAGE() { return getToken(OGLParser.CODEPAGE, 0); }
		public CodePageNameContext codePageName() {
			return getRuleContext(CodePageNameContext.class,0);
		}
		public FontWithCharSetContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fontWithCharSet; }
	}

	public final FontWithCharSetContext fontWithCharSet() throws RecognitionException {
		FontWithCharSetContext _localctx = new FontWithCharSetContext(_ctx, getState());
		enterRule(_localctx, 220, RULE_fontWithCharSet);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(805);
			fontName();
			setState(806);
			match(CHARSET);
			setState(807);
			charSetName();
			setState(808);
			match(CODEPAGE);
			setState(809);
			codePageName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FontDDNameContext extends ParserRuleContext {
		public TerminalNode DDNAME() { return getToken(OGLParser.DDNAME, 0); }
		public DdNameNameContext ddNameName() {
			return getRuleContext(DdNameNameContext.class,0);
		}
		public FontDDNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fontDDName; }
	}

	public final FontDDNameContext fontDDName() throws RecognitionException {
		FontDDNameContext _localctx = new FontDDNameContext(_ctx, getState());
		enterRule(_localctx, 222, RULE_fontDDName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(811);
			match(DDNAME);
			setState(812);
			ddNameName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DdNameNameContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(OGLParser.IDENTIFIER, 0); }
		public TerminalNode FONTDD() { return getToken(OGLParser.FONTDD, 0); }
		public DdNameNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ddNameName; }
	}

	public final DdNameNameContext ddNameName() throws RecognitionException {
		DdNameNameContext _localctx = new DdNameNameContext(_ctx, getState());
		enterRule(_localctx, 224, RULE_ddNameName);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(814);
			_la = _input.LA(1);
			if ( !(_la==FONTDD || _la==IDENTIFIER) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FontHeightContext extends ParserRuleContext {
		public TerminalNode HEIGHT() { return getToken(OGLParser.HEIGHT, 0); }
		public OglMeasurementContext oglMeasurement() {
			return getRuleContext(OglMeasurementContext.class,0);
		}
		public FontHeightContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fontHeight; }
	}

	public final FontHeightContext fontHeight() throws RecognitionException {
		FontHeightContext _localctx = new FontHeightContext(_ctx, getState());
		enterRule(_localctx, 226, RULE_fontHeight);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(816);
			match(HEIGHT);
			setState(817);
			oglMeasurement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FontScaleContext extends ParserRuleContext {
		public TerminalNode SCALE() { return getToken(OGLParser.SCALE, 0); }
		public OglMeasurementContext oglMeasurement() {
			return getRuleContext(OglMeasurementContext.class,0);
		}
		public FontScaleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fontScale; }
	}

	public final FontScaleContext fontScale() throws RecognitionException {
		FontScaleContext _localctx = new FontScaleContext(_ctx, getState());
		enterRule(_localctx, 228, RULE_fontScale);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(819);
			match(SCALE);
			setState(820);
			oglMeasurement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FontColorContext extends ParserRuleContext {
		public TerminalNode COLOR() { return getToken(OGLParser.COLOR, 0); }
		public FontColorNameContext fontColorName() {
			return getRuleContext(FontColorNameContext.class,0);
		}
		public FontColorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fontColor; }
	}

	public final FontColorContext fontColor() throws RecognitionException {
		FontColorContext _localctx = new FontColorContext(_ctx, getState());
		enterRule(_localctx, 230, RULE_fontColor);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(822);
			match(COLOR);
			setState(823);
			fontColorName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FontUColorContext extends ParserRuleContext {
		public TerminalNode UCOLOR() { return getToken(OGLParser.UCOLOR, 0); }
		public FontColorNameContext fontColorName() {
			return getRuleContext(FontColorNameContext.class,0);
		}
		public FontUColorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fontUColor; }
	}

	public final FontUColorContext fontUColor() throws RecognitionException {
		FontUColorContext _localctx = new FontUColorContext(_ctx, getState());
		enterRule(_localctx, 232, RULE_fontUColor);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(825);
			match(UCOLOR);
			setState(826);
			fontColorName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FontColorNameContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(OGLParser.IDENTIFIER, 0); }
		public FontColorNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fontColorName; }
	}

	public final FontColorNameContext fontColorName() throws RecognitionException {
		FontColorNameContext _localctx = new FontColorNameContext(_ctx, getState());
		enterRule(_localctx, 234, RULE_fontColorName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(828);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FontNameContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(OGLParser.IDENTIFIER, 0); }
		public FontNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fontName; }
	}

	public final FontNameContext fontName() throws RecognitionException {
		FontNameContext _localctx = new FontNameContext(_ctx, getState());
		enterRule(_localctx, 236, RULE_fontName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(830);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MemIdContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(OGLParser.IDENTIFIER, 0); }
		public MemIdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_memId; }
	}

	public final MemIdContext memId() throws RecognitionException {
		MemIdContext _localctx = new MemIdContext(_ctx, getState());
		enterRule(_localctx, 238, RULE_memId);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(832);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CharSetNameContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(OGLParser.IDENTIFIER, 0); }
		public CharSetNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_charSetName; }
	}

	public final CharSetNameContext charSetName() throws RecognitionException {
		CharSetNameContext _localctx = new CharSetNameContext(_ctx, getState());
		enterRule(_localctx, 240, RULE_charSetName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(834);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CodePageNameContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(OGLParser.IDENTIFIER, 0); }
		public CodePageNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_codePageName; }
	}

	public final CodePageNameContext codePageName() throws RecognitionException {
		CodePageNameContext _localctx = new CodePageNameContext(_ctx, getState());
		enterRule(_localctx, 242, RULE_codePageName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(836);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DefineGroupCommandContext extends ParserRuleContext {
		public TerminalNode DEFINE() { return getToken(OGLParser.DEFINE, 0); }
		public GroupNameContext groupName() {
			return getRuleContext(GroupNameContext.class,0);
		}
		public TerminalNode GROUP() { return getToken(OGLParser.GROUP, 0); }
		public TerminalNode ENDDEF() { return getToken(OGLParser.ENDDEF, 0); }
		public List<CommandContext> command() {
			return getRuleContexts(CommandContext.class);
		}
		public CommandContext command(int i) {
			return getRuleContext(CommandContext.class,i);
		}
		public DefineGroupCommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_defineGroupCommand; }
	}

	public final DefineGroupCommandContext defineGroupCommand() throws RecognitionException {
		DefineGroupCommandContext _localctx = new DefineGroupCommandContext(_ctx, getState());
		enterRule(_localctx, 244, RULE_defineGroupCommand);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(838);
			match(DEFINE);
			setState(839);
			groupName();
			setState(840);
			match(GROUP);
			setState(842); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(841);
				command();
				}
				}
				setState(844); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 281456672768L) != 0) || ((((_la - 68)) & ~0x3f) == 0 && ((1L << (_la - 68)) & 917587L) != 0) );
			setState(846);
			match(ENDDEF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GroupNameContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(OGLParser.IDENTIFIER, 0); }
		public GroupNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_groupName; }
	}

	public final GroupNameContext groupName() throws RecognitionException {
		GroupNameContext _localctx = new GroupNameContext(_ctx, getState());
		enterRule(_localctx, 246, RULE_groupName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(848);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OglMeasurementContext extends ParserRuleContext {
		public TerminalNode INTEGERLITERAL() { return getToken(OGLParser.INTEGERLITERAL, 0); }
		public TerminalNode PELS() { return getToken(OGLParser.PELS, 0); }
		public TerminalNode IN() { return getToken(OGLParser.IN, 0); }
		public TerminalNode MM() { return getToken(OGLParser.MM, 0); }
		public TerminalNode CPI() { return getToken(OGLParser.CPI, 0); }
		public TerminalNode LPI() { return getToken(OGLParser.LPI, 0); }
		public TerminalNode POINTS() { return getToken(OGLParser.POINTS, 0); }
		public OglMeasurementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_oglMeasurement; }
	}

	public final OglMeasurementContext oglMeasurement() throws RecognitionException {
		OglMeasurementContext _localctx = new OglMeasurementContext(_ctx, getState());
		enterRule(_localctx, 248, RULE_oglMeasurement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(850);
			match(INTEGERLITERAL);
			setState(852);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 23)) & ~0x3f) == 0 && ((1L << (_la - 23)) & 1407385625165825L) != 0)) {
				{
				setState(851);
				_la = _input.LA(1);
				if ( !(((((_la - 23)) & ~0x3f) == 0 && ((1L << (_la - 23)) & 1407385625165825L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001v\u0357\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007!\u0002\"\u0007\"\u0002"+
		"#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007&\u0002\'\u0007\'\u0002"+
		"(\u0007(\u0002)\u0007)\u0002*\u0007*\u0002+\u0007+\u0002,\u0007,\u0002"+
		"-\u0007-\u0002.\u0007.\u0002/\u0007/\u00020\u00070\u00021\u00071\u0002"+
		"2\u00072\u00023\u00073\u00024\u00074\u00025\u00075\u00026\u00076\u0002"+
		"7\u00077\u00028\u00078\u00029\u00079\u0002:\u0007:\u0002;\u0007;\u0002"+
		"<\u0007<\u0002=\u0007=\u0002>\u0007>\u0002?\u0007?\u0002@\u0007@\u0002"+
		"A\u0007A\u0002B\u0007B\u0002C\u0007C\u0002D\u0007D\u0002E\u0007E\u0002"+
		"F\u0007F\u0002G\u0007G\u0002H\u0007H\u0002I\u0007I\u0002J\u0007J\u0002"+
		"K\u0007K\u0002L\u0007L\u0002M\u0007M\u0002N\u0007N\u0002O\u0007O\u0002"+
		"P\u0007P\u0002Q\u0007Q\u0002R\u0007R\u0002S\u0007S\u0002T\u0007T\u0002"+
		"U\u0007U\u0002V\u0007V\u0002W\u0007W\u0002X\u0007X\u0002Y\u0007Y\u0002"+
		"Z\u0007Z\u0002[\u0007[\u0002\\\u0007\\\u0002]\u0007]\u0002^\u0007^\u0002"+
		"_\u0007_\u0002`\u0007`\u0002a\u0007a\u0002b\u0007b\u0002c\u0007c\u0002"+
		"d\u0007d\u0002e\u0007e\u0002f\u0007f\u0002g\u0007g\u0002h\u0007h\u0002"+
		"i\u0007i\u0002j\u0007j\u0002k\u0007k\u0002l\u0007l\u0002m\u0007m\u0002"+
		"n\u0007n\u0002o\u0007o\u0002p\u0007p\u0002q\u0007q\u0002r\u0007r\u0002"+
		"s\u0007s\u0002t\u0007t\u0002u\u0007u\u0002v\u0007v\u0002w\u0007w\u0002"+
		"x\u0007x\u0002y\u0007y\u0002z\u0007z\u0002{\u0007{\u0002|\u0007|\u0001"+
		"\u0000\u0005\u0000\u00fc\b\u0000\n\u0000\f\u0000\u00ff\t\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001\u0111\b\u0001\u0001\u0002"+
		"\u0001\u0002\u0003\u0002\u0115\b\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0003\u0002\u011a\b\u0002\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0003\u0007\u012a\b\u0007"+
		"\u0001\u0007\u0003\u0007\u012d\b\u0007\u0001\u0007\u0003\u0007\u0130\b"+
		"\u0007\u0001\u0007\u0003\u0007\u0133\b\u0007\u0001\u0007\u0003\u0007\u0136"+
		"\b\u0007\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001"+
		"\u000b\u0001\u000b\u0001\f\u0001\f\u0004\f\u0143\b\f\u000b\f\f\f\u0144"+
		"\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0003\r\u014c\b\r\u0001\u000e"+
		"\u0001\u000e\u0003\u000e\u0150\b\u000e\u0001\u000f\u0001\u000f\u0004\u000f"+
		"\u0154\b\u000f\u000b\u000f\f\u000f\u0155\u0001\u0010\u0001\u0010\u0004"+
		"\u0010\u015a\b\u0010\u000b\u0010\f\u0010\u015b\u0001\u0011\u0001\u0011"+
		"\u0004\u0011\u0160\b\u0011\u000b\u0011\f\u0011\u0161\u0001\u0011\u0001"+
		"\u0011\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0003\u0013\u016a"+
		"\b\u0013\u0001\u0013\u0003\u0013\u016d\b\u0013\u0001\u0013\u0003\u0013"+
		"\u0170\b\u0013\u0001\u0013\u0004\u0013\u0173\b\u0013\u000b\u0013\f\u0013"+
		"\u0174\u0001\u0014\u0001\u0014\u0003\u0014\u0179\b\u0014\u0001\u0015\u0001"+
		"\u0015\u0003\u0015\u017d\b\u0015\u0001\u0016\u0001\u0016\u0001\u0017\u0001"+
		"\u0017\u0003\u0017\u0183\b\u0017\u0001\u0018\u0001\u0018\u0003\u0018\u0187"+
		"\b\u0018\u0001\u0019\u0001\u0019\u0001\u001a\u0001\u001a\u0001\u001a\u0001"+
		"\u001b\u0001\u001b\u0001\u001c\u0001\u001c\u0003\u001c\u0192\b\u001c\u0001"+
		"\u001c\u0003\u001c\u0195\b\u001c\u0001\u001c\u0003\u001c\u0198\b\u001c"+
		"\u0001\u001c\u0003\u001c\u019b\b\u001c\u0001\u001c\u0003\u001c\u019e\b"+
		"\u001c\u0001\u001d\u0001\u001d\u0003\u001d\u01a2\b\u001d\u0001\u001e\u0001"+
		"\u001e\u0001\u001f\u0001\u001f\u0001 \u0001 \u0001 \u0001!\u0001!\u0001"+
		"!\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0003\"\u01b4\b\"\u0001"+
		"#\u0001#\u0001#\u0001$\u0001$\u0001%\u0001%\u0001%\u0001&\u0001&\u0001"+
		"\'\u0001\'\u0001\'\u0001\'\u0001(\u0001(\u0003(\u01c6\b(\u0001(\u0001"+
		"(\u0003(\u01ca\b(\u0001(\u0003(\u01cd\b(\u0001(\u0003(\u01d0\b(\u0001"+
		")\u0001)\u0001*\u0001*\u0001+\u0001+\u0001,\u0001,\u0001-\u0001-\u0001"+
		"-\u0004-\u01dd\b-\u000b-\f-\u01de\u0001.\u0003.\u01e2\b.\u0001.\u0001"+
		".\u0001.\u0001.\u0001/\u0001/\u00010\u00010\u00010\u00010\u00011\u0001"+
		"1\u00012\u00012\u00013\u00013\u00013\u00013\u00013\u00013\u00013\u0001"+
		"3\u00013\u00013\u00013\u00053\u01fd\b3\n3\f3\u0200\t3\u00014\u00014\u0001"+
		"5\u00015\u00016\u00016\u00017\u00017\u00018\u00018\u00038\u020c\b8\u0001"+
		"9\u00019\u00049\u0210\b9\u000b9\f9\u0211\u00039\u0214\b9\u0001:\u0001"+
		":\u0001:\u0001;\u0001;\u0001<\u0001<\u0001<\u0004<\u021e\b<\u000b<\f<"+
		"\u021f\u0001<\u0003<\u0223\b<\u0001=\u0001=\u0001=\u0001=\u0001>\u0001"+
		">\u0001?\u0001?\u0001@\u0001@\u0001@\u0001A\u0001A\u0001B\u0001B\u0001"+
		"B\u0001C\u0001C\u0003C\u0237\bC\u0001D\u0001D\u0003D\u023b\bD\u0001D\u0003"+
		"D\u023e\bD\u0001D\u0003D\u0241\bD\u0001D\u0003D\u0244\bD\u0001E\u0001"+
		"E\u0001E\u0003E\u0249\bE\u0001F\u0001F\u0001G\u0001G\u0001H\u0001H\u0001"+
		"I\u0001I\u0001I\u0001I\u0001J\u0001J\u0001K\u0001K\u0003K\u0259\bK\u0001"+
		"K\u0003K\u025c\bK\u0001K\u0003K\u025f\bK\u0001K\u0003K\u0262\bK\u0001"+
		"K\u0001K\u0001L\u0001L\u0001M\u0001M\u0001M\u0003M\u026b\bM\u0001N\u0001"+
		"N\u0004N\u026f\bN\u000bN\fN\u0270\u0001O\u0004O\u0274\bO\u000bO\fO\u0275"+
		"\u0001O\u0003O\u0279\bO\u0001O\u0003O\u027c\bO\u0001O\u0003O\u027f\bO"+
		"\u0001O\u0004O\u0282\bO\u000bO\fO\u0283\u0001P\u0001P\u0001Q\u0001Q\u0001"+
		"R\u0001R\u0001S\u0001S\u0001T\u0001T\u0001T\u0003T\u0291\bT\u0001U\u0001"+
		"U\u0003U\u0295\bU\u0001V\u0001V\u0001V\u0001V\u0001V\u0001V\u0001V\u0001"+
		"V\u0003V\u029f\bV\u0004V\u02a1\bV\u000bV\fV\u02a2\u0001W\u0001W\u0003"+
		"W\u02a7\bW\u0001X\u0001X\u0001X\u0001X\u0001Y\u0003Y\u02ae\bY\u0001Y\u0001"+
		"Y\u0001Z\u0003Z\u02b3\bZ\u0001Z\u0001Z\u0001[\u0001[\u0005[\u02b9\b[\n"+
		"[\f[\u02bc\t[\u0001[\u0005[\u02bf\b[\n[\f[\u02c2\t[\u0001[\u0005[\u02c5"+
		"\b[\n[\f[\u02c8\t[\u0001[\u0005[\u02cb\b[\n[\f[\u02ce\t[\u0001\\\u0001"+
		"\\\u0001]\u0001]\u0001^\u0001^\u0001_\u0001_\u0001`\u0001`\u0001`\u0001"+
		"`\u0001`\u0001`\u0001`\u0001`\u0001`\u0001a\u0001a\u0001b\u0001b\u0001"+
		"c\u0001c\u0001d\u0001d\u0001e\u0001e\u0001f\u0001f\u0001f\u0001g\u0001"+
		"g\u0001h\u0001h\u0003h\u02f2\bh\u0001i\u0001i\u0001i\u0003i\u02f7\bi\u0001"+
		"i\u0003i\u02fa\bi\u0001i\u0003i\u02fd\bi\u0001i\u0003i\u0300\bi\u0001"+
		"i\u0003i\u0303\bi\u0001i\u0003i\u0306\bi\u0001j\u0001j\u0001j\u0003j\u030b"+
		"\bj\u0001j\u0003j\u030e\bj\u0001j\u0003j\u0311\bj\u0001j\u0003j\u0314"+
		"\bj\u0001j\u0003j\u0317\bj\u0001j\u0003j\u031a\bj\u0001k\u0001k\u0001"+
		"k\u0001l\u0001l\u0001m\u0003m\u0322\bm\u0001m\u0001m\u0001n\u0001n\u0001"+
		"n\u0001n\u0001n\u0001n\u0001o\u0001o\u0001o\u0001p\u0001p\u0001q\u0001"+
		"q\u0001q\u0001r\u0001r\u0001r\u0001s\u0001s\u0001s\u0001t\u0001t\u0001"+
		"t\u0001u\u0001u\u0001v\u0001v\u0001w\u0001w\u0001x\u0001x\u0001y\u0001"+
		"y\u0001z\u0001z\u0001z\u0001z\u0004z\u034b\bz\u000bz\fz\u034c\u0001z\u0001"+
		"z\u0001{\u0001{\u0001|\u0001|\u0003|\u0355\b|\u0001|\u0000\u0000}\u0000"+
		"\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c"+
		"\u001e \"$&(*,.02468:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084"+
		"\u0086\u0088\u008a\u008c\u008e\u0090\u0092\u0094\u0096\u0098\u009a\u009c"+
		"\u009e\u00a0\u00a2\u00a4\u00a6\u00a8\u00aa\u00ac\u00ae\u00b0\u00b2\u00b4"+
		"\u00b6\u00b8\u00ba\u00bc\u00be\u00c0\u00c2\u00c4\u00c6\u00c8\u00ca\u00cc"+
		"\u00ce\u00d0\u00d2\u00d4\u00d6\u00d8\u00da\u00dc\u00de\u00e0\u00e2\u00e4"+
		"\u00e6\u00e8\u00ea\u00ec\u00ee\u00f0\u00f2\u00f4\u00f6\u00f8\u0000\u001b"+
		"\u0002\u0000SSvv\u0002\u0000::==\u0002\u0000<<>>\u0005\u0000\u000b\u000b"+
		"\u000f\u000f11OOff\u0002\u0000\u0014\u0014dd\u0002\u0000PP``\u0002\u0000"+
		"\u000f\u000fgg\u0002\u0000))TT\u0002\u0000\u0005\u0005!!\u0004\u0000\t"+
		"\t2299rr\u0003\u0000\u0019\u0019\u001e\u001e[[\u0002\u0000\f\rgh\u0003"+
		"\u0000\n\n11OO\u0005\u0000\u000b\u000b11OOffmm\u0002\u0000RRaa\u0005\u0000"+
		"\u0018\u00182299oprr\u0001\u0000]^\u0002\u0000BBjj\u0002\u0000\u0010\u0010"+
		",,\u0005\u0000\u0004\u0004!!11OOkk\u0003\u0000??NNbb\u0003\u0000\u0006"+
		"\u0006$$ll\u0002\u0000AAcc\u0002\u0000@@\\\\\u0003\u0000\'\'LLvv\u0002"+
		"\u0000((vv\u0006\u0000\u0017\u0017--6688GGII\u0351\u0000\u00fd\u0001\u0000"+
		"\u0000\u0000\u0002\u0110\u0001\u0000\u0000\u0000\u0004\u0112\u0001\u0000"+
		"\u0000\u0000\u0006\u011b\u0001\u0000\u0000\u0000\b\u011d\u0001\u0000\u0000"+
		"\u0000\n\u0120\u0001\u0000\u0000\u0000\f\u0122\u0001\u0000\u0000\u0000"+
		"\u000e\u0125\u0001\u0000\u0000\u0000\u0010\u0137\u0001\u0000\u0000\u0000"+
		"\u0012\u013a\u0001\u0000\u0000\u0000\u0014\u013c\u0001\u0000\u0000\u0000"+
		"\u0016\u013e\u0001\u0000\u0000\u0000\u0018\u0142\u0001\u0000\u0000\u0000"+
		"\u001a\u0146\u0001\u0000\u0000\u0000\u001c\u014f\u0001\u0000\u0000\u0000"+
		"\u001e\u0151\u0001\u0000\u0000\u0000 \u0157\u0001\u0000\u0000\u0000\""+
		"\u015d\u0001\u0000\u0000\u0000$\u0165\u0001\u0000\u0000\u0000&\u0167\u0001"+
		"\u0000\u0000\u0000(\u0178\u0001\u0000\u0000\u0000*\u017a\u0001\u0000\u0000"+
		"\u0000,\u017e\u0001\u0000\u0000\u0000.\u0180\u0001\u0000\u0000\u00000"+
		"\u0186\u0001\u0000\u0000\u00002\u0188\u0001\u0000\u0000\u00004\u018a\u0001"+
		"\u0000\u0000\u00006\u018d\u0001\u0000\u0000\u00008\u018f\u0001\u0000\u0000"+
		"\u0000:\u019f\u0001\u0000\u0000\u0000<\u01a3\u0001\u0000\u0000\u0000>"+
		"\u01a5\u0001\u0000\u0000\u0000@\u01a7\u0001\u0000\u0000\u0000B\u01aa\u0001"+
		"\u0000\u0000\u0000D\u01b3\u0001\u0000\u0000\u0000F\u01b5\u0001\u0000\u0000"+
		"\u0000H\u01b8\u0001\u0000\u0000\u0000J\u01ba\u0001\u0000\u0000\u0000L"+
		"\u01bd\u0001\u0000\u0000\u0000N\u01bf\u0001\u0000\u0000\u0000P\u01c3\u0001"+
		"\u0000\u0000\u0000R\u01d1\u0001\u0000\u0000\u0000T\u01d3\u0001\u0000\u0000"+
		"\u0000V\u01d5\u0001\u0000\u0000\u0000X\u01d7\u0001\u0000\u0000\u0000Z"+
		"\u01d9\u0001\u0000\u0000\u0000\\\u01e1\u0001\u0000\u0000\u0000^\u01e7"+
		"\u0001\u0000\u0000\u0000`\u01e9\u0001\u0000\u0000\u0000b\u01ed\u0001\u0000"+
		"\u0000\u0000d\u01ef\u0001\u0000\u0000\u0000f\u01f1\u0001\u0000\u0000\u0000"+
		"h\u0201\u0001\u0000\u0000\u0000j\u0203\u0001\u0000\u0000\u0000l\u0205"+
		"\u0001\u0000\u0000\u0000n\u0207\u0001\u0000\u0000\u0000p\u0209\u0001\u0000"+
		"\u0000\u0000r\u0213\u0001\u0000\u0000\u0000t\u0215\u0001\u0000\u0000\u0000"+
		"v\u0218\u0001\u0000\u0000\u0000x\u021a\u0001\u0000\u0000\u0000z\u0224"+
		"\u0001\u0000\u0000\u0000|\u0228\u0001\u0000\u0000\u0000~\u022a\u0001\u0000"+
		"\u0000\u0000\u0080\u022c\u0001\u0000\u0000\u0000\u0082\u022f\u0001\u0000"+
		"\u0000\u0000\u0084\u0231\u0001\u0000\u0000\u0000\u0086\u0236\u0001\u0000"+
		"\u0000\u0000\u0088\u0238\u0001\u0000\u0000\u0000\u008a\u0248\u0001\u0000"+
		"\u0000\u0000\u008c\u024a\u0001\u0000\u0000\u0000\u008e\u024c\u0001\u0000"+
		"\u0000\u0000\u0090\u024e\u0001\u0000\u0000\u0000\u0092\u0250\u0001\u0000"+
		"\u0000\u0000\u0094\u0254\u0001\u0000\u0000\u0000\u0096\u0256\u0001\u0000"+
		"\u0000\u0000\u0098\u0265\u0001\u0000\u0000\u0000\u009a\u026a\u0001\u0000"+
		"\u0000\u0000\u009c\u026c\u0001\u0000\u0000\u0000\u009e\u0273\u0001\u0000"+
		"\u0000\u0000\u00a0\u0285\u0001\u0000\u0000\u0000\u00a2\u0287\u0001\u0000"+
		"\u0000\u0000\u00a4\u0289\u0001\u0000\u0000\u0000\u00a6\u028b\u0001\u0000"+
		"\u0000\u0000\u00a8\u0290\u0001\u0000\u0000\u0000\u00aa\u0292\u0001\u0000"+
		"\u0000\u0000\u00ac\u02a0\u0001\u0000\u0000\u0000\u00ae\u02a4\u0001\u0000"+
		"\u0000\u0000\u00b0\u02a8\u0001\u0000\u0000\u0000\u00b2\u02ad\u0001\u0000"+
		"\u0000\u0000\u00b4\u02b2\u0001\u0000\u0000\u0000\u00b6\u02b6\u0001\u0000"+
		"\u0000\u0000\u00b8\u02cf\u0001\u0000\u0000\u0000\u00ba\u02d1\u0001\u0000"+
		"\u0000\u0000\u00bc\u02d3\u0001\u0000\u0000\u0000\u00be\u02d5\u0001\u0000"+
		"\u0000\u0000\u00c0\u02d7\u0001\u0000\u0000\u0000\u00c2\u02e0\u0001\u0000"+
		"\u0000\u0000\u00c4\u02e2\u0001\u0000\u0000\u0000\u00c6\u02e4\u0001\u0000"+
		"\u0000\u0000\u00c8\u02e6\u0001\u0000\u0000\u0000\u00ca\u02e8\u0001\u0000"+
		"\u0000\u0000\u00cc\u02ea\u0001\u0000\u0000\u0000\u00ce\u02ed\u0001\u0000"+
		"\u0000\u0000\u00d0\u02f1\u0001\u0000\u0000\u0000\u00d2\u02f3\u0001\u0000"+
		"\u0000\u0000\u00d4\u0307\u0001\u0000\u0000\u0000\u00d6\u031b\u0001\u0000"+
		"\u0000\u0000\u00d8\u031e\u0001\u0000\u0000\u0000\u00da\u0321\u0001\u0000"+
		"\u0000\u0000\u00dc\u0325\u0001\u0000\u0000\u0000\u00de\u032b\u0001\u0000"+
		"\u0000\u0000\u00e0\u032e\u0001\u0000\u0000\u0000\u00e2\u0330\u0001\u0000"+
		"\u0000\u0000\u00e4\u0333\u0001\u0000\u0000\u0000\u00e6\u0336\u0001\u0000"+
		"\u0000\u0000\u00e8\u0339\u0001\u0000\u0000\u0000\u00ea\u033c\u0001\u0000"+
		"\u0000\u0000\u00ec\u033e\u0001\u0000\u0000\u0000\u00ee\u0340\u0001\u0000"+
		"\u0000\u0000\u00f0\u0342\u0001\u0000\u0000\u0000\u00f2\u0344\u0001\u0000"+
		"\u0000\u0000\u00f4\u0346\u0001\u0000\u0000\u0000\u00f6\u0350\u0001\u0000"+
		"\u0000\u0000\u00f8\u0352\u0001\u0000\u0000\u0000\u00fa\u00fc\u0003\u0002"+
		"\u0001\u0000\u00fb\u00fa\u0001\u0000\u0000\u0000\u00fc\u00ff\u0001\u0000"+
		"\u0000\u0000\u00fd\u00fb\u0001\u0000\u0000\u0000\u00fd\u00fe\u0001\u0000"+
		"\u0000\u0000\u00fe\u0100\u0001\u0000\u0000\u0000\u00ff\u00fd\u0001\u0000"+
		"\u0000\u0000\u0100\u0101\u0005\u0000\u0000\u0001\u0101\u0001\u0001\u0000"+
		"\u0000\u0000\u0102\u0111\u0003\u00b6[\u0000\u0103\u0111\u0003\u00c0`\u0000"+
		"\u0104\u0111\u0003\u00ccf\u0000\u0105\u0111\u0003\u00d0h\u0000\u0106\u0111"+
		"\u0003\u00f4z\u0000\u0107\u0111\u0003\u00b0X\u0000\u0108\u0111\u0003f"+
		"3\u0000\u0109\u0111\u0003P(\u0000\u010a\u0111\u0003N\'\u0000\u010b\u0111"+
		"\u00038\u001c\u0000\u010c\u0111\u0003&\u0013\u0000\u010d\u0111\u0003\u001a"+
		"\r\u0000\u010e\u0111\u0003\u000e\u0007\u0000\u010f\u0111\u0003\u0004\u0002"+
		"\u0000\u0110\u0102\u0001\u0000\u0000\u0000\u0110\u0103\u0001\u0000\u0000"+
		"\u0000\u0110\u0104\u0001\u0000\u0000\u0000\u0110\u0105\u0001\u0000\u0000"+
		"\u0000\u0110\u0106\u0001\u0000\u0000\u0000\u0110\u0107\u0001\u0000\u0000"+
		"\u0000\u0110\u0108\u0001\u0000\u0000\u0000\u0110\u0109\u0001\u0000\u0000"+
		"\u0000\u0110\u010a\u0001\u0000\u0000\u0000\u0110\u010b\u0001\u0000\u0000"+
		"\u0000\u0110\u010c\u0001\u0000\u0000\u0000\u0110\u010d\u0001\u0000\u0000"+
		"\u0000\u0110\u010e\u0001\u0000\u0000\u0000\u0110\u010f\u0001\u0000\u0000"+
		"\u0000\u0111\u0003\u0001\u0000\u0000\u0000\u0112\u0114\u0005U\u0000\u0000"+
		"\u0113\u0115\u0003\u0006\u0003\u0000\u0114\u0113\u0001\u0000\u0000\u0000"+
		"\u0114\u0115\u0001\u0000\u0000\u0000\u0115\u0116\u0001\u0000\u0000\u0000"+
		"\u0116\u0119\u0003\u00eew\u0000\u0117\u011a\u0003\b\u0004\u0000\u0118"+
		"\u011a\u0003\f\u0006\u0000\u0119\u0117\u0001\u0000\u0000\u0000\u0119\u0118"+
		"\u0001\u0000\u0000\u0000\u0119\u011a\u0001\u0000\u0000\u0000\u011a\u0005"+
		"\u0001\u0000\u0000\u0000\u011b\u011c\u0005v\u0000\u0000\u011c\u0007\u0001"+
		"\u0000\u0000\u0000\u011d\u011e\u0005\u001a\u0000\u0000\u011e\u011f\u0003"+
		"\n\u0005\u0000\u011f\t\u0001\u0000\u0000\u0000\u0120\u0121\u0007\u0000"+
		"\u0000\u0000\u0121\u000b\u0001\u0000\u0000\u0000\u0122\u0123\u0005%\u0000"+
		"\u0000\u0123\u0124\u0003\u00d8l\u0000\u0124\r\u0001\u0000\u0000\u0000"+
		"\u0125\u0126\u0005H\u0000\u0000\u0126\u0127\u0005F\u0000\u0000\u0127\u0129"+
		"\u0003$\u0012\u0000\u0128\u012a\u0003\u00ceg\u0000\u0129\u0128\u0001\u0000"+
		"\u0000\u0000\u0129\u012a\u0001\u0000\u0000\u0000\u012a\u012c\u0001\u0000"+
		"\u0000\u0000\u012b\u012d\u0003\u0018\f\u0000\u012c\u012b\u0001\u0000\u0000"+
		"\u0000\u012c\u012d\u0001\u0000\u0000\u0000\u012d\u012f\u0001\u0000\u0000"+
		"\u0000\u012e\u0130\u0003\u0014\n\u0000\u012f\u012e\u0001\u0000\u0000\u0000"+
		"\u012f\u0130\u0001\u0000\u0000\u0000\u0130\u0132\u0001\u0000\u0000\u0000"+
		"\u0131\u0133\u0003\u0016\u000b\u0000\u0132\u0131\u0001\u0000\u0000\u0000"+
		"\u0132\u0133\u0001\u0000\u0000\u0000\u0133\u0135\u0001\u0000\u0000\u0000"+
		"\u0134\u0136\u0003\u0010\b\u0000\u0135\u0134\u0001\u0000\u0000\u0000\u0135"+
		"\u0136\u0001\u0000\u0000\u0000\u0136\u000f\u0001\u0000\u0000\u0000\u0137"+
		"\u0138\u0005\u0013\u0000\u0000\u0138\u0139\u0003\u0012\t\u0000\u0139\u0011"+
		"\u0001\u0000\u0000\u0000\u013a\u013b\u0005v\u0000\u0000\u013b\u0013\u0001"+
		"\u0000\u0000\u0000\u013c\u013d\u0007\u0001\u0000\u0000\u013d\u0015\u0001"+
		"\u0000\u0000\u0000\u013e\u013f\u0007\u0002\u0000\u0000\u013f\u0017\u0001"+
		"\u0000\u0000\u0000\u0140\u0143\u0003\u008eG\u0000\u0141\u0143\u0003\u0090"+
		"H\u0000\u0142\u0140\u0001\u0000\u0000\u0000\u0142\u0141\u0001\u0000\u0000"+
		"\u0000\u0143\u0144\u0001\u0000\u0000\u0000\u0144\u0142\u0001\u0000\u0000"+
		"\u0000\u0144\u0145\u0001\u0000\u0000\u0000\u0145\u0019\u0001\u0000\u0000"+
		"\u0000\u0146\u0147\u0005\u001b\u0000\u0000\u0147\u0148\u0003$\u0012\u0000"+
		"\u0148\u0149\u0005F\u0000\u0000\u0149\u014b\u0003\u001c\u000e\u0000\u014a"+
		"\u014c\u0005#\u0000\u0000\u014b\u014a\u0001\u0000\u0000\u0000\u014b\u014c"+
		"\u0001\u0000\u0000\u0000\u014c\u001b\u0001\u0000\u0000\u0000\u014d\u0150"+
		"\u0003\u001e\u000f\u0000\u014e\u0150\u0003 \u0010\u0000\u014f\u014d\u0001"+
		"\u0000\u0000\u0000\u014f\u014e\u0001\u0000\u0000\u0000\u0150\u001d\u0001"+
		"\u0000\u0000\u0000\u0151\u0153\u0005G\u0000\u0000\u0152\u0154\u0003\""+
		"\u0011\u0000\u0153\u0152\u0001\u0000\u0000\u0000\u0154\u0155\u0001\u0000"+
		"\u0000\u0000\u0155\u0153\u0001\u0000\u0000\u0000\u0155\u0156\u0001\u0000"+
		"\u0000\u0000\u0156\u001f\u0001\u0000\u0000\u0000\u0157\u0159\u0005\"\u0000"+
		"\u0000\u0158\u015a\u0003\"\u0011\u0000\u0159\u0158\u0001\u0000\u0000\u0000"+
		"\u015a\u015b\u0001\u0000\u0000\u0000\u015b\u0159\u0001\u0000\u0000\u0000"+
		"\u015b\u015c\u0001\u0000\u0000\u0000\u015c!\u0001\u0000\u0000\u0000\u015d"+
		"\u015f\u0005\u0002\u0000\u0000\u015e\u0160\u0005r\u0000\u0000\u015f\u015e"+
		"\u0001\u0000\u0000\u0000\u0160\u0161\u0001\u0000\u0000\u0000\u0161\u015f"+
		"\u0001\u0000\u0000\u0000\u0161\u0162\u0001\u0000\u0000\u0000\u0162\u0163"+
		"\u0001\u0000\u0000\u0000\u0163\u0164\u0005\u0003\u0000\u0000\u0164#\u0001"+
		"\u0000\u0000\u0000\u0165\u0166\u0005v\u0000\u0000\u0166%\u0001\u0000\u0000"+
		"\u0000\u0167\u0169\u0005V\u0000\u0000\u0168\u016a\u0003\u00ceg\u0000\u0169"+
		"\u0168\u0001\u0000\u0000\u0000\u0169\u016a\u0001\u0000\u0000\u0000\u016a"+
		"\u016c\u0001\u0000\u0000\u0000\u016b\u016d\u0003(\u0014\u0000\u016c\u016b"+
		"\u0001\u0000\u0000\u0000\u016c\u016d\u0001\u0000\u0000\u0000\u016d\u016f"+
		"\u0001\u0000\u0000\u0000\u016e\u0170\u00030\u0018\u0000\u016f\u016e\u0001"+
		"\u0000\u0000\u0000\u016f\u0170\u0001\u0000\u0000\u0000\u0170\u0172\u0001"+
		"\u0000\u0000\u0000\u0171\u0173\u0003\u009cN\u0000\u0172\u0171\u0001\u0000"+
		"\u0000\u0000\u0173\u0174\u0001\u0000\u0000\u0000\u0174\u0172\u0001\u0000"+
		"\u0000\u0000\u0174\u0175\u0001\u0000\u0000\u0000\u0175\'\u0001\u0000\u0000"+
		"\u0000\u0176\u0179\u0003*\u0015\u0000\u0177\u0179\u0003.\u0017\u0000\u0178"+
		"\u0176\u0001\u0000\u0000\u0000\u0178\u0177\u0001\u0000\u0000\u0000\u0179"+
		")\u0001\u0000\u0000\u0000\u017a\u017c\u0005;\u0000\u0000\u017b\u017d\u0003"+
		",\u0016\u0000\u017c\u017b\u0001\u0000\u0000\u0000\u017c\u017d\u0001\u0000"+
		"\u0000\u0000\u017d+\u0001\u0000\u0000\u0000\u017e\u017f\u0007\u0003\u0000"+
		"\u0000\u017f-\u0001\u0000\u0000\u0000\u0180\u0182\u0007\u0004\u0000\u0000"+
		"\u0181\u0183\u0003,\u0016\u0000\u0182\u0181\u0001\u0000\u0000\u0000\u0182"+
		"\u0183\u0001\u0000\u0000\u0000\u0183/\u0001\u0000\u0000\u0000\u0184\u0187"+
		"\u00032\u0019\u0000\u0185\u0187\u00034\u001a\u0000\u0186\u0184\u0001\u0000"+
		"\u0000\u0000\u0186\u0185\u0001\u0000\u0000\u0000\u01871\u0001\u0000\u0000"+
		"\u0000\u0188\u0189\u0005\u0007\u0000\u0000\u01893\u0001\u0000\u0000\u0000"+
		"\u018a\u018b\u0005_\u0000\u0000\u018b\u018c\u00036\u001b\u0000\u018c5"+
		"\u0001\u0000\u0000\u0000\u018d\u018e\u0003\u00f8|\u0000\u018e7\u0001\u0000"+
		"\u0000\u0000\u018f\u0191\u0005W\u0000\u0000\u0190\u0192\u0003:\u001d\u0000"+
		"\u0191\u0190\u0001\u0000\u0000\u0000\u0191\u0192\u0001\u0000\u0000\u0000"+
		"\u0192\u0194\u0001\u0000\u0000\u0000\u0193\u0195\u0003@ \u0000\u0194\u0193"+
		"\u0001\u0000\u0000\u0000\u0194\u0195\u0001\u0000\u0000\u0000\u0195\u0197"+
		"\u0001\u0000\u0000\u0000\u0196\u0198\u0003B!\u0000\u0197\u0196\u0001\u0000"+
		"\u0000\u0000\u0197\u0198\u0001\u0000\u0000\u0000\u0198\u019a\u0001\u0000"+
		"\u0000\u0000\u0199\u019b\u0003F#\u0000\u019a\u0199\u0001\u0000\u0000\u0000"+
		"\u019a\u019b\u0001\u0000\u0000\u0000\u019b\u019d\u0001\u0000\u0000\u0000"+
		"\u019c\u019e\u0003J%\u0000\u019d\u019c\u0001\u0000\u0000\u0000\u019d\u019e"+
		"\u0001\u0000\u0000\u0000\u019e9\u0001\u0000\u0000\u0000\u019f\u01a1\u0003"+
		"<\u001e\u0000\u01a0\u01a2\u0003>\u001f\u0000\u01a1\u01a0\u0001\u0000\u0000"+
		"\u0000\u01a1\u01a2\u0001\u0000\u0000\u0000\u01a2;\u0001\u0000\u0000\u0000"+
		"\u01a3\u01a4\u0003\u00f8|\u0000\u01a4=\u0001\u0000\u0000\u0000\u01a5\u01a6"+
		"\u0003\u00f8|\u0000\u01a6?\u0001\u0000\u0000\u0000\u01a7\u01a8\u00054"+
		"\u0000\u0000\u01a8\u01a9\u0003\u00f8|\u0000\u01a9A\u0001\u0000\u0000\u0000"+
		"\u01aa\u01ab\u0005\u0016\u0000\u0000\u01ab\u01ac\u0003D\"\u0000\u01ac"+
		"C\u0001\u0000\u0000\u0000\u01ad\u01b4\u0003\u00f8|\u0000\u01ae\u01b4\u0005"+
		"9\u0000\u0000\u01af\u01b4\u0005Z\u0000\u0000\u01b0\u01b4\u0005/\u0000"+
		"\u0000\u01b1\u01b4\u0005*\u0000\u0000\u01b2\u01b4\u00057\u0000\u0000\u01b3"+
		"\u01ad\u0001\u0000\u0000\u0000\u01b3\u01ae\u0001\u0000\u0000\u0000\u01b3"+
		"\u01af\u0001\u0000\u0000\u0000\u01b3\u01b0\u0001\u0000\u0000\u0000\u01b3"+
		"\u01b1\u0001\u0000\u0000\u0000\u01b3\u01b2\u0001\u0000\u0000\u0000\u01b4"+
		"E\u0001\u0000\u0000\u0000\u01b5\u01b6\u0005e\u0000\u0000\u01b6\u01b7\u0003"+
		"H$\u0000\u01b7G\u0001\u0000\u0000\u0000\u01b8\u01b9\u0007\u0005\u0000"+
		"\u0000\u01b9I\u0001\u0000\u0000\u0000\u01ba\u01bb\u0005K\u0000\u0000\u01bb"+
		"\u01bc\u0003L&\u0000\u01bcK\u0001\u0000\u0000\u0000\u01bd\u01be\u0007"+
		"\u0006\u0000\u0000\u01beM\u0001\u0000\u0000\u0000\u01bf\u01c0\u0005H\u0000"+
		"\u0000\u01c0\u01c1\u0007\u0007\u0000\u0000\u01c1\u01c2\u0003\u00f6{\u0000"+
		"\u01c2O\u0001\u0000\u0000\u0000\u01c3\u01c5\u0005 \u0000\u0000\u01c4\u01c6"+
		"\u0003R)\u0000\u01c5\u01c4\u0001\u0000\u0000\u0000\u01c5\u01c6\u0001\u0000"+
		"\u0000\u0000\u01c6\u01c7\u0001\u0000\u0000\u0000\u01c7\u01c9\u0003T*\u0000"+
		"\u01c8\u01ca\u0003V+\u0000\u01c9\u01c8\u0001\u0000\u0000\u0000\u01c9\u01ca"+
		"\u0001\u0000\u0000\u0000\u01ca\u01cc\u0001\u0000\u0000\u0000\u01cb\u01cd"+
		"\u0003X,\u0000\u01cc\u01cb\u0001\u0000\u0000\u0000\u01cc\u01cd\u0001\u0000"+
		"\u0000\u0000\u01cd\u01cf\u0001\u0000\u0000\u0000\u01ce\u01d0\u0003Z-\u0000"+
		"\u01cf\u01ce\u0001\u0000\u0000\u0000\u01cf\u01d0\u0001\u0000\u0000\u0000"+
		"\u01d0Q\u0001\u0000\u0000\u0000\u01d1\u01d2\u0007\b\u0000\u0000\u01d2"+
		"S\u0001\u0000\u0000\u0000\u01d3\u01d4\u0003\u00f8|\u0000\u01d4U\u0001"+
		"\u0000\u0000\u0000\u01d5\u01d6\u0007\t\u0000\u0000\u01d6W\u0001\u0000"+
		"\u0000\u0000\u01d7\u01d8\u0007\n\u0000\u0000\u01d8Y\u0001\u0000\u0000"+
		"\u0000\u01d9\u01dc\u0005M\u0000\u0000\u01da\u01dd\u0003\\.\u0000\u01db"+
		"\u01dd\u0003`0\u0000\u01dc\u01da\u0001\u0000\u0000\u0000\u01dc\u01db\u0001"+
		"\u0000\u0000\u0000\u01dd\u01de\u0001\u0000\u0000\u0000\u01de\u01dc\u0001"+
		"\u0000\u0000\u0000\u01de\u01df\u0001\u0000\u0000\u0000\u01df[\u0001\u0000"+
		"\u0000\u0000\u01e0\u01e2\u0007\b\u0000\u0000\u01e1\u01e0\u0001\u0000\u0000"+
		"\u0000\u01e1\u01e2\u0001\u0000\u0000\u0000\u01e2\u01e3\u0001\u0000\u0000"+
		"\u0000\u01e3\u01e4\u0003^/\u0000\u01e4\u01e5\u0005_\u0000\u0000\u01e5"+
		"\u01e6\u0003\u0086C\u0000\u01e6]\u0001\u0000\u0000\u0000\u01e7\u01e8\u0005"+
		"r\u0000\u0000\u01e8_\u0001\u0000\u0000\u0000\u01e9\u01ea\u00055\u0000"+
		"\u0000\u01ea\u01eb\u0003d2\u0000\u01eb\u01ec\u0003b1\u0000\u01eca\u0001"+
		"\u0000\u0000\u0000\u01ed\u01ee\u0003\u00f8|\u0000\u01eec\u0001\u0000\u0000"+
		"\u0000\u01ef\u01f0\u0003\u00f8|\u0000\u01f0e\u0001\u0000\u0000\u0000\u01f1"+
		"\u01f2\u0005\u001f\u0000\u0000\u01f2\u01f3\u0003h4\u0000\u01f3\u01fe\u0003"+
		"j5\u0000\u01f4\u01fd\u0003l6\u0000\u01f5\u01fd\u0003n7\u0000\u01f6\u01fd"+
		"\u0003p8\u0000\u01f7\u01fd\u0003t:\u0000\u01f8\u01fd\u0003x<\u0000\u01f9"+
		"\u01fd\u0003\u0088D\u0000\u01fa\u01fd\u0003\u0092I\u0000\u01fb\u01fd\u0003"+
		"\u0096K\u0000\u01fc\u01f4\u0001\u0000\u0000\u0000\u01fc\u01f5\u0001\u0000"+
		"\u0000\u0000\u01fc\u01f6\u0001\u0000\u0000\u0000\u01fc\u01f7\u0001\u0000"+
		"\u0000\u0000\u01fc\u01f8\u0001\u0000\u0000\u0000\u01fc\u01f9\u0001\u0000"+
		"\u0000\u0000\u01fc\u01fa\u0001\u0000\u0000\u0000\u01fc\u01fb\u0001\u0000"+
		"\u0000\u0000\u01fd\u0200\u0001\u0000\u0000\u0000\u01fe\u01fc\u0001\u0000"+
		"\u0000\u0000\u01fe\u01ff\u0001\u0000\u0000\u0000\u01ffg\u0001\u0000\u0000"+
		"\u0000\u0200\u01fe\u0001\u0000\u0000\u0000\u0201\u0202\u0003\u00f8|\u0000"+
		"\u0202i\u0001\u0000\u0000\u0000\u0203\u0204\u0003\u00f8|\u0000\u0204k"+
		"\u0001\u0000\u0000\u0000\u0205\u0206\u0007\t\u0000\u0000\u0206m\u0001"+
		"\u0000\u0000\u0000\u0207\u0208\u0007\n\u0000\u0000\u0208o\u0001\u0000"+
		"\u0000\u0000\u0209\u020b\u0005P\u0000\u0000\u020a\u020c\u0003r9\u0000"+
		"\u020b\u020a\u0001\u0000\u0000\u0000\u020b\u020c\u0001\u0000\u0000\u0000"+
		"\u020cq\u0001\u0000\u0000\u0000\u020d\u0214\u0005\u0006\u0000\u0000\u020e"+
		"\u0210\u0007\u000b\u0000\u0000\u020f\u020e\u0001\u0000\u0000\u0000\u0210"+
		"\u0211\u0001\u0000\u0000\u0000\u0211\u020f\u0001\u0000\u0000\u0000\u0211"+
		"\u0212\u0001\u0000\u0000\u0000\u0212\u0214\u0001\u0000\u0000\u0000\u0213"+
		"\u020d\u0001\u0000\u0000\u0000\u0213\u020f\u0001\u0000\u0000\u0000\u0214"+
		"s\u0001\u0000\u0000\u0000\u0215\u0216\u0005\u001c\u0000\u0000\u0216\u0217"+
		"\u0003v;\u0000\u0217u\u0001\u0000\u0000\u0000\u0218\u0219\u0007\f\u0000"+
		"\u0000\u0219w\u0001\u0000\u0000\u0000\u021a\u021d\u0005M\u0000\u0000\u021b"+
		"\u021e\u0003\u0080@\u0000\u021c\u021e\u0003\u0084B\u0000\u021d\u021b\u0001"+
		"\u0000\u0000\u0000\u021d\u021c\u0001\u0000\u0000\u0000\u021e\u021f\u0001"+
		"\u0000\u0000\u0000\u021f\u021d\u0001\u0000\u0000\u0000\u021f\u0220\u0001"+
		"\u0000\u0000\u0000\u0220\u0222\u0001\u0000\u0000\u0000\u0221\u0223\u0003"+
		"z=\u0000\u0222\u0221\u0001\u0000\u0000\u0000\u0222\u0223\u0001\u0000\u0000"+
		"\u0000\u0223y\u0001\u0000\u0000\u0000\u0224\u0225\u00055\u0000\u0000\u0225"+
		"\u0226\u0003~?\u0000\u0226\u0227\u0003|>\u0000\u0227{\u0001\u0000\u0000"+
		"\u0000\u0228\u0229\u0003\u00f8|\u0000\u0229}\u0001\u0000\u0000\u0000\u022a"+
		"\u022b\u0003\u00f8|\u0000\u022b\u007f\u0001\u0000\u0000\u0000\u022c\u022d"+
		"\u0007\b\u0000\u0000\u022d\u022e\u0003\u0082A\u0000\u022e\u0081\u0001"+
		"\u0000\u0000\u0000\u022f\u0230\u0005r\u0000\u0000\u0230\u0083\u0001\u0000"+
		"\u0000\u0000\u0231\u0232\u0005_\u0000\u0000\u0232\u0233\u0003\u0086C\u0000"+
		"\u0233\u0085\u0001\u0000\u0000\u0000\u0234\u0237\u0005\u001d\u0000\u0000"+
		"\u0235\u0237\u0003\u00f8|\u0000\u0236\u0234\u0001\u0000\u0000\u0000\u0236"+
		"\u0235\u0001\u0000\u0000\u0000\u0237\u0087\u0001\u0000\u0000\u0000\u0238"+
		"\u023a\u0005X\u0000\u0000\u0239\u023b\u0003\u008aE\u0000\u023a\u0239\u0001"+
		"\u0000\u0000\u0000\u023a\u023b\u0001\u0000\u0000\u0000\u023b\u023d\u0001"+
		"\u0000\u0000\u0000\u023c\u023e\u0003\u008cF\u0000\u023d\u023c\u0001\u0000"+
		"\u0000\u0000\u023d\u023e\u0001\u0000\u0000\u0000\u023e\u0240\u0001\u0000"+
		"\u0000\u0000\u023f\u0241\u0003\u008eG\u0000\u0240\u023f\u0001\u0000\u0000"+
		"\u0000\u0240\u0241\u0001\u0000\u0000\u0000\u0241\u0243\u0001\u0000\u0000"+
		"\u0000\u0242\u0244\u0003\u0090H\u0000\u0243\u0242\u0001\u0000\u0000\u0000"+
		"\u0243\u0244\u0001\u0000\u0000\u0000\u0244\u0089\u0001\u0000\u0000\u0000"+
		"\u0245\u0249\u0005\u0006\u0000\u0000\u0246\u0247\u0005\u000e\u0000\u0000"+
		"\u0247\u0249\u0005r\u0000\u0000\u0248\u0245\u0001\u0000\u0000\u0000\u0248"+
		"\u0246\u0001\u0000\u0000\u0000\u0249\u008b\u0001\u0000\u0000\u0000\u024a"+
		"\u024b\u0007\r\u0000\u0000\u024b\u008d\u0001\u0000\u0000\u0000\u024c\u024d"+
		"\u0007\u000e\u0000\u0000\u024d\u008f\u0001\u0000\u0000\u0000\u024e\u024f"+
		"\u0007\u000f\u0000\u0000\u024f\u0091\u0001\u0000\u0000\u0000\u0250\u0251"+
		"\u0005\u0013\u0000\u0000\u0251\u0252\u0003\u008aE\u0000\u0252\u0253\u0003"+
		"\u0094J\u0000\u0253\u0093\u0001\u0000\u0000\u0000\u0254\u0255\u0005v\u0000"+
		"\u0000\u0255\u0095\u0001\u0000\u0000\u0000\u0256\u0258\u0005n\u0000\u0000"+
		"\u0257\u0259\u0003\u008aE\u0000\u0258\u0257\u0001\u0000\u0000\u0000\u0258"+
		"\u0259\u0001\u0000\u0000\u0000\u0259\u025b\u0001\u0000\u0000\u0000\u025a"+
		"\u025c\u0003\u0098L\u0000\u025b\u025a\u0001\u0000\u0000\u0000\u025b\u025c"+
		"\u0001\u0000\u0000\u0000\u025c\u025e\u0001\u0000\u0000\u0000\u025d\u025f"+
		"\u0003\u00a8T\u0000\u025e\u025d\u0001\u0000\u0000\u0000\u025e\u025f\u0001"+
		"\u0000\u0000\u0000\u025f\u0261\u0001\u0000\u0000\u0000\u0260\u0262\u0003"+
		"\u009aM\u0000\u0261\u0260\u0001\u0000\u0000\u0000\u0261\u0262\u0001\u0000"+
		"\u0000\u0000\u0262\u0263\u0001\u0000\u0000\u0000\u0263\u0264\u0003\u009c"+
		"N\u0000\u0264\u0097\u0001\u0000\u0000\u0000\u0265\u0266\u0005r\u0000\u0000"+
		"\u0266\u0099\u0001\u0000\u0000\u0000\u0267\u026b\u0005\u0007\u0000\u0000"+
		"\u0268\u0269\u0005_\u0000\u0000\u0269\u026b\u0003\u00f8|\u0000\u026a\u0267"+
		"\u0001\u0000\u0000\u0000\u026a\u0268\u0001\u0000\u0000\u0000\u026b\u009b"+
		"\u0001\u0000\u0000\u0000\u026c\u026e\u00053\u0000\u0000\u026d\u026f\u0003"+
		"\u009eO\u0000\u026e\u026d\u0001\u0000\u0000\u0000\u026f\u0270\u0001\u0000"+
		"\u0000\u0000\u0270\u026e\u0001\u0000\u0000\u0000\u0270\u0271\u0001\u0000"+
		"\u0000\u0000\u0271\u009d\u0001\u0000\u0000\u0000\u0272\u0274\u0003\u00ec"+
		"v\u0000\u0273\u0272\u0001\u0000\u0000\u0000\u0274\u0275\u0001\u0000\u0000"+
		"\u0000\u0275\u0273\u0001\u0000\u0000\u0000\u0275\u0276\u0001\u0000\u0000"+
		"\u0000\u0276\u0278\u0001\u0000\u0000\u0000\u0277\u0279\u0003\u00a2Q\u0000"+
		"\u0278\u0277\u0001\u0000\u0000\u0000\u0278\u0279\u0001\u0000\u0000\u0000"+
		"\u0279\u027b\u0001\u0000\u0000\u0000\u027a\u027c\u0003\u00a4R\u0000\u027b"+
		"\u027a\u0001\u0000\u0000\u0000\u027b\u027c\u0001\u0000\u0000\u0000\u027c"+
		"\u027e\u0001\u0000\u0000\u0000\u027d\u027f\u0003\u00a6S\u0000\u027e\u027d"+
		"\u0001\u0000\u0000\u0000\u027e\u027f\u0001\u0000\u0000\u0000\u027f\u0281"+
		"\u0001\u0000\u0000\u0000\u0280\u0282\u0003\u00a0P\u0000\u0281\u0280\u0001"+
		"\u0000\u0000\u0000\u0282\u0283\u0001\u0000\u0000\u0000\u0283\u0281\u0001"+
		"\u0000\u0000\u0000\u0283\u0284\u0001\u0000\u0000\u0000\u0284\u009f\u0001"+
		"\u0000\u0000\u0000\u0285\u0286\u0005q\u0000\u0000\u0286\u00a1\u0001\u0000"+
		"\u0000\u0000\u0287\u0288\u0007\u0010\u0000\u0000\u0288\u00a3\u0001\u0000"+
		"\u0000\u0000\u0289\u028a\u0007\u0011\u0000\u0000\u028a\u00a5\u0001\u0000"+
		"\u0000\u0000\u028b\u028c\u0007\u0012\u0000\u0000\u028c\u00a7\u0001\u0000"+
		"\u0000\u0000\u028d\u0291\u0003\u00aaU\u0000\u028e\u0291\u0003\u00aeW\u0000"+
		"\u028f\u0291\u0003\u00acV\u0000\u0290\u028d\u0001\u0000\u0000\u0000\u0290"+
		"\u028e\u0001\u0000\u0000\u0000\u0290\u028f\u0001\u0000\u0000\u0000\u0291"+
		"\u00a9\u0001\u0000\u0000\u0000\u0292\u0294\u0005;\u0000\u0000\u0293\u0295"+
		"\u0003\u00acV\u0000\u0294\u0293\u0001\u0000\u0000\u0000\u0294\u0295\u0001"+
		"\u0000\u0000\u0000\u0295\u00ab\u0001\u0000\u0000\u0000\u0296\u02a1\u0005"+
		"\u000f\u0000\u0000\u0297\u02a1\u0005f\u0000\u0000\u0298\u02a1\u0005\u000b"+
		"\u0000\u0000\u0299\u02a1\u00051\u0000\u0000\u029a\u02a1\u0005O\u0000\u0000"+
		"\u029b\u02a1\u0005\b\u0000\u0000\u029c\u029e\u0005.\u0000\u0000\u029d"+
		"\u029f\u00050\u0000\u0000\u029e\u029d\u0001\u0000\u0000\u0000\u029e\u029f"+
		"\u0001\u0000\u0000\u0000\u029f\u02a1\u0001\u0000\u0000\u0000\u02a0\u0296"+
		"\u0001\u0000\u0000\u0000\u02a0\u0297\u0001\u0000\u0000\u0000\u02a0\u0298"+
		"\u0001\u0000\u0000\u0000\u02a0\u0299\u0001\u0000\u0000\u0000\u02a0\u029a"+
		"\u0001\u0000\u0000\u0000\u02a0\u029b\u0001\u0000\u0000\u0000\u02a0\u029c"+
		"\u0001\u0000\u0000\u0000\u02a1\u02a2\u0001\u0000\u0000\u0000\u02a2\u02a0"+
		"\u0001\u0000\u0000\u0000\u02a2\u02a3\u0001\u0000\u0000\u0000\u02a3\u00ad"+
		"\u0001\u0000\u0000\u0000\u02a4\u02a6\u0007\u0004\u0000\u0000\u02a5\u02a7"+
		"\u0003\u00acV\u0000\u02a6\u02a5\u0001\u0000\u0000\u0000\u02a6\u02a7\u0001"+
		"\u0000\u0000\u0000\u02a7\u00af\u0001\u0000\u0000\u0000\u02a8\u02a9\u0005"+
		"J\u0000\u0000\u02a9\u02aa\u0003\u00b2Y\u0000\u02aa\u02ab\u0003\u00b4Z"+
		"\u0000\u02ab\u00b1\u0001\u0000\u0000\u0000\u02ac\u02ae\u0007\u0013\u0000"+
		"\u0000\u02ad\u02ac\u0001\u0000\u0000\u0000\u02ad\u02ae\u0001\u0000\u0000"+
		"\u0000\u02ae\u02af\u0001\u0000\u0000\u0000\u02af\u02b0\u0003\u00f8|\u0000"+
		"\u02b0\u00b3\u0001\u0000\u0000\u0000\u02b1\u02b3\u0007\u0013\u0000\u0000"+
		"\u02b2\u02b1\u0001\u0000\u0000\u0000\u02b2\u02b3\u0001\u0000\u0000\u0000"+
		"\u02b3\u02b4\u0001\u0000\u0000\u0000\u02b4\u02b5\u0003\u00f8|\u0000\u02b5"+
		"\u00b5\u0001\u0000\u0000\u0000\u02b6\u02ba\u0005\u0015\u0000\u0000\u02b7"+
		"\u02b9\u0003\u00b8\\\u0000\u02b8\u02b7\u0001\u0000\u0000\u0000\u02b9\u02bc"+
		"\u0001\u0000\u0000\u0000\u02ba\u02b8\u0001\u0000\u0000\u0000\u02ba\u02bb"+
		"\u0001\u0000\u0000\u0000\u02bb\u02c0\u0001\u0000\u0000\u0000\u02bc\u02ba"+
		"\u0001\u0000\u0000\u0000\u02bd\u02bf\u0003\u00ba]\u0000\u02be\u02bd\u0001"+
		"\u0000\u0000\u0000\u02bf\u02c2\u0001\u0000\u0000\u0000\u02c0\u02be\u0001"+
		"\u0000\u0000\u0000\u02c0\u02c1\u0001\u0000\u0000\u0000\u02c1\u02c6\u0001"+
		"\u0000\u0000\u0000\u02c2\u02c0\u0001\u0000\u0000\u0000\u02c3\u02c5\u0003"+
		"\u00bc^\u0000\u02c4\u02c3\u0001\u0000\u0000\u0000\u02c5\u02c8\u0001\u0000"+
		"\u0000\u0000\u02c6\u02c4\u0001\u0000\u0000\u0000\u02c6\u02c7\u0001\u0000"+
		"\u0000\u0000\u02c7\u02cc\u0001\u0000\u0000\u0000\u02c8\u02c6\u0001\u0000"+
		"\u0000\u0000\u02c9\u02cb\u0003\u00be_\u0000\u02ca\u02c9\u0001\u0000\u0000"+
		"\u0000\u02cb\u02ce\u0001\u0000\u0000\u0000\u02cc\u02ca\u0001\u0000\u0000"+
		"\u0000\u02cc\u02cd\u0001\u0000\u0000\u0000\u02cd\u00b7\u0001\u0000\u0000"+
		"\u0000\u02ce\u02cc\u0001\u0000\u0000\u0000\u02cf\u02d0\u0007\u0014\u0000"+
		"\u0000\u02d0\u00b9\u0001\u0000\u0000\u0000\u02d1\u02d2\u0007\u0015\u0000"+
		"\u0000\u02d2\u00bb\u0001\u0000\u0000\u0000\u02d3\u02d4\u0007\u0016\u0000"+
		"\u0000\u02d4\u00bd\u0001\u0000\u0000\u0000\u02d5\u02d6\u0007\u0017\u0000"+
		"\u0000\u02d6\u00bf\u0001\u0000\u0000\u0000\u02d7\u02d8\u0005E\u0000\u0000"+
		"\u02d8\u02d9\u0003\u00c2a\u0000\u02d9\u02da\u0005Y\u0000\u0000\u02da\u02db"+
		"\u0003\u00c4b\u0000\u02db\u02dc\u0003\u00c6c\u0000\u02dc\u02dd\u0005C"+
		"\u0000\u0000\u02dd\u02de\u0003\u00c8d\u0000\u02de\u02df\u0003\u00cae\u0000"+
		"\u02df\u00c1\u0001\u0000\u0000\u0000\u02e0\u02e1\u0005v\u0000\u0000\u02e1"+
		"\u00c3\u0001\u0000\u0000\u0000\u02e2\u02e3\u0003\u00f8|\u0000\u02e3\u00c5"+
		"\u0001\u0000\u0000\u0000\u02e4\u02e5\u0003\u00f8|\u0000\u02e5\u00c7\u0001"+
		"\u0000\u0000\u0000\u02e6\u02e7\u0003\u00f8|\u0000\u02e7\u00c9\u0001\u0000"+
		"\u0000\u0000\u02e8\u02e9\u0003\u00f8|\u0000\u02e9\u00cb\u0001\u0000\u0000"+
		"\u0000\u02ea\u02eb\u0005D\u0000\u0000\u02eb\u02ec\u0003\u00ceg\u0000\u02ec"+
		"\u00cd\u0001\u0000\u0000\u0000\u02ed\u02ee\u0005r\u0000\u0000\u02ee\u00cf"+
		"\u0001\u0000\u0000\u0000\u02ef\u02f2\u0003\u00d2i\u0000\u02f0\u02f2\u0003"+
		"\u00d4j\u0000\u02f1\u02ef\u0001\u0000\u0000\u0000\u02f1\u02f0\u0001\u0000"+
		"\u0000\u0000\u02f2\u00d1\u0001\u0000\u0000\u0000\u02f3\u02f6\u0005&\u0000"+
		"\u0000\u02f4\u02f7\u0003\u00dam\u0000\u02f5\u02f7\u0003\u00dcn\u0000\u02f6"+
		"\u02f4\u0001\u0000\u0000\u0000\u02f6\u02f5\u0001\u0000\u0000\u0000\u02f7"+
		"\u02f9\u0001\u0000\u0000\u0000\u02f8\u02fa\u0003\u00deo\u0000\u02f9\u02f8"+
		"\u0001\u0000\u0000\u0000\u02f9\u02fa\u0001\u0000\u0000\u0000\u02fa\u02fc"+
		"\u0001\u0000\u0000\u0000\u02fb\u02fd\u0003\u00e2q\u0000\u02fc\u02fb\u0001"+
		"\u0000\u0000\u0000\u02fc\u02fd\u0001\u0000\u0000\u0000\u02fd\u02ff\u0001"+
		"\u0000\u0000\u0000\u02fe\u0300\u0003\u00e4r\u0000\u02ff\u02fe\u0001\u0000"+
		"\u0000\u0000\u02ff\u0300\u0001\u0000\u0000\u0000\u0300\u0302\u0001\u0000"+
		"\u0000\u0000\u0301\u0303\u0003\u00e6s\u0000\u0302\u0301\u0001\u0000\u0000"+
		"\u0000\u0302\u0303\u0001\u0000\u0000\u0000\u0303\u0305\u0001\u0000\u0000"+
		"\u0000\u0304\u0306\u0003\u00e8t\u0000\u0305\u0304\u0001\u0000\u0000\u0000"+
		"\u0305\u0306\u0001\u0000\u0000\u0000\u0306\u00d3\u0001\u0000\u0000\u0000"+
		"\u0307\u030a\u0005&\u0000\u0000\u0308\u030b\u0003\u00dam\u0000\u0309\u030b"+
		"\u0003\u00dcn\u0000\u030a\u0308\u0001\u0000\u0000\u0000\u030a\u0309\u0001"+
		"\u0000\u0000\u0000\u030b\u030d\u0001\u0000\u0000\u0000\u030c\u030e\u0003"+
		"\u00d6k\u0000\u030d\u030c\u0001\u0000\u0000\u0000\u030d\u030e\u0001\u0000"+
		"\u0000\u0000\u030e\u0310\u0001\u0000\u0000\u0000\u030f\u0311\u0003\u00e2"+
		"q\u0000\u0310\u030f\u0001\u0000\u0000\u0000\u0310\u0311\u0001\u0000\u0000"+
		"\u0000\u0311\u0313\u0001\u0000\u0000\u0000\u0312\u0314\u0003\u00e4r\u0000"+
		"\u0313\u0312\u0001\u0000\u0000\u0000\u0313\u0314\u0001\u0000\u0000\u0000"+
		"\u0314\u0316\u0001\u0000\u0000\u0000\u0315\u0317\u0003\u00e6s\u0000\u0316"+
		"\u0315\u0001\u0000\u0000\u0000\u0316\u0317\u0001\u0000\u0000\u0000\u0317"+
		"\u0319\u0001\u0000\u0000\u0000\u0318\u031a\u0003\u00e8t\u0000\u0319\u0318"+
		"\u0001\u0000\u0000\u0000\u0319\u031a\u0001\u0000\u0000\u0000\u031a\u00d5"+
		"\u0001\u0000\u0000\u0000\u031b\u031c\u0005%\u0000\u0000\u031c\u031d\u0003"+
		"\u00d8l\u0000\u031d\u00d7\u0001\u0000\u0000\u0000\u031e\u031f\u0007\u0018"+
		"\u0000\u0000\u031f\u00d9\u0001\u0000\u0000\u0000\u0320\u0322\u0003\u00ec"+
		"v\u0000\u0321\u0320\u0001\u0000\u0000\u0000\u0321\u0322\u0001\u0000\u0000"+
		"\u0000\u0322\u0323\u0001\u0000\u0000\u0000\u0323\u0324\u0003\u00eew\u0000"+
		"\u0324\u00db\u0001\u0000\u0000\u0000\u0325\u0326\u0003\u00ecv\u0000\u0326"+
		"\u0327\u0005\u0011\u0000\u0000\u0327\u0328\u0003\u00f0x\u0000\u0328\u0329"+
		"\u0005\u0012\u0000\u0000\u0329\u032a\u0003\u00f2y\u0000\u032a\u00dd\u0001"+
		"\u0000\u0000\u0000\u032b\u032c\u0005\u001a\u0000\u0000\u032c\u032d\u0003"+
		"\u00e0p\u0000\u032d\u00df\u0001\u0000\u0000\u0000\u032e\u032f\u0007\u0019"+
		"\u0000\u0000\u032f\u00e1\u0001\u0000\u0000\u0000\u0330\u0331\u0005+\u0000"+
		"\u0000\u0331\u0332\u0003\u00f8|\u0000\u0332\u00e3\u0001\u0000\u0000\u0000"+
		"\u0333\u0334\u0005Q\u0000\u0000\u0334\u0335\u0003\u00f8|\u0000\u0335\u00e5"+
		"\u0001\u0000\u0000\u0000\u0336\u0337\u0005\u0013\u0000\u0000\u0337\u0338"+
		"\u0003\u00eau\u0000\u0338\u00e7\u0001\u0000\u0000\u0000\u0339\u033a\u0005"+
		"i\u0000\u0000\u033a\u033b\u0003\u00eau\u0000\u033b\u00e9\u0001\u0000\u0000"+
		"\u0000\u033c\u033d\u0005v\u0000\u0000\u033d\u00eb\u0001\u0000\u0000\u0000"+
		"\u033e\u033f\u0005v\u0000\u0000\u033f\u00ed\u0001\u0000\u0000\u0000\u0340"+
		"\u0341\u0005v\u0000\u0000\u0341\u00ef\u0001\u0000\u0000\u0000\u0342\u0343"+
		"\u0005v\u0000\u0000\u0343\u00f1\u0001\u0000\u0000\u0000\u0344\u0345\u0005"+
		"v\u0000\u0000\u0345\u00f3\u0001\u0000\u0000\u0000\u0346\u0347\u0005\u001b"+
		"\u0000\u0000\u0347\u0348\u0003\u00f6{\u0000\u0348\u034a\u0005)\u0000\u0000"+
		"\u0349\u034b\u0003\u0002\u0001\u0000\u034a\u0349\u0001\u0000\u0000\u0000"+
		"\u034b\u034c\u0001\u0000\u0000\u0000\u034c\u034a\u0001\u0000\u0000\u0000"+
		"\u034c\u034d\u0001\u0000\u0000\u0000\u034d\u034e\u0001\u0000\u0000\u0000"+
		"\u034e\u034f\u0005#\u0000\u0000\u034f\u00f5\u0001\u0000\u0000\u0000\u0350"+
		"\u0351\u0005v\u0000\u0000\u0351\u00f7\u0001\u0000\u0000\u0000\u0352\u0354"+
		"\u0005r\u0000\u0000\u0353\u0355\u0007\u001a\u0000\u0000\u0354\u0353\u0001"+
		"\u0000\u0000\u0000\u0354\u0355\u0001\u0000\u0000\u0000\u0355\u00f9\u0001"+
		"\u0000\u0000\u0000[\u00fd\u0110\u0114\u0119\u0129\u012c\u012f\u0132\u0135"+
		"\u0142\u0144\u014b\u014f\u0155\u015b\u0161\u0169\u016c\u016f\u0174\u0178"+
		"\u017c\u0182\u0186\u0191\u0194\u0197\u019a\u019d\u01a1\u01b3\u01c5\u01c9"+
		"\u01cc\u01cf\u01dc\u01de\u01e1\u01fc\u01fe\u020b\u0211\u0213\u021d\u021f"+
		"\u0222\u0236\u023a\u023d\u0240\u0243\u0248\u0258\u025b\u025e\u0261\u026a"+
		"\u0270\u0275\u0278\u027b\u027e\u0283\u0290\u0294\u029e\u02a0\u02a2\u02a6"+
		"\u02ad\u02b2\u02ba\u02c0\u02c6\u02cc\u02f1\u02f6\u02f9\u02fc\u02ff\u0302"+
		"\u0305\u030a\u030d\u0310\u0313\u0316\u0319\u0321\u034c\u0354";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}