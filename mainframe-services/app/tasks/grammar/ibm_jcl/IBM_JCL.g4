grammar IBM_JCL;

program: (statement)*  (END_)*  WS? EOF;
statement:  continueStatement|jobStatement|execStatement|jcllibStatement|setStatement|procStatement;

inline: ~DSLASH_ (inlineContent)?  idxNumber? (NEWLINE|EOF);
inline2: DSLASH_ (inlineContent)?  (NEWLINE|EOF);

inlineContent:  ~NEWLINE+ ;

JOB_:'JOB';
EXEC_:'EXEC';
DD_:'DD';
END_:'END';
JCLLIB_:'JCLLIB';
DSLASH_:'//';
SET_:'SET';
PROC_:'PROC';
COMMA: ','|', ';
// emptyStatement:  DSLASH_ (idxNumber)? NEWLINE;
continueStatement: (DSLASH_|'/'cname?) WS+ (ddParameters)+  (idxNumber)? (NEWLINE+|EOF) ;

jobStatement: DSLASH_ (cname)? WS? JOB_ WS? (jobParameters)* (COMMA)? (idxNumber)? (NEWLINE+|EOF) continueStatement*; 
jobParameters: COMMA* jobParam (COMMA (jobParam)?)* ;
jobParam: (jobParamName '=')* jobParamValue;
jobParamName:IDENTIFIER;
jobParamValue: paramValue | '(' paramValueList ')';

execStatement: DSLASH_ (cname)? WS? EXEC_ WS (execParameters)* (COMMA)? (idxNumber)? (NEWLINE+|EOF)  continueStatement* ddStatement*;
execParameters:execParam (COMMA (execParam)?)* ;
execParam: (execParamName '=')* execParamValue;
execParamName:IDENTIFIER|keyword;
execParamValue: paramValue| '(' paramValueList ')';

jcllibStatement: DSLASH_ (cname)? WS? JCLLIB_ WS? (jobParameters)* (COMMA)? (idxNumber)? (NEWLINE+|EOF) continueStatement*; 
setStatement: DSLASH_ (cname)? WS? SET_ WS? (jobParameters)* (COMMA)? (idxNumber)? (NEWLINE+|EOF) continueStatement*; 
procStatement: DSLASH_ (cname)? WS? PROC_ WS? ((procParameters (COMMA)? (idxNumber)? (NEWLINE+|EOF) (inline2)*)
            |(STAR (COMMA)? (idxNumber)? (NEWLINE+) inline2*))*
            ;

procParameters:  (STAR|procParam) (COMMA (WS? procParam)?)* (COMMA)? ;
procParam: (ddParamName '=')+ ddParamValue?;

ddStatement: DSLASH_ (cname)? WS? DD_ WS? ((ddParameters (COMMA)? (idxNumber)? (NEWLINE+|EOF) (continueStatement|inline)*)
            |(STAR (COMMA)? (idxNumber)? (NEWLINE+) inline*))*
            ;


STAR: '*';// slines?;

keyword: STAR|DD_|END_|EXEC_|DSLASH_|SET_|PROC_;

// slines: (sline)+;
// sline: IDENTIFIER* (idxNumber)? (NEWLINE);

ddParameters:  (STAR|ddParam) (COMMA (ddParam)?)* (COMMA)? ;
ddParam: (ddParamName '=')* ddParamValue;
ddParamName:IDENTIFIER|keyword;
ddParamValue:  paramValue| '(' (ddParameters) ')' ;

paramValueList: (COMMA)? paramValue (COMMA paramValue)*;
paramValue: (accessName?'(' paramValueList ')') |value ;


// text:  TEXT ('\n'|EOF);
// SLASH : '/' {input.LA(-2) == '\n'}?;
// TEXT: ~[\r\n]+;

cname: IDENTIFIER;
idxNumber: WS IDENTIFIER;

avalue : (STRING | STRING2 | NUMBER | accessName|keyword);
value: avalue | avalue ')';
accessName: '*.'? IDENTIFIER ('.' IDENTIFIER)* ;
IDENTIFIER: ~[ \t\r\n/=,()*]+ ;
STRING: '"' .*? '"' ;
STRING2: '\'' .*? '\'' ;
NUMBER: [0-9]+ ;

WS: [ \t]+ ;//-> skip ;

comment: LINECOMMENT  ;
LINECOMMENT
    : '/'?'/*' ~[\r\n]* (NEWLINE|EOF)  -> channel(HIDDEN)
    ;

NEWLINE: [\r\n]+;
// NS: ~[\r\n/]+;
