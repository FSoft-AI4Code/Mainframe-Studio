//v1.3

grammar Batch;

// Entry point for the script
startRule: statement* label* EOF;

label: labelName statement*;

labelName: COLON IDENTIFIER;
// Statement rules to match different batch commands and constructs
statement:
	setStatement
	| setLocalStatement
	| delStatement
	| pauseStatement
	| mkdirStatement
	| xcopyStatement
	| callStatement
	| ifStatement
	| gotoStatement
	| echoStatement
	| remStatement
	| endlocalStatement
	| exitStatement
	| execStatement
	| rmdirStatement
	| forStatement
	| typeStatement
	| z7Statement
	| bsortexStatement;

z7Statement: filePath Z7 z7Command z7Switches;

z7Command: IDENTIFIER;

z7Switches: (z7Switch)+;

z7Switch: (DASH_SFX | DASH_P | DASH_W | DASH_Y | DASH_TZIP) referencedVariable*;

// section: startSectionName statement* endSectionName? ; Define statements
echoStatement: ECHOSTATEMENT;
remStatement: REMSTATEMENT;

// startSectionName: COLON IDENTIFIER; endSectionName: COLON IDENTIFIER;

// labelStatement: COLON IDENTIFIER ;

bsortexStatement:
	BSORTEX sortParameters inputParameters recordParameters optionParameters outputParameters;

sortParameters: DASH_SORT (sortParameter)+;

sortParameter: variableName EQUAL sortValue;
sortValue: (INT | DOT | IDENTIFIER)+;
inputParameters: DASH_INPUT (inputParameter)+;

inputParameter: variableName assignmentPart;

recordParameters: DASH_RECORD (recordParameter)+;

recordParameter: variableName assignmentPart;

optionParameters: DASH_OPTION (optionParameter)+;

optionParameter: variableName assignmentPart?;

outputParameters: DASH_OUTPUT (outputParameter)+;

outputParameter: variableName EQUAL outputValue;

outputValue: value | referencedVariable | LPAREN STRING RPAREN;

callStatement: CALL (callWithLabel | callWithFilePath);

callWithLabel: labelName;

callWithFilePath: (filePath | fileName)+ conditionParameter? batchParameters?;

batchParameters: batchParameter+;

batchParameter:
	IDENTIFIER
	| STRING
	| PERCENT INT
	| referencedVariable
	| forVariable;

conditionParameter: COND_COLON INT SLASH INT;
COND_COLON: 'COND:';
// call [drive:][path]<filename> [<batchparameters>]] call [:<label> [<arguments>]]

delStatement: DEL filePath;

endlocalStatement: ENDLOCAL;

execStatement: execFile switches? execParameter*;

execFile: EXE_FILE;

execParameter:
	INT
	| referencedVariable
	| IDENTIFIER
	| filePath
	| STRING
	| concatenateString
	| concatenateFileContent
	| forVariable;

concatenateFileContent: (filePath | referencedVariable) PLUS (
		filePath
		| referencedVariable
	);

exitStatement: EXIT exitCurrentBatch? exitCode?;

exitCurrentBatch: SLASH_B;

exitCode: INT | referencedVariable;

forStatement:
	FOR switches? configurationString? (forVariable) IN (
		forValues
	) DO (forDo);

configurationString: STRING;

forValues: LPAREN (forValue)+ RPAREN;

forValue:
	INT
	| STRING
	| filePath
	| fileName
	| referencedVariable
	| forVariable;

forVariable: PERCENT PERCENT forVariableModifier? IDENTIFIER;

forVariableModifier: TILDE_NX;

forDo: LPAREN statement+ RPAREN;

gotoStatement: GOTO (labelName | IDENTIFIER)?;

ifStatement: IF condition ifThen ifElse?;

ifThen: LPAREN statement+ RPAREN | statement;

ifElse: ELSE LPAREN statement+ RPAREN;

simpleIf: statement;

condition:
	leftConditionOperator? relationalOperator rightConditionOperator;

leftConditionOperator: STRING | referencedVariable | IDENTIFIER;

rightConditionOperator:
	STRING
	| INT
	| IDENTIFIER
	| referencedVariable;

relationalOperator: EQU | NEQ | EXIST | GTR;

mkdirStatement: MKDIR value;

setLocalStatement: SETLOCAL setLocalOption;

typeStatement: TYPE (filePath | fileName);

rmdirStatement: RMDIR switches? value;

xcopyStatement: XCOPY xCopySource xCopyDestination switches?;
// xcopy <Source> [<Destination>] [/w] [/p] [/c] [/v] [/q] [/f] [/l] [/g] [/d [:MM-DD-YYYY]] [/u] [/i] [/s [/e]] [/t] [/k] [/r] [/h] [{/a | /m}] [/n] [/o] [/x] [/exclude:FileName1[+[FileName2]][+[FileName3]]] [{/y | /-y}] [/z] [/b] [/j] [/compress]

xCopySource: value;
xCopyDestination: value;

switches: (switch)+;
switch:
	SLASH_W
	| SLASH_C
	| SLASH_V
	| SLASH_P
	| SLASH_F
	| SLASH_L
	| SLASH_G
	| SLASH_D COLON dateFormat
	| SLASH_U
	| SLASH_I
	| SLASH_S
	| SLASH_E
	| SLASH_T
	| SLASH_K
	| SLASH_R
	| SLASH_H
	| SLASH_A
	| SLASH_M
	| SLASH_N
	| SLASH_O
	| SLASH_X
	| SLASH_Y
	| SLASH_Z
	| SLASH_B
	| SLASH_J
	| SLASH_COMPRESS
	| SLASH_EXCLUDE fileName (PLUS fileName)*
	| SLASH_Y
	| SLASH_Z
	| SLASH_B
	| SLASH_J
	| SLASH_Q
	| SLASH_COMPRESS;

dateFormat: INT DASH INT DASH INT;

// TODO: forfilesStatement forfiles [/P pathname] [/M searchmask] [/S] [/C command] [/D [+ | -]
// [{<date> | <days>}]]

setLocalOption:
	ENABLEDELAYEDEXPANSION
	| DISABLEDELAYEDEXPANSION
	| IDENTIFIER;

setStatement:
	SET switches? (variableName) assignmentPart? (
		displayFormating
	)?;
displayFormating: JP_EQUAL value;
assignmentPart:
	EQUAL (value | STRING_CHARACTERS+)?
	| calcOperator EQUAL INT;

pauseStatement: PAUSE (GREATER_CHAR NUL)?;

variableName: IDENTIFIER;

value:
	STRING
	| IDENTIFIER
	| referencedVariable+
	| identifierCombinedWithReferencedVariable
	| filePath
	| fileName
	| JP_TXT
	| calcValue
	| INT
	| forVariable;

calcValue: (INT | referencedVariable | STRING) calcOperator (
		INT
		| referencedVariable
		| STRING
	);

calcOperator: PLUS | DASH | STAR | SLASH;

filePath: (fileName | DISK_ADDRESS)? (SSLASH fileName?)+;

fileName: fileNameChar+;

fileNameChar:
	IDENTIFIER
	| UNDERSCORE
	| DOT
	| JP_TXT
	| referencedVariable
	| STAR
	| COMMA
	| QUESTION
	| EXE;

identifierCombinedWithReferencedVariable:
	idetifierOrRerencedVariable+;

idetifierOrRerencedVariable: IDENTIFIER | referencedVariable;

// timeComponent: yearComponent DASH monthComponent DASH dayComponent UNDERSCORE hourComponent DASH minuteComponent;

// yearComponent: INT | PERCENT DATE COLON TILDE INT COMMA INT PERCENT; monthComponent: INT |
// PERCENT DATE COLON TILDE INT COMMA INT PERCENT; dayComponent: INT | PERCENT DATE COLON TILDE INT
// COMMA INT PERCENT; hourComponent: INT | PERCENT TIME COLON TILDE INT COMMA INT PERCENT;
// minuteComponent: INT | PERCENT TIME COLON TILDE INT COMMA INT PERCENT;
referencedVariable:
	PERCENT (variableName) variableSubstring? PERCENT
	| EXCLAMATION (variableName) variableSubstring? EXCLAMATION;
// specialVariable: specialVariableChar+; specialVariableChar:systemVariable | COLON | EQUAL | TILDE
// | DOT | DASH | INT; systemVariable: DATE | TIME | ERRORLEVEL | JIKAN | HIZUKE;

variableSubstring:
	COLON (
		leftSubstring
		| rightSubstring
		| removeSubstring
		| removeSpaces
		| replaceSubstring
	);

leftSubstring: TILDE startSub COMMA lengthSub;
rightSubstring: TILDE DASH lengthSub;
replacedOrRemovedSubstring: (
		STRING_CHARACTERS+
		| WS
		| COLON
		| IDENTIFIER
		| DOT
		| INT
	);
removeSubstring: removedSubstring EQUAL;

removedSubstring: replacedOrRemovedSubstring;

removeSpaces: EQUAL;

replaceSubstring: subtringRemoved? EQUAL subStringReplaced;
subtringRemoved: replacedOrRemovedSubstring;
subStringReplaced: replacedOrRemovedSubstring;
startSub: INT;
lengthSub: DASH? INT;
// Specific command statements
variableStart: INT;
variableLength: INT;
// IDENTIFIER : [A-Z][A-Za-z_0-9]* ; FILE_PATH_IDENTIFIER: [A-Za-z][A-Za-z_0-9.]*;
STRING: '"' .*? '"' | '\'' .*? '\'';
concatenateString: STRING PLUS STRING;
ECHOSTATEMENT: ATSIGN? ECHO .*? NL; //-> channel(HIDDEN)

REMSTATEMENT: REM .*? NL; //-> channel(HIDDEN)

EXE_FILE: IDENTIFIER DOT EXE;

ENABLEDELAYEDEXPANSION: 'EnableDelayedExpansion';

DISABLEDELAYEDEXPANSION: 'DisableDelayedExpansion';

// Lexer rules for common tokens

INT: [0-9]+; // Integer values

WS: [ \f\t]+ -> channel(HIDDEN); // Whitespace

NL: ('\r'? '\n')+ -> channel(HIDDEN); // Newlines (Windows or Unix)

COMMENTLINE:
	':: ' .*? ( | EOF) -> channel(HIDDEN); // Comment lines
LPAREN: '(';
RPAREN: ')';

// Keywords:
ECHO: 'echo';
SET: 'set';
SETLOCAL: 'setlocal';
REM: 'rem';

COLON: ':';
EQUAL: '=';
JP_EQUAL: '＝';
ATSIGN: '@';
SLASH: '/';
QUESTION: '?';
SSLASH: '\\';
DASH_SFX: '-sfx';
DASH_TZIP: '-tzip';
DASH_SORT: '-sort';
DASH_INPUT: '-input';
DASH_OUTPUT: '-output';
DASH_OPTION: '-option';
DASH_RECORD: '-record';
DASH_P: '-p' | '-P';
DASH_W: '-w' | '-W';
DASH_Y: '-y' | '-Y';

SLASH_W: '/w' | '/W';
SLASH_P: '/p' | '/P';
SLASH_C: '/c' | '/C';
SLASH_V: '/v' | '/V';
SLASH_Q: '/q' | '/Q';
SLASH_F: '/f' | '/F';
SLASH_L: '/l' | '/L';
SLASH_G: '/g' | '/G';
SLASH_D: '/d' | '/D';
SLASH_U: '/u' | '/U';
SLASH_I: '/i' | '/I';
SLASH_S: '/s' | '/S';
SLASH_E: '/e' | '/E';
SLASH_T: '/t' | '/T';
SLASH_K: '/k' | '/K';
SLASH_R: '/r' | '/R';
SLASH_H: '/h' | '/H';
SLASH_A: '/a' | '/A';
SLASH_M: '/m' | '/M';
SLASH_N: '/n' | '/N';
SLASH_O: '/o' | '/O';
SLASH_X: '/x' | '/X';
SLASH_Y: '/y' | '/Y';
SLASH_Z: '/z' | '/Z';
SLASH_B: '/b' | '/B';
SLASH_J: '/j' | '/J';
SLASH_COMPRESS: '/compress';
SLASH_EXCLUDE: '/exclude';
DOT: '.';
// Variables
COND: 'COND';
DISK_ADDRESS: 'U:' | 'C:' | 'D:' | 'O:' | 'P:' | 'I:';

// keyword
BSORTEX: 'bsortex';
CALL: 'call' | 'CALL';
DEL: 'del';
ELSE: 'else';
EQU: 'equ';
EXIST: 'exist';
EXE: 'exe';
ENDLOCAL: 'endlocal';
EXIT: 'exit';
IF: 'if' | 'IF';
GOTO: 'goto';
GTR: 'gtr';
NUL: 'nul';
NEQ: 'neq';
PAUSE: 'pause';
RMDIR: 'rmdir';
FOR: 'for';
IN: 'in' | 'IN';
DO: 'do' | 'DO';
PERCENT: '%';
EXCLAMATION: '!';
MKDIR: 'mkdir';
XCOPY: 'xcopy';
TYPE: 'type';
Z7: '7z';

// DATE: 'date'; TIME: 'time'; HIZUKE: 'hizuke'; JIKAN: 'jikan';
DASH: '-';
UNDERSCORE: '_';
GREATER_CHAR: '>';

TILDE: '~';
TILDE_NX: '~nx';
COMMA: ',';
PLUS: '+';
STAR: '*';

// Japanese encoding text

JP_TXT: JP_CHAR+;
JP_CHAR:
	HIRAGANA
	| KATAKANA
	| KANJI_
	// | CONTROL_CHARACTER
	| ''
	| ''
	| ''
	| ''
	| ''
	// | '�@'
	| '）'
	| '（'
	| '　';

fragment HIRAGANA: [\u3040-\u309F];

// Hiragana range

fragment KATAKANA: [\u30A0-\u30FF];

// Katakana range

fragment KANJI_: [\u4E00-\u9FAF];

IDENTIFIER: [A-Za-z_][A-Za-z_0-9]*;

STRING_CHARACTERS: ~[\r\n];