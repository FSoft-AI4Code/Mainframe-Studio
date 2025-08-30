# Generated from ./src/mainframe_migration/parser/grammar/ibm_cobol/Cobol85.g4 by ANTLR 4.13.2
from typing import List

from grammar.common.base_cobol_schemas import (
    CalledProgram,
    CobolProgramVariables,
    CopybookReplace,
    DatabaseEntry,
    ImportedCopybook,
    Paragraph,
    ProcedureSection,
)
from grammar.common.cobol_statement_assessor import CobolStatementAssessor
from grammar.copybook.CopyBookParser import CopyBookParser
from grammar.copybook.CopyBookVisitor import CopyBookVisitor
from grammar.copybook.CopyBookVisitorHelper import extract_cobol_variable
from grammar.utils import (
    find_all_children_by_type,
    find_parent_by_type,
    get_original_code_content,
    recursive_find_first_child_by_type,
)


class CopyBookVisitorImp(CopyBookVisitor):

    def __init__(self, parser: CopyBookParser):

        self.parser = parser

        self.program_id = "COPYBOOK"
        self.copybook_list: List[ImportedCopybook] = []
        self.called_program_list: List[CalledProgram] = []
        self.variable_list = CobolProgramVariables(
            working_storage=[], linkage_section=[]
        )
        self.working_storage_copybooks: list[ImportedCopybook] = []
        self.section_list: List[ProcedureSection] = []
        self.paragraph_list: List[Paragraph] = []
        self.statements = []
        self.database_list: List[DatabaseEntry] = []

        self._statement_assessor = CobolStatementAssessor()

    # Custom visit Methods and Their Corresponding Access Methods

    # SECTION LIST

    def visitProcedureSection(self, ctx: CopyBookParser.ProcedureSectionContext):
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

    def visitParagraph(self, ctx: CopyBookParser.ParagraphContext):
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
        self, ctx: CopyBookParser.IdentificationDivisionContext
    ):
        return self.visitChildren(ctx)

    def visitEnvironmentDivision(self, ctx: CopyBookParser.EnvironmentDivisionContext):
        return self.visitChildren(ctx)

    def visitDataDivision(self, ctx: CopyBookParser.DataDivisionContext):
        return self.visitChildren(ctx)

    def visitProcedureDivision(self, ctx: CopyBookParser.ProcedureDivisionContext):
        return self.visitChildren(ctx)

    # VARIABLE LIST

    def visitWorkingStorageSection(
        self, ctx: CopyBookParser.WorkingStorageSectionContext
    ):
        data_description_entry_list: List[
            CopyBookParser.DataDescriptionEntryContext
        ] = ctx.dataDescriptionEntry()

        for data_description_entry in data_description_entry_list:
            entry = data_description_entry.getChild(0)

            if isinstance(entry, CopyBookParser.CopyStatementContext):
                copy_source = recursive_find_first_child_by_type(
                    entry, CopyBookParser.CopySourceContext
                )

                if copy_source is None:
                    raise ValueError(
                        f"File name of COPY statement {get_original_code_content(self.parser, entry.start.tokenIndex, entry.stop.tokenIndex)}"
                    )

                copy_name = copy_source.getChild(0)
                replace_clauses = find_all_children_by_type(
                    entry, CopyBookParser.ReplaceClauseContext
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
                    CopyBookParser.DataDescriptionEntryFormat1Context,
                    CopyBookParser.DataDescriptionEntryFormat2Context,
                    CopyBookParser.DataDescriptionEntryFormat3Context,
                ),
            ):
                variable = extract_cobol_variable(entry)
                self.variable_list.working_storage.append(variable)

        return self.visitChildren(ctx)

    def visitLinkageSection(self, ctx: CopyBookParser.LinkageSectionContext):
        data_description_entry_list: List[
            CopyBookParser.DataDescriptionEntryContext
        ] = ctx.dataDescriptionEntry()

        for data_description_entry in data_description_entry_list:
            if isinstance(
                data_description_entry.getChild(0),
                CopyBookParser.CopyStatementContext,
            ):
                continue

            entry = data_description_entry.getChild(0)
            if isinstance(
                entry,
                (
                    CopyBookParser.DataDescriptionEntryFormat1Context,
                    CopyBookParser.DataDescriptionEntryFormat2Context,
                    CopyBookParser.DataDescriptionEntryFormat3Context,
                ),
            ):
                variable = extract_cobol_variable(entry)
                self.variable_list.linkage_section.append(variable)
        return self.visitChildren(ctx)

    # FILE DESCRIPTION LIST

    def visitFileDescriptionEntry(
        self, ctx: CopyBookParser.FileDescriptionEntryContext
    ):
        code_content = get_original_code_content(
            self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex
        )

        file_name = recursive_find_first_child_by_type(
            ctx, CopyBookParser.FileNameContext
        )

        if file_name is None:
            raise ValueError(
                f"File name is missing for FD statement {get_original_code_content(self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)}"
            )

        data_description_entries = find_all_children_by_type(
            ctx, CopyBookParser.DataDescriptionEntryContext
        )

        variables = []
        copybooks = []

        for entry in data_description_entries:
            entry = entry.getChild(0)

            # copy statement
            if isinstance(entry, CopyBookParser.CopyStatementContext):
                copy_source = recursive_find_first_child_by_type(
                    ctx, CopyBookParser.CopySourceContext
                )

                if copy_source is None:
                    raise ValueError(
                        f"File name of COPY statement {get_original_code_content(self.parser, entry.start.tokenIndex, entry.stop.tokenIndex)}"
                    )

                copy_name = copy_source.getChild(0)

                replace_clauses = find_all_children_by_type(
                    entry, CopyBookParser.ReplaceClauseContext
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

        return self.visitChildren(ctx)

    # FILE CONTROL LIST

    def visitFileControlEntry(self, ctx: CopyBookParser.FileControlEntryContext):
        return self.visitChildren(ctx)

    def visitDataBaseSectionEntry(
        self, ctx: CopyBookParser.DataBaseSectionEntryContext
    ):
        return self.visitChildren(ctx)

    def visitOpenInputStatement(self, ctx: CopyBookParser.OpenInputStatementContext):
        return self.visitChildren(ctx)

    def visitOpenOutputStatement(self, ctx: CopyBookParser.OpenOutputStatementContext):
        return self.visitChildren(ctx)

    def visitOpenIOStatement(self, ctx: CopyBookParser.OpenIOStatementContext):
        return self.visitChildren(ctx)

    def visitOpenExtendStatement(self, ctx: CopyBookParser.OpenExtendStatementContext):
        return self.visitChildren(ctx)

    # STATEMENTS LIST

    def visitEvaluateStatement(self, ctx: CopyBookParser.EvaluateStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)

        return self.visitChildren(ctx)

    def visitExecCicsStatement2(self, ctx: CopyBookParser.ExecCicsStatement2Context):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def visitCloseStatement(self, ctx: CopyBookParser.CloseStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def visitMoveStatement(self, ctx: CopyBookParser.MoveStatementContext):

        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def visitMultiplyStatement(self, ctx: CopyBookParser.MultiplyStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def visitWriteStatement(self, ctx: CopyBookParser.WriteStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)

        return self.visitChildren(ctx)

    def visitCallStatement(self, ctx: CopyBookParser.CallStatementContext):
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
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def visitRewriteStatement(self, ctx: CopyBookParser.RewriteStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def visitReadStatement(self, ctx: CopyBookParser.ReadStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def visitPerformStatement(self, ctx: CopyBookParser.PerformStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def visitIfStatement(self, ctx: CopyBookParser.IfStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def visitOpenStatement(self, ctx: CopyBookParser.OpenStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def visitSetStatement(self, ctx: CopyBookParser.SetStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def visitSubtractStatement(self, ctx: CopyBookParser.SubtractStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def visitStringStatement(self, ctx: CopyBookParser.StringStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def visitSearchStatement(self, ctx: CopyBookParser.SearchStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CopyBookParser#acceptFromDateStatement.
    def visitAcceptFromDateStatement(
        self, ctx: CopyBookParser.AcceptFromDateStatementContext
    ):
        return self.visitChildren(ctx)

    def visitInspectStatement(self, ctx: CopyBookParser.InspectStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def visitInitializeStatement(self, ctx: CopyBookParser.InitializeStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CopyBookParser#cancelStatement.
    def visitCancelStatement(self, ctx: CopyBookParser.CancelStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def visitGoToStatement(self, ctx: CopyBookParser.GoToStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def visitGobackStatement(self, ctx: CopyBookParser.GobackStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CopyBookParser#deleteStatement.
    def visitDeleteStatement(self, ctx: CopyBookParser.DeleteStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CopyBookParser#divideStatement.
    def visitDivideStatement(self, ctx: CopyBookParser.DivideStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def visitExitStatement(self, ctx: CopyBookParser.ExitStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CopyBookParser#returnStatement.
    def visitReturnStatement(self, ctx: CopyBookParser.ReturnStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CopyBookParser#releaseStatement.
    def visitReleaseStatement(self, ctx: CopyBookParser.ReleaseStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def visitDisplayStatement(self, ctx: CopyBookParser.DisplayStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CopyBookParser#sortStatement.
    def visitSortStatement(self, ctx: CopyBookParser.SortStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    # COPYBOOK LIST

    def visitCopyStatement(self, ctx: CopyBookParser.CopyStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)

        # extract dependency
        copy_source = recursive_find_first_child_by_type(
            ctx, CopyBookParser.CopySourceContext
        )

        if copy_source is None:
            raise ValueError(
                f"File name of COPY statement {get_original_code_content(self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)}"
            )

        copy_name = copy_source.getChild(0)

        replace_clauses = find_all_children_by_type(
            ctx, CopyBookParser.ReplaceClauseContext
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

    # Visit a parse tree produced by CopyBookParser#startStatement.
    def visitStartStatement(self, ctx: CopyBookParser.StartStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CopyBookParser#stopStatement.
    def visitStopStatement(self, ctx: CopyBookParser.StopStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)

        return self.visitChildren(ctx)

    def visitContinueStatement(self, ctx: CopyBookParser.ContinueStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def visitComputeStatement(self, ctx: CopyBookParser.ComputeStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def visitAlterStatement(self, ctx: CopyBookParser.AlterStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CopyBookParser#unstringStatement.
    def visitUnstringStatement(self, ctx: CopyBookParser.UnstringStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def visitAddStatement(self, ctx: CopyBookParser.AddStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def visitAcceptMessageCountStatement(
        self, ctx: CopyBookParser.AcceptMessageCountStatementContext
    ):
        return self.visitChildren(ctx)

    def visitAcceptFromMnemonicStatement(
        self, ctx: CopyBookParser.AcceptFromMnemonicStatementContext
    ):
        return self.visitChildren(ctx)

    def visitAcceptFromEscapeKeyStatement(
        self, ctx: CopyBookParser.AcceptFromEscapeKeyStatementContext
    ):
        return self.visitChildren(ctx)

    def visitAcceptStatement(self, ctx: CopyBookParser.AcceptStatementContext):
        res = self._statement_assessor.assess_statement(ctx)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CopyBookParser.SentenceContext):
            self.statements.append(res)

        return self.visitChildren(ctx)
