import re
import os
from antlr4 import CommonTokenStream, InputStream
from loguru import logger
from assessor.assessor import count_line
from parsers.grammar.bms import BMSLexer, BMSParser, MyBMSVisitor
from contextlib import redirect_stdout, redirect_stderr
from parsers.analyzed_bms import AnalyzedBMS
from schema.reverse_engineering import ReverseEngineeringUpdate, ReverseEngineeringStatus

def parse_bms_antlr(content, title):
    # Redirect the standard output and standard error to devnull
    # non unix-like sys or windows: with open('nul', 'w') as devnull
    with open(os.devnull, 'w', encoding='utf-8') as devnull:
        with redirect_stdout(devnull), redirect_stderr(devnull):
            stream = CommonTokenStream(BMSLexer(InputStream(content)))
            stream.fill()

            # tokens = stream.getTokens(0, 100000000)

            parser = BMSParser(stream)
            parser.buildParseTrees = True
            tree = parser.program()

            visitor = MyBMSVisitor()
            visitor.title = title
            tree.accept(visitor)

    return visitor.definitions

def preprocess_bms(code):
    # Get current BMS file's TITLE
    title_match = re.search(r'^\s*TITLE\s+(.*)$', code, flags=re.MULTILINE)
    title = title_match.group(1).strip() if title_match else ""
    code = re.sub(r'^\s*TITLE.*$', '', code,
                     flags=re.MULTILINE).strip()
    code = '\n'.join([line[:71] for line in code.splitlines() if not "PRINT NOGEN" in line and not "PRINT  NOGEN" in line])
    # handle case ''ABCD'' to ""ABCD""
    code = re.sub(r"''([^'\n]*?)''", r'"\1"', code).replace("''",'"')
    keywords = "DFHMDF"
    lines = code.splitlines()
    for i,line in enumerate(lines):
        # print("lines",i)
        for j in range(i+1,len(lines)):

            if lines[j].strip().startswith('*'):
                continue
            else:
                line_to_check = lines[j]
                break   
        # print(line_to_check) 
        if lines[i].endswith(',') and keywords in line_to_check:
            lines[i] = line[:-1]
            # print(lines[i],line_to_check)
    code = '\n'.join(lines)
    code = "\n".join([line.rstrip() for line in code.splitlines() if line.strip()])

    # print(re.match(r"''([^']*?)''",code))
    # print(new_text)
    return title, code

def reverse_bms(name, parsed_bms, line_of_code):
    bms = AnalyzedBMS(
        file_name=name,
        definitions=parsed_bms
    )
    reversed_bms = bms.extract_data()
    reversed_bms["line_of_code"] = line_of_code
    return reversed_bms

def parse_bms(name, content) -> ReverseEngineeringUpdate:
    """Parse BMS using ANTLR4
    
    Args:
        name (str): The name of the BMS file
        content (str): The content of the file
        
    Returns:
        ReverseEngineeringUpdate: Parsed BMS with status
    """
    try:
        title, content = preprocess_bms(content)
        parsed_bms = parse_bms_antlr(content, title=title)
        reversed_bms = reverse_bms(name, parsed_bms, count_line(content,"BMS")[0])
        return ReverseEngineeringUpdate(
            name=name,
            output=reversed_bms,
            type="BMS",
            status=ReverseEngineeringStatus.PARSED
        )
    except Exception as e:
        logger.error(f"Error parsing BMS {name}: {e}", exc_info=True, stack_info=True)
        return ReverseEngineeringUpdate(
            name=name,
            type="BMS",
            status=ReverseEngineeringStatus.PARSED_ERROR
        )
