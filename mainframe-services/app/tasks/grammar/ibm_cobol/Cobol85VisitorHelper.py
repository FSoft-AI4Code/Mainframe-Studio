from typing import Union

from ..common.base_cobol_schemas import (
    CobolVariable,
    CopybookReplace,
    FileControlEntry,
    FileDescriptionEntry,
    ImportedCopybook,
)
from ..utils import recursive_find_first_child_by_type
from .Cobol85Parser import Cobol85Parser


def extract_cobol_variable(
    ctx: Union[
        Cobol85Parser.DataDescriptionEntryFormat1Context,
        Cobol85Parser.DataDescriptionEntryFormat2Context,
        Cobol85Parser.DataDescriptionEntryFormat3Context,
        Cobol85Parser.DataDescriptionEntryExecSqlContext,
    ],
) -> CobolVariable:
    """Extract the COBOL variable from the statement.

    Args:
        ctx (Union[ Cobol85Parser.DataDescriptionEntryFormat1Context, Cobol85Parser.DataDescriptionEntryFormat2Context, Cobol85Parser.DataDescriptionEntryFormat3Context, Cobol85Parser.DataDescriptionEntryExecSqlContext, ]): The statement context

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
        ctx, Cobol85Parser.PictureStringContext
    )
    if picture_clause:
        variable.picture_clause = picture_clause.getText()

    default_value = recursive_find_first_child_by_type(
        ctx, Cobol85Parser.DataValueIntervalContext
    )
    if default_value:
        variable.default_value = default_value.getText()

    redefine = recursive_find_first_child_by_type(
        ctx, Cobol85Parser.DataRedefinesClauseContext
    )

    if redefine:
        redefine_data_name = redefine.getChild(1)
        variable.redefine = redefine_data_name.getText()

    occur = recursive_find_first_child_by_type(
        ctx, Cobol85Parser.DataOccursClauseContext
    )

    if occur:
        occur = occur.getChild(1)
        variable.occur = int(occur.getText())

    return variable
