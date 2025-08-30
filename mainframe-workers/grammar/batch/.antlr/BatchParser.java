// Generated from /Users/nguyen/Work/mainframe-workers/grammar/batch/Batch.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class BatchParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		COND_COLON=1, STRING=2, ECHOSTATEMENT=3, REMSTATEMENT=4, EXE_FILE=5, ENABLEDELAYEDEXPANSION=6, 
		DISABLEDELAYEDEXPANSION=7, INT=8, WS=9, NL=10, COMMENTLINE=11, LPAREN=12, 
		RPAREN=13, ECHO=14, SET=15, SETLOCAL=16, REM=17, COLON=18, EQUAL=19, JP_EQUAL=20, 
		ATSIGN=21, SLASH=22, QUESTION=23, SSLASH=24, DASH_SFX=25, DASH_TZIP=26, 
		DASH_SORT=27, DASH_INPUT=28, DASH_OUTPUT=29, DASH_OPTION=30, DASH_RECORD=31, 
		DASH_P=32, DASH_W=33, DASH_Y=34, SLASH_W=35, SLASH_P=36, SLASH_C=37, SLASH_V=38, 
		SLASH_Q=39, SLASH_F=40, SLASH_L=41, SLASH_G=42, SLASH_D=43, SLASH_U=44, 
		SLASH_I=45, SLASH_S=46, SLASH_E=47, SLASH_T=48, SLASH_K=49, SLASH_R=50, 
		SLASH_H=51, SLASH_A=52, SLASH_M=53, SLASH_N=54, SLASH_O=55, SLASH_X=56, 
		SLASH_Y=57, SLASH_Z=58, SLASH_B=59, SLASH_J=60, SLASH_COMPRESS=61, SLASH_EXCLUDE=62, 
		DOT=63, COND=64, DISK_ADDRESS=65, BSORTEX=66, CALL=67, DEL=68, ELSE=69, 
		EQU=70, EXIST=71, EXE=72, ENDLOCAL=73, EXIT=74, IF=75, GOTO=76, GTR=77, 
		NUL=78, NEQ=79, PAUSE=80, RMDIR=81, FOR=82, IN=83, DO=84, PERCENT=85, 
		EXCLAMATION=86, MKDIR=87, XCOPY=88, TYPE=89, Z7=90, DASH=91, UNDERSCORE=92, 
		GREATER_CHAR=93, TILDE=94, TILDE_NX=95, COMMA=96, PLUS=97, STAR=98, JP_TXT=99, 
		JP_CHAR=100, IDENTIFIER=101, STRING_CHARACTERS=102;
	public static final int
		RULE_startRule = 0, RULE_label = 1, RULE_labelName = 2, RULE_statement = 3, 
		RULE_z7Statement = 4, RULE_z7Command = 5, RULE_z7Switches = 6, RULE_z7Switch = 7, 
		RULE_echoStatement = 8, RULE_remStatement = 9, RULE_bsortexStatement = 10, 
		RULE_sortParameters = 11, RULE_sortParameter = 12, RULE_sortValue = 13, 
		RULE_inputParameters = 14, RULE_inputParameter = 15, RULE_recordParameters = 16, 
		RULE_recordParameter = 17, RULE_optionParameters = 18, RULE_optionParameter = 19, 
		RULE_outputParameters = 20, RULE_outputParameter = 21, RULE_outputValue = 22, 
		RULE_callStatement = 23, RULE_callWithLabel = 24, RULE_callWithFilePath = 25, 
		RULE_batchParameters = 26, RULE_batchParameter = 27, RULE_conditionParameter = 28, 
		RULE_delStatement = 29, RULE_endlocalStatement = 30, RULE_execStatement = 31, 
		RULE_execFile = 32, RULE_execParameter = 33, RULE_concatenateFileContent = 34, 
		RULE_exitStatement = 35, RULE_exitCurrentBatch = 36, RULE_exitCode = 37, 
		RULE_forStatement = 38, RULE_configurationString = 39, RULE_forValues = 40, 
		RULE_forValue = 41, RULE_forVariable = 42, RULE_forVariableModifier = 43, 
		RULE_forDo = 44, RULE_gotoStatement = 45, RULE_ifStatement = 46, RULE_ifThen = 47, 
		RULE_ifElse = 48, RULE_simpleIf = 49, RULE_condition = 50, RULE_leftConditionOperator = 51, 
		RULE_rightConditionOperator = 52, RULE_relationalOperator = 53, RULE_mkdirStatement = 54, 
		RULE_setLocalStatement = 55, RULE_typeStatement = 56, RULE_rmdirStatement = 57, 
		RULE_xcopyStatement = 58, RULE_xCopySource = 59, RULE_xCopyDestination = 60, 
		RULE_switches = 61, RULE_switch = 62, RULE_dateFormat = 63, RULE_setLocalOption = 64, 
		RULE_setStatement = 65, RULE_displayFormating = 66, RULE_assignmentPart = 67, 
		RULE_pauseStatement = 68, RULE_variableName = 69, RULE_value = 70, RULE_calcValue = 71, 
		RULE_calcOperator = 72, RULE_filePath = 73, RULE_fileName = 74, RULE_fileNameChar = 75, 
		RULE_identifierCombinedWithReferencedVariable = 76, RULE_idetifierOrRerencedVariable = 77, 
		RULE_referencedVariable = 78, RULE_variableSubstring = 79, RULE_leftSubstring = 80, 
		RULE_rightSubstring = 81, RULE_replacedOrRemovedSubstring = 82, RULE_removeSubstring = 83, 
		RULE_removedSubstring = 84, RULE_removeSpaces = 85, RULE_replaceSubstring = 86, 
		RULE_subtringRemoved = 87, RULE_subStringReplaced = 88, RULE_startSub = 89, 
		RULE_lengthSub = 90, RULE_variableStart = 91, RULE_variableLength = 92, 
		RULE_concatenateString = 93;
	private static String[] makeRuleNames() {
		return new String[] {
			"startRule", "label", "labelName", "statement", "z7Statement", "z7Command", 
			"z7Switches", "z7Switch", "echoStatement", "remStatement", "bsortexStatement", 
			"sortParameters", "sortParameter", "sortValue", "inputParameters", "inputParameter", 
			"recordParameters", "recordParameter", "optionParameters", "optionParameter", 
			"outputParameters", "outputParameter", "outputValue", "callStatement", 
			"callWithLabel", "callWithFilePath", "batchParameters", "batchParameter", 
			"conditionParameter", "delStatement", "endlocalStatement", "execStatement", 
			"execFile", "execParameter", "concatenateFileContent", "exitStatement", 
			"exitCurrentBatch", "exitCode", "forStatement", "configurationString", 
			"forValues", "forValue", "forVariable", "forVariableModifier", "forDo", 
			"gotoStatement", "ifStatement", "ifThen", "ifElse", "simpleIf", "condition", 
			"leftConditionOperator", "rightConditionOperator", "relationalOperator", 
			"mkdirStatement", "setLocalStatement", "typeStatement", "rmdirStatement", 
			"xcopyStatement", "xCopySource", "xCopyDestination", "switches", "switch", 
			"dateFormat", "setLocalOption", "setStatement", "displayFormating", "assignmentPart", 
			"pauseStatement", "variableName", "value", "calcValue", "calcOperator", 
			"filePath", "fileName", "fileNameChar", "identifierCombinedWithReferencedVariable", 
			"idetifierOrRerencedVariable", "referencedVariable", "variableSubstring", 
			"leftSubstring", "rightSubstring", "replacedOrRemovedSubstring", "removeSubstring", 
			"removedSubstring", "removeSpaces", "replaceSubstring", "subtringRemoved", 
			"subStringReplaced", "startSub", "lengthSub", "variableStart", "variableLength", 
			"concatenateString"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'COND:'", null, null, null, null, "'EnableDelayedExpansion'", 
			"'DisableDelayedExpansion'", null, null, null, null, "'('", "')'", "'echo'", 
			"'set'", "'setlocal'", "'rem'", "':'", "'='", "'\\uFF1D'", "'@'", "'/'", 
			"'?'", "'\\'", "'-sfx'", "'-tzip'", "'-sort'", "'-input'", "'-output'", 
			"'-option'", "'-record'", null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, "'/compress'", 
			"'/exclude'", "'.'", "'COND'", null, "'bsortex'", null, "'del'", "'else'", 
			"'equ'", "'exist'", "'exe'", "'endlocal'", "'exit'", null, "'goto'", 
			"'gtr'", "'nul'", "'neq'", "'pause'", "'rmdir'", "'for'", null, null, 
			"'%'", "'!'", "'mkdir'", "'xcopy'", "'type'", "'7z'", "'-'", "'_'", "'>'", 
			"'~'", "'~nx'", "','", "'+'", "'*'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "COND_COLON", "STRING", "ECHOSTATEMENT", "REMSTATEMENT", "EXE_FILE", 
			"ENABLEDELAYEDEXPANSION", "DISABLEDELAYEDEXPANSION", "INT", "WS", "NL", 
			"COMMENTLINE", "LPAREN", "RPAREN", "ECHO", "SET", "SETLOCAL", "REM", 
			"COLON", "EQUAL", "JP_EQUAL", "ATSIGN", "SLASH", "QUESTION", "SSLASH", 
			"DASH_SFX", "DASH_TZIP", "DASH_SORT", "DASH_INPUT", "DASH_OUTPUT", "DASH_OPTION", 
			"DASH_RECORD", "DASH_P", "DASH_W", "DASH_Y", "SLASH_W", "SLASH_P", "SLASH_C", 
			"SLASH_V", "SLASH_Q", "SLASH_F", "SLASH_L", "SLASH_G", "SLASH_D", "SLASH_U", 
			"SLASH_I", "SLASH_S", "SLASH_E", "SLASH_T", "SLASH_K", "SLASH_R", "SLASH_H", 
			"SLASH_A", "SLASH_M", "SLASH_N", "SLASH_O", "SLASH_X", "SLASH_Y", "SLASH_Z", 
			"SLASH_B", "SLASH_J", "SLASH_COMPRESS", "SLASH_EXCLUDE", "DOT", "COND", 
			"DISK_ADDRESS", "BSORTEX", "CALL", "DEL", "ELSE", "EQU", "EXIST", "EXE", 
			"ENDLOCAL", "EXIT", "IF", "GOTO", "GTR", "NUL", "NEQ", "PAUSE", "RMDIR", 
			"FOR", "IN", "DO", "PERCENT", "EXCLAMATION", "MKDIR", "XCOPY", "TYPE", 
			"Z7", "DASH", "UNDERSCORE", "GREATER_CHAR", "TILDE", "TILDE_NX", "COMMA", 
			"PLUS", "STAR", "JP_TXT", "JP_CHAR", "IDENTIFIER", "STRING_CHARACTERS"
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
	public String getGrammarFileName() { return "Batch.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public BatchParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StartRuleContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(BatchParser.EOF, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public List<LabelContext> label() {
			return getRuleContexts(LabelContext.class);
		}
		public LabelContext label(int i) {
			return getRuleContext(LabelContext.class,i);
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
			setState(191);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & -9223372036829511624L) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & 96803721103L) != 0)) {
				{
				{
				setState(188);
				statement();
				}
				}
				setState(193);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(197);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COLON) {
				{
				{
				setState(194);
				label();
				}
				}
				setState(199);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(200);
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
	public static class LabelContext extends ParserRuleContext {
		public LabelNameContext labelName() {
			return getRuleContext(LabelNameContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public LabelContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_label; }
	}

	public final LabelContext label() throws RecognitionException {
		LabelContext _localctx = new LabelContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_label);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(202);
			labelName();
			setState(206);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & -9223372036829511624L) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & 96803721103L) != 0)) {
				{
				{
				setState(203);
				statement();
				}
				}
				setState(208);
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
	public static class LabelNameContext extends ParserRuleContext {
		public TerminalNode COLON() { return getToken(BatchParser.COLON, 0); }
		public TerminalNode IDENTIFIER() { return getToken(BatchParser.IDENTIFIER, 0); }
		public LabelNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_labelName; }
	}

	public final LabelNameContext labelName() throws RecognitionException {
		LabelNameContext _localctx = new LabelNameContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_labelName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(209);
			match(COLON);
			setState(210);
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
	public static class StatementContext extends ParserRuleContext {
		public SetStatementContext setStatement() {
			return getRuleContext(SetStatementContext.class,0);
		}
		public SetLocalStatementContext setLocalStatement() {
			return getRuleContext(SetLocalStatementContext.class,0);
		}
		public DelStatementContext delStatement() {
			return getRuleContext(DelStatementContext.class,0);
		}
		public PauseStatementContext pauseStatement() {
			return getRuleContext(PauseStatementContext.class,0);
		}
		public MkdirStatementContext mkdirStatement() {
			return getRuleContext(MkdirStatementContext.class,0);
		}
		public XcopyStatementContext xcopyStatement() {
			return getRuleContext(XcopyStatementContext.class,0);
		}
		public CallStatementContext callStatement() {
			return getRuleContext(CallStatementContext.class,0);
		}
		public IfStatementContext ifStatement() {
			return getRuleContext(IfStatementContext.class,0);
		}
		public GotoStatementContext gotoStatement() {
			return getRuleContext(GotoStatementContext.class,0);
		}
		public EchoStatementContext echoStatement() {
			return getRuleContext(EchoStatementContext.class,0);
		}
		public RemStatementContext remStatement() {
			return getRuleContext(RemStatementContext.class,0);
		}
		public EndlocalStatementContext endlocalStatement() {
			return getRuleContext(EndlocalStatementContext.class,0);
		}
		public ExitStatementContext exitStatement() {
			return getRuleContext(ExitStatementContext.class,0);
		}
		public ExecStatementContext execStatement() {
			return getRuleContext(ExecStatementContext.class,0);
		}
		public RmdirStatementContext rmdirStatement() {
			return getRuleContext(RmdirStatementContext.class,0);
		}
		public ForStatementContext forStatement() {
			return getRuleContext(ForStatementContext.class,0);
		}
		public TypeStatementContext typeStatement() {
			return getRuleContext(TypeStatementContext.class,0);
		}
		public Z7StatementContext z7Statement() {
			return getRuleContext(Z7StatementContext.class,0);
		}
		public BsortexStatementContext bsortexStatement() {
			return getRuleContext(BsortexStatementContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_statement);
		try {
			setState(231);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SET:
				enterOuterAlt(_localctx, 1);
				{
				setState(212);
				setStatement();
				}
				break;
			case SETLOCAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(213);
				setLocalStatement();
				}
				break;
			case DEL:
				enterOuterAlt(_localctx, 3);
				{
				setState(214);
				delStatement();
				}
				break;
			case PAUSE:
				enterOuterAlt(_localctx, 4);
				{
				setState(215);
				pauseStatement();
				}
				break;
			case MKDIR:
				enterOuterAlt(_localctx, 5);
				{
				setState(216);
				mkdirStatement();
				}
				break;
			case XCOPY:
				enterOuterAlt(_localctx, 6);
				{
				setState(217);
				xcopyStatement();
				}
				break;
			case CALL:
				enterOuterAlt(_localctx, 7);
				{
				setState(218);
				callStatement();
				}
				break;
			case IF:
				enterOuterAlt(_localctx, 8);
				{
				setState(219);
				ifStatement();
				}
				break;
			case GOTO:
				enterOuterAlt(_localctx, 9);
				{
				setState(220);
				gotoStatement();
				}
				break;
			case ECHOSTATEMENT:
				enterOuterAlt(_localctx, 10);
				{
				setState(221);
				echoStatement();
				}
				break;
			case REMSTATEMENT:
				enterOuterAlt(_localctx, 11);
				{
				setState(222);
				remStatement();
				}
				break;
			case ENDLOCAL:
				enterOuterAlt(_localctx, 12);
				{
				setState(223);
				endlocalStatement();
				}
				break;
			case EXIT:
				enterOuterAlt(_localctx, 13);
				{
				setState(224);
				exitStatement();
				}
				break;
			case EXE_FILE:
				enterOuterAlt(_localctx, 14);
				{
				setState(225);
				execStatement();
				}
				break;
			case RMDIR:
				enterOuterAlt(_localctx, 15);
				{
				setState(226);
				rmdirStatement();
				}
				break;
			case FOR:
				enterOuterAlt(_localctx, 16);
				{
				setState(227);
				forStatement();
				}
				break;
			case TYPE:
				enterOuterAlt(_localctx, 17);
				{
				setState(228);
				typeStatement();
				}
				break;
			case QUESTION:
			case SSLASH:
			case DOT:
			case DISK_ADDRESS:
			case EXE:
			case PERCENT:
			case EXCLAMATION:
			case UNDERSCORE:
			case COMMA:
			case STAR:
			case JP_TXT:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 18);
				{
				setState(229);
				z7Statement();
				}
				break;
			case BSORTEX:
				enterOuterAlt(_localctx, 19);
				{
				setState(230);
				bsortexStatement();
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
	public static class Z7StatementContext extends ParserRuleContext {
		public FilePathContext filePath() {
			return getRuleContext(FilePathContext.class,0);
		}
		public TerminalNode Z7() { return getToken(BatchParser.Z7, 0); }
		public Z7CommandContext z7Command() {
			return getRuleContext(Z7CommandContext.class,0);
		}
		public Z7SwitchesContext z7Switches() {
			return getRuleContext(Z7SwitchesContext.class,0);
		}
		public Z7StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_z7Statement; }
	}

	public final Z7StatementContext z7Statement() throws RecognitionException {
		Z7StatementContext _localctx = new Z7StatementContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_z7Statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(233);
			filePath();
			setState(234);
			match(Z7);
			setState(235);
			z7Command();
			setState(236);
			z7Switches();
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
	public static class Z7CommandContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(BatchParser.IDENTIFIER, 0); }
		public Z7CommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_z7Command; }
	}

	public final Z7CommandContext z7Command() throws RecognitionException {
		Z7CommandContext _localctx = new Z7CommandContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_z7Command);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(238);
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
	public static class Z7SwitchesContext extends ParserRuleContext {
		public List<Z7SwitchContext> z7Switch() {
			return getRuleContexts(Z7SwitchContext.class);
		}
		public Z7SwitchContext z7Switch(int i) {
			return getRuleContext(Z7SwitchContext.class,i);
		}
		public Z7SwitchesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_z7Switches; }
	}

	public final Z7SwitchesContext z7Switches() throws RecognitionException {
		Z7SwitchesContext _localctx = new Z7SwitchesContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_z7Switches);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(241); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(240);
				z7Switch();
				}
				}
				setState(243); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 30165434368L) != 0) );
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
	public static class Z7SwitchContext extends ParserRuleContext {
		public TerminalNode DASH_SFX() { return getToken(BatchParser.DASH_SFX, 0); }
		public TerminalNode DASH_P() { return getToken(BatchParser.DASH_P, 0); }
		public TerminalNode DASH_W() { return getToken(BatchParser.DASH_W, 0); }
		public TerminalNode DASH_Y() { return getToken(BatchParser.DASH_Y, 0); }
		public TerminalNode DASH_TZIP() { return getToken(BatchParser.DASH_TZIP, 0); }
		public List<ReferencedVariableContext> referencedVariable() {
			return getRuleContexts(ReferencedVariableContext.class);
		}
		public ReferencedVariableContext referencedVariable(int i) {
			return getRuleContext(ReferencedVariableContext.class,i);
		}
		public Z7SwitchContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_z7Switch; }
	}

	public final Z7SwitchContext z7Switch() throws RecognitionException {
		Z7SwitchContext _localctx = new Z7SwitchContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_z7Switch);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(245);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 30165434368L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(249);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(246);
					referencedVariable();
					}
					} 
				}
				setState(251);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
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
	public static class EchoStatementContext extends ParserRuleContext {
		public TerminalNode ECHOSTATEMENT() { return getToken(BatchParser.ECHOSTATEMENT, 0); }
		public EchoStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_echoStatement; }
	}

	public final EchoStatementContext echoStatement() throws RecognitionException {
		EchoStatementContext _localctx = new EchoStatementContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_echoStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(252);
			match(ECHOSTATEMENT);
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
	public static class RemStatementContext extends ParserRuleContext {
		public TerminalNode REMSTATEMENT() { return getToken(BatchParser.REMSTATEMENT, 0); }
		public RemStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_remStatement; }
	}

	public final RemStatementContext remStatement() throws RecognitionException {
		RemStatementContext _localctx = new RemStatementContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_remStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(254);
			match(REMSTATEMENT);
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
	public static class BsortexStatementContext extends ParserRuleContext {
		public TerminalNode BSORTEX() { return getToken(BatchParser.BSORTEX, 0); }
		public SortParametersContext sortParameters() {
			return getRuleContext(SortParametersContext.class,0);
		}
		public InputParametersContext inputParameters() {
			return getRuleContext(InputParametersContext.class,0);
		}
		public RecordParametersContext recordParameters() {
			return getRuleContext(RecordParametersContext.class,0);
		}
		public OptionParametersContext optionParameters() {
			return getRuleContext(OptionParametersContext.class,0);
		}
		public OutputParametersContext outputParameters() {
			return getRuleContext(OutputParametersContext.class,0);
		}
		public BsortexStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bsortexStatement; }
	}

	public final BsortexStatementContext bsortexStatement() throws RecognitionException {
		BsortexStatementContext _localctx = new BsortexStatementContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_bsortexStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(256);
			match(BSORTEX);
			setState(257);
			sortParameters();
			setState(258);
			inputParameters();
			setState(259);
			recordParameters();
			setState(260);
			optionParameters();
			setState(261);
			outputParameters();
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
	public static class SortParametersContext extends ParserRuleContext {
		public TerminalNode DASH_SORT() { return getToken(BatchParser.DASH_SORT, 0); }
		public List<SortParameterContext> sortParameter() {
			return getRuleContexts(SortParameterContext.class);
		}
		public SortParameterContext sortParameter(int i) {
			return getRuleContext(SortParameterContext.class,i);
		}
		public SortParametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sortParameters; }
	}

	public final SortParametersContext sortParameters() throws RecognitionException {
		SortParametersContext _localctx = new SortParametersContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_sortParameters);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(263);
			match(DASH_SORT);
			setState(265); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(264);
				sortParameter();
				}
				}
				setState(267); 
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
	public static class SortParameterContext extends ParserRuleContext {
		public VariableNameContext variableName() {
			return getRuleContext(VariableNameContext.class,0);
		}
		public TerminalNode EQUAL() { return getToken(BatchParser.EQUAL, 0); }
		public SortValueContext sortValue() {
			return getRuleContext(SortValueContext.class,0);
		}
		public SortParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sortParameter; }
	}

	public final SortParameterContext sortParameter() throws RecognitionException {
		SortParameterContext _localctx = new SortParameterContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_sortParameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(269);
			variableName();
			setState(270);
			match(EQUAL);
			setState(271);
			sortValue();
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
	public static class SortValueContext extends ParserRuleContext {
		public List<TerminalNode> INT() { return getTokens(BatchParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(BatchParser.INT, i);
		}
		public List<TerminalNode> DOT() { return getTokens(BatchParser.DOT); }
		public TerminalNode DOT(int i) {
			return getToken(BatchParser.DOT, i);
		}
		public List<TerminalNode> IDENTIFIER() { return getTokens(BatchParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(BatchParser.IDENTIFIER, i);
		}
		public SortValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sortValue; }
	}

	public final SortValueContext sortValue() throws RecognitionException {
		SortValueContext _localctx = new SortValueContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_sortValue);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(274); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(273);
					_la = _input.LA(1);
					if ( !(_la==INT || _la==DOT || _la==IDENTIFIER) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(276); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
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
	public static class InputParametersContext extends ParserRuleContext {
		public TerminalNode DASH_INPUT() { return getToken(BatchParser.DASH_INPUT, 0); }
		public List<InputParameterContext> inputParameter() {
			return getRuleContexts(InputParameterContext.class);
		}
		public InputParameterContext inputParameter(int i) {
			return getRuleContext(InputParameterContext.class,i);
		}
		public InputParametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_inputParameters; }
	}

	public final InputParametersContext inputParameters() throws RecognitionException {
		InputParametersContext _localctx = new InputParametersContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_inputParameters);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(278);
			match(DASH_INPUT);
			setState(280); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(279);
				inputParameter();
				}
				}
				setState(282); 
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
	public static class InputParameterContext extends ParserRuleContext {
		public VariableNameContext variableName() {
			return getRuleContext(VariableNameContext.class,0);
		}
		public AssignmentPartContext assignmentPart() {
			return getRuleContext(AssignmentPartContext.class,0);
		}
		public InputParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_inputParameter; }
	}

	public final InputParameterContext inputParameter() throws RecognitionException {
		InputParameterContext _localctx = new InputParameterContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_inputParameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(284);
			variableName();
			setState(285);
			assignmentPart();
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
	public static class RecordParametersContext extends ParserRuleContext {
		public TerminalNode DASH_RECORD() { return getToken(BatchParser.DASH_RECORD, 0); }
		public List<RecordParameterContext> recordParameter() {
			return getRuleContexts(RecordParameterContext.class);
		}
		public RecordParameterContext recordParameter(int i) {
			return getRuleContext(RecordParameterContext.class,i);
		}
		public RecordParametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_recordParameters; }
	}

	public final RecordParametersContext recordParameters() throws RecognitionException {
		RecordParametersContext _localctx = new RecordParametersContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_recordParameters);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(287);
			match(DASH_RECORD);
			setState(289); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(288);
				recordParameter();
				}
				}
				setState(291); 
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
	public static class RecordParameterContext extends ParserRuleContext {
		public VariableNameContext variableName() {
			return getRuleContext(VariableNameContext.class,0);
		}
		public AssignmentPartContext assignmentPart() {
			return getRuleContext(AssignmentPartContext.class,0);
		}
		public RecordParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_recordParameter; }
	}

	public final RecordParameterContext recordParameter() throws RecognitionException {
		RecordParameterContext _localctx = new RecordParameterContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_recordParameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(293);
			variableName();
			setState(294);
			assignmentPart();
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
	public static class OptionParametersContext extends ParserRuleContext {
		public TerminalNode DASH_OPTION() { return getToken(BatchParser.DASH_OPTION, 0); }
		public List<OptionParameterContext> optionParameter() {
			return getRuleContexts(OptionParameterContext.class);
		}
		public OptionParameterContext optionParameter(int i) {
			return getRuleContext(OptionParameterContext.class,i);
		}
		public OptionParametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_optionParameters; }
	}

	public final OptionParametersContext optionParameters() throws RecognitionException {
		OptionParametersContext _localctx = new OptionParametersContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_optionParameters);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(296);
			match(DASH_OPTION);
			setState(298); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(297);
				optionParameter();
				}
				}
				setState(300); 
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
	public static class OptionParameterContext extends ParserRuleContext {
		public VariableNameContext variableName() {
			return getRuleContext(VariableNameContext.class,0);
		}
		public AssignmentPartContext assignmentPart() {
			return getRuleContext(AssignmentPartContext.class,0);
		}
		public OptionParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_optionParameter; }
	}

	public final OptionParameterContext optionParameter() throws RecognitionException {
		OptionParameterContext _localctx = new OptionParameterContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_optionParameter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(302);
			variableName();
			setState(304);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==EQUAL || _la==SLASH || ((((_la - 91)) & ~0x3f) == 0 && ((1L << (_la - 91)) & 193L) != 0)) {
				{
				setState(303);
				assignmentPart();
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
	public static class OutputParametersContext extends ParserRuleContext {
		public TerminalNode DASH_OUTPUT() { return getToken(BatchParser.DASH_OUTPUT, 0); }
		public List<OutputParameterContext> outputParameter() {
			return getRuleContexts(OutputParameterContext.class);
		}
		public OutputParameterContext outputParameter(int i) {
			return getRuleContext(OutputParameterContext.class,i);
		}
		public OutputParametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_outputParameters; }
	}

	public final OutputParametersContext outputParameters() throws RecognitionException {
		OutputParametersContext _localctx = new OutputParametersContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_outputParameters);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(306);
			match(DASH_OUTPUT);
			setState(308); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(307);
					outputParameter();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(310); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
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
	public static class OutputParameterContext extends ParserRuleContext {
		public VariableNameContext variableName() {
			return getRuleContext(VariableNameContext.class,0);
		}
		public TerminalNode EQUAL() { return getToken(BatchParser.EQUAL, 0); }
		public OutputValueContext outputValue() {
			return getRuleContext(OutputValueContext.class,0);
		}
		public OutputParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_outputParameter; }
	}

	public final OutputParameterContext outputParameter() throws RecognitionException {
		OutputParameterContext _localctx = new OutputParameterContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_outputParameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(312);
			variableName();
			setState(313);
			match(EQUAL);
			setState(314);
			outputValue();
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
	public static class OutputValueContext extends ParserRuleContext {
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public ReferencedVariableContext referencedVariable() {
			return getRuleContext(ReferencedVariableContext.class,0);
		}
		public TerminalNode LPAREN() { return getToken(BatchParser.LPAREN, 0); }
		public TerminalNode STRING() { return getToken(BatchParser.STRING, 0); }
		public TerminalNode RPAREN() { return getToken(BatchParser.RPAREN, 0); }
		public OutputValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_outputValue; }
	}

	public final OutputValueContext outputValue() throws RecognitionException {
		OutputValueContext _localctx = new OutputValueContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_outputValue);
		try {
			setState(321);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(316);
				value();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(317);
				referencedVariable();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(318);
				match(LPAREN);
				setState(319);
				match(STRING);
				setState(320);
				match(RPAREN);
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
	public static class CallStatementContext extends ParserRuleContext {
		public TerminalNode CALL() { return getToken(BatchParser.CALL, 0); }
		public CallWithLabelContext callWithLabel() {
			return getRuleContext(CallWithLabelContext.class,0);
		}
		public CallWithFilePathContext callWithFilePath() {
			return getRuleContext(CallWithFilePathContext.class,0);
		}
		public CallStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_callStatement; }
	}

	public final CallStatementContext callStatement() throws RecognitionException {
		CallStatementContext _localctx = new CallStatementContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_callStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(323);
			match(CALL);
			setState(326);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COLON:
				{
				setState(324);
				callWithLabel();
				}
				break;
			case QUESTION:
			case SSLASH:
			case DOT:
			case DISK_ADDRESS:
			case EXE:
			case PERCENT:
			case EXCLAMATION:
			case UNDERSCORE:
			case COMMA:
			case STAR:
			case JP_TXT:
			case IDENTIFIER:
				{
				setState(325);
				callWithFilePath();
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
	public static class CallWithLabelContext extends ParserRuleContext {
		public LabelNameContext labelName() {
			return getRuleContext(LabelNameContext.class,0);
		}
		public CallWithLabelContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_callWithLabel; }
	}

	public final CallWithLabelContext callWithLabel() throws RecognitionException {
		CallWithLabelContext _localctx = new CallWithLabelContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_callWithLabel);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(328);
			labelName();
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
	public static class CallWithFilePathContext extends ParserRuleContext {
		public List<FilePathContext> filePath() {
			return getRuleContexts(FilePathContext.class);
		}
		public FilePathContext filePath(int i) {
			return getRuleContext(FilePathContext.class,i);
		}
		public List<FileNameContext> fileName() {
			return getRuleContexts(FileNameContext.class);
		}
		public FileNameContext fileName(int i) {
			return getRuleContext(FileNameContext.class,i);
		}
		public ConditionParameterContext conditionParameter() {
			return getRuleContext(ConditionParameterContext.class,0);
		}
		public BatchParametersContext batchParameters() {
			return getRuleContext(BatchParametersContext.class,0);
		}
		public CallWithFilePathContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_callWithFilePath; }
	}

	public final CallWithFilePathContext callWithFilePath() throws RecognitionException {
		CallWithFilePathContext _localctx = new CallWithFilePathContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_callWithFilePath);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(332); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					setState(332);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
					case 1:
						{
						setState(330);
						filePath();
						}
						break;
					case 2:
						{
						setState(331);
						fileName();
						}
						break;
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(334); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			setState(337);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COND_COLON) {
				{
				setState(336);
				conditionParameter();
				}
			}

			setState(340);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				{
				setState(339);
				batchParameters();
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
	public static class BatchParametersContext extends ParserRuleContext {
		public List<BatchParameterContext> batchParameter() {
			return getRuleContexts(BatchParameterContext.class);
		}
		public BatchParameterContext batchParameter(int i) {
			return getRuleContext(BatchParameterContext.class,i);
		}
		public BatchParametersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_batchParameters; }
	}

	public final BatchParametersContext batchParameters() throws RecognitionException {
		BatchParametersContext _localctx = new BatchParametersContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_batchParameters);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(343); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(342);
					batchParameter();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(345); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
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
	public static class BatchParameterContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(BatchParser.IDENTIFIER, 0); }
		public TerminalNode STRING() { return getToken(BatchParser.STRING, 0); }
		public TerminalNode PERCENT() { return getToken(BatchParser.PERCENT, 0); }
		public TerminalNode INT() { return getToken(BatchParser.INT, 0); }
		public ReferencedVariableContext referencedVariable() {
			return getRuleContext(ReferencedVariableContext.class,0);
		}
		public ForVariableContext forVariable() {
			return getRuleContext(ForVariableContext.class,0);
		}
		public BatchParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_batchParameter; }
	}

	public final BatchParameterContext batchParameter() throws RecognitionException {
		BatchParameterContext _localctx = new BatchParameterContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_batchParameter);
		try {
			setState(353);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(347);
				match(IDENTIFIER);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(348);
				match(STRING);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(349);
				match(PERCENT);
				setState(350);
				match(INT);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(351);
				referencedVariable();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(352);
				forVariable();
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
	public static class ConditionParameterContext extends ParserRuleContext {
		public TerminalNode COND_COLON() { return getToken(BatchParser.COND_COLON, 0); }
		public List<TerminalNode> INT() { return getTokens(BatchParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(BatchParser.INT, i);
		}
		public TerminalNode SLASH() { return getToken(BatchParser.SLASH, 0); }
		public ConditionParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conditionParameter; }
	}

	public final ConditionParameterContext conditionParameter() throws RecognitionException {
		ConditionParameterContext _localctx = new ConditionParameterContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_conditionParameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(355);
			match(COND_COLON);
			setState(356);
			match(INT);
			setState(357);
			match(SLASH);
			setState(358);
			match(INT);
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
	public static class DelStatementContext extends ParserRuleContext {
		public TerminalNode DEL() { return getToken(BatchParser.DEL, 0); }
		public FilePathContext filePath() {
			return getRuleContext(FilePathContext.class,0);
		}
		public DelStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_delStatement; }
	}

	public final DelStatementContext delStatement() throws RecognitionException {
		DelStatementContext _localctx = new DelStatementContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_delStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(360);
			match(DEL);
			setState(361);
			filePath();
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
	public static class EndlocalStatementContext extends ParserRuleContext {
		public TerminalNode ENDLOCAL() { return getToken(BatchParser.ENDLOCAL, 0); }
		public EndlocalStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_endlocalStatement; }
	}

	public final EndlocalStatementContext endlocalStatement() throws RecognitionException {
		EndlocalStatementContext _localctx = new EndlocalStatementContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_endlocalStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(363);
			match(ENDLOCAL);
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
	public static class ExecStatementContext extends ParserRuleContext {
		public ExecFileContext execFile() {
			return getRuleContext(ExecFileContext.class,0);
		}
		public SwitchesContext switches() {
			return getRuleContext(SwitchesContext.class,0);
		}
		public List<ExecParameterContext> execParameter() {
			return getRuleContexts(ExecParameterContext.class);
		}
		public ExecParameterContext execParameter(int i) {
			return getRuleContext(ExecParameterContext.class,i);
		}
		public ExecStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_execStatement; }
	}

	public final ExecStatementContext execStatement() throws RecognitionException {
		ExecStatementContext _localctx = new ExecStatementContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_execStatement);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(365);
			execFile();
			setState(367);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 9223372002495037440L) != 0)) {
				{
				setState(366);
				switches();
				}
			}

			setState(372);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(369);
					execParameter();
					}
					} 
				}
				setState(374);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
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
	public static class ExecFileContext extends ParserRuleContext {
		public TerminalNode EXE_FILE() { return getToken(BatchParser.EXE_FILE, 0); }
		public ExecFileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_execFile; }
	}

	public final ExecFileContext execFile() throws RecognitionException {
		ExecFileContext _localctx = new ExecFileContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_execFile);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(375);
			match(EXE_FILE);
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
	public static class ExecParameterContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(BatchParser.INT, 0); }
		public ReferencedVariableContext referencedVariable() {
			return getRuleContext(ReferencedVariableContext.class,0);
		}
		public TerminalNode IDENTIFIER() { return getToken(BatchParser.IDENTIFIER, 0); }
		public FilePathContext filePath() {
			return getRuleContext(FilePathContext.class,0);
		}
		public TerminalNode STRING() { return getToken(BatchParser.STRING, 0); }
		public ConcatenateStringContext concatenateString() {
			return getRuleContext(ConcatenateStringContext.class,0);
		}
		public ConcatenateFileContentContext concatenateFileContent() {
			return getRuleContext(ConcatenateFileContentContext.class,0);
		}
		public ForVariableContext forVariable() {
			return getRuleContext(ForVariableContext.class,0);
		}
		public ExecParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_execParameter; }
	}

	public final ExecParameterContext execParameter() throws RecognitionException {
		ExecParameterContext _localctx = new ExecParameterContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_execParameter);
		try {
			setState(385);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,23,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(377);
				match(INT);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(378);
				referencedVariable();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(379);
				match(IDENTIFIER);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(380);
				filePath();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(381);
				match(STRING);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(382);
				concatenateString();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(383);
				concatenateFileContent();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(384);
				forVariable();
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
	public static class ConcatenateFileContentContext extends ParserRuleContext {
		public TerminalNode PLUS() { return getToken(BatchParser.PLUS, 0); }
		public List<FilePathContext> filePath() {
			return getRuleContexts(FilePathContext.class);
		}
		public FilePathContext filePath(int i) {
			return getRuleContext(FilePathContext.class,i);
		}
		public List<ReferencedVariableContext> referencedVariable() {
			return getRuleContexts(ReferencedVariableContext.class);
		}
		public ReferencedVariableContext referencedVariable(int i) {
			return getRuleContext(ReferencedVariableContext.class,i);
		}
		public ConcatenateFileContentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_concatenateFileContent; }
	}

	public final ConcatenateFileContentContext concatenateFileContent() throws RecognitionException {
		ConcatenateFileContentContext _localctx = new ConcatenateFileContentContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_concatenateFileContent);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(389);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				{
				setState(387);
				filePath();
				}
				break;
			case 2:
				{
				setState(388);
				referencedVariable();
				}
				break;
			}
			setState(391);
			match(PLUS);
			setState(394);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,25,_ctx) ) {
			case 1:
				{
				setState(392);
				filePath();
				}
				break;
			case 2:
				{
				setState(393);
				referencedVariable();
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
	public static class ExitStatementContext extends ParserRuleContext {
		public TerminalNode EXIT() { return getToken(BatchParser.EXIT, 0); }
		public ExitCurrentBatchContext exitCurrentBatch() {
			return getRuleContext(ExitCurrentBatchContext.class,0);
		}
		public ExitCodeContext exitCode() {
			return getRuleContext(ExitCodeContext.class,0);
		}
		public ExitStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exitStatement; }
	}

	public final ExitStatementContext exitStatement() throws RecognitionException {
		ExitStatementContext _localctx = new ExitStatementContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_exitStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(396);
			match(EXIT);
			setState(398);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SLASH_B) {
				{
				setState(397);
				exitCurrentBatch();
				}
			}

			setState(401);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
			case 1:
				{
				setState(400);
				exitCode();
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
	public static class ExitCurrentBatchContext extends ParserRuleContext {
		public TerminalNode SLASH_B() { return getToken(BatchParser.SLASH_B, 0); }
		public ExitCurrentBatchContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exitCurrentBatch; }
	}

	public final ExitCurrentBatchContext exitCurrentBatch() throws RecognitionException {
		ExitCurrentBatchContext _localctx = new ExitCurrentBatchContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_exitCurrentBatch);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(403);
			match(SLASH_B);
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
	public static class ExitCodeContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(BatchParser.INT, 0); }
		public ReferencedVariableContext referencedVariable() {
			return getRuleContext(ReferencedVariableContext.class,0);
		}
		public ExitCodeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exitCode; }
	}

	public final ExitCodeContext exitCode() throws RecognitionException {
		ExitCodeContext _localctx = new ExitCodeContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_exitCode);
		try {
			setState(407);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				enterOuterAlt(_localctx, 1);
				{
				setState(405);
				match(INT);
				}
				break;
			case PERCENT:
			case EXCLAMATION:
				enterOuterAlt(_localctx, 2);
				{
				setState(406);
				referencedVariable();
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
	public static class ForStatementContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(BatchParser.FOR, 0); }
		public TerminalNode IN() { return getToken(BatchParser.IN, 0); }
		public TerminalNode DO() { return getToken(BatchParser.DO, 0); }
		public ForVariableContext forVariable() {
			return getRuleContext(ForVariableContext.class,0);
		}
		public ForValuesContext forValues() {
			return getRuleContext(ForValuesContext.class,0);
		}
		public ForDoContext forDo() {
			return getRuleContext(ForDoContext.class,0);
		}
		public SwitchesContext switches() {
			return getRuleContext(SwitchesContext.class,0);
		}
		public ConfigurationStringContext configurationString() {
			return getRuleContext(ConfigurationStringContext.class,0);
		}
		public ForStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forStatement; }
	}

	public final ForStatementContext forStatement() throws RecognitionException {
		ForStatementContext _localctx = new ForStatementContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_forStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(409);
			match(FOR);
			setState(411);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 9223372002495037440L) != 0)) {
				{
				setState(410);
				switches();
				}
			}

			setState(414);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==STRING) {
				{
				setState(413);
				configurationString();
				}
			}

			{
			setState(416);
			forVariable();
			}
			setState(417);
			match(IN);
			{
			setState(418);
			forValues();
			}
			setState(419);
			match(DO);
			{
			setState(420);
			forDo();
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
	public static class ConfigurationStringContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(BatchParser.STRING, 0); }
		public ConfigurationStringContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_configurationString; }
	}

	public final ConfigurationStringContext configurationString() throws RecognitionException {
		ConfigurationStringContext _localctx = new ConfigurationStringContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_configurationString);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(422);
			match(STRING);
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
	public static class ForValuesContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(BatchParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(BatchParser.RPAREN, 0); }
		public List<ForValueContext> forValue() {
			return getRuleContexts(ForValueContext.class);
		}
		public ForValueContext forValue(int i) {
			return getRuleContext(ForValueContext.class,i);
		}
		public ForValuesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forValues; }
	}

	public final ForValuesContext forValues() throws RecognitionException {
		ForValuesContext _localctx = new ForValuesContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_forValues);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(424);
			match(LPAREN);
			setState(426); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(425);
				forValue();
				}
				}
				setState(428); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & -9223372036829609724L) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & 96774127745L) != 0) );
			setState(430);
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
	public static class ForValueContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(BatchParser.INT, 0); }
		public TerminalNode STRING() { return getToken(BatchParser.STRING, 0); }
		public FilePathContext filePath() {
			return getRuleContext(FilePathContext.class,0);
		}
		public FileNameContext fileName() {
			return getRuleContext(FileNameContext.class,0);
		}
		public ReferencedVariableContext referencedVariable() {
			return getRuleContext(ReferencedVariableContext.class,0);
		}
		public ForVariableContext forVariable() {
			return getRuleContext(ForVariableContext.class,0);
		}
		public ForValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forValue; }
	}

	public final ForValueContext forValue() throws RecognitionException {
		ForValueContext _localctx = new ForValueContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_forValue);
		try {
			setState(438);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,32,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(432);
				match(INT);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(433);
				match(STRING);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(434);
				filePath();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(435);
				fileName();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(436);
				referencedVariable();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(437);
				forVariable();
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
	public static class ForVariableContext extends ParserRuleContext {
		public List<TerminalNode> PERCENT() { return getTokens(BatchParser.PERCENT); }
		public TerminalNode PERCENT(int i) {
			return getToken(BatchParser.PERCENT, i);
		}
		public TerminalNode IDENTIFIER() { return getToken(BatchParser.IDENTIFIER, 0); }
		public ForVariableModifierContext forVariableModifier() {
			return getRuleContext(ForVariableModifierContext.class,0);
		}
		public ForVariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forVariable; }
	}

	public final ForVariableContext forVariable() throws RecognitionException {
		ForVariableContext _localctx = new ForVariableContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_forVariable);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(440);
			match(PERCENT);
			setState(441);
			match(PERCENT);
			setState(443);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==TILDE_NX) {
				{
				setState(442);
				forVariableModifier();
				}
			}

			setState(445);
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
	public static class ForVariableModifierContext extends ParserRuleContext {
		public TerminalNode TILDE_NX() { return getToken(BatchParser.TILDE_NX, 0); }
		public ForVariableModifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forVariableModifier; }
	}

	public final ForVariableModifierContext forVariableModifier() throws RecognitionException {
		ForVariableModifierContext _localctx = new ForVariableModifierContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_forVariableModifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(447);
			match(TILDE_NX);
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
	public static class ForDoContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(BatchParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(BatchParser.RPAREN, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ForDoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forDo; }
	}

	public final ForDoContext forDo() throws RecognitionException {
		ForDoContext _localctx = new ForDoContext(_ctx, getState());
		enterRule(_localctx, 88, RULE_forDo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(449);
			match(LPAREN);
			setState(451); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(450);
				statement();
				}
				}
				setState(453); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & -9223372036829511624L) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & 96803721103L) != 0) );
			setState(455);
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
	public static class GotoStatementContext extends ParserRuleContext {
		public TerminalNode GOTO() { return getToken(BatchParser.GOTO, 0); }
		public LabelNameContext labelName() {
			return getRuleContext(LabelNameContext.class,0);
		}
		public TerminalNode IDENTIFIER() { return getToken(BatchParser.IDENTIFIER, 0); }
		public GotoStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_gotoStatement; }
	}

	public final GotoStatementContext gotoStatement() throws RecognitionException {
		GotoStatementContext _localctx = new GotoStatementContext(_ctx, getState());
		enterRule(_localctx, 90, RULE_gotoStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(457);
			match(GOTO);
			setState(460);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,35,_ctx) ) {
			case 1:
				{
				setState(458);
				labelName();
				}
				break;
			case 2:
				{
				setState(459);
				match(IDENTIFIER);
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
	public static class IfStatementContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(BatchParser.IF, 0); }
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public IfThenContext ifThen() {
			return getRuleContext(IfThenContext.class,0);
		}
		public IfElseContext ifElse() {
			return getRuleContext(IfElseContext.class,0);
		}
		public IfStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStatement; }
	}

	public final IfStatementContext ifStatement() throws RecognitionException {
		IfStatementContext _localctx = new IfStatementContext(_ctx, getState());
		enterRule(_localctx, 92, RULE_ifStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(462);
			match(IF);
			setState(463);
			condition();
			setState(464);
			ifThen();
			setState(466);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,36,_ctx) ) {
			case 1:
				{
				setState(465);
				ifElse();
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
	public static class IfThenContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(BatchParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(BatchParser.RPAREN, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public IfThenContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifThen; }
	}

	public final IfThenContext ifThen() throws RecognitionException {
		IfThenContext _localctx = new IfThenContext(_ctx, getState());
		enterRule(_localctx, 94, RULE_ifThen);
		int _la;
		try {
			setState(477);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LPAREN:
				enterOuterAlt(_localctx, 1);
				{
				setState(468);
				match(LPAREN);
				setState(470); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(469);
					statement();
					}
					}
					setState(472); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & -9223372036829511624L) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & 96803721103L) != 0) );
				setState(474);
				match(RPAREN);
				}
				break;
			case ECHOSTATEMENT:
			case REMSTATEMENT:
			case EXE_FILE:
			case SET:
			case SETLOCAL:
			case QUESTION:
			case SSLASH:
			case DOT:
			case DISK_ADDRESS:
			case BSORTEX:
			case CALL:
			case DEL:
			case EXE:
			case ENDLOCAL:
			case EXIT:
			case IF:
			case GOTO:
			case PAUSE:
			case RMDIR:
			case FOR:
			case PERCENT:
			case EXCLAMATION:
			case MKDIR:
			case XCOPY:
			case TYPE:
			case UNDERSCORE:
			case COMMA:
			case STAR:
			case JP_TXT:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 2);
				{
				setState(476);
				statement();
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
	public static class IfElseContext extends ParserRuleContext {
		public TerminalNode ELSE() { return getToken(BatchParser.ELSE, 0); }
		public TerminalNode LPAREN() { return getToken(BatchParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(BatchParser.RPAREN, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public IfElseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifElse; }
	}

	public final IfElseContext ifElse() throws RecognitionException {
		IfElseContext _localctx = new IfElseContext(_ctx, getState());
		enterRule(_localctx, 96, RULE_ifElse);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(479);
			match(ELSE);
			setState(480);
			match(LPAREN);
			setState(482); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(481);
				statement();
				}
				}
				setState(484); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & -9223372036829511624L) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & 96803721103L) != 0) );
			setState(486);
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
	public static class SimpleIfContext extends ParserRuleContext {
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public SimpleIfContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_simpleIf; }
	}

	public final SimpleIfContext simpleIf() throws RecognitionException {
		SimpleIfContext _localctx = new SimpleIfContext(_ctx, getState());
		enterRule(_localctx, 98, RULE_simpleIf);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(488);
			statement();
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
	public static class ConditionContext extends ParserRuleContext {
		public RelationalOperatorContext relationalOperator() {
			return getRuleContext(RelationalOperatorContext.class,0);
		}
		public RightConditionOperatorContext rightConditionOperator() {
			return getRuleContext(RightConditionOperatorContext.class,0);
		}
		public LeftConditionOperatorContext leftConditionOperator() {
			return getRuleContext(LeftConditionOperatorContext.class,0);
		}
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 100, RULE_condition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(491);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==STRING || ((((_la - 85)) & ~0x3f) == 0 && ((1L << (_la - 85)) & 65539L) != 0)) {
				{
				setState(490);
				leftConditionOperator();
				}
			}

			setState(493);
			relationalOperator();
			setState(494);
			rightConditionOperator();
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
	public static class LeftConditionOperatorContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(BatchParser.STRING, 0); }
		public ReferencedVariableContext referencedVariable() {
			return getRuleContext(ReferencedVariableContext.class,0);
		}
		public TerminalNode IDENTIFIER() { return getToken(BatchParser.IDENTIFIER, 0); }
		public LeftConditionOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_leftConditionOperator; }
	}

	public final LeftConditionOperatorContext leftConditionOperator() throws RecognitionException {
		LeftConditionOperatorContext _localctx = new LeftConditionOperatorContext(_ctx, getState());
		enterRule(_localctx, 102, RULE_leftConditionOperator);
		try {
			setState(499);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case STRING:
				enterOuterAlt(_localctx, 1);
				{
				setState(496);
				match(STRING);
				}
				break;
			case PERCENT:
			case EXCLAMATION:
				enterOuterAlt(_localctx, 2);
				{
				setState(497);
				referencedVariable();
				}
				break;
			case IDENTIFIER:
				enterOuterAlt(_localctx, 3);
				{
				setState(498);
				match(IDENTIFIER);
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
	public static class RightConditionOperatorContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(BatchParser.STRING, 0); }
		public TerminalNode INT() { return getToken(BatchParser.INT, 0); }
		public TerminalNode IDENTIFIER() { return getToken(BatchParser.IDENTIFIER, 0); }
		public ReferencedVariableContext referencedVariable() {
			return getRuleContext(ReferencedVariableContext.class,0);
		}
		public RightConditionOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rightConditionOperator; }
	}

	public final RightConditionOperatorContext rightConditionOperator() throws RecognitionException {
		RightConditionOperatorContext _localctx = new RightConditionOperatorContext(_ctx, getState());
		enterRule(_localctx, 104, RULE_rightConditionOperator);
		try {
			setState(505);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case STRING:
				enterOuterAlt(_localctx, 1);
				{
				setState(501);
				match(STRING);
				}
				break;
			case INT:
				enterOuterAlt(_localctx, 2);
				{
				setState(502);
				match(INT);
				}
				break;
			case IDENTIFIER:
				enterOuterAlt(_localctx, 3);
				{
				setState(503);
				match(IDENTIFIER);
				}
				break;
			case PERCENT:
			case EXCLAMATION:
				enterOuterAlt(_localctx, 4);
				{
				setState(504);
				referencedVariable();
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
	public static class RelationalOperatorContext extends ParserRuleContext {
		public TerminalNode EQU() { return getToken(BatchParser.EQU, 0); }
		public TerminalNode NEQ() { return getToken(BatchParser.NEQ, 0); }
		public TerminalNode EXIST() { return getToken(BatchParser.EXIST, 0); }
		public TerminalNode GTR() { return getToken(BatchParser.GTR, 0); }
		public RelationalOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relationalOperator; }
	}

	public final RelationalOperatorContext relationalOperator() throws RecognitionException {
		RelationalOperatorContext _localctx = new RelationalOperatorContext(_ctx, getState());
		enterRule(_localctx, 106, RULE_relationalOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(507);
			_la = _input.LA(1);
			if ( !(((((_la - 70)) & ~0x3f) == 0 && ((1L << (_la - 70)) & 643L) != 0)) ) {
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
	public static class MkdirStatementContext extends ParserRuleContext {
		public TerminalNode MKDIR() { return getToken(BatchParser.MKDIR, 0); }
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public MkdirStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mkdirStatement; }
	}

	public final MkdirStatementContext mkdirStatement() throws RecognitionException {
		MkdirStatementContext _localctx = new MkdirStatementContext(_ctx, getState());
		enterRule(_localctx, 108, RULE_mkdirStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(509);
			match(MKDIR);
			setState(510);
			value();
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
	public static class SetLocalStatementContext extends ParserRuleContext {
		public TerminalNode SETLOCAL() { return getToken(BatchParser.SETLOCAL, 0); }
		public SetLocalOptionContext setLocalOption() {
			return getRuleContext(SetLocalOptionContext.class,0);
		}
		public SetLocalStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_setLocalStatement; }
	}

	public final SetLocalStatementContext setLocalStatement() throws RecognitionException {
		SetLocalStatementContext _localctx = new SetLocalStatementContext(_ctx, getState());
		enterRule(_localctx, 110, RULE_setLocalStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(512);
			match(SETLOCAL);
			setState(513);
			setLocalOption();
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
	public static class TypeStatementContext extends ParserRuleContext {
		public TerminalNode TYPE() { return getToken(BatchParser.TYPE, 0); }
		public FilePathContext filePath() {
			return getRuleContext(FilePathContext.class,0);
		}
		public FileNameContext fileName() {
			return getRuleContext(FileNameContext.class,0);
		}
		public TypeStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeStatement; }
	}

	public final TypeStatementContext typeStatement() throws RecognitionException {
		TypeStatementContext _localctx = new TypeStatementContext(_ctx, getState());
		enterRule(_localctx, 112, RULE_typeStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(515);
			match(TYPE);
			setState(518);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,43,_ctx) ) {
			case 1:
				{
				setState(516);
				filePath();
				}
				break;
			case 2:
				{
				setState(517);
				fileName();
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
	public static class RmdirStatementContext extends ParserRuleContext {
		public TerminalNode RMDIR() { return getToken(BatchParser.RMDIR, 0); }
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public SwitchesContext switches() {
			return getRuleContext(SwitchesContext.class,0);
		}
		public RmdirStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rmdirStatement; }
	}

	public final RmdirStatementContext rmdirStatement() throws RecognitionException {
		RmdirStatementContext _localctx = new RmdirStatementContext(_ctx, getState());
		enterRule(_localctx, 114, RULE_rmdirStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(520);
			match(RMDIR);
			setState(522);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 9223372002495037440L) != 0)) {
				{
				setState(521);
				switches();
				}
			}

			setState(524);
			value();
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
	public static class XcopyStatementContext extends ParserRuleContext {
		public TerminalNode XCOPY() { return getToken(BatchParser.XCOPY, 0); }
		public XCopySourceContext xCopySource() {
			return getRuleContext(XCopySourceContext.class,0);
		}
		public XCopyDestinationContext xCopyDestination() {
			return getRuleContext(XCopyDestinationContext.class,0);
		}
		public SwitchesContext switches() {
			return getRuleContext(SwitchesContext.class,0);
		}
		public XcopyStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_xcopyStatement; }
	}

	public final XcopyStatementContext xcopyStatement() throws RecognitionException {
		XcopyStatementContext _localctx = new XcopyStatementContext(_ctx, getState());
		enterRule(_localctx, 116, RULE_xcopyStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(526);
			match(XCOPY);
			setState(527);
			xCopySource();
			setState(528);
			xCopyDestination();
			setState(530);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 9223372002495037440L) != 0)) {
				{
				setState(529);
				switches();
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
	public static class XCopySourceContext extends ParserRuleContext {
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public XCopySourceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_xCopySource; }
	}

	public final XCopySourceContext xCopySource() throws RecognitionException {
		XCopySourceContext _localctx = new XCopySourceContext(_ctx, getState());
		enterRule(_localctx, 118, RULE_xCopySource);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(532);
			value();
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
	public static class XCopyDestinationContext extends ParserRuleContext {
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public XCopyDestinationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_xCopyDestination; }
	}

	public final XCopyDestinationContext xCopyDestination() throws RecognitionException {
		XCopyDestinationContext _localctx = new XCopyDestinationContext(_ctx, getState());
		enterRule(_localctx, 120, RULE_xCopyDestination);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(534);
			value();
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
	public static class SwitchesContext extends ParserRuleContext {
		public List<SwitchContext> switch_() {
			return getRuleContexts(SwitchContext.class);
		}
		public SwitchContext switch_(int i) {
			return getRuleContext(SwitchContext.class,i);
		}
		public SwitchesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_switches; }
	}

	public final SwitchesContext switches() throws RecognitionException {
		SwitchesContext _localctx = new SwitchesContext(_ctx, getState());
		enterRule(_localctx, 122, RULE_switches);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(537); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(536);
				switch_();
				}
				}
				setState(539); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 9223372002495037440L) != 0) );
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
	public static class SwitchContext extends ParserRuleContext {
		public TerminalNode SLASH_W() { return getToken(BatchParser.SLASH_W, 0); }
		public TerminalNode SLASH_C() { return getToken(BatchParser.SLASH_C, 0); }
		public TerminalNode SLASH_V() { return getToken(BatchParser.SLASH_V, 0); }
		public TerminalNode SLASH_P() { return getToken(BatchParser.SLASH_P, 0); }
		public TerminalNode SLASH_F() { return getToken(BatchParser.SLASH_F, 0); }
		public TerminalNode SLASH_L() { return getToken(BatchParser.SLASH_L, 0); }
		public TerminalNode SLASH_G() { return getToken(BatchParser.SLASH_G, 0); }
		public TerminalNode SLASH_D() { return getToken(BatchParser.SLASH_D, 0); }
		public TerminalNode COLON() { return getToken(BatchParser.COLON, 0); }
		public DateFormatContext dateFormat() {
			return getRuleContext(DateFormatContext.class,0);
		}
		public TerminalNode SLASH_U() { return getToken(BatchParser.SLASH_U, 0); }
		public TerminalNode SLASH_I() { return getToken(BatchParser.SLASH_I, 0); }
		public TerminalNode SLASH_S() { return getToken(BatchParser.SLASH_S, 0); }
		public TerminalNode SLASH_E() { return getToken(BatchParser.SLASH_E, 0); }
		public TerminalNode SLASH_T() { return getToken(BatchParser.SLASH_T, 0); }
		public TerminalNode SLASH_K() { return getToken(BatchParser.SLASH_K, 0); }
		public TerminalNode SLASH_R() { return getToken(BatchParser.SLASH_R, 0); }
		public TerminalNode SLASH_H() { return getToken(BatchParser.SLASH_H, 0); }
		public TerminalNode SLASH_A() { return getToken(BatchParser.SLASH_A, 0); }
		public TerminalNode SLASH_M() { return getToken(BatchParser.SLASH_M, 0); }
		public TerminalNode SLASH_N() { return getToken(BatchParser.SLASH_N, 0); }
		public TerminalNode SLASH_O() { return getToken(BatchParser.SLASH_O, 0); }
		public TerminalNode SLASH_X() { return getToken(BatchParser.SLASH_X, 0); }
		public TerminalNode SLASH_Y() { return getToken(BatchParser.SLASH_Y, 0); }
		public TerminalNode SLASH_Z() { return getToken(BatchParser.SLASH_Z, 0); }
		public TerminalNode SLASH_B() { return getToken(BatchParser.SLASH_B, 0); }
		public TerminalNode SLASH_J() { return getToken(BatchParser.SLASH_J, 0); }
		public TerminalNode SLASH_COMPRESS() { return getToken(BatchParser.SLASH_COMPRESS, 0); }
		public TerminalNode SLASH_EXCLUDE() { return getToken(BatchParser.SLASH_EXCLUDE, 0); }
		public List<FileNameContext> fileName() {
			return getRuleContexts(FileNameContext.class);
		}
		public FileNameContext fileName(int i) {
			return getRuleContext(FileNameContext.class,i);
		}
		public List<TerminalNode> PLUS() { return getTokens(BatchParser.PLUS); }
		public TerminalNode PLUS(int i) {
			return getToken(BatchParser.PLUS, i);
		}
		public TerminalNode SLASH_Q() { return getToken(BatchParser.SLASH_Q, 0); }
		public SwitchContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_switch; }
	}

	public final SwitchContext switch_() throws RecognitionException {
		SwitchContext _localctx = new SwitchContext(_ctx, getState());
		enterRule(_localctx, 124, RULE_switch);
		int _la;
		try {
			setState(584);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,48,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(541);
				match(SLASH_W);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(542);
				match(SLASH_C);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(543);
				match(SLASH_V);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(544);
				match(SLASH_P);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(545);
				match(SLASH_F);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(546);
				match(SLASH_L);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(547);
				match(SLASH_G);
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(548);
				match(SLASH_D);
				setState(549);
				match(COLON);
				setState(550);
				dateFormat();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(551);
				match(SLASH_U);
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(552);
				match(SLASH_I);
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(553);
				match(SLASH_S);
				}
				break;
			case 12:
				enterOuterAlt(_localctx, 12);
				{
				setState(554);
				match(SLASH_E);
				}
				break;
			case 13:
				enterOuterAlt(_localctx, 13);
				{
				setState(555);
				match(SLASH_T);
				}
				break;
			case 14:
				enterOuterAlt(_localctx, 14);
				{
				setState(556);
				match(SLASH_K);
				}
				break;
			case 15:
				enterOuterAlt(_localctx, 15);
				{
				setState(557);
				match(SLASH_R);
				}
				break;
			case 16:
				enterOuterAlt(_localctx, 16);
				{
				setState(558);
				match(SLASH_H);
				}
				break;
			case 17:
				enterOuterAlt(_localctx, 17);
				{
				setState(559);
				match(SLASH_A);
				}
				break;
			case 18:
				enterOuterAlt(_localctx, 18);
				{
				setState(560);
				match(SLASH_M);
				}
				break;
			case 19:
				enterOuterAlt(_localctx, 19);
				{
				setState(561);
				match(SLASH_N);
				}
				break;
			case 20:
				enterOuterAlt(_localctx, 20);
				{
				setState(562);
				match(SLASH_O);
				}
				break;
			case 21:
				enterOuterAlt(_localctx, 21);
				{
				setState(563);
				match(SLASH_X);
				}
				break;
			case 22:
				enterOuterAlt(_localctx, 22);
				{
				setState(564);
				match(SLASH_Y);
				}
				break;
			case 23:
				enterOuterAlt(_localctx, 23);
				{
				setState(565);
				match(SLASH_Z);
				}
				break;
			case 24:
				enterOuterAlt(_localctx, 24);
				{
				setState(566);
				match(SLASH_B);
				}
				break;
			case 25:
				enterOuterAlt(_localctx, 25);
				{
				setState(567);
				match(SLASH_J);
				}
				break;
			case 26:
				enterOuterAlt(_localctx, 26);
				{
				setState(568);
				match(SLASH_COMPRESS);
				}
				break;
			case 27:
				enterOuterAlt(_localctx, 27);
				{
				setState(569);
				match(SLASH_EXCLUDE);
				setState(570);
				fileName();
				setState(575);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==PLUS) {
					{
					{
					setState(571);
					match(PLUS);
					setState(572);
					fileName();
					}
					}
					setState(577);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case 28:
				enterOuterAlt(_localctx, 28);
				{
				setState(578);
				match(SLASH_Y);
				}
				break;
			case 29:
				enterOuterAlt(_localctx, 29);
				{
				setState(579);
				match(SLASH_Z);
				}
				break;
			case 30:
				enterOuterAlt(_localctx, 30);
				{
				setState(580);
				match(SLASH_B);
				}
				break;
			case 31:
				enterOuterAlt(_localctx, 31);
				{
				setState(581);
				match(SLASH_J);
				}
				break;
			case 32:
				enterOuterAlt(_localctx, 32);
				{
				setState(582);
				match(SLASH_Q);
				}
				break;
			case 33:
				enterOuterAlt(_localctx, 33);
				{
				setState(583);
				match(SLASH_COMPRESS);
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
	public static class DateFormatContext extends ParserRuleContext {
		public List<TerminalNode> INT() { return getTokens(BatchParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(BatchParser.INT, i);
		}
		public List<TerminalNode> DASH() { return getTokens(BatchParser.DASH); }
		public TerminalNode DASH(int i) {
			return getToken(BatchParser.DASH, i);
		}
		public DateFormatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dateFormat; }
	}

	public final DateFormatContext dateFormat() throws RecognitionException {
		DateFormatContext _localctx = new DateFormatContext(_ctx, getState());
		enterRule(_localctx, 126, RULE_dateFormat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(586);
			match(INT);
			setState(587);
			match(DASH);
			setState(588);
			match(INT);
			setState(589);
			match(DASH);
			setState(590);
			match(INT);
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
	public static class SetLocalOptionContext extends ParserRuleContext {
		public TerminalNode ENABLEDELAYEDEXPANSION() { return getToken(BatchParser.ENABLEDELAYEDEXPANSION, 0); }
		public TerminalNode DISABLEDELAYEDEXPANSION() { return getToken(BatchParser.DISABLEDELAYEDEXPANSION, 0); }
		public TerminalNode IDENTIFIER() { return getToken(BatchParser.IDENTIFIER, 0); }
		public SetLocalOptionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_setLocalOption; }
	}

	public final SetLocalOptionContext setLocalOption() throws RecognitionException {
		SetLocalOptionContext _localctx = new SetLocalOptionContext(_ctx, getState());
		enterRule(_localctx, 128, RULE_setLocalOption);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(592);
			_la = _input.LA(1);
			if ( !(_la==ENABLEDELAYEDEXPANSION || _la==DISABLEDELAYEDEXPANSION || _la==IDENTIFIER) ) {
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
	public static class SetStatementContext extends ParserRuleContext {
		public TerminalNode SET() { return getToken(BatchParser.SET, 0); }
		public VariableNameContext variableName() {
			return getRuleContext(VariableNameContext.class,0);
		}
		public SwitchesContext switches() {
			return getRuleContext(SwitchesContext.class,0);
		}
		public AssignmentPartContext assignmentPart() {
			return getRuleContext(AssignmentPartContext.class,0);
		}
		public DisplayFormatingContext displayFormating() {
			return getRuleContext(DisplayFormatingContext.class,0);
		}
		public SetStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_setStatement; }
	}

	public final SetStatementContext setStatement() throws RecognitionException {
		SetStatementContext _localctx = new SetStatementContext(_ctx, getState());
		enterRule(_localctx, 130, RULE_setStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(594);
			match(SET);
			setState(596);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 9223372002495037440L) != 0)) {
				{
				setState(595);
				switches();
				}
			}

			{
			setState(598);
			variableName();
			}
			setState(600);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,50,_ctx) ) {
			case 1:
				{
				setState(599);
				assignmentPart();
				}
				break;
			}
			setState(603);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==JP_EQUAL) {
				{
				setState(602);
				displayFormating();
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
	public static class DisplayFormatingContext extends ParserRuleContext {
		public TerminalNode JP_EQUAL() { return getToken(BatchParser.JP_EQUAL, 0); }
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public DisplayFormatingContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_displayFormating; }
	}

	public final DisplayFormatingContext displayFormating() throws RecognitionException {
		DisplayFormatingContext _localctx = new DisplayFormatingContext(_ctx, getState());
		enterRule(_localctx, 132, RULE_displayFormating);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(605);
			match(JP_EQUAL);
			setState(606);
			value();
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
	public static class AssignmentPartContext extends ParserRuleContext {
		public TerminalNode EQUAL() { return getToken(BatchParser.EQUAL, 0); }
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public List<TerminalNode> STRING_CHARACTERS() { return getTokens(BatchParser.STRING_CHARACTERS); }
		public TerminalNode STRING_CHARACTERS(int i) {
			return getToken(BatchParser.STRING_CHARACTERS, i);
		}
		public CalcOperatorContext calcOperator() {
			return getRuleContext(CalcOperatorContext.class,0);
		}
		public TerminalNode INT() { return getToken(BatchParser.INT, 0); }
		public AssignmentPartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignmentPart; }
	}

	public final AssignmentPartContext assignmentPart() throws RecognitionException {
		AssignmentPartContext _localctx = new AssignmentPartContext(_ctx, getState());
		enterRule(_localctx, 134, RULE_assignmentPart);
		int _la;
		try {
			setState(621);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case EQUAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(608);
				match(EQUAL);
				setState(615);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,53,_ctx) ) {
				case 1:
					{
					setState(609);
					value();
					}
					break;
				case 2:
					{
					setState(611); 
					_errHandler.sync(this);
					_la = _input.LA(1);
					do {
						{
						{
						setState(610);
						match(STRING_CHARACTERS);
						}
						}
						setState(613); 
						_errHandler.sync(this);
						_la = _input.LA(1);
					} while ( _la==STRING_CHARACTERS );
					}
					break;
				}
				}
				break;
			case SLASH:
			case DASH:
			case PLUS:
			case STAR:
				enterOuterAlt(_localctx, 2);
				{
				setState(617);
				calcOperator();
				setState(618);
				match(EQUAL);
				setState(619);
				match(INT);
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
	public static class PauseStatementContext extends ParserRuleContext {
		public TerminalNode PAUSE() { return getToken(BatchParser.PAUSE, 0); }
		public TerminalNode GREATER_CHAR() { return getToken(BatchParser.GREATER_CHAR, 0); }
		public TerminalNode NUL() { return getToken(BatchParser.NUL, 0); }
		public PauseStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pauseStatement; }
	}

	public final PauseStatementContext pauseStatement() throws RecognitionException {
		PauseStatementContext _localctx = new PauseStatementContext(_ctx, getState());
		enterRule(_localctx, 136, RULE_pauseStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(623);
			match(PAUSE);
			setState(626);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==GREATER_CHAR) {
				{
				setState(624);
				match(GREATER_CHAR);
				setState(625);
				match(NUL);
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
	public static class VariableNameContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(BatchParser.IDENTIFIER, 0); }
		public VariableNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variableName; }
	}

	public final VariableNameContext variableName() throws RecognitionException {
		VariableNameContext _localctx = new VariableNameContext(_ctx, getState());
		enterRule(_localctx, 138, RULE_variableName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(628);
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
	public static class ValueContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(BatchParser.STRING, 0); }
		public TerminalNode IDENTIFIER() { return getToken(BatchParser.IDENTIFIER, 0); }
		public List<ReferencedVariableContext> referencedVariable() {
			return getRuleContexts(ReferencedVariableContext.class);
		}
		public ReferencedVariableContext referencedVariable(int i) {
			return getRuleContext(ReferencedVariableContext.class,i);
		}
		public IdentifierCombinedWithReferencedVariableContext identifierCombinedWithReferencedVariable() {
			return getRuleContext(IdentifierCombinedWithReferencedVariableContext.class,0);
		}
		public FilePathContext filePath() {
			return getRuleContext(FilePathContext.class,0);
		}
		public FileNameContext fileName() {
			return getRuleContext(FileNameContext.class,0);
		}
		public TerminalNode JP_TXT() { return getToken(BatchParser.JP_TXT, 0); }
		public CalcValueContext calcValue() {
			return getRuleContext(CalcValueContext.class,0);
		}
		public TerminalNode INT() { return getToken(BatchParser.INT, 0); }
		public ForVariableContext forVariable() {
			return getRuleContext(ForVariableContext.class,0);
		}
		public ValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value; }
	}

	public final ValueContext value() throws RecognitionException {
		ValueContext _localctx = new ValueContext(_ctx, getState());
		enterRule(_localctx, 140, RULE_value);
		try {
			int _alt;
			setState(644);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,57,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(630);
				match(STRING);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(631);
				match(IDENTIFIER);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(633); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(632);
						referencedVariable();
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(635); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,56,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(637);
				identifierCombinedWithReferencedVariable();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(638);
				filePath();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(639);
				fileName();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(640);
				match(JP_TXT);
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(641);
				calcValue();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(642);
				match(INT);
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(643);
				forVariable();
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
	public static class CalcValueContext extends ParserRuleContext {
		public CalcOperatorContext calcOperator() {
			return getRuleContext(CalcOperatorContext.class,0);
		}
		public List<TerminalNode> INT() { return getTokens(BatchParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(BatchParser.INT, i);
		}
		public List<ReferencedVariableContext> referencedVariable() {
			return getRuleContexts(ReferencedVariableContext.class);
		}
		public ReferencedVariableContext referencedVariable(int i) {
			return getRuleContext(ReferencedVariableContext.class,i);
		}
		public List<TerminalNode> STRING() { return getTokens(BatchParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(BatchParser.STRING, i);
		}
		public CalcValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_calcValue; }
	}

	public final CalcValueContext calcValue() throws RecognitionException {
		CalcValueContext _localctx = new CalcValueContext(_ctx, getState());
		enterRule(_localctx, 142, RULE_calcValue);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(649);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				{
				setState(646);
				match(INT);
				}
				break;
			case PERCENT:
			case EXCLAMATION:
				{
				setState(647);
				referencedVariable();
				}
				break;
			case STRING:
				{
				setState(648);
				match(STRING);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(651);
			calcOperator();
			setState(655);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				{
				setState(652);
				match(INT);
				}
				break;
			case PERCENT:
			case EXCLAMATION:
				{
				setState(653);
				referencedVariable();
				}
				break;
			case STRING:
				{
				setState(654);
				match(STRING);
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
	public static class CalcOperatorContext extends ParserRuleContext {
		public TerminalNode PLUS() { return getToken(BatchParser.PLUS, 0); }
		public TerminalNode DASH() { return getToken(BatchParser.DASH, 0); }
		public TerminalNode STAR() { return getToken(BatchParser.STAR, 0); }
		public TerminalNode SLASH() { return getToken(BatchParser.SLASH, 0); }
		public CalcOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_calcOperator; }
	}

	public final CalcOperatorContext calcOperator() throws RecognitionException {
		CalcOperatorContext _localctx = new CalcOperatorContext(_ctx, getState());
		enterRule(_localctx, 144, RULE_calcOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(657);
			_la = _input.LA(1);
			if ( !(_la==SLASH || ((((_la - 91)) & ~0x3f) == 0 && ((1L << (_la - 91)) & 193L) != 0)) ) {
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
	public static class FilePathContext extends ParserRuleContext {
		public List<FileNameContext> fileName() {
			return getRuleContexts(FileNameContext.class);
		}
		public FileNameContext fileName(int i) {
			return getRuleContext(FileNameContext.class,i);
		}
		public TerminalNode DISK_ADDRESS() { return getToken(BatchParser.DISK_ADDRESS, 0); }
		public List<TerminalNode> SSLASH() { return getTokens(BatchParser.SSLASH); }
		public TerminalNode SSLASH(int i) {
			return getToken(BatchParser.SSLASH, i);
		}
		public FilePathContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_filePath; }
	}

	public final FilePathContext filePath() throws RecognitionException {
		FilePathContext _localctx = new FilePathContext(_ctx, getState());
		enterRule(_localctx, 146, RULE_filePath);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(661);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case QUESTION:
			case DOT:
			case EXE:
			case PERCENT:
			case EXCLAMATION:
			case UNDERSCORE:
			case COMMA:
			case STAR:
			case JP_TXT:
			case IDENTIFIER:
				{
				setState(659);
				fileName();
				}
				break;
			case DISK_ADDRESS:
				{
				setState(660);
				match(DISK_ADDRESS);
				}
				break;
			case SSLASH:
				break;
			default:
				break;
			}
			setState(667); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(663);
					match(SSLASH);
					setState(665);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,61,_ctx) ) {
					case 1:
						{
						setState(664);
						fileName();
						}
						break;
					}
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(669); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,62,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
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
	public static class FileNameContext extends ParserRuleContext {
		public List<FileNameCharContext> fileNameChar() {
			return getRuleContexts(FileNameCharContext.class);
		}
		public FileNameCharContext fileNameChar(int i) {
			return getRuleContext(FileNameCharContext.class,i);
		}
		public FileNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fileName; }
	}

	public final FileNameContext fileName() throws RecognitionException {
		FileNameContext _localctx = new FileNameContext(_ctx, getState());
		enterRule(_localctx, 148, RULE_fileName);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(672); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(671);
					fileNameChar();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(674); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,63,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
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
	public static class FileNameCharContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(BatchParser.IDENTIFIER, 0); }
		public TerminalNode UNDERSCORE() { return getToken(BatchParser.UNDERSCORE, 0); }
		public TerminalNode DOT() { return getToken(BatchParser.DOT, 0); }
		public TerminalNode JP_TXT() { return getToken(BatchParser.JP_TXT, 0); }
		public ReferencedVariableContext referencedVariable() {
			return getRuleContext(ReferencedVariableContext.class,0);
		}
		public TerminalNode STAR() { return getToken(BatchParser.STAR, 0); }
		public TerminalNode COMMA() { return getToken(BatchParser.COMMA, 0); }
		public TerminalNode QUESTION() { return getToken(BatchParser.QUESTION, 0); }
		public TerminalNode EXE() { return getToken(BatchParser.EXE, 0); }
		public FileNameCharContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fileNameChar; }
	}

	public final FileNameCharContext fileNameChar() throws RecognitionException {
		FileNameCharContext _localctx = new FileNameCharContext(_ctx, getState());
		enterRule(_localctx, 150, RULE_fileNameChar);
		try {
			setState(685);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(676);
				match(IDENTIFIER);
				}
				break;
			case UNDERSCORE:
				enterOuterAlt(_localctx, 2);
				{
				setState(677);
				match(UNDERSCORE);
				}
				break;
			case DOT:
				enterOuterAlt(_localctx, 3);
				{
				setState(678);
				match(DOT);
				}
				break;
			case JP_TXT:
				enterOuterAlt(_localctx, 4);
				{
				setState(679);
				match(JP_TXT);
				}
				break;
			case PERCENT:
			case EXCLAMATION:
				enterOuterAlt(_localctx, 5);
				{
				setState(680);
				referencedVariable();
				}
				break;
			case STAR:
				enterOuterAlt(_localctx, 6);
				{
				setState(681);
				match(STAR);
				}
				break;
			case COMMA:
				enterOuterAlt(_localctx, 7);
				{
				setState(682);
				match(COMMA);
				}
				break;
			case QUESTION:
				enterOuterAlt(_localctx, 8);
				{
				setState(683);
				match(QUESTION);
				}
				break;
			case EXE:
				enterOuterAlt(_localctx, 9);
				{
				setState(684);
				match(EXE);
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
	public static class IdentifierCombinedWithReferencedVariableContext extends ParserRuleContext {
		public List<IdetifierOrRerencedVariableContext> idetifierOrRerencedVariable() {
			return getRuleContexts(IdetifierOrRerencedVariableContext.class);
		}
		public IdetifierOrRerencedVariableContext idetifierOrRerencedVariable(int i) {
			return getRuleContext(IdetifierOrRerencedVariableContext.class,i);
		}
		public IdentifierCombinedWithReferencedVariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifierCombinedWithReferencedVariable; }
	}

	public final IdentifierCombinedWithReferencedVariableContext identifierCombinedWithReferencedVariable() throws RecognitionException {
		IdentifierCombinedWithReferencedVariableContext _localctx = new IdentifierCombinedWithReferencedVariableContext(_ctx, getState());
		enterRule(_localctx, 152, RULE_identifierCombinedWithReferencedVariable);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(688); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(687);
					idetifierOrRerencedVariable();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(690); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,65,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
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
	public static class IdetifierOrRerencedVariableContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(BatchParser.IDENTIFIER, 0); }
		public ReferencedVariableContext referencedVariable() {
			return getRuleContext(ReferencedVariableContext.class,0);
		}
		public IdetifierOrRerencedVariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_idetifierOrRerencedVariable; }
	}

	public final IdetifierOrRerencedVariableContext idetifierOrRerencedVariable() throws RecognitionException {
		IdetifierOrRerencedVariableContext _localctx = new IdetifierOrRerencedVariableContext(_ctx, getState());
		enterRule(_localctx, 154, RULE_idetifierOrRerencedVariable);
		try {
			setState(694);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(692);
				match(IDENTIFIER);
				}
				break;
			case PERCENT:
			case EXCLAMATION:
				enterOuterAlt(_localctx, 2);
				{
				setState(693);
				referencedVariable();
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
	public static class ReferencedVariableContext extends ParserRuleContext {
		public List<TerminalNode> PERCENT() { return getTokens(BatchParser.PERCENT); }
		public TerminalNode PERCENT(int i) {
			return getToken(BatchParser.PERCENT, i);
		}
		public VariableNameContext variableName() {
			return getRuleContext(VariableNameContext.class,0);
		}
		public VariableSubstringContext variableSubstring() {
			return getRuleContext(VariableSubstringContext.class,0);
		}
		public List<TerminalNode> EXCLAMATION() { return getTokens(BatchParser.EXCLAMATION); }
		public TerminalNode EXCLAMATION(int i) {
			return getToken(BatchParser.EXCLAMATION, i);
		}
		public ReferencedVariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_referencedVariable; }
	}

	public final ReferencedVariableContext referencedVariable() throws RecognitionException {
		ReferencedVariableContext _localctx = new ReferencedVariableContext(_ctx, getState());
		enterRule(_localctx, 156, RULE_referencedVariable);
		int _la;
		try {
			setState(710);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PERCENT:
				enterOuterAlt(_localctx, 1);
				{
				setState(696);
				match(PERCENT);
				{
				setState(697);
				variableName();
				}
				setState(699);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COLON) {
					{
					setState(698);
					variableSubstring();
					}
				}

				setState(701);
				match(PERCENT);
				}
				break;
			case EXCLAMATION:
				enterOuterAlt(_localctx, 2);
				{
				setState(703);
				match(EXCLAMATION);
				{
				setState(704);
				variableName();
				}
				setState(706);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COLON) {
					{
					setState(705);
					variableSubstring();
					}
				}

				setState(708);
				match(EXCLAMATION);
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
	public static class VariableSubstringContext extends ParserRuleContext {
		public TerminalNode COLON() { return getToken(BatchParser.COLON, 0); }
		public LeftSubstringContext leftSubstring() {
			return getRuleContext(LeftSubstringContext.class,0);
		}
		public RightSubstringContext rightSubstring() {
			return getRuleContext(RightSubstringContext.class,0);
		}
		public RemoveSubstringContext removeSubstring() {
			return getRuleContext(RemoveSubstringContext.class,0);
		}
		public RemoveSpacesContext removeSpaces() {
			return getRuleContext(RemoveSpacesContext.class,0);
		}
		public ReplaceSubstringContext replaceSubstring() {
			return getRuleContext(ReplaceSubstringContext.class,0);
		}
		public VariableSubstringContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variableSubstring; }
	}

	public final VariableSubstringContext variableSubstring() throws RecognitionException {
		VariableSubstringContext _localctx = new VariableSubstringContext(_ctx, getState());
		enterRule(_localctx, 158, RULE_variableSubstring);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(712);
			match(COLON);
			setState(718);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,70,_ctx) ) {
			case 1:
				{
				setState(713);
				leftSubstring();
				}
				break;
			case 2:
				{
				setState(714);
				rightSubstring();
				}
				break;
			case 3:
				{
				setState(715);
				removeSubstring();
				}
				break;
			case 4:
				{
				setState(716);
				removeSpaces();
				}
				break;
			case 5:
				{
				setState(717);
				replaceSubstring();
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
	public static class LeftSubstringContext extends ParserRuleContext {
		public TerminalNode TILDE() { return getToken(BatchParser.TILDE, 0); }
		public StartSubContext startSub() {
			return getRuleContext(StartSubContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(BatchParser.COMMA, 0); }
		public LengthSubContext lengthSub() {
			return getRuleContext(LengthSubContext.class,0);
		}
		public LeftSubstringContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_leftSubstring; }
	}

	public final LeftSubstringContext leftSubstring() throws RecognitionException {
		LeftSubstringContext _localctx = new LeftSubstringContext(_ctx, getState());
		enterRule(_localctx, 160, RULE_leftSubstring);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(720);
			match(TILDE);
			setState(721);
			startSub();
			setState(722);
			match(COMMA);
			setState(723);
			lengthSub();
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
	public static class RightSubstringContext extends ParserRuleContext {
		public TerminalNode TILDE() { return getToken(BatchParser.TILDE, 0); }
		public TerminalNode DASH() { return getToken(BatchParser.DASH, 0); }
		public LengthSubContext lengthSub() {
			return getRuleContext(LengthSubContext.class,0);
		}
		public RightSubstringContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rightSubstring; }
	}

	public final RightSubstringContext rightSubstring() throws RecognitionException {
		RightSubstringContext _localctx = new RightSubstringContext(_ctx, getState());
		enterRule(_localctx, 162, RULE_rightSubstring);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(725);
			match(TILDE);
			setState(726);
			match(DASH);
			setState(727);
			lengthSub();
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
	public static class ReplacedOrRemovedSubstringContext extends ParserRuleContext {
		public TerminalNode WS() { return getToken(BatchParser.WS, 0); }
		public TerminalNode COLON() { return getToken(BatchParser.COLON, 0); }
		public TerminalNode IDENTIFIER() { return getToken(BatchParser.IDENTIFIER, 0); }
		public TerminalNode DOT() { return getToken(BatchParser.DOT, 0); }
		public TerminalNode INT() { return getToken(BatchParser.INT, 0); }
		public List<TerminalNode> STRING_CHARACTERS() { return getTokens(BatchParser.STRING_CHARACTERS); }
		public TerminalNode STRING_CHARACTERS(int i) {
			return getToken(BatchParser.STRING_CHARACTERS, i);
		}
		public ReplacedOrRemovedSubstringContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_replacedOrRemovedSubstring; }
	}

	public final ReplacedOrRemovedSubstringContext replacedOrRemovedSubstring() throws RecognitionException {
		ReplacedOrRemovedSubstringContext _localctx = new ReplacedOrRemovedSubstringContext(_ctx, getState());
		enterRule(_localctx, 164, RULE_replacedOrRemovedSubstring);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(739);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case STRING_CHARACTERS:
				{
				setState(730); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(729);
					match(STRING_CHARACTERS);
					}
					}
					setState(732); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==STRING_CHARACTERS );
				}
				break;
			case WS:
				{
				setState(734);
				match(WS);
				}
				break;
			case COLON:
				{
				setState(735);
				match(COLON);
				}
				break;
			case IDENTIFIER:
				{
				setState(736);
				match(IDENTIFIER);
				}
				break;
			case DOT:
				{
				setState(737);
				match(DOT);
				}
				break;
			case INT:
				{
				setState(738);
				match(INT);
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
	public static class RemoveSubstringContext extends ParserRuleContext {
		public RemovedSubstringContext removedSubstring() {
			return getRuleContext(RemovedSubstringContext.class,0);
		}
		public TerminalNode EQUAL() { return getToken(BatchParser.EQUAL, 0); }
		public RemoveSubstringContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_removeSubstring; }
	}

	public final RemoveSubstringContext removeSubstring() throws RecognitionException {
		RemoveSubstringContext _localctx = new RemoveSubstringContext(_ctx, getState());
		enterRule(_localctx, 166, RULE_removeSubstring);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(741);
			removedSubstring();
			setState(742);
			match(EQUAL);
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
	public static class RemovedSubstringContext extends ParserRuleContext {
		public ReplacedOrRemovedSubstringContext replacedOrRemovedSubstring() {
			return getRuleContext(ReplacedOrRemovedSubstringContext.class,0);
		}
		public RemovedSubstringContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_removedSubstring; }
	}

	public final RemovedSubstringContext removedSubstring() throws RecognitionException {
		RemovedSubstringContext _localctx = new RemovedSubstringContext(_ctx, getState());
		enterRule(_localctx, 168, RULE_removedSubstring);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(744);
			replacedOrRemovedSubstring();
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
	public static class RemoveSpacesContext extends ParserRuleContext {
		public TerminalNode EQUAL() { return getToken(BatchParser.EQUAL, 0); }
		public RemoveSpacesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_removeSpaces; }
	}

	public final RemoveSpacesContext removeSpaces() throws RecognitionException {
		RemoveSpacesContext _localctx = new RemoveSpacesContext(_ctx, getState());
		enterRule(_localctx, 170, RULE_removeSpaces);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(746);
			match(EQUAL);
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
	public static class ReplaceSubstringContext extends ParserRuleContext {
		public TerminalNode EQUAL() { return getToken(BatchParser.EQUAL, 0); }
		public SubStringReplacedContext subStringReplaced() {
			return getRuleContext(SubStringReplacedContext.class,0);
		}
		public SubtringRemovedContext subtringRemoved() {
			return getRuleContext(SubtringRemovedContext.class,0);
		}
		public ReplaceSubstringContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_replaceSubstring; }
	}

	public final ReplaceSubstringContext replaceSubstring() throws RecognitionException {
		ReplaceSubstringContext _localctx = new ReplaceSubstringContext(_ctx, getState());
		enterRule(_localctx, 172, RULE_replaceSubstring);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(749);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & -9223372036854512896L) != 0) || _la==IDENTIFIER || _la==STRING_CHARACTERS) {
				{
				setState(748);
				subtringRemoved();
				}
			}

			setState(751);
			match(EQUAL);
			setState(752);
			subStringReplaced();
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
	public static class SubtringRemovedContext extends ParserRuleContext {
		public ReplacedOrRemovedSubstringContext replacedOrRemovedSubstring() {
			return getRuleContext(ReplacedOrRemovedSubstringContext.class,0);
		}
		public SubtringRemovedContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subtringRemoved; }
	}

	public final SubtringRemovedContext subtringRemoved() throws RecognitionException {
		SubtringRemovedContext _localctx = new SubtringRemovedContext(_ctx, getState());
		enterRule(_localctx, 174, RULE_subtringRemoved);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(754);
			replacedOrRemovedSubstring();
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
	public static class SubStringReplacedContext extends ParserRuleContext {
		public ReplacedOrRemovedSubstringContext replacedOrRemovedSubstring() {
			return getRuleContext(ReplacedOrRemovedSubstringContext.class,0);
		}
		public SubStringReplacedContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subStringReplaced; }
	}

	public final SubStringReplacedContext subStringReplaced() throws RecognitionException {
		SubStringReplacedContext _localctx = new SubStringReplacedContext(_ctx, getState());
		enterRule(_localctx, 176, RULE_subStringReplaced);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(756);
			replacedOrRemovedSubstring();
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
	public static class StartSubContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(BatchParser.INT, 0); }
		public StartSubContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_startSub; }
	}

	public final StartSubContext startSub() throws RecognitionException {
		StartSubContext _localctx = new StartSubContext(_ctx, getState());
		enterRule(_localctx, 178, RULE_startSub);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(758);
			match(INT);
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
	public static class LengthSubContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(BatchParser.INT, 0); }
		public TerminalNode DASH() { return getToken(BatchParser.DASH, 0); }
		public LengthSubContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lengthSub; }
	}

	public final LengthSubContext lengthSub() throws RecognitionException {
		LengthSubContext _localctx = new LengthSubContext(_ctx, getState());
		enterRule(_localctx, 180, RULE_lengthSub);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(761);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==DASH) {
				{
				setState(760);
				match(DASH);
				}
			}

			setState(763);
			match(INT);
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
	public static class VariableStartContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(BatchParser.INT, 0); }
		public VariableStartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variableStart; }
	}

	public final VariableStartContext variableStart() throws RecognitionException {
		VariableStartContext _localctx = new VariableStartContext(_ctx, getState());
		enterRule(_localctx, 182, RULE_variableStart);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(765);
			match(INT);
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
	public static class VariableLengthContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(BatchParser.INT, 0); }
		public VariableLengthContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variableLength; }
	}

	public final VariableLengthContext variableLength() throws RecognitionException {
		VariableLengthContext _localctx = new VariableLengthContext(_ctx, getState());
		enterRule(_localctx, 184, RULE_variableLength);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(767);
			match(INT);
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
	public static class ConcatenateStringContext extends ParserRuleContext {
		public List<TerminalNode> STRING() { return getTokens(BatchParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(BatchParser.STRING, i);
		}
		public TerminalNode PLUS() { return getToken(BatchParser.PLUS, 0); }
		public ConcatenateStringContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_concatenateString; }
	}

	public final ConcatenateStringContext concatenateString() throws RecognitionException {
		ConcatenateStringContext _localctx = new ConcatenateStringContext(_ctx, getState());
		enterRule(_localctx, 186, RULE_concatenateString);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(769);
			match(STRING);
			setState(770);
			match(PLUS);
			setState(771);
			match(STRING);
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
		"\u0004\u0001f\u0306\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
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
		"Z\u0007Z\u0002[\u0007[\u0002\\\u0007\\\u0002]\u0007]\u0001\u0000\u0005"+
		"\u0000\u00be\b\u0000\n\u0000\f\u0000\u00c1\t\u0000\u0001\u0000\u0005\u0000"+
		"\u00c4\b\u0000\n\u0000\f\u0000\u00c7\t\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0001\u0001\u0005\u0001\u00cd\b\u0001\n\u0001\f\u0001\u00d0\t\u0001"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u0003\u00e8\b\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0006\u0004\u0006\u00f2\b\u0006\u000b\u0006\f\u0006"+
		"\u00f3\u0001\u0007\u0001\u0007\u0005\u0007\u00f8\b\u0007\n\u0007\f\u0007"+
		"\u00fb\t\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n"+
		"\u0001\n\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0004\u000b\u010a"+
		"\b\u000b\u000b\u000b\f\u000b\u010b\u0001\f\u0001\f\u0001\f\u0001\f\u0001"+
		"\r\u0004\r\u0113\b\r\u000b\r\f\r\u0114\u0001\u000e\u0001\u000e\u0004\u000e"+
		"\u0119\b\u000e\u000b\u000e\f\u000e\u011a\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u0010\u0001\u0010\u0004\u0010\u0122\b\u0010\u000b\u0010\f"+
		"\u0010\u0123\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012"+
		"\u0004\u0012\u012b\b\u0012\u000b\u0012\f\u0012\u012c\u0001\u0013\u0001"+
		"\u0013\u0003\u0013\u0131\b\u0013\u0001\u0014\u0001\u0014\u0004\u0014\u0135"+
		"\b\u0014\u000b\u0014\f\u0014\u0136\u0001\u0015\u0001\u0015\u0001\u0015"+
		"\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016"+
		"\u0003\u0016\u0142\b\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0003\u0017"+
		"\u0147\b\u0017\u0001\u0018\u0001\u0018\u0001\u0019\u0001\u0019\u0004\u0019"+
		"\u014d\b\u0019\u000b\u0019\f\u0019\u014e\u0001\u0019\u0003\u0019\u0152"+
		"\b\u0019\u0001\u0019\u0003\u0019\u0155\b\u0019\u0001\u001a\u0004\u001a"+
		"\u0158\b\u001a\u000b\u001a\f\u001a\u0159\u0001\u001b\u0001\u001b\u0001"+
		"\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0003\u001b\u0162\b\u001b\u0001"+
		"\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001d\u0001"+
		"\u001d\u0001\u001d\u0001\u001e\u0001\u001e\u0001\u001f\u0001\u001f\u0003"+
		"\u001f\u0170\b\u001f\u0001\u001f\u0005\u001f\u0173\b\u001f\n\u001f\f\u001f"+
		"\u0176\t\u001f\u0001 \u0001 \u0001!\u0001!\u0001!\u0001!\u0001!\u0001"+
		"!\u0001!\u0001!\u0003!\u0182\b!\u0001\"\u0001\"\u0003\"\u0186\b\"\u0001"+
		"\"\u0001\"\u0001\"\u0003\"\u018b\b\"\u0001#\u0001#\u0003#\u018f\b#\u0001"+
		"#\u0003#\u0192\b#\u0001$\u0001$\u0001%\u0001%\u0003%\u0198\b%\u0001&\u0001"+
		"&\u0003&\u019c\b&\u0001&\u0003&\u019f\b&\u0001&\u0001&\u0001&\u0001&\u0001"+
		"&\u0001&\u0001\'\u0001\'\u0001(\u0001(\u0004(\u01ab\b(\u000b(\f(\u01ac"+
		"\u0001(\u0001(\u0001)\u0001)\u0001)\u0001)\u0001)\u0001)\u0003)\u01b7"+
		"\b)\u0001*\u0001*\u0001*\u0003*\u01bc\b*\u0001*\u0001*\u0001+\u0001+\u0001"+
		",\u0001,\u0004,\u01c4\b,\u000b,\f,\u01c5\u0001,\u0001,\u0001-\u0001-\u0001"+
		"-\u0003-\u01cd\b-\u0001.\u0001.\u0001.\u0001.\u0003.\u01d3\b.\u0001/\u0001"+
		"/\u0004/\u01d7\b/\u000b/\f/\u01d8\u0001/\u0001/\u0001/\u0003/\u01de\b"+
		"/\u00010\u00010\u00010\u00040\u01e3\b0\u000b0\f0\u01e4\u00010\u00010\u0001"+
		"1\u00011\u00012\u00032\u01ec\b2\u00012\u00012\u00012\u00013\u00013\u0001"+
		"3\u00033\u01f4\b3\u00014\u00014\u00014\u00014\u00034\u01fa\b4\u00015\u0001"+
		"5\u00016\u00016\u00016\u00017\u00017\u00017\u00018\u00018\u00018\u0003"+
		"8\u0207\b8\u00019\u00019\u00039\u020b\b9\u00019\u00019\u0001:\u0001:\u0001"+
		":\u0001:\u0003:\u0213\b:\u0001;\u0001;\u0001<\u0001<\u0001=\u0004=\u021a"+
		"\b=\u000b=\f=\u021b\u0001>\u0001>\u0001>\u0001>\u0001>\u0001>\u0001>\u0001"+
		">\u0001>\u0001>\u0001>\u0001>\u0001>\u0001>\u0001>\u0001>\u0001>\u0001"+
		">\u0001>\u0001>\u0001>\u0001>\u0001>\u0001>\u0001>\u0001>\u0001>\u0001"+
		">\u0001>\u0001>\u0001>\u0001>\u0005>\u023e\b>\n>\f>\u0241\t>\u0001>\u0001"+
		">\u0001>\u0001>\u0001>\u0001>\u0003>\u0249\b>\u0001?\u0001?\u0001?\u0001"+
		"?\u0001?\u0001?\u0001@\u0001@\u0001A\u0001A\u0003A\u0255\bA\u0001A\u0001"+
		"A\u0003A\u0259\bA\u0001A\u0003A\u025c\bA\u0001B\u0001B\u0001B\u0001C\u0001"+
		"C\u0001C\u0004C\u0264\bC\u000bC\fC\u0265\u0003C\u0268\bC\u0001C\u0001"+
		"C\u0001C\u0001C\u0003C\u026e\bC\u0001D\u0001D\u0001D\u0003D\u0273\bD\u0001"+
		"E\u0001E\u0001F\u0001F\u0001F\u0004F\u027a\bF\u000bF\fF\u027b\u0001F\u0001"+
		"F\u0001F\u0001F\u0001F\u0001F\u0001F\u0003F\u0285\bF\u0001G\u0001G\u0001"+
		"G\u0003G\u028a\bG\u0001G\u0001G\u0001G\u0001G\u0003G\u0290\bG\u0001H\u0001"+
		"H\u0001I\u0001I\u0003I\u0296\bI\u0001I\u0001I\u0003I\u029a\bI\u0004I\u029c"+
		"\bI\u000bI\fI\u029d\u0001J\u0004J\u02a1\bJ\u000bJ\fJ\u02a2\u0001K\u0001"+
		"K\u0001K\u0001K\u0001K\u0001K\u0001K\u0001K\u0001K\u0003K\u02ae\bK\u0001"+
		"L\u0004L\u02b1\bL\u000bL\fL\u02b2\u0001M\u0001M\u0003M\u02b7\bM\u0001"+
		"N\u0001N\u0001N\u0003N\u02bc\bN\u0001N\u0001N\u0001N\u0001N\u0001N\u0003"+
		"N\u02c3\bN\u0001N\u0001N\u0003N\u02c7\bN\u0001O\u0001O\u0001O\u0001O\u0001"+
		"O\u0001O\u0003O\u02cf\bO\u0001P\u0001P\u0001P\u0001P\u0001P\u0001Q\u0001"+
		"Q\u0001Q\u0001Q\u0001R\u0004R\u02db\bR\u000bR\fR\u02dc\u0001R\u0001R\u0001"+
		"R\u0001R\u0001R\u0003R\u02e4\bR\u0001S\u0001S\u0001S\u0001T\u0001T\u0001"+
		"U\u0001U\u0001V\u0003V\u02ee\bV\u0001V\u0001V\u0001V\u0001W\u0001W\u0001"+
		"X\u0001X\u0001Y\u0001Y\u0001Z\u0003Z\u02fa\bZ\u0001Z\u0001Z\u0001[\u0001"+
		"[\u0001\\\u0001\\\u0001]\u0001]\u0001]\u0001]\u0001]\u0000\u0000^\u0000"+
		"\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c"+
		"\u001e \"$&(*,.02468:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084"+
		"\u0086\u0088\u008a\u008c\u008e\u0090\u0092\u0094\u0096\u0098\u009a\u009c"+
		"\u009e\u00a0\u00a2\u00a4\u00a6\u00a8\u00aa\u00ac\u00ae\u00b0\u00b2\u00b4"+
		"\u00b6\u00b8\u00ba\u0000\u0005\u0002\u0000\u0019\u001a \"\u0003\u0000"+
		"\b\b??ee\u0003\u0000FGMMOO\u0002\u0000\u0006\u0007ee\u0003\u0000\u0016"+
		"\u0016[[ab\u034e\u0000\u00bf\u0001\u0000\u0000\u0000\u0002\u00ca\u0001"+
		"\u0000\u0000\u0000\u0004\u00d1\u0001\u0000\u0000\u0000\u0006\u00e7\u0001"+
		"\u0000\u0000\u0000\b\u00e9\u0001\u0000\u0000\u0000\n\u00ee\u0001\u0000"+
		"\u0000\u0000\f\u00f1\u0001\u0000\u0000\u0000\u000e\u00f5\u0001\u0000\u0000"+
		"\u0000\u0010\u00fc\u0001\u0000\u0000\u0000\u0012\u00fe\u0001\u0000\u0000"+
		"\u0000\u0014\u0100\u0001\u0000\u0000\u0000\u0016\u0107\u0001\u0000\u0000"+
		"\u0000\u0018\u010d\u0001\u0000\u0000\u0000\u001a\u0112\u0001\u0000\u0000"+
		"\u0000\u001c\u0116\u0001\u0000\u0000\u0000\u001e\u011c\u0001\u0000\u0000"+
		"\u0000 \u011f\u0001\u0000\u0000\u0000\"\u0125\u0001\u0000\u0000\u0000"+
		"$\u0128\u0001\u0000\u0000\u0000&\u012e\u0001\u0000\u0000\u0000(\u0132"+
		"\u0001\u0000\u0000\u0000*\u0138\u0001\u0000\u0000\u0000,\u0141\u0001\u0000"+
		"\u0000\u0000.\u0143\u0001\u0000\u0000\u00000\u0148\u0001\u0000\u0000\u0000"+
		"2\u014c\u0001\u0000\u0000\u00004\u0157\u0001\u0000\u0000\u00006\u0161"+
		"\u0001\u0000\u0000\u00008\u0163\u0001\u0000\u0000\u0000:\u0168\u0001\u0000"+
		"\u0000\u0000<\u016b\u0001\u0000\u0000\u0000>\u016d\u0001\u0000\u0000\u0000"+
		"@\u0177\u0001\u0000\u0000\u0000B\u0181\u0001\u0000\u0000\u0000D\u0185"+
		"\u0001\u0000\u0000\u0000F\u018c\u0001\u0000\u0000\u0000H\u0193\u0001\u0000"+
		"\u0000\u0000J\u0197\u0001\u0000\u0000\u0000L\u0199\u0001\u0000\u0000\u0000"+
		"N\u01a6\u0001\u0000\u0000\u0000P\u01a8\u0001\u0000\u0000\u0000R\u01b6"+
		"\u0001\u0000\u0000\u0000T\u01b8\u0001\u0000\u0000\u0000V\u01bf\u0001\u0000"+
		"\u0000\u0000X\u01c1\u0001\u0000\u0000\u0000Z\u01c9\u0001\u0000\u0000\u0000"+
		"\\\u01ce\u0001\u0000\u0000\u0000^\u01dd\u0001\u0000\u0000\u0000`\u01df"+
		"\u0001\u0000\u0000\u0000b\u01e8\u0001\u0000\u0000\u0000d\u01eb\u0001\u0000"+
		"\u0000\u0000f\u01f3\u0001\u0000\u0000\u0000h\u01f9\u0001\u0000\u0000\u0000"+
		"j\u01fb\u0001\u0000\u0000\u0000l\u01fd\u0001\u0000\u0000\u0000n\u0200"+
		"\u0001\u0000\u0000\u0000p\u0203\u0001\u0000\u0000\u0000r\u0208\u0001\u0000"+
		"\u0000\u0000t\u020e\u0001\u0000\u0000\u0000v\u0214\u0001\u0000\u0000\u0000"+
		"x\u0216\u0001\u0000\u0000\u0000z\u0219\u0001\u0000\u0000\u0000|\u0248"+
		"\u0001\u0000\u0000\u0000~\u024a\u0001\u0000\u0000\u0000\u0080\u0250\u0001"+
		"\u0000\u0000\u0000\u0082\u0252\u0001\u0000\u0000\u0000\u0084\u025d\u0001"+
		"\u0000\u0000\u0000\u0086\u026d\u0001\u0000\u0000\u0000\u0088\u026f\u0001"+
		"\u0000\u0000\u0000\u008a\u0274\u0001\u0000\u0000\u0000\u008c\u0284\u0001"+
		"\u0000\u0000\u0000\u008e\u0289\u0001\u0000\u0000\u0000\u0090\u0291\u0001"+
		"\u0000\u0000\u0000\u0092\u0295\u0001\u0000\u0000\u0000\u0094\u02a0\u0001"+
		"\u0000\u0000\u0000\u0096\u02ad\u0001\u0000\u0000\u0000\u0098\u02b0\u0001"+
		"\u0000\u0000\u0000\u009a\u02b6\u0001\u0000\u0000\u0000\u009c\u02c6\u0001"+
		"\u0000\u0000\u0000\u009e\u02c8\u0001\u0000\u0000\u0000\u00a0\u02d0\u0001"+
		"\u0000\u0000\u0000\u00a2\u02d5\u0001\u0000\u0000\u0000\u00a4\u02e3\u0001"+
		"\u0000\u0000\u0000\u00a6\u02e5\u0001\u0000\u0000\u0000\u00a8\u02e8\u0001"+
		"\u0000\u0000\u0000\u00aa\u02ea\u0001\u0000\u0000\u0000\u00ac\u02ed\u0001"+
		"\u0000\u0000\u0000\u00ae\u02f2\u0001\u0000\u0000\u0000\u00b0\u02f4\u0001"+
		"\u0000\u0000\u0000\u00b2\u02f6\u0001\u0000\u0000\u0000\u00b4\u02f9\u0001"+
		"\u0000\u0000\u0000\u00b6\u02fd\u0001\u0000\u0000\u0000\u00b8\u02ff\u0001"+
		"\u0000\u0000\u0000\u00ba\u0301\u0001\u0000\u0000\u0000\u00bc\u00be\u0003"+
		"\u0006\u0003\u0000\u00bd\u00bc\u0001\u0000\u0000\u0000\u00be\u00c1\u0001"+
		"\u0000\u0000\u0000\u00bf\u00bd\u0001\u0000\u0000\u0000\u00bf\u00c0\u0001"+
		"\u0000\u0000\u0000\u00c0\u00c5\u0001\u0000\u0000\u0000\u00c1\u00bf\u0001"+
		"\u0000\u0000\u0000\u00c2\u00c4\u0003\u0002\u0001\u0000\u00c3\u00c2\u0001"+
		"\u0000\u0000\u0000\u00c4\u00c7\u0001\u0000\u0000\u0000\u00c5\u00c3\u0001"+
		"\u0000\u0000\u0000\u00c5\u00c6\u0001\u0000\u0000\u0000\u00c6\u00c8\u0001"+
		"\u0000\u0000\u0000\u00c7\u00c5\u0001\u0000\u0000\u0000\u00c8\u00c9\u0005"+
		"\u0000\u0000\u0001\u00c9\u0001\u0001\u0000\u0000\u0000\u00ca\u00ce\u0003"+
		"\u0004\u0002\u0000\u00cb\u00cd\u0003\u0006\u0003\u0000\u00cc\u00cb\u0001"+
		"\u0000\u0000\u0000\u00cd\u00d0\u0001\u0000\u0000\u0000\u00ce\u00cc\u0001"+
		"\u0000\u0000\u0000\u00ce\u00cf\u0001\u0000\u0000\u0000\u00cf\u0003\u0001"+
		"\u0000\u0000\u0000\u00d0\u00ce\u0001\u0000\u0000\u0000\u00d1\u00d2\u0005"+
		"\u0012\u0000\u0000\u00d2\u00d3\u0005e\u0000\u0000\u00d3\u0005\u0001\u0000"+
		"\u0000\u0000\u00d4\u00e8\u0003\u0082A\u0000\u00d5\u00e8\u0003n7\u0000"+
		"\u00d6\u00e8\u0003:\u001d\u0000\u00d7\u00e8\u0003\u0088D\u0000\u00d8\u00e8"+
		"\u0003l6\u0000\u00d9\u00e8\u0003t:\u0000\u00da\u00e8\u0003.\u0017\u0000"+
		"\u00db\u00e8\u0003\\.\u0000\u00dc\u00e8\u0003Z-\u0000\u00dd\u00e8\u0003"+
		"\u0010\b\u0000\u00de\u00e8\u0003\u0012\t\u0000\u00df\u00e8\u0003<\u001e"+
		"\u0000\u00e0\u00e8\u0003F#\u0000\u00e1\u00e8\u0003>\u001f\u0000\u00e2"+
		"\u00e8\u0003r9\u0000\u00e3\u00e8\u0003L&\u0000\u00e4\u00e8\u0003p8\u0000"+
		"\u00e5\u00e8\u0003\b\u0004\u0000\u00e6\u00e8\u0003\u0014\n\u0000\u00e7"+
		"\u00d4\u0001\u0000\u0000\u0000\u00e7\u00d5\u0001\u0000\u0000\u0000\u00e7"+
		"\u00d6\u0001\u0000\u0000\u0000\u00e7\u00d7\u0001\u0000\u0000\u0000\u00e7"+
		"\u00d8\u0001\u0000\u0000\u0000\u00e7\u00d9\u0001\u0000\u0000\u0000\u00e7"+
		"\u00da\u0001\u0000\u0000\u0000\u00e7\u00db\u0001\u0000\u0000\u0000\u00e7"+
		"\u00dc\u0001\u0000\u0000\u0000\u00e7\u00dd\u0001\u0000\u0000\u0000\u00e7"+
		"\u00de\u0001\u0000\u0000\u0000\u00e7\u00df\u0001\u0000\u0000\u0000\u00e7"+
		"\u00e0\u0001\u0000\u0000\u0000\u00e7\u00e1\u0001\u0000\u0000\u0000\u00e7"+
		"\u00e2\u0001\u0000\u0000\u0000\u00e7\u00e3\u0001\u0000\u0000\u0000\u00e7"+
		"\u00e4\u0001\u0000\u0000\u0000\u00e7\u00e5\u0001\u0000\u0000\u0000\u00e7"+
		"\u00e6\u0001\u0000\u0000\u0000\u00e8\u0007\u0001\u0000\u0000\u0000\u00e9"+
		"\u00ea\u0003\u0092I\u0000\u00ea\u00eb\u0005Z\u0000\u0000\u00eb\u00ec\u0003"+
		"\n\u0005\u0000\u00ec\u00ed\u0003\f\u0006\u0000\u00ed\t\u0001\u0000\u0000"+
		"\u0000\u00ee\u00ef\u0005e\u0000\u0000\u00ef\u000b\u0001\u0000\u0000\u0000"+
		"\u00f0\u00f2\u0003\u000e\u0007\u0000\u00f1\u00f0\u0001\u0000\u0000\u0000"+
		"\u00f2\u00f3\u0001\u0000\u0000\u0000\u00f3\u00f1\u0001\u0000\u0000\u0000"+
		"\u00f3\u00f4\u0001\u0000\u0000\u0000\u00f4\r\u0001\u0000\u0000\u0000\u00f5"+
		"\u00f9\u0007\u0000\u0000\u0000\u00f6\u00f8\u0003\u009cN\u0000\u00f7\u00f6"+
		"\u0001\u0000\u0000\u0000\u00f8\u00fb\u0001\u0000\u0000\u0000\u00f9\u00f7"+
		"\u0001\u0000\u0000\u0000\u00f9\u00fa\u0001\u0000\u0000\u0000\u00fa\u000f"+
		"\u0001\u0000\u0000\u0000\u00fb\u00f9\u0001\u0000\u0000\u0000\u00fc\u00fd"+
		"\u0005\u0003\u0000\u0000\u00fd\u0011\u0001\u0000\u0000\u0000\u00fe\u00ff"+
		"\u0005\u0004\u0000\u0000\u00ff\u0013\u0001\u0000\u0000\u0000\u0100\u0101"+
		"\u0005B\u0000\u0000\u0101\u0102\u0003\u0016\u000b\u0000\u0102\u0103\u0003"+
		"\u001c\u000e\u0000\u0103\u0104\u0003 \u0010\u0000\u0104\u0105\u0003$\u0012"+
		"\u0000\u0105\u0106\u0003(\u0014\u0000\u0106\u0015\u0001\u0000\u0000\u0000"+
		"\u0107\u0109\u0005\u001b\u0000\u0000\u0108\u010a\u0003\u0018\f\u0000\u0109"+
		"\u0108\u0001\u0000\u0000\u0000\u010a\u010b\u0001\u0000\u0000\u0000\u010b"+
		"\u0109\u0001\u0000\u0000\u0000\u010b\u010c\u0001\u0000\u0000\u0000\u010c"+
		"\u0017\u0001\u0000\u0000\u0000\u010d\u010e\u0003\u008aE\u0000\u010e\u010f"+
		"\u0005\u0013\u0000\u0000\u010f\u0110\u0003\u001a\r\u0000\u0110\u0019\u0001"+
		"\u0000\u0000\u0000\u0111\u0113\u0007\u0001\u0000\u0000\u0112\u0111\u0001"+
		"\u0000\u0000\u0000\u0113\u0114\u0001\u0000\u0000\u0000\u0114\u0112\u0001"+
		"\u0000\u0000\u0000\u0114\u0115\u0001\u0000\u0000\u0000\u0115\u001b\u0001"+
		"\u0000\u0000\u0000\u0116\u0118\u0005\u001c\u0000\u0000\u0117\u0119\u0003"+
		"\u001e\u000f\u0000\u0118\u0117\u0001\u0000\u0000\u0000\u0119\u011a\u0001"+
		"\u0000\u0000\u0000\u011a\u0118\u0001\u0000\u0000\u0000\u011a\u011b\u0001"+
		"\u0000\u0000\u0000\u011b\u001d\u0001\u0000\u0000\u0000\u011c\u011d\u0003"+
		"\u008aE\u0000\u011d\u011e\u0003\u0086C\u0000\u011e\u001f\u0001\u0000\u0000"+
		"\u0000\u011f\u0121\u0005\u001f\u0000\u0000\u0120\u0122\u0003\"\u0011\u0000"+
		"\u0121\u0120\u0001\u0000\u0000\u0000\u0122\u0123\u0001\u0000\u0000\u0000"+
		"\u0123\u0121\u0001\u0000\u0000\u0000\u0123\u0124\u0001\u0000\u0000\u0000"+
		"\u0124!\u0001\u0000\u0000\u0000\u0125\u0126\u0003\u008aE\u0000\u0126\u0127"+
		"\u0003\u0086C\u0000\u0127#\u0001\u0000\u0000\u0000\u0128\u012a\u0005\u001e"+
		"\u0000\u0000\u0129\u012b\u0003&\u0013\u0000\u012a\u0129\u0001\u0000\u0000"+
		"\u0000\u012b\u012c\u0001\u0000\u0000\u0000\u012c\u012a\u0001\u0000\u0000"+
		"\u0000\u012c\u012d\u0001\u0000\u0000\u0000\u012d%\u0001\u0000\u0000\u0000"+
		"\u012e\u0130\u0003\u008aE\u0000\u012f\u0131\u0003\u0086C\u0000\u0130\u012f"+
		"\u0001\u0000\u0000\u0000\u0130\u0131\u0001\u0000\u0000\u0000\u0131\'\u0001"+
		"\u0000\u0000\u0000\u0132\u0134\u0005\u001d\u0000\u0000\u0133\u0135\u0003"+
		"*\u0015\u0000\u0134\u0133\u0001\u0000\u0000\u0000\u0135\u0136\u0001\u0000"+
		"\u0000\u0000\u0136\u0134\u0001\u0000\u0000\u0000\u0136\u0137\u0001\u0000"+
		"\u0000\u0000\u0137)\u0001\u0000\u0000\u0000\u0138\u0139\u0003\u008aE\u0000"+
		"\u0139\u013a\u0005\u0013\u0000\u0000\u013a\u013b\u0003,\u0016\u0000\u013b"+
		"+\u0001\u0000\u0000\u0000\u013c\u0142\u0003\u008cF\u0000\u013d\u0142\u0003"+
		"\u009cN\u0000\u013e\u013f\u0005\f\u0000\u0000\u013f\u0140\u0005\u0002"+
		"\u0000\u0000\u0140\u0142\u0005\r\u0000\u0000\u0141\u013c\u0001\u0000\u0000"+
		"\u0000\u0141\u013d\u0001\u0000\u0000\u0000\u0141\u013e\u0001\u0000\u0000"+
		"\u0000\u0142-\u0001\u0000\u0000\u0000\u0143\u0146\u0005C\u0000\u0000\u0144"+
		"\u0147\u00030\u0018\u0000\u0145\u0147\u00032\u0019\u0000\u0146\u0144\u0001"+
		"\u0000\u0000\u0000\u0146\u0145\u0001\u0000\u0000\u0000\u0147/\u0001\u0000"+
		"\u0000\u0000\u0148\u0149\u0003\u0004\u0002\u0000\u01491\u0001\u0000\u0000"+
		"\u0000\u014a\u014d\u0003\u0092I\u0000\u014b\u014d\u0003\u0094J\u0000\u014c"+
		"\u014a\u0001\u0000\u0000\u0000\u014c\u014b\u0001\u0000\u0000\u0000\u014d"+
		"\u014e\u0001\u0000\u0000\u0000\u014e\u014c\u0001\u0000\u0000\u0000\u014e"+
		"\u014f\u0001\u0000\u0000\u0000\u014f\u0151\u0001\u0000\u0000\u0000\u0150"+
		"\u0152\u00038\u001c\u0000\u0151\u0150\u0001\u0000\u0000\u0000\u0151\u0152"+
		"\u0001\u0000\u0000\u0000\u0152\u0154\u0001\u0000\u0000\u0000\u0153\u0155"+
		"\u00034\u001a\u0000\u0154\u0153\u0001\u0000\u0000\u0000\u0154\u0155\u0001"+
		"\u0000\u0000\u0000\u01553\u0001\u0000\u0000\u0000\u0156\u0158\u00036\u001b"+
		"\u0000\u0157\u0156\u0001\u0000\u0000\u0000\u0158\u0159\u0001\u0000\u0000"+
		"\u0000\u0159\u0157\u0001\u0000\u0000\u0000\u0159\u015a\u0001\u0000\u0000"+
		"\u0000\u015a5\u0001\u0000\u0000\u0000\u015b\u0162\u0005e\u0000\u0000\u015c"+
		"\u0162\u0005\u0002\u0000\u0000\u015d\u015e\u0005U\u0000\u0000\u015e\u0162"+
		"\u0005\b\u0000\u0000\u015f\u0162\u0003\u009cN\u0000\u0160\u0162\u0003"+
		"T*\u0000\u0161\u015b\u0001\u0000\u0000\u0000\u0161\u015c\u0001\u0000\u0000"+
		"\u0000\u0161\u015d\u0001\u0000\u0000\u0000\u0161\u015f\u0001\u0000\u0000"+
		"\u0000\u0161\u0160\u0001\u0000\u0000\u0000\u01627\u0001\u0000\u0000\u0000"+
		"\u0163\u0164\u0005\u0001\u0000\u0000\u0164\u0165\u0005\b\u0000\u0000\u0165"+
		"\u0166\u0005\u0016\u0000\u0000\u0166\u0167\u0005\b\u0000\u0000\u01679"+
		"\u0001\u0000\u0000\u0000\u0168\u0169\u0005D\u0000\u0000\u0169\u016a\u0003"+
		"\u0092I\u0000\u016a;\u0001\u0000\u0000\u0000\u016b\u016c\u0005I\u0000"+
		"\u0000\u016c=\u0001\u0000\u0000\u0000\u016d\u016f\u0003@ \u0000\u016e"+
		"\u0170\u0003z=\u0000\u016f\u016e\u0001\u0000\u0000\u0000\u016f\u0170\u0001"+
		"\u0000\u0000\u0000\u0170\u0174\u0001\u0000\u0000\u0000\u0171\u0173\u0003"+
		"B!\u0000\u0172\u0171\u0001\u0000\u0000\u0000\u0173\u0176\u0001\u0000\u0000"+
		"\u0000\u0174\u0172\u0001\u0000\u0000\u0000\u0174\u0175\u0001\u0000\u0000"+
		"\u0000\u0175?\u0001\u0000\u0000\u0000\u0176\u0174\u0001\u0000\u0000\u0000"+
		"\u0177\u0178\u0005\u0005\u0000\u0000\u0178A\u0001\u0000\u0000\u0000\u0179"+
		"\u0182\u0005\b\u0000\u0000\u017a\u0182\u0003\u009cN\u0000\u017b\u0182"+
		"\u0005e\u0000\u0000\u017c\u0182\u0003\u0092I\u0000\u017d\u0182\u0005\u0002"+
		"\u0000\u0000\u017e\u0182\u0003\u00ba]\u0000\u017f\u0182\u0003D\"\u0000"+
		"\u0180\u0182\u0003T*\u0000\u0181\u0179\u0001\u0000\u0000\u0000\u0181\u017a"+
		"\u0001\u0000\u0000\u0000\u0181\u017b\u0001\u0000\u0000\u0000\u0181\u017c"+
		"\u0001\u0000\u0000\u0000\u0181\u017d\u0001\u0000\u0000\u0000\u0181\u017e"+
		"\u0001\u0000\u0000\u0000\u0181\u017f\u0001\u0000\u0000\u0000\u0181\u0180"+
		"\u0001\u0000\u0000\u0000\u0182C\u0001\u0000\u0000\u0000\u0183\u0186\u0003"+
		"\u0092I\u0000\u0184\u0186\u0003\u009cN\u0000\u0185\u0183\u0001\u0000\u0000"+
		"\u0000\u0185\u0184\u0001\u0000\u0000\u0000\u0186\u0187\u0001\u0000\u0000"+
		"\u0000\u0187\u018a\u0005a\u0000\u0000\u0188\u018b\u0003\u0092I\u0000\u0189"+
		"\u018b\u0003\u009cN\u0000\u018a\u0188\u0001\u0000\u0000\u0000\u018a\u0189"+
		"\u0001\u0000\u0000\u0000\u018bE\u0001\u0000\u0000\u0000\u018c\u018e\u0005"+
		"J\u0000\u0000\u018d\u018f\u0003H$\u0000\u018e\u018d\u0001\u0000\u0000"+
		"\u0000\u018e\u018f\u0001\u0000\u0000\u0000\u018f\u0191\u0001\u0000\u0000"+
		"\u0000\u0190\u0192\u0003J%\u0000\u0191\u0190\u0001\u0000\u0000\u0000\u0191"+
		"\u0192\u0001\u0000\u0000\u0000\u0192G\u0001\u0000\u0000\u0000\u0193\u0194"+
		"\u0005;\u0000\u0000\u0194I\u0001\u0000\u0000\u0000\u0195\u0198\u0005\b"+
		"\u0000\u0000\u0196\u0198\u0003\u009cN\u0000\u0197\u0195\u0001\u0000\u0000"+
		"\u0000\u0197\u0196\u0001\u0000\u0000\u0000\u0198K\u0001\u0000\u0000\u0000"+
		"\u0199\u019b\u0005R\u0000\u0000\u019a\u019c\u0003z=\u0000\u019b\u019a"+
		"\u0001\u0000\u0000\u0000\u019b\u019c\u0001\u0000\u0000\u0000\u019c\u019e"+
		"\u0001\u0000\u0000\u0000\u019d\u019f\u0003N\'\u0000\u019e\u019d\u0001"+
		"\u0000\u0000\u0000\u019e\u019f\u0001\u0000\u0000\u0000\u019f\u01a0\u0001"+
		"\u0000\u0000\u0000\u01a0\u01a1\u0003T*\u0000\u01a1\u01a2\u0005S\u0000"+
		"\u0000\u01a2\u01a3\u0003P(\u0000\u01a3\u01a4\u0005T\u0000\u0000\u01a4"+
		"\u01a5\u0003X,\u0000\u01a5M\u0001\u0000\u0000\u0000\u01a6\u01a7\u0005"+
		"\u0002\u0000\u0000\u01a7O\u0001\u0000\u0000\u0000\u01a8\u01aa\u0005\f"+
		"\u0000\u0000\u01a9\u01ab\u0003R)\u0000\u01aa\u01a9\u0001\u0000\u0000\u0000"+
		"\u01ab\u01ac\u0001\u0000\u0000\u0000\u01ac\u01aa\u0001\u0000\u0000\u0000"+
		"\u01ac\u01ad\u0001\u0000\u0000\u0000\u01ad\u01ae\u0001\u0000\u0000\u0000"+
		"\u01ae\u01af\u0005\r\u0000\u0000\u01afQ\u0001\u0000\u0000\u0000\u01b0"+
		"\u01b7\u0005\b\u0000\u0000\u01b1\u01b7\u0005\u0002\u0000\u0000\u01b2\u01b7"+
		"\u0003\u0092I\u0000\u01b3\u01b7\u0003\u0094J\u0000\u01b4\u01b7\u0003\u009c"+
		"N\u0000\u01b5\u01b7\u0003T*\u0000\u01b6\u01b0\u0001\u0000\u0000\u0000"+
		"\u01b6\u01b1\u0001\u0000\u0000\u0000\u01b6\u01b2\u0001\u0000\u0000\u0000"+
		"\u01b6\u01b3\u0001\u0000\u0000\u0000\u01b6\u01b4\u0001\u0000\u0000\u0000"+
		"\u01b6\u01b5\u0001\u0000\u0000\u0000\u01b7S\u0001\u0000\u0000\u0000\u01b8"+
		"\u01b9\u0005U\u0000\u0000\u01b9\u01bb\u0005U\u0000\u0000\u01ba\u01bc\u0003"+
		"V+\u0000\u01bb\u01ba\u0001\u0000\u0000\u0000\u01bb\u01bc\u0001\u0000\u0000"+
		"\u0000\u01bc\u01bd\u0001\u0000\u0000\u0000\u01bd\u01be\u0005e\u0000\u0000"+
		"\u01beU\u0001\u0000\u0000\u0000\u01bf\u01c0\u0005_\u0000\u0000\u01c0W"+
		"\u0001\u0000\u0000\u0000\u01c1\u01c3\u0005\f\u0000\u0000\u01c2\u01c4\u0003"+
		"\u0006\u0003\u0000\u01c3\u01c2\u0001\u0000\u0000\u0000\u01c4\u01c5\u0001"+
		"\u0000\u0000\u0000\u01c5\u01c3\u0001\u0000\u0000\u0000\u01c5\u01c6\u0001"+
		"\u0000\u0000\u0000\u01c6\u01c7\u0001\u0000\u0000\u0000\u01c7\u01c8\u0005"+
		"\r\u0000\u0000\u01c8Y\u0001\u0000\u0000\u0000\u01c9\u01cc\u0005L\u0000"+
		"\u0000\u01ca\u01cd\u0003\u0004\u0002\u0000\u01cb\u01cd\u0005e\u0000\u0000"+
		"\u01cc\u01ca\u0001\u0000\u0000\u0000\u01cc\u01cb\u0001\u0000\u0000\u0000"+
		"\u01cc\u01cd\u0001\u0000\u0000\u0000\u01cd[\u0001\u0000\u0000\u0000\u01ce"+
		"\u01cf\u0005K\u0000\u0000\u01cf\u01d0\u0003d2\u0000\u01d0\u01d2\u0003"+
		"^/\u0000\u01d1\u01d3\u0003`0\u0000\u01d2\u01d1\u0001\u0000\u0000\u0000"+
		"\u01d2\u01d3\u0001\u0000\u0000\u0000\u01d3]\u0001\u0000\u0000\u0000\u01d4"+
		"\u01d6\u0005\f\u0000\u0000\u01d5\u01d7\u0003\u0006\u0003\u0000\u01d6\u01d5"+
		"\u0001\u0000\u0000\u0000\u01d7\u01d8\u0001\u0000\u0000\u0000\u01d8\u01d6"+
		"\u0001\u0000\u0000\u0000\u01d8\u01d9\u0001\u0000\u0000\u0000\u01d9\u01da"+
		"\u0001\u0000\u0000\u0000\u01da\u01db\u0005\r\u0000\u0000\u01db\u01de\u0001"+
		"\u0000\u0000\u0000\u01dc\u01de\u0003\u0006\u0003\u0000\u01dd\u01d4\u0001"+
		"\u0000\u0000\u0000\u01dd\u01dc\u0001\u0000\u0000\u0000\u01de_\u0001\u0000"+
		"\u0000\u0000\u01df\u01e0\u0005E\u0000\u0000\u01e0\u01e2\u0005\f\u0000"+
		"\u0000\u01e1\u01e3\u0003\u0006\u0003\u0000\u01e2\u01e1\u0001\u0000\u0000"+
		"\u0000\u01e3\u01e4\u0001\u0000\u0000\u0000\u01e4\u01e2\u0001\u0000\u0000"+
		"\u0000\u01e4\u01e5\u0001\u0000\u0000\u0000\u01e5\u01e6\u0001\u0000\u0000"+
		"\u0000\u01e6\u01e7\u0005\r\u0000\u0000\u01e7a\u0001\u0000\u0000\u0000"+
		"\u01e8\u01e9\u0003\u0006\u0003\u0000\u01e9c\u0001\u0000\u0000\u0000\u01ea"+
		"\u01ec\u0003f3\u0000\u01eb\u01ea\u0001\u0000\u0000\u0000\u01eb\u01ec\u0001"+
		"\u0000\u0000\u0000\u01ec\u01ed\u0001\u0000\u0000\u0000\u01ed\u01ee\u0003"+
		"j5\u0000\u01ee\u01ef\u0003h4\u0000\u01efe\u0001\u0000\u0000\u0000\u01f0"+
		"\u01f4\u0005\u0002\u0000\u0000\u01f1\u01f4\u0003\u009cN\u0000\u01f2\u01f4"+
		"\u0005e\u0000\u0000\u01f3\u01f0\u0001\u0000\u0000\u0000\u01f3\u01f1\u0001"+
		"\u0000\u0000\u0000\u01f3\u01f2\u0001\u0000\u0000\u0000\u01f4g\u0001\u0000"+
		"\u0000\u0000\u01f5\u01fa\u0005\u0002\u0000\u0000\u01f6\u01fa\u0005\b\u0000"+
		"\u0000\u01f7\u01fa\u0005e\u0000\u0000\u01f8\u01fa\u0003\u009cN\u0000\u01f9"+
		"\u01f5\u0001\u0000\u0000\u0000\u01f9\u01f6\u0001\u0000\u0000\u0000\u01f9"+
		"\u01f7\u0001\u0000\u0000\u0000\u01f9\u01f8\u0001\u0000\u0000\u0000\u01fa"+
		"i\u0001\u0000\u0000\u0000\u01fb\u01fc\u0007\u0002\u0000\u0000\u01fck\u0001"+
		"\u0000\u0000\u0000\u01fd\u01fe\u0005W\u0000\u0000\u01fe\u01ff\u0003\u008c"+
		"F\u0000\u01ffm\u0001\u0000\u0000\u0000\u0200\u0201\u0005\u0010\u0000\u0000"+
		"\u0201\u0202\u0003\u0080@\u0000\u0202o\u0001\u0000\u0000\u0000\u0203\u0206"+
		"\u0005Y\u0000\u0000\u0204\u0207\u0003\u0092I\u0000\u0205\u0207\u0003\u0094"+
		"J\u0000\u0206\u0204\u0001\u0000\u0000\u0000\u0206\u0205\u0001\u0000\u0000"+
		"\u0000\u0207q\u0001\u0000\u0000\u0000\u0208\u020a\u0005Q\u0000\u0000\u0209"+
		"\u020b\u0003z=\u0000\u020a\u0209\u0001\u0000\u0000\u0000\u020a\u020b\u0001"+
		"\u0000\u0000\u0000\u020b\u020c\u0001\u0000\u0000\u0000\u020c\u020d\u0003"+
		"\u008cF\u0000\u020ds\u0001\u0000\u0000\u0000\u020e\u020f\u0005X\u0000"+
		"\u0000\u020f\u0210\u0003v;\u0000\u0210\u0212\u0003x<\u0000\u0211\u0213"+
		"\u0003z=\u0000\u0212\u0211\u0001\u0000\u0000\u0000\u0212\u0213\u0001\u0000"+
		"\u0000\u0000\u0213u\u0001\u0000\u0000\u0000\u0214\u0215\u0003\u008cF\u0000"+
		"\u0215w\u0001\u0000\u0000\u0000\u0216\u0217\u0003\u008cF\u0000\u0217y"+
		"\u0001\u0000\u0000\u0000\u0218\u021a\u0003|>\u0000\u0219\u0218\u0001\u0000"+
		"\u0000\u0000\u021a\u021b\u0001\u0000\u0000\u0000\u021b\u0219\u0001\u0000"+
		"\u0000\u0000\u021b\u021c\u0001\u0000\u0000\u0000\u021c{\u0001\u0000\u0000"+
		"\u0000\u021d\u0249\u0005#\u0000\u0000\u021e\u0249\u0005%\u0000\u0000\u021f"+
		"\u0249\u0005&\u0000\u0000\u0220\u0249\u0005$\u0000\u0000\u0221\u0249\u0005"+
		"(\u0000\u0000\u0222\u0249\u0005)\u0000\u0000\u0223\u0249\u0005*\u0000"+
		"\u0000\u0224\u0225\u0005+\u0000\u0000\u0225\u0226\u0005\u0012\u0000\u0000"+
		"\u0226\u0249\u0003~?\u0000\u0227\u0249\u0005,\u0000\u0000\u0228\u0249"+
		"\u0005-\u0000\u0000\u0229\u0249\u0005.\u0000\u0000\u022a\u0249\u0005/"+
		"\u0000\u0000\u022b\u0249\u00050\u0000\u0000\u022c\u0249\u00051\u0000\u0000"+
		"\u022d\u0249\u00052\u0000\u0000\u022e\u0249\u00053\u0000\u0000\u022f\u0249"+
		"\u00054\u0000\u0000\u0230\u0249\u00055\u0000\u0000\u0231\u0249\u00056"+
		"\u0000\u0000\u0232\u0249\u00057\u0000\u0000\u0233\u0249\u00058\u0000\u0000"+
		"\u0234\u0249\u00059\u0000\u0000\u0235\u0249\u0005:\u0000\u0000\u0236\u0249"+
		"\u0005;\u0000\u0000\u0237\u0249\u0005<\u0000\u0000\u0238\u0249\u0005="+
		"\u0000\u0000\u0239\u023a\u0005>\u0000\u0000\u023a\u023f\u0003\u0094J\u0000"+
		"\u023b\u023c\u0005a\u0000\u0000\u023c\u023e\u0003\u0094J\u0000\u023d\u023b"+
		"\u0001\u0000\u0000\u0000\u023e\u0241\u0001\u0000\u0000\u0000\u023f\u023d"+
		"\u0001\u0000\u0000\u0000\u023f\u0240\u0001\u0000\u0000\u0000\u0240\u0249"+
		"\u0001\u0000\u0000\u0000\u0241\u023f\u0001\u0000\u0000\u0000\u0242\u0249"+
		"\u00059\u0000\u0000\u0243\u0249\u0005:\u0000\u0000\u0244\u0249\u0005;"+
		"\u0000\u0000\u0245\u0249\u0005<\u0000\u0000\u0246\u0249\u0005\'\u0000"+
		"\u0000\u0247\u0249\u0005=\u0000\u0000\u0248\u021d\u0001\u0000\u0000\u0000"+
		"\u0248\u021e\u0001\u0000\u0000\u0000\u0248\u021f\u0001\u0000\u0000\u0000"+
		"\u0248\u0220\u0001\u0000\u0000\u0000\u0248\u0221\u0001\u0000\u0000\u0000"+
		"\u0248\u0222\u0001\u0000\u0000\u0000\u0248\u0223\u0001\u0000\u0000\u0000"+
		"\u0248\u0224\u0001\u0000\u0000\u0000\u0248\u0227\u0001\u0000\u0000\u0000"+
		"\u0248\u0228\u0001\u0000\u0000\u0000\u0248\u0229\u0001\u0000\u0000\u0000"+
		"\u0248\u022a\u0001\u0000\u0000\u0000\u0248\u022b\u0001\u0000\u0000\u0000"+
		"\u0248\u022c\u0001\u0000\u0000\u0000\u0248\u022d\u0001\u0000\u0000\u0000"+
		"\u0248\u022e\u0001\u0000\u0000\u0000\u0248\u022f\u0001\u0000\u0000\u0000"+
		"\u0248\u0230\u0001\u0000\u0000\u0000\u0248\u0231\u0001\u0000\u0000\u0000"+
		"\u0248\u0232\u0001\u0000\u0000\u0000\u0248\u0233\u0001\u0000\u0000\u0000"+
		"\u0248\u0234\u0001\u0000\u0000\u0000\u0248\u0235\u0001\u0000\u0000\u0000"+
		"\u0248\u0236\u0001\u0000\u0000\u0000\u0248\u0237\u0001\u0000\u0000\u0000"+
		"\u0248\u0238\u0001\u0000\u0000\u0000\u0248\u0239\u0001\u0000\u0000\u0000"+
		"\u0248\u0242\u0001\u0000\u0000\u0000\u0248\u0243\u0001\u0000\u0000\u0000"+
		"\u0248\u0244\u0001\u0000\u0000\u0000\u0248\u0245\u0001\u0000\u0000\u0000"+
		"\u0248\u0246\u0001\u0000\u0000\u0000\u0248\u0247\u0001\u0000\u0000\u0000"+
		"\u0249}\u0001\u0000\u0000\u0000\u024a\u024b\u0005\b\u0000\u0000\u024b"+
		"\u024c\u0005[\u0000\u0000\u024c\u024d\u0005\b\u0000\u0000\u024d\u024e"+
		"\u0005[\u0000\u0000\u024e\u024f\u0005\b\u0000\u0000\u024f\u007f\u0001"+
		"\u0000\u0000\u0000\u0250\u0251\u0007\u0003\u0000\u0000\u0251\u0081\u0001"+
		"\u0000\u0000\u0000\u0252\u0254\u0005\u000f\u0000\u0000\u0253\u0255\u0003"+
		"z=\u0000\u0254\u0253\u0001\u0000\u0000\u0000\u0254\u0255\u0001\u0000\u0000"+
		"\u0000\u0255\u0256\u0001\u0000\u0000\u0000\u0256\u0258\u0003\u008aE\u0000"+
		"\u0257\u0259\u0003\u0086C\u0000\u0258\u0257\u0001\u0000\u0000\u0000\u0258"+
		"\u0259\u0001\u0000\u0000\u0000\u0259\u025b\u0001\u0000\u0000\u0000\u025a"+
		"\u025c\u0003\u0084B\u0000\u025b\u025a\u0001\u0000\u0000\u0000\u025b\u025c"+
		"\u0001\u0000\u0000\u0000\u025c\u0083\u0001\u0000\u0000\u0000\u025d\u025e"+
		"\u0005\u0014\u0000\u0000\u025e\u025f\u0003\u008cF\u0000\u025f\u0085\u0001"+
		"\u0000\u0000\u0000\u0260\u0267\u0005\u0013\u0000\u0000\u0261\u0268\u0003"+
		"\u008cF\u0000\u0262\u0264\u0005f\u0000\u0000\u0263\u0262\u0001\u0000\u0000"+
		"\u0000\u0264\u0265\u0001\u0000\u0000\u0000\u0265\u0263\u0001\u0000\u0000"+
		"\u0000\u0265\u0266\u0001\u0000\u0000\u0000\u0266\u0268\u0001\u0000\u0000"+
		"\u0000\u0267\u0261\u0001\u0000\u0000\u0000\u0267\u0263\u0001\u0000\u0000"+
		"\u0000\u0267\u0268\u0001\u0000\u0000\u0000\u0268\u026e\u0001\u0000\u0000"+
		"\u0000\u0269\u026a\u0003\u0090H\u0000\u026a\u026b\u0005\u0013\u0000\u0000"+
		"\u026b\u026c\u0005\b\u0000\u0000\u026c\u026e\u0001\u0000\u0000\u0000\u026d"+
		"\u0260\u0001\u0000\u0000\u0000\u026d\u0269\u0001\u0000\u0000\u0000\u026e"+
		"\u0087\u0001\u0000\u0000\u0000\u026f\u0272\u0005P\u0000\u0000\u0270\u0271"+
		"\u0005]\u0000\u0000\u0271\u0273\u0005N\u0000\u0000\u0272\u0270\u0001\u0000"+
		"\u0000\u0000\u0272\u0273\u0001\u0000\u0000\u0000\u0273\u0089\u0001\u0000"+
		"\u0000\u0000\u0274\u0275\u0005e\u0000\u0000\u0275\u008b\u0001\u0000\u0000"+
		"\u0000\u0276\u0285\u0005\u0002\u0000\u0000\u0277\u0285\u0005e\u0000\u0000"+
		"\u0278\u027a\u0003\u009cN\u0000\u0279\u0278\u0001\u0000\u0000\u0000\u027a"+
		"\u027b\u0001\u0000\u0000\u0000\u027b\u0279\u0001\u0000\u0000\u0000\u027b"+
		"\u027c\u0001\u0000\u0000\u0000\u027c\u0285\u0001\u0000\u0000\u0000\u027d"+
		"\u0285\u0003\u0098L\u0000\u027e\u0285\u0003\u0092I\u0000\u027f\u0285\u0003"+
		"\u0094J\u0000\u0280\u0285\u0005c\u0000\u0000\u0281\u0285\u0003\u008eG"+
		"\u0000\u0282\u0285\u0005\b\u0000\u0000\u0283\u0285\u0003T*\u0000\u0284"+
		"\u0276\u0001\u0000\u0000\u0000\u0284\u0277\u0001\u0000\u0000\u0000\u0284"+
		"\u0279\u0001\u0000\u0000\u0000\u0284\u027d\u0001\u0000\u0000\u0000\u0284"+
		"\u027e\u0001\u0000\u0000\u0000\u0284\u027f\u0001\u0000\u0000\u0000\u0284"+
		"\u0280\u0001\u0000\u0000\u0000\u0284\u0281\u0001\u0000\u0000\u0000\u0284"+
		"\u0282\u0001\u0000\u0000\u0000\u0284\u0283\u0001\u0000\u0000\u0000\u0285"+
		"\u008d\u0001\u0000\u0000\u0000\u0286\u028a\u0005\b\u0000\u0000\u0287\u028a"+
		"\u0003\u009cN\u0000\u0288\u028a\u0005\u0002\u0000\u0000\u0289\u0286\u0001"+
		"\u0000\u0000\u0000\u0289\u0287\u0001\u0000\u0000\u0000\u0289\u0288\u0001"+
		"\u0000\u0000\u0000\u028a\u028b\u0001\u0000\u0000\u0000\u028b\u028f\u0003"+
		"\u0090H\u0000\u028c\u0290\u0005\b\u0000\u0000\u028d\u0290\u0003\u009c"+
		"N\u0000\u028e\u0290\u0005\u0002\u0000\u0000\u028f\u028c\u0001\u0000\u0000"+
		"\u0000\u028f\u028d\u0001\u0000\u0000\u0000\u028f\u028e\u0001\u0000\u0000"+
		"\u0000\u0290\u008f\u0001\u0000\u0000\u0000\u0291\u0292\u0007\u0004\u0000"+
		"\u0000\u0292\u0091\u0001\u0000\u0000\u0000\u0293\u0296\u0003\u0094J\u0000"+
		"\u0294\u0296\u0005A\u0000\u0000\u0295\u0293\u0001\u0000\u0000\u0000\u0295"+
		"\u0294\u0001\u0000\u0000\u0000\u0295\u0296\u0001\u0000\u0000\u0000\u0296"+
		"\u029b\u0001\u0000\u0000\u0000\u0297\u0299\u0005\u0018\u0000\u0000\u0298"+
		"\u029a\u0003\u0094J\u0000\u0299\u0298\u0001\u0000\u0000\u0000\u0299\u029a"+
		"\u0001\u0000\u0000\u0000\u029a\u029c\u0001\u0000\u0000\u0000\u029b\u0297"+
		"\u0001\u0000\u0000\u0000\u029c\u029d\u0001\u0000\u0000\u0000\u029d\u029b"+
		"\u0001\u0000\u0000\u0000\u029d\u029e\u0001\u0000\u0000\u0000\u029e\u0093"+
		"\u0001\u0000\u0000\u0000\u029f\u02a1\u0003\u0096K\u0000\u02a0\u029f\u0001"+
		"\u0000\u0000\u0000\u02a1\u02a2\u0001\u0000\u0000\u0000\u02a2\u02a0\u0001"+
		"\u0000\u0000\u0000\u02a2\u02a3\u0001\u0000\u0000\u0000\u02a3\u0095\u0001"+
		"\u0000\u0000\u0000\u02a4\u02ae\u0005e\u0000\u0000\u02a5\u02ae\u0005\\"+
		"\u0000\u0000\u02a6\u02ae\u0005?\u0000\u0000\u02a7\u02ae\u0005c\u0000\u0000"+
		"\u02a8\u02ae\u0003\u009cN\u0000\u02a9\u02ae\u0005b\u0000\u0000\u02aa\u02ae"+
		"\u0005`\u0000\u0000\u02ab\u02ae\u0005\u0017\u0000\u0000\u02ac\u02ae\u0005"+
		"H\u0000\u0000\u02ad\u02a4\u0001\u0000\u0000\u0000\u02ad\u02a5\u0001\u0000"+
		"\u0000\u0000\u02ad\u02a6\u0001\u0000\u0000\u0000\u02ad\u02a7\u0001\u0000"+
		"\u0000\u0000\u02ad\u02a8\u0001\u0000\u0000\u0000\u02ad\u02a9\u0001\u0000"+
		"\u0000\u0000\u02ad\u02aa\u0001\u0000\u0000\u0000\u02ad\u02ab\u0001\u0000"+
		"\u0000\u0000\u02ad\u02ac\u0001\u0000\u0000\u0000\u02ae\u0097\u0001\u0000"+
		"\u0000\u0000\u02af\u02b1\u0003\u009aM\u0000\u02b0\u02af\u0001\u0000\u0000"+
		"\u0000\u02b1\u02b2\u0001\u0000\u0000\u0000\u02b2\u02b0\u0001\u0000\u0000"+
		"\u0000\u02b2\u02b3\u0001\u0000\u0000\u0000\u02b3\u0099\u0001\u0000\u0000"+
		"\u0000\u02b4\u02b7\u0005e\u0000\u0000\u02b5\u02b7\u0003\u009cN\u0000\u02b6"+
		"\u02b4\u0001\u0000\u0000\u0000\u02b6\u02b5\u0001\u0000\u0000\u0000\u02b7"+
		"\u009b\u0001\u0000\u0000\u0000\u02b8\u02b9\u0005U\u0000\u0000\u02b9\u02bb"+
		"\u0003\u008aE\u0000\u02ba\u02bc\u0003\u009eO\u0000\u02bb\u02ba\u0001\u0000"+
		"\u0000\u0000\u02bb\u02bc\u0001\u0000\u0000\u0000\u02bc\u02bd\u0001\u0000"+
		"\u0000\u0000\u02bd\u02be\u0005U\u0000\u0000\u02be\u02c7\u0001\u0000\u0000"+
		"\u0000\u02bf\u02c0\u0005V\u0000\u0000\u02c0\u02c2\u0003\u008aE\u0000\u02c1"+
		"\u02c3\u0003\u009eO\u0000\u02c2\u02c1\u0001\u0000\u0000\u0000\u02c2\u02c3"+
		"\u0001\u0000\u0000\u0000\u02c3\u02c4\u0001\u0000\u0000\u0000\u02c4\u02c5"+
		"\u0005V\u0000\u0000\u02c5\u02c7\u0001\u0000\u0000\u0000\u02c6\u02b8\u0001"+
		"\u0000\u0000\u0000\u02c6\u02bf\u0001\u0000\u0000\u0000\u02c7\u009d\u0001"+
		"\u0000\u0000\u0000\u02c8\u02ce\u0005\u0012\u0000\u0000\u02c9\u02cf\u0003"+
		"\u00a0P\u0000\u02ca\u02cf\u0003\u00a2Q\u0000\u02cb\u02cf\u0003\u00a6S"+
		"\u0000\u02cc\u02cf\u0003\u00aaU\u0000\u02cd\u02cf\u0003\u00acV\u0000\u02ce"+
		"\u02c9\u0001\u0000\u0000\u0000\u02ce\u02ca\u0001\u0000\u0000\u0000\u02ce"+
		"\u02cb\u0001\u0000\u0000\u0000\u02ce\u02cc\u0001\u0000\u0000\u0000\u02ce"+
		"\u02cd\u0001\u0000\u0000\u0000\u02cf\u009f\u0001\u0000\u0000\u0000\u02d0"+
		"\u02d1\u0005^\u0000\u0000\u02d1\u02d2\u0003\u00b2Y\u0000\u02d2\u02d3\u0005"+
		"`\u0000\u0000\u02d3\u02d4\u0003\u00b4Z\u0000\u02d4\u00a1\u0001\u0000\u0000"+
		"\u0000\u02d5\u02d6\u0005^\u0000\u0000\u02d6\u02d7\u0005[\u0000\u0000\u02d7"+
		"\u02d8\u0003\u00b4Z\u0000\u02d8\u00a3\u0001\u0000\u0000\u0000\u02d9\u02db"+
		"\u0005f\u0000\u0000\u02da\u02d9\u0001\u0000\u0000\u0000\u02db\u02dc\u0001"+
		"\u0000\u0000\u0000\u02dc\u02da\u0001\u0000\u0000\u0000\u02dc\u02dd\u0001"+
		"\u0000\u0000\u0000\u02dd\u02e4\u0001\u0000\u0000\u0000\u02de\u02e4\u0005"+
		"\t\u0000\u0000\u02df\u02e4\u0005\u0012\u0000\u0000\u02e0\u02e4\u0005e"+
		"\u0000\u0000\u02e1\u02e4\u0005?\u0000\u0000\u02e2\u02e4\u0005\b\u0000"+
		"\u0000\u02e3\u02da\u0001\u0000\u0000\u0000\u02e3\u02de\u0001\u0000\u0000"+
		"\u0000\u02e3\u02df\u0001\u0000\u0000\u0000\u02e3\u02e0\u0001\u0000\u0000"+
		"\u0000\u02e3\u02e1\u0001\u0000\u0000\u0000\u02e3\u02e2\u0001\u0000\u0000"+
		"\u0000\u02e4\u00a5\u0001\u0000\u0000\u0000\u02e5\u02e6\u0003\u00a8T\u0000"+
		"\u02e6\u02e7\u0005\u0013\u0000\u0000\u02e7\u00a7\u0001\u0000\u0000\u0000"+
		"\u02e8\u02e9\u0003\u00a4R\u0000\u02e9\u00a9\u0001\u0000\u0000\u0000\u02ea"+
		"\u02eb\u0005\u0013\u0000\u0000\u02eb\u00ab\u0001\u0000\u0000\u0000\u02ec"+
		"\u02ee\u0003\u00aeW\u0000\u02ed\u02ec\u0001\u0000\u0000\u0000\u02ed\u02ee"+
		"\u0001\u0000\u0000\u0000\u02ee\u02ef\u0001\u0000\u0000\u0000\u02ef\u02f0"+
		"\u0005\u0013\u0000\u0000\u02f0\u02f1\u0003\u00b0X\u0000\u02f1\u00ad\u0001"+
		"\u0000\u0000\u0000\u02f2\u02f3\u0003\u00a4R\u0000\u02f3\u00af\u0001\u0000"+
		"\u0000\u0000\u02f4\u02f5\u0003\u00a4R\u0000\u02f5\u00b1\u0001\u0000\u0000"+
		"\u0000\u02f6\u02f7\u0005\b\u0000\u0000\u02f7\u00b3\u0001\u0000\u0000\u0000"+
		"\u02f8\u02fa\u0005[\u0000\u0000\u02f9\u02f8\u0001\u0000\u0000\u0000\u02f9"+
		"\u02fa\u0001\u0000\u0000\u0000\u02fa\u02fb\u0001\u0000\u0000\u0000\u02fb"+
		"\u02fc\u0005\b\u0000\u0000\u02fc\u00b5\u0001\u0000\u0000\u0000\u02fd\u02fe"+
		"\u0005\b\u0000\u0000\u02fe\u00b7\u0001\u0000\u0000\u0000\u02ff\u0300\u0005"+
		"\b\u0000\u0000\u0300\u00b9\u0001\u0000\u0000\u0000\u0301\u0302\u0005\u0002"+
		"\u0000\u0000\u0302\u0303\u0005a\u0000\u0000\u0303\u0304\u0005\u0002\u0000"+
		"\u0000\u0304\u00bb\u0001\u0000\u0000\u0000K\u00bf\u00c5\u00ce\u00e7\u00f3"+
		"\u00f9\u010b\u0114\u011a\u0123\u012c\u0130\u0136\u0141\u0146\u014c\u014e"+
		"\u0151\u0154\u0159\u0161\u016f\u0174\u0181\u0185\u018a\u018e\u0191\u0197"+
		"\u019b\u019e\u01ac\u01b6\u01bb\u01c5\u01cc\u01d2\u01d8\u01dd\u01e4\u01eb"+
		"\u01f3\u01f9\u0206\u020a\u0212\u021b\u023f\u0248\u0254\u0258\u025b\u0265"+
		"\u0267\u026d\u0272\u027b\u0284\u0289\u028f\u0295\u0299\u029d\u02a2\u02ad"+
		"\u02b2\u02b6\u02bb\u02c2\u02c6\u02ce\u02dc\u02e3\u02ed\u02f9";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}