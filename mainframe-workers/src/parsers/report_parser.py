import re 
from typing import Any, Dict
from antlr4 import CommonTokenStream, InputStream
from loguru import logger

from schema.reverse_engineering import (
    ReverseEngineeringStatus,
    ReverseEngineeringUpdate,
)

from parsers.grammar.ogl.OGLLexer import OGLLexer
from parsers.grammar.ogl.OGLParser import OGLParser
from parsers.grammar.ogl.OGLVisitorImp import OGLVisitorImp
from classifier.constants import FileType


# This function inherits from the repository parser
def preprocess_ogl(code):
    code = "\n".join([line.rstrip() for line in code.splitlines() if line.strip()])
    code = re.sub(r"\d{8}$", "", code, flags=re.MULTILINE)
    code = code.replace("          '","'")
    L = 72  # length of COBOL Unisys terminal
    code = "\n".join([line[:L].rstrip() for line in code.splitlines() if line.strip()])

    return code.replace("- '","-'")

def parse_report_antlr(
        code:str
) -> dict:
    try:

        # Preprocess
        code = preprocess_ogl(code)

        # Run lexer
        stream = InputStream(code)
        lexer = OGLLexer(stream)
        stream = CommonTokenStream(lexer)
        stream.fill()
        # Run parser
        parser = OGLParser(stream)
        # Build tree
        tree = parser.startRule()
        # Visit tree and Collect Information
        visitor = OGLVisitorImp()
        visitor.visit(tree)

        parsed_program = {
        "commands": [command.dict() for command in visitor.commands]
        }
        return parsed_program
    except Exception as e:
        logger.error(f"Error parsing Panel code: {e}")
        return None

def parse_report(
    content: str
) -> ReverseEngineeringUpdate:
    parsed_program = parse_report_antlr(content)
    if not parsed_program:
        status = ReverseEngineeringStatus.PARSED_ERROR
    else:
        status = ReverseEngineeringStatus.PARSED
    reverse_update_payload = ReverseEngineeringUpdate(
        output=parsed_program,
        type=FileType.REPORT,
        status=status,
    )
    return reverse_update_payload