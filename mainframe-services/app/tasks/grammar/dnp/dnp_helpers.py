from typing import Union

from app.tasks.grammar.dnp.DNPParser import DNPParser

from ..common.base_cobol_schemas import CobolVariable
from ..utils import recursive_find_first_child_by_type


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

    if redefine:
        redefine_data_name = redefine.getChild(1)
        variable.redefine = redefine_data_name.getText()

    occur = recursive_find_first_child_by_type(ctx, DNPParser.DataOccursClauseContext)

    if occur:
        occur = occur.getChild(1)
        variable.occur = int(occur.getText())

    return variable
