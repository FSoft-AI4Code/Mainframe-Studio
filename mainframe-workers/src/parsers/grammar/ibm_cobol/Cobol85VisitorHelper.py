from typing import List, Union

from parsers.grammar.common.base_cobol_schemas import (
    CobolVariable,
    CopybookReplace,
    FileControlEntry,
    FileDescriptionEntry,
    ImportedCopybook,
    MultiLayoutProgram,
    MultiLayoutFileDescription,
    MultiLayoutVariable

)
from parsers.grammar.ibm_cobol.Cobol85Parser import Cobol85Parser
from parsers.grammar.utils import (
    calculate_cobol_variable_length,
    get_original_code_content,
    recursive_find_first_child_by_type,
)

from parsers.variable_flow_utils import VariableFlowUtils

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
        name=name.getText() if name else "",
        line_number=ctx.start.line,
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

    data_usage_clause = recursive_find_first_child_by_type(
        ctx, Cobol85Parser.DataUsageClauseContext
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
        ctx, Cobol85Parser.DataOccursClauseContext
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

def generate_multiLayout_file_section(repository_id: str, file_description_list: List[FileDescriptionEntry]) -> List[MultiLayoutFileDescription]:
    file_section: List[MultiLayoutFileDescription] = []
    for file_description in file_description_list:
        variables_01 = [
            variable.name
            for variable in file_description.variables
            if variable.level == "01"
        ]

        copybooks = []
        for copybook in file_description.copybooks:
            first_var_level = VariableFlowUtils.get_copybook_first_var_level(repository_id, {"copybook_name": copybook.copybook_name})
            if first_var_level == 1:
                copybooks.append(copybook.copybook_name)



        if len(variables_01) + len(copybooks) >= 2:
            file_section.append(MultiLayoutFileDescription(
                file_name=file_description.file_name,
                variable_names=variables_01,
                copybook_names=copybooks
            ))

    return file_section

def build_multi_layout_program(
    repository_id: str,
    program_id: str,
    working_storage: List[CobolVariable],
    linkage_section: List[CobolVariable],
    file_section: List[FileDescriptionEntry],
) -> MultiLayoutProgram:
    """Build a multi-layout program structure."""
    multi_layout_program = MultiLayoutProgram(
        name_program=program_id,
        type="COBOL",
        working_storage=[],
        linkage_section=[],
        File_section=[],
    )

    # Process variables
    multi_layout_program.working_storage = find_redefine_variables(working_storage)
    multi_layout_program.linkage_section = find_redefine_variables(linkage_section)
    # Process file section
    multi_layout_program.File_section = generate_multiLayout_file_section(repository_id, file_section)
    return multi_layout_program