import math
import re
from typing import Dict, List, Optional, Type, TypeVar, Union

from antlr4 import CommonTokenStream, Parser, ParserRuleContext, TerminalNode

from grammar.copybook.CopyBookParser import CopyBookParser
from grammar.dnp.DNPLexer import DNPLexer
from grammar.dnp.DNPParser import DNPParser
from grammar.ibm_cobol.Cobol85Lexer import Cobol85Lexer
from grammar.ibm_cobol.Cobol85Parser import Cobol85Parser
from grammar.unisys_cobol.CobolUnisysLexer import CobolUnisysLexer
from grammar.unisys_cobol.CobolUnisysParser import CobolUnisysParser


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


def print_tree(ctx: ParserRuleContext, level=0, write_file_path: Optional[str] = None):
    """A debugging function for printing the ANTLR tree.

    Args:
        ctx (ParserRuleContext): The starting node
        level (int, optional): Level for keeping track the indentation, ignore this parameter. Defaults to 0.
        write_file_path (Optional[str], optional): The path to save the tree to file if specified. Defaults to None.
    """
    if write_file_path and level == 0:
        # rewrite the file
        with open(write_file_path, "w") as f:
            f.write("")

    indent = " " * 4
    pad = indent * level

    print(f"{pad}{type(ctx).__name__}   {ctx.getText()}")

    if write_file_path:
        with open(write_file_path, "a") as f:
            f.write(f"{pad}{type(ctx).__name__}   {ctx.getText()}\n")

    if not isinstance(ctx, TerminalNode):
        for child in ctx.getChildren():
            print_tree(child, level + 1, write_file_path)


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
        length = math.ceil(length / 2) + 1 if is_half_int else math.ceil(length / 2)
    elif is_binary_compression_format:
        if length <= 4:
            length = 2
        elif length <= 9:
            length = 4
        elif length <= 18:
            length = 8

    return length


def get_paragraph_section_of_cobol_statement(
    parser: Union[CobolUnisysParser, Cobol85Parser, DNPParser, CopyBookParser],
    ctx: ParserRuleContext,
) -> Dict[str, str]:
    """Get the paragraph and section of a cobol statement.

    Args:
        parser CobolUnisysParser: The ANTLR Parser for the cobol language.
        ctx (ParserRuleContext): The node to start the search from.

    Returns:
       dict[str, str]: Dictionary with paragraph and section of the cobol statement
    """
    res = {}
    paragraph = find_parent_by_type(ctx, parser.ParagraphContext)
    if paragraph:
        paragraph_name = paragraph.paragraphName()
        res["paragraph"] = paragraph_name.getText()
    else:
        res["paragraph"] = None
    procedure_section = find_parent_by_type(ctx, parser.ProcedureSectionContext)
    if procedure_section:
        procedure_section_header = procedure_section.procedureSectionHeader()
        section_name = procedure_section_header.sectionName()
        res["section"] = section_name.getText()
    else:
        res["section"] = None

    return res


def get_original_code_content(parser: Parser, start_index: int, stop_index: int) -> str:
    """Get the code content of the file given the start index and stop index of the tokens.

    Args:
        parser (Parser): The ANTLR Parser
        start_index (int): Start token index
        stop_index (int): Stop token index

    Returns:
        str: The code content from start to stop index.
    """
    token_stream = parser.getTokenStream()
    original_code = token_stream.getText(start_index, stop_index)

    return original_code


def get_original_code_content_without_hidden(parser: Parser, start_index: int, stop_index: int, exclude_token_types=None) -> str:
    """Get the code content of the file given the start index and stop index of the tokens,
    excluding specific token types (like comments).

    Args:
        parser (Parser): The ANTLR Parser
        start_index (int): Start token index
        stop_index (int): Stop token index
        exclude_token_types (list, optional): List of token type indices to exclude. Defaults to None.

    Returns:
        str: The code content from start to stop index without excluded token types.
    """
    token_stream = parser.getTokenStream()
    result = []
    
    # If no specific token types to exclude, default to empty list
    if exclude_token_types is None:
        exclude_token_types = []
    
    for i in range(start_index, stop_index + 1):
        token = token_stream.get(i)
        # Include tokens that are not in the excluded token types list
        if token.type not in exclude_token_types:
            result.append(token.text)
    
    return ''.join(result)


T = TypeVar("T", bound=ParserRuleContext)


def recursive_find_first_child_by_type(
    current: ParserRuleContext, type: Type[T]
) -> Optional[T]:
    """Find the first child inside the ANTLR AST given the parent.

    Args:
        current (ParserRuleContext): The starting node.
        type (Type[T]): The type of the node to be found.

    Returns:
        Optional[T]: The node of the given type if found.
    """
    if isinstance(current, TerminalNode):
        return None

    if isinstance(current, type):
        return current

    for child in current.getChildren():
        match = recursive_find_first_child_by_type(child, type)

        if match:
            return match

    return None


def find_all_children_by_type(current: ParserRuleContext, type: Type[T]) -> List[T]:
    """Find all children of a specific node in the ANTLR AST.

    Args:
        current (ParserRuleContext): The starting node.
        type (Type[T]): The type of node to be found.

    Returns:
        list[T]: List of children of the given type.
    """
    result: list[T] = []

    if isinstance(current, TerminalNode):
        return result

    if isinstance(current, type):
        result.append(current)
    for child in current.getChildren():
        result.extend(find_all_children_by_type(child, type))
    return result


def find_parent_by_type(node: ParserRuleContext, type: Type[T]) -> Optional[T]:
    """Find the parent of a node with a specific type in the ANTLR AST.

    Args:
        node (ParserRuleContext): The node to start the search from.
        type (Type[T]): The type of the parent node to be found.

    Returns:
        Optional[T]:
            The parent node of the given type, if found. Otherwise, returns None.
    """
    current = node

    while True:
        if isinstance(current, type):
            return current

        if current.parentCtx:
            current = current.parentCtx
        else:
            return None
