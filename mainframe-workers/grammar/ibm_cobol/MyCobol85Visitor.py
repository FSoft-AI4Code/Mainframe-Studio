# Generated from ./src/mainframe_migration/parser/grammar/ibm_cobol/Cobol85.g4 by ANTLR 4.13.2
from typing import List

from grammar.common.base_cobol_schemas import (
    CalledProgram,
    CobolProgramVariables,
    CopybookReplace,
    DatabaseEntry,
    Division,
    FileControlEntry,
    FileDescriptionEntry,
    ImportedCopybook,
    Paragraph,
    ProcedureSection,
)
from grammar.common.cobol_statement_assessor import CobolStatementAssessor
from grammar.utils import (
    find_all_children_by_type,
    find_parent_by_type,
    get_original_code_content,
    recursive_find_first_child_by_type,
)

from .Cobol85Parser import Cobol85Parser
from .Cobol85Visitor import Cobol85Visitor
from .Cobol85VisitorHelper import extract_cobol_variable


class MyCobol85Visitor(Cobol85Visitor):

    def __init__(self, parser: Cobol85Parser):

        self.parser = parser

        self.program_id = ""
        self.copybook_list: List[ImportedCopybook] = []
        self.called_program_list: List[CalledProgram] = []
        self.file_control_list: List[FileControlEntry] = []
        self.file_description_list: List[FileDescriptionEntry] = []
        self.variable_list = CobolProgramVariables(
            working_storage=[], linkage_section=[]
        )
        self.working_storage_copybooks: list[ImportedCopybook] = []
        self.division_list: List[Division] = []
        self.section_list: List[ProcedureSection] = []
        self.paragraph_list: List[Paragraph] = []
        self.statements = []
        self.database_list: List[DatabaseEntry] = []
        self._statement_assessor = CobolStatementAssessor()

    # Custom visit Methods and Their Corresponding Access Methods

    # SECTION LIST

    def visitProcedureSection(self, ctx: Cobol85Parser.ProcedureSectionContext):
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

    def visitParagraph(self, ctx: Cobol85Parser.ParagraphContext):
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
        self, ctx: Cobol85Parser.IdentificationDivisionContext
    ):
        self.division_list.append(
            Division(
                division_name="IDENTIFICATION DIVISION",
                start_line=ctx.start.line,
                stop_line=ctx.stop.line,
            )
        )
        return self.visitChildren(ctx)

    def visitEnvironmentDivision(self, ctx: Cobol85Parser.EnvironmentDivisionContext):
        self.division_list.append(
            Division(
                division_name="ENVIRONMENT DIVISION",
                start_line=ctx.start.line,
                stop_line=ctx.stop.line,
            )
        )
        return self.visitChildren(ctx)

    def visitDataDivision(self, ctx: Cobol85Parser.DataDivisionContext):
        self.division_list.append(
            Division(
                division_name="DATA DIVISION",
                start_line=ctx.start.line,
                stop_line=ctx.stop.line,
            )
        )
        return self.visitChildren(ctx)

    def visitProcedureDivision(self, ctx: Cobol85Parser.ProcedureDivisionContext):
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
        self, ctx: Cobol85Parser.WorkingStorageSectionContext
    ):
        data_description_entry_list: List[Cobol85Parser.DataDescriptionEntryContext] = (
            ctx.dataDescriptionEntry()
        )

        for data_description_entry in data_description_entry_list:
            entry = data_description_entry.getChild(0)

            if isinstance(entry, Cobol85Parser.CopyStatementContext):
                copy_source = recursive_find_first_child_by_type(
                    entry, Cobol85Parser.CopySourceContext
                )

                if copy_source is None:
                    raise ValueError(
                        f"File name of COPY statement {get_original_code_content(self.parser, entry.start.tokenIndex, entry.stop.tokenIndex)}"
                    )

                copy_name = copy_source.getChild(0)
                replace_clauses = find_all_children_by_type(
                    entry, Cobol85Parser.ReplaceClauseContext
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

                self.working_storage_copybooks.append(copybook)
                continue

            entry = data_description_entry.getChild(0)

            if isinstance(
                entry,
                (
                    Cobol85Parser.DataDescriptionEntryFormat1Context,
                    Cobol85Parser.DataDescriptionEntryFormat2Context,
                    Cobol85Parser.DataDescriptionEntryFormat3Context,
                ),
            ):
                variable = extract_cobol_variable(entry)
                self.variable_list.working_storage.append(variable)

        return self.visitChildren(ctx)

    def visitLinkageSection(self, ctx: Cobol85Parser.LinkageSectionContext):
        data_description_entry_list: List[Cobol85Parser.DataDescriptionEntryContext] = (
            ctx.dataDescriptionEntry()
        )

        for data_description_entry in data_description_entry_list:
            if isinstance(
                data_description_entry.getChild(0),
                Cobol85Parser.CopyStatementContext,
            ):
                continue

            entry = data_description_entry.getChild(0)
            if isinstance(
                entry,
                (
                    Cobol85Parser.DataDescriptionEntryFormat1Context,
                    Cobol85Parser.DataDescriptionEntryFormat2Context,
                    Cobol85Parser.DataDescriptionEntryFormat3Context,
                ),
            ):
                variable = extract_cobol_variable(entry)
                self.variable_list.linkage_section.append(variable)
        return self.visitChildren(ctx)

    # FILE DESCRIPTION LIST

    def visitFileDescriptionEntry(self, ctx: Cobol85Parser.FileDescriptionEntryContext):
        code_content = get_original_code_content(
            self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex
        )

        file_name = recursive_find_first_child_by_type(
            ctx, Cobol85Parser.FileNameContext
        )

        if file_name is None:
            raise ValueError(
                f"File name is missing for FD statement {get_original_code_content(self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)}"
            )

        data_description_entries = find_all_children_by_type(
            ctx, Cobol85Parser.DataDescriptionEntryContext
        )

        variables = []
        copybooks = []

        for entry in data_description_entries:
            entry = entry.getChild(0)

            # copy statement
            if isinstance(entry, Cobol85Parser.CopyStatementContext):
                copy_source = recursive_find_first_child_by_type(
                    ctx, Cobol85Parser.CopySourceContext
                )

                if copy_source is None:
                    raise ValueError(
                        f"File name of COPY statement {get_original_code_content(self.parser, entry.start.tokenIndex, entry.stop.tokenIndex)}"
                    )

                copy_name = copy_source.getChild(0)

                replace_clauses = find_all_children_by_type(
                    entry, Cobol85Parser.ReplaceClauseContext
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
            variable = extract_cobol_variable(entry)

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

    def visitFileControlEntry(self, ctx: Cobol85Parser.FileControlEntryContext):
        select_clause = recursive_find_first_child_by_type(
            ctx, Cobol85Parser.SelectClauseContext
        )

        if select_clause is None:
            raise ValueError(
                f"Select clause of statement '{ctx.getText()}' is missing."
            )

        file_name = recursive_find_first_child_by_type(
            select_clause, Cobol85Parser.FileNameContext
        )

        if file_name is None:
            raise ValueError(
                f"File name in select clause of statement'{ctx.getText()}' is missing."
            )

        file_control_clause_list: List[Cobol85Parser.FileControlClauseContext] = (
            ctx.fileControlClause()
        )

        assignment_name = None
        for file_control_clause in file_control_clause_list:
            assign_clause: Cobol85Parser.AssignClauseContext = (
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
            ctx, Cobol85Parser.AccessModeClauseContext
        )
        organization_clause = recursive_find_first_child_by_type(
            ctx, Cobol85Parser.OrganizationClauseContext
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

    def visitDataBaseSectionEntry(self, ctx: Cobol85Parser.DataBaseSectionEntryContext):
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
            DatabaseEntry(
                database_name=database_name,
                invoke_name=invoke_name,
                using_names=[],
            )
        )
        return self.visitChildren(ctx)

    def visitOpenInputStatement(self, ctx: Cobol85Parser.OpenInputStatementContext):
        open_input_list: List[Cobol85Parser.OpenInputContext] = ctx.openInput()
        for open_input in open_input_list:
            file_control_name = recursive_find_first_child_by_type(
                open_input, Cobol85Parser.FileNameContext
            )

            if file_control_name is None:
                raise ValueError(
                    f"Missing file name in OPEN statement {get_original_code_content(self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)}"
                )

            for file_control in self.file_control_list:
                if file_control.file_name == file_control_name.getText():
                    file_control.open_type = "INPUT"
        return self.visitChildren(ctx)

    def visitOpenOutputStatement(self, ctx: Cobol85Parser.OpenOutputStatementContext):

        open_output_list: List[Cobol85Parser.OpenOutputContext] = ctx.openOutput()

        for open_output in open_output_list:
            file_control_name = recursive_find_first_child_by_type(
                open_output, Cobol85Parser.FileNameContext
            )

            if file_control_name is None:
                raise ValueError(
                    f"Missing file name in OPEN statement {get_original_code_content(self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)}"
                )

            for file_control in self.file_control_list:
                if file_control.file_name == file_control_name.getText():
                    file_control.open_type = "OUTPUT"
        return self.visitChildren(ctx)

    def visitOpenIOStatement(self, ctx: Cobol85Parser.OpenIOStatementContext):
        file_name_list: List[Cobol85Parser.FileNameContext] = ctx.fileName()

        for file_name in file_name_list:
            file_control_name = recursive_find_first_child_by_type(
                file_name, Cobol85Parser.FileNameContext
            )

            if file_control_name is None:
                raise ValueError(
                    f"Missing file name in OPEN statement {get_original_code_content(self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)}"
                )

            for file_control in self.file_control_list:
                if file_control.file_name == file_control_name.getText():
                    file_control.open_type = "I-O"
        return self.visitChildren(ctx)

    def visitOpenExtendStatement(self, ctx: Cobol85Parser.OpenExtendStatementContext):
        file_name_list: List[Cobol85Parser.FileNameContext] = ctx.fileName()

        for file_name in file_name_list:
            file_control_name = recursive_find_first_child_by_type(
                file_name, Cobol85Parser.FileNameContext
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

    def visitEvaluateStatement(self, ctx: Cobol85Parser.EvaluateStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, Cobol85Parser.SentenceContext):
            self.statements.append(res)

        return self.visitChildren(ctx)

    def visitExecCicsStatement2(self, ctx: Cobol85Parser.ExecCicsStatement2Context):
        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)
        return self.visitChildren(ctx)

    def visitExecSqlStatement2(self, ctx: Cobol85Parser.ExecSqlStatement2Context):
        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)
        return self.visitChildren(ctx)

    def visitCloseStatement(self, ctx: Cobol85Parser.CloseStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, Cobol85Parser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def visitMoveStatement(self, ctx: Cobol85Parser.MoveStatementContext):

        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)
        return self.visitChildren(ctx)

    def visitMultiplyStatement(self, ctx: Cobol85Parser.MultiplyStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, Cobol85Parser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def visitWriteStatement(self, ctx: Cobol85Parser.WriteStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)

        return self.visitChildren(ctx)

    def visitCallStatement(self, ctx: Cobol85Parser.CallStatementContext):
        res = self._statement_assessor.assess_statement(ctx)

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

        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, Cobol85Parser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def visitRewriteStatement(self, ctx: Cobol85Parser.RewriteStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)
        return self.visitChildren(ctx)

    def visitReadStatement(self, ctx: Cobol85Parser.ReadStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def visitPerformStatement(self, ctx: Cobol85Parser.PerformStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def visitIfStatement(self, ctx: Cobol85Parser.IfStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def visitOpenStatement(self, ctx: Cobol85Parser.OpenStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, Cobol85Parser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def visitSetStatement(self, ctx: Cobol85Parser.SetStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)
        return self.visitChildren(ctx)

    def visitSubtractStatement(self, ctx: Cobol85Parser.SubtractStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)
        return self.visitChildren(ctx)

    def visitStringStatement(self, ctx: Cobol85Parser.StringStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def visitSearchStatement(self, ctx: Cobol85Parser.SearchStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Cobol85Parser#acceptFromDateStatement.
    def visitAcceptFromDateStatement(
        self, ctx: Cobol85Parser.AcceptFromDateStatementContext
    ):
        return self.visitChildren(ctx)

    def visitInspectStatement(self, ctx: Cobol85Parser.InspectStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)
        return self.visitChildren(ctx)

    def visitInitializeStatement(self, ctx: Cobol85Parser.InitializeStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Cobol85Parser#cancelStatement.
    def visitCancelStatement(self, ctx: Cobol85Parser.CancelStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)
        return self.visitChildren(ctx)

    def visitGoToStatement(self, ctx: Cobol85Parser.GoToStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)
        return self.visitChildren(ctx)

    def visitGobackStatement(self, ctx: Cobol85Parser.GobackStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Cobol85Parser#deleteStatement.
    def visitDeleteStatement(self, ctx: Cobol85Parser.DeleteStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Cobol85Parser#divideStatement.
    def visitDivideStatement(self, ctx: Cobol85Parser.DivideStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)
        return self.visitChildren(ctx)

    def visitExitStatement(self, ctx: Cobol85Parser.ExitStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Cobol85Parser#returnStatement.
    def visitReturnStatement(self, ctx: Cobol85Parser.ReturnStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Cobol85Parser#releaseStatement.
    def visitReleaseStatement(self, ctx: Cobol85Parser.ReleaseStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)
        return self.visitChildren(ctx)

    def visitDisplayStatement(self, ctx: Cobol85Parser.DisplayStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Cobol85Parser#sortStatement.
    def visitSortStatement(self, ctx: Cobol85Parser.SortStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)
        return self.visitChildren(ctx)

    # COPYBOOK LIST

    def visitCopyStatement(self, ctx: Cobol85Parser.CopyStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)

        # extract dependency
        copy_source = recursive_find_first_child_by_type(
            ctx, Cobol85Parser.CopySourceContext
        )

        if copy_source is None:
            raise ValueError(
                f"File name of COPY statement {get_original_code_content(self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)}"
            )

        copy_name = copy_source.getChild(0)

        replace_clauses = find_all_children_by_type(
            ctx, Cobol85Parser.ReplaceClauseContext
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

    # Visit a parse tree produced by Cobol85Parser#startStatement.
    def visitStartStatement(self, ctx: Cobol85Parser.StartStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Cobol85Parser#stopStatement.
    def visitStopStatement(self, ctx: Cobol85Parser.StopStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)

        return self.visitChildren(ctx)

    def visitContinueStatement(self, ctx: Cobol85Parser.ContinueStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)
        return self.visitChildren(ctx)

    def visitComputeStatement(self, ctx: Cobol85Parser.ComputeStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)
        return self.visitChildren(ctx)

    def visitAlterStatement(self, ctx: Cobol85Parser.AlterStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Cobol85Parser#unstringStatement.
    def visitUnstringStatement(self, ctx: Cobol85Parser.UnstringStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)
        return self.visitChildren(ctx)

    def visitAddStatement(self, ctx: Cobol85Parser.AddStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)
        return self.visitChildren(ctx)

    def visitAcceptMessageCountStatement(
        self, ctx: Cobol85Parser.AcceptMessageCountStatementContext
    ):
        return self.visitChildren(ctx)

    def visitAcceptFromMnemonicStatement(
        self, ctx: Cobol85Parser.AcceptFromMnemonicStatementContext
    ):
        return self.visitChildren(ctx)

    def visitAcceptFromEscapeKeyStatement(
        self, ctx: Cobol85Parser.AcceptFromEscapeKeyStatementContext
    ):
        return self.visitChildren(ctx)

    def visitAcceptStatement(self, ctx: Cobol85Parser.AcceptStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        if res:
            grandparent = ctx.parentCtx.parentCtx
            if isinstance(grandparent, Cobol85Parser.SentenceContext):
                self.statements.append(res)

        return self.visitChildren(ctx)
