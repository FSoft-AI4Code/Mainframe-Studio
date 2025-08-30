from typing import List
from antlr4 import ParserRuleContext

from parsers.grammar.clist.ClistVisitor import ClistVisitor
from parsers.grammar.clist.ClistParser import ClistParser
from parsers.grammar.clist.clist_schemas import Statement, ControlStatement, WriteStatement, IfStatement, SubmitStatement, ISPExecStatement, VgetService, FTOpenSevice, FTInclService, FTCloseService, DoEndStatement, ATTNStatement, InlineStatement, ReadStatement, SmCopyStatement, EditStatement, InsertStatement, ChangeStatement, FindStatement, WriteNrStatement, GotoStatement, FreeFileStatement, AllocStatement, RunStatement,DSNEndStatement, CallStatement, OpenfileStatement, GetfileStatement, ClosefileStatement, SetStatement, DeleteStatement, GlobalStatement, AttributeStatement, ListDmsStatement, BrowseService, EditService, FtEraseService, VputService, LminitService, LmcopyService, LmfreeService, TableService, ControlService, LogService, DisplayService, AddpopService,ExecStatement, OutputStatement, CancelStatement, KdsPrintStatement, HrecoverStatement, JprintrStatement, HlistStatement, DoWhileStatement, PutfileStatement, ReaddvalStatement, SelectStatement, ErrorStatement, ReturnStatement, Label
from parsers.grammar.utils import get_original_code_content
class ClistVisitorImp(ClistVisitor):
    def __init__(self):
        self.statements: List[Statement] = []
        self.labels: List[Label] = []
        self.func = {
            "ControlStatementContext" : self.assess_control_statement,
            "WriteStatementContext": self.assess_write_statement,
            "WriteNrStatementContext": self.assess_writenr_statement,
            "SubmitStatementContext": self.assess_submit_statement,
            "AttnStatementContext": self.assess_attn_statement,
            "IspExecStatementContext": self.assess_isp_exec_statement,
            "DoEndStatementContext": self.assess_doend_statement,
            "IfStatementContext": self.assess_if_statement,
            "ExitStatementContext": self.assess_exit_statement,
            "ATTNStatementContext": self.assess_attn_statement,
            "InlineStatementContext": self.assess_inline_statement,
            "ReadStatementContext": self.assess_read_statement,
            "SmCopyStatementContext": self.assess_smcopy_statement,
            "EditStatementContext": self.assess_edit_statement,
            "InsertStatementContext": self.assess_insert_statement,
            "ChangeStatementContext": self.assess_change_statement,
            "FindStatementContext": self.assess_find_statement,
            "GotoStatementContext": self.assess_goto_statement,
            "FreeFileStatementContext": self.assess_freefile_statement,
            "AllocStatementContext": self.assess_alloc_statement,
            "RunStatementContext": self.assess_run_statement,
            "DsnEndStatementContext": self.assess_dsnend_statement,
            "CallStatementContext": self.assess_call_statement,
            "OpenfileStatementContext": self.assess_openfile_statement,
            "GetfileStatementContext": self.assess_getfile_statement,
            "ClosefileStatementContext": self.assess_closefile_statement,
            "SetStatementContext": self.assess_set_statement,
            "DeleteStatementContext": self.assess_delete_statement,
            "GlobalStatementContext": self.assess_global_statement,
            "AttributeStatementContext": self.assess_attribute_statement,
            "ListDmsStatementContext": self.assess_list_dms_statement,
            "ErrorStatementContext": self.assess_error_statement,
            "ReturnStatementContext": self.assess_return_statement,
            "DoWhileStatementContext": self.assess_dowhile_statement,
            "PutfileStatementContext": self.assess_putfile_statement,
            "ReaddvalStatementContext": self.assess_readdval_statement,
            "SelectStatementContext": self.assess_select_statement,
            "ExecStatementContext": self.assess_exec_statement,
            "OutputStatementContext": self.assess_output_statement,
            "CancelStatementContext": self.assess_cancel_statement,
            "KdsPrintStatementContext": self.assess_kdsprint_statement,
            "HrecoverStatementContext": self.assess_hrecover_statement,
            "JprintrStatementContext": self.assess_jprintr_statement,
            "HlistStatementContext": self.assess_hlist_statement
        }

    def assess_statement(self, ctx: ParserRuleContext):
        """Extract information of a statement context in PLI. Do not pass statement context of other languages.

        Args:
            ctx (ParserRuleContext): The statement context of PLI to be assessed.

        Returns:
            dict: The assessment result of the statement context.
        """
        # get the type of the statement
        if isinstance(ctx, ClistParser.StatementContext):
            ctx = ctx.getChild(0)

        statement_type = type(ctx).__name__
        if statement_type in self.func:
            f = self.func[statement_type]
            return f(ctx)

        print(f"Statement assessment not implemented: '{statement_type}'")
        return None
    def assess_label(self, ctx: ClistParser.LabelContext):
        metadata = self._extract_statement_metadata(ctx)
        label_name = ctx.labelName().getText()
        statement_ctx = ctx.statement()
        statement = None
        if statement_ctx:
            statement = self.assess_statement(statement_ctx)       
        # print("STATEMENT CONTEXT: ", statement)
        label = Label(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="Label",
            label_name=label_name,
            statement=statement

        )
        # self.labels.append(label)
        return label
    
    def visitLabel(self, ctx: ClistParser.LabelContext):
        try:
            label = self.assess_label(ctx)
            if label:
                self.labels.append(label)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess label: '{raw}'")
            print(f"Error: {e}")
        finally:
            return self.visitChildren(ctx)

    def _extract_statement_metadata(self, ctx: ParserRuleContext) -> dict:
        res = {}
        tag = type(ctx).__name__.replace("Context", "")
        res["tag"] = tag
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            ctx.parser, start_token.tokenIndex, stop_token.tokenIndex  # type: ignore
        )
        return res
    
    def _assess_nested_statements(self, ctx) -> List[dict]:
        if not hasattr(ctx, "statement"):
            print(
                f"Context does not have statement attribute: {type(ctx).__name__}"
            )
            return []

        if not isinstance(ctx.statement(), list):
            print(
                f"Context statement attribute is not a list: {type(ctx).__name__}"
            )
            return [] 

        statements = []

        for statement_ctx in ctx.statement():
            statement = self.assess_statement(statement_ctx)
            if statement:
                statements.append(statement)

        return statements
    
    def assess_control_statement(self, ctx: ClistParser.ControlStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        control_option_list = []

        control_options__list_ctx  =  ctx.controlOption()
        for option in control_options__list_ctx:            
            control_option_list.append(get_original_code_content(option.parser,option.start.tokenIndex, option.stop.tokenIndex))
        control_statement = ControlStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="ControlStatement",
            control_options=control_option_list
        )
        return control_statement

    def visitControlStatement(self, ctx: ClistParser.ControlStatementContext):
        try:
            control_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(control_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess control statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
    
    def assess_write_statement(self, ctx: ClistParser.WriteStatementContext):
        # print("ASSESS WRITE STATEMENT")
        metadata = self._extract_statement_metadata(ctx)
        # print(metadata)
        write_statement = WriteStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="WriteStatement",
            content=get_original_code_content(ctx.parser, ctx.start.tokenIndex,ctx.stop.tokenIndex).replace("WRITE ","").replace("WRITENR ","")
        )
        # print(write_statement)

        return write_statement
    
    def visitWriteStatement(self, ctx:ClistParser.WriteStatementContext):
        try:
            write_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(write_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess write statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
            
    def assess_writenr_statement(self, ctx: ClistParser.WriteNrStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        write_nr_statement = WriteNrStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="WriteNrStatement",
            content=get_original_code_content(ctx.parser, ctx.start.tokenIndex,ctx.stop.tokenIndex).replace("WRITENR ","")
        )
        return write_nr_statement
    def visitWriteNrStatement(self, ctx: ClistParser.WriteNrStatementContext):
        try:
            write_nr_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(write_nr_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess writenr statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)

    def assess_submit_statement(self, ctx: ClistParser.SubmitStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        dataset_name = None
        jcl_code = None
        if ctx.dataset_name():
            dataset_name = get_original_code_content(ctx.parser, ctx.dataset_name().start.tokenIndex, ctx.dataset_name().stop.tokenIndex)
        if ctx.jcl_code_submited():
            jcl_code = get_original_code_content(ctx.parser, ctx.jcl_code_submited().jcl_code().start.tokenIndex, ctx.jcl_code_submited().jcl_code().stop.tokenIndex)
        submit_statement = SubmitStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="SubmitStatement",
            dataset_name=dataset_name if dataset_name else "",
            jcl_code=jcl_code if jcl_code else ""
        )
        return submit_statement


    def visitSubmitStatement(self, ctx: ClistParser.SubmitStatementContext):
        try:
            submit_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(submit_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess submit statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
        
    def assess_isp_exec_statement(self, ctx: ClistParser.IspExecStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        service_name = ctx.getChild(1).parser.ruleNames[ctx.getChild(1).getRuleIndex()]
        # print(ctx.getText())

        if service_name == "vgetService":
            vget_service_ctx = ctx.vgetService()
            name_list = []
            vget_parameters = []
            name_list_ctx = vget_service_ctx.name_list()
            name_list_items = name_list_ctx.getChildren()
            if name_list_items:
                for item in name_list_items:
                    if item.getText() != "(" and item.getText() != ")":
                        name_list.append(item.getText())
            vget_parameter_ctx = vget_service_ctx.vgetParameter()
            if vget_parameter_ctx:
                vget_parameters = []
                for param in vget_parameter_ctx:
                    vget_parameters.append(get_original_code_content(ctx.parser, param.start.tokenIndex, param.stop.tokenIndex))

            return VgetService(
                raw=metadata["raw"],
                start_line=metadata["start_line"],
                stop_line=metadata["stop_line"],
                start_idx=metadata["start_idx"],
                stop_idx=metadata["stop_idx"],
                tag="VgetService",
                service_name=service_name,
                name_list=name_list,
                vget_parameter=vget_parameters
            )
        elif service_name == "ftopenService":
            if ctx.ftopenService().ftopenServiceParameter():
                return FTOpenSevice(
                    raw=metadata["raw"],
                    start_line=metadata["start_line"],
                    stop_line=metadata["stop_line"],
                    start_idx=metadata["start_idx"],
                    stop_idx=metadata["stop_idx"],
                    tag="ispExecStatement",
                    service_name=service_name,
                    open_name=ctx.ftopenService().ftopenServiceParameter().getText())
                
            else:
                return FTOpenSevice(
                    raw=metadata["raw"],
                    start_line=metadata["start_line"],
                    stop_line=metadata["stop_line"],
                    start_idx=metadata["start_idx"],
                    stop_idx=metadata["stop_idx"],
                    tag="ispExecStatement",
                    service_name=service_name,
                    open_name=None
                )
        if service_name == "ftinclService":
            skel_name = ctx.ftinclService().skel_name().getText()
            ftincl_parameters = []
            if ctx.ftinclService().ftinclParameter():
                ftincl_parameters_ctx = ctx.ftinclService().ftinclParameter()
                for param in ftincl_parameters_ctx:
                    ftincl_parameters.append(param.getText())

            return FTInclService(
                raw=metadata["raw"],
                start_line=metadata["start_line"],
                stop_line=metadata["stop_line"],
                start_idx=metadata["start_idx"],
                stop_idx=metadata["stop_idx"],
                tag="ispExecStatement",
                service_name=service_name,
                skel_name=skel_name,
                ftincl_parameters=ftincl_parameters
            )
        
        if service_name == "ftCloseService":
            close_name = None
            ftclose_library = None
            ftclose_parameters = None
            if ctx.ftCloseService().ftCloseName():
                close_name = ctx.ftCloseService().ftCloseName().getText()
            if ctx.ftCloseService().ftCloseLibrary():
                ftclose_library = ctx.ftCloseService().ftCloseLibrary().getText()
            if ctx.ftCloseService().ftCloseParameter():
                ftclose_parameters = []
                ftclose_parameters_ctx = ctx.ftCloseService().ftCloseParameter()
                for param in ftclose_parameters_ctx:
                    ftclose_parameters.append(param.getText())
            return FTCloseService(
                raw=metadata["raw"],
                start_line=metadata["start_line"],
                stop_line=metadata["stop_line"],
                start_idx=metadata["start_idx"],
                stop_idx=metadata["stop_idx"],
                tag="ispExecStatement",
                service_name=service_name,
                close_name=close_name if close_name else None,
                ftclose_library=ftclose_library if ftclose_library else None,
                ftclose_parameters=ftclose_parameters if ftclose_parameters else None
            )
        if service_name == "browseService":
            browse_service_ctx = ctx.browseService()
            dataset_list = []
            file_name = []
            data_id = ""
            first_child = browse_service_ctx.getChild(1)
            if isinstance(first_child, ClistParser.Clist_dataset_presentationContext):
                dataset_name_ctx = first_child.dataset_name()
                for ds in dataset_name_ctx:
                    dataset_list.append(ds.getText())
            elif isinstance(first_child, ClistParser.Clist_file_presentationContext):
                file_name_ctx = first_child.fileName()
                for file_ctx in file_name_ctx:
                    file_name.append(file_ctx.getText())
            elif isinstance(first_child, ClistParser.Clist_data_id_presentationContext):
                data_id = first_child.data_id().getText()
            browse_parameters = []
            browse_parameters_ctx = browse_service_ctx.browseServiceParameter()
            
            if browse_parameters_ctx:
                for param in browse_parameters_ctx:
                    browse_parameters.append(param.getText())
            return BrowseService(
                raw=metadata["raw"],
                start_line=metadata["start_line"],
                stop_line=metadata["stop_line"],
                start_idx=metadata["start_idx"],
                stop_idx=metadata["stop_idx"],
                tag="IspExecStatement",
                service_name=service_name,
                dataset_list=dataset_list if dataset_list else None,
                file_name=file_name if file_name else None,
                data_id=data_id if data_id else None,
                browse_parameters=browse_parameters if browse_parameters else None
            )
        if service_name == "editService":
            edit_service_ctx = ctx.editService()
            dataset_list = []
            file_name = []
            data_id = ""
            first_child = edit_service_ctx.getChild(1)
            if isinstance(first_child, ClistParser.Clist_dataset_presentationContext):
                dataset_name_ctx = first_child.dataset_name()
                for ds in dataset_name_ctx:
                    dataset_list.append(ds.getText())
            elif isinstance(first_child, ClistParser.Clist_file_presentationContext):
                file_name_ctx = first_child.fileName()
                for file_ctx in file_name_ctx:
                    file_name.append(file_ctx.getText())
            elif isinstance(first_child, ClistParser.Clist_data_id_presentationContext):
                data_id = first_child.data_id().getText()
            edit_parameters = []
            edit_parameters_ctx = edit_service_ctx.editServiceParameter()
            if edit_parameters_ctx:
                for param in edit_parameters_ctx:
                    edit_parameters.append(param.getText())
            return EditService(
                raw=metadata["raw"],
                start_line=metadata["start_line"],
                stop_line=metadata["stop_line"],
                start_idx=metadata["start_idx"],
                stop_idx=metadata["stop_idx"],
                tag="IspExecStatement",
                service_name=service_name,
                dataset_list=dataset_list if dataset_list else None,
                file_name=file_name if file_name else None,
                data_id=data_id if data_id else None,
                edit_parameters=edit_parameters if edit_parameters else None
            )
        if service_name == "fteraseService":
            member_name = ctx.fteraseService().member_name().getText()
            library_name = ctx.fteraseService().clist_library_presentation().library_name().getText() if ctx.fteraseService().clist_library_presentation() else ""
            return FtEraseService(
                raw=metadata["raw"],
                start_line=metadata["start_line"],
                stop_line=metadata["stop_line"],
                start_idx=metadata["start_idx"],
                stop_idx=metadata["stop_idx"],
                tag="IspExecStatement",
                service_name=service_name,
                member_name=member_name,
                library_name=library_name
            )
        if service_name == "vputService":
            vput_service_ctx = ctx.vputService()
            name_list = []
            vput_parameters = []
            name_list_ctx = vput_service_ctx.name_list()
            name_list_items = name_list_ctx.getChildren()
            if name_list_items:
                for item in name_list_items:
                    if item.getText() != "(" and item.getText() != ")":
                        name_list.append(item.getText())
            vput_parameter_ctx = vput_service_ctx.vputParameter()
            if vput_parameter_ctx:
                vput_parameters = []
                for param in vput_parameter_ctx:
                    vput_parameters.append(get_original_code_content(ctx.parser, param.start.tokenIndex, param.stop.tokenIndex))

            return VputService(
                raw=metadata["raw"],
                start_line=metadata["start_line"],
                stop_line=metadata["stop_line"],
                start_idx=metadata["start_idx"],
                stop_idx=metadata["stop_idx"],
                tag="VputService",
                service_name=service_name,
                name_list=name_list,
                vput_parameter=vput_parameters
            )
        if service_name == "lminitService":
            lminit_service_ctx = ctx.lminitService()
            data_id = lminit_service_ctx.clist_data_id_presentation().data_id().getText()
            dataset_list = []
            if lminit_service_ctx.clist_dataset_presentation():
                dataset_name_ctx = lminit_service_ctx.clist_dataset_presentation().dataset_name()
                for ds in dataset_name_ctx:
                    dataset_list.append(ds.getText())
            lminit_parameters = []
            lminit_parameters_ctx = lminit_service_ctx.lminitParameter()
            if lminit_parameters_ctx:
                for param in lminit_parameters_ctx:
                    lminit_parameters.append(param.getText())
            return LminitService(
                raw=metadata["raw"],
                start_line=metadata["start_line"],
                stop_line=metadata["stop_line"],
                start_idx=metadata["start_idx"],
                stop_idx=metadata["stop_idx"],
                tag="LminitService",
                service_name=service_name,
                dataset_list=dataset_list,
                data_id=data_id,
                parameters=lminit_parameters 
            )
        if service_name == "lmcopyService":
            copy_from = ctx.lmcopyService().fromId().value().getText()
            from_member = ctx.lmcopyService().fromMem().member_name().getText() if ctx.lmcopyService().fromMem() else ""
            copy_to = ctx.lmcopyService().toDataId().value().getText()
            to_member = ctx.lmcopyService().toMem().member_name().getText() if ctx.lmcopyService().toMem() else ""
            lmcopy_parameters = []
            lmcopy_parameters_ctx = ctx.lmcopyService().lmcopyParameter()
            if lmcopy_parameters_ctx:
                for param in lmcopy_parameters_ctx:
                    lmcopy_parameters.append(param.getText())
            return LmcopyService(

                raw=metadata["raw"],
                start_line=metadata["start_line"],
                stop_line=metadata["stop_line"],
                start_idx=metadata["start_idx"],
                stop_idx=metadata["stop_idx"],
                tag="LmcopyService",
                service_name=service_name,
                copy_from=copy_from,
                from_member=from_member,
                copy_to=copy_to,
                to_member=to_member,
                parameters=lmcopy_parameters
            )
        
        if service_name == "lmfreeService":
            lmfree_service_ctx = ctx.lmfreeService()
            data_id = lmfree_service_ctx.clist_data_id_presentation().data_id().getText()
            return LmfreeService(
                raw=metadata["raw"],
                start_line=metadata["start_line"],
                stop_line=metadata["stop_line"],
                start_idx=metadata["start_idx"],
                stop_idx=metadata["stop_idx"],
                tag="LmfreeService",
                service_name=service_name,
                data_id=data_id
            )
        
        if service_name == "tablebService":
            table_service_ctx = ctx.tablebService()
            table_service_name = table_service_ctx.tableServiceName().getText()
            table_name = table_service_ctx.table_name().getText()
            table_parameters = []
            table_parameters_ctx = table_service_ctx.tableParameter()
            if table_parameters_ctx:
                for param in table_parameters_ctx:
                    table_parameters.append(param.getText())
            return TableService(
                raw=metadata["raw"],
                start_line=metadata["start_line"],
                stop_line=metadata["stop_line"],
                start_idx=metadata["start_idx"],
                stop_idx=metadata["stop_idx"],
                tag="TableService",
                service_name=service_name,
                table_service_name=table_service_name,
                table_name=table_name,
                table_parameters=table_parameters if table_parameters else None
            )
        
        if service_name == "controlService":
            control_service_ctx = ctx.controlService()
            control_parameters = []
            control_parameters_ctx = control_service_ctx.controlServiceParameter()
            if control_parameters_ctx:
                for param in control_parameters_ctx:
                    control_parameters.append(param.getText())
            return ControlService(
                raw=metadata["raw"],
                start_line=metadata["start_line"],
                stop_line=metadata["stop_line"],
                start_idx=metadata["start_idx"],
                stop_idx=metadata["stop_idx"],
                tag="ControlService",
                service_name=service_name,
                parameters=control_parameters if control_parameters else None
            )
        
        if service_name == "logService":
            log_service_ctx = ctx.logService()
            message = log_service_ctx.message().getText()
            return LogService(
                raw=metadata["raw"],
                start_line=metadata["start_line"],
                stop_line=metadata["stop_line"],
                start_idx=metadata["start_idx"],
                stop_idx=metadata["stop_idx"],
                tag="LogService",
                service_name=service_name,
                message=message
            )
        
        if service_name == "displayService":
            display_service_ctx = ctx.displayService()
            display_parameters = []
            display_parameters_ctx = display_service_ctx.displayParameter()
            if display_parameters_ctx:
                for param in display_parameters_ctx:
                    display_parameters.append(param.getText())
            return DisplayService(
                raw=metadata["raw"],
                start_line=metadata["start_line"],
                stop_line=metadata["stop_line"],
                start_idx=metadata["start_idx"],
                stop_idx=metadata["stop_idx"],
                tag="DisplayService",
                service_name=service_name,
                parameters=display_parameters if display_parameters else None
            )
        
        if service_name == "addpopService":
            addpop_service_ctx = ctx.addpopService()
            addpop_parameters = []
            addpop_parameters_ctx = addpop_service_ctx.addpopServiceParameter()
            if addpop_parameters_ctx:
                for param in addpop_parameters_ctx:
                    addpop_parameters.append(param.getText())
            return AddpopService(
                raw=metadata["raw"],
                start_line=metadata["start_line"],
                stop_line=metadata["stop_line"],
                start_idx=metadata["start_idx"],
                stop_idx=metadata["stop_idx"],
                tag="AddpopService",
                service_name=service_name,
                parameters=addpop_parameters if addpop_parameters else None
            )
        
        isp_exec_statement = ISPExecStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="IspExecStatement",
            service_name=service_name
        )
        return isp_exec_statement

    
    def visitIspExecStatement(self, ctx: ClistParser.IspExecStatementContext):
        try:
            isp_exec_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(isp_exec_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess ispexec statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
    
    def assess_doend_statement(self, ctx: ClistParser.DoEndStatementContext):

        metadata = self._extract_statement_metadata(ctx)
        statements_ctx = ctx.statement()
        statements = []
        if statements_ctx:
            for statement_ctx in statements_ctx:

                statement = self.assess_statement(statement_ctx)
                # print(f"Statement: {statement}")
                if statement:
                    statements.append(statement)
        # print(f"Statements: {statements}")
        do_end_statement = DoEndStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="DoEndStatement",
            
            statements=statements
        )
        # print(f"DoEndStatement: {do_end_statement}")
        return do_end_statement
    
    def visitDoEndStatement(self, ctx: ClistParser.DoEndStatementContext):
        try:
            do_end_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(do_end_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess doend statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
        
    
    def assess_if_statement(self, ctx: ClistParser.IfStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        condition = ctx.getChild(1)
        if not isinstance(condition, ParserRuleContext):
            print(
                f"Condition is not a ParserRuleContext: {type(condition).__name__}"
            )
            return None
        condition = get_original_code_content(
            ctx.parser, condition.start.tokenIndex, condition.stop.tokenIndex
        )
        then_if_ctx = ctx.thenIf()
        then_if_statements = []
        then_if_statement = then_if_ctx.statement()
        then_if_statements = [self.assess_statement(then_if_statement)]
        else_if_ctx = ctx.elseIf() if ctx.elseIf() else None
        else_if_statements = []
        if else_if_ctx:
            else_if_statement = else_if_ctx.statement()
            else_if_statements = [self.assess_statement(else_if_statement)]
        if_statement = IfStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="IfStatement",
            condition=condition,
            then_statement=then_if_statements,
            else_statement=else_if_statements
        )
        return if_statement
    def visitIfStatement(self, ctx: ClistParser.IfStatementContext):
        try:
            if_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(if_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess if statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)

    def assess_exit_statement(self, ctx: ClistParser.ExitStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        exit_statement = Statement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="ExitStatement"
        )
        return exit_statement
    def visitExitStatement(self, ctx: ClistParser.ExitStatementContext):
        try:
            exit_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(exit_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess exit statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
        
    def assess_attn_statement(self, ctx: ClistParser.AttnStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        statements_ctx = ctx.statement()
        statements = []
        if statements_ctx:
            statement = self.assess_statement(statements_ctx)
            if statement:
                statements.append(statement)
        attn_statement = ATTNStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="ATTNStatement",
            statements=statements
        )
        return attn_statement
    
    def visitAttnStatement(self, ctx: ClistParser.AttnStatementContext):
        try:
            attn_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(attn_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess attn statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
    

    def assess_inline_statement(self, ctx: ClistParser.InlineStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        name_of_statement = get_original_code_content(
            ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex
        )
        inline_statement = InlineStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="InlineStatement",
            name_of_statement=name_of_statement.replace("%", "").strip()  
        )
        return inline_statement
    
    def visitInlineStatement(self, ctx: ClistParser.InlineStatementContext):
        try:
            inline_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(inline_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess inline statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
        
    def assess_read_statement(self, ctx: ClistParser.ReadStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        variables_list = []
        variables_list_ctx = ctx.variable()
        if variables_list_ctx:
            for variable in variables_list_ctx:
                variables_list.append(variable.getText())
        read_statement = ReadStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="ReadStatement",
            variables=variables_list
        )
        return read_statement
    def visitReadStatement(self, ctx: ClistParser.ReadStatementContext):
        try:
            read_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(read_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess read statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
    
    def assess_smcopy_statement(self, ctx: ClistParser.SmCopyStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        copy_from = ctx.smCopyFrom().fromDataset().dataset_name().getText()
        copy_to = ctx.smCopyTo().toDataset().dataset_name().getText()
        copy_options = []
        copy_options_ctx = ctx.smCopyOption()
        if copy_options_ctx:
            for option in copy_options_ctx:
                copy_options.append(option.getText())
        smcopy_statement = SmCopyStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="SmCopyStatement",
            copy_from=copy_from,
            copy_to=copy_to,
            copy_options=copy_options
        )
        return smcopy_statement
    
    def visitSmCopyStatement(self, ctx: ClistParser.SmCopyStatementContext):
        try:
            smcopy_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(smcopy_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess smcopy statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
        
    def assess_edit_statement(self, ctx: ClistParser.EditStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        dataset_name = ctx.dataset_name().getText()
        edit_options = []
        edit_options_ctx = ctx.editOption()
        if edit_options_ctx:
            for option in edit_options_ctx:
                edit_options.append(option.getText())
        edit_statement = EditStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="EditStatement",
            data_name=dataset_name,
            edit_options=edit_options
        )
        return edit_statement
    def visitEditStatement(self, ctx: ClistParser.EditStatementContext):
        try:
            edit_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(edit_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess edit statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
        
    def assess_insert_statement(self, ctx: ClistParser.InsertStatementContext):
        string_function = ctx.stringFuntion()
        metadata = self._extract_statement_metadata(ctx)

        return InsertStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="InsertStatement",
            string_to_insert=get_original_code_content(ctx.parser, string_function.start.tokenIndex, string_function.stop.tokenIndex)
        )

    def visitInsertStatement(self, ctx: ClistParser.InsertStatementContext):
        try:
            insert_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(insert_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess insert statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
        
    def assess_change_statement(self, ctx: ClistParser.ChangeStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        change_string = ctx.changeString().getText()
        original_string = ctx.orignalString().getText()
        change_parameters = []
        change_parameters_ctx = ctx.changeParameter()
        if change_parameters_ctx:
            for param in change_parameters_ctx:
                change_parameters.append(param.getText())
        change_statement = ChangeStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="ChangeStatement",
            change_string=change_string,
            original_string=original_string,
            change_parameters=change_parameters
        )
        return change_statement
    def visitChangeStatement(self, ctx: ClistParser.ChangeStatementContext):
        try:
            change_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(change_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess change statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
        

    def assess_find_statement(self, ctx: ClistParser.FindStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        find_string = ctx.findString().getText()
        find_statement = FindStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="FindStatement",
            find_string=find_string
        )
        return find_statement
    def visitFindStatement(self, ctx: ClistParser.FindStatementContext):
        try:
            find_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(find_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess find statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
        
    
    def assess_goto_statement(self, ctx: ClistParser.GotoStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        label_name = ctx.labelName().getText()
        goto_statement = GotoStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="GotoStatement",
            label=label_name
        )
        return goto_statement
    
    def visitGotoStatement(self, ctx: ClistParser.GotoStatementContext):
        try:
            goto_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(goto_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess goto statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
    
    def assess_freefile_statement(self, ctx: ClistParser.FreeFileStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        items = ctx.getChildren()
        list_of_file = []
        list_of_attribute = []
        list_of_datasets = []
        for item in items:
            if isinstance(item, ClistParser.Clist_file_presentationContext):
                list_of_file_ctx = item.fileName()
                if list_of_file_ctx:
                    for file_ctx in list_of_file_ctx:
                        list_of_file.append(file_ctx.getText())
            elif isinstance(item, ClistParser.Clist_attribute_list_presentationContext) or isinstance(item, ClistParser.Clist_attribute_presentationContext):
                list_of_attribute_ctx = item.attribute_name()
                # list_of_attribute = []
                if list_of_attribute_ctx:
                    for attribute_ctx in list_of_attribute_ctx:
                        list_of_attribute.append(attribute_ctx.getText())
            elif isinstance(item, ClistParser.Clist_dataset_presentationContext):
                list_of_dataset_ctx = item.dataset_name()
                # list_of_datasets = []
                if list_of_dataset_ctx:
                    for dataset_ctx in list_of_dataset_ctx:
                        list_of_datasets.append(dataset_ctx.getText())
                
        freefile_statement = FreeFileStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="FreeFileStatement",
            list_of_files=list_of_file,
            list_of_attributes=list_of_attribute,
            list_of_datasets=list_of_datasets
        )
        return freefile_statement
    
    def visitFreeFileStatement(self, ctx: ClistParser.FreeFileStatementContext):
        try:
            freefile_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(freefile_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess freefile statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
        
    def assess_alloc_statement(self, ctx: ClistParser.AllocStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        alloc_parameters_ctx = ctx.allocParameter()
        alloc_file_list = []
        alloc_dataset_list = []
        alloc_parameter_list = []
        
        for param_ctx in alloc_parameters_ctx:
            if param_ctx.clist_file_presentation():
                file_name_ctx = param_ctx.clist_file_presentation().fileName()
                if file_name_ctx:
                    for file_ctx in file_name_ctx:
                        alloc_file_list.append(file_ctx.getText())
            elif param_ctx.clist_dataset_presentation():
                dataset_name_ctx = param_ctx.clist_dataset_presentation().dataset_name()
                if dataset_name_ctx:
                    for dataset_ctx in dataset_name_ctx:
                        alloc_dataset_list.append(dataset_ctx.getText())
            elif param_ctx.otherAllocParameter():
                alloc_parameter_list.append(get_original_code_content(
                    ctx.parser, param_ctx.start.tokenIndex, param_ctx.stop.tokenIndex
                ))
        
        alloc_statement = AllocStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="AllocStatement",
            list_of_files=alloc_file_list,
            list_of_datasets=alloc_dataset_list,
            alloc_parameters=alloc_parameter_list
        )
        return alloc_statement
    
    def visitAllocStatement(self, ctx: ClistParser.AllocStatementContext):
        try:
            alloc_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(alloc_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess alloc statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
    
    def assess_run_statement(self, ctx: ClistParser.RunStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        program_name = ctx.clist_program_presentation().program_name().getText()
        plan_name = ctx.clist_plan_presentation().plan_name().getText()
        library_name = ctx.clist_library_presentation().library_name().getText()
        run_parameter = ctx.clist_params_presentation().params_name().getText() if ctx.clist_params_presentation() else ""

        run_statement = RunStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="RunStatement",
            program_name=program_name,
            plan_name=plan_name,
            library_name=library_name,
            run_parameter=run_parameter
        )
        return run_statement
    
    def visitRunStatement(self, ctx: ClistParser.RunStatementContext):
        try:
            run_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(run_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess run statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
        
    def assess_dsnend_statement(self, ctx: ClistParser.DsnEndStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        system_name = ctx.clist_system_presentation().system_name().getText()
        statement_ctx = ctx.statement()
        statements = []
        

        statements.append(self.assess_statement(statement_ctx))
        dnsend_statement = DSNEndStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="DnsendStatement",
            system_name=system_name,
            statements=statements
        )
        return dnsend_statement
    
    def visitDsnEndStatement(self, ctx: ClistParser.DsnEndStatementContext):
        try:
            dsnend_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(dsnend_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess dsnend statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
    
    def assess_call_statement(self, ctx: ClistParser.CallStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        dataset_name = ctx.dataset_name().getText()
        member_name = ctx.member_name().getText() if ctx.member_name() else ""
        call_options = []
        call_options_ctx = ctx.callOption()
        if call_options_ctx:
            for option in call_options_ctx:
                call_options.append(option.getText())
        call_statement = CallStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="CallStatement",
            dataset_name=dataset_name,
            member_name=member_name,
            call_options=call_options
        )
        return call_statement
    
    def visitCallStatement(self, ctx: ClistParser.CallStatementContext):
        try:
            call_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(call_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess call statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)

    def assess_openfile_statement(self, ctx: ClistParser.OpenfileStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        file_name = ctx.fileName().getText()
        openfile_option = ctx.openfileOption().getText() if ctx.openfileOption() else ""
        openfile_statement = OpenfileStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="OpenFileStatement",
            file_name=file_name,
            open_file_option=openfile_option
        )
        return openfile_statement
    def visitOpenfileStatement(self, ctx: ClistParser.OpenfileStatementContext):
        try:
            openfile_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(openfile_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess openfile statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)

    def assess_getfile_statement(self, ctx: ClistParser.GetfileStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        file_name = ctx.fileName().getText()
        getfile_statement = GetfileStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="GetFileStatement",
            file_name=file_name,
        )
        return getfile_statement
    def visitGetfileStatement(self, ctx: ClistParser.GetfileStatementContext):
        try:
            getfile_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(getfile_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess getfile statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
        
    
    def assess_closefile_statement(self, ctx: ClistParser.ClosefileStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        file_name = ctx.fileName().getText()
        closefile_statement = ClosefileStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="CloseFileStatement",
            file_name=file_name
        )
        return closefile_statement
    def visitClosefileStatement(self, ctx: ClistParser.ClosefileStatementContext):
        try:
            closefile_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(closefile_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess closefile statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
    
    def assess_set_statement(self, ctx: ClistParser.SetStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        variable_name = ctx.variable().getText()
        value = ctx.variableAssignment().getChild(1).getText() if ctx.variableAssignment().getChild(1) else None
        set_statement = SetStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="SetStatement",
            variable=variable_name,
            value=value
        )
        return set_statement
    
    def visitSetStatement(self, ctx: ClistParser.SetStatementContext):
        try:
            set_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(set_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess set statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
        

    def assess_delete_statement(self, ctx: ClistParser.DeleteStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        dataset_name = ctx.dataset_name().getText()
        delete_statement = DeleteStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="DeleteStatement",
            dataset_name=dataset_name
        )
        return delete_statement

    def visitDeleteStatement(self, ctx: ClistParser.DeleteStatementContext):
        try:
            delete_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(delete_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess delete statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
        
    def assess_global_statement(self, ctx: ClistParser.GlobalStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        variable_list = []
        variable_list_ctx = ctx.variable()
        for var in variable_list_ctx:
            variable_list.append(var.getText()) 
        global_statement = GlobalStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="GlobalStatement",
            variable=variable_list
        )
        return global_statement
    
    def visitGlobalStatement(self, ctx: ClistParser.GlobalStatementContext):
        try:
            global_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(global_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess global statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
    
    def assess_attribute_statement(self, ctx: ClistParser.AttributeStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        attribute_name_list = []
        attribute_name_ctx = ctx.attribute_name()
        if attribute_name_ctx:
            for name in attribute_name_ctx:
                attribute_name_list.append(name.getText()) 
        attribute_parameter_ctx = ctx.attributeStatementParameter()
        attribute_parameters_list = []
        if attribute_parameter_ctx:
            for param in attribute_parameter_ctx:
                attribute_parameters_list.append(get_original_code_content(ctx.parser, param.start.tokenIndex, param.stop.tokenIndex))
        attribute_statement = AttributeStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="AttributeStatement",
            attribute_name_list=attribute_name_list,           
            attribute_parameters=attribute_parameters_list
        )
        return attribute_statement
        
    def visitAttributeStatement(self, ctx: ClistParser.AttributeStatementContext):
        try:
            attribute_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(attribute_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess attribute statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)

    def assess_list_dms_statement(self, ctx: ClistParser.ListDmsStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        parameter_list = []
        parameter_list_ctx = ctx.listDmsParameter()
        if parameter_list_ctx:
            for param in parameter_list_ctx:
                parameter_list.append(get_original_code_content(ctx.parser, param.start.tokenIndex, param.stop.tokenIndex))

        list_dms_statement = ListDmsStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="ListDMSStatement",
            parameters=parameter_list
        )
        return list_dms_statement
    
    def assess_error_statement(self, ctx: ClistParser.ErrorStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        statement_ctx = ctx.statement()
        inner_statement = None
        if statement_ctx:
            inner_statement = self.assess_statement(statement_ctx)
            
        error_statement = ErrorStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="ErrorStatement",
            statement=inner_statement
        )
        return error_statement
        
    def visitErrorStatement(self, ctx: ClistParser.ErrorStatementContext):
        try:
            error_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(error_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess error statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
    
    def assess_return_statement(self, ctx: ClistParser.ReturnStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        
        return_statement = ReturnStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="ReturnStatement"
        )
        return return_statement
        
    def visitReturnStatement(self, ctx: ClistParser.ReturnStatementContext):
        try:
            return_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(return_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess return statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
    
    def assess_dowhile_statement(self, ctx: ClistParser.DoWhileStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        condition = get_original_code_content(
            ctx.parser, ctx.condition().start.tokenIndex, ctx.condition().stop.tokenIndex
        )
        
        statements = []
        labels = []
        statements_ctx = ctx.statement()
        if statements_ctx:
            for statement_ctx in statements_ctx:
                statement = self.assess_statement(statement_ctx)
                if statement:
                    statements.append(statement)
                
        # Check for labels
        label_ctx = ctx.label()
        if label_ctx:
            for label in label_ctx:
                labels.append(self.assess_label(label))
                
        dowhile_statement = DoWhileStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="DoWhileStatement",
            condition=condition,
            statements=statements,
            labels=labels
        )
        return dowhile_statement
        
    def visitDoWhileStatement(self, ctx: ClistParser.DoWhileStatementContext):
        try:
            dowhile_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(dowhile_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess dowhile statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)

    def assess_putfile_statement(self, ctx: ClistParser.PutfileStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        file_name = ctx.fileName().getText()
        
        putfile_statement = PutfileStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="PutfileStatement",
            file_name=file_name
        )
        return putfile_statement
        
    def visitPutfileStatement(self, ctx: ClistParser.PutfileStatementContext):
        try:
            putfile_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(putfile_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess putfile statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
        
    def assess_readdval_statement(self, ctx: ClistParser.ReaddvalStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        variable_list_ctx = ctx.variable()
        variable_name = []
        if variable_list_ctx:
            for var in variable_list_ctx:
                variable_name.append(var.getText())
        readd_value_statement = ReaddvalStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="ReaddValueStatement",
            variables=variable_name
        )
        return readd_value_statement
    
    def visitReaddvalStatement(self, ctx: ClistParser.ReaddvalStatementContext):
        try:
            readdval_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(readdval_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess readdval statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
            
    def assess_select_statement(self, ctx: ClistParser.SelectStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        test_variable = get_original_code_content(
            ctx.parser, ctx.testExpression().start.tokenIndex, ctx.testExpression().stop.tokenIndex
        )
        
        when_clauses = []
        when_select_contexts = ctx.whenSelect()
        for when_ctx in when_select_contexts:
            condition = get_original_code_content(
                ctx.parser, when_ctx.condition().start.tokenIndex, when_ctx.condition().stop.tokenIndex
            )
            statement = self.assess_statement(when_ctx.statement())
            when_clauses.append((condition, statement))
        
        otherwise_statement = None
        if ctx.otherwiseSelect():
            otherwise_statement = self.assess_statement(ctx.otherwiseSelect().statement())
            
        select_statement = SelectStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="SelectStatement",
            test_variable=test_variable,
            when_clauses=when_clauses,
            otherwise_statement=otherwise_statement
        )
        return select_statement
    
    def visitSelectStatement(self, ctx: ClistParser.SelectStatementContext):
        try:
            select_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(select_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess select statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
    
    def assess_exec_statement(self, ctx: ClistParser.ExecStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        dataset_names = []
        
        # Extract dataset names from context
        if ctx.dataset_name():
            dataset_names.append(get_original_code_content(
                ctx.parser, ctx.dataset_name().start.tokenIndex, ctx.dataset_name().stop.tokenIndex
            ))
        elif ctx.clist_dataset_presentation():
            for dataset_name_ctx in ctx.clist_dataset_presentation().dataset_name():
                dataset_names.append(get_original_code_content(
                    ctx.parser, dataset_name_ctx.start.tokenIndex, dataset_name_ctx.stop.tokenIndex
                ))
                
        exec_statement = ExecStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="ExecStatement",
            dataset_name=dataset_names
        )
        return exec_statement
    
    def visitExecStatement(self, ctx: ClistParser.ExecStatementContext):
        try:
            exec_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(exec_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess exec statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
    
    def assess_output_statement(self, ctx: ClistParser.OutputStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        
        job_name = None
        job_id = None
        parameters = []
        
        # Extract job parameters if available
        job_parameter_contexts = ctx.job_parameter()
        if job_parameter_contexts:
            for job_param_ctx in job_parameter_contexts:
                job_name = get_original_code_content(
                    ctx.parser, job_param_ctx.job_name().start.tokenIndex, job_param_ctx.job_name().stop.tokenIndex
                )
                job_id = get_original_code_content(
                    ctx.parser, job_param_ctx.job_id().start.tokenIndex, job_param_ctx.job_id().stop.tokenIndex
                )
        
        # Extract other parameters
        output_param_contexts = ctx.outputParameter()
        if output_param_contexts:
            for param_ctx in output_param_contexts:
                parameters.append(get_original_code_content(
                    ctx.parser, param_ctx.start.tokenIndex, param_ctx.stop.tokenIndex
                ))
                
        output_statement = OutputStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="OutputStatement",
            job_name=job_name,
            job_id=job_id,
            parameters=parameters if parameters else None
        )
        return output_statement
    
    def visitOutputStatement(self, ctx: ClistParser.OutputStatementContext):
        try:
            output_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(output_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess output statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
    
    def assess_cancel_statement(self, ctx: ClistParser.CancelStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        
        job_name = None
        job_id = None
        
        # Extract job parameters if available
        job_parameter_contexts = ctx.job_parameter()
        if job_parameter_contexts:
            for job_param_ctx in job_parameter_contexts:
                job_name = get_original_code_content(
                    ctx.parser, job_param_ctx.job_name().start.tokenIndex, job_param_ctx.job_name().stop.tokenIndex
                )
                job_id = get_original_code_content(
                    ctx.parser, job_param_ctx.job_id().start.tokenIndex, job_param_ctx.job_id().stop.tokenIndex
                )
                
        cancel_statement = CancelStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="CancelStatement",
            job_name=job_name,
            job_id=job_id
        )
        return cancel_statement
    
    def visitCancelStatement(self, ctx: ClistParser.CancelStatementContext):
        try:
            cancel_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(cancel_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess cancel statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
    
    def assess_kdsprint_statement(self, ctx: ClistParser.KdsPrintStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        
        parameters = []
        file_name = []
        
        # Extract parameters
        param_contexts = ctx.kdsPrintParamater()
        if param_contexts:
            for param_ctx in param_contexts:
                if isinstance(param_ctx, ClistParser.Clist_file_presentationContext):
                    file_name_ctx = param_ctx.fileName()
                    for f_ctx in file_name_ctx:
                        file_name.append(get_original_code_content(
                            ctx.parser, f_ctx.start.tokenIndex, f_ctx.stop.tokenIndex
                        ))
                else:
                    parameters.append(get_original_code_content(
                        ctx.parser, param_ctx.start.tokenIndex, param_ctx.stop.tokenIndex
                    ))
                
        kdsprint_statement = KdsPrintStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="KdsPrintStatement",
            parameters=parameters if parameters else None,
            file_name=file_name if file_name else None
        )
        return kdsprint_statement
    
    def visitKdsPrintStatement(self, ctx: ClistParser.KdsPrintStatementContext):
        try:
            kdsprint_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(kdsprint_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess kdsprint statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
    
    def assess_hrecover_statement(self, ctx: ClistParser.HrecoverStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        dataset_name = get_original_code_content(
            ctx.parser, ctx.dataset_name().start.tokenIndex, ctx.dataset_name().stop.tokenIndex
        )
        
        parameters = []
        param_contexts = ctx.hrecoverParameter()
        if param_contexts:
            for param_ctx in param_contexts:
                parameters.append(get_original_code_content(
                    ctx.parser, param_ctx.start.tokenIndex, param_ctx.stop.tokenIndex
                ))
                
        hrecover_statement = HrecoverStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="HrecoverStatement",
            dataset_name=dataset_name,
            parameters=parameters if parameters else None
        )
        return hrecover_statement
    
    def visitHrecoverStatement(self, ctx: ClistParser.HrecoverStatementContext):
        try:
            hrecover_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(hrecover_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess hrecover statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
    
    def assess_jprintr_statement(self, ctx: ClistParser.JprintrStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        
        content = get_original_code_content(
            ctx.parser, ctx.jprintContent().start.tokenIndex, ctx.jprintContent().stop.tokenIndex
        )
        
        parameters = []
        param_contexts = ctx.jprintParameter()
        if param_contexts:
            for param_ctx in param_contexts:
                parameters.append(get_original_code_content(
                    ctx.parser, param_ctx.start.tokenIndex, param_ctx.stop.tokenIndex
                ))
                
        jprintr_statement = JprintrStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="JprintrStatement",
            content=content,
            parameters=parameters if parameters else None
        )
        return jprintr_statement
    
    def visitJprintrStatement(self, ctx: ClistParser.JprintrStatementContext):
        try:
            jprintr_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(jprintr_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess jprintr statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
    
    def assess_hlist_statement(self, ctx: ClistParser.HlistStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        
        parameters = []
        param_contexts = ctx.hlistParameter()
        if param_contexts:
            for param_ctx in param_contexts:
                parameters.append(get_original_code_content(
                    ctx.parser, param_ctx.start.tokenIndex, param_ctx.stop.tokenIndex
                ))
                
        hlist_statement = HlistStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="HlistStatement",
            parameters=parameters if parameters else None
        )
        return hlist_statement
    
    def visitHlistStatement(self, ctx: ClistParser.HlistStatementContext):
        try:
            hlist_statement = self.assess_statement(ctx)
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, ClistParser.ProcedureContext):
                self.statements.append(hlist_statement)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            print(f"Failed to assess hlist statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)

