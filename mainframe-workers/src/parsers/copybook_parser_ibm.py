import re
import sys
import traceback
from typing import Any, Dict, List, Optional

from antlr4 import CommonTokenStream, InputStream
from loguru import logger

from assessor.assessor import count_line
from parsers.constants import COMMENT_TOKEN_FILTER
from parsers.grammar.copybook.CopyBookLexer import CopyBookLexer
from parsers.grammar.copybook.CopyBookParser import CopyBookParser
from parsers.grammar.copybook.CopybookVisitorImp import CopyBookVisitorImp
from parsers.grammar.copybook.CopyBookVisitorHelper import build_multi_layout_program
from schema.reverse_engineering import ReverseEngineeringStatus, ReverseEngineeringUpdate
from utils.parse_util import (
    extract_cobol_comment,
    get_copybook_variable_declarations,
    map_picture_clause_ibm,
)


def extract_special_dataname_pattern(code: str) -> list:
    # Extract some special word like this :TAG:
    # Match only the special data name patterns
    pattern = re.compile(r"\d{2}\s+(:[A-Z0-9]+:|\([A-Z0-9]+\))-")

    # Extract just the special data name using groups
    matches = [match.group(1) for match in pattern.finditer(code)]
    return matches


def preprocess_cob(code: str):
    code = code.replace("\u001E", "<RS>")
    L = 72 # lenght of COBOL Unisys terminal
    code = "\n".join([line[:L] for line in code.splitlines() if line.strip()])
    lines = code.splitlines()
    # Pattern to match any of these cases separately
    pattern = re.compile(r'^[A-Z]\d{4}$|^\d{4}$')
    extracted_numbers = set()
    for line in lines:
        if len(line) >= 70:
            candidate = line[L:80].strip()
            # print(candidate)
            if pattern.match(candidate):
                extracted_numbers.add(candidate)
    for num in extracted_numbers:
        code = code.replace(num, "")
    # print(extracted_numbers)
    # Regex to detect the line number at the beginning of each line (e.g., 000100)
    # and replace it with a tab character.
    # The regex matches the beginning of the line (^) followed by 6 digits (\d{6}),
    # and then replaces that part with a tab.
    code = re.sub(r"^\d{6}\s?", "      ", code, flags=re.MULTILINE)  
    code = re.sub(r"^\s\s\s\s\s\s\/", "      *", code, flags=re.MULTILINE)
    # code = re.sub(r"\d{8}$", "", code, flags=re.MULTILINE)
    # code = re.sub(r"^\s\s\s\s\s\s\s", "      *", code, flags=re.MULTILINE)
    # Remove lines starting with "AUTHOR"
    code = '\n'.join([line for line in code.splitlines() if not line.strip().startswith("AUTHOR")])
    # Remove lines starting with "DATE-WRIITEN"
    code = '\n'.join([line for line in code.splitlines() if not line.strip().startswith("DATE-WRITTEN")])
    # Remove lines starting with "DATA-WRIITEN"
    code = '\n'.join([line for line in code.splitlines() if not line.strip().startswith("DATA-WRITTEN")])
    # Remove lines starting with "DATA-COMPILED"
    code = '\n'.join([line for line in code.splitlines() if not line.strip().startswith("DATA-COMPILED")])
    code = "\n".join([line[:L] for line in code.splitlines() if line.strip()])
    code = code.replace(":XXX:", "CONSTANTVALUE")
        # Remove right white space
    code = "\n".join([line.rstrip() for line in code.splitlines() if line.strip()])
    lines = code.splitlines()
    for i, line in enumerate(lines):
        if  line.endswith("      000") or line.endswith("        0212") or line.endswith("         9403") or line.endswith("          9707") or line.endswith("          9702") or line.endswith("        970") or line.endswith("        0502") or line.endswith("    A") or line.endswith("    D") or line.endswith("      ****")or line.endswith("T               00") or line.endswith("T                   00"):
            lines[i] = line[:-4]
        if line.endswith("        100107") or line.endswith("         A2211") or line.endswith("          R2211"):
            lines[i] = line[:-6]
        if line.endswith(" **"):
            lines[i] = line[:-3]
    code = "\n".join(lines)
    pattern = re.compile(r'\.\s{2,}[\d/]+$')
    
    # Process each line
    cleaned_lines = []
    for line in code.splitlines():
        # Remove trailing pattern if found
        cleaned_line = re.sub(pattern, '.', line)
        cleaned_lines.append(cleaned_line)
    
    # Rejoin lines
    code = '\n'.join(cleaned_lines)
    lines = code.splitlines()
    for i, line in enumerate(lines):
        if len(line) < 7:
            # Remove lines with less than 7 characters
            lines[i] = ""
        if len(line) >= 6 and not line.startswith("      "):
            lines[i] = "      " + line[6:]
    code = "\n".join(lines)
    code = '\n'.join([line for line in code.splitlines() if not line.strip() == "SKIP3"])
    code = '\n'.join([line for line in code.splitlines() if not line.strip() == "SKIP2"])
    code = '\n'.join([line for line in code.splitlines() if not line.strip() == "SKIP1"])
    code = '\n'.join([line.rstrip() for line in code.splitlines() if not line.strip() == "EJECT"])
    code = code.replace("      D    ", "       "). replace("REMARKS *  *********************************************", "REMARKS")
    code = code.replace(":TAG:", "CONSTANTTAGVALUE").replace("(TESTVAR1)","TESTVAR1").replace("(SCRNVAR2)", "SCRNVAR2").replace("(MAPNAME3)", "MAPNAME3").replace("(*)","CONSTANTSTARVALUE").replace("'###'", "CONSTANTHASHVALUE")
    list_of_special_data_name = extract_special_dataname_pattern(code)
    # print(list_of_special_data_name)
    for char in list(set(list_of_special_data_name)):
        code = code.replace(char,"CONSTANTVALUEOF" + char[1:-2])
    # Logic to handle case 2 consecutive dots
    lines = code.splitlines()
    for i,line in enumerate(lines):
        if line.strip() == '.':
            index = i - 1
            while lines[index].startswith("      *"):
                index -= 1
            if lines[index].endswith("."):
                print(lines[index])
                # remove the line
                lines[i] = ""
        if line.replace(" ","").endswith(".."):
            lines[i] = lines[i][:-1]
        #  Logic to handle case "      *" in the middle of the line won't
        # be catched as comment tag
        if (not line.startswith("      *") and "      *" in line):
            lines[i] = line.replace("      *", "   *")
    code = "\n".join(lines)
    code = code.replace("<RS>","\u001E") 
    return code



def parse_copybook(copybook_name:str, code: str) -> Dict[str, Any]:
    try:
        code = preprocess_cob(code)
        COPY_TEMPLATE = """       IDENTIFICATION DIVISION.
       PROGRAM-ID. {}.

       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
{}"""
        code = COPY_TEMPLATE.format(copybook_name, code)
        lexer = CopyBookLexer(InputStream(code))
        stream = CommonTokenStream(lexer)
        stream.fill()

        parser = CopyBookParser(stream)
        parser.buildParseTrees = True
        tree = parser.startRule()

        visitor = CopyBookVisitorImp(parser)
        tree.accept(visitor)
        visitor.program_id = copybook_name

        if visitor.variable_list is None:
            return {"variables_declaration": [], "copy_length": ""}

        visitor.multi_layout_program = build_multi_layout_program( visitor.program_id, visitor.variable_list.working_storage,
                                                                  visitor.variable_list.linkage_section)

        comments = extract_cobol_comment(lexer, COMMENT_TOKEN_FILTER["IBM"], stream)
        variables_declaration = get_copybook_variable_declarations(
            visitor.variable_list, comments, map_picture_clause_ibm
        )
        copy_lengths = [
            comment.content for comment in comments if "RL=" in comment.content
        ]
        copy_length = copy_lengths[-1] if copy_lengths else ""

        parsed_program = {
            "variables_declaration": variables_declaration,
            "copy_length": copy_length,
            "line_of_code": count_line(code, "COPY")[0],
            "paragraph_list": visitor.paragraph_list,
            "multi_layout_program": visitor.multi_layout_program
        }
        return parsed_program

    except Exception as e:
        if not isinstance(e, TimeoutError):
            logger.error(f"Failed to parse copybook: {e}\n{traceback.format_exc()}")
            exception = sys.exc_info()
            logger.opt(exception=exception).info("Logging exception traceback")
            return None
        raise


def parse_copybook_ibm(copybook_name: str, content: str) -> ReverseEngineeringUpdate:
    parsed_program = parse_copybook(copybook_name, code=content)
    if parsed_program:
        return ReverseEngineeringUpdate(name=copybook_name, output=parsed_program, type="COPY", status=ReverseEngineeringStatus.PARSED)
    return ReverseEngineeringUpdate(name=copybook_name, type="COPY", status=ReverseEngineeringStatus.PARSED_ERROR)
