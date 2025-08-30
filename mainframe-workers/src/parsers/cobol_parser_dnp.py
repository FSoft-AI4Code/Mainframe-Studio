import re
import sys
from typing import Optional, Dict

from antlr4 import CommonTokenStream, InputStream
from assessor.assessor import count_line
from loguru import logger
# Import the moved execution flow classes
from parsers.execution_flow import ExecutionFlowBuilder, organize_statements
from parsers.grammar.dnp_cobol.DNPLexer import DNPLexer
from parsers.grammar.dnp_cobol.DNPParser import DNPParser
from parsers.grammar.dnp_cobol.DNPVisitorImp import DNPVisitorImp
from parsers.grammar.dnp_cobol.dnp_cobol_schemas import DNPStatementFactory
from parsers.utils import calculate_cobol_complexity
from parsers.io_variables_flow import IOVariableFlowBuilder
from parsers.constants import COMMENT_TOKEN_FILTER
from schema.reverse_engineering import ReverseEngineeringUpdate
from utils.parse_util import get_io_files, map_picture_clause, extract_cobol_comment, get_working_storage_variables, get_subroutines_called


def preprocess_dnp(code):
    code = code.replace("\u001E", "<RS>")  # change the token

    code = re.sub(r"^.{6}", "      ", code, flags=re.MULTILINE)
    code = re.sub(r"^.{6}\/", "      *", code, flags=re.MULTILINE)
    code = re.sub(r"^\s{7}\*", "      **", code, flags=re.MULTILINE)
    code = re.sub(r"\*>.*$", "", code, flags=re.MULTILINE)
    code = re.sub(r"^\s*\\.*$", "", code, flags=re.MULTILINE)
    code = re.sub(r"\d{6}[A-Za-z]{2}", "        ", code, flags=re.MULTILINE)

    # Remove empty line, keep only 72 characters
    code = "\n".join([line for line in code.splitlines() if line.strip()])
    code = code.replace("<RS>", "\u001E")  # restore token

    return code


def parse_cobol_dnp_antlr(repository_id, code: str) -> Optional[Dict]:
    try:
        code = preprocess_dnp(code)
        code = "\n".join(code.splitlines())
        stream = CommonTokenStream(DNPLexer(InputStream(code)))
        stream.fill()
        lexer = DNPLexer(InputStream(code))
        parser = DNPParser(stream)
        parser.buildParseTrees = True
        tree = parser.startRule()

        visitor = DNPVisitorImp(parser)
        tree.accept(visitor)

        statements = [DNPStatementFactory.from_dict(statement) for statement in visitor.statements]
        organized_statements = organize_statements(statements)

        # Use ExecutionFlowBuilder from the imported module
        flow_builder = ExecutionFlowBuilder(organized_statements, visitor.program_id)
        exec_flow_graph = flow_builder.build()
        exec_flow_tree = flow_builder.build_tree(exec_flow_graph)

        io_files = get_io_files(visitor.file_control_list, visitor.file_description_list)
        working_storage_variables = get_working_storage_variables(visitor.variable_list, map_picture_clause)
        working_storage_copybooks = [copybook.model_dump() for copybook in visitor.working_storage_copybooks]
        comments = extract_cobol_comment(lexer, COMMENT_TOKEN_FILTER["DNP"], stream)

        identification_division = next(
            (division for division in visitor.division_list if division.division_name == "IDENTIFICATION DIVISION"),
            None)
        description = "\n".join([comment.content for comment in comments if
                                 comment.line_number < identification_division.start_line]) if identification_division else ""

        subroutines_called = get_subroutines_called(statements, comments)

        io_variables_flow_builder = IOVariableFlowBuilder(
            repository_id,
            visitor.file_control_list,
            visitor.file_description_list,
            working_storage_variables,
            working_storage_copybooks,
            statements,
            map_picture_clause,
        )
        variables_flow = io_variables_flow_builder.build()

        parsed_program = {
            "statements": statements,
            "paragraph_list": visitor.paragraph_list,
            "complexity": calculate_cobol_complexity(lexer, stream),
            "line_of_code": count_line(code, "COBOL")[0],
            "copybook_list": visitor.copybook_list,
            "called_program_list": visitor.called_program_list,
            "program_id": visitor.program_id,
            "io_files": io_files,
            "description": description,
            "working_storage_variables": working_storage_variables,
            "subroutines_called": subroutines_called,
            "variables_flow": variables_flow,
            "exec_flow": exec_flow_graph,
            "exec_flow_tree": exec_flow_tree,
        }

        return parsed_program
    except Exception as e:
        exception = sys.exc_info()
        logger.error(f"Error parsing COBOL code: {e}")
        logger.opt(exception=exception).info("Logging exception traceback")
        return None


def parse_cobol_dnp(repository_id, content: str) -> ReverseEngineeringUpdate:
    parsed_program = parse_cobol_dnp_antlr(repository_id=repository_id, code=content)
    if parsed_program:
        return ReverseEngineeringUpdate(
            output=parsed_program,
            type="COBOL"
        )
    return ReverseEngineeringUpdate(
        type="COBOL"
    )
