# src/parsers/copybook_parser_unisys.py
import re
from typing import Any, Dict, List
from pydantic import BaseModel
from antlr4 import CommonTokenStream, InputStream
from assessor.assessor import count_line
from utils.parse_util import extract_cobol_comment, get_copybook_variable_declarations, map_picture_clause
from parsers.grammar.unisys_cobol.CobolUnisysLexer import CobolUnisysLexer
from parsers.grammar.unisys_cobol.CobolUnisysParser import CobolUnisysParser
from parsers.grammar.unisys_cobol.DaikyoUnisysCobolVistor import DaikyoUnisysCobolVistor
from parsers.grammar.common.base_cobol_schemas import CobolVariable
from parsers.constants import COMMENT_TOKEN_FILTER
from schema.reverse_engineering import ReverseEngineeringStatus, ReverseEngineeringUpdate

class ParsedUnisysCopybook(BaseModel):
    variables_declaration: List[Dict[str, Any]]
    copy_length: str
    line_of_code: int

def preprocess_cob_unisys(code: str) -> str:
    # Predefined lines to add at the beginning of the content
    predefined_lines = """
000130 IDENTIFICATION          DIVISION.\n
000140 PROGRAM-ID.             COPYBOOK.\n
000150 ENVIRONMENT             DIVISION.\n
000160 CONFIGURATION           SECTION.\n
000170 SOURCE-COMPUTER.        FACOM.\n
000180 OBJECT-COMPUTER.        FACOM.\n
000250 DATA                    DIVISION.\n
000780 WORKING-STORAGE         SECTION.\n
\n
"""
    # Add predefined lines at the beginning of the code
    code = predefined_lines + code
    # Regex to detect the line number at the beginning of each line (e.g., 000100)
    # and replace it with a tab character.
    # The regex matches the beginning of the line (^) followed by 6 digits (\d{6}),
    # and then replaces that part with a tab.
    code = re.sub(r"^\d{6}\s*", "      ", code, flags=re.MULTILINE)  
    code = re.sub(r"^\s\s\s\s\s\s\/", "      *", code, flags=re.MULTILINE)
    # Replace (*)- with PRE- across the code
    code = re.sub(r"\(\*\)\-", "PRE-", code)
    # Strip trailing spaces from each line
    lines = code.splitlines() # Split the text into lines
    cleaned_lines = [line.rstrip() for line in lines if line.strip()]
    # Concate lines
    code = '\n'.join(cleaned_lines)
    # Remove empty comment
    lines = code.splitlines() # Split the text into lines
    cleaned_lines = [line[:72] for line in lines]    
    # Join the lines back into a single string
    return '\n'.join(cleaned_lines)

def parse_unisys_copybook(code: str) -> ParsedUnisysCopybook:
    try:
        code = preprocess_cob_unisys(code)
        lexer = CobolUnisysLexer(InputStream(code))
        stream = CommonTokenStream(lexer)
        stream.fill()

        parser = CobolUnisysParser(stream)
        parser.buildParseTrees = True 
        tree = parser.startRule()

        visitor = DaikyoUnisysCobolVistor(parser)
        tree.accept(visitor)
        
        comments = extract_cobol_comment(lexer, COMMENT_TOKEN_FILTER["UNISYS"], stream)
        copy_lengths = [comment.content for comment in comments if "RL=" in comment.content]
        copy_length = copy_lengths[-1] if copy_lengths else ""

        return ParsedUnisysCopybook(
            variables_declaration = get_copybook_variable_declarations(visitor.variable_list, comments, map_picture_clause),
            copy_length=copy_length,
            line_of_code=count_line(code,"COPY")[0]
        )

    except Exception as e:
        raise ValueError(f"Failed to parse Unisys copybook: {str(e)}")
    
def parse_copybook_unisys(content: str) -> ReverseEngineeringUpdate:
    parsed_program = parse_unisys_copybook(code=content)
    if parsed_program:
        return ReverseEngineeringUpdate(
            output=parsed_program.model_dump(),
            type="COPY", status=ReverseEngineeringStatus.PARSED,
        )
    return ReverseEngineeringUpdate(
        type="COPY", status=ReverseEngineeringStatus.PARSED_ERROR
    )