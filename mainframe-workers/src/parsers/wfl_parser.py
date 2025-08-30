from typing import Dict, Optional
from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener
from loguru import logger
import re

from assessor.assessor import count_line
from parsers.grammar.wfl.WFLLexer import WFLLexer
from parsers.grammar.wfl.WFLParser import WFLParser
from parsers.grammar.wfl.WFLVisitorImp import WFLVisitorImp
from schema.reverse_engineering import ReverseEngineeringStatus, ReverseEngineeringUpdate

class QuietErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        pass
    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass
    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass
    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass

def preprocess_wfl(code: str) -> str:
    # Remove 8-digit numbers
    pattern = re.compile(r'\b\d{8}\b')
    code = pattern.sub('', code)
    
    # Right strip and remove empty lines
    return "\n".join([line.rstrip() for line in code.splitlines() if line.strip()])

def parse_wfl_antlr(code: str) -> Optional[Dict]:
    try:
        # Setup lexer with custom error listener
        stream = InputStream(code)
        lexer = WFLLexer(stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(QuietErrorListener())
        
        # Setup parser
        token_stream = CommonTokenStream(lexer)
        parser = WFLParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(QuietErrorListener())
        parser.buildParseTrees = True
        
        # Parse and visit
        tree = parser.startRule()
        visitor = WFLVisitorImp()
        visitor.visit(tree)
        
        return {
            "job_name": visitor.job_name,
            "statements": [stmt.dict() for stmt in visitor.statements],
            "subroutines": [sub.dict() for sub in visitor.subroutines],
            "line_of_code": count_line(code, "WFL")[0]
        }
        
    except Exception as e:
        logger.error(f"Error parsing WFL: {str(e)}")
        return None

def parse_wfl(repository_id: str, content: str) -> ReverseEngineeringUpdate:
    try:
        processed_code = preprocess_wfl(content)
        parsed_data = parse_wfl_antlr(processed_code)
        
        if not parsed_data:
            raise Exception("Failed to parse WFL")
            
        return ReverseEngineeringUpdate(
            name=parsed_data.get("job_name"),
            output=parsed_data,
            type="WFL",
            status=ReverseEngineeringStatus.PARSED,
        )
        
    except Exception as e:
        logger.error(f"Error in WFL parser: {str(e)}")
        return ReverseEngineeringUpdate(
            type="WFL",
            status=ReverseEngineeringStatus.PARSED_ERROR,
        )
