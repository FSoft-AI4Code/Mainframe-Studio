grammar Panel;


startRule: section+ EOF;

section: attributeSection | bodySection | initSection | procSection | endSection | modelSection | reinitSection;

reinitSection: RPAREN REINIT statement*;

modelSection: RPAREN MODEL modelParam* model+;

modelParam: IDENTIFIER ;

model: (IDENTIFIER | attrChar | charDataKeyword)+;
//////////////// attributeSection
attributeSection: RPAREN ATTR defaultParam? formatParam? attributeComponent+;



attributeComponent: attrChar attrParameter+;

attrParameter: typeParam | intensParam | colorParam | hiliteParam | skipParam | padParam | capsParam | extendParam | areaParam | scrollParam | justParam | formatParam | padcParam | outlineParam;

outlineParam: OUTLINE LPAREN outlineValue RPAREN;

outlineValue: NONE | BOX | IDENTIFIER+;

padcParam: PADC LPAREN padcValue RPAREN;

padcValue: INTEGERLITERAL | NULLS | USER | STRINGLITERAL;


justParam: JUST LPAREN justValue RPAREN;
justValue: LEFT | RIGHT | AXIS;

areaParam: AREA LPAREN areaValue RPAREN;
areaValue: DYNAMIC | GRAPHIC | SCRL;

scrollParam: SCROLL LPAREN scrollValue RPAREN;

scrollValue: ON | OFF ;

extendParam: EXTEND LPAREN extendValue RPAREN;
extendValue: ON | OFF;

capsParam: CAPS LPAREN capsValue RPAREN;
capsValue: ON | OFF | IN | OUT;

padParam: PAD LPAREN padValue RPAREN;

padValue: INTEGERLITERAL | NULLS | USER | STRINGLITERAL;

skipParam: SKIP_ LPAREN skipValue RPAREN;

skipValue: ON | OFF;


typeParam: TYPE LPAREN value RPAREN;

intensParam: INTENS LPAREN intensValue RPAREN;

intensValue: HIGH | LOW | NON;

colorParam: COLOR LPAREN value RPAREN;

hiliteParam: HILITE LPAREN value RPAREN;

attrChar: SSLASH | JP_MYSTERYCHAR | AMPCHAR | EXCLAIMCHAR | DOLLARCHAR | JP_CHAR | PLUSCHAR | HASHCHAR | LBRACKET | RBRACKET | DOUBLEQUOTE | UNDERSCORE | ASTERISK | SLASH | PIPECHAR | SINGLEQUOTE | GREATERTHAN | LESSTHAN | CARET;


/////////////// bodySection

bodySection: RPAREN BODY bodyParam*;

bodyParam: kanaParam | windowParam | defaultParam | formatParam | widthPara;

kanaParam: KANA;

windowParam: WINDOW LPAREN width COMMACHAR? length RPAREN;

width: INTEGERLITERAL;

length: INTEGERLITERAL;

widthPara: WIDTH LPAREN width RPAREN;

// bodyText: BODYTEXT;

//////////////////// statement

statement: 
    assignStatement
    | vputStatement
    | ifStatement
    | verStatement
    | vgetStatement
    | refreshStatement
;

refreshStatement: REFRESH LPAREN variable RPAREN;

ifStatement: IF condition thenIf elseIf?;
condition
    : combinableCondition andOrCondition*
    ;

andOrCondition
    : (AND | OR ) (combinableCondition | INTEGERLITERAL)
    ;

combinableCondition
    : NOT? simpleCondition
    ;

simpleCondition
    : LPAREN condition RPAREN
    | relationCondition

    ;



relationCondition
    : relationArithmeticComparison

    ;

relationArithmeticComparison
    : (arithmeticExpression relationalOperator)? (arithmeticExpression) (COMMACHAR arithmeticExpression)*
    ;

arithmeticExpression
    : value
    ;

relationalOperator: EQUALCHAR;


thenIf: statement | verStatement+;

verStatement: VER LPAREN variable COMMACHAR verCriteria (COMMACHAR verCriteria)* (COMMACHAR verMsg)? RPAREN;

verMsg: MSG EQUALCHAR value;

verCriteria
    : simpleCriteria
    | lengthCriteria
    | listCriteria
    | pictCriteria
    | rangeCriteria
    ;

simpleCriteria
    : NONBLANK
    | ALPHA
    | ALPHAB
    | BIT
    | DBCS
    | DSNAME
    | DSNAMEF
    | DSNAMEFM
    | DSNAMEPQ
    | DSNAMEQ
    | EBCDIC
    | ENUM
    | FILEID
    | HEX
    | IDATE
    | INCLUDE
    | IPADDR4
    | ITIME
    | JDATE
    | JSTD
    | MIX
    | NAME
    | NAMEF
    | NUM
    | STDDATE
    | STDTIME
    ;

lengthCriteria
    : LEN ',' relationalOperator ',' expectedLength
    ;

listCriteria
    : LIST ',' value (COMMACHAR value)*
    | LISTV ',' varlist
    | LISTVX ',' varlist
    | LISTX ',' value
    ;

pictCriteria
    : PICT ',' picValue
    | PICTCN ',' maskCharacter ',' fieldMask ',' stringValue
    ;

picValue: IDENTIFIER | STRINGLITERAL;

rangeCriteria
    : RANGE ',' lower ',' upper
    ;


expectedLength
    : INTEGERLITERAL     // or whatever your lexer rule is for numeric values
    ;

stringValue
    : STRINGLITERAL  // assumed lexer rule for quoted strings
    ;

varlist
    : IDENTIFIER (',' IDENTIFIER)*   // if var names are identifiers
    ;

maskCharacter
    : IDENTIFIER    // assumed lexer rule for single character
    ;

fieldMask
    : STRINGLITERAL  // or a custom rule if mask format is unique
    ;

lower
    : value
    ;

upper
    : value
    ;


elseIf: ELSE statement?;
assignStatement: variable assignPart;

variable: IDENTIFIER;
assignPart: EQUALCHAR value;

vgetStatement: VGET name_list vgetParameter*;
vputStatement: VPUT name_list vputParameter*;

name_list: IDENTIFIER | LPAREN name_list_item+ RPAREN | LPAREN name_list_item (COMMACHAR name_list_item)* RPAREN;

name_list_item: value;

vgetParameter: value;
vputParameter: value;
//////////////////// initSection

initSection: RPAREN INIT statement*;

/////////////////// procSection

procSection: RPAREN PROC statement*;
////////////////// endSection

defaultParam: DEFAULT LPAREN defValue+ RPAREN;
//////////////////////////////////////////////////////
defValue: attrChar;

formatParam: FORMAT LPAREN formatValue RPAREN;

formatValue: EBCDIC | DBCS | MIX;

endSection: RPAREN END;

panelFunction: transFunc | truncFunc | lvlineFunc | pfkFunc;

pfkFunc: PFK LPAREN pfkParam (COMMACHAR pfkParam)* RPAREN;

pfkParam: IDENTIFIER | END;

lvlineFunc: LVLINE LPAREN lvlineParam (COMMACHAR lvlineParam)* RPAREN;

lvlineParam: IDENTIFIER;

stringExpression: STRINGLITERAL | variable;

integerExpression: INTEGERLITERAL | variable;

truncFunc: TRUNC LPAREN stringToTrunc COMMACHAR (indexToTrunc | subStringToTrunc) RPAREN;

stringToTrunc: stringExpression;
indexToTrunc: integerExpression;
subStringToTrunc: stringExpression;



transFunc: TRANS LPAREN variable_to_trans transParam* RPAREN;
variable_to_trans: variable;
transParam: transVariable COMMACHAR transReturn;

transVariable: value;

transReturn: value;

value: IDENTIFIER | stringExpression |panelFunction | integerExpression | ASTERISK | variable | charDataKeyword;


charDataKeyword: MSG | TYPE | USER | NAME;
LPAREN: '(';
RPAREN: ')';
SSLASH: '\\';
SLASH: '/';
AMPCHAR: '@';
EXCLAIMCHAR: '!';
DOLLARCHAR: '$';
JP_MYSTERYCHAR: '?';
COMMACHAR: ',';
EQUALCHAR: '=';
ASTERISK: '*';
PLUSCHAR: '+';
HASHCHAR: '#';
DOUBLEQUOTE: '"';
UNDERSCORE: '_';
PIPECHAR: '|';
RBRACKET: ']';
LBRACKET: '[';
SINGLEQUOTE: '\'';
GREATERTHAN: '>';
LESSTHAN: '<';
CARET: '^';



ATTR: A T T R;
BODY: B O D Y;
COLOR: C O L O R;
DEFAULT: D E F A U L T;
FORMAT: F O R M A T;
HIGH: H I G H;
EBCDIC: E B C D I C;
DBCS: D B C S;
MIX: M I X;
HILITE: H I L I T E;
INTENS: I N T E N S;
LOW: L O W;
NON: N O N;
TRUNC: T R U N C;
TYPE: T Y P E;
KANA: K A N A;
WINDOW: W I N D O W;
INIT: I N I T;
VGET: V G E T;
VPUT: V P U T;
PROC: P R O C;
END : E N D;
MSG: M S G;
THEN: T H E N;
IF: I F;
AND: A N D;
OR: O R;
NOT: N O T;
ELSE: E L S E;
TRANS: T R A N S;
SKIP_: S K I P;
ON: O N;
OFF: O F F;
VER: V E R;
NONBLANK: N O N B L A N K | N B;
ALPHA: A L P H A;
ALPHAB: A L P H A B;
BIT: B I T;
DSNAME: D S N A M E;
DSNAMEF: D S N A M E F;
DSNAMEFM: D S N A M E F M;
DSNAMEPQ: D S N A M E P Q;
DSNAMEQ: D S N A M E Q;
ENUM: E N U M;
FILEID: F I L E I D;
HEX: H E X;
IDATE: I D A T E;
INCLUDE: I N C L U D E;
IPADDR4: I P A D D R '4';
ITIME: I T I M E;
JDATE: J D A T E;
JSTD: J S T D;
LEN: L E N;
LIST: L I S T;
LISTV: L I S T V;
LISTVX: L I S T V X;
LISTX: L I S T X;
NAME: N A M E;
NAMEF: N A M E F;
NUM: N U M;
PICT: P I C T;
PICTCN: P I C T C N;
RANGE: R A N G E;
STDDATE: S T D D A T E;
STDTIME: S T D T I M E;
PAD: P A D;
NULLS: N U L L S;
USER: U S E R;
EXTEND: E X T E N D;
CAPS: C A P S;
IN: I N;
OUT: O U T;
WIDTH: W I D T H;
SCRL: S C R L;
AREA: A R E A;
DYNAMIC: D Y N A M I C;
GRAPHIC: G R A P H I C;
SCROLL: S C R O L L;
LVLINE: L V L I N E;
LEFT: L E F T;
// CENTER: C E N T E R;
RIGHT: R I G H T;
AXIS: A X I S;
JUST: J U S T;
MODEL: M O D E L;
REINIT: R E I N I T;
PADC: P A D C;
REFRESH: R E F R E S H;
OUTLINE: O U T L I N E;
NONE: N O N E;
BOX: B O X;
PFK: P F K;


NEWLINE
    : '\r'? '\n' -> channel(HIDDEN)
    ;


WS
    : [ \t\f;]+ -> channel(HIDDEN)
    ;

// SEPARATOR
//     : ',\n' -> channel(HIDDEN)
//     ;
// SEPARATOR_2: ',' WS? NEWLINE -> channel(HIDDEN);
INTEGERLITERAL: [0-9]+ 
// ('.' [0-9]+)? | '.' [0-9]+
;
COMMENT: '/*' ~[\n\r]* '*/' -> channel(HIDDEN);
COMMENT2: '/*' ~[\n\r]* -> channel(HIDDEN);
IDENTIFIER
    : [a-zA-Z0-9\\.&#]+ ([-_/]+ [a-zA-Z0-9#@]+)*
    ;
STRINGLITERAL: '\'' ~[\r\n']* '\'';

JP_CHAR: HIRAGANA | KATAKANA | KANJI_ | FULLWIDTH_ROMAJI | FULLWIDTH_SPACE | '\u2020' | '\u02dd'| '\u00fd' | '\u0020' | '\u00a0';

// case insensitive chars
fragment A
    : ('a' | 'A')
    ;

fragment B
    : ('b' | 'B')
    ;

fragment C
    : ('c' | 'C')
    ;

fragment D
    : ('d' | 'D')
    ;

fragment E
    : ('e' | 'E')
    ;

fragment F
    : ('f' | 'F')
    ;

fragment G
    : ('g' | 'G')
    ;

fragment H
    : ('h' | 'H')
    ;

fragment I
    : ('i' | 'I')
    ;

fragment J
    : ('j' | 'J')
    ;

fragment K
    : ('k' | 'K')
    ;

fragment L
    : ('l' | 'L')
    ;

fragment M
    : ('m' | 'M')
    ;

fragment N
    : ('n' | 'N')
    ;

fragment O
    : ('o' | 'O')
    ;

fragment P
    : ('p' | 'P')
    ;

fragment Q
    : ('q' | 'Q')
    ;

fragment R
    : ('r' | 'R')
    ;

fragment S
    : ('s' | 'S')
    ;

fragment T
    : ('t' | 'T')
    ;

fragment U
    : ('u' | 'U')
    ;

fragment V
    : ('v' | 'V')
    ;

fragment W
    : ('w' | 'W')
    ;

fragment X
    : ('x' | 'X')
    ;

fragment Y
    : ('y' | 'Y')
    ;

fragment Z
    : ('z' | 'Z')
    ;

fragment FULLWIDTH_SPACE
    : '\u3000'
    ;

fragment FULLWIDTH_ROMAJI
    : [\uFF10-\uFF19\uFF21-\uFF3A\uFF41-\uFF5A]
    ;

fragment HIRAGANA
    : [\u3040-\u309F]
    ;


// Hiragana range

fragment KATAKANA
    : [\u30A0-\u30FF]
    ;

// Katakana range

fragment KANJI_
    : [\u4E00-\u9FAF]
    ;

// Common Kanji range

fragment CONTROL_CHARACTER
    : [\u001E]
    ;

// BODYTEXT: .+?;