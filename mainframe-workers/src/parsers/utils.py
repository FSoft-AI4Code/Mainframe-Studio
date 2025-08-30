import itertools
import math
import re
from typing import List, Dict, Union, Optional, Any

from antlr4 import CommonTokenStream
from controller.reverse_controller import ReverseController
from parsers.grammar.dnp_cobol.DNPLexer import DNPLexer
from parsers.grammar.ibm_cobol.Cobol85Lexer import Cobol85Lexer
from parsers.grammar.unisys_cobol.CobolUnisysLexer import CobolUnisysLexer



def calculate_cobol_complexity(
        lexer: Union[Cobol85Lexer, CobolUnisysLexer, DNPLexer], stream: CommonTokenStream
) -> int:
    """Calculate the complexity of the COBOL program

    Args:
        lexer (Union[Cobol85Lexer, CobolUnisysLexer, DNPLexer]): The lexer of the COBOL program
        stream (CommonTokenStream): The input stream of the COBOL program

    Returns:
        int: The cyclomatic complexity of the COBOL program
    """
    symbolic_names = lexer.symbolicNames
    tokens = stream.tokens
    complexity = 0

    # Reference: https://www.ibm.com/docs/en/raa/6.1?topic=metrics-cyclomatic-complexity
    reserved_words = [
        "ALSO",
        "ALTER",
        "AND",
        "DEPENDING",
        "EXEC",
        "END-OF-PAGE",
        "ENTRY",
        "EOP",
        "EXCEPTION",
        "EXIT",
        "GOBACK",
        "IF",
        "INVALID",
        "OR",
        "OVERFLOW",
        "SIZE",
        "STOP",
        "TIMES",
        "UNTIL",
        "USE",
        "VARYING",
        "WHEN",
    ]

    for token in tokens:
        token_name = (
            symbolic_names[token.type] if token.type < len(symbolic_names) else None
        )
        if token_name in reserved_words:
            complexity += 1

    return complexity


def calculate_cobol_variable_length(
        pic: str, compression_format: Optional[str] = None
) -> int:
    pic = pic.upper()
    symbol_list = ["9", "X", "A", "P", "Z"]
    regex_extract_length = re.compile(r"\((.*?)\)")

    # sum all the numbers inside brackets
    length_list = re.findall(regex_extract_length, pic)
    length = 0
    for item in length_list:
        try:
            length += int(item)
        except ValueError:
            continue

    # sum the number of symbols which are not before "("
    for element in pic.split(")"):
        if "(" not in element:
            element = element.upper()

            for symbol in symbol_list:
                length += element.count(symbol)

    if compression_format is None:
        return length

    compression_format = compression_format.upper()
    # recalculate length with compression format
    is_half_int = math.ceil(length / 2) == math.floor(length / 2)

    is_binary_compression_format = (
            "COMP" in compression_format or "BINARY" in compression_format
    )

    is_bcd_compressed_format = (
            "COMP-3" in compression_format or "PACKED-DECIMAL" in compression_format
    )

    if is_bcd_compressed_format:
        length = math.ceil(length / 2) + \
                 1 if is_half_int else math.ceil(length / 2)
    elif is_binary_compression_format:
        if length <= 4:
            length = 2
        elif length <= 9:
            length = 4
        elif length <= 18:
            length = 8

    return length


def handle_analysis_map(analysis_map: Dict[str, Any]) -> Dict[str, Any]:
    data_map_list = analysis_map["dataMapList"]
    io_map_list = analysis_map["ioMapList"]
    linkage_map_list = analysis_map["linkageMapList"]

    for i, data_map in enumerate(data_map_list):
        if "pic" not in data_map:
            continue

        pic = data_map["pic"]
        compression_format: Optional[str] = data_map.get("data_type")

        length = calculate_cobol_variable_length(
            pic=pic, compression_format=compression_format
        )

        data_map_list[i]["num_digits"] = str(length)

    if len(io_map_list) > 0 and isinstance(io_map_list[0], list):
        io_map_list = list(itertools.chain(*io_map_list))

    for io_map in io_map_list:
        if "pic" not in io_map:
            continue

        pic = io_map["pic"]
        compression_format = io_map.get("data_type")

        length = calculate_cobol_variable_length(
            pic=pic, compression_format=compression_format
        )

        io_map["num_digits"] = str(length)

    for linkage_map in linkage_map_list:
        if "num_digits" not in linkage_map:
            continue

        pic = linkage_map["pic"]
        compression_format = linkage_map.get("data_type")

        length = calculate_cobol_variable_length(
            pic=pic, compression_format=compression_format
        )

        linkage_map["num_digits"] = str(length)


def extract_copy_filenames(lines: List[str]) -> Dict[str, Union[str, int]]:
    """Find COPY statements in the COBOL file lines and extract filenames with their line numbers."""
    return {
        line_number: re.search(r"^\s+COPY\s+([^\s]+)", line).group(1).split(".")[0]
        for line_number, line in enumerate(lines)
        if re.match(r"^\s+COPY\s+.*\.", line) and not line.lstrip().startswith("*")
    }


def handle_replacing_copy(copy_line: str, copy_content: str) -> str:
    if "REPLACING" not in copy_line:
        return copy_content

    copy_content_lines = copy_content.split("\n")
    match = re.search(
        r"REPLACING\s+(==\s+)?([^\s]+)(\s+==)?\s+BY\s+(==\s+)?([^\s]+)(\s+==)?",
        copy_line,
    )
    if match:
        source, target = match.group(2).replace("==", ""), match.group(5).strip(".").replace("==", "")
        copy_content_lines = [
            line.replace(source, target) for line in copy_content_lines
        ]
    return "\n".join(copy_content_lines)


def merge_cpy(code_lines: List[str], not_found_files: List[str] = [],
              preprocess_function: Optional[callable] = None) -> str:
    reverse_controller = ReverseController()
    copy_filenames = extract_copy_filenames(code_lines)
    if not copy_filenames:
        return "\n".join(code_lines)
    if all(filename in not_found_files for filename in copy_filenames.values()):
        return "\n".join(code_lines)
    for line, filename in copy_filenames.items():
        copy_content = reverse_controller.query_copy_content(filename.replace("'", ""))
        copy_content = preprocess_function(copy_content) if preprocess_function else copy_content
        if not copy_content:
            not_found_files.append(filename)
            continue
        copy_content = handle_replacing_copy(code_lines[line], copy_content)
        code_lines[line] = copy_content
    return merge_cpy(code_lines, not_found_files)
