grammar BMS;

program: (partitionSetDefinition | partitionDefinition | mapsetDefinition)* ('END')* EOF;


partitionSetDefinition: (name)? 'DFHPSD' (attribute_list)*;
partitionDefinition: (name)? 'DFHPDI' (attribute_list)*;
mapsetDefinition: (name)? 'DFHMSD'  (attribute_list)* (mapDefinition)* 'DFHMSD' endMap;
mapDefinition: (name)? 'DFHMDI' (attribute_list)* (fieldDefinition)*;
fieldDefinition: (name)? 'DFHMDF' (attribute_list)* ;


name: IDENTIFIER;

attribute_list: attribute (','  attribute)*;

attribute: type | (IDENTIFIER '=' (value | '(' valueList ')'));

endMap: 'TYPE' '=' 'FINAL';

type: 'TYPE' '=' IDENTIFIER;

valueList: value (',' value)* ;

value : (STRING | STRING2 | NUMBER | IDENTIFIER);

IDENTIFIER: [&]?[a-zA-Z0-9][a-zA-Z0-9\-]* ;
STRING: '"' .*? '"' ;
STRING2: '\'' .*? '\'' ;
NUMBER: [0-9]+ ;

WS: [ \t\r\n]+ -> skip ;

LineComment
    : '*' ~[\r\n]* -> channel(HIDDEN)
    ;