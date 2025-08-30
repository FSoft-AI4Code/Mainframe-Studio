/**
 * Grammar Assembler
 */

grammar asm;

startRule:
    line+ EOF
    ;

line:
    label? (instruction | macro | comment) EOL
    ;

label:
    LABEL_IDENTIFIER
    | IDENTIFIER
    | GET
    | WTO
    | DCB
    ;

instruction:
    load_store_instruction
    | arithmetric_instruction
    | logical_instruction
    | branch_instruction
    | decimal_instruction
    | special_instruction
    | assembler_instruction
    | other_instruction
    ;

load_store_instruction:
    ic_statement
    | icm_statement
    | l_statement
    | la_statement
    | lcr_statement
    | lh_statement
    | lhi_statement
    | lm_statement
    | lnr_statement
    | lpr_statement
    | lr_statement
    | ltr_statement
    | mvc_statement
    | mvcl_statement
    | mvi_statement
    | st_statement
    | stc_statement
    | stcm_statement
    | sth_statement
    | stm_statement
    ;

arithmetric_instruction:
    a_statement
    | ah_statement
    | ahi_statement
    | al_statement
    | alr_statement
    | ar_statement
    | c_statement
    | ch_statement
    | cr_statement
    ;

logical_instruction:
    cl_statement
    | clc_statement
    | clcl_statement
    | cli_statement
    | clm_statement
    | clr_statement
    | n_statement
    | nc_statement
    | ni_statement
    | nr_statement
    | o_statement
    | oc_statement
    | oi_statement
    | or_statement
    | sla_statement
    | slda_statement
    | sldl_statement
    | sll_statement
    | sra_statement
    | srda_statement
    | srl_statement
    | tm_statement
    | x_statement
    | xc_statement
    | xi_statement
    | xr_statement
    ;

branch_instruction:
    bal_statement
    | balr_statement
    | bas_statement
    | basr_statement
    | bc_statement
    | bcr_statement
    | bct_statement
    | bctr_statement
    | bxh_statement
    | bxle_statement
    ;

decimal_instruction:
    ap_statement
    | cp_statement
    | cvp_statement
    | cvd_statement
    | dp_statement
    | ed_statement
    | edmk_statement
    | mp_statement
    | mvn_statement
    | mvo_statement
    | mvz_statement
    | pack_statement
    | sp_statement
    |srp_statement
    | unpk_statement
    | zap_statement
    ;

special_instruction:
    cs_statement
    | cds_statement
    | ex_statement
    | stck_statement
    | svc_statement
    | tr_statement
    | trt_statement
    | ts_statement
    ;

assembler_instruction:
    amode_statement
    | csect_statement
    | dc_statement
    | dsect_statement
    | drop_statement
    | ejec_statement
    | end_statement
    | equ_statement
    | ltorg_statement
    | org_statement
    | pop_statement
    | print_statement
    | push_statement
    | rmode_statement
    | space_statement
    | title_statement
    | using_statement
    ;

// Add other statement
other_instruction:
    wto_statement
    | extract_statement
    | display_statement
    | cnop_statement
    | comp_statement
    | be_statement
    | move_statement
    | write_statement
    | bh_statement
    | bo_statement
    | bl_statement
    | b_statement
    | bne_statement
    | br_statement
    | bz_statement
    | bnl_statement
    | slr_statement
    | sr_statement
    | mh_statement
    | ds_statement
    | and_statement
    | start_statement
    | getmain_statement
    ;

getmain_statement:
    GETMAIN getmain_params
    ;

getmain_params:
    R_CHAR COMMA getmain_param_list
    | operand_list
    ;

getmain_param_list:
    getmain_param (COMMA getmain_param)*
    ;

getmain_param:
    LV EQUAL number
    | SP EQUAL number
    | identifier EQUAL number
    | identifier EQUAL identifier
    ;
  
macro:
    abend_statement
    | call_statement
    | close_statement
    | dcb_statement
    | get_statement
    | open_statement
    | put_statement
    | return_statement
    | save_statement
    | storage_statement
    | yregs_statement
    ;

// Comments
comment:
    single_line_comment
    | multiline_comment
    ;

single_line_comment:
    SINGLE_LINE_COMMENT
    ;

multiline_comment:
    MULTILINE_COMMENT
    ;

// Operands
operand:
    identifier
    | register 
    | symbol
    | memory_reference
    | character_literal
    | hex_literal
    | halfword_literal
    | cl_literal
    | xl_literal
    | b_literal
    | pl_literal
    | f_literal
    | displacement_expression
    | displacement_with_length
    | indexed_memory_reference
    | addr_expression
    | calc_expression
    | r_register
    | GET
    | number
    | hash_label
    ;
    
hash_label:
    HASH_LABEL
    ;

calc_expression:
    identifier PLUS number
    | identifier MINUS number
    ;

addr_expression:
    '=A' LP expression RP
    ;

expression:
    term (PLUS term)*
    | term (MINUS term)*
    ;

term:
    identifier
    | number
    ;

displacement_expression:
    identifier PLUS number (LP number RP)?
    | identifier MINUS number (LP number RP)?
    ;

displacement_with_length:
    identifier PLUS number LP number RP
    | identifier MINUS number LP number RP
    ;

// C'...'
character_literal:
    EQUAL? C_CHAR STRING
    ;

// X'...' or 6X'F0' etc.
hex_literal:
    (EQUAL? X_CHAR | number X_CHAR) STRING
    ;

// H'...'
halfword_literal:
    EQUAL? H_CHAR STRING
    ;

// CL'...'
cl_literal:
    EQUAL? C_CHAR L_CHAR (NUMBER)? STRING
    ;

// XL'...'
xl_literal:
    EQUAL? X_CHAR L_CHAR (NUMBER)? STRING
    ;

// B'...'
b_literal:
    EQUAL? B_CHAR STRING
    ;

// F'...'
f_literal:
    EQUAL? F_CHAR STRING
    ;

pl_literal:
    EQUAL? P_CHAR L_CHAR (NUMBER)? STRING
    ;

memory_reference:
    number LP number RP
    | number LP identifier RP
    | number LP register RP
    | number LP identifier COMMA identifier RP
    | base_register_reference
    ;

base_register_reference:
    identifier LP register RP
    | identifier LP number RP
    | identifier LP identifier RP
    | identifier LP number COMMA register RP
    ;

indexed_memory_reference:
    number LP number COMMA identifier RP
    | number LP number COMMA register RP
    ;

identifier:
    IDENTIFIER
    | GET
    | WTO
    | END
    | P_HASH_LABEL
    ;

symbol:
    ASTERISK
    ;

operand_list:
    operand (COMMA operand)*
    ;

relative_branch:
    ASTERISK PLUS NUMBER
    | ASTERISK MINUS NUMBER
    ;

// Register definitions
register:
    REGISTER
    ;

// Implementation of Load/Store Instructions
ic_statement:
    IC ic_operand_list
    ;

ic_operand_list:
    ic_operand (COMMA ic_operand)*
    ;

ic_operand:
    register
    | memory_reference
    | indexed_memory_reference
    | base_register_reference
    | identifier LP identifier RP
    | identifier
    ;

icm_statement:
    ICM operand_list
    ;

l_statement:
    L_CHAR operand_list
    ;

number:
    NUMBER
    ;


la_statement:
    LA operand_list
    ;

lcr_statement:
    LCR operand_list
    ;

lh_statement:
    LH operand_list
    ;

lhi_statement:
    LHI operand_list
    ;

lm_statement:
    LM operand_list
    ;

lnr_statement:
    LNR operand_list
    ;

lpr_statement:
    LPR operand_list
    ;

lr_statement:
    LR operand_list
    ;

ltr_statement:
    LTR operand_list
    ;

mvc_statement:
    MVC operand_list
    ;

mvcl_statement:
    MVCL operand_list
    ;

mvi_statement:
    MVI operand_list
    ;

st_statement:
    ST operand_list
    ;

stc_statement:
    STC operand_list
    ;

stcm_statement:
    STCM operand_list
    ;

sth_statement:
    STH operand_list
    ;

stm_statement:
    STM operand_list
    ;

// Implementation of Arithmetic Instructions
a_statement:
    A_CHAR operand_list
    ;

ah_statement:
    AH operand_list
    ;

ahi_statement:
    AHI operand_list
    ;

al_statement:
    AL operand_list
    ;

alr_statement:
    ALR operand_list
    ;

ar_statement:
    AR operand_list
    ;

c_statement:
    C_CHAR operand_list
    ;

ch_statement:
    CH operand_list
    ;

cr_statement:
    CR operand_list
    ;

// Implementation of Logical Instructions

cl_statement:
    CL operand_list
    ;

clc_statement:
    CLC operand_list
    ;

clcl_statement:
    CLCL operand_list
    ;

cli_statement:
    CLI operand_list
    ;

clm_statement:
    CLM operand_list
    ;

clr_statement:
    CLR operand_list
    ;

n_statement:
    N_CHAR operand_list
    ;

nc_statement:
    NC operand_list
    ;

ni_statement:
    NI operand_list
    ;

nr_statement:
    NR operand_list
    ;

o_statement:
    O_CHAR operand_list
    ;

oc_statement:
    OC operand_list
    ;

oi_statement:
    OI operand_list
    ;

or_statement:
    OR operand_list
    ;

sla_statement:
    SLA operand_list
    ;

slda_statement:
    SLDA operand_list
    ;

sldl_statement:
    SLDL operand_list
    ;

sll_statement:
    SLL operand_list
    ;

sra_statement:
    SRA operand_list
    ;

srda_statement:
    SRDA operand_list
    ;

srl_statement:
    SRL operand_list
    ;

tm_statement:
    TM operand_list
    ;

x_statement:
    X_CHAR operand_list
    ;

xc_statement:
    XC operand_list
    ;

xi_statement:
    XI operand_list
    ;

xr_statement:
    XR operand_list
    ;

// Implementation of Branch Instructions
bal_statement:
    BAL bal_operand_list
    ;

bal_operand_list:
    bal_operand (COMMA bal_operand)*
    ;

bal_operand:
    register
    | identifier
    ;

balr_statement:
    BALR operand_list
    ;

bas_statement:
    BAS operand_list
    ;

basr_statement:
    BASR operand_list
    ;

bc_statement:
    BC operand_list
    ;

bcr_statement:
    BCR operand_list
    ;

bct_statement:
    BCT operand_list
    ;

bctr_statement:
    BCTR operand_list
    ;

bxh_statement:
    BXH operand_list
    ;

bxle_statement:
    BXLE operand_list
    ;

// Implementation of Decimal Instructions

ap_statement:
    AP operand_list
    ;

cp_statement:
    CP operand_list
    ;

cvp_statement:
    CVP operand_list
    ;

cvd_statement:
    CVD operand_list
    ;

dp_statement:
    DP operand_list
    ;

ed_statement:
    ED operand_list
    ;

edmk_statement:
    EDMK operand_list
    ;

mp_statement:
    MP operand_list
    ;

mvn_statement:
    MVN operand_list
    ;

mvo_statement:
    MVO operand_list
    ;

mvz_statement:
    MVZ operand_list
    ;

pack_statement:
    PACK operand_list
    ;

sp_statement:
    SP operand_list
    ;

srp_statement:
    SRP operand_list
    ;

unpk_statement:
    UNPK operand_list
    ;

zap_statement:
    ZAP operand_list
    ;

// Implementation of Special Instructions

cs_statement:
    CS operand_list
    ;

cds_statement:
    CDS operand_list
    ;

ex_statement:
    EX operand_list
    ;

stck_statement:
    STCK operand_list
    ;

svc_statement:
    SVC operand_list
    ;

tr_statement:
    TR operand_list
    ;

trt_statement:
    TRT operand_list
    ;

ts_statement:
    TS operand_list
    ;

// Implementation of Assembler Instructions

amode_statement:
    AMODE operand_list
    ;

csect_statement:
    CSECT
    ;

dc_statement:
    DC dc_operand_list
    ;

dc_operand_list:
    dc_operand (COMMA dc_operand)*
    ;

dc_operand:
    dc_constant
    | identifier
    | register
    | symbol
    | hex_literal
    | character_literal
    | halfword_literal
    | cl_literal
    | xl_literal
    | b_literal
    | pl_literal
    | f_literal
    | address_constant
    ;

dc_constant:
    DC_CONSTANT
    ;

address_constant:
    A_CHAR LP (number | identifier) RP
    ;

dsect_statement:
    DSECT
    ;

drop_statement:
    DROP operand_list
    ;

ejec_statement:
    EJECT
    ;

end_statement:
    END (identifier)?
    ;

equ_statement:
    EQU equ_value
    ;

equ_value: 
    NUMBER
    | ASTERISK
    | hex_literal
    | character_literal
    | halfword_literal
    | cl_literal
    | xl_literal
    | b_literal
    | pl_literal
    | f_literal
    ;

ltorg_statement:
    LTORG
    ;

org_statement:
    ORG operand_list
    ;

pop_statement:
    POP operand_list
    ;

print_statement:
    PRINT operand_list
    ;

push_statement:
    PUSH operand_list
    ;

rmode_statement:
    RMODE operand_list
    ;

space_statement:
    SPACE operand_list
    ;

title_statement:
    TITLE operand_list
    ;

using_statement:
    USING ASTERISK (COMMA using_operand)+
    ;

using_operand:
    register
    | number
    ;

// Implementation of Macro Instructions

abend_statement:
    ABEND operand_list
    ;

call_statement:
    CALL call_operand_list
    ;

call_operand_list:
    call_operand (COMMA call_operand)*
    ;

call_operand:
    identifier
    | LP identifier COMMA identifier RP
    | vl_operand
    ;

vl_operand: 
    VL
    ;

close_statement:
    CLOSE LP params RP
    ;

dcb_statement:
    DCB dcb_params
    ;

dcb_params:
    dcb_param (COMMA dcb_param)*
    ;

dcb_param:
    dcb_key_value
    ;

dcb_key_value:
    identifier EQUAL identifier
    | identifier EQUAL number
    | identifier EQUAL END
    ;

get_statement:
    GET operand_list
    ;

open_statement:
    OPEN LP open_operand_list RP
    ;

open_operand_list:
    open_operand (COMMA open_operand)*
    ;

open_operand:
    identifier
    | LP identifier RP
    ;

put_statement:
    PUT operand_list
    ;

return_statement:
    RETURN (LP params RP| number)
    ;

save_statement:
    SAVE LP params RP
    ;

params:
    param (COMMA param)*
    ;

param:
    NUMBER
    | identifier
    ;

storage_statement:
    STORAGE operand_list
    ;

yregs_statement:
    YREGS
    ;

wto_statement:
    WTO (STRING | operand_list)
    ;

extract_statement:
    EXTRACT operand_list
    ;

display_statement:
    DISPLAY LP display_msg RP (COMMA r_register)?
    ;

r_register:
    R_CHAR (PLUS number)? LP number RP
    | R_CHAR LP number RP
    ;

display_msg:
    STRING
    ;

cnop_statement:
    CNOP operand_list
    ;

comp_statement:
    COMP operand_list
    ;

be_statement:
    BE (identifier | END)
    ;

move_statement:
    MOVE operand_list
    ;

write_statement:
    WRITE operand_list
    ;

bh_statement:
    BH operand_list
    ;

bo_statement:
    BO operand_list
    ;

bl_statement:
    BL operand_list
    ;

b_statement:
    B_CHAR operand_list
    ;

bne_statement:
    BNE operand_list
    ;

br_statement:
    BR operand_list
    ;

bz_statement:
    BZ operand_list
    ;

bnl_statement:
    BNL operand_list
    ;

slr_statement:
    SLR operand_list
    ;

sr_statement:
    SR operand_list
    ;

mh_statement:
    MH operand_list
    ;

ds_statement:
    DS operand_list
    ;

and_statement:
    AND operand_list
    ;

start_statement:
    START
    ;

// Lexer Rules

// Single character

A_CHAR: A ;

B_CHAR: B ;

C_CHAR: C ;

D_CHAR: D ;

N_CHAR: N ;

O_CHAR: O ;

L_CHAR: L ;

R_CHAR: R ;

S_CHAR: S ;

P_CHAR: P ;

H_CHAR: H ;

X_CHAR: X ;

Y_CHAR: Y ;

Z_CHAR: Z ;

V_CHAR: V ;

F_CHAR: F ;

// Keywords

LA: L A ;

LCR: L C R ;

LH: L H ;

LHI: L H I ;

LM: L M ;

LNR: L N R ;

LPR: L P R ;

LR: L R ;

LTR: L T R ;

AH: A H ;

AHI: A H I ;

AL: A L ;

ALR: A L R ;

AR: A R ;

CH: C H ;

CR: C R ;

CL: C L ;

CLC: C L C ;

CLCL: C L C L ;

CLI: C L I ;

CLM: C L M ;

CLR: C L R ;

NC: N C ;

NI: N I ;

NR: N R ;

OC: O C ;

OI: O I ;

OR: O R ;

SLA: S L A ;

SLDA: S L D A ;

SLDL: S L D L ;

SLL: S L L ;

SRA: S R A ;

SRDA: S R D A ;

SRL: S R L ;

TM: T M ;

XC: X C ;

XI: X I ;

XR: X R ;

BAL: B A L ;

BALR: B A L R ;

BAS: B A S ;

BASR: B A S R ;

BC: B C ;

BCR: B C R ;

BCT: B C T ;

BCTR: B C T R ;

BXH: B X H ;

BXLE: B X L E ;

AP: A P ;

CP: C P ;

CVP: C V P ;

CVD: C V D ;

DP: D P ;

ED: E D ;

EDMK: E D M K ;

MP: M P ;

MVN: M V N ;

MVO: M V O ;

MVZ: M V Z ;

PACK: P A C K ;

SP: S P ;

SRP: S R P ;

UNPK: U N P K ;

ZAP: Z A P ;

CS: C S ;

CDS: C D S ;

EX: E X ;

STCK: S T C K ;

SVC: S V C ;

TR: T R ;

TRT: T R T ;

TS: T S ;

AMODE: A M O D E ;

CSECT: C S E C T ;

DC: D C ;

DSECT: D S E C T ;

DROP: D R O P ;

EJECT: E J E C T ;

END: E N D ;

EQU: E Q U ;

LTORG: L T O R G ;

ORG: O R G ;

POP: P O P ;

PRINT: P R I N T ;

PUSH: P U S H ;

RMODE: R M O D E ;

SPACE: S P A C E ;

TITLE: T I T L E ;

USING: U S I N G ;

ABEND: A B E N D ;

CALL: C A L L ;

CLOSE: C L O S E ;

DCB: D C B ;

GET: G E T ;

OPEN: O P E N ;

PUT: P U T ;

RETURN: R E T U R N ;

SAVE: S A V E ;

STORAGE: S T O R A G E ;

YREGS: Y R E G S ;

WTO: W T O ;

EXTRACT: E X T R A C T ;

DISPLAY: D I S P L A Y ;

CNOP: C N O P ;

DB: D B ;

FD: F D ;

GR: G R;

MVC: M V C ;

MVCL: M V C L ;

MVI: M V I ;

ST: S T ;

STC: S T C ;

STCM: S T C M ;

STH: S T H ;

STM: S T M ;

IC: I C ;

ICM: I C M ;

COMP: C O M P ;

BE: B E ;

MOVE: M O V E ;

WRITE: W R I T E ;

BH: B H ;

BO: B O ;

BL: B L ;

BNE: B N E ;

BR: B R ;

BZ: B Z ;

BNL: B N L ;

SLR: S L R ;

SR: S R ;

MH: M H ;

DS: D S ;

AND: A N D ;

START: S T A R T ;

GETMAIN: G E T M A I N ;

LV: L V ;

VL: V L ;

// Symbols

DOT: '.' ;
COMMA: ',' ;
LP: '(' ;
RP: ')' ;
PLUS: '+' ;
MINUS: '-' ;
EQUAL: '=' ;
ASTERISK: '*' ;
HASH_SIGN: '#' ;


IDENTIFIER:
    [A-Z][A-Za-z0-9]*
    ;

LABEL_IDENTIFIER:
    [A-Z@#][A-Za-z0-9#]*
    | P_HASH_LABEL
    ;

P_HASH_LABEL:
    'P#' [0-9A-Za-z]+
    ;

HASH_LABEL:
    '#' [0-9]+
    ;

REGISTER:
    R_CHAR [0-9]+
    | GR [0-9]+
    ;

NUMBER:
    [0-9]+
    ;

STRING:
    '\'' (~['\r\n])* '\''
    ;


SINGLE_LINE_COMMENT:
    '*' ~[\r\n]* 
    ;

MULTILINE_COMMENT:
    '/*' .*? '*/'
    ;

EOL:
    [\r\n]+
    ;

WS:
    [ \t]+ -> skip
    ;

// Special characters for Japanese text
SPECIAL_CHAR:
    [¥£¢¬]
    ;

DC_CONSTANT:
    [0-9]+ [A-Z] '(' [0-9]+ ')'
    ;

// fragments

fragment A: 'A';
fragment B: 'B';
fragment C: 'C';
fragment D: 'D';
fragment E: 'E';
fragment F: 'F';
fragment G: 'G';
fragment H: 'H';
fragment I: 'I';
fragment J: 'J';
fragment K: 'K';
fragment L: 'L';
fragment M: 'M';
fragment N: 'N';
fragment O: 'O';
fragment P: 'P';
fragment Q: 'Q';
fragment R: 'R';
fragment S: 'S';
fragment T: 'T';
fragment U: 'U';
fragment V: 'V';
fragment W: 'W';
fragment X: 'X';
fragment Y: 'Y';
fragment Z: 'Z';
