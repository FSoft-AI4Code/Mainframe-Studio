from antlr4 import CommonTokenStream, InputStream
from parsers.grammar.asm.asmLexer import asmLexer
from parsers.grammar.asm.asmParser import asmParser
from parsers.grammar.asm.myAsmVisitor import MyAsmVisitor
from schema.reverse_engineering import (
    ReverseEngineeringUpdate,
    ReverseEngineeringStatus,
)
from loguru import logger


def preprocess_asm(code: str):
    lines = code.splitlines()
    processed = "\n".join(l.rstrip() for l in lines if l.strip() != "*")
    return processed


def parse_asm_antlr(code: str) -> dict:
    try:
        input = preprocess_asm(code)

        input_stream = InputStream(input)
        lexer = asmLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        token_stream.fill()
        parser = asmParser(token_stream)
        tree = parser.startRule()
        visitor = MyAsmVisitor()
        visitor.visit(tree)
        return {"call_statements": visitor.call_statements}
    except Exception as e:
        logger.error(f"Error parsing ASM code: {e}")
        return None


def parse_asm(content: str) -> ReverseEngineeringUpdate:
    """Parse ASM using ANTLR4

    Args:
        content (str): The content of the file

    Returns:
        ReverseEngineeringUpdate: Parsed ASM with status
    """
    try:
        parsed_program = parse_asm_antlr(content)
        if not parsed_program:
            raise Exception("Failed to parse ASM")
        return ReverseEngineeringUpdate(
            output=parsed_program,
            type="ASM",
             status=ReverseEngineeringStatus.PARSED
        )
    except Exception as e:
        logger.error(f"Error parsing ASM: {e}", exc_info=True, stack_info=True)
        return ReverseEngineeringUpdate(
            type="ASM",
            status=ReverseEngineeringStatus.PARSED_ERROR
        )
