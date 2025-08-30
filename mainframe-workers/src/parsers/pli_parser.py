import json
import re
from typing import Any, Dict
from antlr4 import CommonTokenStream, InputStream
from loguru import logger

from schema.reverse_engineering import (
    ReverseEngineeringStatus,
    ReverseEngineeringUpdate,
)
from parsers.grammar.pli.PLIParser import PLIParser
from parsers.grammar.pli.PLILexer import PLILexer
from parsers.grammar.pli.PLIVisitorImp import PLIVisitorImp

def preprocess_pli(code:str)->str:
    
    code_st = ""

    lines = code.splitlines()

    for line in lines:
    
        if line.startswith(''):
            continue
        
        tline = line.rstrip()
        
        l = re.findall(r'\d+', tline)

        tmp = tline[0:72]

        if (len(l)>0):
            last = l[-1]
            if tline.endswith(last):
                ttmp = tline[:-len(last)].rstrip()
                if not (ttmp.endswith('-') or ttmp.endswith('+') or ttmp.endswith('*') 
                        or (ttmp.endswith('/') and not ttmp.endswith('*/')) 
                        or ttmp.endswith('>') or ttmp.endswith('<') or ttmp.endswith('=')):
                    tmp = ttmp

        tline = tmp
        
        if len(tmp[0:1].strip())>0:
            tline = tmp[1:]

        code_st +=tline + '\n'

    return code_st

def parse_pli_antlr(
    code: str
) -> dict:
    try:
        code = preprocess_pli(code)
        input_stream = InputStream(code)
        lexer = PLILexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        token_stream.fill()
        parser = PLIParser(token_stream)
        tree = parser.startRule()
        visitor = PLIVisitorImp()
        visitor.visit(tree)
        return {
            "statements": visitor.statements
        }
    except Exception as e:
        logger.error(f"Error parsing PLI code: {e}")
        return None

def parse_pli(
    name: str,
    content: str
) -> ReverseEngineeringUpdate:
    parsed_program = parse_pli_antlr(content)
    if not parsed_program:
        status = ReverseEngineeringStatus.PARSED_ERROR
    else:
        status = ReverseEngineeringStatus.PARSED
    reverse_update_payload = ReverseEngineeringUpdate(
        name=name,
        output=parsed_program,
        type="PLI",
        status=status,
    )
    return reverse_update_payload
