// Orignal

grammar IBM_JCL;

startRule: (statement)* (END_)* WS? EOF;
statement:
	continueStatement
	| jobStatement
	| execStatement
	| jcllibStatement
	| setStatement
	| procStatement
	| joblibStatement
	| ifStatement;

inlineContent:
	backUpDatasetContent
	| prtfileContent
	| sortContent
	| tdumpContent
	| extentContent
	| inlineParameters
	| generateContent
	| recordFieldContent
	| ~NEWLINE+;

recordFieldContent: RECORD_ WS recordField;

recordField:
	FIELD_ '=' '(' recordFieldParam (COMMA recordFieldParam?)* ')';
recordFieldParam: value;

generateContent:
	GENERATE_ WS generateParam (COMMA generateParam)*;
generateParam: generateParaName '=' generateParaValue;
generateParaName: IDENTIFIER;
generateParaValue: IDENTIFIER | NUMBER;

inlineParameters: inlineParam (COMMA inlineParam)*;
inlineParam: inlineParaName ('=' inlineParaValue)?;
inlineParaName: IDENTIFIER | DD_;
inlineParaValue: IDENTIFIER | NUMBER;
extentContent: EXTENT_ WS extentParam (COMMA extentParam)*;
extentParam: extentParaName '=' extentParaValue;
extentParaName: IDENTIFIER;
extentParaValue: IDENTIFIER | NUMBER;
// sourceControlName: IDENTIFIER '=' IDENTIFIER; extentNumber: EXT_ '=' NUMBER; targetDDName: TODD_
// '=' IDENTIFIER;

tdumpContent: TDUMP_ WS systemIdentifier COMMA processedData;

processedData: DATA_ '=' IDENTIFIER;
systemIdentifier: SISN_ '=' IDENTIFIER;

sortContent:
	SORT_ WS FIELDS_ '=' '(' sortFields ')' (COMMA sortOption)* WS?;
sortOption: formatOption;
formatOption: FORMAT_ '=' IDENTIFIER;

sortFields: sortField (COMMA sortField)*;
sortField: IDENTIFIER | NUMBER;
prtfileContent: PRTFILE_ (WS prtFileParameter)+;

prtFileParameter: (IDENTIFIER | DD_) '(' paramValue ')';

backUpDatasetContent:
	BACKUP_ WS backUpFrom COMMA backUpTo COMMA LIST_ COMMA datasetContent;
backUpFrom: FROM_ '(' DD_ '(' IDENTIFIER ')' ')';

backUpTo: TO_ '(' DD_ '(' IDENTIFIER ')' ')';

datasetContent:
	DATASET_ '(' datasetList ')' (COMMA datasetOptions)? WS?;

datasetOptions: datasetOption (COMMA datasetOption)*;

datasetOption: IDENTIFIER;

datasetList:
	'(' datasetName ((COMMA | COMMA WS NEWLINE WS) datasetName)* ')';

datasetName: accessName;

DATASET_: 'DATASET';
BACKUP_: 'BACKUP';
JOB_: 'JOB';
PRTFILE_: 'PRTFILE';
EXEC_: 'EXEC';
DD_: 'DD';
FROM_: 'FROM';
TO_: 'TO';
END_: 'END';
LIST_: 'LIST';
JCLLIB_: 'JCLLIB';
JOBLIB_: 'JOBLIB';
INCLUDE_: 'INCLUDE';
MEMBER_: 'MEMBER';
DSLASH_: '//';
DATA_: 'DATA';
TDUMP_: 'TDUMP';
SISN_: 'SISN';
SET_: 'SET';
SORT_: 'SORT';
FIELDS_: 'FIELDS';
RECORD_: 'RECORD';
FIELD_: 'FIELD';
GENERATE_: 'GENERATE';
PROC_: 'PROC';
EXTENT_: 'EXTENT';
FORMAT_: 'FORMAT';
IF_: 'IF';
THEN_: 'THEN';
ENDIF_: 'ENDIF';
// SCN_:'SCN'; TODD_:'TODD'; EXT_:'EXT';
PEND_: 'PEND';
AND_: 'AND';
OR_: 'OR';
COMMA: ',' | ', ' | ',' WS+;
// SYSIN_: 'SYSIN'; emptyStatement: DSLASH_ (idxNumber)? NEWLINE;
ifStatement:
	DSLASH_ (cname)? WS? IF_ WS? condition WS THEN_ WS? (NEWLINE) statement* endIf;

condition: combinableCondition andOrCondition*;

andOrCondition:
	NEWLINE? DSLASH_? WS? (AND_ | OR_) WS? (combinableCondition);
combinableCondition: simpleCondition;

simpleCondition: '(' condition ')' | conditionOperator;

conditionOperator: ddParamName ('=' ddParamValue)?;

endIf: DSLASH_ (cname)? WS? ENDIF_ (NEWLINE+ | EOF);

joblibStatement:
	DSLASH_ JOBLIB_ WS? DD_ WS? ddParameters (NEWLINE+ | EOF) continueStatement* ddStatement*;
// sysinStatement: DSLASH_ SYSIN_ WS? DD_ WS? ddParameters (NEWLINE+|EOF) continueStatement* ddStatement*;
continueStatement: (DSLASH_ | '/' cname?) WS+ (ddParameters)+ (
		idxNumber
	)? (NEWLINE+ | EOF);

jobStatement:
	DSLASH_ (cname)? WS? JOB_ WS? (jobParameters)* (COMMA)? (
		idxNumber
	)? (NEWLINE+ | EOF) continueStatement*;
jobParameters:
	COMMA* jobParam (COMMA (NEWLINE DSLASH_ WS)? (jobParam)?)*;
jobParam: (jobParamName '=')* jobParamValue;
jobParamName: IDENTIFIER;
jobParamValue: paramValue | '(' paramValueList ')';

execStatement:
	DSLASH_ (cname)? WS? EXEC_ WS (execParameters)* (COMMA)? (
		idxNumber
	)? (NEWLINE+ | EOF) continueStatement* (
		ddStatement
		| includeStatement
	)*;
execParameters: execParam (COMMA (execParam)?)*;
execParam: (execParamName '=')* execParamValue;
execParamName: IDENTIFIER | keyword;
execParamValue: paramValue | '(' paramValueList ')';
includeStatement:
	DSLASH_ cname? WS? INCLUDE_ WS MEMBER_ '=' memberName (
		NEWLINE+
	);
memberName: IDENTIFIER;

jcllibStatement:
	DSLASH_ (cname)? WS? JCLLIB_ WS? (jobParameters)* (COMMA)? (
		idxNumber
	)? (NEWLINE+ | EOF) continueStatement*;
setStatement:
	DSLASH_ (cname)? WS? SET_ WS? (jobParameters)* (COMMA)? (
		idxNumber
	)? (NEWLINE+ | EOF) continueStatement*;
procStatement:
	DSLASH_ (cname)? WS? PROC_ WS? procParameters? (COMMA)? NEWLINE execStatement* procEnd?;
// | DSLASH_ (cname)? WS? PROC_ WS? (procParameters (COMMA)? (idxNumber)? (NEWLINE+|EOF))
procEnd: (DSLASH_ | '/' cname?) WS+ PEND_ (NEWLINE+ | EOF);

procParameters: (STAR | procParam) (
		COMMA (NEWLINE DSLASH_ WS)? (WS? procParam)?
	)* (COMMA)?;
procParam: (ddParamName '=')+ ddParamValue?;

ddStatement:
	DSLASH_ (cname)? WS? DD_ WS? (
		(
			ddParameters (COMMA)? (idxNumber)? (NEWLINE+ | EOF) (
				continueStatement
				| inline
			)*
		)
		| (STAR (COMMA)? (idxNumber)? (NEWLINE+) inline*)
	)*;

STAR: '*'; // slines?;

keyword: STAR | DD_ | END_ | EXEC_ | SET_ | PROC_;

// slines: (sline)+; sline: IDENTIFIER* (idxNumber)? (NEWLINE);

ddParameters: (STAR | ddParam) ((COMMA | WS) (ddParam)?)* (COMMA)?;
ddParam: (ddParamName '=')* ddParamValue;
ddParamName: IDENTIFIER | keyword;
ddParamValue: paramValue | '(' (ddParameters) ')';

paramValueList: (COMMA)? paramValue (COMMA paramValue)*;
paramValue: (accessName? '(' paramValueList ')') | value;

// text: TEXT ('\n'|EOF); SLASH : '/' {input.LA(-2) == '\n'}?; TEXT: ~[\r\n]+;

cname: IDENTIFIER | charDataKeyword;
idxNumber: WS IDENTIFIER;

avalue: (
		STRING
		| STRING2
		| NUMBER
		| accessName
		| keyword
		| charDataKeyword
		| '()'
	);
value: avalue | avalue ')';
accessName:
	'*.'? (IDENTIFIER | charDataKeyword) (
		'.' (IDENTIFIER | charDataKeyword)
	)*;
IDENTIFIER: ~[ \t\r\n/=,()*]+;
STRING: '"' .*? '"';
STRING2: '\'' .*? '\'';
NUMBER: [0-9]+;

WS: [ \t]+; //-> skip ;

comment: LINECOMMENT;
LINECOMMENT:
	'/'? '/*' ~[\r\n]* (NEWLINE | EOF) -> channel(HIDDEN);
INLINECOMMENT:
	'<==' ~[\r\n]* (NEWLINE | EOF) -> channel(HIDDEN);
NEWLINE: [\r\n]+;
// NS: ~[\r\n/]+;
charDataKeyword:
	DATASET_
	| BACKUP_
	| LIST_
	| FROM_
	| TO_
	| SORT_
	| JOBLIB_
	| MEMBER_;
inline: ~DSLASH_ (inlineContent)? idxNumber? (NEWLINE | EOF);
inline2: DSLASH_ (inlineContent)? (NEWLINE | EOF);