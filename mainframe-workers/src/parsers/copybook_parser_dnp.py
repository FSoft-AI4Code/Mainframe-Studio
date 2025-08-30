import re, sys, os
from typing import List, Dict, Optional, Any
from pydantic import BaseModel
from loguru import logger
from antlr4 import CommonTokenStream, InputStream
from pymongo import MongoClient

from assessor.assessor import count_line
from utils.parse_util import extract_cobol_comment, get_copybook_variable_declarations, map_picture_clause
from parsers.grammar.dnp_cobol.DNPLexer import DNPLexer
from parsers.grammar.dnp_cobol.DNPParser import DNPParser
from parsers.grammar.dnp_cobol.DNPVisitorImp import DNPVisitorImp
from parsers.grammar.common.base_cobol_schemas import Comment
from parsers.constants import COMMENT_TOKEN_FILTER
from schema.reverse_engineering import ReverseEngineeringUpdate, ParsedProgramAntlr

def preprocess_cob_dnp(code: str) -> str:
    predefined_lines = """
000130 IDENTIFICATION          DIVISION.\n
000140 PROGRAM-ID.             NHKS1CHK.\n
000150 ENVIRONMENT             DIVISION.\n
000160 CONFIGURATION           SECTION.\n
000170 SOURCE-COMPUTER.        FACOM.\n
000180 OBJECT-COMPUTER.        FACOM.\n
000250 DATA                    DIVISION.\n
000780 WORKING-STORAGE         SECTION.\n
\n
"""
    code = predefined_lines + code
    lines = code.splitlines()
 
    for i, line in enumerate(lines):
        lines[i] = " " * 6 + line[6:]
 
    code = "\n".join(lines)
    code = re.sub(r"\(\*\)\-", "PRE-", code)
    return code


def parse_copybook_dnp_antlr(code: str) -> Dict[str, Any]:
    try:
        code = preprocess_cob_dnp(code)
        code = "\n".join(code.splitlines())
        stream = CommonTokenStream(DNPLexer(InputStream(code)))
        stream.fill()
        lexer = DNPLexer(InputStream(code))
        parser = DNPParser(stream)
        parser.buildParseTrees = True
        tree = parser.startRule()

        visitor = DNPVisitorImp(parser)
        tree.accept(visitor)
        comments = extract_cobol_comment(lexer, COMMENT_TOKEN_FILTER["DNP"], stream)
        variables_declaration = get_copybook_variable_declarations(visitor.variable_list, comments, map_picture_clause)
        copy_lengths = [comment.content for comment in comments if "RL=" in comment.content]
        copy_length = copy_lengths[-1] if copy_lengths else ""

        parsed_program = {
            "variables_declaration": variables_declaration,
            "copy_length": copy_length,
            "line_of_code": count_line(code,"COPY")[0]
        }

        return parsed_program

    except Exception as e:
        logger.error(f"Failed to parse DNP copybook: {str(e)}")
        return None
    
def parse_copybook_dnp(content: str) -> ReverseEngineeringUpdate:
    parsed_program = parse_copybook_dnp_antlr(code=content)
    if parsed_program:
        return ReverseEngineeringUpdate(
            output=parsed_program,
            type="COPY"
        )
    return ReverseEngineeringUpdate(
        type="COPY"
    )