from typing import List
from antlr4 import ParserRuleContext

from parsers.grammar.pli.PLIVisitor import PLIVisitor
from parsers.grammar.pli.PLIParser import PLIParser
from parsers.grammar.pli.pli_schemas import CallStatement, Statement
from parsers.grammar.utils import get_original_code_content

class PLIVisitorImp(PLIVisitor):
    def __init__(self):
        self.statements: List[Statement] = []
        self.func = {
            "CallstmtContext": self.assess_call_statement,
        }
        
    def assess_statement(self, ctx: ParserRuleContext):
        """Extract information of a statement context in PLI. Do not pass statement context of other languages.

        Args:
            ctx (ParserRuleContext): The statement context of PLI to be assessed.

        Returns:
            dict: The assessment result of the statement context.
        """
        # get the type of the statement
        if isinstance(ctx, PLIParser.StmtContext):
            ctx = ctx.getChild(0)

        statement_type = type(ctx).__name__
        if statement_type in self.func:
            f = self.func[statement_type]
            return f(ctx)

        logger.warning(f"Statement assessment not implemented: '{statement_type}'")
        return None
        
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
            logger.exception(
                f"Context does not have statement attribute: {type(ctx).__name__}"
            )
            return []

        if not isinstance(ctx.statement(), list):
            logger.warning(
                f"Context statement attribute is not a list: {type(ctx).__name__}"
            )
            return []

        statements = []

        for statement_ctx in ctx.statement():
            statement = self.assess_statement(statement_ctx)
            if statement:
                statements.append(statement)

        return statements

    def assess_call_statement(self, ctx:PLIParser.CallstmtContext):
        metadata = self._extract_statement_metadata(ctx)
        
        call_option_list_ctx = ctx.calloptionlist()
        call_option_list = []
        
        if call_option_list_ctx:
            for child in call_option_list_ctx.getChildren():
                
                if isinstance(child, PLIParser.VarnamerefContext):
                    call_option = get_original_code_content(ctx.parser, child.start.tokenIndex, child.stop.tokenIndex)
                    call_option_list.append(call_option)
                
                elif isinstance(child, PLIParser.CallmultitaskoptionlistContext):
                    for grand_child in child.getChildren():
                        call_option = get_original_code_content(ctx.parser, grand_child.start.tokenIndex, grand_child.stop.tokenIndex)
                        call_option_list.append(call_option)
        
        file_name = None
        if ctx.filename():
            file_name = get_original_code_content(ctx.parser, ctx.filename().start.tokenIndex, ctx.filename().stop.tokenIndex)
        
        callstmt = CallStatement(
            raw=metadata["raw"],
            start_line=metadata["start_line"],
            stop_line=metadata["stop_line"],
            start_idx=metadata["start_idx"],
            stop_idx=metadata["stop_idx"],
            tag="CallStatement",
            call_option_list=call_option_list,
            file_name=file_name
        )
        return callstmt
        
    
    def visitCallstmt(self, ctx:PLIParser.CallstmtContext):
        try:
            callstmt = self.assess_statement(ctx)
            if callstmt:
                self.statements.append(callstmt)
        except Exception as e:
            raw = get_original_code_content(ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)
            logger.exception(f"Failed to assess call statement: '{raw}'")
        finally:
            return self.visitChildren(ctx)