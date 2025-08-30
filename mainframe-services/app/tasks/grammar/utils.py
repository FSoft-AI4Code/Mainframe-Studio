from typing import Optional, Type, TypeVar, Union

from antlr4 import Parser, ParserRuleContext, TerminalNode

from app.tasks.grammar.dnp.DNPParser import DNPParser
from app.tasks.grammar.ibm_cobol.Cobol85Parser import Cobol85Parser
from app.tasks.grammar.unisys_cobol.CobolUnisysParser import CobolUnisysParser


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


def get_paragraph_section_of_cobol_statement(
    parser: Union[CobolUnisysParser, Cobol85Parser, DNPParser], ctx: ParserRuleContext
) -> dict[str, str]:
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


def find_all_children_by_type(current: ParserRuleContext, type: Type[T]) -> list[T]:
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
