import re
import sys
from typing import Dict, Optional

from antlr4 import CommonTokenStream, InputStream
from loguru import logger

from assessor.assessor import count_line
from parsers.constants import COMMENT_TOKEN_FILTER
from parsers.database_crud import extract_crud
from parsers.dead_paragraph import get_dead_paragraphs
from parsers.execution_flow import ExecutionFlowBuilder, organize_statements
from parsers.grammar.common.base_cobol_schemas import Statement
from parsers.grammar.unisys_cobol.cobol_unisys_schemas import UnisysStatementFactory
from parsers.grammar.unisys_cobol.CobolUnisysLexer import CobolUnisysLexer
from parsers.grammar.unisys_cobol.CobolUnisysParser import CobolUnisysParser
from parsers.grammar.unisys_cobol.DaikyoUnisysCobolVistor import DaikyoUnisysCobolVistor
from parsers.utils import calculate_cobol_complexity
from parsers.io_variables_flow import IOVariableFlowBuilder
from schema.reverse_engineering import ReverseEngineeringStatus, ReverseEngineeringUpdate
from utils.parse_util import (
    extract_cobol_comment,
    get_io_files,
    get_subroutines_called,
    get_working_storage_variables,
    map_picture_clause,
)


def preprocess_cobol_unisys(code: str) -> str:
    L = 72  # lenght of COBOL Unisys terminal
    i = 0
    # Regex to detect the line number at the beginning of each line (e.g., 000100)
    # Find position of line start with
    code = code.replace("\u001e", "<RS>")  # change the token
    lines = code.splitlines()
    pattern = re.compile(
        r"^.{7}IDENTIFICATION\s*DIVISION.|^.{7}ID\s*DIVISION.|^.{8}IDENTIFICATION\s*DIVISION.|^.{8}ID\s*DIVISION."
    )

    for i, line in enumerate(lines):
        if pattern.search(line):
            break
        if i > 100:
            break
    if i <= 100:
        # Delete all file before
        code = "\n".join(lines[i:])

    # Store unwanted characters after the code line
    pattern = re.compile(
        r"^\d{6}$|^\d{2}/\d{2}/\d{2}$|^[^\s]{8}$|^[^\s]{7}$|^\d{6}\s[A-Z]$"
    )
    extracted_numbers = set()
    for line in lines:
        if len(line) >= 70:
            candidate = line[L:80].strip()
            if pattern.match(candidate):
                extracted_numbers.add(candidate)

    code = re.sub(r"^.{6}", "      ", code, flags=re.MULTILINE)
    code = re.sub(r"^.{6}\/", "      *", code, flags=re.MULTILINE)
    code = re.sub(r"^\s{7}\*", "      **", code, flags=re.MULTILINE)
    code = re.sub(r"^\s*\\.*$", "", code, flags=re.MULTILINE)
    code = re.sub(r"\d{6}[A-Za-z]{2}", "        ", code, flags=re.MULTILINE)

    # Remove unwanted characters
    for num in extracted_numbers:
        code = code.replace(num, "")

    # Remove empty line, keep only 72 characters
    code = "\n".join([line[:L] for line in code.splitlines() if line.strip()])
    code = code.replace("<RS>", "\u001e")  # restore token

    return code


def parse_cobol_unisys_antlr(repository_id: str, code: str) -> Optional[Dict]:
    try:
        code = preprocess_cobol_unisys(code)
        code = "\n".join(code.splitlines())
        stream = CommonTokenStream(CobolUnisysLexer(InputStream(code)))
        stream.fill()
        lexer = CobolUnisysLexer(InputStream(code))
        parser = CobolUnisysParser(stream)
        parser.buildParseTrees = True
        tree = parser.startRule()

        visitor = DaikyoUnisysCobolVistor(parser)
        tree.accept(visitor)

        # Convert visitor statements to proper format and build execution flow
        statements = []
        for statement_dict in visitor.statements:
            statement = UnisysStatementFactory.from_dict(statement_dict)
            statements.append(statement)

        organized_statements = organize_statements(statements)
        flow_builder = ExecutionFlowBuilder(organized_statements, visitor.program_id)
        exec_flow_graph = flow_builder.build()
        exec_flow_tree = flow_builder.build_tree(exec_flow_graph)

        io_files = get_io_files(
            visitor.file_control_list, visitor.file_description_list
        )
        working_storage_variables = get_working_storage_variables(
            visitor.variable_list, map_picture_clause
        )
        comments = extract_cobol_comment(lexer, COMMENT_TOKEN_FILTER["UNISYS"], stream)

        identification_division = next(
            (
                division
                for division in visitor.division_list
                if division.division_name == "IDENTIFICATION DIVISION"
            ),
            None,
        )
        description = (
            "\n".join(
                [
                    comment.content
                    for comment in comments
                    if comment.line_number < identification_division.start_line
                ]
            )
            if identification_division
            else ""
        )

        table_descriptors = []
        for database in visitor.database_list:
            database_table_descriptor = extract_crud(statements, database)
            table_descriptors.extend(database_table_descriptor)

        subroutines_called = get_subroutines_called(statements, comments)
        working_storage_copybooks = [
            copybook.model_dump() for copybook in visitor.working_storage_copybooks
        ]

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
        
        exit_paragraphs = [
            paragraph.split(".")[-1] for paragraph in flow_builder._single_exit_paragraph_set
        ]
        dead_paragraphs = get_dead_paragraphs(visitor.paragraph_list, exec_flow_graph, excluded_paragraph_names=exit_paragraphs)

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
            "table_descriptors": table_descriptors,
            "subroutines_called": subroutines_called,
            "variables_flow": variables_flow,
            "exec_flow": exec_flow_graph,
            "dead_paragraphs": dead_paragraphs,
            "exec_flow_tree": exec_flow_tree,
        }

        return parsed_program
    except Exception as e:
        exception = sys.exc_info()
        logger.error(f"Error parsing COBOL code: {e}")
        logger.opt(exception=exception).info("Logging exception traceback")
        return None


def parse_cobol_unisys(repository_id: str, content: str) -> ReverseEngineeringUpdate:
    parsed_program = parse_cobol_unisys_antlr(repository_id=repository_id, code=content)
    if parsed_program:
        return ReverseEngineeringUpdate(output=parsed_program, type="COBOL", status=ReverseEngineeringStatus.PARSED)
    return ReverseEngineeringUpdate(type="COBOL", status=ReverseEngineeringStatus.PARSED_ERROR)
