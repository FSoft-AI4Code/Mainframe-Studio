from typing import List, Optional, Union

from antlr4 import TerminalNode

from parsers.grammar.common.base_cobol_schemas import (
    CalledProgram,
    CobolProgramVariables,
    CobolVariable,
    CopybookReplace,
    DatabaseTable,
    Division,
    FileControlEntry,
    FileDescriptionEntry,
    ImportedCopybook,
    Paragraph,
    ProcedureSection,
)
from parsers.grammar.isuzu_cobol.CobolIsuzuParser import CobolIsuzuParser
from parsers.grammar.isuzu_cobol.CobolIsuzuVisitor import CobolIsuzuVisitor
from parsers.grammar.utils import (
    calculate_cobol_variable_length,
    find_all_children_by_type,
    find_parent_by_type,
    get_original_code_content,
    get_paragraph_section_of_cobol_statement,
    recursive_find_first_child_by_type,
)


# Custom Visitor for Collecting COBOL Program Information
class CobolIsuzuVisitorImp(CobolIsuzuVisitor):

    # Initialization Method
    def __init__(self, parser: CobolIsuzuParser):

        self.parser = parser

        self.program_id = ""
        self.copybook_list: list[ImportedCopybook] = []
        self.called_program_list: list[CalledProgram] = []
        self.file_control_list: list[FileControlEntry] = []
        self.file_description_list: list[FileDescriptionEntry] = []
        self.variable_list = CobolProgramVariables(
            working_storage=[], linkage_section=[]
        )
        self.division_list: List[Division] = []
        self.section_list: list[ProcedureSection] = []
        self.paragraph_list: list[Paragraph] = []
        self.statements = []
        self.database_list: List[DatabaseTable] = []

        self.func = {
            "AcceptStatement": self.assessAcceptStatement,
            "AcceptFromEscapeKeyStatement": self.assessAcceptFromEscapeKeyStatement,
            "AcceptFromMnemonicStatement": self.assessAcceptFromMnemonicStatement,
            "AcceptFromMessageCountStatement": self.assessAcceptFromMessageCountStatement,
            "EvaluateStatementContext": self.assessEvaluateStatement,
            "AddStatementContext": self.assessAddStatement,
            "AlterStatementContext": self.assessAlterStatement,
            "CloseStatementContext": self.assessCloseStatement,
            "ComputeStatementContext": self.assessComputeStatement,
            "ContinueStatementContext": self.assessContinueStatement,
            "CopyStatementContext": self.assessCopyStatement,
            "DisplayStatementContext": self.assessDisplayStatement,
            "ExitStatementContext": self.assessExitStatement,
            "FindStatementContext": self.assessFindStatement,
            "GobackStatementContext": self.assessGobackStatement,
            "GoToStatementContext": self.assessGoToStatement,
            "InitializeStatementContext": self.assessInitializeStatement,
            "InspectStatementContext": self.assessInspectStatement,
            "MoveStatementContext": self.assessMoveStatement,
            "ModifyStatementContext": self.assessModifyStatement,
            "SearchStatementContext": self.assessSearchStatement,
            "StringStatementContext": self.assessStringStatement,
            "SubtractStatementContext": self.assessSubtractStatement,
            "SetStatementContext": self.assessSetStatement,
            "WriteStatementContext": self.assessWriteStatement,
            "OpenStatementContext": self.assessOpenStatement,
            "IfStatementContext": self.assessIfStatement,
            "PerformStatementContext": self.assessPerformStatement,
            "ReadStatementContext": self.assessReadStatement,
            "RewriteStatementContext": self.assessRewriteStatement,
            # Other Statements
        }

    # Helper Methods

    def extract_cobol_variable(
        self,
        ctx: Union[
            CobolIsuzuParser.DataDescriptionEntryFormat1Context,
            CobolIsuzuParser.DataDescriptionEntryFormat2Context,
            CobolIsuzuParser.DataDescriptionEntryFormat3Context,
            CobolIsuzuParser.DataDescriptionEntryExecSqlContext,
        ],
    ) -> CobolVariable:
        """Extract the COBOL variable from the statement.

        Args:
            ctx (Union[ CobolIsuzuParser.DataDescriptionEntryFormat1Context, CobolIsuzuParser.DataDescriptionEntryFormat2Context, CobolIsuzuParser.DataDescriptionEntryFormat3Context, CobolIsuzuParser.DataDescriptionEntryExecSqlContext, ]): Data description context

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
            ctx, CobolIsuzuParser.PictureStringContext
        )
        if picture_clause:
            variable.picture_clause = picture_clause.getText()

        default_value = recursive_find_first_child_by_type(
            ctx, CobolIsuzuParser.DataValueIntervalContext
        )
        if default_value:
            variable.default_value = default_value.getText()

        redefine = recursive_find_first_child_by_type(
            ctx, CobolIsuzuParser.DataRedefinesClauseContext
        )

        data_usage_clause = recursive_find_first_child_by_type(
            ctx, CobolIsuzuParser.DataUsageClauseContext
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

        occur = recursive_find_first_child_by_type(
            ctx, CobolIsuzuParser.DataOccursClauseContext
        )

        if occur:
            occur = occur.getChild(1)
            variable.occur = int(occur.getText())

        return variable

    def extract_inspect_replacing_phrase(
        self, inspect_phrase: CobolIsuzuParser.InspectReplacingPhraseContext
    ):
        inspect_replacing_phrase_dict = {"replacements": []}

        for child in inspect_phrase.getChildren():
            if isinstance(child, CobolIsuzuParser.InspectReplacingCharactersContext):
                inspect_by = child.inspectBy()
                identifier = inspect_by.identifier()
                literal = inspect_by.literal() or inspect_by.figurativeConstant()
                inspect_replacing_characters_dict = {"by": None, "before_after": []}
                inspect_replacing_phrase_dict["replacements"].append(
                    inspect_replacing_characters_dict
                )

                inspect_by_dict = {
                    "by_identifier": identifier.getText() if identifier else None,
                    "by_literal": literal.getText() if literal else None,
                }

                inspect_replacing_characters_dict["by"] = inspect_by_dict

                inspect_before_after_list = child.inspectBeforeAfter()

                for inspect_before_after in inspect_before_after_list:
                    inspect_before_after_dict = self.extract_inspect_before_after(
                        inspect_before_after
                    )

                    inspect_replacing_characters_dict["before_after"].append(
                        inspect_before_after_dict
                    )
            elif isinstance(child, CobolIsuzuParser.InspectReplacingAllLeadingsContext):
                leading_type = child.getChild(0).getText().upper()
                inspect_replacing_all_leadings_dict = {
                    "leading_type": leading_type,
                    "replacements": [],
                }
                inspect_replacing_phrase_dict["replacements"].append(
                    inspect_replacing_all_leadings_dict
                )

                inspect_replacing_all_leading_list: List[
                    CobolIsuzuParser.InspectReplacingAllLeadingContext
                ] = child.inspectReplacingAllLeading()
                for inspect_replacing_all_leading in inspect_replacing_all_leading_list:
                    replacing_identifier = inspect_replacing_all_leading.identifier()
                    replacing_literal = (
                        inspect_replacing_all_leading.literal()
                        or inspect_replacing_all_leading.figurativeConstant()
                    )

                    inspect_replacing_all_leading_dict = {
                        "replacing_identifier": (
                            replacing_identifier.getText()
                            if replacing_identifier
                            else None
                        ),
                        "replacing_literal": (
                            replacing_literal.getText() if replacing_literal else None
                        ),
                        "inspect_by": [],
                        "before_after": [],
                    }
                    inspect_replacing_all_leadings_dict["replacements"].append(
                        inspect_replacing_all_leading_dict
                    )

                    inspect_by_list = inspect_replacing_all_leading.inspectBy()
                    for inspect_by in inspect_by_list:
                        by_identifier = inspect_by.identifier()
                        by_literal = (
                            inspect_by.literal() or inspect_by.figurativeConstant()
                        )

                        inspect_by_dict = {
                            "by_identifier": (
                                by_identifier.getText() if by_identifier else None
                            ),
                            "by_literal": (
                                by_literal.getText() if by_literal else None
                            ),
                        }

                        inspect_replacing_all_leading_dict["inspect_by"].append(
                            inspect_by_dict
                        )

                    inspect_before_after_list = (
                        inspect_replacing_all_leading.inspectBeforeAfter()
                    )
                    for inspect_before_after in inspect_before_after_list:
                        inspect_before_after_dict = self.extract_inspect_before_after(
                            inspect_before_after
                        )

                        inspect_replacing_all_leading_dict["before_after"].append(
                            inspect_before_after_dict
                        )
        return inspect_replacing_phrase_dict

    def extract_inspect_tallying(
        self, inspect_tallying: CobolIsuzuParser.InspectTallyingPhraseContext
    ):
        inspect_tallying_phrase_dict = {"tallying": []}
        inspect_for_list: List[CobolIsuzuParser.InspectForContext] = (
            inspect_tallying.inspectFor()
        )

        for inspect_for in inspect_for_list:
            inspect_for_dict = self.extract_inspect_for(inspect_for)
            inspect_tallying_phrase_dict["tallying"].append(inspect_for_dict)

        return inspect_tallying_phrase_dict

    def extract_inspect_for(self, inspect_for: CobolIsuzuParser.InspectForContext):
        identifier = inspect_for.identifier()
        inspect_for_dict = {
            "identifier": identifier.getText(),
            "for_targets": [],
        }

        for child in inspect_for.getChildren():
            if isinstance(child, CobolIsuzuParser.InspectCharactersContext):
                inspect_characters_dict = {"before_after": []}
                inspect_for_dict["for_targets"].append(inspect_characters_dict)

                inspect_before_after_list = child.inspectBeforeAfter()
                for inspect_before_after in inspect_before_after_list:
                    inspect_before_after_dict = self.extract_inspect_before_after(
                        inspect_before_after
                    )

                    inspect_characters_dict["before_after"].append(
                        inspect_before_after_dict
                    )
            elif isinstance(child, CobolIsuzuParser.InspectAllLeadingsContext):
                leading_type = child.getChild(0).getText().upper()
                inspect_all_leadings_dict = {
                    "leading_type": leading_type,
                    "inspect_all_leading": [],
                }
                inspect_for_dict["for_targets"].append(inspect_all_leadings_dict)

                inspect_all_leading_list: List[
                    CobolIsuzuParser.InspectAllLeadingContext
                ] = child.inspectAllLeading()

                for inspect_all_leading in inspect_all_leading_list:
                    inspect_all_leading_dict = {
                        "identifier": None,
                        "literal": None,
                        "before_after": [],
                    }
                    inspect_all_leadings_dict["inspect_all_leading"].append(
                        inspect_all_leading_dict
                    )

                    identifier = inspect_all_leading.identifier()
                    literal = inspect_all_leading.literal()

                    inspect_all_leading_dict["identifier"] = (
                        identifier.getText() if identifier else None
                    )
                    inspect_all_leading_dict["literal"] = (
                        literal.getText() if literal else None
                    )

                    inspect_before_after_list = inspect_all_leading.inspectBeforeAfter()
                    for inspect_before_after in inspect_before_after_list:
                        inspect_before_after_dict = self.extract_inspect_before_after(
                            inspect_before_after
                        )

                        inspect_all_leading_dict["before_after"].append(
                            inspect_before_after_dict
                        )

        return inspect_for_dict

    def extract_inspect_before_after(
        self, inspect_before_after: CobolIsuzuParser.InspectBeforeAfterContext
    ):
        position = inspect_before_after.getChild(0).getText().upper()
        replacing_identifier = inspect_before_after.identifier()
        replacing_literal = inspect_before_after.literal()

        inspect_before_after_dict = {
            "position": position,
            "replacing_identifier": (
                replacing_identifier.getText() if replacing_identifier else None
            ),
            "replacing_literal": (
                replacing_literal.getText() if replacing_literal else None
            ),
        }

        return inspect_before_after_dict

    def extract_inspect_converting_phrase(
        self,
        inspect_converting_phrase: CobolIsuzuParser.InspectConvertingPhraseContext,
    ):
        inspect_converting_phrase_dict = {
            "converting_from_identifier": None,
            "converting_from_literal": None,
            "to": None,
            "before_after": [],
        }

        identifier = inspect_converting_phrase.identifier()
        inspect_converting_phrase_dict["converting_from_identifier"] = (
            identifier.getText() if identifier else None
        )

        literal = inspect_converting_phrase.literal()
        inspect_converting_phrase_dict["converting_from_literal"] = (
            literal.getText() if literal else None
        )

        inspect_to = inspect_converting_phrase.inspectTo()
        inspect_to_identifier = inspect_to.identifier()
        inspect_to_literal = inspect_to.literal()
        inspect_to_dict = {
            "to_identifier": (
                inspect_to_identifier.getText() if inspect_to_identifier else None
            ),
            "to_literal": inspect_to_literal.getText() if inspect_to_literal else None,
        }
        inspect_converting_phrase_dict["to"] = inspect_to_dict

        inspect_before_after_list = inspect_converting_phrase.inspectBeforeAfter()

        for inspect_before_after in inspect_before_after_list:
            inspect_before_after_dict = self.extract_inspect_before_after(
                inspect_before_after
            )
            inspect_converting_phrase_dict["before_after"].append(
                inspect_before_after_dict
            )

        return inspect_converting_phrase_dict

    # Custom visit Methods and Their Corresponding Access Methods

    # SECTION LIST

    def visitProcedureSection(self, ctx: CobolIsuzuParser.ProcedureSectionContext):
        procedure_section_header = ctx.procedureSectionHeader()

        section_name = procedure_section_header.sectionName()

        self.section_list.append(
            ProcedureSection(
                section_name=section_name.getText(),
                start_line=ctx.start.line,
                stop_line=ctx.stop.line,
                paragraph_name_list=[],
            )
        )

        return self.visitChildren(ctx)

    def visitParagraph(self, ctx: CobolIsuzuParser.ParagraphContext):
        paragraph_name = ctx.getChild(0)
        start_line = ctx.start.line
        end_line = ctx.stop.line

        code_content = get_original_code_content(
            self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex
        )

        procedure_section = find_parent_by_type(
            ctx, self.parser.ProcedureSectionContext
        )
        section = None
        if procedure_section:
            procedure_section_header = procedure_section.procedureSectionHeader()
            section_name = procedure_section_header.sectionName()
            section = section_name.getText()

        paragraph = Paragraph(
            paragraph_name=paragraph_name.getText(),
            section=section,
            paragraph_code=code_content,
            paragraph_lines=[start_line, end_line],
        )

        self.paragraph_list.append(paragraph)

        for procedure_section in self.section_list:
            if procedure_section.section_name == section:
                procedure_section.paragraph_name_list.append(paragraph_name.getText())
                break

        return self.visitChildren(ctx)

    # DIVISION LIST

    def visitIdentificationDivision(
        self, ctx: CobolIsuzuParser.IdentificationDivisionContext
    ):
        self.division_list.append(
            Division(
                division_name="IDENTIFICATION DIVISION",
                start_line=ctx.start.line,
                stop_line=ctx.stop.line,
            )
        )
        return self.visitChildren(ctx)

    def visitEnvironmentDivision(
        self, ctx: CobolIsuzuParser.EnvironmentDivisionContext
    ):
        self.division_list.append(
            Division(
                division_name="ENVIRONMENT DIVISION",
                start_line=ctx.start.line,
                stop_line=ctx.stop.line,
            )
        )
        return self.visitChildren(ctx)

    def visitDataDivision(self, ctx: CobolIsuzuParser.DataDivisionContext):
        self.division_list.append(
            Division(
                division_name="DATA DIVISION",
                start_line=ctx.start.line,
                stop_line=ctx.stop.line,
            )
        )
        return self.visitChildren(ctx)

    def visitProcedureDivision(self, ctx: CobolIsuzuParser.ProcedureDivisionContext):
        self.division_list.append(
            Division(
                division_name="PROCEDURE DIVISION",
                start_line=ctx.start.line,
                stop_line=ctx.stop.line,
            )
        )
        return self.visitChildren(ctx)

    # VARIABLE LIST

    def visitWorkingStorageSection(
        self, ctx: CobolIsuzuParser.WorkingStorageSectionContext
    ):
        data_description_entry_list: List[
            CobolIsuzuParser.DataDescriptionEntryContext
        ] = ctx.dataDescriptionEntry()

        for data_description_entry in data_description_entry_list:
            if isinstance(
                data_description_entry.getChild(0),
                CobolIsuzuParser.CopyStatementContext,
            ):
                continue

            variable = self.extract_cobol_variable(data_description_entry.getChild(0))
            self.variable_list.working_storage.append(variable)

        return self.visitChildren(ctx)

    def visitLinkageSection(self, ctx: CobolIsuzuParser.LinkageSectionContext):
        data_description_entry_list: List[
            CobolIsuzuParser.DataDescriptionEntryContext
        ] = ctx.dataDescriptionEntry()

        for data_description_entry in data_description_entry_list:
            if isinstance(
                data_description_entry.getChild(0),
                CobolIsuzuParser.CopyStatementContext,
            ):
                continue
            variable = self.extract_cobol_variable(data_description_entry.getChild(0))
            self.variable_list.linkage_section.append(variable)
        return self.visitChildren(ctx)

    # FILE DESCRIPTION LIST

    def visitFileDescriptionEntry(
        self, ctx: CobolIsuzuParser.FileDescriptionEntryContext
    ):
        code_content = get_original_code_content(
            self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex
        )

        file_name = recursive_find_first_child_by_type(
            ctx, CobolIsuzuParser.FileNameContext
        )

        if file_name is None:
            raise ValueError(
                f"File name is missing for FD statement {get_original_code_content(self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)}"
            )

        data_description_entries = find_all_children_by_type(
            ctx, CobolIsuzuParser.DataDescriptionEntryContext
        )

        variables = []
        copybooks = []

        for entry in data_description_entries:
            entry = entry.getChild(0)

            # copy statement
            if isinstance(entry, CobolIsuzuParser.CopyStatementContext):
                copy_source = recursive_find_first_child_by_type(
                    ctx, CobolIsuzuParser.CopySourceContext
                )

                if copy_source is None:
                    raise ValueError(
                        f"File name of COPY statement {get_original_code_content(self.parser, entry.start.tokenIndex, entry.stop.tokenIndex)}"
                    )

                copy_name = copy_source.getChild(0)

                replace_clauses = find_all_children_by_type(
                    entry, CobolIsuzuParser.ReplaceClauseContext
                )

                replace_list = []

                for replace_clause in replace_clauses:
                    replaceable = replace_clause.getChild(0)
                    replacement = replace_clause.getChild(2)

                    replace = CopybookReplace(
                        replaceable=replaceable.getText(),
                        replacement=replacement.getText(),
                    )
                    replace_list.append(replace)

                copybook = ImportedCopybook(
                    copybook_name=copy_name.getText(),
                    line_number=copy_source.start.line,
                    replacing=replace_list,
                )

                copybooks.append(copybook)
                continue

            # variable definition
            variable = self.extract_cobol_variable(entry)

            variables.append(variable)

        fd = FileDescriptionEntry(
            file_name=file_name.getText(),
            code_content=code_content,
            variables=variables,
            copybooks=copybooks,
        )

        self.file_description_list.append(fd)
        return self.visitChildren(ctx)

    # FILE CONTROL LIST

    def visitFileControlEntry(self, ctx: CobolIsuzuParser.FileControlEntryContext):
        select_clause = recursive_find_first_child_by_type(
            ctx, CobolIsuzuParser.SelectClauseContext
        )

        if select_clause is None:
            raise ValueError(
                f"Select clause of statement '{ctx.getText()}' is missing."
            )

        file_name = recursive_find_first_child_by_type(
            select_clause, CobolIsuzuParser.FileNameContext
        )

        if file_name is None:
            raise ValueError(
                f"File name in select clause of statement'{ctx.getText()}' is missing."
            )

        file_control_clause_list: List[CobolIsuzuParser.FileControlClauseContext] = (
            ctx.fileControlClause()
        )

        assignment_name = None
        for file_control_clause in file_control_clause_list:
            assign_clause: CobolIsuzuParser.AssignClauseContext = (
                file_control_clause.assignClause()
            )

            if assign_clause:
                # get the last child, 'TO' in assign clause is optional
                assignment_name = (
                    assign_clause.getChild(2)
                    if assign_clause.getChildCount() == 3
                    else assign_clause.getChild(1)
                )

        if assignment_name is None:
            # raise ValueError(
            #     f"Assignment name in select clause of statement'{ctx.getText()}' is missing."
            # )
            assignment_name = ""
        else:
            assignment_name = assignment_name.getText()

        access_mode_clause = recursive_find_first_child_by_type(
            ctx, CobolIsuzuParser.AccessModeClauseContext
        )
        organization_clause = recursive_find_first_child_by_type(
            ctx, CobolIsuzuParser.OrganizationClauseContext
        )

        access_mode = "SEQUENTIAL"  # default value
        if access_mode_clause:
            access_mode = (
                access_mode_clause.SEQUENTIAL()
                or access_mode_clause.RANDOM()
                or access_mode_clause.DYNAMIC()
                or access_mode_clause.EXCLUSIVE()
            )
            access_mode = access_mode.getText()
        else:
            if organization_clause:
                organization_type = (
                    organization_clause.SEQUENTIAL()
                    or organization_clause.RELATIVE()
                    or organization_clause.INDEXED()
                )
                organization_type_text = organization_type.getText()

                match organization_type_text:
                    case "SEQUENTIAL":
                        access_mode = "SEQUENTIAL"
                    case "RELATIVE":
                        access_mode = "RANDOM"
                    case "INDEXED":
                        access_mode = "DYNAMIC"

        file_control = FileControlEntry(
            file_name=file_name.getText(),
            assignment_name=assignment_name,
            code_content=get_original_code_content(
                self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex
            ),
            open_type="",
            access_mode=access_mode,
        )

        self.file_control_list.append(file_control)
        return self.visitChildren(ctx)

    def visitDataBaseSectionEntry(
        self, ctx: CobolIsuzuParser.DataBaseSectionEntryContext
    ):
        database_name = get_original_code_content(
            self.parser,
            ctx.getChild(1).start.tokenIndex,
            ctx.getChild(1).stop.tokenIndex,
        )

        invoke_name = get_original_code_content(
            self.parser,
            ctx.getChild(3).start.tokenIndex,
            ctx.getChild(3).stop.tokenIndex,
        )

        self.database_list.append(
            DatabaseTable(
                table_name=database_name,
                invoke_name=invoke_name,
                using_names=[],
            )
        )
        return self.visitChildren(ctx)

    def visitOpenInputStatement(self, ctx: CobolIsuzuParser.OpenInputStatementContext):
        open_input_list: List[CobolIsuzuParser.OpenInputContext] = ctx.openInput()
        for open_input in open_input_list:
            file_control_name = recursive_find_first_child_by_type(
                open_input, CobolIsuzuParser.FileNameContext
            )

            if file_control_name is None:
                raise ValueError(
                    f"Missing file name in OPEN statement {get_original_code_content(self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)}"
                )

            for file_control in self.file_control_list:
                if file_control.file_name == file_control_name.getText():
                    file_control.open_type = "INPUT"
        return self.visitChildren(ctx)

    def visitOpenOutputStatement(
        self, ctx: CobolIsuzuParser.OpenOutputStatementContext
    ):

        open_output_list: List[CobolIsuzuParser.OpenOutputContext] = ctx.openOutput()

        for open_output in open_output_list:
            file_control_name = recursive_find_first_child_by_type(
                open_output, CobolIsuzuParser.FileNameContext
            )

            if file_control_name is None:
                raise ValueError(
                    f"Missing file name in OPEN statement {get_original_code_content(self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)}"
                )

            for file_control in self.file_control_list:
                if file_control.file_name == file_control_name.getText():
                    file_control.open_type = "OUTPUT"
        return self.visitChildren(ctx)

    def visitOpenIOStatement(self, ctx: CobolIsuzuParser.OpenIOStatementContext):
        file_name_list: List[CobolIsuzuParser.FileNameContext] = ctx.fileName()

        for file_name in file_name_list:
            file_control_name = recursive_find_first_child_by_type(
                file_name, CobolIsuzuParser.FileNameContext
            )

            if file_control_name is None:
                raise ValueError(
                    f"Missing file name in OPEN statement {get_original_code_content(self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)}"
                )

            for file_control in self.file_control_list:
                if file_control.file_name == file_control_name.getText():
                    file_control.open_type = "I-O"
        return self.visitChildren(ctx)

    def visitOpenExtendStatement(
        self, ctx: CobolIsuzuParser.OpenExtendStatementContext
    ):
        file_name_list: List[CobolIsuzuParser.FileNameContext] = ctx.fileName()

        for file_name in file_name_list:
            file_control_name = recursive_find_first_child_by_type(
                file_name, CobolIsuzuParser.FileNameContext
            )

            if file_control_name is None:
                raise ValueError(
                    f"Missing file name in OPEN statement {get_original_code_content(self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)}"
                )

            for file_control in self.file_control_list:
                if file_control.file_name == file_control_name.getText():
                    file_control.open_type = "EXTEND"
        return self.visitChildren(ctx)

    # STATEMENTS LIST

    def assessEvaluateStatement(self, ctx: CobolIsuzuParser.EvaluateStatementContext):
        # Intialize
        tag = "EvaluateStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )

        evaluate_select: CobolIsuzuParser.EvaluateSelectContext = ctx.evaluateSelect()

        if evaluate_select.identifier():
            res["evaluate_identifier"] = evaluate_select.identifier().getText()
        elif (
            evaluate_select.literal()
            or evaluate_select.TRUE()
            or evaluate_select.FALSE()
        ):
            res["evaluate_literal"] = get_original_code_content(
                self.parser,
                evaluate_select.start.tokenIndex,
                evaluate_select.stop.tokenIndex,
            )

        # evaluateSelect
        evaluateSelect = ctx.evaluateSelect()
        if evaluateSelect:
            res["evaluateSelect"] = evaluateSelect.getText()

        # evaluateAlsoSelect
        evaluateAlsoSelect = ctx.evaluateAlsoSelect()
        if evaluateAlsoSelect:
            res["evaluateAlsoSelect"] = []
            for eas in evaluateAlsoSelect:
                evaluateSelect = eas.evaluateSelect()
                res["evaluateAlsoSelect"].append(evaluateSelect.getText())

        # evaluateWhenPhrase
        evaluateWhenPhrase = ctx.evaluateWhenPhrase()
        if evaluateWhenPhrase:
            res["evaluateWhenPhrase"] = []
            for ewp in evaluateWhenPhrase:
                r = {}
                # evaluateWhen
                evaluateWhen = ewp.evaluateWhen()
                if evaluateWhen:
                    r["evaluateWhen"] = []
                    for ew in evaluateWhen:
                        start_idx = ew.start.tokenIndex
                        stop_idx = ew.stop.tokenIndex
                        evaluateCondition = ew.evaluateCondition()
                        # r["evaluateWhen"].append(self.code[start_idx:stop_idx+1])
                        r["evaluateWhen"].append(evaluateCondition.getText())

                # statement
                statement = ewp.statement()
                if statement:
                    r["statement"] = []
                    for st in statement:
                        start_idx = st.start.tokenIndex
                        stop_idx = st.stop.tokenIndex
                        c = st.getChild(0)
                        type_ = type(c).__name__
                        if type_ in self.func:
                            f = self.func[type_]
                            r["statement"].append(f(c))
                        # else:
                        #     r["statement"].append(
                        #         get_original_code_content(
                        #             self.parser, start_idx, stop_idx
                        #         )
                        #     )
                # Update
                res["evaluateWhenPhrase"].append(r)

        # evaluateWhenOther
        evaluateWhenOther = ctx.evaluateWhenOther()
        if evaluateWhenOther:
            res["evaluateWhenOther"] = []

        return res

    def visitEvaluateStatement(self, ctx: CobolIsuzuParser.EvaluateStatementContext):
        res = self.assessEvaluateStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolIsuzuParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessModifyStatement(self, ctx: CobolIsuzuParser.ModifyStatementContext):
        tag = "ModifyStatement"
        res = {}

        start_token = ctx.start
        stop_token = ctx.stop

        res["tag"] = tag
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )

        identifier = ctx.identifier()
        if identifier:
            res["identifier"] = identifier.getText()

        literal = ctx.literal()
        if literal:
            res["literal"] = literal.getText()

        return res

    def visitModifyStatement(self, ctx: CobolIsuzuParser.ModifyStatementContext):
        res = self.assessModifyStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolIsuzuParser.SentenceContext):
            self.statements.append(res)

        return super().visitModifyStatement(ctx)

    def assessCloseStatement(self, ctx: CobolIsuzuParser.CloseStatementContext):
        # Intialize
        tag = "CloseStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        # closeFile
        res["close_files"] = []
        close_phrases = ctx.closePhrase()

        for close_phrase in close_phrases:
            close_file_details = {}

            close_file = close_phrase.closeFile()

            file_name = close_file.fileName()
            close_file_details["file_name"] = file_name.getText()

            close_option = (
                close_phrase.SAVE()
                or close_phrase.PURGE()
                or close_phrase.RELEASE()
                or close_phrase.CRUNCH()
            )
            close_file_details["close_option"] = (
                close_option.getText() if close_option else None
            )

            close_file_details["on_exception_clause"] = []
            on_exception_clause = close_file.onExceptionClause()
            if on_exception_clause:
                statements = on_exception_clause.statement()
                for statement in statements:
                    child = statement.getChild(0)
                    type_ = type(child).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        close_file_details["on_exception_clause"].append(f(child))

            res["close_files"].append(close_file_details)

        return res

    def visitCloseStatement(self, ctx: CobolIsuzuParser.CloseStatementContext):
        res = self.assessCloseStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolIsuzuParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessFindStatement(self, ctx: CobolIsuzuParser.FindStatementContext):
        tag = "FindStatement"
        res = {}

        start_token = ctx.start
        stop_token = ctx.stop

        res["tag"] = tag
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )

        find_options = ctx.findOption()
        res["find_option"] = []

        if find_options:
            for find_option in find_options:
                res["find_option"].append(find_option.getText().upper())

        record_name = ctx.identifier()
        if record_name:
            res["record_name"] = record_name.getText()

        via_clause = ctx.viaClause()

        if via_clause:
            via_find_option = via_clause.findOption()
            via_identifier = via_clause.identifier()

            res["via_find_option"] = (
                via_find_option.getText().upper() if via_find_option else None
            )
            res["via_identifier"] = via_identifier.getText()

        condition = ctx.condition()
        if condition:
            res["condition"] = get_original_code_content(
                self.parser, condition.start.tokenIndex, condition.stop.tokenIndex
            )

        res["on_exception_clause"] = []
        on_exception_clause = ctx.onExceptionClause()
        if on_exception_clause:
            statements = on_exception_clause.statement()
            for statement in statements:
                child = statement.getChild(0)
                type_ = type(child).__name__
                if type_ in self.func:
                    f = self.func[type_]
                    res["on_exception_clause"].append(f(child))

        return res

    def visitFindStatement(self, ctx: CobolIsuzuParser.FindStatementContext):
        res = self.assessFindStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolIsuzuParser.SentenceContext):
            self.statements.append(res)

        return self.visitChildren(ctx)

    def assessMoveStatement(self, ctx: CobolIsuzuParser.MoveStatementContext):
        # Intialize
        tag = "MoveStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )

        if ctx.ALL():
            res["move_option"] = "ALL"

        if ctx.ATTRIBUTE():
            res["move_option"] = "ATTRIBUTE"

        move_to_statement: Optional[CobolIsuzuParser.MoveToStatementContext] = (
            ctx.moveToStatement()
        )

        move_corresponding_to_statement: Optional[
            CobolIsuzuParser.MoveCorrespondingToStatementContext
        ] = ctx.moveCorrespondingToStatement()

        if move_to_statement:
            res["move_type"] = "TO"

            move_to_sending_area: CobolIsuzuParser.MoveToSendingAreaContext = (
                move_to_statement.moveToSendingArea()
            )
            res["move_from"] = get_original_code_content(
                self.parser,
                move_to_sending_area.start.tokenIndex,
                move_to_sending_area.stop.tokenIndex,
            )

            move_to_sending_area_child = move_to_sending_area.getChild(0)
            if isinstance(
                move_to_sending_area_child, CobolIsuzuParser.IdentifierContext
            ):
                res["from_identifier"] = move_to_sending_area_child.getText()
            elif isinstance(
                move_to_sending_area_child, CobolIsuzuParser.MoveAttributeClauseContext
            ):
                cobol_word = move_to_sending_area_child.cobolWord(1)
                if isinstance(
                    cobol_word.getChild(0), CobolIsuzuParser.CharDataKeywordContext
                ):
                    res["from_literal"] = cobol_word.getText()
                else:
                    res["from_identifier"] = cobol_word.getText()
            else:
                res["from_literal"] = get_original_code_content(
                    self.parser,
                    move_to_sending_area_child.start.tokenIndex,
                    move_to_sending_area_child.stop.tokenIndex,
                )

            move_to_identifier_list = move_to_statement.identifier()
            res["move_to"] = ""
            res["to_identifiers"] = []
            for move_to_identifier in move_to_identifier_list:
                res["move_to"] += (
                    get_original_code_content(
                        self.parser,
                        move_to_identifier.start.tokenIndex,
                        move_to_identifier.stop.tokenIndex,
                    )
                    + " "
                )

                res["to_identifiers"].append(move_to_identifier.getText())
            res["move_to"] = res["move_to"].strip()

        if isinstance(
            move_corresponding_to_statement,
            CobolIsuzuParser.MoveCorrespondingToStatementContext,
        ):
            res["move_type"] = "CORRESPONDING"

            move_corresponding_to_sending_aarea = (
                move_corresponding_to_statement.moveCorrespondingToSendingArea()
            )

            if move_corresponding_to_sending_aarea:
                res["from_identifier"] = move_corresponding_to_sending_aarea.getText()
                res["move_from"] = move_corresponding_to_sending_aarea.getText()

            move_to_identifier_list = move_corresponding_to_statement.identifier()
            res["move_to"] = ""
            res["to_identifiers"] = []
            for move_to_identifier in move_to_identifier_list:
                res["move_to"] += (
                    get_original_code_content(
                        self.parser,
                        move_to_identifier.start.tokenIndex,
                        move_to_identifier.stop.tokenIndex,
                    )
                    + " "
                )

                res["to_identifiers"].append(move_to_identifier.getText())

            res["move_to"] = res["move_to"].strip()

        return res

    def visitMoveStatement(self, ctx: CobolIsuzuParser.MoveStatementContext):

        res = self.assessMoveStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolIsuzuParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def assessWriteStatement(self, ctx: CobolIsuzuParser.WriteStatementContext):
        tag = "WriteStatement"
        res = {}

        start_token = ctx.start
        stop_token = ctx.stop

        res["tag"] = tag
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )

        record_name = ctx.recordName()
        res["record_name"] = record_name.getText()

        write_from = ctx.writeFromPhrase()
        if write_from:
            res["write_from_phrase"] = {}

            res["write_from_phrase"]["identifier"] = (
                write_from.identifier().getText() if write_from.identifier() else None
            )
            res["write_from_phrase"]["literal"] = (
                write_from.literal().getText() if write_from.literal() else None
            )

        write_advancing_phrase = ctx.writeAdvancingPhrase()
        if write_advancing_phrase:
            res["write_advancing_phrase"] = {}
            res["write_advancing_phrase"]["position"] = (
                write_advancing_phrase.getChild(0).getText().upper()
            )
            advancing_type = (
                write_advancing_phrase.ADVANCING().getText().upper()
                if write_advancing_phrase.ADVANCING()
                else None
            )
            advancing_type = (
                advancing_type or write_advancing_phrase.CHANNEL().getText().upper()
                if write_advancing_phrase.CHANNEL()
                else None
            )
            res["write_advancing_phrase"]["advancing_type"] = advancing_type

            write_advancing_page = write_advancing_phrase.writeAdvancingPage()
            if write_advancing_page:
                res["write_advancing_phrase"]["advancing"] = "PAGE"

            write_advancing_lines = write_advancing_phrase.writeAdvancingLines()
            if write_advancing_lines:
                res["write_advancing_phrase"]["advancing"] = {
                    "identifier": (
                        write_advancing_lines.identifier().getText()
                        if write_advancing_lines.identifier()
                        else None
                    ),
                    "literal": (
                        write_advancing_lines.literal().getText()
                        if write_advancing_lines.literal()
                        else None
                    ),
                }

            write_advancing_mnemonic = write_advancing_phrase.writeAdvancingMnemonic()
            if write_advancing_mnemonic:
                res["write_advancing_phrase"]["advancing"] = {}
                res["write_advancing_phrase"]["advancing"][
                    "mnemonic_name"
                ] = write_advancing_mnemonic.getText().upper()

        write_at_end_of_page_phrase = ctx.writeAtEndOfPagePhrase()
        if write_at_end_of_page_phrase:
            res["write_at_end_of_page_phrase"] = []
            statement = write_at_end_of_page_phrase.statement()
            if statement:
                for st in statement:
                    start_idx = st.start.tokenIndex
                    stop_idx = st.stop.tokenIndex
                    c = st.getChild(0)
                    type_ = type(c).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        res["write_at_end_of_page_phrase"].append(f(c))

        write_not_at_end_of_page_phrase = ctx.writeNotAtEndOfPagePhrase()
        if write_not_at_end_of_page_phrase:
            res["not_invalid_key_phrase"] = []
            statement = write_not_at_end_of_page_phrase.statement()
            if statement:
                for st in statement:
                    start_idx = st.start.tokenIndex
                    stop_idx = st.stop.tokenIndex
                    c = st.getChild(0)
                    type_ = type(c).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        res["write_not_at_end_of_page_phrase"].append(f(c))

        # invalidKeyPhrase
        invalidKeyPhrase = ctx.invalidKeyPhrase()
        if invalidKeyPhrase:
            res["invalid_key_phrase"] = []
            statement = invalidKeyPhrase.statement()
            if statement:
                for st in statement:
                    start_idx = st.start.tokenIndex
                    stop_idx = st.stop.tokenIndex
                    c = st.getChild(0)
                    type_ = type(c).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        res["invalid_key_phrase"].append(f(c))

        # notInvalidKeyPhrase
        notInvalidKeyPhrase = ctx.notInvalidKeyPhrase()
        if notInvalidKeyPhrase:
            res["not_invalid_key_phrase"] = []
            statement = notInvalidKeyPhrase.statement()
            if statement:
                for st in statement:
                    start_idx = st.start.tokenIndex
                    stop_idx = st.stop.tokenIndex
                    c = st.getChild(0)
                    type_ = type(c).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        res["not_invalid_key_phrase"].append(f(c))

        return res

    def visitWriteStatement(self, ctx: CobolIsuzuParser.WriteStatementContext):
        res = self.assessWriteStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolIsuzuParser.SentenceContext):
            self.statements.append(res)

        return self.visitChildren(ctx)

    def assessCallStatement(self, ctx: CobolIsuzuParser.CallStatementContext):
        # Intialize
        tag = "CallStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )

        # Get all children of context
        children = ctx.getChildren()
        children = [type(c) for c in children]

        # literal_1
        if CobolIsuzuParser.LiteralContext in children:
            literal = ctx.literal()
            res["call_literal"] = literal.getText()

        # identifier_1
        elif CobolIsuzuParser.IdentifierContext in children:
            identifier = ctx.identifier()
            # res["identifier_1"] = identifier.getText()
            res["call_identifiers"].append(
                get_original_code_content(
                    self.parser,
                    identifier.start.tokenIndex,
                    identifier.stop.tokenIndex,
                )
            )

        # callUsingPhrase
        res["using_identifiers"] = []
        res["using_literals"] = []
        callUsingPhrase = ctx.callUsingPhrase()

        if callUsingPhrase:

            res["call_type"] = "USING"
            call_using_parameter_list: List[
                CobolIsuzuParser.CallUsingParameterContext
            ] = callUsingPhrase.callUsingParameter()

            for call_using_parameter in call_using_parameter_list:
                call_using_parameter = call_using_parameter.getChild(0)

                if isinstance(
                    call_using_parameter, CobolIsuzuParser.CallByReferencePhraseContext
                ):
                    call_by_reference_list: List[
                        CobolIsuzuParser.CallByReferenceContext
                    ] = call_using_parameter.callByReference()

                    for call_by_reference in call_by_reference_list:
                        identifier = call_by_reference.identifier()
                        if identifier:
                            res["using_identifiers"].append(identifier.getText())
                        literal = (
                            call_by_reference.literal()
                            or call_by_reference.fileName()
                            or call_by_reference.OMITTED()
                        )
                        if literal:
                            if isinstance(literal, TerminalNode):
                                res["using_literals"].append(
                                    get_original_code_content(
                                        self.parser,
                                        literal.symbol.tokenIndex,
                                        literal.symbol.tokenIndex,
                                    )
                                )
                            else:
                                res["using_literals"].append(
                                    get_original_code_content(
                                        self.parser,
                                        literal.start.tokenIndex,
                                        literal.stop.tokenIndex,
                                    )
                                )

                elif isinstance(
                    call_using_parameter, CobolIsuzuParser.CallByValuePhraseContext
                ):
                    call_by_value_list = call_using_parameter.callByValue()
                    for call_by_value in call_by_value_list:
                        identifier = call_by_value.identifier()
                        if identifier:
                            res["using_identifiers"].append(identifier.getText())

                        literal = call_by_value.literal()
                        if literal:
                            res["using_literals"].append(literal.getText())

                elif isinstance(
                    call_using_parameter, CobolIsuzuParser.CallByContentPhraseContext
                ):
                    call_by_content_list = call_using_parameter.callByContent()
                    for call_by_content in call_by_content_list:
                        identifier = call_by_content.identifier()
                        if identifier:
                            res["using_identifiers"].append(identifier.getText())

                        literal = call_by_content.literal() or call_by_content.OMITTED()
                        if literal:
                            if isinstance(literal, TerminalNode):
                                res["using_literals"].append(
                                    get_original_code_content(
                                        self.parser,
                                        literal.symbol.tokenIndex,
                                        literal.symbol.tokenIndex,
                                    )
                                )
                            else:
                                res["using_literals"].append(
                                    get_original_code_content(
                                        self.parser,
                                        literal.start.tokenIndex,
                                        literal.stop.tokenIndex,
                                    )
                                )

        call_giving_phrase = ctx.callGivingPhrase()

        if call_giving_phrase:
            res["giving_identifier"] = call_giving_phrase.identifier().getText()

        # call system
        if ctx.callSystem():
            res["call_type"] = "SYSTEM"

        return res

    def visitCallStatement(self, ctx: CobolIsuzuParser.CallStatementContext):
        res = self.assessCallStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )

        parameters = res.get("using_literals", []) + res.get("using_identifiers", [])

        if "giving_identifier" in res:
            parameters.append(res["giving_identifier"])

        if "call_literal" in res:
            self.called_program_list.append(
                CalledProgram(
                    program_id=res["call_literal"].replace('"', ""),
                    line_number=res["start_line"],
                    parameters=parameters,
                    call_type="STATIC",
                )
            )

        if "call_identifiers" in res:
            for call_identifier in res["call_identifiers"]:
                self.called_program_list.append(
                    CalledProgram(
                        program_id=call_identifier,
                        line_number=res["start_line"],
                        parameters=parameters,
                        call_type="DYNAMIC",
                    )
                )

        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolIsuzuParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def assessRewriteStatement(self, ctx: CobolIsuzuParser.RewriteStatementContext):
        # Intialize
        tag = "RewriteStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        # recordName
        recordName = ctx.recordName()
        if recordName:
            res["record_name"] = recordName.getText()
        else:
            res["record_name"] = ""

        # rewriteFrom
        rewriteFrom = ctx.rewriteFrom()
        if rewriteFrom:
            # res["record_name_1"] = rewriteFrom.identifier().getText()
            res["rewrite_from_identifier"] = get_original_code_content(
                self.parser,
                rewriteFrom.identifier().start.tokenIndex,
                rewriteFrom.identifier().stop.tokenIndex,
            )

        # invalidKeyPhrase
        invalidKeyPhrase = ctx.invalidKeyPhrase()
        if invalidKeyPhrase:
            res["invalid_key_phrase"] = []
            statement = invalidKeyPhrase.statement()
            if statement:
                for st in statement:
                    start_idx = st.start.tokenIndex
                    stop_idx = st.stop.tokenIndex
                    c = st.getChild(0)
                    type_ = type(c).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        res["invalid_key_phrase"].append(f(c))

        # notInvalidKeyPhrase
        notInvalidKeyPhrase = ctx.notInvalidKeyPhrase()
        if notInvalidKeyPhrase:
            res["not_invalid_key_phrase"] = []
            statement = notInvalidKeyPhrase.statement()
            if statement:
                for st in statement:
                    start_idx = st.start.tokenIndex
                    stop_idx = st.stop.tokenIndex
                    c = st.getChild(0)
                    type_ = type(c).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        res["not_invalid_key_phrase"].append(f(c))
        return res

    def visitRewriteStatement(self, ctx: CobolIsuzuParser.RewriteStatementContext):
        res = self.assessRewriteStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolIsuzuParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def assessRewriteStatement(self, ctx: CobolIsuzuParser.RewriteStatementContext):
        # Intialize
        tag = "RewriteStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        # recordName
        recordName = ctx.recordName()
        if recordName:
            res["record_name"] = recordName.getText()
        # rewriteFrom
        rewriteFrom = ctx.rewriteFrom()
        if rewriteFrom:
            # res["record_name_1"] = rewriteFrom.identifier().getText()
            res["rewrite_from_identifier"] = get_original_code_content(
                self.parser,
                rewriteFrom.identifier().start.tokenIndex,
                rewriteFrom.identifier().stop.tokenIndex,
            )

        # invalidKeyPhrase
        invalidKeyPhrase = ctx.invalidKeyPhrase()
        if invalidKeyPhrase:
            res["invalid_key_phrase"] = []
            statement = invalidKeyPhrase.statement()
            if statement:
                for st in statement:
                    start_idx = st.start.tokenIndex
                    stop_idx = st.stop.tokenIndex
                    c = st.getChild(0)
                    type_ = type(c).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        res["invalid_key_phrase"].append(f(c))

        # notInvalidKeyPhrase
        notInvalidKeyPhrase = ctx.notInvalidKeyPhrase()
        if notInvalidKeyPhrase:
            res["not_invalid_key_phrase"] = []
            statement = notInvalidKeyPhrase.statement()
            if statement:
                for st in statement:
                    start_idx = st.start.tokenIndex
                    stop_idx = st.stop.tokenIndex
                    c = st.getChild(0)
                    type_ = type(c).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        res["not_invalid_key_phrase"].append(f(c))
        return res

    def visitRewriteStatement(self, ctx: CobolIsuzuParser.RewriteStatementContext):
        res = self.assessRewriteStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolIsuzuParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def assessReadStatement(self, ctx: CobolIsuzuParser.ReadStatementContext):
        # Intialize
        tag = "ReadStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        # fileName
        fileName = ctx.fileName()
        if fileName:
            res["fileName"] = fileName.getText()

        next_record = ctx.NEXT()

        res["next_record"] = True if next_record else False

        # readInto
        readInto = ctx.readInto()
        if readInto:
            # res["identifier_1"] = readInto.identifier().getText()
            res["read_into_identifier"] = get_original_code_content(
                self.parser,
                readInto.identifier().start.tokenIndex,
                readInto.identifier().stop.tokenIndex,
            )

        read_with = ctx.readWith()
        if read_with:
            res["read_with"] = get_original_code_content(
                self.parser,
                read_with.start.tokenIndex,
                read_with.stop.tokenIndex,
            ).upper()

        read_key = ctx.readKey()
        if read_key:
            res["read_key"] = get_original_code_content(
                self.parser,
                read_key.start.tokenIndex,
                read_key.stop.tokenIndex,
            )

        # invalidKeyPhrase
        invalidKeyPhrase = ctx.invalidKeyPhrase()
        if invalidKeyPhrase:
            res["invalid_key_phrase"] = []
            statement = invalidKeyPhrase.statement()
            if statement:
                for st in statement:
                    start_idx = st.start.tokenIndex
                    stop_idx = st.stop.tokenIndex
                    c = st.getChild(0)
                    type_ = type(c).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        res["invalid_key_phrase"].append(f(c))

        # notInvalidKeyPhrase
        notInvalidKeyPhrase = ctx.notInvalidKeyPhrase()
        if notInvalidKeyPhrase:
            res["not_invalid_key_phrase"] = []
            statement = notInvalidKeyPhrase.statement()
            if statement:
                for st in statement:
                    start_idx = st.start.tokenIndex
                    stop_idx = st.stop.tokenIndex
                    c = st.getChild(0)
                    type_ = type(c).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        res["not_invalid_key_phrase"].append(f(c))

        at_end_phrase = ctx.atEndPhrase()
        if at_end_phrase:
            res["at_end_phrase"] = []
            statement = at_end_phrase.statement()
            if statement:
                for st in statement:
                    start_idx = st.start.tokenIndex
                    stop_idx = st.stop.tokenIndex
                    c = st.getChild(0)
                    type_ = type(c).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        res["at_end_phrase"].append(f(c))

        not_at_end_phrase = ctx.notAtEndPhrase()
        if not_at_end_phrase:
            res["not_at_end_phrase"] = []
            statement = not_at_end_phrase.statement()
            if statement:
                for st in statement:
                    start_idx = st.start.tokenIndex
                    stop_idx = st.stop.tokenIndex
                    c = st.getChild(0)
                    type_ = type(c).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        res["not_at_end_phrase"].append(f(c))

        return res

    def visitReadStatement(self, ctx: CobolIsuzuParser.ReadStatementContext):
        res = self.assessReadStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolIsuzuParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessPerformStatement(self, ctx: CobolIsuzuParser.PerformStatementContext):
        # Intialize
        res = {}
        res["tag"] = "PerformStatement"
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        sub_tags = []
        # performProcedureStatement
        performProcedureStatement = ctx.performProcedureStatement()
        if performProcedureStatement:
            procedureName = performProcedureStatement.procedureName()
            if len(procedureName) == 1:
                res["procedure_name_1"] = procedureName[0].getText()
            if len(procedureName) == 2:
                res["procedure_name_1"] = procedureName[0].getText()
                res["procedure_name_2"] = procedureName[1].getText()
                sub_tags.append("THRU")

            performType = performProcedureStatement.performType()

            perform_times = recursive_find_first_child_by_type(
                ctx, CobolIsuzuParser.PerformTimesContext
            )

            perform_until = recursive_find_first_child_by_type(
                ctx, CobolIsuzuParser.PerformUntilContext
            )

            perform_varying = recursive_find_first_child_by_type(
                ctx, CobolIsuzuParser.PerformVaryingContext
            )

            if perform_times:
                res["loop_times"] = get_original_code_content(
                    self.parser,
                    perform_times.start.tokenIndex,
                    perform_times.stop.tokenIndex,
                )
                sub_tags.append("TIMES")

            if perform_until:
                condition = recursive_find_first_child_by_type(
                    perform_until,
                    CobolIsuzuParser.ConditionContext,
                )
                res["condition"] = get_original_code_content(
                    self.parser,
                    condition.start.tokenIndex,
                    condition.stop.tokenIndex,
                )
                sub_tags.append("UNTIL")

            if perform_varying:
                perform_varying_clause = recursive_find_first_child_by_type(
                    perform_varying, CobolIsuzuParser.PerformVaryingClauseContext
                )
                perform_varying_phrase = perform_varying_clause.performVaryingPhrase()
                varying_variable = perform_varying_phrase.getChild(0)
                res["varying_variable"] = get_original_code_content(
                    self.parser,
                    varying_variable.start.tokenIndex,
                    varying_variable.stop.tokenIndex,
                )

                from_phrase = perform_varying_phrase.getChild(1)
                res["varying_from"] = get_original_code_content(
                    self.parser,
                    from_phrase.getChild(1).start.tokenIndex,
                    from_phrase.getChild(1).stop.tokenIndex,
                )

                by_phrase = perform_varying_phrase.getChild(2)
                res["varying_by"] = get_original_code_content(
                    self.parser,
                    by_phrase.getChild(1).start.tokenIndex,
                    by_phrase.getChild(1).stop.tokenIndex,
                )

                sub_tags.append("VARYING")

        res["sub_tags"] = sub_tags

        # performInlineStatement
        performInlineStatement = ctx.performInlineStatement()
        if performInlineStatement:
            # handle nested perform
            perform_times = recursive_find_first_child_by_type(
                performInlineStatement, CobolIsuzuParser.PerformTimesContext
            )

            perform_until = recursive_find_first_child_by_type(
                performInlineStatement, CobolIsuzuParser.PerformUntilContext
            )

            perform_varying = recursive_find_first_child_by_type(
                performInlineStatement, CobolIsuzuParser.PerformVaryingContext
            )

            if perform_times:
                res["loop_times"] = get_original_code_content(
                    self.parser,
                    perform_times.start.tokenIndex,
                    perform_times.stop.tokenIndex,
                )
                sub_tags.append("TIMES")

            if perform_until:
                condition = recursive_find_first_child_by_type(
                    perform_until,
                    CobolIsuzuParser.ConditionContext,
                )
                res["condition"] = get_original_code_content(
                    self.parser,
                    condition.start.tokenIndex,
                    condition.stop.tokenIndex,
                )
                sub_tags.append("UNTIL")

            if perform_varying:
                perform_varying_clause = recursive_find_first_child_by_type(
                    perform_varying, CobolIsuzuParser.PerformVaryingClauseContext
                )
                perform_varying_phrase = perform_varying_clause.performVaryingPhrase()
                varying_variable = perform_varying_phrase.getChild(0)
                res["varying_variable"] = get_original_code_content(
                    self.parser,
                    varying_variable.start.tokenIndex,
                    varying_variable.stop.tokenIndex,
                )

                from_phrase = perform_varying_phrase.getChild(1)
                res["varying_from"] = get_original_code_content(
                    self.parser,
                    from_phrase.getChild(1).start.tokenIndex,
                    from_phrase.getChild(1).stop.tokenIndex,
                )

                by_phrase = perform_varying_phrase.getChild(2)
                res["varying_by"] = get_original_code_content(
                    self.parser,
                    by_phrase.getChild(1).start.tokenIndex,
                    by_phrase.getChild(1).stop.tokenIndex,
                )

                sub_tags.append("VARYING")

            res["sub_tags"] = sub_tags

            res["performInlineStatement"] = {}
            performType = performInlineStatement.performType()
            if performType:
                res["performInlineStatement"]["performType"] = (
                    get_original_code_content(
                        self.parser,
                        performType.start.tokenIndex,
                        performType.stop.tokenIndex,
                    )
                )
            statement = performInlineStatement.statement()
            if statement:
                res["performInlineStatement"]["statement"] = []
                for st in statement:
                    start_idx = st.start.tokenIndex
                    stop_idx = st.stop.tokenIndex
                    c = st.getChild(0)
                    type_ = type(c).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        res["performInlineStatement"]["statement"].append(f(c))

        return res

    def visitPerformStatement(self, ctx: CobolIsuzuParser.PerformStatementContext):
        res = self.assessPerformStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolIsuzuParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessIfStatement(self, ctx: CobolIsuzuParser.IfStatementContext):
        # Intialize
        tag = "IfStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        # condition
        condition = ctx.condition()
        if condition:
            start_idx = condition.start.tokenIndex
            stop_idx = condition.stop.tokenIndex
            res["condition"] = get_original_code_content(
                self.parser, start_idx, stop_idx
            )
        # ifThen
        ifThen = ctx.ifThen()
        if ifThen:
            res["ifThen"] = []
            statement = ifThen.statement()
            if statement:
                for st in statement:
                    start_idx = st.start.tokenIndex
                    stop_idx = st.stop.tokenIndex
                    c = st.getChild(0)
                    type_ = type(c).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        res["ifThen"].append(f(c))

        # ifElse
        ifElse = ctx.ifElse()
        if ifElse:
            res["ifElse"] = []
            statement = ifElse.statement()
            if statement:
                for st in statement:
                    start_idx = st.start.tokenIndex
                    stop_idx = st.stop.tokenIndex
                    c = st.getChild(0)
                    type_ = type(c).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        res["ifElse"].append(f(c))

        return res

    def visitIfStatement(self, ctx: CobolIsuzuParser.IfStatementContext):
        res = self.assessIfStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolIsuzuParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessOpenStatement(self, ctx: CobolIsuzuParser.OpenStatementContext):
        # Intialize
        tag = "OpenStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        # Get all children of context
        children = ctx.getChildren()

        res["open_files"] = []

        for child in children:

            if isinstance(child, CobolIsuzuParser.OpenInputStatementContext):
                open_inputs = child.openInput()
                for open_input in open_inputs:
                    file_name = open_input.fileName()
                    res["open_files"].append(
                        {
                            "file_name": file_name.getText(),
                            "open_type": "INPUT",
                            "on_exception_clause": [],
                        }
                    )

            elif isinstance(child, CobolIsuzuParser.OpenOutputStatementContext):
                open_outputs = child.openOutput()
                for open_output in open_outputs:
                    file_name = open_output.fileName()
                    res["open_files"].append(
                        {
                            "file_name": file_name.getText(),
                            "open_type": "OUTPUT",
                            "on_exception_clause": [],
                        }
                    )

            elif isinstance(child, CobolIsuzuParser.OpenIOStatementContext):
                file_names = child.fileName()
                for file_name in file_names:
                    res["open_files"].append(
                        {
                            "file_name": file_name.getText(),
                            "open_type": "IO",
                            "on_exception_clause": [],
                        }
                    )

            # elif isinstance(child, CobolIsuzuParser.OpenInquiryContext):
            #     file_name = child.qualifiedDataName()
            #     on_exception_statements = []
            #     on_exception_clause = child.onExceptionClause()
            #     if on_exception_clause:
            #         statements = on_exception_clause.statement()
            #         for statement in statements:
            #             child = statement.getChild(0)
            #             type_ = type(child).__name__
            #             if type_ in self.func:
            #                 f = self.func[type_]
            #                 on_exception_statements.append(f(child))

            #     res["open_files"].append(
            #         {
            #             "file_name": file_name.getText(),
            #             "open_type": "INQUIRY",
            #             "on_exception_clause": on_exception_statements,
            #         }
            #     )

            elif isinstance(child, CobolIsuzuParser.OpenExtendStatementContext):
                file_names = child.fileName()
                for file_name in file_names:
                    res["open_files"].append(
                        {
                            "file_name": file_name.getText(),
                            "open_type": "EXTEND",
                            "on_exception_clause": [],
                        }
                    )

            # elif isinstance(child, CobolIsuzuParser.OpenUpdateStatementContext):
            #     file_name = child.qualifiedDataName()

            #     on_exception_clause = child.onExceptionClause()
            #     on_exception_statements = []
            #     if on_exception_clause:
            #         statements = on_exception_clause.statement()
            #         for statement in statements:
            #             child = statement.getChild(0)
            #             type_ = type(child).__name__
            #             if type_ in self.func:
            #                 f = self.func[type_]
            #                 on_exception_statements.append(f(child))

            #     res["open_files"].append(
            #         {
            #             "file_name": file_name.getText(),
            #             "open_type": "UPDATE",
            #             "on_exception_clause": on_exception_statements,
            #         }
            #     )

        return res

    def visitOpenStatement(self, ctx: CobolIsuzuParser.OpenStatementContext):
        res = self.assessOpenStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolIsuzuParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def assessSetStatement(self, ctx: CobolIsuzuParser.SetStatementContext):
        # Intialize
        tag = "SetStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        # Get all children of context
        children = ctx.getChildren()
        children = [type(c) for c in children]

        # SetTo
        if CobolIsuzuParser.SetToStatementContext in children:
            res["set_type"] = "TO"
            res["set_to"] = []
            setToStatement = ctx.setToStatement()
            for s in setToStatement:
                # init
                r = {}
                # setTo
                setTo = s.setTo()
                if setTo:
                    r["source_identifier"] = []
                    for c in setTo:
                        # r["identifier_1"].append(c.getText())
                        r["source_identifier"].append(
                            get_original_code_content(
                                self.parser, c.start.tokenIndex, c.stop.tokenIndex
                            )
                        )
                # setToValue
                setToValue = s.setToValue()
                if setToValue:
                    setToValue: CobolIsuzuParser.SetToValueContext = setToValue[0]
                    setToIdentifier = setToValue.identifier()
                    if setToIdentifier:
                        r["target_identifier"] = get_original_code_content(
                            self.parser,
                            setToValue.start.tokenIndex,
                            setToValue.stop.tokenIndex,
                        )
                    else:
                        setToLiteral = setToValue.getChild(0)

                        if isinstance(setToLiteral, TerminalNode):
                            r["target_literal"] = get_original_code_content(
                                self.parser,
                                setToLiteral.symbol.tokenIndex,
                                setToLiteral.symbol.tokenIndex,
                            )
                        else:
                            r["target_literal"] = get_original_code_content(
                                self.parser,
                                setToLiteral.start.tokenIndex,
                                setToLiteral.stop.tokenIndex,
                            )
                    # r["identifier_2"] = []
                    # for c in setToValue:
                    #     # r["identifier_2"].append(c.getText())
                    #     r["identifier_2"].append(
                    #         get_original_code_content(
                    #             self.parser, c.start.tokenIndex, c.stop.tokenIndex
                    #         )
                    #     )
                # collect
                res["set_to"].append(r)
        else:
            set_up_down_by_statement: CobolIsuzuParser.SetUpDownByStatementContext = (
                ctx.setUpDownByStatement()
            )

            res["set_type"] = get_original_code_content(
                self.parser,
                set_up_down_by_statement.getChild(1).symbol.tokenIndex,
                set_up_down_by_statement.getChild(1).symbol.tokenIndex,
            )

            res["set_up_down"] = {}

            setTo = set_up_down_by_statement.setTo()
            if setTo:
                res["set_up_down"]["source_identifier"] = []
                for c in setTo:
                    res["set_up_down"]["source_identifier"].append(
                        get_original_code_content(
                            self.parser, c.start.tokenIndex, c.stop.tokenIndex
                        )
                    )

            set_by_value: CobolIsuzuParser.SetByValueContext = (
                set_up_down_by_statement.setByValue()
            )

            if set_by_value.identifier():
                res["set_up_down"][
                    "by_identifier"
                ] = set_by_value.identifier().getText()
            else:
                res["set_up_down"]["by_literal"] = get_original_code_content(
                    self.parser,
                    set_by_value.start.tokenIndex,
                    set_by_value.stop.tokenIndex,
                )

        return res

    def visitSetStatement(self, ctx: CobolIsuzuParser.SetStatementContext):
        res = self.assessSetStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolIsuzuParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def assessSubtractStatement(self, ctx: CobolIsuzuParser.SubtractStatementContext):
        # Intialize
        tag = "SubtractStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        res["subtrahends"] = []
        res["minuends"] = []
        res["results"] = []

        subtract_phrase = ctx.getChild(1)

        if isinstance(subtract_phrase, CobolIsuzuParser.SubtractFromStatementContext):

            subtract_from_statement = subtract_phrase
            subtrahend_list = subtract_from_statement.subtractSubtrahend()

            for subtrahend in subtrahend_list:
                subtrahend = subtrahend.getChild(0)
                if isinstance(subtrahend, CobolIsuzuParser.IdentifierContext):
                    res["subtrahends"].append(
                        {"identifier": subtrahend.getText(), "literal": None}
                    )
                else:
                    res["subtrahends"].append(
                        {"identifier": None, "literal": subtrahend.getText()}
                    )

            minuend_list = subtract_from_statement.subtractMinuend()

            for minuend in minuend_list:
                res["minuends"].append(
                    {"identifier": minuend.identifier().getText(), "literal": None}
                )
                res["results"].append(
                    {
                        "identifier": minuend.identifier().getText(),
                        "is_rounded": minuend.ROUNDED() is not None,
                    }
                )

        elif isinstance(
            subtract_phrase, CobolIsuzuParser.SubtractFromGivingStatementContext
        ):
            subtract_from_statement = subtract_phrase
            subtrahend_list = subtract_from_statement.subtractSubtrahend()

            for subtrahend in subtrahend_list:
                subtrahend = subtrahend.getChild(0)
                if isinstance(subtrahend, CobolIsuzuParser.IdentifierContext):
                    res["subtrahends"].append(
                        {"identifier": subtrahend.getText(), "literal": None}
                    )
                else:
                    res["subtrahends"].append(
                        {"identifier": None, "literal": subtrahend.getText()}
                    )

            minuend_giving = subtract_from_statement.subtractMinuendGiving()

            res["minuends"].append(
                {
                    "identifier": (
                        minuend_giving.identifier().getText()
                        if minuend_giving.identifier()
                        else None
                    ),
                    "literal": (
                        minuend_giving.getText()
                        if minuend_giving.literal()
                        or minuend_giving.figurativeConstant()
                        else None
                    ),
                }
            )

            subtract_giving_list = subtract_from_statement.subtractGiving()

            for subtract_giving in subtract_giving_list:
                res["results"].append(
                    {
                        "identifier": subtract_giving.identifier().getText(),
                        "is_rounded": subtract_giving.ROUNDED() is not None,
                    }
                )

        elif isinstance(
            subtract_phrase, CobolIsuzuParser.SubtractCorrespondingStatementContext
        ):
            subtract_corresponding_statement = subtract_phrase
            qualified_data_name = subtract_corresponding_statement.qualifiedDataName()
            res["subtrahends"].append(
                {
                    "identifier": get_original_code_content(
                        self.parser,
                        qualified_data_name.start.tokenIndex,
                        qualified_data_name.stop.tokenIndex,
                    ),
                    "literal": None,
                }
            )

            subtract_minuend_corresponding = (
                subtract_corresponding_statement.subtractMinuendCorresponding()
            )
            res["minuends"].append(
                {
                    "identifier": get_original_code_content(
                        self.parser,
                        subtract_minuend_corresponding.start.tokenIndex,
                        subtract_minuend_corresponding.stop.tokenIndex,
                    ),
                    "literal": None,
                }
            )
            res["results"].append(
                {
                    "identifier": get_original_code_content(
                        self.parser,
                        subtract_minuend_corresponding.start.tokenIndex,
                        subtract_minuend_corresponding.stop.tokenIndex,
                    ),
                    "is_rounded": subtract_minuend_corresponding.ROUNDED() is not None,
                }
            )

        res["on_size_error_phrase"] = []
        on_size_error_phrase = ctx.onSizeErrorPhrase()
        if on_size_error_phrase:
            statements = on_size_error_phrase.statement()
            for statement in statements:
                child = statement.getChild(0)
                type_ = type(child).__name__
                if type_ in self.func:
                    f = self.func[type_]
                    res["on_size_error_phrase"].append(f(child))

        res["not_on_size_error_phrase"] = []
        not_on_size_error_phrase = ctx.notOnSizeErrorPhrase()
        if not_on_size_error_phrase:
            statements = not_on_size_error_phrase.statement()
            for statement in statements:
                child = statement.getChild(0)
                type_ = type(child).__name__
                if type_ in self.func:
                    f = self.func[type_]
                    res["not_on_size_error_phrase"].append(f(child))

        return res

    def visitSubtractStatement(self, ctx: CobolIsuzuParser.SubtractStatementContext):
        res = self.assessSubtractStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolIsuzuParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def assessStringStatement(self, ctx: CobolIsuzuParser.StringStatementContext):
        # Intialize
        tag = "StringStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        res["stringSendingPhrase"] = []
        res["destination_identifier"] = None
        res["pointer_name"] = None

        string_sending_phrase_list: List[
            CobolIsuzuParser.StringSendingPhraseContext
        ] = ctx.stringSendingPhrase()

        for string_sending_phrase in string_sending_phrase_list:
            string_sending_phrase_dict = {
                "source_identifiers": [],
                "source_literals": [],
                "delimiter_identifier": None,
                "delimiter_literal": None,
                "for_identifier": None,
                "for_literal": None,
            }
            res["stringSendingPhrase"].append(string_sending_phrase_dict)

            string_sending_list: List[CobolIsuzuParser.StringSendingContext] = (
                string_sending_phrase.stringSending()
            )
            for string_sending in string_sending_list:
                sending_identifier = string_sending.identifier()
                sending_literal = string_sending.literal()

                if sending_identifier:
                    string_sending_phrase_dict["source_identifiers"].append(
                        sending_identifier.getText()
                    )

                if sending_literal:
                    string_sending_phrase_dict["source_literals"].append(
                        sending_literal.getText()
                    )

            string_delimited_by_phrase: Optional[
                CobolIsuzuParser.StringDelimitedByPhraseContext
            ] = string_sending_phrase.stringDelimitedByPhrase()

            if string_delimited_by_phrase:
                delimiter_identifier = string_delimited_by_phrase.identifier()
                delimiter_literal = (
                    string_delimited_by_phrase.literal()
                    or string_delimited_by_phrase.SIZE()
                )

                string_sending_phrase_dict["delimiter_identifier"] = (
                    delimiter_identifier.getText() if delimiter_identifier else None
                )

                string_sending_phrase_dict["delimiter_literal"] = (
                    delimiter_literal.getText() if delimiter_literal else None
                )

            string_for_phrase: Optional[CobolIsuzuParser.StringForPhraseContext] = (
                string_sending_phrase.stringForPhrase()
            )

            if string_for_phrase:
                identifier = string_for_phrase.identifier()
                literal = string_for_phrase.literal()

                string_sending_phrase_dict["for_identifier"] = (
                    identifier.getText() if identifier else None
                )
                string_sending_phrase_dict["for_literal"] = (
                    literal.getText() if literal else None
                )

        string_into_phrase: CobolIsuzuParser.StringIntoPhraseContext = (
            ctx.stringIntoPhrase()
        )

        into_identifier = string_into_phrase.identifier()
        res["destination_identifier"] = into_identifier.getText()

        string_pointer_phrase: Optional[
            CobolIsuzuParser.StringWithPointerPhraseContext
        ] = ctx.stringWithPointerPhrase()

        if string_pointer_phrase:
            pointer_qualified_data_name = string_pointer_phrase.qualifiedDataName()

            res["pointer_name"] = pointer_qualified_data_name.getText()

        res["on_overflow_phrase"] = []
        on_overflow_phrase = ctx.onOverflowPhrase()
        if on_overflow_phrase:
            statements = on_overflow_phrase.statement()
            for statement in statements:
                child = statement.getChild(0)
                type_ = type(child).__name__
                if type_ in self.func:
                    f = self.func[type_]
                    res["on_overflow_phrase"].append(f(child))

        res["not_on_overflow_phrase"] = []
        not_on_overflow_phrase = ctx.notOnOverflowPhrase()
        if not_on_overflow_phrase:
            statements = not_on_overflow_phrase.statement()
            for statement in statements:
                child = statement.getChild(0)
                type_ = type(child).__name__
                if type_ in self.func:
                    f = self.func[type_]
                    res["not_on_overflow_phrase"].append(f(child))

        return res

    def visitStringStatement(self, ctx: CobolIsuzuParser.StringStatementContext):
        res = self.assessStringStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolIsuzuParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessSearchStatement(self, ctx: CobolIsuzuParser.SearchStatementContext):
        tag = "SearchStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )

        all_token = ctx.ALL()
        res["is_all"] = True if all_token else False
        record_name = ctx.qualifiedDataName()
        res["record_name"] = get_original_code_content(
            self.parser, record_name.start.tokenIndex, record_name.stop.tokenIndex
        )

        search_varying: CobolIsuzuParser.SearchVaryingContext = ctx.searchVarying()
        if search_varying:
            varying_record_name = search_varying.qualifiedDataName()
            res["varying_record_name"] = get_original_code_content(
                self.parser,
                varying_record_name.start.tokenIndex,
                varying_record_name.stop.tokenIndex,
            )

        res["at_end_phrase"] = []
        at_end_phrase: CobolIsuzuParser.AtEndPhraseContext = ctx.atEndPhrase()
        if at_end_phrase:
            statement_list = at_end_phrase.statement()
            for statement in statement_list:
                child = statement.getChild(0)
                type_ = type(child).__name__
                if type_ in self.func:
                    f = self.func[type_]
                    res["at_end_phrase"].append(f(child))

        search_when_list = ctx.searchWhen()
        res["when"] = []
        for search_when in search_when_list:
            condition = search_when.condition()
            statement_list = search_when.statement()
            res["when"].append(
                {
                    "condition": get_original_code_content(
                        self.parser,
                        condition.start.tokenIndex,
                        condition.stop.tokenIndex,
                    ),
                    "statements": [],
                }
            )
            for statement in statement_list:
                child = statement.getChild(0)
                type_ = type(child).__name__
                if type_ in self.func:
                    f = self.func[type_]
                    res["when"][-1]["statements"].append(f(child))

        return res

    def visitSearchStatement(self, ctx: CobolIsuzuParser.SearchStatementContext):
        res = self.assessSearchStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolIsuzuParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def assessInspectStatement(self, ctx: CobolIsuzuParser.InspectStatementContext):
        # Intialize
        tag = "InspectStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )

        identifier = ctx.identifier()
        res["identifier"] = identifier.getText()

        inspect_phrase = ctx.getChild(2)

        if isinstance(inspect_phrase, CobolIsuzuParser.InspectReplacingPhraseContext):
            inspect_replacing_phrase_dict = self.extract_inspect_replacing_phrase(
                inspect_phrase
            )
            res["phrase"] = inspect_replacing_phrase_dict

        elif isinstance(inspect_phrase, CobolIsuzuParser.InspectTallyingPhraseContext):
            inspect_tallying_phrase_dict = self.extract_inspect_tallying(inspect_phrase)
            res["phrase"] = inspect_tallying_phrase_dict

        elif isinstance(
            inspect_phrase, CobolIsuzuParser.InspectTallyingReplacingPhraseContext
        ):
            inspect_tallying_replacing_dict = self.extract_inspect_tallying_replacing(
                inspect_phrase
            )
            res["phrase"] = inspect_tallying_replacing_dict

        elif isinstance(
            inspect_phrase, CobolIsuzuParser.InspectConvertingPhraseContext
        ):
            inspect_converting_phrase_dict = self.extract_inspect_converting_phrase(
                inspect_phrase
            )
            res["phrase"] = inspect_converting_phrase_dict

        return res

    def visitInspectStatement(self, ctx: CobolIsuzuParser.InspectStatementContext):
        res = self.assessInspectStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolIsuzuParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def assessInitializeStatement(
        self, ctx: CobolIsuzuParser.InitializeStatementContext
    ):
        # Intialize
        tag = "InitializeStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        # identifier
        identifier = ctx.identifier()
        if identifier:
            res["identifier_1"] = []
            for i in identifier:
                # res["identifier_1"].append(i.getText())
                res["identifier_1"].append(
                    get_original_code_content(
                        self.parser, i.start.tokenIndex, i.stop.tokenIndex
                    )
                )
        return res

    def visitInitializeStatement(
        self, ctx: CobolIsuzuParser.InitializeStatementContext
    ):
        res = self.assessInitializeStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolIsuzuParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def assessGoToStatement(self, ctx: CobolIsuzuParser.GoToStatementContext):
        # Intialize
        tag = "GoToStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        goToStatementSimple = ctx.goToStatementSimple()
        if goToStatementSimple:
            res["procedure_name_1"] = goToStatementSimple.getText()
        return res

    def visitGoToStatement(self, ctx: CobolIsuzuParser.GoToStatementContext):
        res = self.assessGoToStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolIsuzuParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def assessGobackStatement(self, ctx: CobolIsuzuParser.GobackStatementContext):
        # Intialize
        tag = "GobackStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        return res

    def visitGobackStatement(self, ctx: CobolIsuzuParser.GobackStatementContext):
        res = self.assessGobackStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolIsuzuParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def assessExitStatement(self, ctx: CobolIsuzuParser.ExitStatementContext):
        # Intialize
        tag = "ExitStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        return res

    def visitExitStatement(self, ctx: CobolIsuzuParser.ExitStatementContext):
        res = self.assessExitStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolIsuzuParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def assessDisplayStatement(self, ctx: CobolIsuzuParser.DisplayStatementContext):
        # Intialize
        tag = "DisplayStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        displayOperand = ctx.displayOperand()
        if displayOperand:
            res["identifier_1"] = []
            res["literal_1"] = []
            for do in displayOperand:
                for d in do.getChildren():
                    if isinstance(d, CobolIsuzuParser.IdentifierContext):
                        res["identifier_1"].append(
                            get_original_code_content(
                                self.parser, d.start.tokenIndex, d.stop.tokenIndex
                            )
                        )
                    elif isinstance(d, CobolIsuzuParser.LiteralContext):
                        res["literal_1"].append(d.getText())
        return res

    def visitDisplayStatement(self, ctx: CobolIsuzuParser.DisplayStatementContext):
        res = self.assessDisplayStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolIsuzuParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    # COPYBOOK LIST

    def assessCopyStatement(self, ctx: CobolIsuzuParser.CopyStatementContext):
        # Intialize
        tag = "CopyStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        copySource = ctx.copySource()
        if copySource:
            # Get all children of context
            children = copySource.getChildren()
            children = [type(c) for c in children]
            # CobolIsuzuParser.LiteralContext
            if CobolIsuzuParser.LiteralContext in children:
                literal = copySource.literal()
                res["literal_1"] = literal.getText()
            # CobolIsuzuParser.CobolWordContext
            elif CobolIsuzuParser.CobolWordContext in children:
                cobolWord = copySource.cobolWord()
                res["text_name"] = cobolWord.getText()
            # CobolIsuzuParser.FileNameContext
            elif CobolIsuzuParser.FileNameContext in children:
                filename = copySource.filename()
                res["filename"] = filename.getText()
        # replacingPhrase
        replacingPhrase = ctx.replacingPhrase()
        if replacingPhrase:
            res["replacingPhrase"] = []
            for rp in replacingPhrase:
                replaceClause = rp.replaceClause()
                if replaceClause:
                    for rc in replaceClause:
                        replaceable = rc.replaceable()
                        replacement = rc.replacement()
                        res["replacingPhrase"].append(
                            {
                                "partial_word_1": replaceable.getText(),
                                "partial_word_2": replacement.getText(),
                            }
                        )
        return res

    def visitCopyStatement(self, ctx: CobolIsuzuParser.CopyStatementContext):
        # extract statements
        res = self.assessCopyStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolIsuzuParser.SentenceContext):
            self.statements.append(res)

        # extract dependency
        copy_source = recursive_find_first_child_by_type(
            ctx, CobolIsuzuParser.CopySourceContext
        )

        if copy_source is None:
            raise ValueError(
                f"File name of COPY statement {get_original_code_content(self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)}"
            )

        copy_name = copy_source.getChild(0)

        replace_clauses = find_all_children_by_type(
            ctx, CobolIsuzuParser.ReplaceClauseContext
        )

        replace_list = []

        for replace_clause in replace_clauses:
            replaceable = replace_clause.getChild(0)
            replacement = replace_clause.getChild(2)

            replace = CopybookReplace(
                replaceable=replaceable.getText(),
                replacement=replacement.getText(),
            )
            replace_list.append(replace)

        copybook = ImportedCopybook(
            copybook_name=copy_name.getText(),
            line_number=copy_source.start.line,
            replacing=replace_list,
        )

        self.copybook_list.append(copybook)
        return self.visitChildren(ctx)

    def assessContinueStatement(self, ctx: CobolIsuzuParser.ContinueStatementContext):
        # Intialize
        tag = "ContinueStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        return res

    def visitContinueStatement(self, ctx: CobolIsuzuParser.ContinueStatementContext):
        res = self.assessContinueStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolIsuzuParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def assessComputeStatement(self, ctx: CobolIsuzuParser.ComputeStatementContext):
        # Intialize
        tag = "ComputeStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        computeStore = ctx.computeStore()
        if computeStore:
            computeStore = [c.getText() for c in computeStore]
            res["identifier_1"] = computeStore
        arithmeticExpression = ctx.arithmeticExpression()
        if arithmeticExpression:
            arithmetic_expression = " ".join(
                c.getText() for c in arithmeticExpression.getChildren()
            )
            res["arithmetic_expression"] = arithmetic_expression.strip()
        return res

    def visitComputeStatement(self, ctx: CobolIsuzuParser.ComputeStatementContext):
        res = self.assessComputeStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolIsuzuParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def assessAlterStatement(self, ctx: CobolIsuzuParser.AlterStatementContext):
        # Intialize
        tag = "AlterStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        # alterProceedTo
        alterProceedTo = ctx.alterProceedTo()
        if alterProceedTo:
            res["alterProceedTo"] = []
            for t in alterProceedTo:
                procedureName = t.procedureName()
                procedureName = [p.getText() for p in procedureName]  # Convert to list
                res["alterProceedTo"].append(
                    {
                        "procedure_name_1": procedureName[0],
                        "procedure_name_2": procedureName[1],
                    }
                )
        return res

    def visitAlterStatement(self, ctx: CobolIsuzuParser.AlterStatementContext):
        res = self.assessAlterStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolIsuzuParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def assessAddStatement(self, ctx: CobolIsuzuParser.AddStatementContext):
        # Intialize
        tag = "AddStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        # Get all children of context
        children = ctx.getChildren()
        children = [type(c) for c in children]

        # AddTo
        if CobolIsuzuParser.AddToStatementContext in children:
            addToStatement = ctx.addToStatement()
            # addFrom
            addFrom = addToStatement.addFrom()
            if addFrom:
                res["identifier_1"] = []
                res["literal_1"] = []
                for af in addFrom:
                    for a in af.getChildren():
                        if isinstance(a, CobolIsuzuParser.IdentifierContext):
                            # res["identifier_1"].append(a.getText())
                            res["identifier_1"].append(
                                get_original_code_content(
                                    self.parser,
                                    a.start.tokenIndex,
                                    a.stop.tokenIndex,
                                )
                            )
                        elif isinstance(a, CobolIsuzuParser.LiteralContext):
                            res["literal_1"].append(a.getText())
            # addTo
            addTo = addToStatement.addTo()
            if addTo:
                res["identifier_2"] = []
                res["literal_2"] = []
                for at in addTo:
                    for a in at.getChildren():
                        if isinstance(a, CobolIsuzuParser.IdentifierContext):
                            # res["identifier_2"].append(a.getText())
                            res["identifier_2"].append(
                                get_original_code_content(
                                    self.parser,
                                    a.start.tokenIndex,
                                    a.stop.tokenIndex,
                                )
                            )
                        elif isinstance(a, CobolIsuzuParser.LiteralContext):
                            res["literal_2"].append(a.getText())
                        elif isinstance(a, CobolIsuzuParser.FigurativeConstantContext):
                            res["literal_2"].append(a.getText())

        # AddToGiving
        elif CobolIsuzuParser.AddToGivingStatementContext in children:
            addToGivingStatement = ctx.addToGivingStatement()
            # addFrom
            addFrom = addToGivingStatement.addFrom()
            if addFrom:
                res["identifier_1"] = []
                res["literal_1"] = []
                for af in addFrom:
                    for a in af.getChildren():
                        if isinstance(a, CobolIsuzuParser.IdentifierContext):
                            # res["identifier_1"].append(a.getText())
                            res["identifier_1"].append(
                                get_original_code_content(
                                    self.parser,
                                    a.start.tokenIndex,
                                    a.stop.tokenIndex,
                                )
                            )
                        elif isinstance(a, CobolIsuzuParser.LiteralContext):
                            res["literal_1"].append(a.getText())
            # addToGiving
            addToGiving = addToGivingStatement.addToGiving()
            if addToGiving:
                res["identifier_2"] = []
                res["literal_2"] = []
                for at in addToGiving:
                    for a in at.getChildren():
                        if isinstance(a, CobolIsuzuParser.IdentifierContext):
                            # res["identifier_2"].append(a.getText())
                            res["identifier_2"].append(
                                get_original_code_content(
                                    self.parser,
                                    a.start.tokenIndex,
                                    a.stop.tokenIndex,
                                )
                            )
                        elif isinstance(a, CobolIsuzuParser.LiteralContext):
                            res["literal_2"].append(a.getText())
                        elif isinstance(a, CobolIsuzuParser.FigurativeConstantContext):
                            res["literal_2"].append(a.getText())
            # addGiving
            addGiving = addToGivingStatement.addGiving()
            if addGiving:
                res["identifier_3"] = []
                res["literal_3"] = []
                for ag in addGiving:
                    for a in ag.getChildren():
                        if isinstance(a, CobolIsuzuParser.IdentifierContext):
                            # res["identifier_3"].append(a.getText())
                            res["identifier_3"].append(
                                get_original_code_content(
                                    self.parser,
                                    a.start.tokenIndex,
                                    a.stop.tokenIndex,
                                )
                            )
                        elif isinstance(a, CobolIsuzuParser.LiteralContext):
                            res["literal_3"].append(a.getText())

        return res

    def visitAddStatement(self, ctx: CobolIsuzuParser.AddStatementContext):
        res = self.assessAddStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolIsuzuParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessAcceptFromMessageCountStatement(
        self, ctx: CobolIsuzuParser.AcceptMessageCountStatementContext
    ):
        tag = "AcceptFromMessageCountStatement"

        accept_statement_context: CobolIsuzuParser.AcceptStatementContext = (
            ctx.parentCtx
        )
        identifier = accept_statement_context.identifier()

        raw = get_original_code_content(
            self.parser,
            accept_statement_context.start.tokenIndex,
            accept_statement_context.stop.tokenIndex,
        )
        start_token = ctx.start
        stop_token = ctx.stop

        return {
            "tag": tag,
            "raw": raw,
            "start_line": start_token.line,
            "stop_line": stop_token.line,
            "start_idx": start_token.start,
            "stop_idx": stop_token.stop,
            "identifier": identifier.getText() if identifier else "",
        }

    def visitAcceptMessageCountStatement(
        self, ctx: CobolIsuzuParser.AcceptMessageCountStatementContext
    ):
        res = self.assessAcceptFromMessageCountStatement(ctx)

        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolIsuzuParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def assessAcceptFromMnemonicStatement(
        self, ctx: CobolIsuzuParser.AcceptFromMnemonicStatementContext
    ):
        tag = "AcceptFromMnemonicStatement"
        mnemonic = ctx.getChild(1)

        accept_statement_context: CobolIsuzuParser.AcceptStatementContext = (
            ctx.parentCtx
        )

        identifier = accept_statement_context.identifier()

        raw = get_original_code_content(
            self.parser,
            accept_statement_context.start.tokenIndex,
            accept_statement_context.stop.tokenIndex,
        )
        start_token = ctx.start
        stop_token = ctx.stop

        return {
            "tag": tag,
            "raw": raw,
            "start_line": start_token.line,
            "stop_line": stop_token.line,
            "start_idx": start_token.start,
            "stop_idx": stop_token.stop,
            "identifier": identifier.getText() if identifier else "",
            "mnemonic_name": mnemonic.getText() if mnemonic else "",
        }

    def visitAcceptFromMnemonicStatement(
        self, ctx: CobolIsuzuParser.AcceptFromMnemonicStatementContext
    ):
        res = self.assessAcceptFromMnemonicStatement(ctx)

        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolIsuzuParser.SentenceContext):
            self.statements.append(res)

        return self.visitChildren(ctx)

    def assessAcceptFromEscapeKeyStatement(
        self, ctx: CobolIsuzuParser.AcceptFromEscapeKeyStatementContext
    ):
        tag = "AcceptFromEscapeKeyStatement"

        accept_statement_context: CobolIsuzuParser.AcceptStatementContext = (
            ctx.parentCtx
        )
        identifier = accept_statement_context.identifier()

        raw = get_original_code_content(
            self.parser,
            accept_statement_context.start.tokenIndex,
            accept_statement_context.stop.tokenIndex,
        )
        start_token = ctx.start
        stop_token = ctx.stop

        return {
            "tag": tag,
            "raw": raw,
            "start_line": start_token.line,
            "stop_line": stop_token.line,
            "start_idx": start_token.start,
            "stop_idx": stop_token.stop,
            "identifier": identifier.getText() if identifier else "",
        }

    def visitAcceptFromEscapeKeyStatement(
        self, ctx: CobolIsuzuParser.AcceptFromEscapeKeyStatementContext
    ):
        res = self.assessAcceptFromEscapeKeyStatement(ctx)

        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolIsuzuParser.SentenceContext):
            self.statements.append(res)

        return self.visitChildren(ctx)

    def assessAcceptStatement(self, ctx: CobolIsuzuParser.AcceptStatementContext):
        tag = "AcceptStatement"

        identifier = recursive_find_first_child_by_type(
            ctx, CobolIsuzuParser.IdentifierContext
        )

        raw = get_original_code_content(
            self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex
        )

        start_token = ctx.start
        stop_token = ctx.stop

        return {
            "tag": tag,
            "raw": raw,
            "start_line": start_token.line,
            "stop_line": stop_token.line,
            "start_idx": start_token.start,
            "stop_idx": stop_token.stop,
            "identifier": identifier.getText() if identifier else "",
        }

    def visitAcceptStatement(self, ctx: CobolIsuzuParser.AcceptStatementContext):

        # ignore other accept statements
        if (
            ctx.acceptFromDateStatement()
            or ctx.acceptFromMnemonicStatement()
            or ctx.acceptFromEscapeKeyStatement()
            or ctx.acceptMessageCountStatement()
        ):
            return self.visitChildren(ctx)

        res = self.assessAcceptStatement(ctx)

        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )

        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolIsuzuParser.SentenceContext):
            self.statements.append(res)

        self.statements.append(res)

        return self.visitChildren(ctx)
