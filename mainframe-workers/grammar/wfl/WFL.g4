// Version 3.3

grammar WFL;

// Root rule

startRule: (job | statements) EOF
    ;

// Parser rules

job: beginJob attributes? declarations? statements endJob
    ;

beginJob: QMARK? (AT hostname)? BEGIN JOB (filePath | COPY)? parameters? SEMICOLON
    ;

hostname: Identifier
    ;

// Job parameter list

parameters: LP parameterList? RP
    ;

parameterList: parameter (COMMA parameter)*
    ;

parameter: dataType (Identifier | charDataKeyword) parameterDefaultValue?
    ;

parameterDefaultValue: (OPTIONAL DEFAULT EQUAL (stringExpression | realExpression | integerExpression | booleanConstantExpression))
    ;

dataType: REAL 
    | INTEGER 
    | STRING 
    | BOOLEAN 
    | TASK
    ;

endJob: QMARK? END JOB DOT? SEMICOLON?
    ;

filePath:( (LP filePathName RP)? (filePathName | EQUAL) | (LP filePathName RP))(SLASH (filePathName)?)*  (LP Identifier (COMMA (Identifier | Num)*))? equal? | SLASH filePathName (SLASH (filePathName)?)*
    ;

equal: EQUAL
    ;

filePathName: filePathNameChar+
    ;

filePathNameChar: Identifier 
    | charDataKeyword 
    | Num 
    | UNDERSCORE 
    | reservedKeyword 
    | NumCombineWithChar 
    | taskAttribute 
    | MINUS 
    | addOption 
    | STAR 
    | LITERAL 
    | realRelation 
    | fileReferencedVariable 
    | DOLLAR
    ;

// Attributes List

attributes: attribute+
    ;

attribute: priorityAttribute
    | userAttribute
    | userCodeAttribute
    | chargeCodeAttribute
    | classAttribute
    | fetchAttribute
    | accessCodeAttribute
    | familyAttribute
    | elapsedLimitAttribute
    | maxIOTimeAttribute
    | maxLinesAttribute
    | maxProcTimeAttribute
    | maxWaitAttribute
    | startTimeAttribute
    | bdNameAttribute
    | languageAttribute
    | optionsAttribute
    // | stackLimitAttribute
    ;

stackLimitAttribute: STACKLIMIT EQUAL Num SEMICOLON
    ;

optionsAttribute: OPTIONS EQUAL LP optionList RP SEMICOLON
    ;

optionList: option (COMMA option)*
    ;

option: Identifier
    ;

languageAttribute: LANGUAGE EQUAL Identifier SEMICOLON
    ;

bdNameAttribute: BDNAME EQUAL filePath SEMICOLON
    ;

startTimeAttribute: STARTTIME EQUAL startTimeSpec SEMICOLON
    ;

startTimeSpec: time
    | time PLUS timeInterval
    | TODAY
    | TOMORROW
    | ON date
    | ON date PLUS dayInterval
    | date AT time
    | date AT time PLUS timeInterval
    | PLUS dayInterval
    | time ON date
    | time ON  dayInterval
    | fileReferencedVariable
    ;

time: Num COLON Num
    ;

timeInterval: Num COLON Num
    ;

date: mm SLASH dd SLASH (yy | yyyy)
    | yyddd
    | yyyyddd
    | TODAY
    | TOMORROW
    | dayOfWeek
    | month COMMA Num (COMMA (yy | yyyy))?
    ;

dayOfWeek: SUNDAY | MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY
    ;

month: JANUARY | FEBRUARY | MARCH | APRIL | MAY | JUNE | JULY | AUGUST | SEPTEMBER | OCTOBER | NOVEMBER | DECEMBER
    ;

mm: Num
    ;

dd: Num
    ;

yy: Num
    ;

yyyy: Num
    ;

yyddd: Num
    ;

yyyyddd: Num
    ;

dayInterval: PLUS Num
    ;

fetchAttribute: FETCH EQUAL LITERAL SEMICOLON
    ;

maxIOTimeAttribute: MAXIOTIME EQUAL Num SEMICOLON
    ;

maxLinesAttribute: MAXLINES EQUAL Num SEMICOLON
    ;

maxProcTimeAttribute: MAXPROCTIME EQUAL Num SEMICOLON
    ;

maxWaitAttribute: MAXWAIT EQUAL Num SEMICOLON
    ;

elapsedLimitAttribute: ELAPSEDLIMIT EQUAL Num SEMICOLON
    ;

familyAttribute: FAMILY reservedKeyword EQUAL (reservedKeyword | storageUnit) ONLY? (OTHERWISE (reservedKeyword |storageUnit))? SEMICOLON
    ;

reservedKeyword: TITLE | KIND | DISK | MYPACK
    ;
    
accessCodeAttribute: ACCESSCODE EQUAL filePath SEMICOLON
    ;

userAttribute: USER EQUAL filePath SEMICOLON
    ;

userCodeAttribute: USERCODE EQUAL filePath SEMICOLON
    ;

classAttribute: CLASS EQUAL Num SEMICOLON
    ;

priorityAttribute: PRIORITY EQUAL Num SEMICOLON
    ;

chargeCodeAttribute: CHARGECODE EQUAL Identifier SEMICOLON
    ;

// Declarations List

declarations: declaration+
    ;

declaration: constantDeclaration
    | booleanDeclaration
    | integerDeclaration
    | realDeclaration
    | stringDeclaration
    | fileDeclaration
    | taskDeclaration
    | subroutineDeclaration
    | includeDeclaration
    | dataDeclaration

//    | globalDataSpecification
    ;

dataDeclaration: QMARK? DATA (CARD)? SEMICOLON? (databaseDeclaration dumpDeclaration | (setListZipClause | resetZipClause)? updateClause? generateBlock* SEMICOLON? globalAndResourseSetting+ | setMergeResetList | setMergeLabelsintable |
    setListClause | dataUserAndAccessCodeListClause+ | resetZipClause updateClause | databaseClause | dataUseClause | dataSpecification | dataSystemClause | dataShowName | dataFilePathDelaration) QMARK
    ;

dataFilePathDelaration: (filePath DOT)+
    ;

dataShowName: filePath (ON storageUnit)?Identifier NAME COLON FILE filePath
    ;

dataSystemClause: (filePath (ON storageUnit)? COLON (Identifier | taskAttribute) COLON ((ENABLE | DISABLE) (PROGRAM | Identifier) Identifier | QUIT Identifier))+
    ;

dataSpecification: 
    SPEC (dataSpecificationAssignment | dataSpecificationSection)+
    ;

dataSpecificationAssignment: dataSpecificationAttribute EQUAL dataSpecificationValue (COMMA dataSpecificationValue)*  DOT
    ;

dataSpecificationSection: dataSpecificationSectionType dataSpecificationSectionName? COLON (dataSpecificationAssignment | dataSpecificationEntry)+
    ;

dataSpecificationEntry: ENTRY Num LP Identifier RP COLON dataSpecificationAssignment+
    ;

dataSpecificationSectionType: Identifier 
    | DATASET
    ;

dataSpecificationSectionName: Identifier 
    | filePath (LP Num (COMMA Num)* RP)?
    ;

dataSpecificationAttribute: Identifier 
    | taskAttribute
    ;

dataSpecificationValue: filePath 
    | Identifier 
    | Num 
    | NumCombineWithChar
    | LP (Num | NumCombineWithChar) COMMA (Num | NumCombineWithChar) RP 
    | booleanConstantExpression
    ;

dataUseClause: dataUseClauseComponent+ END
    ;

dataUseClauseComponent: useComponent 
    | reportComponent 
    | sourceComponent 
    | sortByComponent 
    | breakComponent 
    | includeComponent 
    | excludeComponent 
    | outputComponent 
    | reportsComponent 
    | pageComponent 
    | headingComponent
    ;

headingComponent: HEADING IS? LITERAL
    ;

pageComponent: PAGE Identifier IS Num
    ;

includeComponent: INCLUDE RECORD? IF condition
    ;

excludeComponent: EXCLUDE RECORD? IF condition
    ;

outputComponent: OUTPUT ITEMS ARE outputItems (COMMA outputItems)*
    ;

reportsComponent: REPORTS ARE Identifier Num
    ;

outputItems: MINUS? (taskAttribute | USERCODE | Identifier | STARTTIME)
    ;

useComponent: USE (Identifier | Num)+ (ON storageUnit)?
    ;

reportComponent: REPORT
    ;

sourceComponent: SOURCE IS (JOBSUMMARY | Identifier)
    ;

sortByComponent: SORT BY sortByParam (COMMA sortByParam)* (ASCENDING | DESCENDING)?
    ;

sortByParam: taskAttribute | USERCODE | STARTTIME | Identifier
    ;

breakComponent: BREAK ON breakOnParam (COMMA breakOnParam)* MINUS? totalling?
    ;

breakOnParam: taskAttribute | USERCODE | TYPE | ACCESSCODE | Identifier
    ;

totalling: TOTALING totallingParam (COMMA totallingParam)*
    ;

totallingParam: ELAPSEDTIME | Identifier
    ;

// dataUseOutputClause?
// breakOnClause+ dataUseIncludeClause? dataUseOutputClause? reportAreSummaryClause END; // Define manually to skip it
// dataUseIncludeClause: INCLUDE IF TYPE EQUAL LITERAL;
// dataUseOutputClause: Identifier Identifier Identifier ELAPSEDTIME;
// reportAreSummaryClause: Identifier Identifier Identifier Num;
// breakOnClause: BREAK ON breakOnParam (COMMA breakOnParam)* totallingClause;
// breakOnParam: taskAttribute | USERCODE | TYPE | ACCESSCODE;
// totallingClause: MINUS? TOTALING totallingParam (COMMA totallingParam)*;
// totallingParam: ELAPSEDTIME | Identifier ;
// dataUseSortClause: SORT BY (taskAttribute| USERCODE) (COMMA (taskAttribute| USERCODE))*;

databaseClause: DATABASE COLON Identifier otherDatabaseClauseInput* databaseMalnipulationOptions* SEMICOLON?
    ;

databaseMalnipulationOptions: UPDATE 
    | Identifier
    ;

otherDatabaseClauseInput: Identifier COLON Identifier
    ;

datasetClause: datasetDbDeclaration datasetDatasetDeclaration datasetFileDeclaration datasetRecordDeclaration datasetSourceDeclaration datasetLoadDeclaration
    ;

datasetDbDeclaration: DB Identifier SEMICOLON
    ;

datasetDatasetDeclaration: DATASET Identifier SEMICOLON
    ;

datasetFileDeclaration: FILE Identifier fileAttribute EQUAL filePath (ON storageUnit)? SEMICOLON
    ;

datasetRecordDeclaration: RECORD Identifier SEMICOLON
    ;

datasetSourceDeclaration: SOURCE DATASET SEMICOLON
    ;

datasetLoadDeclaration: (LOAD | DUMP) SEMICOLON
    ;

dataUserAndAccessCodeListClause: USER EQUAL (Identifier | charDataKeyword) ACCESSCODELIST (PLUS | MINUS) filePath SEMICOLON
    ;

setMergeLabelsintable: DOLLAR SET Identifier LABELSINTABLE
    ;

setMergeResetList: DOLLAR SET Identifier RESET Identifier; // Update to lexer rules later

updateClause: UPDATE SEMICOLON
    ;

resetZipClause: DOLLAR RESET Identifier
    ;

globalAndResourseSetting: (globalConfig | internalFileConfig | allowedCoreConfig | taskAttributeAssignment|nopostdumpConfig) SEMICOLON
    ;

nopostdumpConfig: NOPOSTDUMP
    ;

globalConfig: GLOBAL (ONLINE | OFFLINE | Identifier) (SEMICOLON (ONLINE | OFFLINE))?
    ;

internalFileConfig: INTERNAL FILES LP FAMILYNAME EQUAL Identifier RP
    ;

allowedCoreConfig: ALLOWEDCORE EQUAL Num
    ;

setListZipClause: DOLLAR SET Identifier Identifier
    ;

setListClause: DOLLAR SET Identifier
    ;

generateBlock: GENERATE generateParameters SEMICOLON
    ;

generateParameters: generateNonCopyParameters (SEMICOLON generateCopyParameters)?
    ;

generateNonCopyParameters: generateNonCopyParameter (COMMA generateNonCopyParameter)*
    ;

generateNonCopyParameter: Identifier orderByClause?
    ;

generateCopyParameters: generateCopyParameter (COMMA generateCopyParameter)* LP COPY TO storageUnit RP
    ;

generateCopyParameter: Identifier orderByClause?
    ;

orderByClause: ORDER BY Identifier
    ;

databaseDeclaration: DB EQUAL filePath (ON storageUnit)? (OPTIONS LP databaseOptions RP)? (OFFLINE|ONLINE)?
    ;

databaseOptions: databaseOption (COMMA databaseOption)*
    ;

databaseOption: Identifier EQUAL (LITERAL | Num | Identifier) | Identifier addOption
    ;

dumpDeclaration: (ONLINE | OFFLINE)? DUMP EQUAL TO filePath (ON storageUnit)? (LP dumpParameters RP)? SEMICOLON?
    ;

dumpParameters: dumpParameter (COMMA dumpParameter)*
    ;

dumpParameter: (fileAttribute | Identifier| charDataKeyword) (LP Num RP)? EQUAL ((LITERAL | Num | Identifier | NumCombineWithChar) (COMMA (LITERAL | Num | Identifier | NumCombineWithChar))*) 
    ;

includeDeclaration: DOLLAR INCLUDE filePath 
    ;

// globalDataSpecification: EBCDIC Identifier Something;

taskDeclaration: TASK taskIdentifierDeclaration (COMMA taskIdentifierDeclaration)* SEMICOLON
    ;

taskIdentifierDeclaration: taskIdentifier (LP taskIdentifierAssigments RP)? | myselfTaskAssignment | myjobTaskAssignment
    ;

myselfTaskAssignment: MYSELF LP FAMILY reservedKeyword EQUAL (reservedKeyword | storageUnit) ONLY? RP SEMICOLON?
    ;

myjobTaskAssignment: MYJOB LP (((FAMILY reservedKeyword | ACCESSCODE | JOBNUMBER) EQUAL (reservedKeyword | storageUnit | filePath) (ONLY | OTHERWISE reservedKeyword)?) | (JOBSUMMARY EQUAL Identifier)) RP SEMICOLON?
    ;

taskIdentifier: Identifier
    ;

// <task identifier assignment>

taskIdentifierAssigments: taskIdentifierAssigment (COMMA taskIdentifierAssigment)*
    ;

taskIdentifierAssigment: taskAttributeAssignment
    | fileEquation
    ;

fileEquation: FILE (Identifier | charDataKeyword | filePath) (LP fileAttributeAssignment (COMMA fileAttributeAssignment)* RP)? SEMICOLON? 
    | FILE (Identifier | charDataKeyword) EQUAL filePath (ON storageUnit)? SEMICOLON? 
    | FILE (fileIdentifier | charDataKeyword) LP fileAttributeAssignment (COMMA fileAttributeAssignment)* RP SEMICOLON? 
//    | fileIdentifier LP (fileAttributeValue | EMPTYSTRING) (COMMA (fileAttributeValue | EMPTYSTRING))* RP SEMICOLON?
    ;

fileAttributeAssignment: fileAttribute (EQUAL fileAttributeValue)?
    ;

fileAttribute: booleanFileAttribute
    | integerFileAttribute
    | stringFileAttribute
    | titleFileAttribute
    | blockSizeFileAttribute
    | fileNameFileAttribute
    | longFileNameFileAttribute
    | longTitleFileAttribute
    | mnemonicFileAttribute
    | deviceKindAssigment
    | serialNumberAssigment
    | LOCKEDFILE
    ;

// Example file attributes (expand as needed)

booleanFileAttribute: DEPENDENTSPECS 
    | OPEN 
    | NEWFILE 
    | EXCLUSIVE
    ;

integerFileAttribute: MAXRECSIZE 
    | SERIALNO
    ;

stringFileAttribute: PATHNAME
    | LICENSEKEY 
    | TRANSFORM 
    | WARNINGS 
    | AFTER 
    | DESTINATION 
    | FORMID 
    | NOTE 
    | RELEASEID
    ;

titleFileAttribute: TITLE
    ;

blockSizeFileAttribute: BLOCKSIZE
    ;

fileNameFileAttribute: FILENAME 
    | FAMILYOWNER 
    | PRINTCHARGE 
    | STATIONLIST
    ;

longFileNameFileAttribute: LFILENAME
    ;

longTitleFileAttribute: LTITLE
    ;

mnemonicFileAttribute: APPLICATIONGROUP 
    | FAMILYNAME 
    | HOSTNAME 
    | INTNAME 
    | MYHOST 
    | MYHOSTGROUP 
    | SCRATCHPOOL 
    | YOURHOST 
    | YOURHOSTGROUP 
    | YOURUSERCODE 
    | USERBACKUPNAME 
    | DENSITY 
    | BLOCKSTRUCTURE
    ;

deviceKindAssigment: DEVICEKIND | KIND | FILEKIND
    ;

serialNumberAssigment: SERIALNO
    ;

fileAttributeValue: Num 
    | LITERAL 
    | Identifier 
    | booleanConstantExpression 
    | realConstantExpression 
    | stringConstantExpression
    | filePath (ON (storageUnit | reservedKeyword))?
    | reservedKeyword
    | fileReferencedVariable (ON (storageUnit | fileReferencedVariable))?
    | LP LITERAL (COMMA LITERAL)* RP
    ;

taskAttributeAssignment: taskAttribute (EQUAL (taskAttributeValue | EMPTYSTRING | LP Identifier (COMMA Identifier)* RP | myselfMethod))? (OTHERWISE reservedKeyword)? SEMICOLON?
    ;

taskAttribute: CHARGE
    | USERCODE
    | HOSTNAME
    | AUTOSWITCHTOMARC
    | DESTSTATION
    | DISPLAYONLYTOMCS
    | LANGUAGE
    | ORGUNIT
    | SOURCEKIND
    | SOURCESTATION
    | STATION
    | STATIONNAME
    | TANKING
    | ITINERARY
    | OPTION
    | TADS
    | TASKFILE
    | CURRENTDIRECTORY
    | DATABASE
    | DATAPATH
    | EXECUTEPATH
    | FAMILY
//    | FILE
    | FILEACCESSRULE
    | JOBNUMBER
    | MIXNUMBER
    | NAME
    | MPID
    | WORKLOADGROUP
    | AX
    | LOCKED
    | PARTNEREXISTS
    | STATUS
    | SW1
    | SW2
    | SW3
    | SW4
    | SW5
    | SW6
    | SW7
    | SW8
    | TARGET
    | TASKLIMIT
    | TASKSTRING
    | TASKVALUE
    | TYPE
    | JOBSUMMARY
    | JOBSUMMARYTITLE
    | NOJOBSUMMARYIO
    | LIBRARY
    | LIBRARYSTATE
    | LIBRARYUSERS
    | CORE
    | STACKLIMIT
    | STACKSIZE
    | BACKUPFAMILY
    | BDNAME
    | DESTSTATION
    | PRINTDEFAULTS
    | TASKFILE
    | ACCUMIOTIME
    | ACCUMPROCTIME
    | ELAPSEDTIME
    | INITPBITCOUNT
    | INITPBITTIME
    | OTHERPBITCOUNT
    | OTHERPBITTIME
    | TEMPFILEMBYTES
    | ELAPSEDLIMIT
    | MAXIOTIME
    | MAXLINES
    | MAXPROCTIME
    | MAXWAIT
    | PRIORITY
    | RESOURCE
    | SAVEMEMORYLIMIT
    | STACKLIMIT
    | TASKLIMIT
    | TEMPFILELIMIT
    | TOTALMEMORYLIMIT
    | WAITLIMIT
    | BRCLASS
    | CHECKPOINTABLE
    | RESTART
    | RESTARTED
    | ACCESSCODE
    | FILEACCESSRULE
    | USERCODE
    | DECKGROUPNO
    | ERROR
    | HISTORY
    | HISTORYCAUSE
    | HISTORYTYPE
    | HSPARAMSIZE
    | STACKHISTORY
    | STATUS
    | STOPPOINT
    | SUPPRESSWARNING
    | TASKWARNINGS
    | FAMILYDISK
    ;

taskAttributeValue: Num 
    | LITERAL 
    | Identifier 
    | booleanConstantExpression 
    | realConstantExpression 
    | stringConstantExpression
    ;

fileDeclaration: FILE fileDeclarationElement (COMMA fileDeclarationElement)* SEMICOLON
    ;

fileDeclarationElement: Identifier (LP fileAttributeAssignment (COMMA fileAttributeAssignment)* RP)?
    ;

booleanDeclaration: BOOLEAN booleanDeclarationElement (COMMA booleanDeclarationElement)* SEMICOLON
    ;

booleanDeclarationElement: Identifier (ASSIGN booleanConstantExpression)?
    ;

booleanConstantExpression: TRUE | FALSE | Identifier
    ;

integerDeclaration: INTEGER integerDeclarationElement (COMMA integerDeclarationElement)* SEMICOLON
    ;

integerDeclarationElement: Identifier (ASSIGN integerConstantExpression)?
    ;

integerConstantExpression: Num | Identifier | parameterReference
    ;

realDeclaration: REAL realDeclarationElement (COMMA realDeclarationElement)* SEMICOLON
    ;

realDeclarationElement: Identifier (ASSIGN realConstantExpression)?
    ;

realConstantExpression: Num (DOT Num)? 
    | Identifier 
    | parameterReference
    ;

stringDeclaration: STRING stringDeclarationElement (COMMA stringDeclarationElement)* SEMICOLON
    ;

stringDeclarationElement: (Identifier | charDataKeyword) (ASSIGN stringConstantExpression)?
    ;

stringConstantExpression: primaryStringExpression (AMPERSAND primaryStringExpression)*
    ;

primaryStringExpression: LITERAL 
    | Identifier 
    | parameterReference
    | stringFunction
    | stringExpression
    ;

stringFunction: STRING LP (Identifier | Num) (COMMA STAR)? RP
    ;

parameterReference: Identifier
    ;

constantDeclaration: CONSTANT constantDeclarationElement (COMMA constantDeclarationElement)* SEMICOLON
    ;

constantDeclarationElement: booleanConstantDeclaration
    | integerConstantDeclaration
    | realConstantDeclaration
    | stringConstantDeclaration
    ;

booleanConstantDeclaration: Identifier EQUAL booleanConstantExpression
    ;

integerConstantDeclaration: Identifier EQUAL integerConstantExpression
    ;

realConstantDeclaration: Identifier EQUAL realConstantExpression
    ;

stringConstantDeclaration: Identifier EQUAL stringConstantExpression
    ;

subroutineDeclaration: SUBROUTINE subroutineName subroutineParameters? SEMICOLON (statement| subroutineBlock)
    ;

subroutineName: Identifier 
    | compilerName 
    | charDataKeyword
    ;

subroutineParameters: LP subroutineParameterList RP
    ;

subroutineParameterList: subroutineParameter (COMMA subroutineParameter)*
    ;

subroutineParameter: booleanParameter
    | integerParameter
    | realParameter
    | stringParameter
    | fileParameter
    | taskParameter
    ;

booleanParameter: BOOLEAN Identifier (VALUE)?
    ;

integerParameter: INTEGER Identifier (VALUE)?
    ;

realParameter: REAL Identifier (VALUE)?
    ;

stringParameter: STRING ( Identifier | charDataKeyword) (VALUE)?
    ;

fileParameter: FILE Identifier
    ;

taskParameter: TASK Identifier
    ;

subroutineBlock: 
    BEGIN declarations? statements? END subroutineName? SEMICOLON
    ;

//fileReferencedVariable:HASH LP? (Identifier | stringExpression)  RP? (ON storageUnit)?;

fileReferencedVariable: HASH LP? (Identifier | stringExpression)  RP?
    ;

// label

label: labelIdentifer COLON
    ;

// Statements List

statements: (statement)+
    ;

statement: compileStatement
    | runStatement
    | displayStatement
    | initializeStatement
    | abortStatement
    | waitStatement
    | addStatement
    | processStatement
    | assignmentStatement
    | startStatement
    | ifStatement
    | doStatement
    | whileStatement
    | caseStatement
    | alterStatement
    | changeStatement
    | crunchStatement
    | goStatement
    | modifyStatement
    | removeStatement
    | onStatement
    | openStatement
    | lockStatement
    | releaseStatement
    | replaceStatement
    | subroutineInvocationStatement
    | copyStatement
    | copyAndRemoveStatement
    | copyAndCompareStatement
    | label
    | myselfTaskAssignment
    | myjobTaskAssignment
    | printStatement
    |wrapAndCompressStatement
    | dataDeclaration
    | startAndWaitStatement
    | stackLimitAttribute
    | userAttribute
    // MOVE
    // ACCESS
    // ARCHIVE
    // BIND
    // CATALOG
    // INSTRUCTION
    // LOCK
    // LOG
    // MKDIR
    // Null
    // PASSWORD
    // PB
    // PRINT
    // PURGE
    // RERUN
    // RESTORE
    // RETURN
    // REWIND
    // STOP
    // UNWRAP
    // WRAP
    // USER
    // VOLUME           
    ;

// startAndWaitStatement

startAndWaitStatement: START AND WAIT filePath  runParameterList  SEMICOLON
    ;

// WRAP AND COMPRESS STATEMENT

wrapAndCompressStatement: 
    WRAP AMPERSAND COMPRESS  wrapAndCompressFrom (COMMA wrapAndCompressFrom)* (intoClause) fromClause? (toClause)? (LS taskIdentifier RS)? SEMICOLON
    ;

wrapAndCompressFrom: (filePath | fileReferencedVariable | EQUAL) (COMMA (filePath | fileReferencedVariable | EQUAL))* (copyAsClause)? (fromClause)?
    ;

// Print statement

printStatement: PRINT printSpecification SEMICOLON printDefault SEMICOLON
    ;

printSpecification: (filePath | fileReferencedVariable) (COMMA (filePath | fileReferencedVariable))* (LS taskIdentifier RS)?
    ;

printDefault: PRINTDEFAULTS EQUAL (LP printDefaultParameters RP)?
    ;

printDefaultParameters: (printDefaultParameter (COMMA printDefaultParameter)*)?
    ;

printDefaultParameter: printAttribute EQUAL printAttributeValue (COMMA printAttributeValue)*
    ;

printAttributeValue: Num 
    | LITERAL 
    | Identifier 
    | booleanConstantExpression 
    | realConstantExpression 
    | stringConstantExpression 
    | filePath 
    | fileReferencedVariable
    ;

printAttribute: DESTINATION 
    | NOTE 
    | PRINTPARTIAL
    ;

// Copy Statement

copyAndCompareStatement: 
    (COPY AMPERSAND COMPARE) (filePath | fileReferencedVariable) (COMMA (filePath | fileReferencedVariable))* (fromClause)? (toClause)? (LS taskIdentifier RS)? SEMICOLON
    ;

copyAndRemoveStatement: 
    (COPY AMPERSAND REMOVE) (filePath | fileReferencedVariable) (COMMA (filePath | fileReferencedVariable))* (fromClause)? (toClause)? (LS taskIdentifier RS)? SEMICOLON
    ;

copyStatement: 
QMARK? COPY copyProtocol? copyFromClause
(COMMA copyFromClause)*
(toClause)? (LS taskIdentifier RS)? SEMICOLON?
    ;
copyProtocol: LS Identifier RS
    ;
copyFromClause: (filePath | fileReferencedVariable| EQUAL) (COMMA (filePath) )* (copyAsClause)?
(fromClause)?;

copyAsClause: AS (fileReferencedVariable | LITERAL | filePath) (LP Identifier EQUAL Identifier RP)?
    ;

// Compile Statement

compileStatement: 
    (COMPILE | BIND) (filePath | fileReferencedVariable) (ON storageUnit)?
    (WITH compilerName (ON familyName)? | WITH compilerTitle)? 
    (LP taskIdentifier RP)?
    (LS taskIdentifier RS)? 
    (SYNTAX | LIBRARY | GO | LIBRARY GO)? 
    SEMICOLON?
    (compilerTaskEquationList)? 
    SEMICOLON?
    ;

compilerTaskEquationList: (COMPILER (taskAttributeAssignment | fileEquation | libraryEquation | databaseEquation | dataDeclaration))+
    ;

libraryEquation: LIBRARY filePath (LP fileAttributeAssignment (COMMA fileAttributeAssignment)* RP)?
    ;

databaseEquation: DATABASE filePath (LP fileAttributeAssignment (COMMA fileAttributeAssignment)* RP)?
    ;

compilerName: ALGOL | BINDER | CC | COBOL74 | COBOL85 | DCALGOL | DMALGOL | FORTRAN77 | MODULA2 | NDLII | NEWP | PASCAL | RPG | SORT | LCOBOL74
    ;

compilerTitle: filePath
    ;

familyName: Identifier
    ;

// Run Statement   

runStatement: 
    (RUN | EXECUTE) (filePath | fileReferencedVariable) (ON (storageUnit | reservedKeyword))? 
    (runParameterList)?
    (LP taskIdentifier RP)?
    SEMICOLON?
    (LS taskIdentifier RS)?
    SEMICOLON
    (taskEquationList)?
    (localDataSpecification)?
    // SEMICOLON
    ;

localDataSpecification: 
    EBCDIC CARD ((ACCESSED | Identifier) (BEFORE | AFTER) date)? ALL? FILES LP (filePath | EQUAL) FROM filePath RP TO filePath (LP fileAttributeAssignment (COMMA fileAttributeAssignment)* RP)* excludeClause* LOCKDECK DECKLABEL filePath (ON storageUnit)? JOBSYMBOL NOSUMMARY CLASS Num TASKFAULT NOZ?  QMARK | dataDeclaration
    ;

excludeClause: EXCLUDE FILEKIND? LP ((Identifier | charDataKeyword | filePath (FROM storageUnit)?) (COMMA (Identifier | charDataKeyword | filePath (FROM storageUnit)?))*) RP
    ;

runParameterList: 
    LP (runParameter (COMMA runParameter)*)? RP 
    ;

runParameter: 
    realExpression 
    | integerExpression 
    | booleanConstantExpression 
    | stringExpression 
    | Identifier REFERENCE
    | MYJOB LP (NAME) RP
    |fileReferencedVariable
    ;

realExpression: 
    Num (DOT Num)?
    ;

integerExpression: 
    Num 
    | calcExpression 
    | Identifier 
    | taskIdentifier LP (integerTaskAttribute | taskAttribute) RP 
    | integerMethod
    ;

integerMethod:
    integerIntegerMethod 
    | myselfMethod
    | myjobMethod
    | otherIntegerMethod
    ;

otherIntegerMethod: Identifier LP (integerExpression | stringExpression) RP
    ;

integerIntegerMethod:
    INTEGER LP integerExpression RP | DECIMAL LP stringExpression RP
    ;

calcExpression: 
    LP? calcExpressionTerm ((PLUS | MINUS) calcExpressionTerm)* RP?
    ;

calcExpressionTerm:
    calcExpressionFactor ((STAR | SLASH | MOD | DIV) calcExpressionFactor)*
    ;

calcExpressionFactor:
    Identifier
    | Num
    | integerMethod
    | taskIdentifier LP taskAttribute RP
    | LP calcExpression RP
    ;

stringExpression: 
    LITERAL 
    | stringIdentifier 
    | stringMethod 
    | EMPTYSTRING 
    ;

stringMethod: headMethod 
    | tailMethod 
    | concatMethod 
    | stringStringMethod 
    | subStringMethod 
    | takeMethod 
    | dropMethod 
    | myselfMethod 
    | timeDateMethod 
    | acceptMethod 
    | otherStringMethod
    ;

otherStringMethod: Identifier LP (Identifier | fileAttribute | taskAttribute) RP
    ;

acceptMethod: ACCEPT LP stringExpression RP
    ;

timeDateMethod: TIMEDATE LP timeDateParameter RP
    ;

timeDateParameter: YYMMDD 
    | HHMMSS 
    | YYYYMMDD 
    | MMDDYY 
    | MMDDYYYY 
    | DAYNUMBER 
    | LITERAL 
    | YYYYMMDDHHMMSS
    ;

myselfMethod: MYSELF LP (Identifier | HOSTNAME | JOBNUMBER | taskAttribute) RP
    ;

myjobMethod: MYJOB LP (Identifier | HOSTNAME | JOBNUMBER | taskAttribute) RP
    ;

takeMethod: TAKE LP (LP? stringExpression RP?) COMMA integerExpression RP
    ;

dropMethod: DROP LP stringExpression COMMA integerExpression RP
    ;
    
subStringMethod: (stringIdentifier | MYJOB) LP (integerExpression | Identifier | taskAttribute) RP
    ;

stringStringMethod: STRING LP (stringExpression | integerExpression) COMMA (integerExpression | STAR) RP
    ;

headMethod: HEAD LP headParameter (COMMA headParameter)* RP
    ;

headParameter: Identifier | NOT? LITERAL
    ;

tailMethod: TAIL LP tailParameter (COMMA tailParameter)* RP
    ;

tailParameter: Identifier 
    | NOT? LITERAL
    ;

concatMethod: (stringIdentifier | LITERAL | timeDateMethod | takeMethod | EMPTYSTRING | stringStringMethod | dropMethod) ((AMPERSAND | SLASH) (stringExpression))+
    ;

taskEquationList: 
    (taskAttributeAssignment | fileEquation | libraryEquation | databaseEquation)+
    ;

// Display Statement   

displayStatement: DISPLAY LP?stringConstantExpression RP? SEMICOLON?
    ;

// Initialize Statement

initializeStatement: INITIALIZE LP taskIdentifier RP SEMICOLON
    ;

// Abort Statement

abortStatement: ABORT (LS (taskIdentifier | MYSELF) RS)? LP? stringConstantExpression? RP? SEMICOLON?
    ;

// Wait Statement

waitStatement: 
    WAIT (LP waitContent RP)? SEMICOLON?
    ;

waitContent: 
    stringExpression (COMMA waitSpecification)?
    | waitSpecification
    ;

waitSpecification: 
    OK
    | realExpression
    | taskIdentifier
    | taskState
    | taskIdentifier (IS | ISNT) taskState
    | simpleTaskRelation
    | taskMnemonicComparison
    | taskIdentifier LP booleanTaskAttribute RP
    | FILE (filePath | fileReferencedVariable) (ON storageUnit)? IS (RESIDENT | COMPLETEDOK | COMPILEDOK)
    ;

simpleTaskRelation: taskIdentifier LP (integerTaskAttribute | realTaskAttribute) RP realRelation realExpression
    ;

taskMnemonicComparison: taskIdentifier LP mnemonicTaskAttribute RP IS taskState
    ;

taskState: COMPLETED 
    | ACTIVE 
    | TERMINATED 
    | BADINITIATE 
    | NEVERUSED
    | STOPPED
    ;

booleanTaskAttribute: TASKVALUE 
    | STATUS 
    | SW1 
    | SW2 
    | SW3 
    | SW4 
    | SW5 
    | SW6 
    | SW7 
    | SW8
    ;

integerTaskAttribute: ACCUMPROCTIME 
    | MAXRECSIZE 
    | SERIALNO
    | VALUE
    ;

realTaskAttribute: ELAPSEDTIME 
    | INITPBITTIME 
    | OTHERPBITTIME
    ;

mnemonicTaskAttribute: STATUS 
    | TASKVALUE
    ;

realRelation: EQL 
    | GTR 
    | LSS 
    | GEQ 
    | LEQ 
    | NEQ
    | LT
    | GT
    ;

// Add Statement

addStatement: ADD addOptions? copyRequest (LS taskIdentifier RS)? taskAttributeAssignment? SEMICOLON 
    | ADD (filePath copyAsClause) (COMMA filePath copyAsClause)* (fromClause)? (toClause)? (LS taskIdentifier RS)? SEMICOLON?
    ;
    
addOptions: (AND | AMPERSAND)? addOption (COMMA addOption)*
    ;

addOption: BECOMEOWNER 
    | CATALOG 
    | BACKUP 
    | COMPARE 
    | VERIFY 
    | DSONERROR 
    | WAITONERROR 
    | REPORT 
    | SKIPEXCLUSIVE 
    | FROMSTART 
    ;

copyRequest: 
        ((filePath | fileReferencedVariable| EQUAL) (COMMA (filePath) )* (copyAsClause)? 
    (fromClause)?) toClause?
    ;

// Process Statement

processStatement: 
    PROCESS (addStatement
    | compileStatement
    | runStatement 
    | startStatement
    | subroutineInvocationStatement
    //| bindStatement 
    | copyStatement 
    //| logStatement 
    //| pbStatement 
    | wrapAndCompressStatement
    //| filePath (LP LITERAL RP)?
    ) 
    (LS taskIdentifier RS)? 
    taskEquationList? 
    SEMICOLON?
    ;

// Assignment Statement

assignmentStatement: 
    booleanAssignmentStatement
    | integerAssignmentStatement
    | realAssignmentStatement
    | stringAssignmentStatement
    | fileAssignmentStatement
    | taskAssignmentStatement
    ;

booleanAssignmentStatement: 
    booleanIdentifier ASSIGN booleanConstantExpression SEMICOLON
    ;

booleanIdentifier: Identifier
    ;   

integerAssignmentStatement: 
    integerIdentifier ASSIGN integerExpression SEMICOLON?
    ;

integerIdentifier: Identifier
    ;  

realAssignmentStatement: 
    realIdentifier ASSIGN realExpression SEMICOLON
    ;

realIdentifier: Identifier
    ;  

stringAssignmentStatement: 
    stringIdentifier ASSIGN stringExpression? SEMICOLON?
    ;

stringIdentifier: Identifier | charDataKeyword
    ;  

fileAssignmentStatement: 
    fileIdentifier LP fileAttributeAssignment (COMMA fileAttributeAssignment)* RP SEMICOLON;
    
fileIdentifier: Identifier
    ;  

taskAssignmentStatement: 
    taskIdentifier LP (taskAttributeAssignment | fileEquation) (COMMA (taskAttributeAssignment | fileEquation))* RP SEMICOLON
    ;

// Start Statement

startStatement: 
    (START | STARTJOB) filePath (ON storageUnit)? 
    (LP startParameterList RP)? 
    (LS taskIdentifier RS)? 
    (FOR SYNTAX)? 
    (SEMICOLON 
    | HASH stringPrimary 
    | SEMICOLON startTimeAttribute
    ) 
    ;

startParameterList: 
    namedParameterList 
    | positionalParameterList (COMMA namedParameterList)?
    ;

namedParameterList: 
    namedParameter (COMMA namedParameter)*
    ;

namedParameter: 
    realFormalParameter ASSIGN realExpression
    | integerFormalParameter ASSIGN integerExpression
    | booleanFormalParameter ASSIGN booleanConstantExpression
    | stringFormalParameter ASSIGN stringExpression
    ;

realFormalParameter: Identifier
    ;

integerFormalParameter: Identifier
    ;

booleanFormalParameter: Identifier
    ;

stringFormalParameter: Identifier
    ;

positionalParameterList: 
    positionalParameter (COMMA positionalParameter)*
    ;

positionalParameter: 
    realExpression 
    | integerExpression 
    | booleanConstantExpression 
    | stringExpression
    ;

stringPrimary: 
    STRING LP (Identifier | Num) (COMMA STAR)? RP
    ;

// If Statement

ifStatement: 
     IF condition thenClause  elseClause? 
     | BEGIN IF condition thenClause  elseClause? END SEMICOLON
    ;

condition: simpleCondition 
    | combineComplexCondition
    ;

simpleCondition: 
    (NOT)? LP? booleanExpression RP? ((OR|AND) (NOT)? LP? booleanExpression RP?)*
    ;

complexCondition: LP LP LP booleanExpression RP (AND | OR) LP booleanExpression RP RP (OR | AND) LP LP booleanExpression RP (AND | OR) LP booleanExpression RP RP RP
    ;

combineComplexCondition: 
    complexCondition ((OR | AND) complexCondition)?
    ;

thenClause: THEN statement | THEN BEGIN SEMICOLON? statement+ END SEMICOLON?
    ;

elseClause: ELSE statement | ELSE BEGIN SEMICOLON? statement+ END SEMICOLON?
    ;

booleanExpression: 
    booleanConstantExpression
    | booleanComparison
    | NOT LP? booleanExpression RP?
    | NOT LP? calcExpression (realRelation | EQUAL) (Num | Identifier | LP? calcExpression RP?) RP?
    | LP booleanExpression RP
    ;

booleanComparison: 
    taskIdentifier LP booleanTaskAttribute RP (IS|ISNT) booleanConstantExpression
    | taskIdentifier LP (booleanTaskAttribute 
    | integerTaskAttribute) RP (realRelation | IS | ISNT | EQUAL) (Num | LP? calcExpression RP?)
    | filePath (IS|ISNT) ( RESIDENT | ABORTED | COMPLETEDOK | COMPILEDOK)
    | FILE (fileReferencedVariable | filePath) (ON storageUnit)? (IS|ISNT) (RESIDENT | ABORTED | COMPLETEDOK | COMPILEDOK)
    | (Identifier | stringExpression | charDataKeyword | taskAttribute) (realRelation | EQUAL ) (LITERAL | Num | LP? calcExpression RP? | Identifier | EMPTYSTRING)
    | taskIdentifier (IS | ISNT) taskState
    | NOT Identifier LP RESIDENT RP
    | integerExpression (realRelation | EQUAL) (Num | Identifier | LP? calcExpression RP?)
    | LP? calcExpression RP? (realRelation | EQUAL) (Num | Identifier | LP? calcExpression RP?)
    ;

storageUnit: Identifier
    ;

// Do Statement

doStatement: 
    DO BEGIN? statements END? SEMICOLON? UNTIL condition SEMICOLON
    ;

// While Statement

whileStatement: 
    WHILE condition DO (BEGIN statement+ END | statement) SEMICOLON
    ;

// Case Statement

caseStatement: 
    CASE caseExpression OF BEGIN caseClauses (ELSE COLON? BEGIN? statement* END? SEMICOLON?)? END SEMICOLON
    ;

caseExpression: 
    integerExpression
    | stringExpression
    | Identifier
    ;

caseClauses: caseClause+
    ;

caseClause: 
    LP caseConstantExpression RP COLON  (BEGIN statement+ END | statement) SEMICOLON?
    ;

caseConstantExpression: 
    integerConstantExpression
    | stringConstantExpression (COMMA stringConstantExpression)*
    ;

// Alter Statement

alterStatement: 
    ALTER (longFileTitle | longDirectoryTitle) (ON storageUnit)? LP alterAttributeList RP SEMICOLON
    ;

longFileTitle: 
    filePath
    ;

longDirectoryTitle: 
    filePath
    ;

alterAttributeList: 
    alterAttribute (COMMA alterAttribute)*
    ;

alterAttribute: 
    ALTERNATEGROUPS EQUAL alternategroupsValue
    | PROPAGATESECURITYTODIRS EQUAL (DONTPROPAGATE | PROPAGATE)
    | PROPAGATESECURITYTOFILES EQUAL (DONTPROPAGATE | PROPAGATE)
    | ALIGNFILE EQUAL filePath
    | ALIGNMENT EQUAL booleanExpression
    | APL EQUAL booleanExpression
    | BANNER EQUAL booleanExpression
    | LOCKEDFILE EQUAL booleanExpression
    | SECURITYADMIN EQUAL booleanExpression
    | SENSITIVEDATA EQUAL booleanExpression
    | CCSVERSION EQUAL mnemonicValue
    | EXTMODE EQUAL mnemonicValue
    | FORMID EQUAL stringPrimary
    | PAGECOMP EQUAL booleanExpression
    | TRANSFORM EQUAL booleanExpression
    | groupExpression
    | EXTDELIMITER EQUAL mnemonic
    | FILEKIND EQUAL mnemonic
    | LABEL EQUAL mnemonic
    | PRINTERKIND EQUAL mnemonic
    | TRAINID EQUAL mnemonic
    | NOTE EQUAL stringPrimary
    | PRODUCT EQUAL stringPrimary
    | RELEASEID EQUAL stringPrimary
    | SAVEFACTOR EQUAL integerExpression
    | SECURITYGUARD EQUAL (filePath | EMPTYSTRING)
    | SECURITYMODE EQUAL integerExpression
    | SECURITYTYPE EQUAL fileMnemonicPrimary
    | SECURITYUSE EQUAL fileMnemonicPrimary
    | USERINFO EQUAL integerExpression
    ;

alternategroupsValue: 
    EMPTYSTRING
    | HASH stringPrimary
    | STRING
    ;

groupExpression: 
    GROUP EQUAL (nameConstant | HASH stringPrimary | EMPTYSTRING)
    | OWNER EQUAL (nameConstant | HASH stringPrimary | EMPTYSTRING)
    | GROUPRWX EQUAL mnemonic
    | OTHERRWX EQUAL mnemonic
    | OWNERRWX EQUAL mnemonic
    | GROUPR EQUAL booleanExpression
    | GROUPW EQUAL booleanExpression
    | GROUPX EQUAL booleanExpression
    | OTHERR EQUAL booleanExpression
    | OTHERW EQUAL booleanExpression
    | OTHERX EQUAL booleanExpression
    | OWNERR EQUAL booleanExpression
    | OWNERW EQUAL booleanExpression
    | OWNERX EQUAL booleanExpression
    | SETUSERCODE EQUAL booleanExpression
    | SETGROUPCODE EQUAL booleanExpression
    | USEGUARDFILE EQUAL booleanExpression
    | GUARDOWNER EQUAL booleanExpression
    ;

mnemonicValue: 
    Identifier
    ;

fileMnemonicPrimary: 
    Identifier
    ;

nameConstant: 
    Identifier
    ;

mnemonic: RWX 
    | RW 
    | RX  
    | WX 
    | NO
    //| W 
    //| X
    //| R 
    ;

// Change Statement

changeStatement: CHANGE changeItem (ON familyName)? TO changeItem fromClause? SEMICOLON
    ;

changeItem: 
    filePath | fileReferencedVariable
    ;

// Crunch Statement

crunchStatement: CRUNCH LP fileIdentifier RP SEMICOLON
    ;

// Go Statement

goStatement: GO TO? labelIdentifer SEMICOLON
    ;

labelIdentifer: Identifier
    ;

// Modify Statement

modifyStatement: 
        MODIFY (filePath | fileReferencedVariable) (ON (storageUnit | reservedKeyword))? 
    (runParameterList)?
    (LP taskIdentifier RP)?
    SEMICOLON?
    (LS taskIdentifier RS)?
    SEMICOLON
    (taskEquationList)?
    (localDataSpecification QMARK)?
    // SEMICOLON
    ;
    
onClause: ON Identifier
    ;

// Remove Statement

removeStatement: REMOVE (filePath) (COMMA filePath)* (onClause|fromClause)? SEMICOLON?
    ;

fromClause: FROM (storageUnit | fileReferencedVariable | reservedKeyword) (LP fromClauseParameter (COMMA fromClauseParameter)* RP)?
    ;

fromClauseParameter: (Identifier | charDataKeyword | taskAttribute | reservedKeyword) (EQUAL (Identifier | charDataKeyword | reservedKeyword | filePath | LITERAL))?
    ;

toClause: TO (storageUnit | reservedKeyword | fileReferencedVariable | charDataKeyword | Num) (LP toClauseParameters (COMMA toClauseParameters)*RP)?
    ;

// On Statement

toClauseParameters: (Identifier | charDataKeyword | taskAttribute | reservedKeyword) (EQUAL (Identifier | charDataKeyword | reservedKeyword | LP ((LITERAL | Identifier | ATS Identifier LP Identifier RP ATS) (COMMA (LITERAL | Identifier))*) RP | filePath | booleanConstantExpression))?
    ;

onStatement: ON (TASKFAULT|RESTART) (COMMA (BEGIN statement+ END SEMICOLON?| statement))?
    ;

intoClause: INTO (storageUnit | fileReferencedVariable) (LP (Identifier | charDataKeyword) (EQUAL (Identifier | charDataKeyword | reservedKeyword))? RP)?
    ;

// Open Statement

openStatement: OPEN LP fileIdentifier RP SEMICOLON
    ;

lockStatement: LOCK LP fileIdentifier RP SEMICOLON
    ;

// Release Statement

releaseStatement: RELEASE LP fileIdentifier RP SEMICOLON
    ;

// Replace Statement

replaceStatement: 
    REPLACE replaceOptions? copyRequest (LS taskIdentifier RS)? (SEMICOLON taskAttributeAssignment)? SEMICOLON
    ;

replaceOptions: 
    (AMPERSAND | AND)? (COMPARE | VERIFY | CATALOG | BACKUP | REPORT | SELECT | DSONERROR | WAITONERROR) (COMMA replaceOptions)*
    ;

// Subroutine Invocation Statement

subroutineInvocationStatement: subroutineIdentifier (LP argumentList? RP)? SEMICOLON
    ;

subroutineIdentifier: Identifier | compilerName | charDataKeyword
    ;

argumentList: argument (COMMA argument)*
    ;

argument: realConstantExpression
    | integerConstantExpression
    | booleanConstantExpression
    | stringConstantExpression
    | taskIdentifier
    | fileIdentifier
    | LITERAL
    ;

charDataKeyword:
    JOB 
    |COMPILE
    | GO
    | ADD
    | DIV
    | AFTER
    | GROUP
//    | END
    | KIND
    | SELECT
    | REMOVE
    | DISPLAY
    | PRINT
    | LOG
    | OPEN
    | LABEL
    | COPY
    | OK
    | ACCEPT
    | SECURITY
    | USERDATA
    | INITIALIZE
    | DO
    | WHILE
    | MODIFY
    | RELEASE
    | AS
    | SERIALNO
    | APRIL
    | TAKE
    | DROP
    | USERCODE
    | SUNDAY
    | NDLII
    | PRINTPARTIAL 
    | INTO
    | COMPRESS
    | TYPE
    | CHANGE
    | DATA
    | DB
    | OFFLINE
    | OPTIONS
    | DUMP
    | ALL
    | CARD
    | DENSITY
    | JOBSYMBOL
    | ACCESSED
    | BEFORE
    | NOZ
    | ONLINE
    | STOP
    | TODAY
    | GENERATE
    | ORDER
    | BY
    | SET
    | GLOBAL
    | INTERNAL
    | ALLOWEDCORE
    | ONLY
    | EXCLUDE
    | DECIMAL
    | CC
    | AX
    | UPDATE
    | RESET
    | NOPOSTDUMP
    | LOCK
//    | OR
//    | FROM
    | TO
    | MOD
    | DAYNUMBER
    | FILES
    | WRAP
    | RECORD
    | SOURCE
    | LOAD
    | YYYYMMDD
    | USE
    | BREAK
    | BLOCKSTRUCTURE
    | SYNTAX
    | BDNAME
    | OUTPUT
    | ITEMS
    | ARE
    | REPORTS
    | HEADING
    | PAGE
    | SPEC
    | ENTRY
    | DISABLE
    | ENABLE
    | PROGRAM
    | ASCENDING
    | DESCENDING
    | QUIT
    | STOPPED
    | START
    | OWNER
    | ERRORFILE
    // | FONT 
    // | TYPESCALE 
    // | CPI 
    // | DLFONT
    ;

// Lexer rules

AMPERSAND: '&'
    ;

EMPTYSTRING: '""'
    ;

UNDERSCORE: '_' 
    ;

COMMA: ','
    ;

BACKSLASH: '\\'
    ;

TILDE: '~'
    ;

BACKTICK: '`'
    ;

LS: '['
    ;

RS: ']'
    ;

LB: '{'
    ;

RB: '}'
    ;

LP: '('
    ;

RP: ')'
    ;

PIPE: '|'
    ;

COLON: ':'
    ;

DOLLAR: '$'
    ;

ATS: '@'
    ;

HASH: '#'
    ;

DOT: '.'
    ;

SEMICOLON: ';'
    ;

EXCLAMATION: '!'
    ;

QMARK: '?'
    ;

LT: '<'
    ;

GT: '>'
    ;

PLUS: '+'
    ;

MINUS: '-'
    ;

SLASH: '/'
    ;

STAR: '*'
    ;

EQUAL: '='
    ;

ASSIGN: ':='
    ;

CARET: '^'
    ;

SW1: 'SW1'
    ;

SW2: 'SW2'
    ;

SW3: 'SW3'
    ;

SW4: 'SW4'
    ;

SW5: 'SW5'
    ;

SW6: 'SW6'
    ;

SW7: 'SW7'
    ;

SW8: 'SW8'
    ;

COBOL74: 'COBOL74'
    ;

COBOL85: 'COBOL85'
    ;

FORTRAN77: 'FORTRAN77'
    ;

MODULA2: 'MODULA2'
    ;

LCOBOL74: 'LCOBOL74'
    ;

REPLACE: R E P L A C E
    ;

SELECT: S E L E C T
    ;

DIV: D I V
    ;

TASKFAULT: T A S K F A U L T
    ;

SETGROUPCODE: S E T G R O U P C O D E
    ;

ALTERNATEGROUPS: A L T E R N A T E G R O U P S
    ;

PROPAGATESECURITYTODIRS: P R O P A G A T E S E C U R I T Y T O D I R S
    ;

ACCESSED: A C C E S S E D
    ;

BEFORE: B E F O R E
    ;

QUIT: Q U I T
    ;

DATASET: D A T A S E T
    ;

PROGRAM: P R O G R A M
    ;

RECORD: R E C O R D
    ;

STOPPED: S T O P P E D
    ;

USE: U S E
    ;

TOTALING: T O T A L I N G
    ;

SOURCE: S O U R C E
    ;

BREAK: B R E A K
    ;

LOAD: L O A D
    ;

DECIMAL: D E C I M A L
    ;

ORDER: O R D E R
    ;

BY: B Y
    ;

DONTPROPAGATE: D O N T P R O P A G A T E
    ;

EXCLUSIVE: E X C L U S I V E
    ;

DISABLE: D I S A B L E
    ;

ENABLE: E N A B L E
    ;

PROPAGATE: P R O P A G A T E
    ;

NOZ: N O Z
    ;

PROPAGATESECURITYTOFILES: P R O P A G A T E S E C U R I T Y T O F I L E S
    ;

ALIGNMENT: A L I G N M E N T
    ;

UPDATE: U P D A T E
    ;

NOPOSTDUMP: N O P O S T D U M P
    ;

RESET: R E S E T
    ;

APL: A P L
    ;

DB: D B
    ;

ALL: A L L
    ;

CARD: C A R D
    ;

BANNER: B A N N E R
    ;

SPEC: S P E C
    ;

LOCKEDFILE: L O C K E D F I L E
    ;  

SECURITYADMIN: S E C U R I T Y A D M I N
    ;

HEADING: H E A D I N G
    ;

PAGE: P A G E
    ;

SENSITIVEDATA: S E N S I T I V E D A T A
    ;

SET: S E T
    ;

CCSVERSION: C C S V E R S I O N
    ;

OPTIONS: O P T I O N S
    ;

DUMP: D U M P
    ;

OFFLINE: O F F L I N E
    ;

ONLINE: O N L I N E
    ;

TAKE: T A K E
    ;

DROP: D R O P
    ;

EXTMODE: E X T M O D E
    ;

PAGECOMP: P A G E C O M P
    ;

TRANSFORM: T R A N S F O R M
    ;

EXTDELIMITER: E X T D E L I M I T E R
    ;

GLOBAL: G L O B A L
    ;

INTERNAL: I N T E R N A L
    ;

ALLOWEDCORE: A L L O W E D C O R E
    ;

FILEKIND: F I L E K I N D
    ;

LABEL: L A B E L
    ;

PRINTERKIND: P R I N T E R K I N D
    ;

TRAINID: T R A I N I D
    ;

PRODUCT: P R O D U C T
    ;

SAVEFACTOR: S A V E F A C T O R
    ;

SECURITYMODE: S E C U R I T Y M O D E
    ;

SECURITYUSE: S E C U R I T Y U S E
    ;

INCLUDE: I N C L U D E
    ;

PRINTPARTIAL: P R I N T P A R T I A L
    ;

INTO: I N T O
    ;

COMPRESS: C O M P R E S S
    ;

// FONT: F O N T;

// TYPESCALE: T Y P E S C A L E
//     ;

// CPI: C P I;

// DLFONT: D L F O N T
//     ;

ERRORFILE: E R R O R F I L E
    ;

ENTRY: E N T R Y
    ;

USERINFO: U S E R I N F O
    ;

GROUP: G R O U P
    ;

COMPLETEDOK: C O M P L E T E D O K
    ;

OPTIONAL: O P T I O N A L
    ;

OR: O R
    ;

YYMMDD: Y Y M M D D
    ;

YYYYMMDD: Y Y Y Y M M D D
    ;

HHMMSS: H H M M S S
    ;

MMDDYY: M M D D Y Y
    ;

MMDDYYYY:M M D D Y Y Y Y
    ;

YYYYMMDDHHMMSS: Y Y Y Y M M D D H H M M S S
    ;

TIMEDATE: T I M E D A T E
    ;

DAYNUMBER: D A Y N U M B E R
    ;

OWNER: O W N E R
    ;

GROUPRWX: G R O U  P R W X
    ;

USERBACKUPNAME: U S E R B A C K U P N A M E
    ;

OTHERRWX: O T H E R R W X
    ;

OWNERRWX: O W N E R R W X
    ;

GROUPR: G R O U P R
    ;

GROUPW: G R O U P W
    ;

GROUPX: G R O U P X
    ;

OTHERR: O T H E R R
    ;

OTHERW: O T H E R W
    ;

OTHERX: O T H E R X
    ;

OWNERR: O W N E R R
    ;

OWNERW: O W N E R W
    ;

OWNERX: O W N E R X
    ;

SETUSERCODE: S E T U S E R C O D E
    ;

USEGUARDFILE: U S E G U A R D F I L E
    ;

GUARDOWNER: G U A R D O W N E R
    ;

RWX: R W X
    ;

RW: R W
    ;

RX: R X
    ;

WX: W X
    ;

NO: N O
    ;

BACKUP: B A C K U P
    ;

DSONERROR: D S O N E R R O R
    ;

WAITONERROR: W A I T O N E R R O R
    ;

REPORTS: R E P O R T S
    ;

REPORT: R E P O R T
    ;

SKIPEXCLUSIVE: S K I P E X C L U S I V E
    ;

FROMSTART: F R O M S T A R T
    ;

VERIFY: V E R I F Y
    ;

COMPARE: C O M P A R E
    ;

BECOMEOWNER: B E C O M E O W N E R
    ;

AND: A N D
    ;

LABELSINTABLE: L A B E L S I N T A B L E 
    ;

RESIDENT: R E S I D E N T
    ;

ACTIVE: A C T I V E
    ;

TERMINATED: T E R M I N A T E D
    ;

BADINITIATE: B A D I N I T I A T E
    ;

NEVERUSED: N E V E R U S E D
    ;

COMPLETED: C O M P L E T E D
    ;

EQL: E Q L
    ;

GTR: G T R
    ;

LSS: L S S
    ;

GEQ: G E Q
    ;

LEQ: L E Q
    ;

NEQ: N E Q
    ;

//ONLYC: C;

CC: C C
    ;

SORT: S O R T
    ;

RPG: R P G
    ;

PASCAL: P A S C A L
    ;

NEWP: N E W P
    ;

NDLII: N D L I I
    ;

DMALGOL: D M A L G O L
    ;

DCALGOL: D C A L G O L
    ;

BINDER: B I N D E R
    ;

ALGOL: 'ALGOL'
    ;

PRIORITY: P R I O R I T Y
    ;

AT: A T
    ;

AS: A S
    ;

EXECUTE: E X E C U T E
    ;

ACCESSCODELIST: A C C E S S C O D E L I S T
    ;

ACCESSCODE: A C C E S S C O D E
    ;

BEGIN: B E G I N
    ;

CASE:  C A S E
    ;

COMPILE: C O M P I L E
    ;

COMPILER: C O M P I L E R
    ;

CONVENTION: C O N V E N T I O N
    ;

CLASS: C L A S S
    ;

CHARGECODE: C H A R G E C O D E
    ;

DATA: D A T A
    ;

DISK: D I S K
    ;

DISPLAY: D I S P L A Y
    ;

ELSE: E L S E
    ;

END: E N D
    ;

GENERATE: G E N E R A T E
    ;

EBCDIC: E B C D I C
    ;

ELAPSEDLIMIT: E L A P S E D L I M I T
    ;

FAMILY: F A M I L Y
    ;

KIND: K I N D
    ;

LIBRARY: L I B R A R Y
    ;

TITLE: T I T L E
    ;

WITH: W I T H
    ;

RUN: R U N
    ;

OF: O F
    ;

FOR: F O R
    ;

FROM: F R O M
    ;

JOB: J O B
    ;

OTHERWISE: O T H E R W I S E
    ;

MYPACK: M Y P A C K
    ;

MAXPROCTIME: M A X P R O C T I M E
    ;

MAXIOTIME: M A X I O T I M E
    ;

MAXLINES: M A X L I N E S
    ;

MAXWAIT: M A X W A I T
    ;
    
UNTIL: U N T I L
    ;

USER: U S E R
    ;

USERDATA: U S E R D A T A
    ;

USERDATAFILE: U S E R D A T A F I L E
    ;

USERCODE: U S E R C O D E
    ;

CONSTANT: C O N S T A N T
    ;

BOOLEAN: B O O L E A N
    ;

REAL: R E A L
    ;

INTEGER: I N T E G E R
    ;

ASCENDING: A S C E N D I N G
    ;

DESCENDING: D E S C E N D I N G
    ;

STRING: S T R I N G
    ;

FILES: F I L E S
    ;

FILE: F I L E
    ;

TASK: T A S K
    ;

TRUE: T R U E
    ;

JOBSYMBOL: J O B S Y M B O L
    ;

NOSUMMARY: N O S U M M A R Y
    ;

LOCKDECK: L O C K D E C K
    ;

DECKLABEL: D E C K L A B E L
    ;

EXCLUDE: E X C L U D E
    ;

FALSE: F A L S E
    ;

SUBROUTINE: S U B R O U T I N E
    ;

ABORTED: A B O R T E D
    ;

ABORT: A B O R T
    ;

DENSITY: D E N S I T Y
    ;

STOP: S T O P
    ;

REFERENCE: R E F E R E N C E
    ;
    
WAIT: W A I T
    ;

ON: O N
    ;

OK: O K
    ;

GO: G O
    ;

SYNTAX: S Y N T A X
    ;

CRUNCH: C R U N C H
    ;

LOCK: L O C K
    ;

PURGE: P U R G E
    ;

RELEASE: R E L E A S E
    ;    

REWIND: R E W I N D
    ;

COPY: C O P Y
    ;

ADD: A D D
    ;

CHANGE: C H A N G E
    ;

REMOVE: R E M O V E
    ;

SECURITY: S E C U R I T Y
    ;

ACCEPT: A C C E P T
    ;

TO:  T O
    ;
    
IF: I F
    ;

IS: I S
    ;

ISNT: I S N T
    ;

INSTRUCTION: I N S T R U C T I O N
    ;

FETCH: F E T C H
    ;

ALTER: A L T E R
    ;

PRINT: P R I N T
    ;

PB: P B
    ;

RERUN: R E R U N
    ;

START: S T A R T
    ;

STARTJOB: S T A R T J O B
    ;

STARTTIME: S T A R T T I M E
    ;

ARCHIVE: A R C H I V E
    ;

CATALOG: C A T A L O G
    ;

BLOCKSTRUCTURE: B L O C K S T R U C T U R E
    ;

MODIFY: M O D I F Y
    ;

UNWRAP: U N W R A P
    ;

VALUE: V A L U E
    ;

WHILE: W H I L E
    ;

WRAP:  W R A P
    ;

LOG: L O G
    ;

DO: D O
    ;

BIND: B I N D
    ;

NOLIST: N O L I S T
    ;

TODAY: T O D A Y
    ;

TOMORROW: T O M O R R O W
    ;

SUNDAY: S U N D A Y
    ;

MONDAY: M O N D A Y
    ;

TUESDAY: T U E S D A Y
    ;

WEDNESDAY: W E D N E S D A Y
    ;

THURSDAY: T H U R S D A Y
    ;

FRIDAY: F R I D A Y
    ;

SATURDAY: S A T U R D A Y
    ;

JANUARY: J A N U A R Y
    ;

FEBRUARY: F E B R U A R Y
    ;

MARCH: M A R C H
    ;

APRIL: A P R I L
    ;

MAY: M A Y
    ;

JUNE: J U N E
    ;

JULY: J U L Y
    ;

AUGUST: A U G U S T
    ;

SEPTEMBER: S E P T E M B E R
    ;

OCTOBER: O C T O B E R
    ;

MOD: M O D
    ;

NOVEMBER: N O V E M B E R
    ;

DECEMBER: D E C E M B E R
    ;

ITINERARY: I T I N E R A R Y
    ;

AUTOSWITCHTOMARC: A U T O S W I T C H T O M A R C
    ;

DESTSTATION: D E S T S T A T I O N
    ;

DISPLAYONLYTOMCS: D I S P L A Y O N L Y T O M C S
    ; 

LANGUAGE: L A N G U A G E
    ;

ORGUNIT: O R G U N I T
    ;

SOURCEKIND: S O U R C E K I N D
    ;

SOURCESTATION: S O U R C E S T A T I O N
    ;

STATION: S T A T I O N
    ;

STATIONNAME: S T A T I O N N A M E
    ;

TANKING: T A N K I N G
    ;

OPTION: O P T I O N
    ;

TADS: T A D S
    ;

TASKFILE: T A S K F I L E
    ;

CURRENTDIRECTORY: C U R R E N T D I R E C T O R Y
    ;

DATABASE: D A T A B A S E
    ;

DATAPATH: D A T A P A T H
    ;

EXECUTEPATH: E X E C U T E P A T H
    ;

FILEACCESSRULE: F I L E A C C E S S R U L E
    ;

JOBNUMBER:  J O B N U M B E R
    ;

MIXNUMBER: M I X N U M B E R
    ;

NAME: N A M E
    ;

MPID: M P I D
    ;

WORKLOADGROUP: W O R K L O A D G R O U P
    ;

AX: A X
    ;

LOCKED: L O C K E D
    ; 

PARTNEREXISTS: P A R T N E R E X I S T S
    ;

STATUS: S T A T U S
    ;
OUTPUT: O U T P U T
    ;


ITEMS: I T E M S
    ;

ARE: A R E 
    ;
TARGET: T A R G E T
    ;

TASKLIMIT: T A S K L I M I T
    ;

TASKSTRING: T A S K S T R I N G
    ;

TASKVALUE: T A S K V A L U E
    ;

TYPE: T Y P E
    ;

JOBSUMMARY: J O B S U M M A R Y
    ;

JOBSUMMARYTITLE: J O B S U M M A R Y T I T L E
    ;

NOJOBSUMMARYIO: N O J O B S U M M A R Y I O
    ;

LIBRARYSTATE: L I B R A R Y S T A T E
    ;   

LIBRARYUSERS: L I B R A R Y U S E R S
    ;

CORE: C O R E
    ;

STACKLIMIT: S T A C K L I M I T
    ;

STACKSIZE: S T A C K S I Z E
    ;

BACKUPFAMILY: B A C K U P F A M I L Y
    ;

BDNAME: B D N A M E
    ;

PRINTDEFAULTS: P R I N T D E F A U L T S
    ;

ACCUMIOTIME: A C C U M I O T I M E
    ;

ACCUMPROCTIME: A C C U M P R O C T I M E
    ;

ELAPSEDTIME: E L A P S E D T I M E
    ;

INITPBITCOUNT: I N I T P B I T C O U N T
    ;

INITPBITTIME: I N I T P B I T T I M E
    ;

OTHERPBITCOUNT: O T H E R P B I T C O U N T
    ;

OTHERPBITTIME: O T H E R P B I T T I M E
    ;

TEMPFILEMBYTES: T E M P F I L E M B Y T E S
    ;

RESOURCE: R E S O U R C E
    ; 

SAVEMEMORYLIMIT: S A V E M E M O R Y L I M I T
    ;

TEMPFILELIMIT: T E M P F I L E L I M I T
    ;

TOTALMEMORYLIMIT: T O T A L M E M O R Y L I M I T
    ;

WAITLIMIT: W A I T L I M I T
    ;

BRCLASS: B R C L A S S
    ;

CHECKPOINTABLE: C H E C K P O I N T A B L E
    ;

RESTART: R E S T A R T
    ;

RESTARTED: R E S T A R T E D
    ;

DECKGROUPNO: D E C K G R O U P N O
    ;

ERROR: E R R O R
    ;

HISTORY: H I S T O R Y
    ;

HISTORYCAUSE: H I S T O R Y C A U S E
    ;

HISTORYTYPE: H I S T O R Y T Y P E
    ;

HSPARAMSIZE: H S P A R A M S I Z E
    ;

STACKHISTORY: S T A C K H I S T O R Y
    ;

STOPPOINT: S T O P P O I N T
    ;

SUPPRESSWARNING: S U P P R E S S W A R N I N G
    ;

TASKWARNINGS: T A S K W A R N I N G S
    ;

FAMILYDISK: F A M I L Y D I S K
    ;

DEFAULT: D E F A U L T
    ; 

INITIALIZE: I N I T I A L I Z E
    ;

PROCESS: P R O C E S S
    ;

// CARD: C A R D
//     ;

THEN: T H E N
    ;

ONLY: O N L Y
    ;

MYJOB: M Y J O B
    ;

MYSELF: M Y S E L F
    ;

MAXRECSIZE: M A X R E C S I Z E
    ;

SERIALNO: S E R I A L N O
    ;

SECURITYTYPE: S E C U R I T Y T Y P E
    ;

PUBLIC: P U B L I C
    ;

UNITS: U N I T S
    ;

CHARACTERS: C H A R A C T E R S
    ;

FAMILYOWNER: F A M I L Y O W N E R
    ;

FILENAME: F I L E N A M E
    ;

PRINTCHARGE: P R I N T C H A R G E
    ; 

STATIONLIST: S T A T I O N L I S T
    ;

LFILENAME: L F I L E N A M E
    ;

LTITLE: L T I T L E
    ;

APPLICATIONGROUP: A P P L I C A T I O N G R O U P
    ;

INTNAME: I N T N A M E
    ;

MYHOST: M Y H O S T
    ;

MYHOSTGROUP: M Y H O S T G R O U P
    ;

SCRATCHPOOL: S C R A T C H P O O L
    ;

YOURHOST: Y O U R H O S T
    ;

YOURHOSTGROUP: Y O U R H O S T G R O U P
    ;

YOURUSERCODE: Y O U R U S E R C O D E
    ;

FAMILYNAME: F A M I L Y N A M E
    ;

AFTER: A F T E R
    ;

DESTINATION: D E S T I N A T I O N
    ;

FORMID: F O R M I D
    ;

LICENSEKEY: L I C E N S E K E Y
    ;

NOTE: N O T E
    ;

PATHNAME: P A T H N A M E
    ;

RELEASEID: R E L E A S E I D
    ;

WARNINGS: W A R N I N G S
    ;

ALIGNFILE: A L I G N F I L E
    ;

COPYNAME: C O P Y N A M E
    ;

MYNAME: M Y N A M E
    ;

SECURITYGUARD: S E C U R I T Y G U A R D
    ;

YOURNAME: Y O U R N A M E
    ;

STATE: S T A T E
    ;

TIMESTAMP: T I M E S T A M P
    ;

DEPENDENTSPECS: D E P E N D E N T S P E C S
    ;

NEWFILE: N E W F I L E
    ;

LIBACCESS: L I B A C C E S S
    ;

LIBPARAMETER: L I B P A R A M E T E R
    ;

COMPILEDOK: C O M P I L E D O K
    ;

CHARGE: C H A R G E
    ;   

HEAD: H E A D
    ;

TAIL: T A I L
    ;

NOT: N O T
    ;

HOSTNAME: H O S T N A M E
    ;

DEVICEKIND: D E V I C E K I N D
    ;

OPEN: O P E N
    ;

BLOCKSIZE: B L O C K S I Z E
    ;
    
Identifier: [a-zA-Z][a-zA-Z0-9-_]*
    ;

Num: [0-9]+
    ;

NumCombineWithChar: [a-zA-Z0-9][a-zA-Z0-9]*
    ;

LITERAL:'"' .*? '"' | '\'' .*? '\'' 
    ;

COMMENT: '%' ~[\r\n]*-> channel(HIDDEN)
    ;

// INLINECOMMENT: '%' ~[\r\n]* '%' -> channel(HIDDEN) ;

WS: [ \t\r\n] -> channel(HIDDEN)
    ;

fragment A : 'A';
fragment B : 'B';
fragment C : 'C';
fragment D : 'D';
fragment E : 'E';
fragment F : 'F';
fragment G : 'G';
fragment H : 'H';
fragment I : 'I';
fragment J : 'J';
fragment K : 'K';
fragment L : 'L';
fragment M : 'M';
fragment N : 'N';
fragment O : 'O';
fragment P : 'P';
fragment Q : 'Q';
fragment R : 'R';
fragment S : 'S';
fragment T : 'T';
fragment U : 'U';
fragment V : 'V';
fragment W : 'W';
fragment X : 'X';
fragment Y : 'Y';
fragment Z : 'Z';