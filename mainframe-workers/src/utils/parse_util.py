from typing import Dict, List, Union, Iterable, Callable
from antlr4 import CommonTokenStream
import structlog

# Import the moved execution flow classes
from parsers.execution_flow import iterate_statements
from parsers.grammar.common.base_cobol_schemas import Comment
from parsers.grammar.dnp_cobol.DNPLexer import DNPLexer
from parsers.grammar.ibm_cobol.Cobol85Lexer import Cobol85Lexer
from parsers.grammar.unisys_cobol.CobolUnisysLexer import CobolUnisysLexer

logger = structlog.get_logger()

def get_io_files(file_control_list, file_description_list) -> List[Dict[str, str]]:
    """
    Returns a list of dictionaries describing file assignments, access modes,
    open types, and copybooks. The 'copybooks_dict' is used to quickly look up
    copybooks for a given file name.
    """
    copybooks_dict = {
        fd.file_name: fd.copybooks
        for fd in file_description_list
    }

    return [
        {
            "name": fc.assignment_name,
            "access_mode": fc.access_mode,
            "open_type": fc.open_type,
            "copybooks": [cb.model_dump() for cb in copybooks_dict.get(fc.file_name, [])],
        }
        for fc in file_control_list
    ]


def map_picture_clause(picture_clause: str) -> Union[str, None]:
    """
    Maps a COBOL PIC clause string to a simpler data-type indicator:
    - 'X' for alphanumeric
    - 'A' for alphabetic
    - '9' for numeric (including S9)
    - 'N' for National
    Returns None if no recognized pattern is found or the clause is empty.
    """
    if not picture_clause:
        return None
    if "X" in picture_clause:
        return "X"
    elif "A" in picture_clause:
        return "A"
    elif "9" in picture_clause or "S9" in picture_clause:
        return "9"
    elif "N" in picture_clause:
        return "N"
    return None


def map_picture_clause_ibm(picture_clause: str) -> str:
    if picture_clause is not None:
        if "X" in picture_clause or "A" in picture_clause:
            return "char"
        elif "9" in picture_clause or "S9" in picture_clause:
            return "numeric"
        else:
            return "unknown"
    else:
        return "unknown"


def extract_cobol_comment(
    lexer: Union[Cobol85Lexer, CobolUnisysLexer, DNPLexer],
    token_name_filter: Iterable[str],
    stream: CommonTokenStream
) -> List[Comment]:
    """
    Iterates through the token stream, extracting tokens whose symbolic name
    matches any in 'token_name_filter'. Lines containing only '*' are ignored.
    For standard comment lines, the first 6 characters are removed (except when
    they start with '*>', which denotes an inline comment).
    """
    symbolic_names = lexer.symbolicNames
    tokens = stream.tokens
    comment_list = []

    for token in tokens:
        # Resolve token name; if out of range, use "UNKNOWN"
        token_name = (
            symbolic_names[token.type]
            if token.type < len(symbolic_names)
            else "UNKNOWN"
        )

        if token_name in token_name_filter:
            # Ignore comment lines that contain only '*'
            if token.text.strip('*').strip() == '':
                continue

            content = token.text
            # Remove first 6 characters for comment lines unless they're inline (start with "*>")
            if not content.startswith("*>") and len(content) > 6:
                content = content[5:]

            comment_list.append(
                Comment(
                    content=content.strip(),
                    line_number=token.line,
                )
            )

    return comment_list


def get_working_storage_variables(variable_list, map_picture_clause_fn) -> List[Dict[str, str]]:
    """
    Returns a list of dictionaries describing working-storage variables
    including data type, byte length, and remarks.
    """
    return [
        {
            "level": v.level,
            "line_number": v.line_number,
            "name": v.name,
            "data_type": map_picture_clause_fn(v.picture_clause) if v.picture_clause else "",
            "length": f"{v.picture_clause}{f' {v.compression_format}' if v.compression_format else ''}",
            "byte_length": (v.length or 0) * (v.occur or 1),
            "default_value": v.default_value or "",
            "remarks": (
                v.redefine if v.redefine
                else (v.occur if v.occur else "")
            ),
        }
        for v in variable_list.working_storage
    ]


def get_subroutines_called(statements, comments) -> List[Dict[str, str]]:
    """
    Iterates through parsed statements to find 'CallStatement' nodes, returning
    subroutine name and a "business name" from the most recent prior comment
    (if any).
    """
    # Pre-sort comments just once, descending by line number
    sorted_comments = sorted(comments, key=lambda x: x.line_number, reverse=True)
    subroutines_called = []

    for statement in iterate_statements(statements):
        if statement.tag == "CallStatement":
            subroutine_name = (
                statement.call_identifiers[0]
                if statement.call_identifiers
                else statement.call_literal
            )
            # Find the first comment in reverse order whose line_number < statement.start_line
            business_name = next(
                (
                    comment.content
                    for comment in sorted_comments
                    if comment.line_number < statement.start_line
                ),
                None
            )
            subroutines_called.append({
                "name": subroutine_name,
                "business_name": business_name
            })

    return subroutines_called


def get_copybook_variable_declarations(variable_list, comments, map_picture_clause_fn) -> List[Dict[str, str]]:
    variables_declaration = []
    variable_position = 1
    for variable in variable_list.working_storage:
        try:
            business_name = next(
                (comment.content for comment in comments
                    if comment.line_number == variable.line_number), 
                None
            )
            try:
                byte_length = (variable.length if variable.length else 0) * (variable.occur if variable.occur else 1)
            except ValueError as e:
                logger.error(f"Error converting length or occur to int: {e}")
                byte_length = 0

            variables_declaration.append({
                "level": variable.level,
                "name": variable.name.replace("PRE-", "(*)-"),
                "business_name": business_name,
                "data_type": map_picture_clause_fn(variable.picture_clause) if variable.picture_clause else "",
                "length": f"{variable.picture_clause}{f' {variable.compression_format}' if variable.compression_format else ''}",
                "byte_length": byte_length,
                "variable_position": variable_position,
                "remarks": variable.redefine if variable.redefine else variable.occur if variable.occur else "",
                "default_value": variable.default_value or "",
            })
            variable_position = variable_position + byte_length
        except Exception as e:
            logger.error(f"Error processing variable: {e}")
            continue
    return variables_declaration