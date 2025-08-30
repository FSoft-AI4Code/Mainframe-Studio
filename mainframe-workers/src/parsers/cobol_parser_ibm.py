import json
import os
import re
import subprocess
import sys
import uuid
from typing import Any, Dict, Optional
from antlr4 import CommonTokenStream, InputStream
from loguru import logger

from assessor.assessor import count_line
from parsers.constants import COMMENT_TOKEN_FILTER

# Import from the new module
from parsers.database_crud import extract_crud
from parsers.dead_paragraph import get_dead_paragraphs
from parsers.execution_flow import ExecutionFlowBuilder, organize_statements
from parsers.grammar.ibm_cobol.Cobol85Lexer import Cobol85Lexer
from parsers.grammar.ibm_cobol.Cobol85Parser import Cobol85Parser
from parsers.grammar.ibm_cobol.ibm_cobol_schemas import IBMStatementFactory
from parsers.grammar.ibm_cobol.MyCobol85Visitor import MyCobol85Visitor
from parsers.grammar.ibm_cobol.Cobol85VisitorHelper import build_multi_layout_program
from parsers.missing_paragraphs import analyze_missing_paragraphs
from parsers.utils import calculate_cobol_complexity
from parsers.db_variables_flow import DBVariableFlowBuilder
from parsers.io_variables_flow import IOVariableFlowBuilder
from schema.reverse_engineering import (
    ReverseEngineeringStatus,
    ReverseEngineeringUpdate,
)
from utils.parse_util import (
    extract_cobol_comment,
    get_io_files,
    get_subroutines_called,
    get_working_storage_variables,
    map_picture_clause_ibm,
)

def preprocess_cbl(code: str) -> str:
    code = code.replace("\u001e", "<RS>")
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
    # Remove 8-digit numeric patterns
    pattern = re.compile(r"\b0\d{7}\b$")
    code = pattern.sub("", code)
    # Handle short lines and line beginnings
    lines = code.splitlines()
    processed_lines = []
    for line in lines:
        if not line.strip():
            continue
        if len(line) < 7:
            continue
        if not line.startswith("      "):
            line = "      " + line[6:]
        processed_lines.append(line)

    code = "\n".join(processed_lines)

    # Standard line processing
    code = re.sub(r"^.{6}", "      ", code, flags=re.MULTILINE)
    code = re.sub(r"^.{6}\/", "      *", code, flags=re.MULTILINE)
    code = re.sub(r"^\s{7}\*", "      **", code, flags=re.MULTILINE)
    code = re.sub(
        r"^(.*?)(\*>.*)$",
        lambda m: (
            m.group(1) if m.group(1).count("'") % 2 == 0 else m.group(1) + m.group(2)
        ),
        code,
        flags=re.MULTILINE,
    )
    # Remove 8-digit pattern at line ends
    code = re.sub(r"\b(?!99999999$)\d{8}$", "", code, flags=re.MULTILINE)
    code = "\n".join(
        [line for line in code.splitlines() if not line.strip() == "SKIP3"]
    )
    code = "\n".join(
        [line for line in code.splitlines() if not line.strip() == "SKIP2"]
    )
    code = "\n".join(
        [line for line in code.splitlines() if not line.strip() == "SKIP1"]
    )
    code = "\n".join(
        [line.rstrip() for line in code.splitlines() if not line.strip() == "EJECT"]
    )

    # Special replacements
    code = code.replace("      D    ", "       ")
    code = code.replace(
        "REMARKS *  *********************************************", "REMARKS"
    )
    L = 72
    # Trim to 72 characters
    code = "\n".join([line[:L] for line in code.splitlines() if line.strip()])
    lines = code.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("      D"):
            lines[i] = line.replace("      D", "       ")
    code = "\n".join(lines)
    code = "\n".join([line.rstrip() for line in code.splitlines() if line.strip()])
    code = code.replace("<RS>", "\u001e")
    return code.replace("DATE-COMILED", "DATE-COMPILED")


def format_koopa_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Format the Koopa parser output data by replacing spaces with underscores in keys.
    Handles nested dictionaries and lists recursively.
    """
    formatted_data = {}
    for key, value in data.items():
        formatted_key = key.replace(" ", "_")
        if isinstance(value, dict):
            formatted_data[formatted_key] = format_koopa_data(value)
        elif isinstance(value, list):
            formatted_list = []
            for item in value:
                if isinstance(item, dict):
                    formatted_list.append(format_koopa_data(item))
                else:
                    formatted_list.append(item)
            formatted_data[formatted_key] = formatted_list
        else:
            formatted_data[formatted_key] = value
    return formatted_data


def parse_cobol_koopa(
    parse_func: str, code: str, cache_path: str, encoding: str = "utf-8", last_depth: str = "200"
):
    if code is None:
        raise ValueError("Code parameter cannot be None")

    try:
        root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        cobol_parser = os.path.join(root_folder, "koopa.jar")

        # Create cache directory if it doesn't exist
        os.makedirs(cache_path, exist_ok=True)

        # Write code to a temporary file
        tmp_code_file = f"{uuid.uuid4().hex}.cbl"
        tmp_parsed_file = f"{uuid.uuid4().hex}.json"
        tmp_code_file_path = os.path.join(cache_path, tmp_code_file)
        tmp_parsed_file_path = os.path.join(cache_path, tmp_parsed_file)

        with open(tmp_code_file_path, "w", encoding=encoding) as f:
            f.write(code)

        subprocess.call(
            [
                "java",
                "-classpath",
                cobol_parser,
                f"koopa.examples.basic.{parse_func}",
                tmp_code_file_path,
                tmp_parsed_file_path,
                last_depth,
                cache_path,
            ],
            stdout=subprocess.DEVNULL,
        )

        with open(tmp_parsed_file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Format the data
        formatted_data = format_koopa_data(data)

        # Clean up temporary files
        os.remove(tmp_code_file_path)
        os.remove(tmp_parsed_file_path)

        return formatted_data

    except Exception as e:
        logger.error(
            "Koopa parsing failed",
            error=str(e),
            code_file=tmp_code_file_path,
            parsed_file=tmp_parsed_file_path,
        )
        raise


def parse_cobol_antlr(
    repository_id: str, program_name: str, code: str
) -> Dict[str, Any]:
    try:
        code = preprocess_cbl(code)
        code = "\n".join(code.splitlines())
        lexer = Cobol85Lexer(InputStream(code))
        stream = CommonTokenStream(lexer)
        stream.fill()

        parser = Cobol85Parser(stream)
        parser.buildParseTrees = True
        tree = parser.startRule()

        visitor = MyCobol85Visitor(parser)
        tree.accept(visitor)

        visitor.multi_layout_program = build_multi_layout_program(repository_id, visitor.program_id, visitor.variable_list.working_storage,
                                                                  visitor.variable_list.linkage_section, visitor.file_description_list)

        statements_dict = visitor.statements

        statements = []
        for statement_dict in statements_dict:
            statement = IBMStatementFactory.from_dict(statement_dict)
            statements.append(statement)

        # Add execution flow analysis
        organized_statements = organize_statements(statements)
        flow_builder = ExecutionFlowBuilder(
            organized_statements, visitor.program_id or program_name
        )
        exec_flow_graph = flow_builder.build()
        exec_flow_tree = flow_builder.build_tree(exec_flow_graph)
        
        local_missing_paragraphs = flow_builder.missing_paragraphs
        
        missing_paragraphs = analyze_missing_paragraphs(repository_id, local_missing_paragraphs, visitor.copybook_list)

        comments = extract_cobol_comment(lexer, COMMENT_TOKEN_FILTER["IBM"], stream)
        io_files = get_io_files(
            visitor.file_control_list, visitor.file_description_list
        )
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
        working_storage_variables = get_working_storage_variables(
            visitor.variable_list, map_picture_clause_ibm
        )
        working_storage_copybooks = [
            copybook.model_dump() for copybook in visitor.working_storage_copybooks
        ]
        subroutines_called = get_subroutines_called(statements, comments)

        io_variables_flow_builder = IOVariableFlowBuilder(
            repository_id,
            visitor.file_control_list,
            visitor.file_description_list,
            working_storage_variables,
            working_storage_copybooks,
            statements,
            map_picture_clause_ibm,
        )
        db_variables_flow_builder = DBVariableFlowBuilder(
            repository_id,
            working_storage_variables,
            working_storage_copybooks,
            statements,
        )
        io_variables_flow = io_variables_flow_builder.build()
        db_variables_flow = db_variables_flow_builder.build()
        variables_flow = io_variables_flow + db_variables_flow

        table_descriptors = extract_crud(statements)

        exit_paragraphs = [
            paragraph.split(".")[-1]
            for paragraph in flow_builder._single_exit_paragraph_set
        ]
        dead_paragraphs = get_dead_paragraphs(
            visitor.paragraph_list,
            exec_flow_graph,
            excluded_paragraph_names=exit_paragraphs,
        )

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
            "variables_flow": variables_flow,
            "subroutines_called": subroutines_called,
            "exec_flow": exec_flow_graph,
            "dead_paragraphs": dead_paragraphs,
            "missing_paragraphs": missing_paragraphs,
            "exec_flow_tree": exec_flow_tree,
            "table_descriptors": table_descriptors,
            "file_control_list": visitor.file_control_list,
            "file_description_list": visitor.file_description_list,
            "multi_layout_program": visitor.multi_layout_program
        }

        return parsed_program
    except Exception as e:
        exception = sys.exc_info()
        logger.error(f"Error parsing COBOL code: {e}")
        logger.opt(exception=exception).info("Logging exception traceback")
        return None

def parse_screen_access(content: str, cache_dir: str) -> Optional[str]:
    parsed_cics_output = parse_cobol_koopa(
        parse_func="ParseFileForCICSAnalysis", code=content, cache_path=cache_dir
    )
    for _, value in parsed_cics_output.items():
        if isinstance(value, dict) and value.get("mapset"):
            mapset_value = value.get("mapset")
            screen_name = (
                mapset_value[8:-2]
                if mapset_value.startswith("MAPSET('") and mapset_value.endswith("')")
                else None
            )
            return screen_name

def parse_cobol_ibm(
    repository_id: str, program_name: str, content: str
) -> ReverseEngineeringUpdate:
    parsed_program = parse_cobol_antlr(repository_id, program_name, code=content)

    if not parsed_program:
        status = ReverseEngineeringStatus.PARSED_ERROR
    else:
        status = ReverseEngineeringStatus.PARSED

    reverse_update_payload = ReverseEngineeringUpdate(
        name=program_name,
        output=parsed_program,
        type="COBOL",
        status=status,
    )
    return reverse_update_payload
