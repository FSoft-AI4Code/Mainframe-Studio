from typing import List, Union

from parsers.grammar.common.base_cobol_schemas import (
    CobolVariable,
    MultiLayoutProgram,
    MultiLayoutVariable
)
from parsers.grammar.copybook.CopyBookParser import CopyBookParser
from parsers.grammar.utils import (
    calculate_cobol_variable_length,
    get_original_code_content,
    recursive_find_first_child_by_type,
)

from loguru import logger
from parsers.variable_flow_utils import VariableFlowUtils

def extract_cobol_variable(
    ctx: Union[
        CopyBookParser.DataDescriptionEntryFormat1Context,
        CopyBookParser.DataDescriptionEntryFormat2Context,
        CopyBookParser.DataDescriptionEntryFormat3Context,
    ],
) -> CobolVariable:
    """Extract the COBOL variable from the statement.

    Args:
        ctx (Union[ CopyBookParser.DataDescriptionEntryFormat1Context, CopyBookParser.DataDescriptionEntryFormat2Context, CopyBookParser.DataDescriptionEntryFormat3Context, CopyBookParser.DataDescriptionEntryExecSqlContext, ]): The statement context

    Returns:
        CobolVariable: The COBOL variable
    """
    level = ctx.getChild(0)
    name = ctx.getChild(1)

    variable = CobolVariable(
        level=level.getText(),
        name=name.getText() if name else "",
        line_number=ctx.start.line,
    )

    picture_clause = recursive_find_first_child_by_type(
        ctx, CopyBookParser.PictureStringContext
    )
    if picture_clause:
        variable.picture_clause = picture_clause.getText()

    default_value = recursive_find_first_child_by_type(
        ctx, CopyBookParser.DataValueIntervalContext
    )
    if default_value:
        variable.default_value = default_value.getText()

    redefine = recursive_find_first_child_by_type(
        ctx, CopyBookParser.DataRedefinesClauseContext
    )

    if redefine:
        redefine_data_name = redefine.getChild(1)
        variable.redefine = redefine_data_name.getText()

    data_usage_clause = recursive_find_first_child_by_type(
        ctx, CopyBookParser.DataUsageClauseContext
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

    occur = recursive_find_first_child_by_type(
        ctx, CopyBookParser.DataOccursClauseContext
    )

    if occur:
        occur = occur.getChild(1)
        try:
            variable.occur = int(occur.getText())
        except ValueError:
            variable.occur = None

    return variable

def find_redefine_variables(variables: List[CobolVariable]) -> List[MultiLayoutVariable]:
    redefined_variables: List[MultiLayoutVariable] = []

    for variable in variables:
        if variable.redefine:
            existing_variable = next(
                (rv for rv in redefined_variables if rv.redefined_variableName == variable.redefine),
                None
            )
            if existing_variable:
                existing_variable.redefining_variableNames.append(variable.name)
            else:
                redefined_variable = MultiLayoutVariable(
                    redefined_variableName=variable.redefine,
                    redefining_variableNames=[variable.name]
                )
                redefined_variables.append(redefined_variable)
    return redefined_variables


def build_multi_layout_program(
    program_id: str,
    working_storage: List[CobolVariable],
    linkage_section: List[CobolVariable]
) -> MultiLayoutProgram:
    """Build a multi-layout program structure."""
    multi_layout_program = MultiLayoutProgram(
        name_program=program_id,
        type="COPY",
        working_storage=[],
        linkage_section=[],
        File_section=[],
    )

    # Process variables
    multi_layout_program.working_storage = find_redefine_variables(working_storage)
    multi_layout_program.linkage_section = find_redefine_variables(linkage_section)
    return multi_layout_program