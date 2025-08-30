// v1.3

grammar LDLP;

// Parser Rules

startRule: runtime EOF;

runtime: expression? statements?;

statements: statement+;

statement:
	moveStatement
	| assignment
	| dowhenStatement
	| recallStatement
	| advanceStatement
	| addStatement
	| divideStatement
	| multiplyStatement
	| dateConvertStatement
	| insertStatement
	| caseStatement
	| computeStatement
	| determineStatement
	| breakStatement
	| accessExtStatement
	| lookupStatement
	| attachStatement
	| attachAndSpaceStatement
	| messageStatement
	| acceptStatement
	| jumptoStatement
	| extractStatement
	| sleepStatement
	| labelStatement
	| subtractStatement
	| cursorStatement
	| flagStatement
	| detachStatement
	| movedateStatement
	| initializeStatement
	| abortStatement
	| continueStatement
	| ifStatement
	| loopStatement
	| returnStatement
	| rocStatement
	| startStatement
	| switchtoStatement
	| criticalpointStatement
	| enduseStatement
	| excludeStatement
	| loadStatement
	| matchStatement
	| setDBStatement
	| sendListDynamicStatement
	| sendListStaticStatement
	| sendMessageStatement
	| setTitleStatement
	| attributeStatement
	| beginpageStatement
	| onchangeStatement
	| pageStatement
	| releaseStatement
	| restartStatement
	| runStatement
	| sendPrintStatement
	| wakeStatement
	| logStatement
	| functionCallingStatement
	| movetimeStatement;

functionCallingStatement: function_name LP (paramList)? RP;

function_name: variable;

abortStatement: ABORT (literal (literal | objectName)?)?;

acceptStatement: ACCEPT objectName;

accessExtStatement: ACCESS_EXT dbName locator?;

locator: find | get;

find: FIND (FIRST | LAST | NEXT | PRIOR)? database;

get: GET database item;

database: variable | literal;

item: variable | literal;

addStatement:
	ADD expression (variable | literal) (GIVING variable)? (
		ROUNDED
	)? (GS status)?;

advanceStatement:
	ADVANCE (
		NUMERIC_LITERALS
		| NEW_PAGE
		| variable
		| CHANNEL NUMERIC_LITERALS
	) (AS outputStream)?;

outputStream: variable;

assignment: variable ASSIGN expression;

attachStatement: ATTACH stringExpression variable;

attachAndSpaceStatement:
	ATTACH_AND_SPACE stringExpression variable;

attributeStatement:
	ATTRIBUTE BDNAME literal (userCode)? (GS status)?;

beginpageStatement:
	BEGIN_PAGE (CLEAR | frameName) (AS outputStream)?;

breakStatement: BREAK (ALL)?;

case:
	CASE (literal | variable) (COMMA (literal | variable))* statements?;

otherwise: OTHERWISE statements?;

caseStatement: beginCase expression case* otherwise? endcase;

beginCase: BEGIN_CASE;

endcase: END_CASE;

computeStatement:
	COMPUTE variable expression (ROUNDED)? (GS status)?;

continueStatement: CONTINUE;

criticalpointStatement:
	CRITICAL_POINT (SLEEP expression)? (NO_RELEASE)?;

cursorStatement: CURSOR (varName | END_OF_PAGE);

dateConvertStatement:
	DATE_CONVERT (
		(
			dateVariable (Arithmetic_operators ( dateVariable))? FORMAT dateFormat (
				(variable FORMAT dateFormat)
				| EDIT_ONLY
			)? (GS status)?
		)
		| (TODAY_NUMBER | TO_DATE | TO_ALPHA) dateVariable (
			GS status
		)?
	);

dateVariable: variable | NUMERIC_LITERALS;

detachStatement:
	DETACH expression variable (
		(POSITION | START) start_position = expression
	)? (DELIMITER delimiter = expression)?;

determineStatement:
	determineActualStatement
	| determineBackStatement
	| determineEveryStatement
	| determineFromStatement
	| determineGroupStatement
	| determineLastStatement
	| determineTotalStatement;

determineActualStatement:
	DETERMINE ACTUAL variant (GS status)? statements? determineEnd;

variant: databaseVariant | extractFileVariant;

databaseVariant:
	iterator SERIAL? (SECURE | KEY_ONLY)? (MULTI records)?;

extractFileVariant:
	extractFile EXTRACTED_AS (records | EVENT) (
		RETAINED_AS fileName
	)?;

determineBackStatement:
	DETERMINE BACK iterator SERIAL? (SECURE | KEY_ONLY)? (
		MULTI records
	)? (GS status)? statements? determineEnd;

determineEveryStatement:
	DETERMINE EVERY iterator SERIAL? (SECURE | KEY_ONLY)? (
		MULTI records
	)? (GS status)? statements? determineEnd;

determineFromStatement:
	DETERMINE FROM iterator SERIAL? (SECURE | KEY_ONLY)? (
		MULTI records
	)? (GS status)? statements? determineEnd;

determineGroupStatement:
	DETERMINE GROUP iterator (FROM | BACK) (
		LP args += argument (COMMA args += argument)* RP
	)? (
		UNTIL LP until_args += argument (
			COMMA until_args += argument
		)* RP
	)? SERIAL? (SECURE | KEY_ONLY)? (MULTI records)? (GS status)? statements? determineEnd;

determineLastStatement:
	DETERMINE LAST iterator (SECURE | KEY_ONLY)? (GS status)?;

determineTotalStatement:
	DETERMINE TOTAL identifier attributeName LP keyArguments RP (
		MULTI records
	)? (GS status)? statements? determineEnd;

attributeName: variable;

keyArguments: argument (COMMA argument)*;

records: variable;

extractFile: variable;

iterator: variable (LP argument (COMMA argument)* RP)?;

argument: expression;

determineEnd: END | END_EXIT | END_NO_PRINT;

divideStatement:
	DIVIDE expression (variable | literal) (
		GIVING giving_variable = variable
	)? (ROUNDED)? (REMAINDER remainder_variable = variable)? (
		GS status
	)?;

dowhenBlock: statements;

elseBlock: statements;

dowhenStatement:
	DO_WHEN condition dowhenBlock? (ELSE elseBlock?)? endDowhen;

condition: expression;

classAttribute: variable;

endDowhen: END | END_EXIT | END_NO_PRINT;

enduseStatement: END_USE className;

excludeStatement: EXCLUSIVE className;

ifStatement:
	IF expression dowhenBlock? (ELSE elseBlock?)? endIf;

endIf: (END | END_EXIT | END_NO_PRINT);

methodCall: variable LP paramList? RP;

expression:
	Arithmetic_operators expression (
		Arithmetic_operators expression
	)?
	| expression NOT? NUMERIC (logical_operator expression)?
	| expression Arithmetic_operators expression
	| expression relational_operator expression
	| expression logical_operator expression
	| LP expression RP
	| methodCall
	| identifier
	| literal;

// setExpression: ( identifier | expression (COMMA expression)* | literal '..' literal )
// (logical_operator setExpression*)?;

stringExpression: (variable | literal) (
		AMPERSAND stringExpression
	)*;

paramList: param ( COMMA param)*;

param: expression;

extractStatement:
	EXTRACT attributeName (MAPPER header)? AS extractFile (
		RETAIN_AS fileName
	)?;

header: variable;

foreachStatement:
	FOREACH variable IN iterator (FROM | BACK | EVERY) POLYMORPHIC? SERIAL? (
		SECURE
		| KEY_ONLY
	) (MULTI expression)? (GS status)?;

flagStatement: FLAG expression variable;

initializeStatement: INITIALIZE variable (initializationValue)?;

initializationValue: variable;

insertStatement:
	INSERT insertable (LP mapping (AMPERSAND mapping)* RP)?;

insertable: expression;

mapping: insertable EQ className;

tableName: identifier;

jumptoStatement: JUMP_TO label;

labelStatement: LABEL label;

label: variable;

loadStatement: LOAD LENGTH expression ispecAttribute;

ispecAttribute: variable;

logStatement:
	LOG (DEBUG | RELEASE | ALWAYS) (ERROR | WARNING | HALT)? expression expression?;

lookupStatement:
	lookupBaseStatement
	| lookupFromStatement
	| lookupEveryStatement
	| lookupGroupStatement;

lookupBaseStatement:
	LOOKUP expression className (SECURE | KEY_ONLY)? (GS status)?;

lookupFromStatement:
	LOOKUP FROM expression className SERIAL? (SECURE | KEY_ONLY)? (
		MULTI expression
	)? (GS status)? statements END;

lookupEveryStatement:
	LOOKUP EVERY className SERIAL? (SECURE | KEY_ONLY)? (
		MULTI expression
	)? (GS status)? statements END;

lookupGroupStatement:
	LOOKUP GROUP className (FROM | BACK) expression (
		UNTIL until_exp = expression
	)? SERIAL? (SECURE | KEY_ONLY)? (
		MULTI multi_exp = expression
	)? (GS status)? statements END;

loopStatement:
	LOOP (WHILE LP expression RP)? loopBlock (
		END
		| END_EXIT
		| END_NO_PRINT
	);

loopBlock: statements;

compareType: COMPARE_ASCENDING | COMPARE_DESCENDING;

matchStatement:
	MATCH compareType LP extractFile COMMA extractFile RP (
		AND compareType LP extractFile COMMA extractFile RP
	)? (GS status)?;

messageStatement:
	MESSAGE (ATTENTION | ERROR | expression) expression?;

moveStatement:
	MOVE expression (POSITION source_variable)? length? variable (
		POSITION target_variable
		| SORTA
		| SORTD
	)? (GS status)?;

length: LENGTH (variable | literal);

source_variable: variable | literal;

target_variable: variable | literal;

movedateStatement: MOVE_DATE variable ( FORMAT identifier)?;

movetimeStatement: MOVE_TIME variable;

multiplyStatement:
	MULTIPLY expression (variable | literal) (
		GIVING giving_variable = variable
	)? (ROUNDED)? (GS status)?;

onchangeStatement:
	ON_CHANGE variable AS literal (
		FOOTING footing_frame_name = frameName (
			AT footing_line_number = lineNumber
		)?
	)? (
		HEADING heading_frame_name = frameName (
			AT heading_line_number = lineNumber
		)?
	)? routineCall?;

routineCall: variable GIVING variable;

pageStatement: PAGE pageNumber varName;

recallStatement:
	RECALL (expression | BYE | EXIT)? (TEACH expression)?;

releaseStatement: RELEASE (AS reportName)?;

restartStatement: RESTART (profileName | fileName);

rocStatement: ROC (expression (expression | CLEAR)?)?;

returnStatement: RETURN (expression | instance ASA interface)?;

instance: variable;

interface: variable;

runStatement:
	RUN (literal | variable) device? TRACE? (
		LA initial_language = expression
	)? (PA parameter = expression)?;

device: variable;

sleepStatement:
	SLEEP (
		expression
		| UNTIL (WAKEUP | WOKEN)
		| END_AFTER expression
	) (NO_COMMIT)?;

startStatement: START expression expression?;

sendListDynamicStatement: SEND_LIST_DYNAMIC expression variable;

sendListStaticStatement:
	SEND_LIST_STATIC expression (downloadFile | FILE extractFile);

downloadFile: ( fileName | expression) (ON expression)?;

sendMessageStatement:
	SEND_MESSAGE (ALL | ODT | variable) expression;

sendPrintStatement:
	SEND_PRINT (AS reportName)? device output_device = expression? (
		AT at_expr = expression
	)?;

setDBStatement: SET_DB dbName (className | ALL);

setTitleStatement:
	SET_TITLE extractFile expression (PACK expression)? (EXIST)?;

stninfoStatement: STN_INFO expression variable;

subtractStatement:
	SUBTRACT expression (variable | literal) (GIVING variable)? (
		ROUNDED
	)? (GS status)?;

switchtoStatement:
	SWITCH_TO expression (DATA data = expression)? (
		PARTITION partition = expression
	)? BYE? CLEAR? INHERIT?;

wakeStatement: WAKE reportName (PA expression) (GS status);

relational_operator:
	EQ
	| GT
	| GE
	| LE
	| LT
	| NEQ
	| NOT
	| CAST
	| IN
	| ISA;

logical_operator: NOT | AND | OR;

status: variable;

dbName: identifier;

fileName: variable | literal;

dateFormat: identifier;

className: variable;

varName: variable;

objectName: variable;

userCode: literal;

frameName: variable;

lineNumber: NUMERIC_LITERALS;

pageNumber: NUMERIC_LITERALS;

reportName: variable;

profileName: variable;

deviceName: variable;

// identifier can be the same as LDLP keywords
keywords:
	BACK
	| ABORT
	| ACCESS_EXT
	| ACCEPT
	| ACTUAL
	| ADD
	| ALL
	| ALWAYS
	| AS
	| ASA
	| AT
	| ATTACH
	| ATTACH_AND_SPACE
	| ATTENTION
	| ATTRIBUTE
	| BDNAME
	| BEGIN_CASE
	| BEGIN_PAGE
	| BREAK
	| BYE
	| CALL
	| CASE
	| CHANNEL
	| CLEAR
	| COMMA
	| COMPARE_ASCENDING
	| COMPARE_DESCENDING
	| COMPUTE
	| CONTINUE
	| CRITICAL_POINT
	| CURSOR
	| DATA
	| DATE_CONVERT
	| DEBUG
	| DELIMITER
	| DETACH
	| DETERMINE
	| DIVIDE
	| EDIT_ONLY
	| ELSE
	| ERROR
	| EVENT
	| EVERY
	| EXCLUSIVE
	| EXIST
	| EXTRACT
	| EXTRACTED_AS
	| FILE
	| FIND
	| FLAG
	| FOOTING
	| FOREACH
	| FORMAT
	| FROM
	| GET
	| GIVING
	| GROUP
	| HALT
	| HEADING
	| IF
	| IN
	| INITIALIZE
	| INHERIT
	| INSERT
	| JUMP_TO
	| KEY_ONLY
	| LA
	| LABEL
	| LAST
	| LENGTH
	| LOOKUP
	| LOAD
	| LOG
	| LOOP
	| NUMERIC
	| MAPPER
	| MATCH
	| MESSAGE
	| MOVE
	| MOVE_DATE
	| MOVE_TIME
	| MULTI
	| MULTIPLY
	| NEW_PAGE
	| NEXT
	| NO_COMMIT
	| NO_RELEASE
	| ODT
	| ON
	| ON_CHANGE
	| OTHERWISE
	| PA
	| PACK
	| PAGE
	| PARTITION
	| POLYMORPHIC
	| POSITION
	| RECALL
	| RELEASE
	| REMAINDER
	| RESTART
	| RETAIN_AS
	| RETAINED_AS
	| RETURN
	| ROC
	| ROUNDED
	| RUN
	| SECURE
	| SEND_LIST_DYNAMIC
	| SEND_LIST_STATIC
	| SEND_MESSAGE
	| SEND_PRINT
	| SEND_STATUS
	| SERIAL
	| SET_DB
	| SET_TITLE
	| SLEEP
	| SORTA
	| SORTD
	| START
	| STN_INFO
	| SUBTRACT
	| SWITCH_TO
	| TEACH
	| THIS
	| TO_ALPHA
	| TOTAL
	| TODAY_NUMBER
	| TO_DATE
	| TRACE
	| WAKE
	| WAKEUP
	| WARNING
	| WOKEN
	| WHILE;

// Lexer rules

STRING_LITERALS: String;

Arithmetic_operators: PLUS | MINUS | EXP | MULT | DIV;

ABORT: A B O R T;

ACCESS_EXT: A C C E S S E X T;

ACCEPT: A C C E P T | A X;

ACTUAL: A C T U A L;

ADD: A D D;

ADVANCE: A D V A N C E | A V;

ALL: A L L;

ALWAYS: A L W A Y S;

AS: A S;

ASA: 'AsA';

AT: A T;

ATTACH: A T T A C H | A T T;

ATTACH_AND_SPACE: A T T A C H A N D S P A C E | A T S;

ATTENTION: A T T E N T I O N;

ATTRIBUTE: A T T R I B U T E | A T T R;

BACK: B A C K;

BDNAME: B D N A M E;

BEGIN_CASE: B E G I N C A S E | B C;

BEGIN_PAGE: B E G I N P A G E | B P;

BREAK: B R E A K | B K;

BYE: B Y E;

CALL: C A L L;

CASE: C A S E | C S;

CHANNEL: C H A N N E L;

CLEAR: C L E A R | C L;

COMMA: ',';

COMPARE_ASCENDING: C O M P A R E A S C E N D I N G;

COMPARE_DESCENDING: C O M P A R E D E S C E N D I N G;

COMPUTE: C O M P U T E | C O M P;

CONTINUE: C O N T I N U E;

CRITICAL_POINT: C R I T I C A L P O I N T | C P;

CURSOR: C U R S O R | C U;

DATA: D A T A | D A;

DATE_CONVERT: D A T E C O N V E R T | D C;

DEBUG: D E B U G;

DELIMITER: D E L I M I T E R;

DETACH: D E T A C H | D E T | D T H;

DETERMINE: D E T E R M I N E | D T;

DIVIDE: D I V I D E | D V;

DO_WHEN: D O W H E N | D W;

EDIT_ONLY: E D I T O N L Y;

ELSE: E L S E;

END: 'End' | 'end';

END_AFTER: E N D A F T E R;

END_CASE: E N D C A S E | E C;

END_EXIT: E N D E X I T | E E | 'EE;';

END_USE: E N D U S E | E U;

END_NO_PRINT: E N D N O P R I N T;

END_OF_PAGE: E N D O F P A G E | E O P;

ERROR: E R R O R;

EVENT: E V E N T;

EVERY: E V E R Y;

EXCLUSIVE: E X C L U S I V E | E X U;

EXIT: E X I T;

EXIST: E X I S T;

EXTRACT: E X T R A C T | E X;

EXTRACTED_AS: E X T R A C T E D A S;

FILE: F I L E;

FIND: F I N D;

FIRST: F I R S T;

FLAG: F L A G | F L | F G;

FOOTING: F O O T I N G | F T G;

FOREACH: F O R E A C H;

FORMAT: F O R M A T | F M T;

FROM: F R O M;

GET: G E T;

GIVING: G I V I N G;

GROUP: G R O U P;

GS: G S;

HALT: H A L T;

HEADING: H E A D I N G | H D G;

IF: I F;

IN: I N;

INITIALIZE: I N I T I A L I Z E;

INHERIT: I N H E R I T | I N;

INSERT: I N S E R T;

JUMP_TO: J U M P T O | J T O | G O T O;

KEY_ONLY: K E Y O N L Y;

LA: L A;

LABEL: L A B E L | L A B;

LAST: L A S T;

LENGTH: L E N G T H;

LOOKUP: L O O K U P | L U;

LOAD: L O A D;

LOG: L O G;

LOOP: L O O P;

NUMERIC: N U M E R I C;

MAPPER: M A P P E R | M P;

MATCH: M A T C H;

MESSAGE: M E S S A G E | M E;

MOVE: M O V E | M V;

MOVE_DATE: M O V E D A T E | M D;

MOVE_TIME: M O V E T I M E | M T;

MULTI: M U L T I;

MULTIPLY: M U L T I P L Y;

NEW_PAGE: N E W P A G E;

NEXT: N E X T;

NO_COMMIT: N O C O M M I T;

NO_RELEASE: N O R E L E A S E | N R;

ODT: O D T;

ON: O N;

ON_CHANGE: O N C H A N G E | O C H;

OTHERWISE: O T H E R W I S E;

PA: P A;

PACK: P A C K;

PAGE: P A G E | P G;

PARTITION: P A R T I T I O N | P A;

POLYMORPHIC: P O L Y M O R P H I C;

POSITION: P O S I T I O N | P O S | P O;

PRIOR: P R I O R;

RECALL: R E C A L L | 'RC;';

RELEASE: R E L E A S E | R E L;

REMAINDER: R E M A I N D E R | R E M;

RESTART: R E S T A R T | R T;

RETAIN_AS: R E T A I N A S | R A S | R T N;

RETAINED_AS: R E T A I N E D A S | E A S;

RETURN: R E T U R N;

ROC: R O C;

ROUNDED: R O U N D E D;

RUN: R U N;

SECURE: S E C U R E;

SEND_LIST_DYNAMIC: S E N D L I S T D Y N A M I C | S L D Y N;

SEND_LIST_STATIC: S E N D L I S T S T A T I C | S L S T A;

SEND_MESSAGE: S E N D M E S S A G E | S M S G | S M;

SEND_PRINT: S E N D P R I N T | S E N D | S P;

SEND_STATUS: S E N D S T A T U S | S S;

SERIAL: S E R I A L;

SET_DB: S E T D B;

SET_TITLE: S E T T I T L E;

SLEEP: S L E E P | S L P;

SORTA: S O R T A;

SORTD: S O R T D;

START: S T A R T;

STN_INFO: S T N I N F O | S I;

SUBTRACT: S U B T R A C T | S B;

SWITCH_TO: S W I T C H T O | S W T;

TEACH: T E A C H;

THIS: T H I S;

TO_ALPHA: T O A L P H A;

TOTAL: T O T A L;

TODAY_NUMBER: T O D A Y N U M B E R;

TO_DATE: T O D A T E;

TRACE: T R A C E | T R;

UNTIL: U N T I L;

WAKE: W A K E;

WAKEUP: W A K E U P;

WARNING: W A R N I N G;

WOKEN: W O K E N;

WHILE: W H I L E;

ASSIGN: ':=';

Backslash: '\\' -> channel(HIDDEN);

WS: Ws -> channel(HIDDEN);

fragment Ws: [ \r\n\t]+;

COMMENT: Comment -> channel(HIDDEN);

fragment Comment: ':' ~[=] ~[\r\n]*;

specialName: CLEAR | INITIALIZE;

DOT: '.';

variable: LP? identifier RP?;

identifier:
	(IDENTIFIER | keywords) (DOT (IDENTIFIER | keywords))* (
		LB expression (COMMA expression)* RB
	)?;

literal:
	STRING_LITERALS
	| LP? Arithmetic_operators? NUMERIC_LITERALS RP?;

fragment Letter: ~[0-9;/\\+!~#$%^&()\-=`'":,.?[\]{}*| \r\n\t];

fragment Digit:
	'0'
	| '1'
	| '2'
	| '3'
	| '4'
	| '5'
	| '6'
	| '7'
	| '8'
	| '9';

AND: 'AND' | '&&';

EQ: '=';

GT: '>';

GE: '≥' | '>=';

LB: '[';

LE: '<=' | '≤';

LP: '(';

LT: '<';

NEQ: '<>';

NOT: 'NOT' | '~';

OR: 'OR' | '||' | 'or';

RB: ']';

RP: ')';

CAST: ASA;

ISA: 'isA';

SHIFT: '>>';

COLON: ':';

AMPERSAND: '&';

PLUS: '+';
MINUS: '-';
EXP: '**';
MULT: '*';
DIV: '/';

IDENTIFIER: [_A-Za-z][A-Za-z0-9_]*;

NUMERIC_LITERALS: [0-9][.0-9]*;

fragment String: '"' (EscapedChar | ~["\\])* '"';

fragment EscapedChar:
	'\\' [efnrtv"\\]
	| '\\x' [0-9]+
	| '@' [A-Za-z0-9]+ '@';

fragment A: ('a' | 'A');

fragment B: ('b' | 'B');

fragment C: ('c' | 'C');

fragment D: ('d' | 'D');

fragment E: ('e' | 'E');

fragment F: ('f' | 'F');

fragment G: ('g' | 'G');

fragment H: ('h' | 'H');

fragment I: ('i' | 'I');

fragment J: ('j' | 'J');

fragment K: ('k' | 'K');

fragment L: ('l' | 'L');

fragment M: ('m' | 'M');

fragment N: ('n' | 'N');

fragment O: ('o' | 'O');

fragment P: ('p' | 'P');

fragment Q: ('q' | 'Q');

fragment R: ('r' | 'R');

fragment S: ('s' | 'S');

fragment T: ('t' | 'T');

fragment U: ('u' | 'U');

fragment V: ('v' | 'V');

fragment W: ('w' | 'W');

fragment X: ('x' | 'X');

fragment Y: ('y' | 'Y');

fragment Z: ('z' | 'Z');