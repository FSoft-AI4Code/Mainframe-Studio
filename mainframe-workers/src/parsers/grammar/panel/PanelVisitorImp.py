from typing import List, Dict, Any, Optional
import traceback
from loguru import logger

from antlr4 import ParserRuleContext
from antlr4.tree.Tree import TerminalNodeImpl

from parsers.grammar.panel.PanelParser import PanelParser
from parsers.grammar.panel.PanelVisitor import PanelVisitor

from parsers.grammar.panel.panel_schemas import (
    Section,
    AttributeSection,
    BodySection,
    InitSection,
    ProcedureSection,
    ModelSection,
    ReInitSection,
    Statement,
    AssignStatement,
    VgetStatement,
    VputStatement,
    RefreshStatement,
    IfStatement,
    VerStatement,
    AttributeComponent,
    TransFunction,
    TransParam
)

from parsers.grammar.utils import get_original_code_content, get_original_code_content_without_hidden

class PanelVisitorImp(PanelVisitor):
    
    def __init__(self, body_text):
        self.sections = []
        self.body_text = body_text
        self.statements = []
        # Dictionary mapping statement context names to their assessment functions
        self.statement_func = {
            "AssignStatementContext": self.assess_assign_statement,
            "VgetStatementContext": self.assess_vget_statement, 
            "VputStatementContext": self.assess_vput_statement,
            "RefreshStatementContext": self.assess_refresh_statement,
            "IfStatementContext": self.assess_if_statement,
            "VerStatementContext": self.assess_ver_statement
        }
        # Dictionary mapping section context names to their assessment functions
        self.section_func = {
            "AttributeSectionContext": self.assess_attribute_section,
            "BodySectionContext": self.assess_body_section,
            "InitSectionContext": self.assess_init_section,
            "ProcSectionContext": self.assess_proc_section,
            "ModelSectionContext": self.assess_model_section,
            "ReinitSectionContext": self.assess_reinit_section,
            "EndSectionContext": self.assess_end_section
        }
    
    def assess_statement(self, ctx: ParserRuleContext):
        """Assess a statement context and return the appropriate statement object"""
        statement_type = type(ctx).__name__
        if statement_type in self.statement_func:
            f = self.statement_func[statement_type]
            return f(ctx)
        
        logger.warning(f"Statement assessment not implemented: '{statement_type}'")
        return None
    
    def assess_section(self, ctx: ParserRuleContext):
        """Assess a section context and return the appropriate section object"""
        section_type = type(ctx).__name__
        if section_type in self.section_func:
            f = self.section_func[section_type]
            return f(ctx)
        
        logger.warning(f"Section assessment not implemented: '{section_type}'")
        return None
    
    def _extract_statement_metadata(self, ctx: ParserRuleContext) -> dict:
        """Extract common metadata for statements"""
        res = {}
        tag = type(ctx).__name__.replace("Context", "")
        res["tag"] = tag
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content_without_hidden(
            ctx.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        return res
    
    def _assess_nested_statements(self, ctx) -> List[Statement]:
        """Assess nested statements in a context"""
        if not hasattr(ctx, "statement"):
            logger.warning(f"Context does not have statement attribute: {type(ctx).__name__}")
            return []
            
        statements = []
        
        # Handle both single statement and list of statements
        statement_contexts = ctx.statement()
        if not isinstance(statement_contexts, list):
            statement_contexts = [statement_contexts]
            
        for statement_ctx in statement_contexts:
            if statement_ctx.getChildCount() > 0:
                statement_child = statement_ctx.getChild(0)
                statement = self.assess_statement(statement_child)
                if statement:
                    statements.append(statement)
                    # Also add to global statements list
                    self.statements.append(statement)
                    
        return statements
    
    # Assessment methods for statements
    def _trans_func_convert_helper(self,trans_return):
        if "CMD" in trans_return:
            return "CMD", trans_return.replace("CMD(","").replace(")","")
        elif "PANEL" in trans_return:
            return "PANEL", trans_return.replace("PANEL(","").replace(")","")
        elif "EXIT" in trans_return:
            return "EXIT", trans_return
        elif "?" in trans_return:
            return "HELP", trans_return

    def assess_assign_statement(self, ctx: PanelParser.AssignStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        variable = ctx.variable().getText()
        value = ""
        if ctx.assignPart().value():
            value_ctx = ctx.assignPart().value()
            if value_ctx.panelFunction():
                if value_ctx.panelFunction().transFunc():
                    trans_func_ctx = value_ctx.panelFunction().transFunc()
                    trans_params_list = []
                    trans_param_list_ctx = trans_func_ctx.transParam()
                    for param_ctx in trans_param_list_ctx:
                        trans_return_type, trans_return_value = self._trans_func_convert_helper(param_ctx.transReturn().getText())
                        trans_params_list.append(TransParam(
                            trans_variable=param_ctx.transVariable().getText(),
                            trans_return_type=trans_return_type,
                            trans_return_value=trans_return_value
                        ))
                    value = TransFunction(
                        trans_params=trans_params_list,
                        variable_to_trans=trans_func_ctx.variable_to_trans().getText()
                    )
            else:
                value = get_original_code_content_without_hidden(
                    ctx.parser, value_ctx.start.tokenIndex, value_ctx.stop.tokenIndex
                )
        
        statement = AssignStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag=metadata["tag"],
            variable=variable,
            value=value
        )
        return statement
    
    def assess_vget_statement(self, ctx: PanelParser.VgetStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        name_list = []
        name_list_ctx = ctx.name_list()
        
        if name_list_ctx.IDENTIFIER():
            name_list.append(name_list_ctx.IDENTIFIER().getText())
        elif name_list_ctx.name_list_item():
            for item in name_list_ctx.name_list_item():
                name_list.append(item.getText())
        
        vget_parameters = []
        for param in ctx.vgetParameter():
            vget_parameters.append(param.getText())
        
        statement = VgetStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag=metadata["tag"],
            name_list=name_list,
            vget_parameters=vget_parameters
        )
        return statement
    
    def assess_vput_statement(self, ctx: PanelParser.VputStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        name_list = []
        name_list_ctx = ctx.name_list()
        
        if name_list_ctx.IDENTIFIER():
            name_list.append(name_list_ctx.IDENTIFIER().getText())
        elif name_list_ctx.name_list_item():
            for item in name_list_ctx.name_list_item():
                name_list.append(item.getText())
        
        vput_parameters = []
        for param in ctx.vputParameter():
            vput_parameters.append(param.getText())
        
        statement = VputStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag=metadata["tag"],
            name_list=name_list,
            vput_parameters=vput_parameters
        )
        return statement
    
    def assess_refresh_statement(self, ctx: PanelParser.RefreshStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        variable = ctx.variable().getText()
        
        statement = RefreshStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag=metadata["tag"],
            variable=variable
        )
        return statement
    
    def assess_if_statement(self, ctx: PanelParser.IfStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        condition_ctx = ctx.condition()
        condition = get_original_code_content_without_hidden(
            ctx.parser, condition_ctx.start.tokenIndex, condition_ctx.stop.tokenIndex
        )
        
        # Special handling for then and else statements
        then_statements = []
        then_ctx = ctx.thenIf()
        
        if then_ctx.statement():
            statement_ctx = then_ctx.statement()
            if statement_ctx.getChildCount() > 0:
                statement_child = statement_ctx.getChild(0)
                statement = self.assess_statement(statement_child)
                if statement:
                    then_statements.append(statement)
                    self.statements.append(statement)
        
        elif then_ctx.verStatement():
            for ver_stmt in then_ctx.verStatement():
                statement = self.assess_ver_statement(ver_stmt)
                if statement:
                    then_statements.append(statement)
                    self.statements.append(statement)
        
        else_statements = []
        if ctx.elseIf():
            else_ctx = ctx.elseIf()
            if else_ctx.statement():
                statement_ctx = else_ctx.statement()
                if statement_ctx.getChildCount() > 0:
                    statement_child = statement_ctx.getChild(0)
                    statement = self.assess_statement(statement_child)
                    if statement:
                        else_statements.append(statement)
                        self.statements.append(statement)
        
        statement = IfStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag=metadata["tag"],
            condition=condition,
            then_statements=then_statements,
            else_statements=else_statements if else_statements else None
        )
        return statement
    
    def assess_ver_statement(self, ctx: PanelParser.VerStatementContext):
        metadata = self._extract_statement_metadata(ctx)
        variable = ctx.variable().getText()
        
        criteria = []
        for ver_criteria in ctx.verCriteria():
            criteria.append(get_original_code_content_without_hidden(
                ctx.parser, ver_criteria.start.tokenIndex, ver_criteria.stop.tokenIndex
            ))
        
        message = None
        if ctx.verMsg():
            message = ctx.verMsg().value().getText()
        
        statement = VerStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag=metadata["tag"],
            variable=variable,
            criteria=criteria,
            message=message
        )
        return statement
    
    # Assessment methods for sections
    
    def assess_attribute_section(self, ctx: PanelParser.AttributeSectionContext):
        metadata = self._extract_statement_metadata(ctx)
        
        default_parameter = None
        if ctx.defaultParam():
            default_param_ctx = ctx.defaultParam()
            default_parameter = get_original_code_content_without_hidden(
                ctx.parser, default_param_ctx.start.tokenIndex, default_param_ctx.stop.tokenIndex
            )
        
        format_parameter = None
        if ctx.formatParam():
            format_param_ctx = ctx.formatParam()
            format_parameter = get_original_code_content_without_hidden(
                ctx.parser, format_param_ctx.start.tokenIndex, format_param_ctx.stop.tokenIndex
            )
        
        attribute_components = []
        for attr_comp_ctx in ctx.attributeComponent():
            attr_char = attr_comp_ctx.attrChar().getText()
            attr_params = []
            
            for attr_param_ctx in attr_comp_ctx.attrParameter():
                attr_param = get_original_code_content_without_hidden(
                    ctx.parser, attr_param_ctx.start.tokenIndex, attr_param_ctx.stop.tokenIndex
                )
                attr_params.append(attr_param)
            
            attribute_components.append(AttributeComponent(
                attribute_character=attr_char,
                attribute_parameters=attr_params
            ))
        
        attr_section = AttributeSection(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag=metadata["tag"],
            default_parameter=default_parameter,
            format_parameter=format_parameter,
            attribute_components=attribute_components
        )
        
        return attr_section
    
    def assess_body_section(self, ctx: PanelParser.BodySectionContext):
        metadata = self._extract_statement_metadata(ctx)
        
        body_parameters = []
        for param_ctx in ctx.bodyParam():
            param = get_original_code_content_without_hidden(
                ctx.parser, param_ctx.start.tokenIndex, param_ctx.stop.tokenIndex
            )
            body_parameters.append(param)
        
        body_section = BodySection(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag=metadata["tag"],
            body_parameters=body_parameters,
            body_text=self.body_text
        )
        
        return body_section
    
    def assess_init_section(self, ctx: PanelParser.InitSectionContext):
        metadata = self._extract_statement_metadata(ctx)
        
        # Use the utility method to assess nested statements
        statements = self._assess_nested_statements(ctx)
        
        init_section = InitSection(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag=metadata["tag"],
            statements=statements
        )
        
        return init_section
    
    def assess_proc_section(self, ctx: PanelParser.ProcSectionContext):
        metadata = self._extract_statement_metadata(ctx)
        
        # Use the utility method to assess nested statements
        statements = self._assess_nested_statements(ctx)
        
        proc_section = ProcedureSection(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag=metadata["tag"],
            statements=statements
        )
        
        return proc_section
    
    def assess_model_section(self, ctx: PanelParser.ModelSectionContext):
        metadata = self._extract_statement_metadata(ctx)
        
        model_parameters = []
        for param_ctx in ctx.modelParam():
            model_parameters.append(param_ctx.getText())
        
        models = []
        for model_ctx in ctx.model():
            model_metadata = self._extract_statement_metadata(model_ctx)
            model = Statement(
                raw=model_metadata["raw"],
                start_line=model_metadata["start_line"],
                stop_line=model_metadata["stop_line"],
                start_idx=model_metadata["start_idx"],
                stop_idx=model_metadata["stop_idx"],
                tag="Model"
            )
            models.append(model)
            # Add models to global statements list as well
            self.statements.append(model)
        
        model_section = ModelSection(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag=metadata["tag"],
            model_parameters=model_parameters,
            models=models
        )
        
        return model_section
    
    def assess_reinit_section(self, ctx: PanelParser.ReinitSectionContext):
        metadata = self._extract_statement_metadata(ctx)
        
        # Use the utility method to assess nested statements
        statements = self._assess_nested_statements(ctx)
        
        reinit_section = ReInitSection(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag=metadata["tag"],
            statements=statements
        )
        
        return reinit_section
    
    def assess_end_section(self, ctx: PanelParser.EndSectionContext):
        metadata = self._extract_statement_metadata(ctx)
        
        end_section = Section(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag=metadata["tag"],
        )
        
        return end_section
    
    # Visit methods for statements
    
    def visitAssignStatement(self, ctx: PanelParser.AssignStatementContext):
        try:
            assign_statement = self.assess_statement(ctx)
            if assign_statement:
                self.statements.append(assign_statement)
        except Exception:
            raw = get_original_code_content_without_hidden(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            logger.exception(f"Failed to assess assign statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
    
    def visitVgetStatement(self, ctx: PanelParser.VgetStatementContext):
        try:
            vget_statement = self.assess_statement(ctx)
            if vget_statement:
                self.statements.append(vget_statement)
        except Exception:
            raw = get_original_code_content_without_hidden(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            logger.exception(f"Failed to assess vget statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
    
    def visitVputStatement(self, ctx: PanelParser.VputStatementContext):
        try:
            vput_statement = self.assess_statement(ctx)
            if vput_statement:
                self.statements.append(vput_statement)
        except Exception:
            raw = get_original_code_content_without_hidden(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            logger.exception(f"Failed to assess vput statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
    
    def visitRefreshStatement(self, ctx: PanelParser.RefreshStatementContext):
        try:
            refresh_statement = self.assess_statement(ctx)
            if refresh_statement:
                self.statements.append(refresh_statement)
        except Exception:
            raw = get_original_code_content_without_hidden(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            logger.exception(f"Failed to assess refresh statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
    
    def visitIfStatement(self, ctx: PanelParser.IfStatementContext):
        try:
            if_statement = self.assess_statement(ctx)
            if if_statement:
                self.statements.append(if_statement)
        except Exception:
            raw = get_original_code_content_without_hidden(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            logger.exception(f"Failed to assess if statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
    
    def visitVerStatement(self, ctx: PanelParser.VerStatementContext):
        try:
            ver_statement = self.assess_statement(ctx)
            if ver_statement:
                self.statements.append(ver_statement)
        except Exception:
            raw = get_original_code_content_without_hidden(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            logger.exception(f"Failed to assess ver statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)
    
    # Visit methods for sections
    
    def visitAttributeSection(self, ctx: PanelParser.AttributeSectionContext):
        try:
            attribute_section = self.assess_section(ctx)
            if attribute_section:
                self.sections.append(attribute_section)
        except Exception:
            raw = get_original_code_content_without_hidden(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            logger.exception(f"Failed to assess attribute section: '{raw}'")
        finally:
            return self.visitChildren(ctx)
    
    def visitBodySection(self, ctx: PanelParser.BodySectionContext):
        try:
            body_section = self.assess_section(ctx)
            if body_section:
                self.sections.append(body_section)
        except Exception:
            raw = get_original_code_content_without_hidden(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            logger.exception(f"Failed to assess body section: '{raw}'")
        finally:
            return self.visitChildren(ctx)
    
    def visitInitSection(self, ctx: PanelParser.InitSectionContext):
        try:
            init_section = self.assess_section(ctx)
            if init_section:
                self.sections.append(init_section)
        except Exception:
            raw = get_original_code_content_without_hidden(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            logger.exception(f"Failed to assess init section: '{raw}'")
        finally:
            return self.visitChildren(ctx)
    
    def visitProcSection(self, ctx: PanelParser.ProcSectionContext):
        try:
            proc_section = self.assess_section(ctx)
            if proc_section:
                self.sections.append(proc_section)
        except Exception:
            raw = get_original_code_content_without_hidden(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            logger.exception(f"Failed to assess proc section: '{raw}'")
        finally:
            return self.visitChildren(ctx)
    
    def visitModelSection(self, ctx: PanelParser.ModelSectionContext):
        try:
            model_section = self.assess_section(ctx)
            if model_section:
                self.sections.append(model_section)
        except Exception:
            raw = get_original_code_content_without_hidden(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            logger.exception(f"Failed to assess model section: '{raw}'")
        finally:
            return self.visitChildren(ctx)
    
    def visitReinitSection(self, ctx: PanelParser.ReinitSectionContext):
        try:
            reinit_section = self.assess_section(ctx)
            if reinit_section:
                self.sections.append(reinit_section)
        except Exception:
            raw = get_original_code_content_without_hidden(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            logger.exception(f"Failed to assess reinit section: '{raw}'")
        finally:
            return self.visitChildren(ctx)
    
    def visitEndSection(self, ctx: PanelParser.EndSectionContext):
        try:
            end_section = self.assess_section(ctx)
            if end_section:
                self.sections.append(end_section)
        except Exception:
            raw = get_original_code_content_without_hidden(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            logger.exception(f"Failed to assess end section: '{raw}'")
        finally:
            return self.visitChildren(ctx)