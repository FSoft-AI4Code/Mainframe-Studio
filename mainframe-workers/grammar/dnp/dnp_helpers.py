from typing import Union

from grammar.common.base_cobol_schemas import CobolVariable
from grammar.dnp.DNPParser import DNPParser
from grammar.utils import (
    calculate_cobol_variable_length,
    get_original_code_content,
    recursive_find_first_child_by_type,
)


def extract_cobol_variable(
    ctx: Union[
        DNPParser.DataDescriptionEntryFormat1Context,
        DNPParser.DataDescriptionEntryFormat2Context,
        DNPParser.DataDescriptionEntryFormat3Context,
        DNPParser.DataDescriptionEntryExecSqlContext,
    ],
) -> CobolVariable:
    """Extract the COBOL variable from the statement.

    Args:
        ctx (Union[ DNPParser.DataDescriptionEntryFormat1Context, DNPParser.DataDescriptionEntryFormat2Context, DNPParser.DataDescriptionEntryFormat3Context, DNPParser.DataDescriptionEntryExecSqlContext, ]): Data description context

    Returns:
        CobolVariable: The COBOL variable
    """
    level = ctx.getChild(0)
    name = ctx.getChild(1)

    variable = CobolVariable(
        level=level.getText(),
        name=name.getText(),
        line_number=ctx.start.line,
    )

    picture_clause = recursive_find_first_child_by_type(
        ctx, DNPParser.PictureStringContext
    )
    if picture_clause:
        variable.picture_clause = picture_clause.getText()

    default_value = recursive_find_first_child_by_type(
        ctx, DNPParser.DataValueIntervalContext
    )
    if default_value:
        variable.default_value = default_value.getText()

    redefine = recursive_find_first_child_by_type(
        ctx, DNPParser.DataRedefinesClauseContext
    )

    data_usage_clause = recursive_find_first_child_by_type(
        ctx, DNPParser.DataUsageClauseContext
    )

    compression_format = None
    if data_usage_clause:
        compression_format = get_original_code_content(
            ctx.parser,
            data_usage_clause.start.tokenIndex,
            data_usage_clause.stop.tokenIndex,
        )
    variable.compression_format = compression_format

    length = (
        calculate_cobol_variable_length(variable.picture_clause, compression_format)
        if variable.picture_clause
        else None
    )
    variable.length = length

    if redefine:
        redefine_data_name = redefine.getChild(1)
        variable.redefine = redefine_data_name.getText()

    occur = recursive_find_first_child_by_type(ctx, DNPParser.DataOccursClauseContext)

    if occur:
        occur = occur.getChild(1)
        try:
            variable.occur = int(occur.getText())
        except ValueError:
            variable.occur = None

    return variable
