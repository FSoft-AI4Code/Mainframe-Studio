grammar Clist;


startRule
    : procedure;

procedure: PROC NUMBER procOption* (statement | label)* (labelEnd|(END | EXIT))?;

labelEnd: labelName COLON (END | exitStatement);


procOption: IDENTIFIER (LPAREN IDENTIFIER? RPAREN)?;
label: labelName COLON statement ;

commandName: AMPCHAR IDENTIFIER;

labelName
    : charDataKeyword | IDENTIFIER
    ;


statement
    : controlStatement
    | attnStatement
    | doEndStatement
    | writeStatement
    | writeNrStatement
    | readStatement
    | smCopyStatement
    | editStatement
    | findStatement
    | changeStatement
    | inlineStatement
    | submitStatement
    | exitStatement
    | insertStatement
    | ifStatement
    | gotoStatement
    | freeFileStatement
    | allocStatement
    | runStatement
    | dsnEndStatement
    | callStatement
    | openfileStatement
    | getfileStatement
    | closefileStatement
    | setStatement
    | ispExecStatement
    | globalStatement
    | deleteStatement
    | attributeStatement
    | listDmsStatement
    | errorStatement
    | returnStatement
    | doWhileStatement
    | putfileStatement
    | readdvalStatement
    | selectStatement
    | execStatement
    | outputStatement
    | cancelStatement
    | kdsPrintStatement
    | hrecoverStatement
    | jprintrStatement
    | hlistStatement
;


hlistStatement: HLIST hlistParameter*;

hlistParameter: generalStatementParemeter;

jprintrStatement: JPRINTR jprintContent jprintParameter*;

jprintContent: stringExpression;

jprintParameter: generalStatementParemeter;

hrecoverStatement: HRECOVER dataset_name hrecoverParameter*;

hrecoverParameter: generalStatementParemeter;

kdsPrintStatement: KDSPRINT kdsPrintParamater*;

kdsPrintParamater: generalStatementParemeter | clist_file_presentation;


cancelStatement: CANCEL job_parameter*;
outputStatement: OUTPUT job_parameter* outputParameter*;

outputParameter: generalStatementParemeter;

job_parameter: job_name LPAREN job_id RPAREN;

job_name: value;

job_id: value;

execStatement: (EXEC|EX) (dataset_name | clist_dataset_presentation
);
selectStatement: SELECT testExpression whenSelect+ otherwiseSelect? (END | ENDO);
otherwiseSelect: OTHERWISE statement;
testExpression: LPAREN variable RPAREN;

whenSelect: WHEN condition statement;

readdvalStatement: READDVAL variable*;

putfileStatement: PUTFILE fileName;

doWhileStatement: DO WHILE condition (statement | label)* (END | ENDO);

returnStatement: RETURN;
errorStatement: ERROR statement;

listDmsStatement: LISTDMS listDmsParameter*;

listDmsParameter: generalStatementParemeter;
attributeStatement: (ATTRIB | ATTR) attribute_name+ attributeStatementParameter*;

attributeStatementParameter: generalStatementParemeter;


deleteStatement: DELETE  dataset_name;

setStatement: SET variable variableAssignment;

variableAssignment: EQUALCHAR (value | calcExpression)?;

globalStatement: GLOBAL variable+;

ispExecStatement
    : ISPEXEC 
    (vgetService
    | ftopenService
    | ftCloseService
    | ftinclService
    | browseService
    | editService
    | fteraseService
    | vputService
    | lminitService
    | lmcopyService
    | lmfreeService
    | tablebService
    | controlService
    | logService
    | displayService
    | addpopService
    | fenService);

fenService: FEN fenParameter?;

fenParameter: IDENTIFIER;
addpopService: ADDPOP addpopServiceParameter*;

addpopServiceParameter: generalStatementParemeter;

displayService: DISPLAY displayParameter*;

displayParameter: generalStatementParemeter;

logService: LOG message;

message: generalStatementParemeter;

controlService: CONTROL controlServiceParameter*;

controlServiceParameter: generalStatementParemeter;

tablebService: tableServiceName table_name tableParameter*;
tableServiceName: TBDISPL | TBQUERY | TBTOP | TBSKIP | TBDELETE | TBSORT | TBMOD | TBOPEN | TBCREATE | TBEND | TBCLOSE|TB;
table_name: referencedVariable (DOT referencedVariable)*;

tableParameter: generalStatementParemeter;

lminitService: LMINIT clist_data_id_presentation clist_dataset_presentation? lminitParameter*;

lmfreeService: LMFREE clist_data_id_presentation;

lmcopyService: LMCOPY fromId fromMem? toDataId toMem? lmcopyParameter*;

fromMem: FROMMEM LPAREN member_name RPAREN;

toMem: TOMEM LPAREN member_name RPAREN;

lmcopyParameter: generalStatementParemeter;

fromId: FROMID LPAREN value RPAREN;

toDataId: TODATAID LPAREN value RPAREN;

lminitParameter: generalStatementParemeter;


fteraseService: FTERASE member_name clist_library_presentation?;
browseService: BROWSE (clist_dataset_presentation | clist_file_presentation | clist_data_id_presentation)? browseServiceParameter*;


browseServiceParameter: generalStatementParemeter;

editService: EDIT (clist_dataset_presentation | clist_file_presentation | clist_data_id_presentation)? editServiceParameter*;

editServiceParameter: generalStatementParemeter;

ftinclService: FTINCL skel_name ftinclParameter*;
skel_name: IDENTIFIER;

ftinclParameter: IDENTIFIER ;

ftCloseService: FTCLOSE ftCloseName? ftCloseLibrary? ftCloseParameter?;

ftCloseName: IDENTIFIER LPAREN member_name RPAREN;

ftCloseLibrary: LIB LPAREN IDENTIFIER RPAREN;

ftCloseParameter: IDENTIFIER;
ftopenService: FTOPEN ftopenServiceParameter?;
ftopenServiceParameter:IDENTIFIER;

vgetService: VGET name_list vgetParameter*;
vputService: VPUT name_list vputParameter*;

name_list: IDENTIFIER | LPAREN name_list_item+ RPAREN | LPAREN name_list_item (COMMACHAR name_list_item)*;

name_list_item: value;

vgetParameter: value;
vputParameter: value;

value: IDENTIFIER | STRING | buildInFuntion | NUMBER | variable | stringExpression | dataset_name | charDataKeyword;

stringExpression: (variable | buildInFuntion | NUMBER | COLON | STRING)+;



// Parser rule
calcExpression
    : expression
    ;

// Expression rules with operator precedence
expression
    : expression (MINUSCHAR | PLUSCHAR) term     #AddSubExpr
    | term                               #ToTerm
    ;

term
    : term (ASTERISKCHAR | DIVCHAR) factor         #MulDivExpr
    | factor                             #ToFactor
    ;

factor
    : LPAREN expression RPAREN                 #ParenExpr
    | value                             #NumberExpr
    ;


closefileStatement: CLOSFILE fileName;

getfileStatement: GETFILE fileName;

openfileStatement: OPENFILE fileName openfileOption?;

openfileOption: IDENTIFIER;

callStatement: CALL dataset_name member_name? callOption*;

member_name: IDENTIFIER | STRING;

callOption: IDENTIFIER;

dsnEndStatement: DSN clist_system_presentation statement (END | ENDO);
runStatement: RUN clist_program_presentation clist_plan_presentation clist_library_presentation clist_params_presentation?;

allocStatement: (ALLOC | ALLOCATE) allocParameter*;

allocParameter: clist_file_presentation | clist_dataset_presentation | otherAllocParameter;

otherAllocParameter: allocParameterName (LPAREN
allocParameterParams RPAREN)?;

allocParameterName: clistKeyword;

allocParameterParams: allocParameterParam (COMMACHAR allocParameterParam)* | allocParameterParam+;

allocParameterParam: clistKeyword | NUMBER | F_CHAR | attribute_name | ASTERISKCHAR | dataset_name;

freeFileStatement: FREE (clist_file_presentation | clist_attribute_presentation | clist_attribute_list_presentation | clist_dataset_presentation)+ ;

clist_attribute_list_presentation: ATTRLIST LPAREN attribute_name+ RPAREN;

clist_attribute_presentation: ATTR LPAREN attribute_name+ RPAREN;


attribute_name: SSLASH? IDENTIFIER;
clist_file_presentation: (FILE|F_CHAR|FI | DDNAME | DDN) LPAREN (fileName* | fileName (COMMACHAR fileName)*) RPAREN;
clist_dataset_presentation: (DATASET|DA | DATA) LPAREN dataset_name+ RPAREN;

clist_program_presentation: PROGRAM LPAREN program_name RPAREN;

clist_plan_presentation: PLAN LPAREN plan_name RPAREN;

clist_library_presentation: (LIB) LPAREN library_name RPAREN;

clist_params_presentation: PARMS LPAREN params_name RPAREN;

clist_system_presentation: SYSTEM LPAREN system_name RPAREN;

clist_data_id_presentation: DATAID LPAREN data_id RPAREN;

data_id: IDENTIFIER;

system_name: IDENTIFIER;

plan_name: IDENTIFIER;
program_name: IDENTIFIER;

library_name: IDENTIFIER | STRING;

params_name: STRING;

fileName: clistKeyword;

generalStatementParemeter: (value) (LPAREN (clistKeyword | attribute_name | NUMBER | variable|signed_number | STRING)+ RPAREN)?;

gotoStatement: GOTO labelName;

ifStatement: IF condition thenIf elseIf? endIf?;

endIf: END | ENDO;

thenIf: THEN statement;

elseIf: ELSE statement?;


clistKeyword: IDENTIFIER | charDataKeyword;


charDataKeyword: DSN | DELETE | F_CHAR | OFF  | CANCEL | ERROR | LOG | DISPLAY | ENDO | DATA | OUTPUT | LIB;
condition
    : combinableCondition andOrCondition*
    ;

andOrCondition
    : (AND | OR | PIPECHAR) (combinableCondition | NUMBER)
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
    : (arithmeticExpression relationalOperator)? (arithmeticExpression | END)
    ;

arithmeticExpression
    : value
    ;

relationalOperator: EQUALCHAR | GREATERTHANCHAR | LESSTHANCHAR | EQ;

insertStatement: INSERT stringFuntion;

exitStatement: EXIT exitParameters*;

exitParameters: generalStatementParemeter;

submitStatement: SUBMIT (dataset_name | jcl_code_submited);

jcl_code_submited: ASTERISKCHAR END LPAREN jcl_code_start_and_end_symbol RPAREN jcl_code jcl_code_start_and_end_symbol;

jcl_code: .*?;

jcl_code_start_and_end_symbol: DOUBLE_ADOTCHAR;


inlineStatement: PERCENTAGECHAR (CLEAR | IDENTIFIER);

changeStatement: CHANGE changeString orignalString changeParameter*;
changeParameter: generalStatementParemeter;
changeString: STRING;
orignalString: stringExpression;

findStatement: FIND findString;

findString: STRING;


editStatement: EDIT dataset_name editOption*;



editOption: clistKeyword | END;
smCopyStatement: (SMCOPY | SMC) smCopyFrom smCopyTo smCopyOption* 
// smCopyLine?
;

smCopyFrom: fromDataset;

fromDataset: (FROMDATASET | FDS) LPAREN (dataset_name) RPAREN;

smCopyTo: toDataset;

toDataset: (TODATASET | TDS) LPAREN (dataset_name) RPAREN;

smCopyOption: IDENTIFIER | NOT;




readStatement: READ variable*;

variable: IDENTIFIER | referencedVariable | charDataKeyword | normalVariableCombineWithReferenced;

normalVariableCombineWithReferenced: (IDENTIFIER | referencedVariable)+;

referencedVariable: AMPCHAR (clistKeyword);

writeNrStatement: WRITESTATMENT;
writeStatement: WRITESTATMENT;


WRITESTATMENT: (WRITE | WRITENR) WS .*? NEWLINE;

attnStatement: ATTN (OFF | statement);

controlStatement: CONTROL (controlOption)*;

controlOption
    : clistKeyword | (END | IDENTIFIER) (LPAREN clistKeyword RPAREN)? 
    ;

doEndStatement: DO ((statement | label)* | clist_file_name) (END | ENDO | labelEnd);

clist_file_name: IDENTIFIER;

buildInFuntion: stringFuntion | subStringFunction | lengthFunction | otherBuildInFunction;

otherBuildInFunction: function_name LPAREN function_parameter* RPAREN;

function_name: AMPCHAR clistKeyword;

function_parameter: value;

lengthFunction: AMPCHAR LENGTH LPAREN stringExpression RPAREN;

subStringFunction: AMPCHAR SUBSTR LPAREN partToSubString COMMACHAR stringToSubString RPAREN;

partToSubString: startIndex COLON endIndex;

startIndex: intergerLiteral;

endIndex: intergerLiteral;

intergerLiteral: NUMBER | referencedVariable;

stringToSubString: STRING | variable;

stringFuntion: AMPCHAR STR LPAREN STRING RPAREN;
dataset_name: dataset_part (DOT dataset_part?)* | STRING | ASTERISKCHAR;

dataset_part: IDENTIFIER (LPAREN IDENTIFIER RPAREN)? | variable;

signed_number: (PLUSCHAR | MINUSCHAR) NUMBER;

COMMENTLINE_2
    : '/*' ~('\n' | '\r')* -> channel(HIDDEN)
    ;

STRING
    : '"' .*? '"' | '\'' .*? '\''
    ;
NEWLINE
    : '\r'? '\n' -> channel(HIDDEN)
    ;

WS
    : [ \t\f;]+ -> channel(HIDDEN)
    ;

SEPARATOR
    : ', ' -> channel(HIDDEN)
    ;

SEPARATOR_2
    : ',\n' -> channel(HIDDEN)
    ;
DATAENDDATASEQUENCE : DATA .*? ENDDATA -> channel(HIDDEN)
    ;


LPAREN:'(';
RPAREN: ')';
COLON: ':'
    ;
PLUSCHAR: '+';
GREATERTHANCHAR: '>';
LESSTHANCHAR: '<';
MINUSCHAR: '-';

DIVCHAR: '/';
SSLASH: '\\';
PIPECHAR: '|';
ASTERISKCHAR
    : '*'
    ;
DOUBLE_ADOTCHAR
    : '@@';
AMPCHAR
    : '&'
    ;
PERCENTAGECHAR: '%';

EQUALCHAR: '=';

DOT: '.';
COMMACHAR: ',';
ATTN: A T T N;
OFF: O F F
    ;
DATA: D A T A;
ALLOCATE: A L L O C A T E;
ALLOC: A L L O C;

PROGRAM: P R O G R A M;

PLAN: P L A N;


LIB: L I B;

PARMS: P A R M S;

RUN: R U N;

CLOSFILE: C L O S F I L E;

DSN: D S N;

SYSTEM: S Y S T E M;

ENDDATA: E N D D A T A
    ;
DDNAME: D D N A M E;
DDN: D D N;

HRECOVER: H R E C O V E R;
CONTROL: C O N T R O L
    ;
FEN: F E N;
TB: T B;
CALL: C A L L;
CLEAR: C L E A R;
DO    : D O
    ;
CANCEL: C A N C E L;
OUTPUT: O U T P U T;
FROMID: F R O M I D;
TODATAID: T O D A T A I D;
FROMMEM: F R O M M E M;
TOMEM: T O M E M;
SELECT: S E L E C T;
EDIT: E D I T;
KDSPRINT: K D S P R I N T;
TBDISPL: T B D I S P L;
TBQUERY: T B Q U E R Y;
TBTOP: T B T O P;
TBSKIP: T B S K I P;
TBDELETE: T B D E L E T E;
TBSORT: T B S O R T;
TBMOD: T B M O D;
TBOPEN: T B O P E N;
TBCREATE: T B C R E A T E;
TBEND: T B E N D;
TBCLOSE: T B C L O S E;
EXIT: E X I T;
LMINIT: L M I N I T;
LMCOPY: L M C O P Y;
LMFREE: L M F R E E;
PROC: P R O C    ;

LENGTH: L E N G T H;

END : E N D
    ;
WHEN: W H E N;
HLIST: H L I S T;
OTHERWISE: O T H E R W I S E;
READDVAL: R E A D D V A L;
CHANGE    : C H A N G E
    ;
OPENFILE: O P E N F I L E;
JPRINTR: J P R I N T R;
GETFILE: G E T F I L E;
FREE: F R E E;
FILE: F I L E;
INSERT: I N S E R T;
IF: I F;
THEN: T H E N;
FIND: F I N D;
READ    : R E A D
    ;
PUTFILE: P U T F I L E;
LISTDMS: L I S T D M S ;
WHILE: W H I L E;
ERROR: E R R O R;
RETURN: R E T U R N;
WRITE    : W R I T E
    ;
WRITENR: W R I T E N R;
SMCOPY: S M C O P Y
    ;
SMC: S M C
    ;
ENDO: E N D O;
ADDPOP: A D D P O P;
LOG: L O G;
EXEC: E X E C;
EX: E X;
FI: F I;
EQ: E Q;
ATTRIB: A T T R I B;
SUBSTR: S U B S T R;
STR    : S T R
    ;

GOTO: G O T O
    ;
ATTRLIST: A T T R L I S T;
DELETE: D E L E T E;
GLOBAL: G L O B A L;
ATTR: A T T R;
NOT: N O T;
AND: A N D;
ELSE: E L S E;
OR: O R;
FROMDATASET    : F R O M D A T A S E T
    ;
DATAID: D A T A I D;
VGET: V G E T;
VPUT: V P U T;
BROWSE: B R O W S E;
ISPEXEC: I S P E X E C
    ;
DISPLAY: D I S P L A Y;
FTOPEN: F T O P E N;
FTCLOSE: F T C L O S E;
FTINCL: F T I N C L
    ;
FTERASE: F T E R A S E;

FDS: F D S    ;

TODATASET    : T O D A T A S E T
    ;
TDS: T D S    ;
SUBMIT    : S U B M I T
    ;

DATASET: D A T A S E T;

DA: D A;

SET: S E T;




F_CHAR: F;

NUMBER
    : [0-9]+
    ;
IDENTIFIER
    : [a-zA-Z0-9#@]+ ([_/]+ [a-zA-Z0-9#]+)*
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
