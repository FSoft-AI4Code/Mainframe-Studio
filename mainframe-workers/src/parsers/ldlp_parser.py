import os
import re
from contextlib import redirect_stderr, redirect_stdout
from xml.etree import ElementTree

from antlr4 import CommonTokenStream, InputStream
from loguru import logger

from parsers.grammar.ldlp.ldlp_schemas import ParsedLDLP
from parsers.grammar.ldlp.LDLPLexer import LDLPLexer
from parsers.grammar.ldlp.LDLPParser import LDLPParser
from parsers.grammar.ldlp.LDLPVisitorImp import LDLPVisitorImp


def preprocess_ldlp(code: str):
    try:
        xml_tree = ElementTree.fromstring(code)
        logic_tag = xml_tree.find(".//Logic")
        if logic_tag is not None:
            logic_code = logic_tag.text or ""
        else:
            logic_code = ""
    except ElementTree.ParseError:
        logger.error(f"XML parsing error for LDL+ file", exc_info=True)
        raise
    # add a space to empty comment to avoid parsing errors
    pattern = re.compile(r":$", re.MULTILINE)
    logic_code = pattern.sub(": ", logic_code)
    return logic_code


def parse_ldlp_antlr(code: str):
    try:
        code = preprocess_ldlp(code)
    except ElementTree.ParseError:
        logger.error("Failed to preprocess LDL+ code", exc_info=True)
        raise

    with open(os.devnull, "w", encoding="utf-8") as devnull:
        with redirect_stdout(devnull), redirect_stderr(devnull):
            lexer = LDLPLexer(InputStream(code))
            stream = CommonTokenStream(lexer)
            parser = LDLPParser(stream)
            tree = parser.startRule()
            visitor = LDLPVisitorImp()
            visitor.visit(tree)

    parsed_ldlp = ParsedLDLP(statements=visitor.statements)

    return parsed_ldlp
