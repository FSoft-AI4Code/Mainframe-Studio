import re 
from typing import Any, Dict
from antlr4 import CommonTokenStream, InputStream
from loguru import logger

from schema.reverse_engineering import (
    ReverseEngineeringStatus,
    ReverseEngineeringUpdate,
)

from parsers.grammar.clist.ClistLexer import ClistLexer
from parsers.grammar.clist.ClistParser import ClistParser
from parsers.grammar.clist.ClistVisitorImp import ClistVisitorImp
from classifier.constants import FileType

def modify_str(line):

    new_line = ""
    i = 0
    while i < len(line):
        if line[i:i+5] == "&STR(":
            # Found &STR(
            start = i + 5
            count = 1  # parentheses counter
            j = start
            while j < len(line) and count > 0:
                if line[j] == '(':
                    count += 1
                elif line[j] == ')':
                    count -= 1
                j += 1
            # Now line[start:j-1] is the inside content
            content = line[start:j-1]
            new_line += f'&STR("{content}")'
            i = j  # move pointer after the closing )
        else:
            new_line += line[i]
            i += 1

    return new_line

def preprocess_clist(code:str):
    L = 72
    code = code.replace("\u001E", "<RS>")
    code = "\n".join([line[:L] for line in code.splitlines() if line.strip()])
    code = code.replace("TOP ","")
    pattern1 = r"\+\s*\n"
    pattern2 = r"-\s*\n"
    code = re.sub(pattern1,"",code,flags=re.MULTILINE)
    code = re.sub(pattern2,"",code, flags=re.MULTILINE)
    lines = code.splitlines()
    for i,line in enumerate(lines):
        if "&STR(" in line:
            lines[i] = modify_str(line)
    code = "\n".join(lines)
    
    code = "\n".join([line.rstrip() for line in code.splitlines() if line.strip()])
    lines = code.splitlines()
    for i,line in enumerate(lines):
        if line.endswith("WRITE") or line.endswith("WRITENR"):
            lines[i] = lines[i] + "  "
    code = "\n".join(lines)
    code = code.replace("                 )'","").replace("POS3820C","").replace("POS3810C","").replace("POS3840C","")
    code = code.replace("<RS>","\u001E")
    if code.endswith("//"):
        code = code[:-2]
    return code


def parse_clist_antlr(
        code:str
) -> dict:
    try:
        code = preprocess_clist(code)

        # Run lexer
        stream = InputStream(code)
        lexer = ClistLexer(stream)
        stream = CommonTokenStream(lexer)
        stream.fill()
        # Run parser
        parser = ClistParser(stream)
        # Build tree
        tree = parser.startRule()
        # Visit tree and Collect Information
        visitor = ClistVisitorImp()
        visitor.visit(tree)
        parsed_program = {
        "statements": [statement.dict() for statement in visitor.statements],
        "labels": [label.dict() for label in visitor.labels]  
    }
        return parsed_program
    except Exception as e:
        logger.error(f"Error parsing Clist code: {e}")
        return None
    

def parse_clist(
    content: str
) -> ReverseEngineeringUpdate:
    parsed_program = parse_clist_antlr(content)
    if not parsed_program:
        status = ReverseEngineeringStatus.PARSED_ERROR
    else:
        status = ReverseEngineeringStatus.PARSED
    reverse_update_payload = ReverseEngineeringUpdate(
        output=parsed_program,
        type=FileType.CLIST,
        status=status,
    )
    return reverse_update_payload