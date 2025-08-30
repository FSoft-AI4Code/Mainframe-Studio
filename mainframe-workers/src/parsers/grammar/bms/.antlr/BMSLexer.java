// Generated from /home/minhnl11aic/Documents/mainframe-workers/src/parsers/grammar/bms/BMS.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class BMSLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, IDENTIFIER=13, STRING=14, STRING2=15, NUMBER=16, 
		WS=17, LineComment=18;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "T__10", "T__11", "IDENTIFIER", "STRING", "STRING2", "NUMBER", 
			"WS", "LineComment"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'END'", "'DFHPSD'", "'DFHPDI'", "'DFHMSD'", "'DFHMDI'", "'DFHMDF'", 
			"'TYPE'", "','", "'='", "'('", "')'", "'FINAL'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, "IDENTIFIER", "STRING", "STRING2", "NUMBER", "WS", "LineComment"
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


	public BMSLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "BMS.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0012\u0090\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001"+
		"\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\f\u0003\fa\b\f\u0001\f\u0001\f\u0005\f"+
		"e\b\f\n\f\f\fh\t\f\u0001\r\u0001\r\u0005\rl\b\r\n\r\f\ro\t\r\u0001\r\u0001"+
		"\r\u0001\u000e\u0001\u000e\u0005\u000eu\b\u000e\n\u000e\f\u000ex\t\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000f\u0004\u000f}\b\u000f\u000b\u000f"+
		"\f\u000f~\u0001\u0010\u0004\u0010\u0082\b\u0010\u000b\u0010\f\u0010\u0083"+
		"\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0005\u0011\u008a\b\u0011"+
		"\n\u0011\f\u0011\u008d\t\u0011\u0001\u0011\u0001\u0011\u0002mv\u0000\u0012"+
		"\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r"+
		"\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e"+
		"\u001d\u000f\u001f\u0010!\u0011#\u0012\u0001\u0000\u0006\u0001\u0000&"+
		"&\u0003\u000009AZaz\u0005\u0000##--09AZaz\u0001\u000009\u0003\u0000\t"+
		"\n\r\r  \u0002\u0000\n\n\r\r\u0096\u0000\u0001\u0001\u0000\u0000\u0000"+
		"\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000"+
		"\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000"+
		"\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f"+
		"\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013"+
		"\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017"+
		"\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b"+
		"\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f"+
		"\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000"+
		"\u0000\u0000\u0001%\u0001\u0000\u0000\u0000\u0003)\u0001\u0000\u0000\u0000"+
		"\u00050\u0001\u0000\u0000\u0000\u00077\u0001\u0000\u0000\u0000\t>\u0001"+
		"\u0000\u0000\u0000\u000bE\u0001\u0000\u0000\u0000\rL\u0001\u0000\u0000"+
		"\u0000\u000fQ\u0001\u0000\u0000\u0000\u0011S\u0001\u0000\u0000\u0000\u0013"+
		"U\u0001\u0000\u0000\u0000\u0015W\u0001\u0000\u0000\u0000\u0017Y\u0001"+
		"\u0000\u0000\u0000\u0019`\u0001\u0000\u0000\u0000\u001bi\u0001\u0000\u0000"+
		"\u0000\u001dr\u0001\u0000\u0000\u0000\u001f|\u0001\u0000\u0000\u0000!"+
		"\u0081\u0001\u0000\u0000\u0000#\u0087\u0001\u0000\u0000\u0000%&\u0005"+
		"E\u0000\u0000&\'\u0005N\u0000\u0000\'(\u0005D\u0000\u0000(\u0002\u0001"+
		"\u0000\u0000\u0000)*\u0005D\u0000\u0000*+\u0005F\u0000\u0000+,\u0005H"+
		"\u0000\u0000,-\u0005P\u0000\u0000-.\u0005S\u0000\u0000./\u0005D\u0000"+
		"\u0000/\u0004\u0001\u0000\u0000\u000001\u0005D\u0000\u000012\u0005F\u0000"+
		"\u000023\u0005H\u0000\u000034\u0005P\u0000\u000045\u0005D\u0000\u0000"+
		"56\u0005I\u0000\u00006\u0006\u0001\u0000\u0000\u000078\u0005D\u0000\u0000"+
		"89\u0005F\u0000\u00009:\u0005H\u0000\u0000:;\u0005M\u0000\u0000;<\u0005"+
		"S\u0000\u0000<=\u0005D\u0000\u0000=\b\u0001\u0000\u0000\u0000>?\u0005"+
		"D\u0000\u0000?@\u0005F\u0000\u0000@A\u0005H\u0000\u0000AB\u0005M\u0000"+
		"\u0000BC\u0005D\u0000\u0000CD\u0005I\u0000\u0000D\n\u0001\u0000\u0000"+
		"\u0000EF\u0005D\u0000\u0000FG\u0005F\u0000\u0000GH\u0005H\u0000\u0000"+
		"HI\u0005M\u0000\u0000IJ\u0005D\u0000\u0000JK\u0005F\u0000\u0000K\f\u0001"+
		"\u0000\u0000\u0000LM\u0005T\u0000\u0000MN\u0005Y\u0000\u0000NO\u0005P"+
		"\u0000\u0000OP\u0005E\u0000\u0000P\u000e\u0001\u0000\u0000\u0000QR\u0005"+
		",\u0000\u0000R\u0010\u0001\u0000\u0000\u0000ST\u0005=\u0000\u0000T\u0012"+
		"\u0001\u0000\u0000\u0000UV\u0005(\u0000\u0000V\u0014\u0001\u0000\u0000"+
		"\u0000WX\u0005)\u0000\u0000X\u0016\u0001\u0000\u0000\u0000YZ\u0005F\u0000"+
		"\u0000Z[\u0005I\u0000\u0000[\\\u0005N\u0000\u0000\\]\u0005A\u0000\u0000"+
		"]^\u0005L\u0000\u0000^\u0018\u0001\u0000\u0000\u0000_a\u0007\u0000\u0000"+
		"\u0000`_\u0001\u0000\u0000\u0000`a\u0001\u0000\u0000\u0000ab\u0001\u0000"+
		"\u0000\u0000bf\u0007\u0001\u0000\u0000ce\u0007\u0002\u0000\u0000dc\u0001"+
		"\u0000\u0000\u0000eh\u0001\u0000\u0000\u0000fd\u0001\u0000\u0000\u0000"+
		"fg\u0001\u0000\u0000\u0000g\u001a\u0001\u0000\u0000\u0000hf\u0001\u0000"+
		"\u0000\u0000im\u0005\"\u0000\u0000jl\t\u0000\u0000\u0000kj\u0001\u0000"+
		"\u0000\u0000lo\u0001\u0000\u0000\u0000mn\u0001\u0000\u0000\u0000mk\u0001"+
		"\u0000\u0000\u0000np\u0001\u0000\u0000\u0000om\u0001\u0000\u0000\u0000"+
		"pq\u0005\"\u0000\u0000q\u001c\u0001\u0000\u0000\u0000rv\u0005\'\u0000"+
		"\u0000su\t\u0000\u0000\u0000ts\u0001\u0000\u0000\u0000ux\u0001\u0000\u0000"+
		"\u0000vw\u0001\u0000\u0000\u0000vt\u0001\u0000\u0000\u0000wy\u0001\u0000"+
		"\u0000\u0000xv\u0001\u0000\u0000\u0000yz\u0005\'\u0000\u0000z\u001e\u0001"+
		"\u0000\u0000\u0000{}\u0007\u0003\u0000\u0000|{\u0001\u0000\u0000\u0000"+
		"}~\u0001\u0000\u0000\u0000~|\u0001\u0000\u0000\u0000~\u007f\u0001\u0000"+
		"\u0000\u0000\u007f \u0001\u0000\u0000\u0000\u0080\u0082\u0007\u0004\u0000"+
		"\u0000\u0081\u0080\u0001\u0000\u0000\u0000\u0082\u0083\u0001\u0000\u0000"+
		"\u0000\u0083\u0081\u0001\u0000\u0000\u0000\u0083\u0084\u0001\u0000\u0000"+
		"\u0000\u0084\u0085\u0001\u0000\u0000\u0000\u0085\u0086\u0006\u0010\u0000"+
		"\u0000\u0086\"\u0001\u0000\u0000\u0000\u0087\u008b\u0005*\u0000\u0000"+
		"\u0088\u008a\b\u0005\u0000\u0000\u0089\u0088\u0001\u0000\u0000\u0000\u008a"+
		"\u008d\u0001\u0000\u0000\u0000\u008b\u0089\u0001\u0000\u0000\u0000\u008b"+
		"\u008c\u0001\u0000\u0000\u0000\u008c\u008e\u0001\u0000\u0000\u0000\u008d"+
		"\u008b\u0001\u0000\u0000\u0000\u008e\u008f\u0006\u0011\u0001\u0000\u008f"+
		"$\u0001\u0000\u0000\u0000\b\u0000`fmv~\u0083\u008b\u0002\u0006\u0000\u0000"+
		"\u0000\u0001\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}