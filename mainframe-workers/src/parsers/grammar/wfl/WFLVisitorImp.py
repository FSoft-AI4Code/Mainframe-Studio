import traceback
from typing import List
from loguru import logger

from antlr4 import ParserRuleContext
from antlr4.tree.Tree import TerminalNodeImpl

from parsers.grammar.wfl.WFLParser import WFLParser
from parsers.grammar.wfl.WFLVisitor import WFLVisitor

from parsers.grammar.wfl.wfl_schemas import (WFLStatement,
                                     RunStatement,
                                     SubRoutineDeclaration,
                                     SubroutineInvocationStatement,
                                     CompileStatement,
                                     DisplayStatement,
                                     InitializeStatement,
                                     WaitStatement,
                                     AbortStatement,
                                     AddStatement,
                                     CopyStatement,
                                     ProcessStatement,
                                     BooleanAssignmentStatement,
                                     IntegerAssignmentStatement,
                                     RealAssignmentStatement,
                                     StringAssignmentStatement,
                                     FileAssignmentStatement,
                                     TaskAssignmentStatement,
                                     StartStatement,
                                     IfStatement,
                                     DoStatement,
                                     WhileStatement,
                                     CaseStatement,
                                     CaseClause,
                                     AlterStatement,
                                     ChangeStatement,
                                     CrunchStatement,
                                     GoStatement,
                                     ModifyStatement,
                                     RemoveStatement,
                                     OnStatement,
                                     OpenStatement,
                                     LockStatement,
                                     ReleaseStatement,
                                     ReplaceStatement,
                                     CopyAndCompareStatement,
                                     CopyAndRemoveStatement,
                                     MyselfTaskAssignment,
                                     MyjobTaskAssignment,
                                     PrintStatement,
                                     WrapAndCompressStatement,
                                     StartAndWaitStatement,
                                     Attribute,
                                     Parameter,
                                     Declaration,
                                     Label
                                    )

from parsers.grammar.utils import (
    find_parent_by_type,
    get_original_code_content_without_hidden,
)

# Custom Visitor for Collecting WFL Program Information
class WFLVisitorImp(WFLVisitor):

    # Initialization Method

    def __init__(self):
        
        self.job_name = ""
        self.parameters = []
        self.attributes: List[Attribute] = []
        self.subroutines: List[SubRoutineDeclaration] = []
        self.statements: List[WFLStatement] = []
        self.declarations: List[Declaration] = []
        self.func = {
            "ProcessStatementContext": self.assessProcessStatement,
            "SubroutineInvocationStatementContext": self.assessSubroutineInvocationStatement,
            "CopyStatementContext": self.assessCopyStatement,
            "AddStatementContext": self.assessAddStatement,
            "AbortStatementContext": self.assessAbortStatement,
            "WaitStatementContext": self.assessWaitStatement,
            "InitializeStatementContext": self.assessInitializeStatement,
            "DisplayStatementContext": self.assessDisplayStatement,
            "CompileStatementContext": self.assessCompileStatement,
            "RunStatementContext": self.assessRunStatement,
            "BooleanAssignmentStatementContext": self.assessBooleanAssignmentStatement,
            "IntegerAssignmentStatementContext": self.assessIntegerAssignmentStatement,
            "RealAssignmentStatementContext": self.assessRealAssignmentStatement,
            "StringAssignmentStatementContext": self.assessStringAssignmentStatement,
            "FileAssignmentStatementContext": self.assessFileAssignmentStatement,
            "TaskAssignmentStatementContext": self.assessTaskAssignmentStatement,
            "StartStatementContext": self.assessStartStatement,
            "IfStatementContext": self.assessIfStatement,
            "DoStatementContext": self.assessDoStatement,
            "WhileStatementContext": self.assessWhileStatement,
            "ChangeStatementContext": self.assessChangeStatement,
            "CrunchStatementContext": self.assessCrunchStatement,
            "GoStatementContext": self.assessGoStatement,
            "ModifyStatementContext": self.assessModifyStatement,
            "RemoveStatementContext": self.assessRemoveStatement,
            "OnStatementContext": self.assessOnStatement,
            "OpenStatementContext": self.assessOpenStatement,
            "LockStatementContext": self.assessLockStatement,
            "ReleaseStatementContext": self.assessReleaseStatement,
            "ReplaceStatementContext": self.assessReplaceStatement,
            "CopyAndCompareStatementContext": self.assessCopyAndCompareStatement,
            "CopyAndRemoveStatementContext": self.assessCopyAndRemoveStatement,
            "MyjobTaskAssignmentContext": self.assessMyjobTaskAssignment,
            "MyselfTaskAssignmentContext": self.assessMyselfTaskAssignment,
            "CaseStatementContext": self.assessCaseStatement,
            "LabelContext": self.assessLabel,
            "StartAndWaitStatementContext": self.assessStartAndWaitStatement
        }

    # Helper Methods

    def extract_statement(self, ctx, statement_class, **kwargs):
        raw = get_original_code_content_without_hidden(
            ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex
        )
        start_line = ctx.start.line
        stop_line = ctx.stop.line
        statement = statement_class(
            raw=raw,
            start_line=start_line,
            stop_line=stop_line,
            tag=ctx.__class__.__name__.replace("Context", ""),
            **kwargs,
        )
        return statement

    # Custom visit Methods and Their Corresponding Access Methods

    def assessBeginJob(self, ctx:WFLParser.BeginJobContext):
        try:
            file_path = ctx.filePath().getText() if ctx.filePath() else ""
            return file_path
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process BeginJob, skipping")
            return None
    
    def visitBeginJob(self, ctx:WFLParser.BeginJobContext):
        begin_job = self.assessBeginJob(ctx)
        if begin_job:
            self.job_name = begin_job
        return self.visitChildren(ctx)

    def assessParameterList(self, ctx:WFLParser.ParameterListContext):
        try:
            parameters = []
            parameter_list = ctx.parameter()
            for param in  parameter_list:
                if isinstance(param,ParserRuleContext):
                    param_ = get_original_code_content_without_hidden(ctx.parser,
                                                    start_index=param.start.tokenIndex,
                                                    stop_index=param.stop.tokenIndex
                                                    ).replace('\n', '')
                    parameters.append(Parameter(param=param_))
            return parameters
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement Parameters, skipping")
            return None
    
    def visitParameterList(self, ctx:WFLParser.ParameterListContext):
        parameters = self.assessParameterList(ctx)
        if parameters:
            self.parameters = parameters
        return self.visitChildren(ctx)

    def assesAttributes(self, ctx:WFLParser.AttributesContext):
        attributes = []
        attribute_list = ctx.attribute()
        for attr in attribute_list:
            try:
                attr_  = attr.getChild(0)

                if isinstance(attr_, WFLParser.UserAttributeContext):
                    name = "USER"
                    value = attr_.filePath().getText()
                    attributes.append(self.extract_statement(attr_,
                                                          Attribute,
                                                          name=name,
                                                          value=value
                                                          )
                                    )

                elif isinstance(attr_,WFLParser.UserCodeAttributeContext):
                    name = "USERCODE"
                    value = attr_.filePath().getText()
                    attributes.append(self.extract_statement(attr_,
                                                          Attribute,
                                                          name=name,
                                                          value=value
                                                          )
                                    )
                
                elif isinstance(attr_,WFLParser.ChargeCodeAttributeContext):
                    name = "CHARGECODE"
                    value = attr_.Identifier().getText()
                    attributes.append(self.extract_statement(attr_,
                                                          Attribute,
                                                          name=name,
                                                          value=value
                                                          )
                                    )
                
                elif isinstance(attr_,WFLParser.ClassAttributeContext):
                    name = "CLASS"
                    value = attr_.Num().getText()
                    attributes.append(self.extract_statement(attr_,
                                                          Attribute,
                                                          name=name,
                                                          value=value
                                                          )
                                    )
                
                elif isinstance(attr_,WFLParser.FetchAttributeContext):
                    name = "FETCH"
                    value = attr_.LITERAL().getText()
                    attributes.append(self.extract_statement(attr_,
                                                          Attribute,
                                                          name=name,
                                                          value=value
                                                          )
                                    )
                
                elif isinstance(attr_,WFLParser.AccessCodeAttributeContext):
                    name = "ACCESSCODE"
                    value = attr_.filePath().getText()
                    attributes.append(self.extract_statement(attr_,
                                                          Attribute,
                                                          name=name,
                                                          value=value
                                                          )
                                    )
                
                elif isinstance(attr_,WFLParser.FamilyAttributeContext):
                    name = "FAMILY DISK"
                    value = get_original_code_content_without_hidden(ctx.parser,
                                                    start_index=attr_.start.tokenIndex,
                                                    stop_index=attr_.stop.tokenIndex
                                                    ).replace('\n', '')
                    value = value.replace(name, "")
                    value = value.replace("=", "")
                    attributes.append(self.extract_statement(attr_,
                                                          Attribute,
                                                          name=name,
                                                          value=value.strip()
                                                          )
                                    )
                                    
                elif isinstance(attr_,WFLParser.ElapsedLimitAttributeContext):
                    name = "ELAPSEDLIMIT"
                    value = attr_.Num().getText()
                    attributes.append(self.extract_statement(attr_,
                                                          Attribute,
                                                          name=name,
                                                          value=value
                                                          )
                                    )
                
                elif isinstance(attr_,WFLParser.MaxIOTimeAttributeContext):
                    name = "MAXIOTIME"
                    value = attr_.Num().getText()
                    attributes.append(self.extract_statement(attr_,
                                                          Attribute,
                                                          name=name,
                                                          value=value
                                                          )
                                    )
                
                elif isinstance(attr_,WFLParser.MaxLinesAttributeContext):
                    name = "MAXIOTIME"
                    value = attr_.Num().getText()
                    attributes.append(self.extract_statement(attr_,
                                                          Attribute,
                                                          name=name,
                                                          value=value
                                                          )
                                    )
                
                elif isinstance(attr_,WFLParser.MaxProcTimeAttributeContext):
                    name = "MAXPROCTIME"
                    value = attr_.Num().getText()
                    attributes.append(self.extract_statement(attr_,
                                                          Attribute,
                                                          name=name,
                                                          value=value
                                                          )
                                    )
                
                elif isinstance(attr_,WFLParser.MaxWaitAttributeContext):
                    name = "MAXWAIT"
                    value = attr_.Num().getText()
                    attributes.append(self.extract_statement(attr_,
                                                          Attribute,
                                                          name=name,
                                                          value=value
                                                          )
                                    )
                
                elif isinstance(attr_,WFLParser.StartTimeAttributeContext):
                    name = "STARTTIME"
                    value = get_original_code_content_without_hidden(ctx.parser,
                                                    start_index=attr_.startTimeSpec().start.tokenIndex,
                                                    stop_index=attr_.startTimeSpec().stop.tokenIndex,
                                                    ).replace('\n', '') if attr_.startTimeSpec() else ""
                    
                    attributes.append(self.extract_statement(attr_,
                                                          Attribute,
                                                          name=name,
                                                          value=value
                                                          )
                                    )
                
                elif isinstance(attr_,WFLParser.BdNameAttributeContext):
                    name = "BDNAME"
                    value = attr_.filePath().getText()
                    attributes.append(self.extract_statement(attr_,
                                                          Attribute,
                                                          name=name,
                                                          value=value
                                                          )
                                    )
                
                elif isinstance(attr_,WFLParser.LanguageAttributeContext):
                    name = "LANGUAGE"
                    value = attr_.Identifier().getText()
                    attributes.append(self.extract_statement(attr_,
                                                          Attribute,
                                                          name=name,
                                                          value=value
                                                          )
                                    )
                
                elif isinstance(attr_,WFLParser.OptionsAttributeContext):
                    name = "OPTIONS"
                    value = get_original_code_content_without_hidden(ctx.parser,
                                                    start_index=attr_.optionList().start.tokenIndex,
                                                    stop_index=attr_.optionList().stop.tokenIndex,
                                                    ).replace('\n', '') if attr_.optionList() else ""
                    
                    attributes.append(self.extract_statement(attr_,
                                                          Attribute,
                                                          name=name,
                                                          value=value
                                                          )
                                    )
                    
                elif isinstance(attr_,WFLParser.PriorityAttributeContext):
                    name = "PRIORITY"
                    
                    value = attr_.Num().getText()
                    
                    attributes.append(self.extract_statement(attr_,
                                                          Attribute,
                                                          name=name,
                                                          value=value
                                                          )
                                    )

            except Exception as e:
                logger.error(traceback.format_exc())
                logger.warning("Cannot process Attribute, skipping")

        return attributes

    def visitAttributes(self, ctx:WFLParser.AttributesContext):
        attributes = self.assesAttributes(ctx)
        if attributes:
            self.attributes = attributes
        return self.visitChildren(ctx)
    
    def assessDeclarations(self, ctx:WFLParser.DeclarationsContext):
        declarations = []
        declaration_list = ctx.declaration()

        for declaration in declaration_list:
            try:
                dec = declaration.getChild(0)

                if isinstance(dec, WFLParser.ConstantDeclarationContext):
                    vars = []

                    constant_declaration_elements = dec.constantDeclarationElement()
                    vars = [get_original_code_content_without_hidden(parser=ctx.parser,
                                                      start_index=var.start.tokenIndex,
                                                      stop_index=var.stop.tokenIndex
                                                      ) for var in constant_declaration_elements]

                    declarations.append(self.extract_statement(dec,
                                                          Declaration,
                                                          vars=vars
                                                          )
                                    )
                    
                elif isinstance(dec, WFLParser.BooleanDeclarationContext):
                    vars = []

                    boolean_declaration_elements = dec.booleanDeclarationElement()
                    vars = [get_original_code_content_without_hidden(parser=ctx.parser,
                                                      start_index=var.start.tokenIndex,
                                                      stop_index=var.stop.tokenIndex
                                                      ) for var in boolean_declaration_elements]
                    
                    declarations.append(self.extract_statement(dec,
                                                          Declaration,
                                                          vars=vars
                                                          )
                                    )
                    
                elif isinstance(dec, WFLParser.IntegerDeclarationContext):
                    vars = []

                    integer_declaration_elements = dec.integerDeclarationElement()
                    vars = [get_original_code_content_without_hidden(parser=ctx.parser,
                                                      start_index=var.start.tokenIndex,
                                                      stop_index=var.stop.tokenIndex
                                                      ) for var in integer_declaration_elements]
                    
                    declarations.append(self.extract_statement(dec,
                                                          Declaration,
                                                          vars=vars
                                                          )
                                    )
                    
                elif isinstance(dec, WFLParser.RealDeclarationContext):
                    vars = []

                    real_declaration_elements = dec.realDeclarationElement()
                    vars = [get_original_code_content_without_hidden(parser=ctx.parser,
                                                      start_index=var.start.tokenIndex,
                                                      stop_index=var.stop.tokenIndex
                                                      ) for var in real_declaration_elements]
                    
                    declarations.append(self.extract_statement(dec,
                                                          Declaration,
                                                          vars=vars
                                                          )
                                    )
                    
                elif isinstance(dec, WFLParser.StringDeclarationContext):
                    vars = []

                    string_declaration_elements = dec.stringDeclarationElement()
                    vars = [get_original_code_content_without_hidden(parser=ctx.parser,
                                                      start_index=var.start.tokenIndex,
                                                      stop_index=var.stop.tokenIndex
                                                      ) for var in string_declaration_elements]

                    declarations.append(self.extract_statement(dec,
                                                          Declaration,
                                                          vars=vars
                                                          )
                                    )
                    
                elif isinstance(dec, WFLParser.FileDeclarationContext):
                    vars = []

                    file_declaration_elements = dec.fileDeclarationElement()
                    vars = [get_original_code_content_without_hidden(parser=ctx.parser,
                                                      start_index=var.start.tokenIndex,
                                                      stop_index=var.stop.tokenIndex
                                                      ) for var in file_declaration_elements]
                    
                    declarations.append(self.extract_statement(dec,
                                                          Declaration,
                                                          vars=vars
                                                          )
                                    )
                    
                elif isinstance(dec, WFLParser.TaskDeclarationContext):
                    vars = []

                    task_declaration_elements = dec.taskIdentifierDeclaration()
                    vars = [get_original_code_content_without_hidden(parser=ctx.parser,
                                                      start_index=var.start.tokenIndex,
                                                      stop_index=var.stop.tokenIndex
                                                      ) for var in task_declaration_elements]
                    
                    declarations.append(self.extract_statement(dec,
                                                          Declaration,
                                                          vars=vars
                                                          )
                                    )

            except Exception as e:
                logger.error(traceback.format_exc())
                logger.warning("Cannot process Declaration, skipping")

        return declarations

    def visitDeclarations(self, ctx:WFLParser.DeclarationsContext):
        
        declarations = self.assessDeclarations(ctx)

        if declarations and type(ctx.parentCtx).__name__ == "JobContext":
            self.declarations = declarations

        return self.visitChildren(ctx)
    
    # Get information of the statements

    def assessLabel(self, ctx:WFLParser.LabelContext):
        try:
            label_identifer = ctx.labelIdentifer().getText()

            context_info = self.extract_statement(
                ctx,
                Label,
                label_identifer=label_identifer
                )
            
            return context_info

        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement Label, skipping")
            return None
    
    def visitLabel(self, ctx:WFLParser.LabelContext):
        label = self.assessLabel(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if label and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(label)

        return self.visitChildren(ctx)

    def assessStartAndWaitStatement(self, ctx:WFLParser.StartAndWaitStatementContext):
            try:
                if ctx.filePath():
                    file_path = ctx.filePath().getText()
                else:
                    file_path=file_path

                run_parameter_list = []
                if ctx.runParameterList():
                    for runParameter in list(ctx.runParameterList().getChildren()):
                        if isinstance(runParameter, ParserRuleContext):
                            run_parameter_list.append(runParameter.getText())

                context_info = self.extract_statement(
                    ctx,
                    StartAndWaitStatement,
                    file_path=file_path,
                    run_parameter_list=run_parameter_list
                )
                return context_info
            except Exception:
                logger.error(traceback.format_exc())
                logger.warning("Cannot process statement StartAndWaitStatement, skipping")
                return None
    
    def visitStartAndWaitStatement(self, ctx:WFLParser.StartAndWaitStatementContext):
        start_and_wait_statment = self.assessStartAndWaitStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if start_and_wait_statment and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(start_and_wait_statment)
        return self.visitChildren(ctx)

    def assessWrapAndCompressStatement(self, ctx:WFLParser.WrapAndCompressStatementContext):
        try:
            wrap_and_compress_from = []
            wrap_and_compress_from_list = ctx.wrapAndCompressFrom()
            if wrap_and_compress_from_list:
                for wcf in wrap_and_compress_from_list:
                    wrap_and_compress_from.append(get_original_code_content_without_hidden(ctx.parser,
                                                                            start_index=wcf.start.tokenIndex,
                                                                            stop_index=wcf.stop.tokenIndex
                                                                            ).replace('\n', ''))
            
            task_identifier = ctx.taskIdentifier().getText() if ctx.taskIdentifier() else ""

            if ctx.intoClause():
                into_clause = get_original_code_content_without_hidden(ctx.parser,
                                                        start_index=ctx.intoClause().start.tokenIndex,
                                                        stop_index=ctx.intoClause().stop.tokenIndex,
                                                    ).replace('\n', '')
            else:
                into_clause=into_clause
            
            if ctx.toClause():
                to_clause = get_original_code_content_without_hidden(ctx.parser,
                                                    start_index=ctx.toClause().start.tokenIndex,
                                                    stop_index=ctx.toClause().stop.tokenIndex,
                                                ).replace('\n', '')
                
            else:
                to_clause = ""

            if ctx.fromClause():
                from_clause = get_original_code_content_without_hidden(ctx.parser,
                                                    start_index=ctx.fromClause().start.tokenIndex,
                                                    stop_index=ctx.fromClause().stop.tokenIndex,
                                                ).replace('\n', '')
                
            else:
                from_clause = ""
            
            context_info = self.extract_statement(
                ctx,
                WrapAndCompressStatement,
                wrap_and_compress_from=wrap_and_compress_from,
                task_identifier=task_identifier,
                into_clause=into_clause,
                to_clause=to_clause,
                from_clause=from_clause
                )
            
            return context_info
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement WrapAndCompressStatement, skipping")
            return None

    def visitWrapAndCompressStatement(self, ctx:WFLParser.WrapAndCompressStatementContext):
        wrap_and_compress_statement = self.assessWrapAndCompressStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if wrap_and_compress_statement and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(wrap_and_compress_statement)
        return self.visitChildren(ctx)

    def assessPrintStatement(self, ctx:WFLParser.PrintStatementContext):
        try:
            
            print_specification = get_original_code_content_without_hidden(ctx.parser,
                                                            start_index=ctx.printSpecification().start.tokenIndex,
                                                            stop_index=ctx.printSpecification().stop.tokenIndex
                                                            ).replace('\n', '') if ctx.printSpecification() else ""
            
            print_default = get_original_code_content_without_hidden(ctx.parser,
                                                            start_index=ctx.printDefault().start.tokenIndex,
                                                            stop_index=ctx.printDefault().stop.tokenIndex
                                                            ).replace('\n', '') if ctx.printDefault() else ""
            
            context_info = self.extract_statement(
                ctx,
                PrintStatement,
                print_specification=print_specification,
                print_default=print_default
            )
            return context_info
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement PrintStatement, skipping")
            return None
    
    def visitPrintStatement(self, ctx:WFLParser.PrintStatementContext):
        print_statement = self.assessPrintStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if print_statement and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(print_statement)
        return self.visitChildren(ctx)

    def assessMyjobTaskAssignment(self, ctx:WFLParser.MyjobTaskAssignmentContext):
        try:
            
            reserved_keywords = ctx.reservedKeyword()

            if len(reserved_keywords)==3:
                reserved_keyword_1 = reserved_keywords[0].getText()
                reserved_keyword_2 = reserved_keywords[1].getText()
                reserved_keyword_3 = reserved_keywords[2].getText()
            elif len(reserved_keywords)==2:
                reserved_keyword_1 = reserved_keywords[0].getText()
                reserved_keyword_2 = reserved_keywords[1].getText()
                reserved_keyword_3 = ""
            elif len(reserved_keywords)==1:
                reserved_keyword_1 = reserved_keywords[0].getText()
                reserved_keyword_3 = ""
                if ctx.storageUnit():
                    reserved_keyword_2 = ctx.storageUnit().getText()
                else:
                    reserved_keyword_2 = ""
            else:
                reserved_keyword_1 = ""
                reserved_keyword_2 = ""
                reserved_keyword_3 = ""

            context_info = self.extract_statement(
                ctx,
                MyjobTaskAssignment,
                reserved_keyword_1=reserved_keyword_1,
                reserved_keyword_2=reserved_keyword_2,
                reserved_keyword_3=reserved_keyword_3,
            )
            return context_info
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement MyjobTaskAssignment, skipping")
            return None

    def visitMyjobTaskAssignment(self, ctx:WFLParser.MyjobTaskAssignmentContext):
        myjob_task_assignment = self.assessMyjobTaskAssignment(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if myjob_task_assignment and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(myjob_task_assignment)
        return self.visitChildren(ctx)

    def assessMyselfTaskAssignment(self, ctx:WFLParser.MyselfTaskAssignmentContext):
        try:
            reserved_keywords = ctx.reservedKeyword()

            if len(reserved_keywords)==2:
                reserved_keyword_1 = reserved_keywords[0].getText()
                reserved_keyword_2 = reserved_keywords[1].getText()
            elif len(reserved_keywords)==1:
                reserved_keyword_1 = reserved_keywords[0].getText()
                if ctx.storageUnit():
                    reserved_keyword_2 = ctx.storageUnit().getText()
                else:
                    reserved_keyword_2 = ""
            else:
                reserved_keyword_1=""
                reserved_keyword_2=""

            context_info = self.extract_statement(
                ctx,
                MyselfTaskAssignment,
                reserved_keyword_1=reserved_keyword_1,
                reserved_keyword_2=reserved_keyword_2,
            )
            return context_info
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement MyselfTaskAssignment, skipping")
            return None

    def visitMyselfTaskAssignment(self, ctx:WFLParser.MyselfTaskAssignmentContext):
        myself_task_assignment = self.assessMyselfTaskAssignment(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if myself_task_assignment and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(myself_task_assignment)
        return self.visitChildren(ctx) 

    def assessCopyAndCompareStatement(self, ctx:WFLParser.CopyAndCompareStatementContext):
        try:
            task_identifier = ctx.taskIdentifier().getText() if ctx.taskIdentifier() else ""
            file_path = [f.getText() for f in ctx.filePath()] if ctx.filePath() else ""
            file_referenced_variable = [f.getText() for f in ctx.fileReferencedVariable()] if ctx.fileReferencedVariable() else []
            from_clause = ctx.fromClause().getText() if ctx.fromClause() else ""
            to_clause = ctx.toClause().getText() if ctx.toClause() else ""
            context_info = self.extract_statement(
                ctx,
                CopyAndCompareStatement,
                task_identifier=task_identifier,
                file_path=file_path,
                file_referenced_variable=file_referenced_variable,
                from_clause=from_clause,
                to_clause=to_clause,
            )
            return context_info
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement CopyAndCompareStatement, skipping")
            return None

    def visitCopyAndCompareStatement(self, ctx:WFLParser.CopyAndCompareStatementContext):
        copy_and_compare_statement = self.assessCopyAndCompareStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if copy_and_compare_statement and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(copy_and_compare_statement)
        return self.visitChildren(ctx)

    def assessCopyAndRemoveStatement(self, ctx:WFLParser.CopyAndRemoveStatementContext):
        try:
            task_identifier = ctx.taskIdentifier().getText() if ctx.taskIdentifier() else ""
            file_path = [f.getText() for f in ctx.filePath()] if ctx.filePath() else ""
            file_referenced_variable = [f.getText() for f in ctx.fileReferencedVariable()] if ctx.fileReferencedVariable() else []
            from_clause = ctx.fromClause().getText() if ctx.fromClause() else ""
            to_clause = ctx.toClause().getText() if ctx.toClause() else ""
            context_info = self.extract_statement(
                ctx,
                CopyAndRemoveStatement,
                task_identifier=task_identifier,
                file_path=file_path,
                file_referenced_variable=file_referenced_variable,
                from_clause=from_clause,
                to_clause=to_clause,
            )
            return context_info
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement CopyAndRemoveStatement, skipping")
            return None
    
    def visitCopyAndRemoveStatement(self, ctx:WFLParser.CopyAndRemoveStatementContext):
        copy_and_remove_statement = self.assessCopyAndRemoveStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if copy_and_remove_statement and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(copy_and_remove_statement)
        return self.visitChildren(ctx)

    def assessReplaceStatement(self, ctx:WFLParser.ReplaceStatementContext):
        try:
            replace_options = get_original_code_content_without_hidden(ctx.parser,
                                                        start_index=ctx.replaceOptions().start.tokenIndex,
                                                        stop_index=ctx.replaceOptions().stop.tokenIndex
                                                        ).replace('\n', '') if ctx.replaceOptions() else ""


            copy_request = get_original_code_content_without_hidden(ctx.parser,
                                                        start_index=ctx.copyRequest().start.tokenIndex,
                                                        stop_index=ctx.copyRequest().stop.tokenIndex
                                                        ).replace('\n', '')
            
            task_identifier = ctx.taskIdentifier().getText() if ctx.taskIdentifier() else ""
            
            task_attribute_assignment = []
            taskAttributeAssignment = ctx.taskAttributeAssignment()
            if taskAttributeAssignment:
                for task_attr  in taskAttributeAssignment:
                    task_attribute_assignment.append(get_original_code_content_without_hidden(ctx.parser,
                                                            start_index=task_attr.start.tokenIndex,
                                                            stop_index=task_attr.stop.tokenIndex,
                                ))
                    
            context_info = self.extract_statement(
                ctx,
                ReplaceStatement,
                replace_options=replace_options,
                copy_request=copy_request,
                task_identifier=task_identifier,
                task_attribute_assignment=task_attribute_assignment
            )
            return context_info
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement ReplaceStatement, skipping")
            return None

    def visitReplaceStatement(self, ctx:WFLParser.ReplaceStatementContext):
        replace_statement = self.assessReplaceStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if replace_statement and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(replace_statement)
        return self.visitChildren(ctx)

    def assessReleaseStatement(self, ctx:WFLParser.ReleaseStatementContext):
        try:
            file_identifier = ctx.fileIdentifier().getText() if ctx.fileIdentifier() else ""
            context_info = self.extract_statement(
                ctx,
                ReleaseStatement,
                file_identifier=file_identifier,
            )
            return context_info
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement ReleaseStatement, skipping")
            return None
        
    def visitReleaseStatement(self, ctx:WFLParser.ReleaseStatementContext):
        release_statement = self.assessReleaseStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if release_statement and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(release_statement)
        return self.visitChildren(ctx)

    def assessLockStatement(self, ctx:WFLParser.LockStatementContext):
        try:
            file_identifier = ctx.fileIdentifier().getText() if ctx.fileIdentifier() else ""
            context_info = self.extract_statement(
                ctx,
                LockStatement,
                file_identifier=file_identifier,
            )
            return context_info
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement LockStatement, skipping")
            return None

    def visitLockStatement(self, ctx:WFLParser.LockStatementContext):
        lock_statement = self.assessLockStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if lock_statement and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(lock_statement)
        return self.visitChildren(ctx)

    def assessOpenStatement(self, ctx:WFLParser.OpenStatementContext):
        try:
            file_identifier = ctx.fileIdentifier().getText() if ctx.fileIdentifier() else "" 
            context_info = self.extract_statement(
                ctx,
                OpenStatement,
                file_identifier=file_identifier,
            )
            return context_info
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement OpenStatement, skipping")
            return None
    
    def visitOpenStatement(self, ctx:WFLParser.OpenStatementContext):
        open_statement = self.assessOpenStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if open_statement and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(open_statement)
        return self.visitChildren(ctx)

    def assessOnStatement(self, ctx:WFLParser.OnStatementContext):
        try:
            if ctx.TASKFAULT():
                on_type = "TASKFAULT"
            elif ctx.RESTART():
                on_type = "RESTART"
            else:
                on_type = ""

            statements = []
            statement_list = ctx.statement()
            for statement in statement_list:
                if statement.getChildCount() > 0:
                    child_statement = statement.getChild(0)
                    if type(child_statement).__name__ == "AssignmentStatementContext":
                            child_statement = child_statement.getChild(0)
                    if type(child_statement).__name__ in self.func:
                        statements.append(self.func[type(child_statement).__name__](child_statement))

            context_info = self.extract_statement(
                ctx,
                OnStatement,
                on_type=on_type,
                statements=statements
            )
            return context_info
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement OnStatement, skipping")
            return None
    
    def visitOnStatement(self, ctx:WFLParser.OnStatementContext):
        on_statement = self.assessOnStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if on_statement and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(on_statement)
        return self.visitChildren(ctx)

    def assessRemoveStatement(self, ctx:WFLParser.RemoveStatementContext):
        try:
            file_path = [f.getText() for f in ctx.filePath()] if ctx.filePath() else []
            
            on_clause = ctx.onClause().getText() if ctx.onClause() else ""
            
            from_clause = get_original_code_content_without_hidden(ctx.parser,
                                                    start_index=ctx.fromClause().start.tokenIndex,
                                                    stop_index=ctx.fromClause().stop.tokenIndex).replace('\n', '') if ctx.fromClause() else ""

            context_info = self.extract_statement(
                ctx,
                RemoveStatement,
                file_path=file_path,
                on_clause=on_clause,
                from_clause=from_clause
            )
            return context_info
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement RemoveStatement, skipping")
            return None
    
    def visitRemoveStatement(self, ctx:WFLParser.RemoveStatementContext):
        remove_statement = self.assessRemoveStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if remove_statement and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(remove_statement)
        return self.visitChildren(ctx)

    def assessModifyStatement(self, ctx:WFLParser.ModifyStatementContext):
        try:
            task_identifier_1= ""
            task_identifier_2= ""
            if ctx.filePath():
                file_path = ctx.filePath().getText()
            elif ctx.fileReferencedVariable():
                file_path = ctx.fileReferencedVariable().getText()
            else:
                file_path = ""

            if ctx.storageUnit():
                storage_unit = ctx.storageUnit().getText()
            elif ctx.reservedKeyword():
                storage_unit = ctx.reservedKeyword().getText()
            else:
                storage_unit = ""

            run_parameter_list = []
            runParameterList = ctx.runParameterList()
            if runParameterList:
                for runParameter in list(runParameterList.getChildren()):
                    if isinstance(runParameter, ParserRuleContext):
                        run_parameter_list.append(runParameter.getText())

            taskIdentifier = ctx.taskIdentifier()
            if taskIdentifier:
                task_identifiers = list(ctx.getChildren())
                if len(task_identifiers) == 2:
                    task_identifier_1 = task_identifiers[0].getText()
                    task_identifier_2 = task_identifiers[1].getText()
                else:
                    task_identifier_1 = task_identifiers[0].getText()
                    task_identifier_2 = ""

            task_equation_list = []
            taskEquationList = ctx.taskEquationList()
            if taskEquationList:
                for taskEquation in taskEquationList.getChildren():

                    if isinstance(taskEquation,ParserRuleContext):
                        task_equation_text = get_original_code_content_without_hidden(ctx.parser,
                                                    start_index=taskEquation.start.tokenIndex,
                                                    stop_index=taskEquation.stop.tokenIndex).replace('\n', '')
                        
                        task_equation_list.append(task_equation_text)

            local_data_specification = ctx.localDataSpecification().getText() if ctx.localDataSpecification() else ""
            
            context_info = self.extract_statement(
                ctx,
                ModifyStatement,
                file_path=file_path,
                storage_unit=storage_unit,
                run_parameter_list=run_parameter_list,
                task_identifier_1=task_identifier_1,
                task_identifier_2=task_identifier_2,
                task_equation_list=task_equation_list,
                local_data_specification=local_data_specification
            )

            return context_info
        
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement ModifyStatement, skipping")
            return None

    def visitModifyStatement(self, ctx:WFLParser.ModifyStatementContext):
        modify_statement = self.assessModifyStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if modify_statement and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(modify_statement)
        return self.visitChildren(ctx)

    def assessGoStatement(self, ctx:WFLParser.GoStatementContext):
        try:
            label_identifer = ctx.labelIdentifer().getText() 
            context_info = self.extract_statement(
                ctx,
                GoStatement,
                label_identifer=label_identifer,
            )
            return context_info
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement GoStatement, skipping")
            return None

    def visitGoStatement(self, ctx:WFLParser.GoStatementContext):
        go_statement = self.assessGoStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if go_statement and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(go_statement)
        return self.visitChildren(ctx)

    def assessCrunchStatement(self, ctx:WFLParser.CrunchStatementContext):
        try:
            file_identifier = ctx.fileIdentifier().getText() 
            context_info = self.extract_statement(
                ctx,
                CrunchStatement,
                file_identifier=file_identifier,
            )
            return context_info
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement CrunchStatement, skipping")
            return None

    def visitCrunchStatement(self, ctx:WFLParser.CrunchStatementContext):
        crunch_statement = self.assessCrunchStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if crunch_statement and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(crunch_statement)
        return self.visitChildren(ctx)

    def assessChangeStatement(self, ctx:WFLParser.ChangeStatementContext):
        try:
            changeItem = ctx.changeItem()

            change_item_1 = changeItem[0].getText()
            change_item_2 = changeItem[1].getText()

            family_name = ctx.familyName().getText() if ctx.familyName() else ""

            from_clause = get_original_code_content_without_hidden(ctx.parser,
                                                    start_index=ctx.fromClause().start.tokenIndex,
                                                    stop_index=ctx.fromClause().stop.tokenIndex
            ).replace('\n', '') if ctx.fromClause() else ""

            context_info = self.extract_statement(
                ctx,
                ChangeStatement,
                change_item_1=change_item_1,
                change_item_2=change_item_2,
                family_name=family_name,
                from_clause=from_clause
            )
            return context_info
        
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement ChangeStatement, skipping")
            return None

    def visitChangeStatement(self, ctx:WFLParser.ChangeStatementContext):
        change_statement = self.assessChangeStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if change_statement and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(change_statement)
        return self.visitChildren(ctx)

    def assessAlterStatement(self, ctx:WFLParser.AlterStatementContext):
        try:
            storage_unit = ""

            if ctx.longFileTitle():
                long_name = ctx.longFileTitle().getText()
            elif ctx.longDirectoryTitle():
                long_name = ctx.longFileTitle().getText()
            
            if ctx.storageUnit():
                storage_unit = get_original_code_content_without_hidden(ctx.parser,
                                                         start_index=ctx.storageUnit().start.tokenIndex,
                                                         stop_index=ctx.storageUnit().stop.tokenIndex
                                                         ).replace('\n', '')
                
            alter_attribute_list = []
            alter_attributes = ctx.alterAttributeList().alterAttribute()
            for alter_attr in alter_attributes:
                alter_attribute_list.append(get_original_code_content_without_hidden(ctx.parser,
                                                                      start_index=alter_attr.start.tokenIndex,
                                                                      stop_index=alter_attr.stop.tokenIndex))

            context_info = self.extract_statement(
                ctx,
                AlterStatement,
                long_name=long_name,
                storage_unit=storage_unit,
                alter_attribute_list=alter_attribute_list    
            )
            return context_info
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement AlterStatement, skipping")
            return None

    def visitAlterStatement(self, ctx:WFLParser.AlterStatementContext):
        alter_statement = self.assessAlterStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if alter_statement and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(alter_statement)
        return self.visitChildren(ctx)

    def assessCaseStatement(self, ctx:WFLParser.CaseStatementContext):
        try:
            case_expression = get_original_code_content_without_hidden(ctx.parser,
                                                        start_index=ctx.caseExpression().start.tokenIndex,
                                                        stop_index=ctx.caseExpression().stop.tokenIndex,
            ).replace('\n', '')

            caseClauses = ctx.caseClauses()
            caseClause = caseClauses.caseClause()
            case_clauses = []

            for clause in caseClause:
                case_constant_expression = get_original_code_content_without_hidden(ctx.parser,
                                                              start_index=clause.caseConstantExpression().start.tokenIndex,
                                                              stop_index=clause.caseConstantExpression().stop.tokenIndex).replace('\n', '')
                statement_list = []
                for sta in clause.statement():
                    if sta.getChildCount() > 0:
                        sta_child = sta.getChild(0)
                        if type(sta_child).__name__ == "AssignmentStatementContext":
                            sta_child = sta_child.getChild(0)
                        if (type(sta_child).__name__) in self.func:
                            statement_list.append(self.func[type(sta_child).__name__](sta_child))

                case_clauses.append(CaseClause(case_constant_expression=case_constant_expression,
                                                statement_list=statement_list))

            else_clause = []
            statement_list = ctx.statement()
            for sta in statement_list:
                if sta.getChildCount() > 0:
                    sta_child = sta.getChild(0)
                    if type(sta_child).__name__ == "AssignmentStatementContext":
                            sta_child = sta_child.getChild(0)
                    if (type(sta_child).__name__) in self.func:
                        else_clause.append(self.func[type(sta_child).__name__](sta_child))

            context_info = self.extract_statement(
                ctx,
                CaseStatement,
                case_expression=case_expression,
                case_clauses=case_clauses,
                else_clause=else_clause
            )
            return context_info
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement CaseStatement, skipping")
            return None

    def visitCaseStatement(self, ctx:WFLParser.CaseStatementContext):
        case_statement = self.assessCaseStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if case_statement and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(case_statement)
        return self.visitChildren(ctx)

    def assessWhileStatement(self, ctx:WFLParser.WhileStatementContext):
        try:
            
            condition  = get_original_code_content_without_hidden(ctx.parser,
                                                            start_index=ctx.condition().start.tokenIndex,
                                                            stop_index=ctx.condition().stop.tokenIndex,
            ).replace('\n', '')

            statements = []
            statement_list = ctx.statement()
            for sta in statement_list:
                if sta.getChildCount() > 0:
                    sta_child = sta.getChild(0)
                    if type(sta_child).__name__ == "AssignmentStatementContext":
                            sta_child = sta_child.getChild(0)
                    if (type(sta_child).__name__) in self.func:
                        statements.append(self.func[type(sta_child).__name__](sta_child))

            context_info = self.extract_statement(
                ctx,
                WhileStatement,
                condition=condition,
                statements=statements
            )
            return context_info
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement WhileStatement, skipping")
            return None
        
    def visitWhileStatement(self, ctx:WFLParser.WhileStatementContext):
        while_statement = self.assessWhileStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if while_statement and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(while_statement)
        return self.visitChildren(ctx)

    def assessDoStatement(self, ctx:WFLParser.DoStatementContext):
        try:
            condition = get_original_code_content_without_hidden(ctx.parser,
                                                            start_index=ctx.condition().start.tokenIndex,
                                                            stop_index=ctx.condition().stop.tokenIndex
                                ).replace('\n', '')

            statements = []
            statement_list = ctx.statements()
            statement = statement_list.statement()
            for sta in statement:
                if sta.getChildCount() > 0:
                    sta_child = sta.getChild(0)
                    if type(sta_child).__name__ in self.func:
                        statements.append(self.func[type(sta_child).__name__](sta_child))
                    else:
                        if type(sta_child).__name__ == "AssignmentStatementContext":
                            sta_grand_child = sta_child.getChild(0)
                            if type(sta_grand_child).__name__ in self.func:
                                statements.append(self.func[type(sta_grand_child).__name__](sta_grand_child))

            context_info = self.extract_statement(
                ctx,
                DoStatement,
                condition=condition,
                statements=statements
            )
            return context_info
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement DoStatement, skipping")
            return None

    def visitDoStatement(self, ctx:WFLParser.DoStatementContext):
        do_statement = self.assessDoStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if do_statement and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(do_statement)
        return self.visitChildren(ctx)

    def assessIfStatement(self, ctx:WFLParser.IfStatementContext):
        try:
            condition = get_original_code_content_without_hidden(ctx.parser,
                                                            start_index=ctx.condition().start.tokenIndex,
                                                            stop_index=ctx.condition().stop.tokenIndex,
                                ).replace('\n', '') if ctx.condition() else ""
            
            then_clause = []
            thenClause = ctx.thenClause()
            if thenClause:
                statements = thenClause.statement()
                for statement in statements:
                    if statement.getChildCount() > 0:
                        child_statement = statement.getChild(0)
                        if type(child_statement).__name__ == "AssignmentStatementContext":
                                child_statement = child_statement.getChild(0)
                        if type(child_statement).__name__ in self.func:
                            then_clause.append(self.func[type(child_statement).__name__](child_statement))

            else_clause = []
            elseClause = ctx.elseClause()
            if elseClause:
                statements = elseClause.statement()
                for statement in statements:
                    if statement.getChildCount() > 0:
                        child_statement = statement.getChild(0)
                        if type(child_statement).__name__ == "AssignmentStatementContext":
                            child_statement = child_statement.getChild(0)
                        if type(child_statement).__name__ in self.func:
                            else_clause.append(self.func[type(child_statement).__name__](child_statement))

            context_info = self.extract_statement(
                ctx,
                IfStatement,
                condition=condition,
                then_clause=then_clause,
                else_clause=else_clause,
            )
            return context_info
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement IfStatement, skipping")
            return None

    def visitIfStatement(self, ctx:WFLParser.IfStatementContext):
        if_statement = self.assessIfStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if if_statement and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(if_statement)
        return self.visitChildren(ctx)
    
    def assessStartStatement(self, ctx:WFLParser.StartStatementContext):
        try:
            file_path = ctx.filePath().getText() if ctx.filePath() else ""

            task_identifier = ctx.taskIdentifier().getText() if ctx.taskIdentifier() else ""

            start_parameter_list = []
            startParameterList = ctx.startParameterList()
            if startParameterList:
                namedParameterList = startParameterList.namedParameterList()
                if namedParameterList:
                    namedParameter = namedParameterList.namedParameter()
                    for named_param  in namedParameter:
                        start_parameter_list.append(get_original_code_content_without_hidden(ctx.parser,
                                                            start_index=named_param.start.tokenIndex,
                                                            stop_index=named_param.stop.tokenIndex,
                                ))

                positionalParameterList = startParameterList.positionalParameterList()
                if positionalParameterList:
                    positionalParameter = positionalParameterList.positionalParameter()
                    for pos_param in positionalParameter:
                        start_parameter_list.append(get_original_code_content_without_hidden(ctx.parser,
                                                            start_index=pos_param.start.tokenIndex,
                                                            stop_index=pos_param.stop.tokenIndex,
                                ))
                        
            #
            storage_unit = get_original_code_content_without_hidden(ctx.parser,
                                                          start_index=ctx.storageUnit().start.tokenIndex,
                                                          stop_index=ctx.storageUnit().stop.tokenIndex,
                                ).replace('\n', '') if ctx.storageUnit() else ""
            
            string_primary = get_original_code_content_without_hidden(ctx.parser,
                                                          start_index=ctx.stringPrimary().start.tokenIndex,
                                                          stop_index=ctx.stringPrimary().stop.tokenIndex,
                                ).replace('\n', '') if ctx.stringPrimary() else ""
            
            start_time_attribute = get_original_code_content_without_hidden(ctx.parser,
                                                          start_index=ctx.startTimeAttribute().start.tokenIndex,
                                                          stop_index=ctx.startTimeAttribute().stop.tokenIndex,
                                ).replace('\n', '') if ctx.startTimeAttribute() else ""

            context_info = self.extract_statement(
                ctx,
                StartStatement,
                file_path=file_path,
                task_identifier=task_identifier,
                start_parameter_list=start_parameter_list,
                storage_unit=storage_unit,
                string_primary=string_primary,
                start_time_attribute=start_time_attribute

            )
            return context_info
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement StartStatement, skipping")
            return None
    
    def visitStartStatement(self, ctx:WFLParser.StartStatementContext):
        start_statement = self.assessStartStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if start_statement and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(start_statement)
        return self.visitChildren(ctx)

    def assessTaskAssignmentStatement(self, ctx:WFLParser.TaskAssignmentStatementContext):
        try:
            task_identifier = ctx.taskIdentifier().getText()

            task_attribute_assignment = []
            taskAttributeAssignment = ctx.taskAttributeAssignment()
            if taskAttributeAssignment:
                for task_attr  in taskAttributeAssignment:
                    task_attribute_assignment.append(get_original_code_content_without_hidden(ctx.parser,
                                                            start_index=task_attr.start.tokenIndex,
                                                            stop_index=task_attr.stop.tokenIndex,
                                ))

            file_equation = []
            fileEquation = ctx.fileEquation()
            if fileEquation:
                for file_eq in fileEquation:
                    file_equation.append(get_original_code_content_without_hidden(ctx.parser,
                                                            start_index=file_eq.start.tokenIndex,
                                                            stop_index=file_eq.stop.tokenIndex,
                                ))

            context_info = self.extract_statement(
                ctx,
                TaskAssignmentStatement,
                task_identifier=task_identifier,
                task_attribute_assignment=task_attribute_assignment,
                file_equation=file_equation
            )
            return context_info
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement TaskAssignmentStatement, skipping")
            return None

    def visitTaskAssignmentStatement(self, ctx:WFLParser.TaskAssignmentStatementContext):
        file_assigment_statement = self.assessTaskAssignmentStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        great_great_grand_parent = great_grand_parent.parentCtx # job
        
        if file_assigment_statement and type(great_great_grand_parent).__name__ == "JobContext":
            self.statements.append(file_assigment_statement)
        return self.visitChildren(ctx)
    
    def assessFileAssignmentStatement(self, ctx:WFLParser.FileAssignmentStatementContext):
        try:
            file_identifier = ctx.fileIdentifier().getText()

            file_attribute_assignment = []
            fileAttributeAssignment = ctx.fileAttributeAssignment()
            if fileAttributeAssignment:
                for file_attr  in fileAttributeAssignment:
                    file_attribute_assignment.append(get_original_code_content_without_hidden(ctx.parser,
                                                            start_index=file_attr.start.tokenIndex,
                                                            stop_index=file_attr.stop.tokenIndex,
                                ))

            context_info = self.extract_statement(
                ctx,
                FileAssignmentStatement,
                file_identifier=file_identifier,
                file_attribute_assignment=file_attribute_assignment
            )
            return context_info
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement FileAssignmentStatement, skipping")
            return None

    def visitFileAssignmentStatement(self, ctx:WFLParser.FileAssignmentStatementContext):
        file_assigment_statement = self.assessFileAssignmentStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        great_great_grand_parent = great_grand_parent.parentCtx # job
        
        if file_assigment_statement and type(great_great_grand_parent).__name__ == "JobContext":
            self.statements.append(file_assigment_statement)
        return self.visitChildren(ctx)
    
    def assessStringAssignmentStatement(self, ctx:WFLParser.StringAssignmentStatementContext):
        try:
            string_identifier = ctx.stringIdentifier().getText()
            if ctx.stringExpression():
                string_expression = get_original_code_content_without_hidden(ctx.parser,
                                                            start_index=ctx.stringExpression().start.tokenIndex,
                                                            stop_index=ctx.stringExpression().stop.tokenIndex,
                                    ).replace('\n', '')
            else:
                string_expression=""
            
            context_info = self.extract_statement(
                ctx,
                StringAssignmentStatement,
                string_identifier=string_identifier,
                string_expression=string_expression
            )
            return context_info
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement StringAssignmentStatement, skipping")
            return None

    def visitStringAssignmentStatement(self, ctx:WFLParser.StringAssignmentStatementContext):
        string_assignment = self.assessStringAssignmentStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        great_great_grand_parent = great_grand_parent.parentCtx # job
        if string_assignment and type(great_great_grand_parent).__name__ == "JobContext":
            self.statements.append(string_assignment)
        return self.visitChildren(ctx)

    def assessRealAssignmentStatement(self, ctx:WFLParser.RealAssignmentStatementContext):
        try:
            real_identifier = ctx.realIdentifier().getText()
            real_expression = get_original_code_content_without_hidden(ctx.parser,
                                                          start_index=ctx.realExpression().start.tokenIndex,
                                                          stop_index=ctx.realExpression().stop.tokenIndex,
                                ).replace('\n', '')
            context_info = self.extract_statement(
                ctx,
                RealAssignmentStatement,
                real_identifier=real_identifier,
                real_expression=real_expression
            )
            return context_info
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement RealAssignmentStatement, skipping")
            return None
    
    def visitRealAssignmentStatement(self, ctx:WFLParser.RealAssignmentStatementContext):
        real_assignment = self.assessRealAssignmentStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        great_great_grand_parent = great_grand_parent.parentCtx # job
        
        if real_assignment and type(great_great_grand_parent).__name__ == "JobContext":
            self.statements.append(real_assignment)
        return self.visitChildren(ctx)
    
    def assessIntegerAssignmentStatement(self, ctx:WFLParser.IntegerAssignmentStatementContext):
        try:
            integer_identifier = ctx.integerIdentifier().getText()
            integer_expression = get_original_code_content_without_hidden(ctx.parser,
                                                          start_index=ctx.integerExpression().start.tokenIndex,
                                                          stop_index=ctx.integerExpression().stop.tokenIndex,
                                ).replace('\n', '')
            context_info = self.extract_statement(
                ctx,
                IntegerAssignmentStatement,
                integer_identifier=integer_identifier,
                integer_expression=integer_expression
            )
            return context_info
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement IntegerAssignmentStatement, skipping")
            return None

    def visitIntegerAssignmentStatement(self, ctx:WFLParser.IntegerAssignmentStatementContext):
        integer_assignment = self.assessIntegerAssignmentStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        great_great_grand_parent = great_grand_parent.parentCtx # job
        
        if integer_assignment and type(great_great_grand_parent).__name__ == "JobContext":
            self.statements.append(integer_assignment)
        return self.visitChildren(ctx)
    
    def assessBooleanAssignmentStatement(self, ctx:WFLParser.BooleanAssignmentStatementContext):
        try:
            boolean_identifier = ctx.booleanIdentifier().getText()
            boolean_expression = get_original_code_content_without_hidden(ctx.parser,
                                                          start_index=ctx.booleanConstantExpression().start.tokenIndex,
                                                          stop_index=ctx.booleanConstantExpression().stop.tokenIndex,
                                ).replace('\n', '')
            context_info = self.extract_statement(
                ctx,
                BooleanAssignmentStatement,
                boolean_identifier=boolean_identifier,
                boolean_expression=boolean_expression
            )
            return context_info
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement BooleanAssignmentStatement, skipping")
            return None

    def visitBooleanAssignmentStatement(self, ctx:WFLParser.BooleanAssignmentStatementContext):
        boolean_assignment = self.assessBooleanAssignmentStatement(ctx)
        parent = ctx.parentCtx # assign statement
        grand_parent = parent.parentCtx # statement
        great_grand_parent = grand_parent.parentCtx # statements
        great_great_grand_parent = great_grand_parent.parentCtx # job
        
        if boolean_assignment and type(great_great_grand_parent).__name__ == "JobContext":
            self.statements.append(boolean_assignment)
        return self.visitChildren(ctx)

    def assessProcessStatement(self, ctx:WFLParser.ProcessStatementContext):
        try:
            task_identifier = ctx.taskIdentifier().getText() if ctx.taskIdentifier() else ""

            task_equation_list = []
            taskEquationList = ctx.taskEquationList()
            if taskEquationList:
                for task_equation in list(taskEquationList.getChildren()):
                    if isinstance(task_equation, ParserRuleContext):
                        task_equation_text = get_original_code_content_without_hidden(ctx.parser,
                                                            start_index=task_equation.start.tokenIndex,
                                                            stop_index=task_equation.stop.tokenIndex,
                                                            ).replace('\n', '')
                        task_equation_list.append(task_equation_text)

            statement = None
            if ctx.addStatement():
                statement = self.func["AddStatementContext"](ctx.addStatement())
            elif ctx.compileStatement():
                statement = self.func["CompileStatementContext"](ctx.compileStatement())
            elif ctx.runStatement():
                statement = self.func["RunStatementContext"](ctx.runStatement())
            elif ctx.subroutineInvocationStatement():
                statement = self.func["SubroutineInvocationStatementContext"](ctx.subroutineInvocationStatement())
            elif ctx.copyStatement():
                statement = self.func["CopyStatementContext"](ctx.copyStatement())
            elif ctx.subroutineInvocationStatement():
                statement = self.func["SubroutineInvocationStatementContext"](ctx.subroutineInvocationStatement())

            context_info = self.extract_statement(
                ctx,
                ProcessStatement,
                task_identifier=task_identifier,
                statement = statement
            )
            return context_info
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement ProcessStatement, skipping")
            return None

    def visitProcessStatement(self, ctx:WFLParser.ProcessStatementContext):
        process_statement = self.assessProcessStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if process_statement and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(process_statement)
        return self.visitChildren(ctx)

    def assessCopyStatement(self, ctx:WFLParser.CopyStatementContext):
        try:
            task_identifier = ctx.taskIdentifier().getText() if ctx.taskIdentifier() else ""

            copy_protocol = get_original_code_content_without_hidden(ctx.parser,
                                                          start_index=ctx.copyProtocol().start.tokenIndex,
                                                          stop_index=ctx.copyProtocol().stop.tokenIndex,
                                ).replace('\n', '') if ctx.copyProtocol() else ""

            # Copy From Clause As a List of String
            copy_from_clause = []
            copyFromClause = ctx.copyFromClause()
            if copyFromClause:
                for copy_from in copyFromClause:
                    if isinstance(copy_from,ParserRuleContext):
                        copy_from_clause.append(get_original_code_content_without_hidden(ctx.parser,
                                                            start_index=copy_from.start.tokenIndex,
                                                            stop_index=copy_from.stop.tokenIndex,
                                                            exclude_token_types=[448]  # 448 is the COMMENT token type
                                    ))

            # Copy From Clause As a String
            # copy_from_clause = ""
            # copyFromClause = ctx.copyFromClause()
            # if copyFromClause:
            #     copy_from_clause = get_original_code_content_without_hidden(ctx.parser,
            #                                                  start_index=copyFromClause.start.tokenIndex,
            #                                                  stop_index=copyFromClause.stop.tokenIndex,
            #                                                  exclude_token_types=[448]  # 448 is the COMMENT token type
            #     )
            
            to_clause = get_original_code_content_without_hidden(ctx.parser,
                                                          start_index=ctx.toClause().start.tokenIndex,
                                                          stop_index=ctx.toClause().stop.tokenIndex,
                                ).replace('\n', '') if ctx.toClause() else ""
            
            context_info = self.extract_statement(
                ctx,
                CopyStatement,
                task_identifier = task_identifier,
                to_clause = to_clause,
                copy_from_clause = copy_from_clause,
                copy_protocol = copy_protocol,
            )

            return context_info
        
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement CopyStatement, skipping")
            return None
    
    def visitCopyStatement(self, ctx:WFLParser.CopyStatementContext):
        copy_statement = self.assessCopyStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if copy_statement and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(copy_statement)
        return self.visitChildren(ctx)

    def assessAddStatement(self, ctx:WFLParser.AddStatementContext):
        try:
            task_identifier = ctx.taskIdentifier().getText() if ctx.taskIdentifier() else ""

            add_options = []
            addOptions = ctx.addOptions()
            if addOptions:
                addOption = addOptions.addOption()
                for add_option in addOption:
                    if isinstance(add_option, ParserRuleContext) :
                        add_options.append(get_original_code_content_without_hidden(ctx.parser,
                                                            start_index=add_option.start.tokenIndex,
                                                            stop_index=add_option.stop.tokenIndex,
                                    ))
            
            copy_request = get_original_code_content_without_hidden(ctx.parser,
                                                          start_index=ctx.copyRequest().start.tokenIndex,
                                                          stop_index=ctx.copyRequest().stop.tokenIndex,
                                ).replace('\n', '') if ctx.copyRequest() else ""
            
            task_attribute_assignment = get_original_code_content_without_hidden(ctx.parser,
                                                          start_index=ctx.taskAttributeAssignment().start.tokenIndex,
                                                          stop_index=ctx.taskAttributeAssignment().stop.tokenIndex,
                                ).replace('\n', '') if ctx.taskAttributeAssignment() else ""
            
            from_clause = get_original_code_content_without_hidden(ctx.parser,
                                                          start_index=ctx.fromClause().start.tokenIndex,
                                                          stop_index=ctx.fromClause().stop.tokenIndex,
                                ).replace('\n', '') if ctx.fromClause() else ""
            
            to_clause = get_original_code_content_without_hidden(ctx.parser,
                                                          start_index=ctx.toClause().start.tokenIndex,
                                                          stop_index=ctx.toClause().stop.tokenIndex,
                                ).replace('\n', '') if ctx.toClause() else ""
            

            context_info = self.extract_statement(
                ctx,
                AddStatement,
                task_identifier=task_identifier,
                copy_request=copy_request,
                from_clause=from_clause,
                to_clause=to_clause,
                task_attribute_assignment=task_attribute_assignment,
                )
            
            return context_info
        
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement AddStatement, skipping")
            return None
    
    def visitAddStatement(self, ctx:WFLParser.AddStatementContext):
        add_statement = self.assessAddStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if add_statement and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(add_statement)
        return self.visitChildren(ctx)

    def assessAbortStatement(self, ctx:WFLParser.AbortStatementContext):
        try:
            task_identifier = ctx.taskIdentifier().getText() if ctx.taskIdentifier() else ""
            string_expression = get_original_code_content_without_hidden(ctx.parser,
                                                          start_index=ctx.stringConstantExpression().start.tokenIndex,
                                                          stop_index=ctx.stringConstantExpression().stop.tokenIndex,
                                ).replace('\n', '') if ctx.stringConstantExpression() else ""
            context_info = self.extract_statement(
                ctx,
                AbortStatement,
                task_identifier=task_identifier,
                string_expression=string_expression
            )
            return context_info
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement AbortStatement, skipping")
            return None
    
    def visitAbortStatement(self, ctx:WFLParser.AbortStatementContext):
        abort_statement = self.assessAbortStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if abort_statement and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(abort_statement)
        return self.visitChildren(ctx)

    def assessWaitStatement(self, ctx:WFLParser.WaitStatementContext):
        try:
            wait_content = get_original_code_content_without_hidden(ctx.parser,
                                                          start_index=ctx.waitContent().start.tokenIndex,
                                                          stop_index=ctx.waitContent().stop.tokenIndex,
                                ).replace('\n', '') if ctx.waitContent() else ""
            context_info = self.extract_statement(
                ctx,
                WaitStatement,
                wait_content = wait_content,
            )
            return context_info
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement WaitStatement, skipping")
            return None
    
    def visitWaitStatement(self, ctx:WFLParser.WaitStatementContext):
        wait_statement = self.assessWaitStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if wait_statement and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(wait_statement)
        return self.visitChildren(ctx)

    def assessInitializeStatement(self, ctx:WFLParser.InitializeStatementContext):
        try:
            task_identifier = ctx.taskIdentifier().getText()
            context_info = self.extract_statement(
                ctx,
                InitializeStatement,
                task_identifier=task_identifier,
            )
            return context_info
        
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement InitializeStatement, skipping")
            return None
    
    def visitInitializeStatement(self, ctx:WFLParser.InitializeStatementContext):
        initialize_statement = self.assessInitializeStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if initialize_statement and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(initialize_statement)
        return self.visitChildren(ctx)

    def assessDisplayStatement(self, ctx:WFLParser.DisplayStatementContext):
        try:
            string_expression = get_original_code_content_without_hidden(ctx.parser,
                                                          start_index=ctx.stringConstantExpression().start.tokenIndex,
                                                          stop_index=ctx.stringConstantExpression().stop.tokenIndex,
                                ).replace('\n', '')

            context_info = self.extract_statement(
                ctx,
                DisplayStatement,
                string_expression=string_expression,
            )
            return context_info
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement DisplayStatement, skipping")
            return None
    
    def visitDisplayStatement(self, ctx:WFLParser.DisplayStatementContext):
        display_statement = self.assessDisplayStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if display_statement and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(display_statement)
        return self.visitChildren(ctx)

    def assessCompileStatement(self, ctx:WFLParser.CompileStatementContext):
        try:
            # First Pass
            file_path = ctx.filePath().getText() if ctx.filePath() else ""
            # Second Pass
            if file_path == "":
                file_path = ctx.fileReferencedVariable().getText() if ctx.fileReferencedVariable() else ""

            task_identifier_1 = ""
            task_identifier_2 = ""
            taskIdentifier = ctx.taskIdentifier()
            
            if taskIdentifier:
                if len(taskIdentifier) == 2:
                    task_identifier_1 = taskIdentifier[0].getText()
                    task_identifier_2 = taskIdentifier[1].getText()
                else:
                    task_identifier_1 = taskIdentifier[0].getText()

            compiler_name = get_original_code_content_without_hidden(ctx.parser,
                                                          start_index=ctx.compilerName().start.tokenIndex,
                                                          stop_index=ctx.compilerName().stop.tokenIndex,
                                ).replace('\n', '') if ctx.compilerName() else ""
            
            family_name = get_original_code_content_without_hidden(ctx.parser,
                                                          start_index=ctx.familyName().start.tokenIndex,
                                                          stop_index=ctx.familyName().stop.tokenIndex,
                                ).replace('\n', '') if ctx.familyName() else ""
            
            compiler_title = get_original_code_content_without_hidden(ctx.parser,
                                                          start_index=ctx.compilerTitle().start.tokenIndex,
                                                          stop_index=ctx.compilerTitle().stop.tokenIndex,
                                ).replace('\n', '') if ctx.compilerTitle() else ""
            
            compiler_task_equation_list = get_original_code_content_without_hidden(ctx.parser,
                                                          start_index=ctx.compilerTaskEquationList().start.tokenIndex,
                                                          stop_index=ctx.compilerTaskEquationList().stop.tokenIndex,
                                ).replace('\n', '') if ctx.compilerTaskEquationList() else ""
            
            storage_unit = get_original_code_content_without_hidden(ctx.parser,
                                                          start_index=ctx.storageUnit().start.tokenIndex,
                                                          stop_index=ctx.storageUnit().stop.tokenIndex,
                                ).replace('\n', '') if ctx.storageUnit() else ""
            


            context_info = self.extract_statement(
            ctx,
            CompileStatement,
            file_path = file_path,
            task_identifier_1 = task_identifier_1,
            task_identifier_2 = task_identifier_2,
            compiler_name = compiler_name,
            family_name = family_name,
            compiler_title = compiler_title,
            compiler_task_equation_list = compiler_task_equation_list,
            storage_unit=storage_unit
            )
            return context_info
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement CompileStatement, skipping")
            return None
        
    def visitCompileStatement(self, ctx:WFLParser.CompileStatementContext):
        compile_statement = self.assessCompileStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if compile_statement and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(compile_statement)
        return self.visitChildren(ctx)

    def assessSubroutineInvocationStatement(self, ctx:WFLParser.SubroutineInvocationStatementContext):
        try:
            subroutine_identifier = ctx.subroutineIdentifier().getText()
            
            argument_list = []
            argumentList = ctx.argumentList()
            if argumentList:
                arguments = argumentList.argument()
                for argument in arguments:
                    argument_value = get_original_code_content_without_hidden(ctx.parser,
                                                          start_index=argument.start.tokenIndex,
                                                          stop_index=argument.stop.tokenIndex,
                                ).replace('\n', '')
                    argument_list.append(argument_value)

            subroutine_invocation_statement = self.extract_statement(
                ctx,
                SubroutineInvocationStatement,
                subroutine_identifier =subroutine_identifier,
                argument_list = argument_list
            )

            return subroutine_invocation_statement

        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement SubroutineInvocationStatement, skipping")
            return None

    def visitSubroutineInvocationStatement(self, ctx:WFLParser.SubroutineInvocationStatementContext):
        subroutine_invocation_statement = self.assessSubroutineInvocationStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if subroutine_invocation_statement and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(subroutine_invocation_statement)
        return self.visitChildren(ctx)

    def assessSubroutineDeclaration(self, ctx:WFLParser.SubroutineDeclarationContext):
        try:
            # Get subrountine's name
            subroutine_name = ctx.subroutineName().getText()
            # Get subrountine's parameters
            subroutine_parameters = []
            subroutineParameters = ctx.subroutineParameters()
            if subroutineParameters:
                subroutineParameterList = subroutineParameters.subroutineParameterList()
                subroutineParameter = subroutineParameterList.subroutineParameter()
                for parameter in subroutineParameter:
                    subroutine_parameters.append(get_original_code_content_without_hidden(ctx.parser,
                                                          start_index=parameter.start.tokenIndex,
                                                          stop_index=parameter.stop.tokenIndex,
                                ))
            
            # Get subrountine's declarations
            declarations = []
            if ctx.subroutineBlock():
                if ctx.subroutineBlock().declarations():
                    declarations = self.assessDeclarations(ctx.subroutineBlock().declarations())

            
            # Get subroutine's statements
            statements = []
            if ctx.statement():
                statement = ctx.statement()
                if statement.getChildCount() > 0:
                    child_statement = statement.getChild(0)
                    if type(child_statement).__name__ in self.func:
                        res = self.func[type(child_statement).__name__](child_statement)
                        statements.append(res)
                
            elif ctx.subroutineBlock():
                subroutine_block = ctx.subroutineBlock()
                if subroutine_block.statements():
                    statements_ctx = subroutine_block.statements()
                    statement_list = statements_ctx.statement()
                    for statement in statement_list:
                        if statement.getChildCount() > 0:
                            child_statement = statement.getChild(0)
                            if type(child_statement).__name__=="AssignmentStatementContext":
                                child_statement = child_statement.getChild(0)
                            if type(child_statement).__name__ in self.func:
                                res = self.func[type(child_statement).__name__](child_statement)
                                statements.append(res)

            subroutine_declaration = self.extract_statement(
                ctx,
                SubRoutineDeclaration,
                subroutine_name = subroutine_name,
                subroutine_parameters = subroutine_parameters,
                statements=statements,
                declarations=declarations
            )
            return subroutine_declaration

        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process SubroutineDeclaration, skipping")
            return None

    def visitSubroutineDeclaration(self, ctx:WFLParser.SubroutineDeclarationContext):
        subroutine_declaration = self.assessSubroutineDeclaration(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if subroutine_declaration and type(great_grand_parent).__name__ == "JobContext":
            self.subroutines.append(subroutine_declaration)
        return self.visitChildren(ctx)

    def assessRunStatement(self, ctx:WFLParser.RunStatementContext):
        try:
            if ctx.filePath():
                file_path = ctx.filePath().getText()
            elif ctx.fileReferencedVariable():
                file_path = ctx.fileReferencedVariable().getText()
            else:
                file_path = ""

            task_identifier = ctx.taskIdentifier()
            if task_identifier:
                task_identifiers = list(task_identifier)
                if len(task_identifiers) == 2:
                    task_identifier = task_identifiers[1].getText()
                elif len(task_identifiers)==1:
                    task_identifier = task_identifiers[0].getText()
                else:
                    task_identifier = ""
            else:
                task_identifier = ""

            run_parameter_list = []

            runParameterList = ctx.runParameterList()
            if  runParameterList:
                runParameter = runParameterList.runParameter()
                if runParameter:
                    for param in runParameter:
                        param_text = get_original_code_content_without_hidden(ctx.parser,
                                                               start_index=param.start.tokenIndex,
                                                               stop_index=param.stop.tokenIndex).replace('\n', '')
                        run_parameter_list.append(param_text)


            # Check parent is subroutine
            subroutine_declaration = find_parent_by_type(ctx, WFLParser.SubroutineDeclarationContext)
            if subroutine_declaration:
                subroutine_name = subroutine_declaration.subroutineName().getText()
            else:
                subroutine_name = ""

            # Check task attributes
            task_equation_list  = []
            task_equations = ctx.taskEquationList()
            if task_equations and type(task_equations).__name__ != "ErrorNodeImpl":
                for task_equation in task_equations.getChildren():
                    task_equation_list.append(get_original_code_content_without_hidden(parser=ctx.parser,
                                                           start_index=task_equation.start.tokenIndex,
                                                           stop_index=task_equation.stop.tokenIndex
                                                           ))
                    
            # Check local data specifications
            local_data_specification_list = ctx.localDataSpecification()
            if local_data_specification_list:
                local_data_specification = get_original_code_content_without_hidden(parser=ctx.parser,
                                                           start_index=local_data_specification_list.start.tokenIndex,
                                                           stop_index=local_data_specification_list.stop.tokenIndex
                                                           ).replace('\n', '')
            else:
                local_data_specification = ""

            if ctx.storageUnit():
                storage_unit = get_original_code_content_without_hidden(parser=ctx.parser,
                                                           start_index=ctx.storageUnit().start.tokenIndex,
                                                           stop_index=ctx.storageUnit().stop.tokenIndex
                                                           ).replace('\n', '')
            elif ctx.reservedKeyword():
                storage_unit = get_original_code_content_without_hidden(parser=ctx.parser,
                                                           start_index=ctx.reservedKeyword().start.tokenIndex,
                                                           stop_index=ctx.reservedKeyword().stop.tokenIndex
                                                           ).replace('\n', '')
            else:
                storage_unit = ""

            statement = self.extract_statement(
                ctx,
                RunStatement,
                file_path = file_path,
                task_identifier = task_identifier,
                run_parameter_list = run_parameter_list,
                subroutine_name = subroutine_name,
                task_equation_list=task_equation_list,
                local_data_specification=local_data_specification,
                storage_unit=storage_unit
            )
            
            return statement
        except Exception:
            logger.error(traceback.format_exc())
            logger.warning("Cannot process statement RunStatement, skipping")
            return None

    def visitRunStatement(self, ctx:WFLParser.RunStatementContext):
        run_statement = self.assessRunStatement(ctx)
        parent = ctx.parentCtx
        grand_parent = parent.parentCtx
        great_grand_parent = grand_parent.parentCtx
        
        if run_statement and type(great_grand_parent).__name__ == "JobContext":
            self.statements.append(run_statement)
        return self.visitChildren(ctx)
