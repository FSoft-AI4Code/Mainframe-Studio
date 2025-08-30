grammar OGL;

startRule: command* EOF;


command: controlCommand | overlayCommand | orientCommand | fontCommand | defineGroupCommand | positionCommand | drawboxCommand | drawruleCommand | placeCommand | setunitsCommand | settextCommand | definepatternCommand | placePatternCommand | segmentCommand;

///////////////// SEGMENT command

segmentCommand: SEGMENT segmentName? memId (segmentDDName | segmentFileType)?;

segmentName: IDENTIFIER;

segmentDDName: DDNAME segmentDDNameName;

segmentDDNameName: IDENTIFIER | SEGDD;

segmentFileType: FILETYPE fileTypeName;

///////////////// PLACEPATTERN command

placePatternCommand: PLACE PATTERN patternName orientRotatedDegree? patternShade? mirrorOption? negativeOption? patternColor?;
patternColor: COLOR patternColorName;
patternColorName: IDENTIFIER;
mirrorOption: NOMIRROR | MIRROR;
negativeOption: NEGATIVE | NONEGATIVE;

patternShade: (shadePattern | shadeType)+; 

///////////////// DEFINEPATTERN command

definepatternCommand: DEFINE patternName PATTERN lineCoding ENDDEF? ;

lineCoding: lineCodingPels | lineCodingEncoded;

lineCodingPels: PELS coded_line+;

lineCodingEncoded: ENCODED coded_line+;


coded_line: LPAREN INTEGERLITERAL+ RPAREN;

patternName: IDENTIFIER;

//////////////// SETTEXT command

settextCommand: SETTEXT orientRotatedDegree? settextFormat? settextAlignment? line+;


settextFormat: settextFormatModern | settextFormatColumn;
settextFormatModern: MODERN settextFormatPlacement?;
settextFormatPlacement: (CENTER | TOP | LEFT | RIGHT | BOTTOM);
settextFormatColumn: (COLUMN | TATE) settextFormatPlacement?;

settextAlignment: settextAlignmentAuto | settextAlignmentSpaced;
settextAlignmentAuto: AUTO;
settextAlignmentSpaced: SPACED settextAlignmentValue;
settextAlignmentValue: oglMeasurement;
//////////////// SETUNIT command
setunitsCommand: SETUNITS setunitsDefault? setunitsLineSp? setunitsCornerLength? setunitsTextMargin? setUnitsPositioning?;


setunitsDefault: primaryDefault secondaryDefault?;

primaryDefault: oglMeasurement;

secondaryDefault: oglMeasurement;

setunitsLineSp: LINESP oglMeasurement;

setunitsCornerLength: CORNERLENGTH conrnerLengthValue;

conrnerLengthValue: oglMeasurement | MEDIUM | SMALL | LARGE | HALF | MAX;

setunitsTextMargin: TEXTMARGIN textMarginValue;

textMarginValue: ROUNDED | SQUARE;

setUnitsPositioning: POSITIONING positionValue;

positionValue: TOPLEFT | CENTER;
//////////////// PLACE command

placeCommand: PLACE (SEGID | GROUP) groupName;

//////////////// DRAWRULE command

drawruleCommand: DRAWRULE ruleDirection? ruleLength ruleThickness? ruleType? ruleRepeated?;


ruleDirection: ACROSS | DOWN;

ruleLength: oglMeasurement;

ruleThickness: MEDIUM | LIGHT | BOLD | INTEGERLITERAL;

ruleType: SOLID | DASHED | DOTTED;

ruleRepeated: REPEAT (ruleRepeatAcross | ruleRepeatLocation)+;

ruleRepeatAcross: (ACROSS | DOWN)? ruleRepetition SPACED spacedValue;

ruleRepetition: INTEGERLITERAL;


ruleRepeatLocation:  LOCATION ruleRepeatHorizonalCoordinate ruleRepeatVerticalCoordinate;



ruleRepeatVerticalCoordinate: oglMeasurement;

ruleRepeatHorizonalCoordinate: oglMeasurement;

///////// DRAWBOX command
drawboxCommand: DRAWBOX boxWidth boxHeight (boxBorderThickness| boxBorderType| boxRounded| boxDiagonal| boxRepeat| boxShade| boxColor| boxWithtext)*  ; // Have to add boxRepeat? at the end because of the BNMO87.txt file contains the boxRepeat after boxWithtext

boxWidth: oglMeasurement;

boxHeight: oglMeasurement;

boxBorderThickness: MEDIUM | LIGHT | BOLD | INTEGERLITERAL;

boxBorderType: SOLID | DASHED | DOTTED;

boxRounded: ROUNDED boxRoundedOption? ;

boxRoundedOption:(ALL | (TOPLEFT | TOPRIGHT | BOTTOMLEFT | BOTTOMRIGHT)+);

boxDiagonal: DIAGONAL boxDiagonalOption;

boxDiagonalOption: LEFT | RIGHT | BOTH;

boxRepeat: REPEAT (boxRepeatAcrossDown | boxRepeatSpaced)+ boxRepeatLocation?;

boxRepeatLocation: LOCATION boxRepeatHorizonalCoordinate boxRepeatVerticalCoordinate;

boxRepeatVerticalCoordinate: oglMeasurement;

boxRepeatHorizonalCoordinate: oglMeasurement;

boxRepeatAcrossDown: (ACROSS | DOWN) boxRepetition;

boxRepetition: INTEGERLITERAL;

boxRepeatSpaced: SPACED spacedValue;

spacedValue: DIAMETER | oglMeasurement;

boxShade: SHADE box? shadeArea? shadePattern? shadeType?;

box: ALL | BOX INTEGERLITERAL;

shadeArea: WHOLE | LEFT | RIGHT | TOP | BOTTOM;

shadePattern: STANDARD | SCREEN;

shadeType: MEDIUM | XLIGHT | LIGHT | DARK | XDARK | INTEGERLITERAL;

boxColor: COLOR box boxColorName;

boxColorName: IDENTIFIER;


boxWithtext: WITHTEXT box? boxWithtextOrient? boxWithtextFormat? boxWithtextLineSpacing? line;


boxWithtextOrient: INTEGERLITERAL;

boxWithtextLineSpacing: AUTO | SPACED oglMeasurement;

line: LINE (line_part)+;

line_part: fontName+ lineSosiMode? lineUnderlying? lineTextType? text+;

text: STRINGLITERAL;

lineSosiMode: SOSI1 | SOSI2;

lineUnderlying: NOUNDERLINE | UNDERLINE;

lineTextType: CHAR | HEX;

boxWithtextFormat: boxWithtextFormatModern | boxWithtextFormatColumn | boxWithtextFormatPlacement ;

boxWithtextFormatModern: MODERN boxWithtextFormatPlacement?;

boxWithtextFormatPlacement: (CENTER | TOP | BOTTOM | LEFT | RIGHT | BALANCE | JUSTIFY LASTNO?)+;


boxWithtextFormatColumn: (COLUMN | TATE) boxWithtextFormatPlacement?;


//////////////////////// POSITION COMMAND

positionCommand: POSITION positionX positionY;

positionX: (ABSOLUTE | LEFT | RIGHT | UP| DOWN)? oglMeasurement;

positionY: (ABSOLUTE | LEFT | RIGHT | UP| DOWN)? oglMeasurement;



/////////// Control command
controlCommand: CONTROL controlStorage* controlMessage* controlSummary* controlSosiOption* ;

controlStorage: NOSTORE | STORE | REPLACE;

controlMessage: ALL | WARN | ERROR;

controlSummary: NOSUMMARY | SUMMARY;


controlSosiOption: SOSI | NOSOSI;

///////////////// Overlay command
overlayCommand: OVERLAY overlayName SIZE overlayWidth overlayHeight OFFSET overlayHorizonalCoordinate overlayVerticalCoordinate;

overlayName: IDENTIFIER;

overlayWidth: oglMeasurement;

overlayHeight:oglMeasurement;

overlayHorizonalCoordinate: oglMeasurement;

overlayVerticalCoordinate: oglMeasurement;

//////////////////////////// ORIENT command
orientCommand: ORIENT orientRotatedDegree;

orientRotatedDegree: INTEGERLITERAL;

////////////////// FONT command

fontCommand: fontCommandMVS | fontCommandVM;

fontCommandMVS: FONT (fontWithMemID | fontWithCharSet) fontDDName? fontHeight? fontScale? fontColor? fontUColor?;



fontCommandVM: FONT (fontWithMemID | fontWithCharSet) fontFileType? fontHeight? fontScale? fontColor? fontUColor?;

fontFileType: FILETYPE fileTypeName;

fileTypeName: FONT38PP | IDENTIFIER | PSEG38PP;

fontWithMemID: fontName? memId;

fontWithCharSet: fontName CHARSET charSetName CODEPAGE codePageName;

fontDDName: DDNAME ddNameName;

ddNameName: IDENTIFIER | FONTDD;


fontHeight: HEIGHT oglMeasurement;

fontScale: SCALE oglMeasurement;

fontColor: COLOR fontColorName;

fontUColor: UCOLOR fontColorName;

fontColorName: IDENTIFIER;
fontName: IDENTIFIER;
memId: IDENTIFIER;
charSetName: IDENTIFIER;
codePageName: IDENTIFIER;

//////////////  DEINE GROUP COMMAND
defineGroupCommand: DEFINE groupName GROUP command+ ENDDEF;

groupName: IDENTIFIER;


oglMeasurement: INTEGERLITERAL (PELS | IN | MM | CPI | LPI | POINTS)?;

DOT: '.';
LPAREN: '(';
RPAREN: ')';

ABSOLUTE: A B S O L U T E | A B S;
ACROSS: A C R O S S;
ALL: A L L;
AUTO: A U T O;
BALANCE: B A L A N C E;
BOLD: B O L D;
BOTH: B O T H;
BOTTOM: B O T T O M;
BOTTOMLEFT: B O T T O M L E F T;
BOTTOMRIGHT: B O T T O M R I G H T;
BOX: B O X;
CENTER: C E N T E R;
CHAR: C H A R;
CHARSET: C H A R S E T;
CODEPAGE: C O D E P A G E;
COLOR: C O L O R;
COLUMN: C O L U M N;
CONTROL: C O N T R O L;
CORNERLENGTH: C O R N E R L E N G T H;
CPI: C P I;
DARK: D A R K;
DASHED: D A S H E D;
DDNAME: D D N A M E;
DEFINE: D E F I N E;
DIAGONAL: D I A G O N A L;
DIAMETER: D I A M E T E R;
DOTTED: D O T T E D;
DRAWBOX: D R A W B O X;
DRAWRULE: D R A W R U L E;
DOWN: D O W N;
ENCODED: E N C O D E D;
ENDDEF: E N D D E F;
ERROR: E R R O R;
FILETYPE: F I L E T Y P E;
FONT: F O N T;
FONT38PP: F O N T '3' '8' P P;
FONTDD: F O N T D D;
GROUP: G R O U P;
HALF: H A L F;
HEIGHT: H E I G H T;
HEX: H E X;
IN: I N;
JUSTIFY: J U S T I F Y;
LARGE: L A R G E;
LASTNO: L A S T N O;
LEFT: L E F T;
LIGHT: L I G H T;
LINE: L I N E;
LINESP: L I N E S P;
LOCATION: L O C A T I O N;
LPI: L P I;
MAX: M A X;
MM: M M;
MEDIUM: M E D I U M;
MIRROR: M I R R O R;
MODERN: M O D E R N;
NEGATIVE: N E G A T I V E;
NOMIRROR: N O M I R R O R;
NONEGATIVE: N O N E G A T I V E;
NOSTORE: N O S T O R E;
NOSOSI: N O S I;
NOSUMMARY: N O S U M M A R Y;
NOUNDERLINE: N O U N D E R L I N E;
OFFSET: O  F F S E T;
ORIENT: O R I E N T;
OVERLAY: O V E R L A Y;
PATTERN: P A T T E R N;
PELS: P E L S | P E L;
PLACE: P L A C E;
POINTS: P O I N T S;
POSITION: P O S I T I O N | P O S;
POSITIONING: P O S I T I O N I N G;
PSEG38PP: P S E G '3' '8' P P;
REPEAT: R E P E A T;
REPLACE: R E P L A C E;
RIGHT: R I G H T;
ROUNDED: R O U N D E D;
SCALE: S C A L E;
SCREEN: S C R E E N;
SEGDD: S E G D D;
SEGID: S E G I D;
SEGMENT: S E G M E N T;
SETTEXT: S E T T E X T | S E T T;
SETUNITS: S E T U N I T S;
SHADE: S H A D E;
SIZE: S I Z E;
SMALL: S M A L L;
SOLID: S O L I D;
SOSI: S O S I;
SOSI1: S O S I '1';
SOSI2: S O S I '2';
SPACED: S P A C E D;
SQUARE: S Q U A R E;
STANDARD: S T A N D A R D;
STORE: S T O R E;
SUMMARY: S U M M A R Y;
TATE: T A T E;
TEXTMARGIN: T E X T M A R G I N;
TOP: T O P;
TOPLEFT: T O P L E F T;
TOPRIGHT: T O P R I G H T;
UCOLOR: U C O L O R;
UNDERLINE: U N D E R L I N E;
UP: U P;
WARN: W A R N;
WHOLE: W H O L E;
WITHTEXT: W I T H T E X T;
XDARK: X D A R K;
XLIGHT: X L I G H T;

STRINGLITERAL
    : '"' (~["\n\r] | '""' | '\'')* '"'
    | '\'' (~['\n\r] | '\'\'' | '"' | NEWLINE '      -' WS? '\'')* '\'' (B)?
    |'\'\''  (~['\n\r] | '""' )* '\'\''
    ;
INTEGERLITERAL: [0-9]+ ('.' [0-9]+)? | '.' [0-9]+;


COMMENT: '-' (STRINGLITERAL+ | IDENTIFIER)? -> channel(HIDDEN);
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
IDENTIFIER
    : [a-zA-Z0-9#@\\]+ ([-_/]+ [a-zA-Z0-9#@]+)*
    ;


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
