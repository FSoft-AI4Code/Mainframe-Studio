import re 
from typing import Any, Dict
from antlr4 import CommonTokenStream, InputStream
from loguru import logger

from schema.reverse_engineering import (
    ReverseEngineeringStatus,
    ReverseEngineeringUpdate,
)

from parsers.grammar.panel.PanelLexer import PanelLexer
from parsers.grammar.panel.PanelParser import PanelParser
from parsers.grammar.panel.PanelVisitorImp import PanelVisitorImp
from classifier.constants import FileType

# This function inherits from the repository parser

def extract_body_section(code: str):
    # Match ")BODY" line with any parameters (including WINDOW(6 7)), then capture content until next section
    pattern = r"(\)BODY[^\n]*\n)(.*?)(?=\n\)\w+)"
    match = re.search(pattern, code, re.DOTALL)

    if not match:
        return None, code
    
    body_header = match.group(1)
    body_text = match.group(2).strip()

    # Remove just the body text, keeping the header and next section
    cleaned_code = code.replace(match.group(0), body_header)
    
    return body_text, cleaned_code

def preprocess_panel(code):
    body_text, code = extract_body_section(code)
    # Remove all lines after the line ")END"
    end_index = code.find(")END")
    if end_index != -1:
        code = code[:end_index + 5]

    return code.replace("\u02dd=","=").replace("\u00fd=","=").replace("?=","=").replace("^=","="), body_text



def parse_panel_antlr(
        code:str
) -> dict:
    try:

        # Preprocess
        code,body_text = preprocess_panel(code)

        # Run lexer
        stream = InputStream(code)
        lexer = PanelLexer(stream)
        stream = CommonTokenStream(lexer)
        stream.fill()
        # Run parser
        parser = PanelParser(stream)
        # Build tree
        tree = parser.startRule()
        # Visit tree and Collect Information
        visitor = PanelVisitorImp(body_text)
        visitor.visit(tree)

        parsed_program = {
            "sections": [section.dict() for section in visitor.sections],
            # "statements": [statement.dict() for statement in visitor.statements],
        }
        return parsed_program
    except Exception as e:
        logger.error(f"Error parsing Panel code: {e}")
        return None

def parse_panel(
    content: str
) -> ReverseEngineeringUpdate:
    parsed_program = parse_panel_antlr(content)
    if not parsed_program:
        status = ReverseEngineeringStatus.PARSED_ERROR
    else:
        status = ReverseEngineeringStatus.PARSED
    reverse_update_payload = ReverseEngineeringUpdate(
        output=parsed_program,
        type=FileType.PANEL,
        status=status,
    )
    return reverse_update_payload