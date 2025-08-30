from typing import List

from antlr4 import CommonTokenStream, InputStream
from loguru import logger
from pydantic import BaseModel

from parsers.grammar.batch.batch_schemas import BatchLabel
from parsers.grammar.batch.BatchLexer import BatchLexer
from parsers.grammar.batch.BatchParser import BatchParser
from parsers.grammar.batch.BatchVisitorImp import BatchVisitorImp
from schema.reverse_engineering import ReverseEngineeringUpdate, ReverseEngineeringStatus


class ParsedBatchProgram(BaseModel):
    labels: List[BatchLabel]


def preprocess_bat(code: str):
    code = code.replace("^\r\n", "").replace(":\r\n", "\r\n")
    return code


def parse_batch_antlr(code: str) -> ParsedBatchProgram:
    """Parse Batch script using ANTLR4

    Args:
        code (str): The Batch script code

    Returns:
        ParsedBatchProgram: Parsed Batch program
    """
    code = preprocess_bat(code)
    lexer = BatchLexer(InputStream(code))
    stream = CommonTokenStream(lexer)
    parser = BatchParser(stream)
    tree = parser.startRule()

    visitor = BatchVisitorImp()
    visitor.visit(tree)

    parsed_program = ParsedBatchProgram(
        labels=visitor.labels,
    )

    return parsed_program


def parse_batch(code: str) -> ReverseEngineeringUpdate:
    """Parse Batch script and update the status

    Args:
        code (str): The Batch script code

    Returns:
        ReverseEngineeringUpdate: Parsed Batch script with status
    """
    try:
        parsed_program = parse_batch_antlr(code)
        return ReverseEngineeringUpdate(
            output=parsed_program.model_dump(),
            type="BAT",
            status=ReverseEngineeringStatus.PARSED
        )
    except Exception as e:
        logger.error(f"Error parsing Batch script: {e}", exc_info=True, stack_info=True)
        return ReverseEngineeringUpdate(
            type="BAT",
            status=ReverseEngineeringStatus.PARSED_ERROR
        )
