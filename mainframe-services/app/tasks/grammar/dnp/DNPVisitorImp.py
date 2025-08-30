# Generated from ./app/tasks/grammar/dnp/DNP.g4 by ANTLR 4.13.2
from typing import List

from antlr4 import ParserRuleContext, TerminalNode
from loguru import logger

from app.tasks.grammar.common.base_cobol_schemas import (
    CobolVariable,
    CopybookReplace,
    FileControlEntry,
    FileDescriptionEntry,
    ImportedCopybook,
    Paragraph,
)
from app.tasks.grammar.dnp.dnp_helpers import extract_cobol_variable
from app.tasks.grammar.dnp.DNPParser import DNPParser
from app.tasks.grammar.dnp.DNPVisitor import DNPVisitor
from app.tasks.grammar.utils import (
    get_original_code_content,
    get_paragraph_section_of_cobol_statement,
)

from ..utils import (
    find_all_children_by_type,
    find_parent_by_type,
    get_original_code_content,
    recursive_find_first_child_by_type,
)

# This class defines a complete generic visitor for a parse tree produced by DNPParser.


class DNPVisitorImp(DNPVisitor):

    def __init__(self, parser: DNPParser):
        self.parser = parser
        self.program_id = ""
        self.copybook_list: list[ImportedCopybook] = []
        self.file_control_list: list[FileControlEntry] = []
        self.file_description_list: list[FileDescriptionEntry] = []
        self.variable_list: list[CobolVariable] = []
        self.paragraph_list: list[Paragraph] = []
        self.statements = []
        self.func = {
            "AcceptStatement": self.assessAcceptStatement,
            "AcceptFromDateStatement": self.assessAcceptFromDateStatement,
            "AcceptFromEscapeKeyStatement": self.assessAcceptFromEscapeKeyStatement,
            "AcceptFromMnemonicStatement": self.assessAcceptFromMnemonicStatement,
            "AcceptFromMessageCountStatement": self.assessAcceptFromMessageCountStatement,
            "EvaluateStatementContext": self.assessEvaluateStatement,
            "AddStatementContext": self.assessAddStatement,
            "AlterStatementContext": self.assessAlterStatement,
            "CallStatementContext": self.assessCallStatement,
            "ChangeStatementContext": self.assessChangeStatement,
            "CloseStatementContext": self.assessCloseStatement,
            "ComputeStatementContext": self.assessComputeStatement,
            "ContinueStatementContext": self.assessContinueStatement,
            "CopyStatementContext": self.assessCopyStatement,
            "CreateStatementContext": self.assessCreateStatement,
            "DisplayStatementContext": self.assessDisplayStatement,
            # "ExecCicsStatement2Context": self.assessExecCicsStatement2,
            "ExitStatementContext": self.assessExitStatement,
            "FreeStatementContext": self.assessFreeStatement,
            "FindStatementContext": self.assessFindStatement,
            "LockStatementContext": self.assessLockStatement,
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
            "TransactionStatementContext": self.assessTransactionStatement,
            "WaitStatementContext": self.assessWaitStatement,
            "WriteStatementContext": self.assessWriteStatement,
            "OpenStatementContext": self.assessOpenStatement,
            "IfStatementContext": self.assessIfStatement,
            "PerformStatementContext": self.assessPerformStatement,
            "ReadStatementContext": self.assessReadStatement,
            "RewriteStatementContext": self.assessRewriteStatement,
        }

    # Visit a parse tree produced by DNPParser#startRule.
    def visitStartRule(self, ctx: DNPParser.StartRuleContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#compilationUnit.
    def visitCompilationUnit(self, ctx: DNPParser.CompilationUnitContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#programUnit.
    def visitProgramUnit(self, ctx: DNPParser.ProgramUnitContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#endProgramStatement.
    def visitEndProgramStatement(self, ctx: DNPParser.EndProgramStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#identificationDivision.
    def visitIdentificationDivision(self, ctx: DNPParser.IdentificationDivisionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#identificationDivisionBody.
    def visitIdentificationDivisionBody(
        self, ctx: DNPParser.IdentificationDivisionBodyContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#programIdParagraph.
    def visitProgramIdParagraph(self, ctx: DNPParser.ProgramIdParagraphContext):
        program_name = recursive_find_first_child_by_type(
            ctx, DNPParser.ProgramNameContext
        )

        if program_name:
            self.program_id = program_name.getText()
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#author_name.
    def visitAuthor_name(self, ctx: DNPParser.Author_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#authorParagraph.
    def visitAuthorParagraph(self, ctx: DNPParser.AuthorParagraphContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#installationParagraph.
    def visitInstallationParagraph(self, ctx: DNPParser.InstallationParagraphContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dateWrittenParagraph.
    def visitDateWrittenParagraph(self, ctx: DNPParser.DateWrittenParagraphContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dateCompiledParagraph.
    def visitDateCompiledParagraph(self, ctx: DNPParser.DateCompiledParagraphContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#securityParagraph.
    def visitSecurityParagraph(self, ctx: DNPParser.SecurityParagraphContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#remarksParagraph.
    def visitRemarksParagraph(self, ctx: DNPParser.RemarksParagraphContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#environmentDivision.
    def visitEnvironmentDivision(self, ctx: DNPParser.EnvironmentDivisionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#environmentDivisionBody.
    def visitEnvironmentDivisionBody(
        self, ctx: DNPParser.EnvironmentDivisionBodyContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#configurationSection.
    def visitConfigurationSection(self, ctx: DNPParser.ConfigurationSectionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#configurationSectionParagraph.
    def visitConfigurationSectionParagraph(
        self, ctx: DNPParser.ConfigurationSectionParagraphContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#sourceComputerParagraph.
    def visitSourceComputerParagraph(
        self, ctx: DNPParser.SourceComputerParagraphContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#objectComputerParagraph.
    def visitObjectComputerParagraph(
        self, ctx: DNPParser.ObjectComputerParagraphContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#objectComputerClause.
    def visitObjectComputerClause(self, ctx: DNPParser.ObjectComputerClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#memorySizeClause.
    def visitMemorySizeClause(self, ctx: DNPParser.MemorySizeClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#diskSizeClause.
    def visitDiskSizeClause(self, ctx: DNPParser.DiskSizeClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#collatingSequenceClause.
    def visitCollatingSequenceClause(
        self, ctx: DNPParser.CollatingSequenceClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#collatingSequenceClauseAlphanumeric.
    def visitCollatingSequenceClauseAlphanumeric(
        self, ctx: DNPParser.CollatingSequenceClauseAlphanumericContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#collatingSequenceClauseNational.
    def visitCollatingSequenceClauseNational(
        self, ctx: DNPParser.CollatingSequenceClauseNationalContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#segmentLimitClause.
    def visitSegmentLimitClause(self, ctx: DNPParser.SegmentLimitClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#characterSetClause.
    def visitCharacterSetClause(self, ctx: DNPParser.CharacterSetClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#specialNamesParagraph.
    def visitSpecialNamesParagraph(self, ctx: DNPParser.SpecialNamesParagraphContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#specialNameClause.
    def visitSpecialNameClause(self, ctx: DNPParser.SpecialNameClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#alphabetClause.
    def visitAlphabetClause(self, ctx: DNPParser.AlphabetClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#alphabetClauseFormat1.
    def visitAlphabetClauseFormat1(self, ctx: DNPParser.AlphabetClauseFormat1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#alphabetLiterals.
    def visitAlphabetLiterals(self, ctx: DNPParser.AlphabetLiteralsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#alphabetThrough.
    def visitAlphabetThrough(self, ctx: DNPParser.AlphabetThroughContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#alphabetAlso.
    def visitAlphabetAlso(self, ctx: DNPParser.AlphabetAlsoContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#alphabetClauseFormat2.
    def visitAlphabetClauseFormat2(self, ctx: DNPParser.AlphabetClauseFormat2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#channelClause.
    def visitChannelClause(self, ctx: DNPParser.ChannelClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#classClause.
    def visitClassClause(self, ctx: DNPParser.ClassClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#classClauseThrough.
    def visitClassClauseThrough(self, ctx: DNPParser.ClassClauseThroughContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#classClauseFrom.
    def visitClassClauseFrom(self, ctx: DNPParser.ClassClauseFromContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#classClauseTo.
    def visitClassClauseTo(self, ctx: DNPParser.ClassClauseToContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#currencySignClause.
    def visitCurrencySignClause(self, ctx: DNPParser.CurrencySignClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#decimalPointClause.
    def visitDecimalPointClause(self, ctx: DNPParser.DecimalPointClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#defaultComputationalSignClause.
    def visitDefaultComputationalSignClause(
        self, ctx: DNPParser.DefaultComputationalSignClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#defaultDisplaySignClause.
    def visitDefaultDisplaySignClause(
        self, ctx: DNPParser.DefaultDisplaySignClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#environmentSwitchNameClause.
    def visitEnvironmentSwitchNameClause(
        self, ctx: DNPParser.EnvironmentSwitchNameClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#environmentSwitchNameSpecialNamesStatusPhrase.
    def visitEnvironmentSwitchNameSpecialNamesStatusPhrase(
        self, ctx: DNPParser.EnvironmentSwitchNameSpecialNamesStatusPhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#odtClause.
    def visitOdtClause(self, ctx: DNPParser.OdtClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reserveNetworkClause.
    def visitReserveNetworkClause(self, ctx: DNPParser.ReserveNetworkClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#symbolicCharactersClause.
    def visitSymbolicCharactersClause(
        self, ctx: DNPParser.SymbolicCharactersClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#symbolicCharacters.
    def visitSymbolicCharacters(self, ctx: DNPParser.SymbolicCharactersContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#inputOutputSection.
    def visitInputOutputSection(self, ctx: DNPParser.InputOutputSectionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#inputOutputSectionParagraph.
    def visitInputOutputSectionParagraph(
        self, ctx: DNPParser.InputOutputSectionParagraphContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#fileControlParagraph.
    def visitFileControlParagraph(self, ctx: DNPParser.FileControlParagraphContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#fileControlEntry.
    def visitFileControlEntry(self, ctx: DNPParser.FileControlEntryContext):
        select_clause = recursive_find_first_child_by_type(
            ctx, DNPParser.SelectClauseContext
        )

        if select_clause is None:
            raise ValueError(
                f"Select clause of statement '{ctx.getText()}' is missing."
            )

        file_name = recursive_find_first_child_by_type(
            select_clause, DNPParser.FileNameContext
        )

        if file_name is None:
            raise ValueError(
                f"File name in select clause of statement'{ctx.getText()}' is missing."
            )

        assignment_name = recursive_find_first_child_by_type(
            ctx, DNPParser.AssignmentNameContext
        )

        if assignment_name is None:
            # raise ValueError(
            #     f"Assignment name in select clause of statement'{ctx.getText()}' is missing."
            # )
            assignment_name = ""
        else:
            assignment_name = assignment_name.getText()

        file_control = FileControlEntry(
            file_name=file_name.getText(),
            assignment_name=assignment_name,
            code_content=get_original_code_content(
                self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex
            ),
            access_mode="",
        )

        self.file_control_list.append(file_control)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#selectClause.
    def visitSelectClause(self, ctx: DNPParser.SelectClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#fileControlClause.
    def visitFileControlClause(self, ctx: DNPParser.FileControlClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#assignClause.
    def visitAssignClause(self, ctx: DNPParser.AssignClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reserveClause.
    def visitReserveClause(self, ctx: DNPParser.ReserveClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#organizationClause.
    def visitOrganizationClause(self, ctx: DNPParser.OrganizationClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#paddingCharacterClause.
    def visitPaddingCharacterClause(self, ctx: DNPParser.PaddingCharacterClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#recordDelimiterClause.
    def visitRecordDelimiterClause(self, ctx: DNPParser.RecordDelimiterClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#accessModeClause.
    def visitAccessModeClause(self, ctx: DNPParser.AccessModeClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#recordKeyClause.
    def visitRecordKeyClause(self, ctx: DNPParser.RecordKeyClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#alternateRecordKeyClause.
    def visitAlternateRecordKeyClause(
        self, ctx: DNPParser.AlternateRecordKeyClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#passwordClause.
    def visitPasswordClause(self, ctx: DNPParser.PasswordClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#fileStatusClause.
    def visitFileStatusClause(self, ctx: DNPParser.FileStatusClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#relativeKeyClause.
    def visitRelativeKeyClause(self, ctx: DNPParser.RelativeKeyClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#ioControlParagraph.
    def visitIoControlParagraph(self, ctx: DNPParser.IoControlParagraphContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#ioControlClause.
    def visitIoControlClause(self, ctx: DNPParser.IoControlClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#rerunClause.
    def visitRerunClause(self, ctx: DNPParser.RerunClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#rerunEveryRecords.
    def visitRerunEveryRecords(self, ctx: DNPParser.RerunEveryRecordsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#rerunEveryOf.
    def visitRerunEveryOf(self, ctx: DNPParser.RerunEveryOfContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#rerunEveryClock.
    def visitRerunEveryClock(self, ctx: DNPParser.RerunEveryClockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#sameClause.
    def visitSameClause(self, ctx: DNPParser.SameClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#multipleFileClause.
    def visitMultipleFileClause(self, ctx: DNPParser.MultipleFileClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#multipleFilePosition.
    def visitMultipleFilePosition(self, ctx: DNPParser.MultipleFilePositionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#commitmentControlClause.
    def visitCommitmentControlClause(
        self, ctx: DNPParser.CommitmentControlClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataDivision.
    def visitDataDivision(self, ctx: DNPParser.DataDivisionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataDivisionSection.
    def visitDataDivisionSection(self, ctx: DNPParser.DataDivisionSectionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#fileSection.
    def visitFileSection(self, ctx: DNPParser.FileSectionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#fileDescriptionEntry.
    def visitFileDescriptionEntry(self, ctx: DNPParser.FileDescriptionEntryContext):
        code_content = get_original_code_content(
            self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex
        )

        file_name = recursive_find_first_child_by_type(ctx, DNPParser.FileNameContext)

        if file_name is None:
            raise ValueError(
                f"File name is missing for FD statement {get_original_code_content(self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)}"
            )

        data_description_entries = find_all_children_by_type(
            ctx, DNPParser.DataDescriptionEntryContext
        )

        variables = []
        copybooks = []

        for entry in data_description_entries:
            entry = entry.getChild(0)

            # copy statement
            if isinstance(entry, DNPParser.CopyStatementContext):
                copy_source = recursive_find_first_child_by_type(
                    ctx, DNPParser.CopySourceContext
                )

                if copy_source is None:
                    raise ValueError(
                        f"File name of COPY statement {get_original_code_content(self.parser, entry.start.tokenIndex, entry.stop.tokenIndex)}"
                    )

                copy_name = copy_source.getChild(0)

                replace_clauses = find_all_children_by_type(
                    entry, DNPParser.ReplaceClauseContext
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

    # Visit a parse tree produced by DNPParser#fileDescriptionEntryClause.
    def visitFileDescriptionEntryClause(
        self, ctx: DNPParser.FileDescriptionEntryClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#externalClause.
    def visitExternalClause(self, ctx: DNPParser.ExternalClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#globalClause.
    def visitGlobalClause(self, ctx: DNPParser.GlobalClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#blockContainsClause.
    def visitBlockContainsClause(self, ctx: DNPParser.BlockContainsClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#blockContainsTo.
    def visitBlockContainsTo(self, ctx: DNPParser.BlockContainsToContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#recordContainsClause.
    def visitRecordContainsClause(self, ctx: DNPParser.RecordContainsClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#recordContainsClauseFormat1.
    def visitRecordContainsClauseFormat1(
        self, ctx: DNPParser.RecordContainsClauseFormat1Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#recordContainsClauseFormat2.
    def visitRecordContainsClauseFormat2(
        self, ctx: DNPParser.RecordContainsClauseFormat2Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#recordContainsClauseFormat3.
    def visitRecordContainsClauseFormat3(
        self, ctx: DNPParser.RecordContainsClauseFormat3Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#recordContainsTo.
    def visitRecordContainsTo(self, ctx: DNPParser.RecordContainsToContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#labelRecordsClause.
    def visitLabelRecordsClause(self, ctx: DNPParser.LabelRecordsClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#valueOfClause.
    def visitValueOfClause(self, ctx: DNPParser.ValueOfClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#valuePair.
    def visitValuePair(self, ctx: DNPParser.ValuePairContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataRecordsClause.
    def visitDataRecordsClause(self, ctx: DNPParser.DataRecordsClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#linageClause.
    def visitLinageClause(self, ctx: DNPParser.LinageClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#linageAt.
    def visitLinageAt(self, ctx: DNPParser.LinageAtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#linageFootingAt.
    def visitLinageFootingAt(self, ctx: DNPParser.LinageFootingAtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#linageLinesAtTop.
    def visitLinageLinesAtTop(self, ctx: DNPParser.LinageLinesAtTopContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#linageLinesAtBottom.
    def visitLinageLinesAtBottom(self, ctx: DNPParser.LinageLinesAtBottomContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#recordingModeClause.
    def visitRecordingModeClause(self, ctx: DNPParser.RecordingModeClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#modeStatement.
    def visitModeStatement(self, ctx: DNPParser.ModeStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#codeSetClause.
    def visitCodeSetClause(self, ctx: DNPParser.CodeSetClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportClause.
    def visitReportClause(self, ctx: DNPParser.ReportClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataBaseSection.
    def visitDataBaseSection(self, ctx: DNPParser.DataBaseSectionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataBaseSectionEntry.
    def visitDataBaseSectionEntry(self, ctx: DNPParser.DataBaseSectionEntryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataBaseDeclare.
    def visitDataBaseDeclare(self, ctx: DNPParser.DataBaseDeclareContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataBaseDatasetDeclare.
    def visitDataBaseDatasetDeclare(self, ctx: DNPParser.DataBaseDatasetDeclareContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#invokeClause.
    def visitInvokeClause(self, ctx: DNPParser.InvokeClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#usingClause.
    def visitUsingClause(self, ctx: DNPParser.UsingClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#workingStorageSection.
    def visitWorkingStorageSection(self, ctx: DNPParser.WorkingStorageSectionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#linkageSection.
    def visitLinkageSection(self, ctx: DNPParser.LinkageSectionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#communicationSection.
    def visitCommunicationSection(self, ctx: DNPParser.CommunicationSectionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#communicationDescriptionEntry.
    def visitCommunicationDescriptionEntry(
        self, ctx: DNPParser.CommunicationDescriptionEntryContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#communicationDescriptionEntryFormat1.
    def visitCommunicationDescriptionEntryFormat1(
        self, ctx: DNPParser.CommunicationDescriptionEntryFormat1Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#communicationDescriptionEntryFormat2.
    def visitCommunicationDescriptionEntryFormat2(
        self, ctx: DNPParser.CommunicationDescriptionEntryFormat2Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#communicationDescriptionEntryFormat3.
    def visitCommunicationDescriptionEntryFormat3(
        self, ctx: DNPParser.CommunicationDescriptionEntryFormat3Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#communicationDescriptionEntryFormat4.
    def visitCommunicationDescriptionEntryFormat4(
        self, ctx: DNPParser.CommunicationDescriptionEntryFormat4Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#communicationAttribute.
    def visitCommunicationAttribute(self, ctx: DNPParser.CommunicationAttributeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#communicationIoHeader.
    def visitCommunicationIoHeader(self, ctx: DNPParser.CommunicationIoHeaderContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#conversationClause.
    def visitConversationClause(self, ctx: DNPParser.ConversationClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#destinationCountClause.
    def visitDestinationCountClause(self, ctx: DNPParser.DestinationCountClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#destinationTableClause.
    def visitDestinationTableClause(self, ctx: DNPParser.DestinationTableClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#endKeyClause.
    def visitEndKeyClause(self, ctx: DNPParser.EndKeyClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#errorKeyClause.
    def visitErrorKeyClause(self, ctx: DNPParser.ErrorKeyClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#messageCountClause.
    def visitMessageCountClause(self, ctx: DNPParser.MessageCountClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#messageDateClause.
    def visitMessageDateClause(self, ctx: DNPParser.MessageDateClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#messageTimeClause.
    def visitMessageTimeClause(self, ctx: DNPParser.MessageTimeClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#statusKeyClause.
    def visitStatusKeyClause(self, ctx: DNPParser.StatusKeyClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#symbolicDestinationClause.
    def visitSymbolicDestinationClause(
        self, ctx: DNPParser.SymbolicDestinationClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#symbolicQueueClause.
    def visitSymbolicQueueClause(self, ctx: DNPParser.SymbolicQueueClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#symbolicSourceClause.
    def visitSymbolicSourceClause(self, ctx: DNPParser.SymbolicSourceClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#symbolicTerminalClause.
    def visitSymbolicTerminalClause(self, ctx: DNPParser.SymbolicTerminalClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#symbolicSubQueueClause.
    def visitSymbolicSubQueueClause(self, ctx: DNPParser.SymbolicSubQueueClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#textLengthClause.
    def visitTextLengthClause(self, ctx: DNPParser.TextLengthClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#localStorageSection.
    def visitLocalStorageSection(self, ctx: DNPParser.LocalStorageSectionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenSection.
    def visitScreenSection(self, ctx: DNPParser.ScreenSectionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenDescriptionEntry.
    def visitScreenDescriptionEntry(self, ctx: DNPParser.ScreenDescriptionEntryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenDescriptionBlankClause.
    def visitScreenDescriptionBlankClause(
        self, ctx: DNPParser.ScreenDescriptionBlankClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenDescriptionBellClause.
    def visitScreenDescriptionBellClause(
        self, ctx: DNPParser.ScreenDescriptionBellClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenDescriptionBlinkClause.
    def visitScreenDescriptionBlinkClause(
        self, ctx: DNPParser.ScreenDescriptionBlinkClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenDescriptionEraseClause.
    def visitScreenDescriptionEraseClause(
        self, ctx: DNPParser.ScreenDescriptionEraseClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenDescriptionLightClause.
    def visitScreenDescriptionLightClause(
        self, ctx: DNPParser.ScreenDescriptionLightClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenDescriptionGridClause.
    def visitScreenDescriptionGridClause(
        self, ctx: DNPParser.ScreenDescriptionGridClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenDescriptionReverseVideoClause.
    def visitScreenDescriptionReverseVideoClause(
        self, ctx: DNPParser.ScreenDescriptionReverseVideoClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenDescriptionUnderlineClause.
    def visitScreenDescriptionUnderlineClause(
        self, ctx: DNPParser.ScreenDescriptionUnderlineClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenDescriptionSizeClause.
    def visitScreenDescriptionSizeClause(
        self, ctx: DNPParser.ScreenDescriptionSizeClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenDescriptionLineClause.
    def visitScreenDescriptionLineClause(
        self, ctx: DNPParser.ScreenDescriptionLineClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenDescriptionColumnClause.
    def visitScreenDescriptionColumnClause(
        self, ctx: DNPParser.ScreenDescriptionColumnClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenDescriptionForegroundColorClause.
    def visitScreenDescriptionForegroundColorClause(
        self, ctx: DNPParser.ScreenDescriptionForegroundColorClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenDescriptionBackgroundColorClause.
    def visitScreenDescriptionBackgroundColorClause(
        self, ctx: DNPParser.ScreenDescriptionBackgroundColorClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenDescriptionControlClause.
    def visitScreenDescriptionControlClause(
        self, ctx: DNPParser.ScreenDescriptionControlClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenDescriptionValueClause.
    def visitScreenDescriptionValueClause(
        self, ctx: DNPParser.ScreenDescriptionValueClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenDescriptionPictureClause.
    def visitScreenDescriptionPictureClause(
        self, ctx: DNPParser.ScreenDescriptionPictureClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenDescriptionFromClause.
    def visitScreenDescriptionFromClause(
        self, ctx: DNPParser.ScreenDescriptionFromClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenDescriptionToClause.
    def visitScreenDescriptionToClause(
        self, ctx: DNPParser.ScreenDescriptionToClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenDescriptionUsingClause.
    def visitScreenDescriptionUsingClause(
        self, ctx: DNPParser.ScreenDescriptionUsingClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenDescriptionUsageClause.
    def visitScreenDescriptionUsageClause(
        self, ctx: DNPParser.ScreenDescriptionUsageClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenDescriptionBlankWhenZeroClause.
    def visitScreenDescriptionBlankWhenZeroClause(
        self, ctx: DNPParser.ScreenDescriptionBlankWhenZeroClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenDescriptionJustifiedClause.
    def visitScreenDescriptionJustifiedClause(
        self, ctx: DNPParser.ScreenDescriptionJustifiedClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenDescriptionSignClause.
    def visitScreenDescriptionSignClause(
        self, ctx: DNPParser.ScreenDescriptionSignClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenDescriptionAutoClause.
    def visitScreenDescriptionAutoClause(
        self, ctx: DNPParser.ScreenDescriptionAutoClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenDescriptionSecureClause.
    def visitScreenDescriptionSecureClause(
        self, ctx: DNPParser.ScreenDescriptionSecureClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenDescriptionRequiredClause.
    def visitScreenDescriptionRequiredClause(
        self, ctx: DNPParser.ScreenDescriptionRequiredClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenDescriptionPromptClause.
    def visitScreenDescriptionPromptClause(
        self, ctx: DNPParser.ScreenDescriptionPromptClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenDescriptionPromptOccursClause.
    def visitScreenDescriptionPromptOccursClause(
        self, ctx: DNPParser.ScreenDescriptionPromptOccursClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenDescriptionFullClause.
    def visitScreenDescriptionFullClause(
        self, ctx: DNPParser.ScreenDescriptionFullClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenDescriptionZeroFillClause.
    def visitScreenDescriptionZeroFillClause(
        self, ctx: DNPParser.ScreenDescriptionZeroFillClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportSection.
    def visitReportSection(self, ctx: DNPParser.ReportSectionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportDescription.
    def visitReportDescription(self, ctx: DNPParser.ReportDescriptionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportDescriptionEntry.
    def visitReportDescriptionEntry(self, ctx: DNPParser.ReportDescriptionEntryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportDescriptionGlobalClause.
    def visitReportDescriptionGlobalClause(
        self, ctx: DNPParser.ReportDescriptionGlobalClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportDescriptionPageLimitClause.
    def visitReportDescriptionPageLimitClause(
        self, ctx: DNPParser.ReportDescriptionPageLimitClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportDescriptionHeadingClause.
    def visitReportDescriptionHeadingClause(
        self, ctx: DNPParser.ReportDescriptionHeadingClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportDescriptionFirstDetailClause.
    def visitReportDescriptionFirstDetailClause(
        self, ctx: DNPParser.ReportDescriptionFirstDetailClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportDescriptionLastDetailClause.
    def visitReportDescriptionLastDetailClause(
        self, ctx: DNPParser.ReportDescriptionLastDetailClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportDescriptionFootingClause.
    def visitReportDescriptionFootingClause(
        self, ctx: DNPParser.ReportDescriptionFootingClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportGroupDescriptionEntry.
    def visitReportGroupDescriptionEntry(
        self, ctx: DNPParser.ReportGroupDescriptionEntryContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportGroupDescriptionEntryFormat1.
    def visitReportGroupDescriptionEntryFormat1(
        self, ctx: DNPParser.ReportGroupDescriptionEntryFormat1Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportGroupDescriptionEntryFormat2.
    def visitReportGroupDescriptionEntryFormat2(
        self, ctx: DNPParser.ReportGroupDescriptionEntryFormat2Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportGroupDescriptionEntryFormat3.
    def visitReportGroupDescriptionEntryFormat3(
        self, ctx: DNPParser.ReportGroupDescriptionEntryFormat3Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportGroupBlankWhenZeroClause.
    def visitReportGroupBlankWhenZeroClause(
        self, ctx: DNPParser.ReportGroupBlankWhenZeroClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportGroupColumnNumberClause.
    def visitReportGroupColumnNumberClause(
        self, ctx: DNPParser.ReportGroupColumnNumberClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportGroupIndicateClause.
    def visitReportGroupIndicateClause(
        self, ctx: DNPParser.ReportGroupIndicateClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportGroupJustifiedClause.
    def visitReportGroupJustifiedClause(
        self, ctx: DNPParser.ReportGroupJustifiedClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportGroupLineNumberClause.
    def visitReportGroupLineNumberClause(
        self, ctx: DNPParser.ReportGroupLineNumberClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportGroupLineNumberNextPage.
    def visitReportGroupLineNumberNextPage(
        self, ctx: DNPParser.ReportGroupLineNumberNextPageContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportGroupLineNumberPlus.
    def visitReportGroupLineNumberPlus(
        self, ctx: DNPParser.ReportGroupLineNumberPlusContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportGroupNextGroupClause.
    def visitReportGroupNextGroupClause(
        self, ctx: DNPParser.ReportGroupNextGroupClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportGroupNextGroupPlus.
    def visitReportGroupNextGroupPlus(
        self, ctx: DNPParser.ReportGroupNextGroupPlusContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportGroupNextGroupNextPage.
    def visitReportGroupNextGroupNextPage(
        self, ctx: DNPParser.ReportGroupNextGroupNextPageContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportGroupPictureClause.
    def visitReportGroupPictureClause(
        self, ctx: DNPParser.ReportGroupPictureClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportGroupResetClause.
    def visitReportGroupResetClause(self, ctx: DNPParser.ReportGroupResetClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportGroupSignClause.
    def visitReportGroupSignClause(self, ctx: DNPParser.ReportGroupSignClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportGroupSourceClause.
    def visitReportGroupSourceClause(
        self, ctx: DNPParser.ReportGroupSourceClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportGroupSumClause.
    def visitReportGroupSumClause(self, ctx: DNPParser.ReportGroupSumClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportGroupTypeClause.
    def visitReportGroupTypeClause(self, ctx: DNPParser.ReportGroupTypeClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportGroupTypeReportHeading.
    def visitReportGroupTypeReportHeading(
        self, ctx: DNPParser.ReportGroupTypeReportHeadingContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportGroupTypePageHeading.
    def visitReportGroupTypePageHeading(
        self, ctx: DNPParser.ReportGroupTypePageHeadingContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportGroupTypeControlHeading.
    def visitReportGroupTypeControlHeading(
        self, ctx: DNPParser.ReportGroupTypeControlHeadingContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportGroupTypeDetail.
    def visitReportGroupTypeDetail(self, ctx: DNPParser.ReportGroupTypeDetailContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportGroupTypeControlFooting.
    def visitReportGroupTypeControlFooting(
        self, ctx: DNPParser.ReportGroupTypeControlFootingContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportGroupUsageClause.
    def visitReportGroupUsageClause(self, ctx: DNPParser.ReportGroupUsageClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportGroupTypePageFooting.
    def visitReportGroupTypePageFooting(
        self, ctx: DNPParser.ReportGroupTypePageFootingContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportGroupTypeReportFooting.
    def visitReportGroupTypeReportFooting(
        self, ctx: DNPParser.ReportGroupTypeReportFootingContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportGroupValueClause.
    def visitReportGroupValueClause(self, ctx: DNPParser.ReportGroupValueClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#programLibrarySection.
    def visitProgramLibrarySection(self, ctx: DNPParser.ProgramLibrarySectionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#libraryDescriptionEntry.
    def visitLibraryDescriptionEntry(
        self, ctx: DNPParser.LibraryDescriptionEntryContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#libraryDescriptionEntryFormat1.
    def visitLibraryDescriptionEntryFormat1(
        self, ctx: DNPParser.LibraryDescriptionEntryFormat1Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#libraryDescriptionEntryFormat2.
    def visitLibraryDescriptionEntryFormat2(
        self, ctx: DNPParser.LibraryDescriptionEntryFormat2Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#libraryAttributeClauseFormat1.
    def visitLibraryAttributeClauseFormat1(
        self, ctx: DNPParser.LibraryAttributeClauseFormat1Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#libraryAttributeClauseFormat2.
    def visitLibraryAttributeClauseFormat2(
        self, ctx: DNPParser.LibraryAttributeClauseFormat2Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#libraryAttributeFunction.
    def visitLibraryAttributeFunction(
        self, ctx: DNPParser.LibraryAttributeFunctionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#libraryAttributeParameter.
    def visitLibraryAttributeParameter(
        self, ctx: DNPParser.LibraryAttributeParameterContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#libraryAttributeTitle.
    def visitLibraryAttributeTitle(self, ctx: DNPParser.LibraryAttributeTitleContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#libraryEntryProcedureClauseFormat1.
    def visitLibraryEntryProcedureClauseFormat1(
        self, ctx: DNPParser.LibraryEntryProcedureClauseFormat1Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#libraryEntryProcedureClauseFormat2.
    def visitLibraryEntryProcedureClauseFormat2(
        self, ctx: DNPParser.LibraryEntryProcedureClauseFormat2Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#libraryEntryProcedureForClause.
    def visitLibraryEntryProcedureForClause(
        self, ctx: DNPParser.LibraryEntryProcedureForClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#libraryEntryProcedureGivingClause.
    def visitLibraryEntryProcedureGivingClause(
        self, ctx: DNPParser.LibraryEntryProcedureGivingClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#libraryEntryProcedureUsingClause.
    def visitLibraryEntryProcedureUsingClause(
        self, ctx: DNPParser.LibraryEntryProcedureUsingClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#libraryEntryProcedureUsingName.
    def visitLibraryEntryProcedureUsingName(
        self, ctx: DNPParser.LibraryEntryProcedureUsingNameContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#libraryEntryProcedureWithClause.
    def visitLibraryEntryProcedureWithClause(
        self, ctx: DNPParser.LibraryEntryProcedureWithClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#libraryEntryProcedureWithName.
    def visitLibraryEntryProcedureWithName(
        self, ctx: DNPParser.LibraryEntryProcedureWithNameContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#libraryIsCommonClause.
    def visitLibraryIsCommonClause(self, ctx: DNPParser.LibraryIsCommonClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#libraryIsGlobalClause.
    def visitLibraryIsGlobalClause(self, ctx: DNPParser.LibraryIsGlobalClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataDescriptionEntry.
    def visitDataDescriptionEntry(self, ctx: DNPParser.DataDescriptionEntryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#copyStatement.
    def visitCopyStatement(self, ctx: DNPParser.CopyStatementContext):
        # extract statements
        res = self.assessCopyStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)

        # extract dependency
        copy_source = recursive_find_first_child_by_type(
            ctx, DNPParser.CopySourceContext
        )

        if copy_source is None:
            raise ValueError(
                f"File name of COPY statement {get_original_code_content(self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)}"
            )

        copy_name = copy_source.getChild(0)

        replace_clauses = find_all_children_by_type(ctx, DNPParser.ReplaceClauseContext)

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

    # Visit a parse tree produced by DNPParser#copySource.
    def visitCopySource(self, ctx: DNPParser.CopySourceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#copyLibrary.
    def visitCopyLibrary(self, ctx: DNPParser.CopyLibraryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#replacingPhrase.
    def visitReplacingPhrase(self, ctx: DNPParser.ReplacingPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#changeFileAttribute.
    def visitChangeFileAttribute(self, ctx: DNPParser.ChangeFileAttributeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#changeLibraryAttribute.
    def visitChangeLibraryAttribute(self, ctx: DNPParser.ChangeLibraryAttributeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#libraryAttributeName.
    def visitLibraryAttributeName(self, ctx: DNPParser.LibraryAttributeNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#libraryValueOption.
    def visitLibraryValueOption(self, ctx: DNPParser.LibraryValueOptionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#toValueOption.
    def visitToValueOption(self, ctx: DNPParser.ToValueOptionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#replaceOffStatement.
    def visitReplaceOffStatement(self, ctx: DNPParser.ReplaceOffStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#replaceClause.
    def visitReplaceClause(self, ctx: DNPParser.ReplaceClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#directoryPhrase.
    def visitDirectoryPhrase(self, ctx: DNPParser.DirectoryPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#familyPhrase.
    def visitFamilyPhrase(self, ctx: DNPParser.FamilyPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#replaceable.
    def visitReplaceable(self, ctx: DNPParser.ReplaceableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#replacement.
    def visitReplacement(self, ctx: DNPParser.ReplacementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#ejectStatement.
    def visitEjectStatement(self, ctx: DNPParser.EjectStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#skipStatement.
    def visitSkipStatement(self, ctx: DNPParser.SkipStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#titleStatement.
    def visitTitleStatement(self, ctx: DNPParser.TitleStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#pseudoText.
    def visitPseudoText(self, ctx: DNPParser.PseudoTextContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#charData.
    def visitCharData(self, ctx: DNPParser.CharDataContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#charDataSql.
    def visitCharDataSql(self, ctx: DNPParser.CharDataSqlContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#charDataLine.
    def visitCharDataLine(self, ctx: DNPParser.CharDataLineContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#cobolWord.
    def visitCobolWord(self, ctx: DNPParser.CobolWordContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#literal.
    def visitLiteral(self, ctx: DNPParser.LiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#jpEncodingText.
    def visitJpEncodingText(self, ctx: DNPParser.JpEncodingTextContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#filename.
    def visitFilename(self, ctx: DNPParser.FilenameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataDescriptionEntryFormat1.
    def visitDataDescriptionEntryFormat1(
        self, ctx: DNPParser.DataDescriptionEntryFormat1Context
    ):
        variable = extract_cobol_variable(ctx)
        self.variable_list.append(variable)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataDescriptionEntryFormat2.
    def visitDataDescriptionEntryFormat2(
        self, ctx: DNPParser.DataDescriptionEntryFormat2Context
    ):
        variable = extract_cobol_variable(ctx)
        self.variable_list.append(variable)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataDescriptionEntryFormat3.
    def visitDataDescriptionEntryFormat3(
        self, ctx: DNPParser.DataDescriptionEntryFormat3Context
    ):
        variable = extract_cobol_variable(ctx)
        self.variable_list.append(variable)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataDescriptionEntryExecSql.
    def visitDataDescriptionEntryExecSql(
        self, ctx: DNPParser.DataDescriptionEntryExecSqlContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataAlignedClause.
    def visitDataAlignedClause(self, ctx: DNPParser.DataAlignedClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataBlankWhenZeroClause.
    def visitDataBlankWhenZeroClause(
        self, ctx: DNPParser.DataBlankWhenZeroClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataCommonOwnLocalClause.
    def visitDataCommonOwnLocalClause(
        self, ctx: DNPParser.DataCommonOwnLocalClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataExternalClause.
    def visitDataExternalClause(self, ctx: DNPParser.DataExternalClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataGlobalClause.
    def visitDataGlobalClause(self, ctx: DNPParser.DataGlobalClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataIntegerStringClause.
    def visitDataIntegerStringClause(
        self, ctx: DNPParser.DataIntegerStringClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataJustifiedClause.
    def visitDataJustifiedClause(self, ctx: DNPParser.DataJustifiedClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataOccursClause.
    def visitDataOccursClause(self, ctx: DNPParser.DataOccursClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataOccursTo.
    def visitDataOccursTo(self, ctx: DNPParser.DataOccursToContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataOccursSort.
    def visitDataOccursSort(self, ctx: DNPParser.DataOccursSortContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataPictureClause.
    def visitDataPictureClause(self, ctx: DNPParser.DataPictureClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#pictureString.
    def visitPictureString(self, ctx: DNPParser.PictureStringContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#pictureChars.
    def visitPictureChars(self, ctx: DNPParser.PictureCharsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#pictureCardinality.
    def visitPictureCardinality(self, ctx: DNPParser.PictureCardinalityContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataReceivedByClause.
    def visitDataReceivedByClause(self, ctx: DNPParser.DataReceivedByClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataRecordAreaClause.
    def visitDataRecordAreaClause(self, ctx: DNPParser.DataRecordAreaClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataRedefinesClause.
    def visitDataRedefinesClause(self, ctx: DNPParser.DataRedefinesClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataRenamesClause.
    def visitDataRenamesClause(self, ctx: DNPParser.DataRenamesClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataSignClause.
    def visitDataSignClause(self, ctx: DNPParser.DataSignClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataSynchronizedClause.
    def visitDataSynchronizedClause(self, ctx: DNPParser.DataSynchronizedClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataThreadLocalClause.
    def visitDataThreadLocalClause(self, ctx: DNPParser.DataThreadLocalClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataTypeClause.
    def visitDataTypeClause(self, ctx: DNPParser.DataTypeClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataTypeDefClause.
    def visitDataTypeDefClause(self, ctx: DNPParser.DataTypeDefClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataUsageClause.
    def visitDataUsageClause(self, ctx: DNPParser.DataUsageClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataUsingClause.
    def visitDataUsingClause(self, ctx: DNPParser.DataUsingClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataValueClause.
    def visitDataValueClause(self, ctx: DNPParser.DataValueClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataValueInterval.
    def visitDataValueInterval(self, ctx: DNPParser.DataValueIntervalContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataValueIntervalFrom.
    def visitDataValueIntervalFrom(self, ctx: DNPParser.DataValueIntervalFromContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataValueIntervalTo.
    def visitDataValueIntervalTo(self, ctx: DNPParser.DataValueIntervalToContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataWithLowerBoundsClause.
    def visitDataWithLowerBoundsClause(
        self, ctx: DNPParser.DataWithLowerBoundsClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#procedureDivision.
    def visitProcedureDivision(self, ctx: DNPParser.ProcedureDivisionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#procedureDivisionUsingClause.
    def visitProcedureDivisionUsingClause(
        self, ctx: DNPParser.ProcedureDivisionUsingClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#procedureDivisionGivingClause.
    def visitProcedureDivisionGivingClause(
        self, ctx: DNPParser.ProcedureDivisionGivingClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#procedureDivisionUsingParameter.
    def visitProcedureDivisionUsingParameter(
        self, ctx: DNPParser.ProcedureDivisionUsingParameterContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#procedureDivisionByReferencePhrase.
    def visitProcedureDivisionByReferencePhrase(
        self, ctx: DNPParser.ProcedureDivisionByReferencePhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#procedureDivisionByReference.
    def visitProcedureDivisionByReference(
        self, ctx: DNPParser.ProcedureDivisionByReferenceContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#procedureDivisionByValuePhrase.
    def visitProcedureDivisionByValuePhrase(
        self, ctx: DNPParser.ProcedureDivisionByValuePhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#procedureDivisionByValue.
    def visitProcedureDivisionByValue(
        self, ctx: DNPParser.ProcedureDivisionByValueContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#procedureDeclaratives.
    def visitProcedureDeclaratives(self, ctx: DNPParser.ProcedureDeclarativesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#procedureDeclarative.
    def visitProcedureDeclarative(self, ctx: DNPParser.ProcedureDeclarativeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#procedureSectionHeader.
    def visitProcedureSectionHeader(self, ctx: DNPParser.ProcedureSectionHeaderContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#procedureDivisionBody.
    def visitProcedureDivisionBody(self, ctx: DNPParser.ProcedureDivisionBodyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#procedureSection.
    def visitProcedureSection(self, ctx: DNPParser.ProcedureSectionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#paragraphs.
    def visitParagraphs(self, ctx: DNPParser.ParagraphsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#paragraph.
    def visitParagraph(self, ctx: DNPParser.ParagraphContext):
        paragraph_name = ctx.getChild(0)
        start_line = ctx.start.line
        end_line = ctx.stop.line

        perform_procedure_statements = find_all_children_by_type(
            ctx, DNPParser.PerformProcedureStatementContext
        )

        procedure_name_list = []

        for perform_statement in perform_procedure_statements:
            # perform statement can have multiple paragraph names
            procedure_names = find_all_children_by_type(
                perform_statement, DNPParser.ProcedureNameContext
            )

            procedure_names = list(
                map(lambda element: element.getText(), procedure_names)
            )

            procedure_name_list.extend(procedure_names)

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
            ref_paragraphs=procedure_name_list,
        )

        self.paragraph_list.append(paragraph)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#sentence.
    def visitSentence(self, ctx: DNPParser.SentenceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#statement.
    def visitStatement(self, ctx: DNPParser.StatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#addToStatement.
    def visitAddToStatement(self, ctx: DNPParser.AddToStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#addToGivingStatement.
    def visitAddToGivingStatement(self, ctx: DNPParser.AddToGivingStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#addCorrespondingStatement.
    def visitAddCorrespondingStatement(
        self, ctx: DNPParser.AddCorrespondingStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#addFrom.
    def visitAddFrom(self, ctx: DNPParser.AddFromContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#addTo.
    def visitAddTo(self, ctx: DNPParser.AddToContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#addToGiving.
    def visitAddToGiving(self, ctx: DNPParser.AddToGivingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#addGiving.
    def visitAddGiving(self, ctx: DNPParser.AddGivingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#alteredGoTo.
    def visitAlteredGoTo(self, ctx: DNPParser.AlteredGoToContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#alterStatement.
    def visitAlterStatement(self, ctx: DNPParser.AlterStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#alterProceedTo.
    def visitAlterProceedTo(self, ctx: DNPParser.AlterProceedToContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#callUsingPhrase.
    def visitCallUsingPhrase(self, ctx: DNPParser.CallUsingPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#callUsingParameter.
    def visitCallUsingParameter(self, ctx: DNPParser.CallUsingParameterContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#callByReferencePhrase.
    def visitCallByReferencePhrase(self, ctx: DNPParser.CallByReferencePhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#callByReference.
    def visitCallByReference(self, ctx: DNPParser.CallByReferenceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#callByValuePhrase.
    def visitCallByValuePhrase(self, ctx: DNPParser.CallByValuePhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#callByValue.
    def visitCallByValue(self, ctx: DNPParser.CallByValueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#callByContentPhrase.
    def visitCallByContentPhrase(self, ctx: DNPParser.CallByContentPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#callByContent.
    def visitCallByContent(self, ctx: DNPParser.CallByContentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#callGivingPhrase.
    def visitCallGivingPhrase(self, ctx: DNPParser.CallGivingPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#callSystem.
    def visitCallSystem(self, ctx: DNPParser.CallSystemContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#cancelStatement.
    def visitCancelStatement(self, ctx: DNPParser.CancelStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#cancelCall.
    def visitCancelCall(self, ctx: DNPParser.CancelCallContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#closeFile.
    def visitCloseFile(self, ctx: DNPParser.CloseFileContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#closeReelUnitStatement.
    def visitCloseReelUnitStatement(self, ctx: DNPParser.CloseReelUnitStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#closeRelativeStatement.
    def visitCloseRelativeStatement(self, ctx: DNPParser.CloseRelativeStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#closePortFileIOStatement.
    def visitClosePortFileIOStatement(
        self, ctx: DNPParser.ClosePortFileIOStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#closePortFileIOUsing.
    def visitClosePortFileIOUsing(self, ctx: DNPParser.ClosePortFileIOUsingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#closePortFileIOUsingCloseDisposition.
    def visitClosePortFileIOUsingCloseDisposition(
        self, ctx: DNPParser.ClosePortFileIOUsingCloseDispositionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#closePortFileIOUsingAssociatedData.
    def visitClosePortFileIOUsingAssociatedData(
        self, ctx: DNPParser.ClosePortFileIOUsingAssociatedDataContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#closePortFileIOUsingAssociatedDataLength.
    def visitClosePortFileIOUsingAssociatedDataLength(
        self, ctx: DNPParser.ClosePortFileIOUsingAssociatedDataLengthContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#computeStore.
    def visitComputeStore(self, ctx: DNPParser.ComputeStoreContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#continueIndicator.
    def visitContinueIndicator(self, ctx: DNPParser.ContinueIndicatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#deleteStatement.
    def visitDeleteStatement(self, ctx: DNPParser.DeleteStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#disableStatement.
    def visitDisableStatement(self, ctx: DNPParser.DisableStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#displayOperand.
    def visitDisplayOperand(self, ctx: DNPParser.DisplayOperandContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#displayAt.
    def visitDisplayAt(self, ctx: DNPParser.DisplayAtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#displayUpon.
    def visitDisplayUpon(self, ctx: DNPParser.DisplayUponContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#displayWith.
    def visitDisplayWith(self, ctx: DNPParser.DisplayWithContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#divideStatement.
    def visitDivideStatement(self, ctx: DNPParser.DivideStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#divideIntoStatement.
    def visitDivideIntoStatement(self, ctx: DNPParser.DivideIntoStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#divideIntoGivingStatement.
    def visitDivideIntoGivingStatement(
        self, ctx: DNPParser.DivideIntoGivingStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#divideByGivingStatement.
    def visitDivideByGivingStatement(
        self, ctx: DNPParser.DivideByGivingStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#divideGivingPhrase.
    def visitDivideGivingPhrase(self, ctx: DNPParser.DivideGivingPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#divideInto.
    def visitDivideInto(self, ctx: DNPParser.DivideIntoContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#divideGiving.
    def visitDivideGiving(self, ctx: DNPParser.DivideGivingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#divideRemainder.
    def visitDivideRemainder(self, ctx: DNPParser.DivideRemainderContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#enableStatement.
    def visitEnableStatement(self, ctx: DNPParser.EnableStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#entryStatement.
    def visitEntryStatement(self, ctx: DNPParser.EntryStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#evaluateSelect.
    def visitEvaluateSelect(self, ctx: DNPParser.EvaluateSelectContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#evaluateAlsoSelect.
    def visitEvaluateAlsoSelect(self, ctx: DNPParser.EvaluateAlsoSelectContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#evaluateWhenPhrase.
    def visitEvaluateWhenPhrase(self, ctx: DNPParser.EvaluateWhenPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#evaluateWhen.
    def visitEvaluateWhen(self, ctx: DNPParser.EvaluateWhenContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#evaluateCondition.
    def visitEvaluateCondition(self, ctx: DNPParser.EvaluateConditionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#evaluateThrough.
    def visitEvaluateThrough(self, ctx: DNPParser.EvaluateThroughContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#evaluateAlsoCondition.
    def visitEvaluateAlsoCondition(self, ctx: DNPParser.EvaluateAlsoConditionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#evaluateWhenOther.
    def visitEvaluateWhenOther(self, ctx: DNPParser.EvaluateWhenOtherContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#evaluateValue.
    def visitEvaluateValue(self, ctx: DNPParser.EvaluateValueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#execCicsStatement.
    def visitExecCicsStatement(self, ctx: DNPParser.ExecCicsStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#execSqlStatement.
    def visitExecSqlStatement(self, ctx: DNPParser.ExecSqlStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#execSqlImsStatement.
    def visitExecSqlImsStatement(self, ctx: DNPParser.ExecSqlImsStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#exhibitStatement.
    def visitExhibitStatement(self, ctx: DNPParser.ExhibitStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#exhibitOperand.
    def visitExhibitOperand(self, ctx: DNPParser.ExhibitOperandContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#findOption.
    def visitFindOption(self, ctx: DNPParser.FindOptionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#generateStatement.
    def visitGenerateStatement(self, ctx: DNPParser.GenerateStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#goToStatementSimple.
    def visitGoToStatementSimple(self, ctx: DNPParser.GoToStatementSimpleContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#goToDependingOnStatement.
    def visitGoToDependingOnStatement(
        self, ctx: DNPParser.GoToDependingOnStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#ifThen.
    def visitIfThen(self, ctx: DNPParser.IfThenContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#ifElse.
    def visitIfElse(self, ctx: DNPParser.IfElseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#initializeReplacingPhrase.
    def visitInitializeReplacingPhrase(
        self, ctx: DNPParser.InitializeReplacingPhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#initializeReplacingBy.
    def visitInitializeReplacingBy(self, ctx: DNPParser.InitializeReplacingByContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#initiateStatement.
    def visitInitiateStatement(self, ctx: DNPParser.InitiateStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#inspectTallyingPhrase.
    def visitInspectTallyingPhrase(self, ctx: DNPParser.InspectTallyingPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#inspectReplacingPhrase.
    def visitInspectReplacingPhrase(self, ctx: DNPParser.InspectReplacingPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#inspectTallyingReplacingPhrase.
    def visitInspectTallyingReplacingPhrase(
        self, ctx: DNPParser.InspectTallyingReplacingPhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#inspectConvertingPhrase.
    def visitInspectConvertingPhrase(
        self, ctx: DNPParser.InspectConvertingPhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#inspectFor.
    def visitInspectFor(self, ctx: DNPParser.InspectForContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#inspectCharacters.
    def visitInspectCharacters(self, ctx: DNPParser.InspectCharactersContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#inspectReplacingCharacters.
    def visitInspectReplacingCharacters(
        self, ctx: DNPParser.InspectReplacingCharactersContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#inspectAllLeadings.
    def visitInspectAllLeadings(self, ctx: DNPParser.InspectAllLeadingsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#inspectReplacingAllLeadings.
    def visitInspectReplacingAllLeadings(
        self, ctx: DNPParser.InspectReplacingAllLeadingsContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#inspectAllLeading.
    def visitInspectAllLeading(self, ctx: DNPParser.InspectAllLeadingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#inspectReplacingAllLeading.
    def visitInspectReplacingAllLeading(
        self, ctx: DNPParser.InspectReplacingAllLeadingContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#inspectBy.
    def visitInspectBy(self, ctx: DNPParser.InspectByContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#inspectTo.
    def visitInspectTo(self, ctx: DNPParser.InspectToContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#inspectBeforeAfter.
    def visitInspectBeforeAfter(self, ctx: DNPParser.InspectBeforeAfterContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#mergeStatement.
    def visitMergeStatement(self, ctx: DNPParser.MergeStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#mergeOnKeyClause.
    def visitMergeOnKeyClause(self, ctx: DNPParser.MergeOnKeyClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#mergeCollatingSequencePhrase.
    def visitMergeCollatingSequencePhrase(
        self, ctx: DNPParser.MergeCollatingSequencePhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#mergeCollatingAlphanumeric.
    def visitMergeCollatingAlphanumeric(
        self, ctx: DNPParser.MergeCollatingAlphanumericContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#mergeCollatingNational.
    def visitMergeCollatingNational(self, ctx: DNPParser.MergeCollatingNationalContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#mergeUsing.
    def visitMergeUsing(self, ctx: DNPParser.MergeUsingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#mergeOutputProcedurePhrase.
    def visitMergeOutputProcedurePhrase(
        self, ctx: DNPParser.MergeOutputProcedurePhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#mergeOutputThrough.
    def visitMergeOutputThrough(self, ctx: DNPParser.MergeOutputThroughContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#mergeGivingPhrase.
    def visitMergeGivingPhrase(self, ctx: DNPParser.MergeGivingPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#mergeGiving.
    def visitMergeGiving(self, ctx: DNPParser.MergeGivingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#moveToStatement.
    def visitMoveToStatement(self, ctx: DNPParser.MoveToStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#moveToSendingArea.
    def visitMoveToSendingArea(self, ctx: DNPParser.MoveToSendingAreaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#moveCorrespondingToStatement.
    def visitMoveCorrespondingToStatement(
        self, ctx: DNPParser.MoveCorrespondingToStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#moveCorrespondingToSendingArea.
    def visitMoveCorrespondingToSendingArea(
        self, ctx: DNPParser.MoveCorrespondingToSendingAreaContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#moveAttributeClause.
    def visitMoveAttributeClause(self, ctx: DNPParser.MoveAttributeClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#modifyOption.
    def visitModifyOption(self, ctx: DNPParser.ModifyOptionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#multiplyStatement.
    def visitMultiplyStatement(self, ctx: DNPParser.MultiplyStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#multiplyRegular.
    def visitMultiplyRegular(self, ctx: DNPParser.MultiplyRegularContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#multiplyRegularOperand.
    def visitMultiplyRegularOperand(self, ctx: DNPParser.MultiplyRegularOperandContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#multiplyGiving.
    def visitMultiplyGiving(self, ctx: DNPParser.MultiplyGivingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#multiplyGivingOperand.
    def visitMultiplyGivingOperand(self, ctx: DNPParser.MultiplyGivingOperandContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#multiplyGivingResult.
    def visitMultiplyGivingResult(self, ctx: DNPParser.MultiplyGivingResultContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#openInputStatement.
    def visitOpenInputStatement(self, ctx: DNPParser.OpenInputStatementContext):
        file_control_name = recursive_find_first_child_by_type(
            ctx, DNPParser.FileNameContext
        )

        if file_control_name is None:
            raise ValueError(
                f"Missing file name in OPEN statement {get_original_code_content(self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)}"
            )

        for file_control in self.file_control_list:
            if file_control.file_name == file_control_name.getText():
                file_control.access_mode = "INPUT"
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#openInput.
    def visitOpenInput(self, ctx: DNPParser.OpenInputContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#openUpdateStatement.
    def visitOpenUpdateStatement(self, ctx: DNPParser.OpenUpdateStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#openOutputStatement.
    def visitOpenOutputStatement(self, ctx: DNPParser.OpenOutputStatementContext):
        file_control_name = recursive_find_first_child_by_type(
            ctx, DNPParser.FileNameContext
        )

        if file_control_name is None:
            raise ValueError(
                f"Missing file name in OPEN statement {get_original_code_content(self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)}"
            )

        for file_control in self.file_control_list:
            if file_control.file_name == file_control_name.getText():
                file_control.access_mode = "OUTPUT"
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#openOutput.
    def visitOpenOutput(self, ctx: DNPParser.OpenOutputContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#openIOStatement.
    def visitOpenIOStatement(self, ctx: DNPParser.OpenIOStatementContext):
        file_control_name = recursive_find_first_child_by_type(
            ctx, DNPParser.FileNameContext
        )

        if file_control_name is None:
            raise ValueError(
                f"Missing file name in OPEN statement {get_original_code_content(self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)}"
            )

        for file_control in self.file_control_list:
            if file_control.file_name == file_control_name.getText():
                file_control.access_mode = "I-O"
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#openInquiry.
    def visitOpenInquiry(self, ctx: DNPParser.OpenInquiryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#openExtendStatement.
    def visitOpenExtendStatement(self, ctx: DNPParser.OpenExtendStatementContext):
        file_control_name = recursive_find_first_child_by_type(
            ctx, DNPParser.FileNameContext
        )

        if file_control_name is None:
            raise ValueError(
                f"Missing file name in OPEN statement {get_original_code_content(self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)}"
            )

        for file_control in self.file_control_list:
            if file_control.file_name == file_control_name.getText():
                file_control.access_mode = "EXTEND"
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#performInlineStatement.
    def visitPerformInlineStatement(self, ctx: DNPParser.PerformInlineStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#performProcedureStatement.
    def visitPerformProcedureStatement(
        self, ctx: DNPParser.PerformProcedureStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#performType.
    def visitPerformType(self, ctx: DNPParser.PerformTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#performTimes.
    def visitPerformTimes(self, ctx: DNPParser.PerformTimesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#performUntil.
    def visitPerformUntil(self, ctx: DNPParser.PerformUntilContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#performVarying.
    def visitPerformVarying(self, ctx: DNPParser.PerformVaryingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#performVaryingClause.
    def visitPerformVaryingClause(self, ctx: DNPParser.PerformVaryingClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#performVaryingPhrase.
    def visitPerformVaryingPhrase(self, ctx: DNPParser.PerformVaryingPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#performAfter.
    def visitPerformAfter(self, ctx: DNPParser.PerformAfterContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#performFrom.
    def visitPerformFrom(self, ctx: DNPParser.PerformFromContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#performBy.
    def visitPerformBy(self, ctx: DNPParser.PerformByContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#performTestClause.
    def visitPerformTestClause(self, ctx: DNPParser.PerformTestClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#purgeStatement.
    def visitPurgeStatement(self, ctx: DNPParser.PurgeStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#readInto.
    def visitReadInto(self, ctx: DNPParser.ReadIntoContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#readWith.
    def visitReadWith(self, ctx: DNPParser.ReadWithContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#readKey.
    def visitReadKey(self, ctx: DNPParser.ReadKeyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#receiveStatement.
    def visitReceiveStatement(self, ctx: DNPParser.ReceiveStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#receiveFromStatement.
    def visitReceiveFromStatement(self, ctx: DNPParser.ReceiveFromStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#receiveFrom.
    def visitReceiveFrom(self, ctx: DNPParser.ReceiveFromContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#receiveIntoStatement.
    def visitReceiveIntoStatement(self, ctx: DNPParser.ReceiveIntoStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#receiveNoData.
    def visitReceiveNoData(self, ctx: DNPParser.ReceiveNoDataContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#receiveWithData.
    def visitReceiveWithData(self, ctx: DNPParser.ReceiveWithDataContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#receiveBefore.
    def visitReceiveBefore(self, ctx: DNPParser.ReceiveBeforeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#receiveWith.
    def visitReceiveWith(self, ctx: DNPParser.ReceiveWithContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#receiveThread.
    def visitReceiveThread(self, ctx: DNPParser.ReceiveThreadContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#receiveSize.
    def visitReceiveSize(self, ctx: DNPParser.ReceiveSizeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#receiveStatus.
    def visitReceiveStatus(self, ctx: DNPParser.ReceiveStatusContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#releaseStatement.
    def visitReleaseStatement(self, ctx: DNPParser.ReleaseStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#returnStatement.
    def visitReturnStatement(self, ctx: DNPParser.ReturnStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#returnInto.
    def visitReturnInto(self, ctx: DNPParser.ReturnIntoContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#rewriteFrom.
    def visitRewriteFrom(self, ctx: DNPParser.RewriteFromContext):
        return self.visitChildren(ctx)

    def assessSearchStatement(self, ctx: DNPParser.SearchStatementContext):
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

        search_varying: DNPParser.SearchVaryingContext = ctx.searchVarying()
        if search_varying:
            varying_record_name = search_varying.qualifiedDataName()
            res["varying_record_name"] = get_original_code_content(
                self.parser,
                varying_record_name.start.tokenIndex,
                varying_record_name.stop.tokenIndex,
            )

        res["at_end_phrase"] = []
        at_end_phrase: DNPParser.AtEndPhraseContext = ctx.atEndPhrase()
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

    # Visit a parse tree produced by DNPParser#searchStatement.
    def visitSearchStatement(self, ctx: DNPParser.SearchStatementContext):
        res = self.assessSearchStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#searchVarying.
    def visitSearchVarying(self, ctx: DNPParser.SearchVaryingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#searchWhen.
    def visitSearchWhen(self, ctx: DNPParser.SearchWhenContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#sendStatement.
    def visitSendStatement(self, ctx: DNPParser.SendStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#sendStatementSync.
    def visitSendStatementSync(self, ctx: DNPParser.SendStatementSyncContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#sendStatementAsync.
    def visitSendStatementAsync(self, ctx: DNPParser.SendStatementAsyncContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#sendFromPhrase.
    def visitSendFromPhrase(self, ctx: DNPParser.SendFromPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#sendWithPhrase.
    def visitSendWithPhrase(self, ctx: DNPParser.SendWithPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#sendReplacingPhrase.
    def visitSendReplacingPhrase(self, ctx: DNPParser.SendReplacingPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#sendAdvancingPhrase.
    def visitSendAdvancingPhrase(self, ctx: DNPParser.SendAdvancingPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#sendAdvancingPage.
    def visitSendAdvancingPage(self, ctx: DNPParser.SendAdvancingPageContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#sendAdvancingLines.
    def visitSendAdvancingLines(self, ctx: DNPParser.SendAdvancingLinesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#sendAdvancingMnemonic.
    def visitSendAdvancingMnemonic(self, ctx: DNPParser.SendAdvancingMnemonicContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#setToStatement.
    def visitSetToStatement(self, ctx: DNPParser.SetToStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#setUpDownByStatement.
    def visitSetUpDownByStatement(self, ctx: DNPParser.SetUpDownByStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#setTo.
    def visitSetTo(self, ctx: DNPParser.SetToContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#setToValue.
    def visitSetToValue(self, ctx: DNPParser.SetToValueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#setByValue.
    def visitSetByValue(self, ctx: DNPParser.SetByValueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#sortStatement.
    def visitSortStatement(self, ctx: DNPParser.SortStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#sortOptional.
    def visitSortOptional(self, ctx: DNPParser.SortOptionalContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#sortOnKeyClause.
    def visitSortOnKeyClause(self, ctx: DNPParser.SortOnKeyClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#sortDuplicatesPhrase.
    def visitSortDuplicatesPhrase(self, ctx: DNPParser.SortDuplicatesPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#sortCollatingSequencePhrase.
    def visitSortCollatingSequencePhrase(
        self, ctx: DNPParser.SortCollatingSequencePhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#sortCollatingAlphanumeric.
    def visitSortCollatingAlphanumeric(
        self, ctx: DNPParser.SortCollatingAlphanumericContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#sortCollatingNational.
    def visitSortCollatingNational(self, ctx: DNPParser.SortCollatingNationalContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#sortInputProcedurePhrase.
    def visitSortInputProcedurePhrase(
        self, ctx: DNPParser.SortInputProcedurePhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#sortInputThrough.
    def visitSortInputThrough(self, ctx: DNPParser.SortInputThroughContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#sortUsing.
    def visitSortUsing(self, ctx: DNPParser.SortUsingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#sortOutputProcedurePhrase.
    def visitSortOutputProcedurePhrase(
        self, ctx: DNPParser.SortOutputProcedurePhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#sortOutputThrough.
    def visitSortOutputThrough(self, ctx: DNPParser.SortOutputThroughContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#sortGivingPhrase.
    def visitSortGivingPhrase(self, ctx: DNPParser.SortGivingPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#sortGiving.
    def visitSortGiving(self, ctx: DNPParser.SortGivingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#startStatement.
    def visitStartStatement(self, ctx: DNPParser.StartStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#startKey.
    def visitStartKey(self, ctx: DNPParser.StartKeyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#stopStatement.
    def visitStopStatement(self, ctx: DNPParser.StopStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#stopOption.
    def visitStopOption(self, ctx: DNPParser.StopOptionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#stringSendingPhrase.
    def visitStringSendingPhrase(self, ctx: DNPParser.StringSendingPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#stringSending.
    def visitStringSending(self, ctx: DNPParser.StringSendingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#stringDelimitedByPhrase.
    def visitStringDelimitedByPhrase(
        self, ctx: DNPParser.StringDelimitedByPhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#stringForPhrase.
    def visitStringForPhrase(self, ctx: DNPParser.StringForPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#stringIntoPhrase.
    def visitStringIntoPhrase(self, ctx: DNPParser.StringIntoPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#stringWithPointerPhrase.
    def visitStringWithPointerPhrase(
        self, ctx: DNPParser.StringWithPointerPhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#subtractFromStatement.
    def visitSubtractFromStatement(self, ctx: DNPParser.SubtractFromStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#subtractFromGivingStatement.
    def visitSubtractFromGivingStatement(
        self, ctx: DNPParser.SubtractFromGivingStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#subtractCorrespondingStatement.
    def visitSubtractCorrespondingStatement(
        self, ctx: DNPParser.SubtractCorrespondingStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#subtractSubtrahend.
    def visitSubtractSubtrahend(self, ctx: DNPParser.SubtractSubtrahendContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#subtractMinuend.
    def visitSubtractMinuend(self, ctx: DNPParser.SubtractMinuendContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#subtractMinuendGiving.
    def visitSubtractMinuendGiving(self, ctx: DNPParser.SubtractMinuendGivingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#subtractGiving.
    def visitSubtractGiving(self, ctx: DNPParser.SubtractGivingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#subtractMinuendCorresponding.
    def visitSubtractMinuendCorresponding(
        self, ctx: DNPParser.SubtractMinuendCorrespondingContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#transactionBegin.
    def visitTransactionBegin(self, ctx: DNPParser.TransactionBeginContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#transactionCancel.
    def visitTransactionCancel(self, ctx: DNPParser.TransactionCancelContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#transactionEnd.
    def visitTransactionEnd(self, ctx: DNPParser.TransactionEndContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#terminateStatement.
    def visitTerminateStatement(self, ctx: DNPParser.TerminateStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#unstringStatement.
    def visitUnstringStatement(self, ctx: DNPParser.UnstringStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#unstringSendingPhrase.
    def visitUnstringSendingPhrase(self, ctx: DNPParser.UnstringSendingPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#unstringDelimitedByPhrase.
    def visitUnstringDelimitedByPhrase(
        self, ctx: DNPParser.UnstringDelimitedByPhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#unstringOrAllPhrase.
    def visitUnstringOrAllPhrase(self, ctx: DNPParser.UnstringOrAllPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#unstringIntoPhrase.
    def visitUnstringIntoPhrase(self, ctx: DNPParser.UnstringIntoPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#unstringInto.
    def visitUnstringInto(self, ctx: DNPParser.UnstringIntoContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#unstringDelimiterIn.
    def visitUnstringDelimiterIn(self, ctx: DNPParser.UnstringDelimiterInContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#unstringCountIn.
    def visitUnstringCountIn(self, ctx: DNPParser.UnstringCountInContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#unstringWithPointerPhrase.
    def visitUnstringWithPointerPhrase(
        self, ctx: DNPParser.UnstringWithPointerPhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#unstringTallyingPhrase.
    def visitUnstringTallyingPhrase(self, ctx: DNPParser.UnstringTallyingPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#useStatement.
    def visitUseStatement(self, ctx: DNPParser.UseStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#useAfterClause.
    def visitUseAfterClause(self, ctx: DNPParser.UseAfterClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#useAfterOn.
    def visitUseAfterOn(self, ctx: DNPParser.UseAfterOnContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#useDebugClause.
    def visitUseDebugClause(self, ctx: DNPParser.UseDebugClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#useDebugOn.
    def visitUseDebugOn(self, ctx: DNPParser.UseDebugOnContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#useDeadLock.
    def visitUseDeadLock(self, ctx: DNPParser.UseDeadLockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#useProcedure.
    def visitUseProcedure(self, ctx: DNPParser.UseProcedureContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#waitArithmeticExpression.
    def visitWaitArithmeticExpression(
        self, ctx: DNPParser.WaitArithmeticExpressionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#attributeChangeEvent.
    def visitAttributeChangeEvent(self, ctx: DNPParser.AttributeChangeEventContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#attributeInputEvent.
    def visitAttributeInputEvent(self, ctx: DNPParser.AttributeInputEventContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#attributeOutputEvent.
    def visitAttributeOutputEvent(self, ctx: DNPParser.AttributeOutputEventContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#attributeAcceptEvent.
    def visitAttributeAcceptEvent(self, ctx: DNPParser.AttributeAcceptEventContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#attributeExceptionEvent.
    def visitAttributeExceptionEvent(
        self, ctx: DNPParser.AttributeExceptionEventContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#eventIdentifier.
    def visitEventIdentifier(self, ctx: DNPParser.EventIdentifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#crcrEvent.
    def visitCrcrEvent(self, ctx: DNPParser.CrcrEventContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#odtInputPresent.
    def visitOdtInputPresent(self, ctx: DNPParser.OdtInputPresentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#readOk.
    def visitReadOk(self, ctx: DNPParser.ReadOkContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#writeOk.
    def visitWriteOk(self, ctx: DNPParser.WriteOkContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#stoqEvent.
    def visitStoqEvent(self, ctx: DNPParser.StoqEventContext):
        return self.visitChildren(ctx)

    def assessWriteStatement(self, ctx: DNPParser.WriteStatementContext):
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

    # Visit a parse tree produced by DNPParser#writeStatement.
    def visitWriteStatement(self, ctx: DNPParser.WriteStatementContext):
        res = self.assessWriteStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)

        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#writeFromPhrase.
    def visitWriteFromPhrase(self, ctx: DNPParser.WriteFromPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#writeAdvancingPhrase.
    def visitWriteAdvancingPhrase(self, ctx: DNPParser.WriteAdvancingPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#writeAdvancingPage.
    def visitWriteAdvancingPage(self, ctx: DNPParser.WriteAdvancingPageContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#writeAdvancingLines.
    def visitWriteAdvancingLines(self, ctx: DNPParser.WriteAdvancingLinesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#writeAdvancingMnemonic.
    def visitWriteAdvancingMnemonic(self, ctx: DNPParser.WriteAdvancingMnemonicContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#writeAtEndOfPagePhrase.
    def visitWriteAtEndOfPagePhrase(self, ctx: DNPParser.WriteAtEndOfPagePhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#writeNotAtEndOfPagePhrase.
    def visitWriteNotAtEndOfPagePhrase(
        self, ctx: DNPParser.WriteNotAtEndOfPagePhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#atEndPhrase.
    def visitAtEndPhrase(self, ctx: DNPParser.AtEndPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#notAtEndPhrase.
    def visitNotAtEndPhrase(self, ctx: DNPParser.NotAtEndPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#invalidKeyPhrase.
    def visitInvalidKeyPhrase(self, ctx: DNPParser.InvalidKeyPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#notInvalidKeyPhrase.
    def visitNotInvalidKeyPhrase(self, ctx: DNPParser.NotInvalidKeyPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#onOverflowPhrase.
    def visitOnOverflowPhrase(self, ctx: DNPParser.OnOverflowPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#notOnOverflowPhrase.
    def visitNotOnOverflowPhrase(self, ctx: DNPParser.NotOnOverflowPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#onSizeErrorPhrase.
    def visitOnSizeErrorPhrase(self, ctx: DNPParser.OnSizeErrorPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#notOnSizeErrorPhrase.
    def visitNotOnSizeErrorPhrase(self, ctx: DNPParser.NotOnSizeErrorPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#onExceptionClause.
    def visitOnExceptionClause(self, ctx: DNPParser.OnExceptionClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#notOnExceptionClause.
    def visitNotOnExceptionClause(self, ctx: DNPParser.NotOnExceptionClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#arithmeticExpression.
    def visitArithmeticExpression(self, ctx: DNPParser.ArithmeticExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#plusMinus.
    def visitPlusMinus(self, ctx: DNPParser.PlusMinusContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#multDivs.
    def visitMultDivs(self, ctx: DNPParser.MultDivsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#multDiv.
    def visitMultDiv(self, ctx: DNPParser.MultDivContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#powers.
    def visitPowers(self, ctx: DNPParser.PowersContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#power.
    def visitPower(self, ctx: DNPParser.PowerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#basis.
    def visitBasis(self, ctx: DNPParser.BasisContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#condition.
    def visitCondition(self, ctx: DNPParser.ConditionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#andOrCondition.
    def visitAndOrCondition(self, ctx: DNPParser.AndOrConditionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#combinableCondition.
    def visitCombinableCondition(self, ctx: DNPParser.CombinableConditionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#simpleCondition.
    def visitSimpleCondition(self, ctx: DNPParser.SimpleConditionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#classCondition.
    def visitClassCondition(self, ctx: DNPParser.ClassConditionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#conditionNameReference.
    def visitConditionNameReference(self, ctx: DNPParser.ConditionNameReferenceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#conditionNameSubscriptReference.
    def visitConditionNameSubscriptReference(
        self, ctx: DNPParser.ConditionNameSubscriptReferenceContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#attributeCondition.
    def visitAttributeCondition(self, ctx: DNPParser.AttributeConditionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#attributeConditionExpr.
    def visitAttributeConditionExpr(self, ctx: DNPParser.AttributeConditionExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#relationCondition.
    def visitRelationCondition(self, ctx: DNPParser.RelationConditionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#relationSignCondition.
    def visitRelationSignCondition(self, ctx: DNPParser.RelationSignConditionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#relationArithmeticComparison.
    def visitRelationArithmeticComparison(
        self, ctx: DNPParser.RelationArithmeticComparisonContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#relationCombinedComparison.
    def visitRelationCombinedComparison(
        self, ctx: DNPParser.RelationCombinedComparisonContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#relationCombinedCondition.
    def visitRelationCombinedCondition(
        self, ctx: DNPParser.RelationCombinedConditionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#relationalOperator.
    def visitRelationalOperator(self, ctx: DNPParser.RelationalOperatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#abbreviation.
    def visitAbbreviation(self, ctx: DNPParser.AbbreviationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#identifier.
    def visitIdentifier(self, ctx: DNPParser.IdentifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#tableCall.
    def visitTableCall(self, ctx: DNPParser.TableCallContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#functionCall.
    def visitFunctionCall(self, ctx: DNPParser.FunctionCallContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#referenceModifier.
    def visitReferenceModifier(self, ctx: DNPParser.ReferenceModifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#characterPosition.
    def visitCharacterPosition(self, ctx: DNPParser.CharacterPositionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#length.
    def visitLength(self, ctx: DNPParser.LengthContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#subscript_.
    def visitSubscript_(self, ctx: DNPParser.Subscript_Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#argument.
    def visitArgument(self, ctx: DNPParser.ArgumentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#qualifiedDataName.
    def visitQualifiedDataName(self, ctx: DNPParser.QualifiedDataNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#qualifiedDataNameFormat1.
    def visitQualifiedDataNameFormat1(
        self, ctx: DNPParser.QualifiedDataNameFormat1Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#qualifiedDataNameFormat2.
    def visitQualifiedDataNameFormat2(
        self, ctx: DNPParser.QualifiedDataNameFormat2Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#qualifiedDataNameFormat3.
    def visitQualifiedDataNameFormat3(
        self, ctx: DNPParser.QualifiedDataNameFormat3Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#qualifiedDataNameFormat4.
    def visitQualifiedDataNameFormat4(
        self, ctx: DNPParser.QualifiedDataNameFormat4Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#qualifiedInData.
    def visitQualifiedInData(self, ctx: DNPParser.QualifiedInDataContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#inData.
    def visitInData(self, ctx: DNPParser.InDataContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#inFile.
    def visitInFile(self, ctx: DNPParser.InFileContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#inMnemonic.
    def visitInMnemonic(self, ctx: DNPParser.InMnemonicContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#inSection.
    def visitInSection(self, ctx: DNPParser.InSectionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#inLibrary.
    def visitInLibrary(self, ctx: DNPParser.InLibraryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#inTable.
    def visitInTable(self, ctx: DNPParser.InTableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#alphabetName.
    def visitAlphabetName(self, ctx: DNPParser.AlphabetNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#assignmentName.
    def visitAssignmentName(self, ctx: DNPParser.AssignmentNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#basisName.
    def visitBasisName(self, ctx: DNPParser.BasisNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#cdName.
    def visitCdName(self, ctx: DNPParser.CdNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#className.
    def visitClassName(self, ctx: DNPParser.ClassNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#computerName.
    def visitComputerName(self, ctx: DNPParser.ComputerNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#conditionName.
    def visitConditionName(self, ctx: DNPParser.ConditionNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataName.
    def visitDataName(self, ctx: DNPParser.DataNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#dataDescName.
    def visitDataDescName(self, ctx: DNPParser.DataDescNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#environmentName.
    def visitEnvironmentName(self, ctx: DNPParser.EnvironmentNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#fileAttribute.
    def visitFileAttribute(self, ctx: DNPParser.FileAttributeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#fileName.
    def visitFileName(self, ctx: DNPParser.FileNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#functionName.
    def visitFunctionName(self, ctx: DNPParser.FunctionNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#indexName.
    def visitIndexName(self, ctx: DNPParser.IndexNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#languageName.
    def visitLanguageName(self, ctx: DNPParser.LanguageNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#libraryName.
    def visitLibraryName(self, ctx: DNPParser.LibraryNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#localName.
    def visitLocalName(self, ctx: DNPParser.LocalNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#mnemonicName.
    def visitMnemonicName(self, ctx: DNPParser.MnemonicNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#paragraphName.
    def visitParagraphName(self, ctx: DNPParser.ParagraphNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#procedureName.
    def visitProcedureName(self, ctx: DNPParser.ProcedureNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#programName.
    def visitProgramName(self, ctx: DNPParser.ProgramNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#recordName.
    def visitRecordName(self, ctx: DNPParser.RecordNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#reportName.
    def visitReportName(self, ctx: DNPParser.ReportNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#routineName.
    def visitRoutineName(self, ctx: DNPParser.RoutineNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#screenName.
    def visitScreenName(self, ctx: DNPParser.ScreenNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#sectionName.
    def visitSectionName(self, ctx: DNPParser.SectionNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#systemName.
    def visitSystemName(self, ctx: DNPParser.SystemNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#symbolicCharacter.
    def visitSymbolicCharacter(self, ctx: DNPParser.SymbolicCharacterContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#textName.
    def visitTextName(self, ctx: DNPParser.TextNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#booleanLiteral.
    def visitBooleanLiteral(self, ctx: DNPParser.BooleanLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#numericLiteral.
    def visitNumericLiteral(self, ctx: DNPParser.NumericLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#integerLiteral.
    def visitIntegerLiteral(self, ctx: DNPParser.IntegerLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#cicsDfhRespLiteral.
    def visitCicsDfhRespLiteral(self, ctx: DNPParser.CicsDfhRespLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#cicsDfhValueLiteral.
    def visitCicsDfhValueLiteral(self, ctx: DNPParser.CicsDfhValueLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#figurativeConstant.
    def visitFigurativeConstant(self, ctx: DNPParser.FigurativeConstantContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#specialRegister.
    def visitSpecialRegister(self, ctx: DNPParser.SpecialRegisterContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#commentEntry.
    def visitCommentEntry(self, ctx: DNPParser.CommentEntryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DNPParser#charDataKeyword.
    def visitCharDataKeyword(self, ctx: DNPParser.CharDataKeywordContext):
        return self.visitChildren(ctx)

    def assessAcceptStatement(self, ctx: DNPParser.AcceptStatementContext):
        tag = "AcceptStatement"

        identifier = recursive_find_first_child_by_type(
            ctx, DNPParser.IdentifierContext
        )

        raw = get_original_code_content(
            self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex
        )
        start_token = ctx.start
        stop_token = ctx.stop

        if not identifier:
            logger.warning(f"Identifier is missing in accept statement'{raw}'")

        return {
            "tag": tag,
            "raw": raw,
            "start_line": start_token.line,
            "stop_line": stop_token.line,
            "start_idx": start_token.start,
            "stop_idx": stop_token.stop,
            "identifier": identifier.getText() if identifier else "",
        }

    # Visit a parse tree produced by DNPParser#acceptStatement.
    def visitAcceptStatement(self, ctx: DNPParser.AcceptStatementContext):

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
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)

        self.statements.append(res)

        return self.visitChildren(ctx)

    def assessAcceptFromDateStatement(
        self, ctx: DNPParser.AcceptFromDateStatementContext
    ):
        tag = "AcceptFromDateStatement"

        accept_from_date_phrase = ctx.acceptFromDatePhrase()

        date = get_original_code_content(
            self.parser,
            accept_from_date_phrase.start.tokenIndex,
            accept_from_date_phrase.stop.tokenIndex,
        )

        # fix missing code by getting the parent code
        accept_statement_context: DNPParser.AcceptStatementContext = ctx.parentCtx

        identifier = accept_statement_context.identifier()

        raw = get_original_code_content(
            self.parser,
            accept_statement_context.start.tokenIndex,
            accept_statement_context.stop.tokenIndex,
        )
        start_token = ctx.start
        stop_token = ctx.stop

        if not date:
            logger.warning(f"Date is missing in accept from date statement'{raw}'")

        return {
            "tag": tag,
            "raw": raw,
            "start_line": start_token.line,
            "stop_line": stop_token.line,
            "start_idx": start_token.start,
            "stop_idx": stop_token.stop,
            "identifier": identifier.getText() if identifier else "",
            "datetime": date,
        }

    # Visit a parse tree produced by DNPParser#acceptFromDateStatement.
    def visitAcceptFromDateStatement(
        self, ctx: DNPParser.AcceptFromDateStatementContext
    ):
        res = self.assessAcceptFromDateStatement(ctx)

        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)

        self.statements.append(res)
        return self.visitChildren(ctx)

    def assessAcceptFromMnemonicStatement(
        self, ctx: DNPParser.AcceptFromMnemonicStatementContext
    ):
        tag = "AcceptFromMnemonicStatement"
        mnemonic = ctx.getChild(1)

        accept_statement_context: DNPParser.AcceptStatementContext = ctx.parentCtx

        identifier = accept_statement_context.identifier()

        raw = get_original_code_content(
            self.parser,
            accept_statement_context.start.tokenIndex,
            accept_statement_context.stop.tokenIndex,
        )
        start_token = ctx.start
        stop_token = ctx.stop

        if not mnemonic:
            logger.warning(
                f"Mnemonic is missing in accept from mnemonic statement'{raw}'"
            )

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

    # Visit a parse tree produced by DNPParser#acceptFromMnemonicStatement.
    def visitAcceptFromMnemonicStatement(
        self, ctx: DNPParser.AcceptFromMnemonicStatementContext
    ):
        res = self.assessAcceptFromMnemonicStatement(ctx)

        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)

        return self.visitChildren(ctx)

    def assessAcceptFromEscapeKeyStatement(
        self, ctx: DNPParser.AcceptFromEscapeKeyStatementContext
    ):
        tag = "AcceptFromEscapeKeyStatement"

        accept_statement_context: DNPParser.AcceptStatementContext = ctx.parentCtx
        identifier = accept_statement_context.identifier()

        raw = get_original_code_content(
            self.parser,
            accept_statement_context.start.tokenIndex,
            accept_statement_context.stop.tokenIndex,
        )
        start_token = ctx.start
        stop_token = ctx.stop

        if not identifier:
            logger.warning(f"Identifier is missing in accept statement'{raw}'")

        return {
            "tag": tag,
            "raw": raw,
            "start_line": start_token.line,
            "stop_line": stop_token.line,
            "start_idx": start_token.start,
            "stop_idx": stop_token.stop,
            "identifier": identifier.getText() if identifier else "",
        }

    # Visit a parse tree produced by DNPParser#acceptFromEscapeKeyStatement.
    def visitAcceptFromEscapeKeyStatement(
        self, ctx: DNPParser.AcceptFromEscapeKeyStatementContext
    ):
        res = self.assessAcceptFromEscapeKeyStatement(ctx)

        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)

        return self.visitChildren(ctx)

    def assessAcceptFromMessageCountStatement(self, ctx):
        tag = "AcceptFromMessageCountStatement"

        accept_statement_context: DNPParser.AcceptStatementContext = ctx.parentCtx
        identifier = accept_statement_context.identifier()

        raw = get_original_code_content(
            self.parser,
            accept_statement_context.start.tokenIndex,
            accept_statement_context.stop.tokenIndex,
        )
        start_token = ctx.start
        stop_token = ctx.stop

        if not identifier:
            logger.warning(f"Identifier is missing in accept statement'{raw}'")

        return {
            "tag": tag,
            "raw": raw,
            "start_line": start_token.line,
            "stop_line": stop_token.line,
            "start_idx": start_token.start,
            "stop_idx": stop_token.stop,
            "identifier": identifier.getText() if identifier else "",
        }

    # Visit a parse tree produced by DNPParser#acceptMessageCountStatement.
    def visitAcceptMessageCountStatement(
        self, ctx: DNPParser.AcceptMessageCountStatementContext
    ):
        res = self.assessAcceptFromMessageCountStatement(ctx)

        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def assessAddStatement(self, ctx: DNPParser.AddStatementContext):
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
        if DNPParser.AddToStatementContext in children:
            addToStatement = ctx.addToStatement()
            # addFrom
            addFrom = addToStatement.addFrom()
            if addFrom:
                res["identifier_1"] = []
                res["literal_1"] = []
                for af in addFrom:
                    for a in af.getChildren():
                        if isinstance(a, DNPParser.IdentifierContext):
                            # res["identifier_1"].append(a.getText())
                            res["identifier_1"].append(
                                get_original_code_content(
                                    self.parser,
                                    a.start.tokenIndex,
                                    a.stop.tokenIndex,
                                )
                            )
                        elif isinstance(a, DNPParser.LiteralContext):
                            res["literal_1"].append(a.getText())
            # addTo
            addTo = addToStatement.addTo()
            if addTo:
                res["identifier_2"] = []
                res["literal_2"] = []
                for at in addTo:
                    for a in at.getChildren():
                        if isinstance(a, DNPParser.IdentifierContext):
                            # res["identifier_2"].append(a.getText())
                            res["identifier_2"].append(
                                get_original_code_content(
                                    self.parser,
                                    a.start.tokenIndex,
                                    a.stop.tokenIndex,
                                )
                            )
                        elif isinstance(a, DNPParser.LiteralContext):
                            res["literal_2"].append(a.getText())
                        elif isinstance(a, DNPParser.FigurativeConstantContext):
                            res["literal_2"].append(a.getText())

        # AddToGiving
        elif DNPParser.AddToGivingStatementContext in children:
            addToGivingStatement = ctx.addToGivingStatement()
            # addFrom
            addFrom = addToGivingStatement.addFrom()
            if addFrom:
                res["identifier_1"] = []
                res["literal_1"] = []
                for af in addFrom:
                    for a in af.getChildren():
                        if isinstance(a, DNPParser.IdentifierContext):
                            # res["identifier_1"].append(a.getText())
                            res["identifier_1"].append(
                                get_original_code_content(
                                    self.parser,
                                    a.start.tokenIndex,
                                    a.stop.tokenIndex,
                                )
                            )
                        elif isinstance(a, DNPParser.LiteralContext):
                            res["literal_1"].append(a.getText())
            # addToGiving
            addToGiving = addToGivingStatement.addToGiving()
            if addToGiving:
                res["identifier_2"] = []
                res["literal_2"] = []
                for at in addToGiving:
                    for a in at.getChildren():
                        if isinstance(a, DNPParser.IdentifierContext):
                            # res["identifier_2"].append(a.getText())
                            res["identifier_2"].append(
                                get_original_code_content(
                                    self.parser,
                                    a.start.tokenIndex,
                                    a.stop.tokenIndex,
                                )
                            )
                        elif isinstance(a, DNPParser.LiteralContext):
                            res["literal_2"].append(a.getText())
                        elif isinstance(a, DNPParser.FigurativeConstantContext):
                            res["literal_2"].append(a.getText())
            # addGiving
            addGiving = addToGivingStatement.addGiving()
            if addGiving:
                res["identifier_3"] = []
                res["literal_3"] = []
                for ag in addGiving:
                    for a in ag.getChildren():
                        if isinstance(a, DNPParser.IdentifierContext):
                            # res["identifier_3"].append(a.getText())
                            res["identifier_3"].append(
                                get_original_code_content(
                                    self.parser,
                                    a.start.tokenIndex,
                                    a.stop.tokenIndex,
                                )
                            )
                        elif isinstance(a, DNPParser.LiteralContext):
                            res["literal_3"].append(a.getText())

        return res

    def visitAddStatement(self, ctx: DNPParser.AddStatementContext):
        res = self.assessAddStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessAlterStatement(self, ctx: DNPParser.AlterStatementContext):
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
        # print(res)
        return res

    def visitAlterStatement(self, ctx: DNPParser.AlterStatementContext):
        res = self.assessAlterStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessCallStatement(self, ctx: DNPParser.CallStatementContext):
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
        if DNPParser.LiteralContext in children:
            literal = ctx.literal()
            res["call_literal"] = literal.getText()
        # identifier_1
        elif DNPParser.IdentifierContext in children:
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
            call_using_parameter_list: List[DNPParser.CallUsingParameterContext] = (
                callUsingPhrase.callUsingParameter()
            )

            for call_using_parameter in call_using_parameter_list:
                call_using_parameter = call_using_parameter.getChild(0)
                if isinstance(
                    call_using_parameter, DNPParser.CallByReferencePhraseContext
                ):
                    call_by_reference_list: List[DNPParser.CallByReferenceContext] = (
                        call_using_parameter.callByReference()
                    )

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
                    call_using_parameter, DNPParser.CallByValuePhraseContext
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
                    call_using_parameter, DNPParser.CallByContentPhraseContext
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

    def visitCallStatement(self, ctx: DNPParser.CallStatementContext):
        res = self.assessCallStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessCloseStatement(self, ctx: DNPParser.CloseStatementContext):
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

    def visitCloseStatement(self, ctx: DNPParser.CloseStatementContext):
        res = self.assessCloseStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessComputeStatement(self, ctx: DNPParser.ComputeStatementContext):
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
        # print(res)
        return res

    def visitComputeStatement(self, ctx: DNPParser.ComputeStatementContext):
        res = self.assessComputeStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessContinueStatement(self, ctx: DNPParser.ContinueStatementContext):
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
        # print(res)
        return res

    def visitContinueStatement(self, ctx: DNPParser.ContinueStatementContext):
        res = self.assessContinueStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessCopyStatement(self, ctx: DNPParser.CopyStatementContext):
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
            # DNPParser.LiteralContext
            if DNPParser.LiteralContext in children:
                literal = copySource.literal()
                res["literal_1"] = literal.getText()
            # DNPParser.CobolWordContext
            elif DNPParser.CobolWordContext in children:
                cobolWord = copySource.cobolWord()
                res["text_name"] = cobolWord.getText()
            # DNPParser.FileNameContext
            elif DNPParser.FileNameContext in children:
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
        # print(res)
        return res

    def assessDisplayStatement(self, ctx: DNPParser.DisplayStatementContext):
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
                    if isinstance(d, DNPParser.IdentifierContext):
                        # res["identifier_1"].append(d.getText())
                        res["identifier_1"].append(
                            get_original_code_content(
                                self.parser, d.start.tokenIndex, d.stop.tokenIndex
                            )
                        )
                    elif isinstance(d, DNPParser.LiteralContext):
                        res["literal_1"].append(d.getText())
        # print(res)
        return res

    def visitDisplayStatement(self, ctx: DNPParser.DisplayStatementContext):
        res = self.assessDisplayStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessEvaluateStatement(self, ctx: DNPParser.EvaluateStatementContext):
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

        evaluate_select: DNPParser.EvaluateSelectContext = ctx.evaluateSelect()

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
                        else:
                            r["statement"].append(
                                get_original_code_content(
                                    self.parser, start_idx, stop_idx
                                )
                            )
                # Update
                res["evaluateWhenPhrase"].append(r)

        # evaluateWhenOther
        evaluateWhenOther = ctx.evaluateWhenOther()
        if evaluateWhenOther:
            res["evaluateWhenOther"] = []

        return res

    def visitEvaluateStatement(self, ctx: DNPParser.EvaluateStatementContext):
        res = self.assessEvaluateStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    # def assessExecCicsStatement2(
    #     self, ctx: DNPParser.ExecCicsStatement2Context
    # ):
    #     # Intialize
    #     tag = "ExecCicsStatement2"
    #     res = {}
    #     res["tag"] = tag
    #     # Get position and raw string
    #     start_token = ctx.start
    #     stop_token = ctx.stop
    #     res["start_line"] = start_token.line
    #     res["stop_line"] = stop_token.line
    #     res["start_idx"] = start_token.start
    #     res["stop_idx"] = stop_token.stop
    #     res["raw"] = get_original_code_content(
    #         self.parser, start_token.tokenIndex, stop_token.tokenIndex
    #     )
    #     # commandName
    #     commandName = ctx.commandName()
    #     res["commandName"] = commandName.getText()
    #     # commandBody
    #     commandBody = ctx.commandBody()
    #     if commandBody:
    #         res["commandBody"] = []
    #         commandParameter = commandBody.commandParameter()
    #         for cp in commandParameter:
    #             parameterName = cp.parameterName()
    #             parameterValue = cp.parameterValue()
    #             parameterValueWithIndex = cp.parameterValueWithIndex()
    #             if parameterValue:
    #                 res["commandBody"].append(
    #                     {
    #                         "parameterName": parameterName.getText(),
    #                         "parameterValue": parameterValue.getText(),
    #                     }
    #                 )
    #             elif parameterValueWithIndex:
    #                 res["commandBody"].append(
    #                     {
    #                         "parameterName": parameterName.getText(),
    #                         "parameterValue": parameterValueWithIndex.getText(),
    #                     }
    #                 )
    #             else:
    #                 res["commandBody"].append(
    #                     {"parameterName": parameterName.getText(), "parameterValue": ""}
    #                 )
    #     return res

    def visitExecCicsStatement2(self, ctx: DNPParser.ExecCicsStatement2Context):
        # res = self.assessExecCicsStatement2(ctx)
        # parent = ctx.parentCtx
        # grand_parent = parent.parentCtx
        # paragraph = find_parent_by_type(ctx, DNPParser.ParagraphContext)
        # if paragraph:
        #     paragraphName = paragraph.paragraphName()
        #     res["paragraph"] = paragraphName.getText()
        # else:
        #     res["paragraph"] = None
        # procedure_section = self.find_parent(
        #     ctx, DNPParser.ProcedureSectionContext
        # )
        # if procedure_section:
        #     procedure_section_header = procedure_section.procedureSectionHeader()
        #     sectionName = procedure_section_header.sectionName()
        #     res["section"] = sectionName.getText()
        # else:
        #     res["section"] = None
        # if type(grand_parent).__name__ == "SentenceContext":
        #     self.statements.append(res)
        return self.visitChildren(ctx)

    def assessExitStatement(self, ctx: DNPParser.ExitStatementContext):
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

    def visitExitStatement(self, ctx: DNPParser.ExitStatementContext):
        res = self.assessExitStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessGobackStatement(self, ctx: DNPParser.GobackStatementContext):
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

    def visitGobackStatement(self, ctx: DNPParser.GobackStatementContext):
        res = self.assessGobackStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessFindStatement(self, ctx: DNPParser.FindStatementContext):
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

    # Visit a parse tree produced by DNPParser#findStatement.
    def visitFindStatement(self, ctx: DNPParser.FindStatementContext):
        res = self.assessFindStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)

        return self.visitChildren(ctx)

        return self.visitChildren(ctx)

    def assessLockStatement(self, ctx: DNPParser.LockStatementContext):
        tag = "LockStatement"
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

        database_name = ctx.qualifiedDataName()
        res["database_name"] = get_original_code_content(
            self.parser,
            database_name.start.tokenIndex,
            database_name.stop.tokenIndex,
        )

        lock_type = ctx.FIRST() or ctx.NEXT()
        res["lock_type"] = lock_type.getText().upper() if lock_type else None

        via_clause = ctx.viaClause()

        if via_clause:
            lock_option = via_clause.findOption()
            via_identifier = via_clause.identifier()

            res["lock_option"] = lock_option.getText().upper() if lock_option else None
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

    def visitLockStatement(self, ctx: DNPParser.LockStatementContext):
        res = self.assessLockStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)

        return super().visitLockStatement(ctx)

    def visitAttachStatement(self, ctx: DNPParser.AttachStatementContext):
        tag = "AttachStatement"
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

        self.statements.append(res)
        return super().visitAttachStatement(ctx)

    def assessTransactionStatement(self, ctx: DNPParser.TransactionStatementContext):
        tag = "TransactionStatement"
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

        transaction = ctx.getChild(0)
        if isinstance(transaction, DNPParser.TransactionBeginContext):
            res["transaction_type"] = "BEGIN"
            audit = transaction.AUDIT()
            no_audit = transaction.NO_AUDIT()
            audit_option = (
                audit.getText().upper()
                if audit
                else no_audit.getText() if no_audit else None
            )

            database_name = transaction.qualifiedDataName()
            sync = True if transaction.SYNC() else False

            transaction_details = {
                "audit_option": audit_option,
                "database_name": database_name.getText(),
                "sync": sync,
            }

            transaction_details["on_exception_clause"] = []
            on_exception_clause = transaction.onExceptionClause()
            if on_exception_clause:
                statements = on_exception_clause.statement()
                for statement in statements:
                    child = statement.getChild(0)
                    type_ = type(child).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        transaction_details["on_exception_clause"].append(f(child))

            res["transaction_details"] = transaction_details

        elif isinstance(transaction, DNPParser.TransactionEndContext):
            res["transaction_type"] = "END"
            audit = transaction.AUDIT()
            no_audit = transaction.NO_AUDIT()
            audit_option = (
                audit.getText().upper()
                if audit
                else no_audit.getText() if no_audit else None
            )

            database_name = transaction.qualifiedDataName()
            sync = True if transaction.SYNC() else False

            transaction_details = {
                "audit_option": audit_option,
                "database_name": database_name.getText(),
                "sync": sync,
            }

            transaction_details["on_exception_clause"] = []
            on_exception_clause = transaction.onExceptionClause()
            if on_exception_clause:
                statements = on_exception_clause.statement()
                for statement in statements:
                    child = statement.getChild(0)
                    type_ = type(child).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        transaction_details["on_exception_clause"].append(f(child))

            res["transaction_details"] = transaction_details

        elif isinstance(transaction, DNPParser.TransactionCancelContext):
            res["transaction_type"] = "CANCEL"
            res["transaction_details"] = None

        return res

    def visitTransactionStatement(self, ctx: DNPParser.TransactionStatementContext):
        res = self.assessTransactionStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)

        return super().visitTransactionStatement(ctx)

    def assessWaitStatement(self, ctx: DNPParser.WaitStatementContext):
        tag = "WaitStatement"
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

        reset = ctx.RESET()
        until = ctx.UNTIL()

        res["is_reset"] = True if reset else False
        res["is_wait_until"] = True if until else False

        wait_arithmetic_expression = ctx.waitArithmeticExpression()

        res["option"] = get_original_code_content(
            self.parser,
            wait_arithmetic_expression.start.tokenIndex,
            wait_arithmetic_expression.stop.tokenIndex,
        )

        identifier = recursive_find_first_child_by_type(
            ctx, DNPParser.IdentifierContext
        )
        if identifier:
            res["identifier"] = identifier.getText()

        literal = recursive_find_first_child_by_type(ctx, DNPParser.LiteralContext)

        if literal:
            res["literal"] = literal.getText()

        library_entry_procedure_using_clause = recursive_find_first_child_by_type(
            ctx, DNPParser.LibraryEntryProcedureUsingClauseContext
        )

        if library_entry_procedure_using_clause:
            using_names = (
                library_entry_procedure_using_clause.libraryEntryProcedureUsingName()
            )

            res["using_data_names"] = [name.getText() for name in using_names]

        library_entry_procedure_giving_clause = recursive_find_first_child_by_type(
            ctx, DNPParser.LibraryEntryProcedureGivingClauseContext
        )

        if library_entry_procedure_giving_clause:
            res["giving_data_name"] = (
                library_entry_procedure_giving_clause.dataName().getText()
            )

        self.statements.append(res)

        return res

    def visitWaitStatement(self, ctx: DNPParser.WaitStatementContext):
        res = self.assessWaitStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)

        return super().visitWaitStatement(ctx)

    def assessCreateStatement(self, ctx: DNPParser.CreateStatementContext):
        tag = "CreateStatement"
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

        create_type = ctx.getChild(0)
        identifier = ctx.identifier()

        res["create_type"] = create_type.getText().upper()
        res["identifier"] = identifier.getText()

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

    def visitCreateStatement(self, ctx: DNPParser.CreateStatementContext):
        res = self.assessCreateStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)

        return super().visitCreateStatement(ctx)

    def assessFreeStatement(self, ctx: DNPParser.FreeStatementContext):
        raw = get_original_code_content(
            self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex
        )
        tag = "FreeStatement"
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

        if not identifier:
            logger.warning(f"No identifier found in FreeStatement '{raw}'")

        res["identifier"] = identifier.getText() if identifier else ""
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

    def visitFreeStatement(self, ctx: DNPParser.FreeStatementContext):
        res = self.assessFreeStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)

        return super().visitFreeStatement(ctx)

    def assessModifyStatement(self, ctx: DNPParser.ModifyStatementContext):
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

        file_name = ctx.fileName()
        modify_to = ctx.modifyTo()
        condition = ctx.condition()

        res["file_name"] = file_name.getText()

        modify_to_child = modify_to.getChild(0)

        if isinstance(modify_to_child, DNPParser.IdentifierContext):
            res["modify_to"] = modify_to_child.getText()
        elif isinstance(modify_to_child, DNPParser.LiteralContext):
            res["modify_to"] = get_original_code_content(
                self.parser,
                modify_to_child.start.tokenIndex,
                modify_to_child.stop.tokenIndex,
            )
        elif isinstance(modify_to_child, DNPParser.ArithmeticExpressionContext):
            res["modify_to"] = get_original_code_content(
                self.parser,
                modify_to_child.start.tokenIndex,
                modify_to_child.stop.tokenIndex,
            )
        else:
            cobol_word = recursive_find_first_child_by_type(
                modify_to, DNPParser.CobolWordContext
            )

            if not cobol_word:
                logger.warning(
                    f"No identifier or literal found in ModifyStatement '{res['raw']}'"
                )
                res["modify_to"] = ""

            else:
                res["modify_to"] = cobol_word.getText()

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

    def visitModifyStatement(self, ctx: DNPParser.ModifyStatementContext):
        res = self.assessModifyStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)

        return super().visitModifyStatement(ctx)

    def assessStoreStatement(self, ctx: DNPParser.StoreStatementContext):
        tag = "StoreStatement"
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

        database_name = ctx.qualifiedDataName()
        res["database_name"] = database_name.getText()

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

    def visitStoreStatement(self, ctx: DNPParser.StoreStatementContext):
        res = self.assessStoreStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)

        return super().visitStoreStatement(ctx)

    def assessChangeStatement(self, ctx: DNPParser.ChangeStatementContext):
        tag = "ChangeStatement"
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

        attribute_token = ctx.ATTRIBUTE()
        change_attribute = ctx.getChild(2)

        if isinstance(change_attribute, DNPParser.ChangeFileAttributeContext):
            res["attribute_type"] = "FILE"
            source_identifier = get_original_code_content(
                self.parser,
                change_attribute.getChild(1).start.tokenIndex,
                change_attribute.getChild(1).stop.tokenIndex,
            )
            res["source_identifier"] = source_identifier
            res["source_option"] = get_original_code_content(
                self.parser,
                attribute_token.symbol.tokenIndex,
                change_attribute.getChild(1).stop.tokenIndex,
            )

            target_identifier = change_attribute.identifier()

            target_literal = change_attribute.literal()
            res["target_identifier"] = (
                target_identifier.getText() if target_identifier else None
            )
            res["target_literal"] = target_literal.getText() if target_literal else None
            res["target_option"] = None

        elif isinstance(change_attribute, DNPParser.ChangeLibraryAttributeContext):
            res["attribute_type"] = "LIBRARY"
            library_attribute_name: DNPParser.LibraryAttributeNameContext = (
                change_attribute.libraryAttributeName()
            )

            # check library attribute name is literal or identifier
            cobol_word: DNPParser.CobolWordContext = library_attribute_name.cobolWord()

            if isinstance(cobol_word, DNPParser.CharDataKeywordContext):
                res["source_identifier"] = None
                res["source_literal"] = library_attribute_name.getText()

            else:
                res["source_identifier"] = library_attribute_name.getText()
                res["source_literal"] = None

            of_library_name = change_attribute.getChild(2)
            if isinstance(of_library_name, TerminalNode):
                library_name = get_original_code_content(
                    self.parser,
                    of_library_name.symbol.tokenIndex,
                    of_library_name.symbol.tokenIndex,
                )
            else:
                library_name = get_original_code_content(
                    self.parser,
                    of_library_name.start.tokenIndex,
                    of_library_name.stop.tokenIndex,
                )
            res["library_name"] = library_name

            source_option = get_original_code_content(
                self.parser,
                attribute_token.symbol.tokenIndex,
                change_attribute.getChild(2).stop.tokenIndex,
            )

            res["source_option"] = source_option

            library_value_option: DNPParser.LibraryValueOptionContext = (
                change_attribute.libraryValueOption()
            )

            target_identifier = library_value_option.identifier()
            target_literal = library_value_option.literal()

            res["target_identifier"] = (
                target_identifier.getText() if target_identifier else None
            )
            res["target_literal"] = target_literal.getText() if target_literal else None
            res["target_option"] = library_value_option.getText()

        return res

    def visitChangeStatement(self, ctx: DNPParser.ChangeStatementContext):
        res = self.assessChangeStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)

        return super().visitChangeStatement(ctx)

    def assessGoToStatement(self, ctx: DNPParser.GoToStatementContext):
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
        # print(res)
        return res

    def visitGoToStatement(self, ctx: DNPParser.GoToStatementContext):
        res = self.assessGoToStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessIfStatement(self, ctx: DNPParser.IfStatementContext):
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

    def visitIfStatement(self, ctx: DNPParser.IfStatementContext):
        res = self.assessIfStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessInitializeStatement(self, ctx: DNPParser.InitializeStatementContext):
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
        # print(res)
        return res

    def visitInitializeStatement(self, ctx: DNPParser.InitializeStatementContext):
        res = self.assessInitializeStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessInspectStatement(self, ctx: DNPParser.InspectStatementContext):
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

        if isinstance(inspect_phrase, DNPParser.InspectReplacingPhraseContext):
            inspect_replacing_phrase_dict = self.extract_inspect_replacing_phrase(
                inspect_phrase
            )
            res["phrase"] = inspect_replacing_phrase_dict

        elif isinstance(inspect_phrase, DNPParser.InspectTallyingPhraseContext):
            inspect_tallying_phrase_dict = self.extract_inspect_tallying(inspect_phrase)
            res["phrase"] = inspect_tallying_phrase_dict

        elif isinstance(
            inspect_phrase, DNPParser.InspectTallyingReplacingPhraseContext
        ):
            inspect_tallying_replacing_dict = self.extract_inspect_tallying_replacing(
                inspect_phrase
            )
            res["phrase"] = inspect_tallying_replacing_dict

        elif isinstance(inspect_phrase, DNPParser.InspectConvertingPhraseContext):
            inspect_converting_phrase_dict = self.extract_inspect_converting_phrase(
                inspect_phrase
            )
            res["phrase"] = inspect_converting_phrase_dict

        return res

    def visitInspectStatement(self, ctx: DNPParser.InspectStatementContext):
        res = self.assessInspectStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def extract_inspect_converting_phrase(
        self,
        inspect_converting_phrase: DNPParser.InspectConvertingPhraseContext,
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

    def extract_inspect_tallying_replacing(
        self, inspect_phrase: DNPParser.InspectTallyingReplacingPhraseContext
    ):
        inspect_tallying_replacing_phrase_dict = {"tallying": [], "replacing": []}
        inspect_for_list = inspect_phrase.inspectFor()

        for inspect_for in inspect_for_list:
            inspect_for_dict = self.extract_inspect_for(inspect_for)
            inspect_tallying_replacing_phrase_dict["tallying"].append(inspect_for_dict)

        inspect_replacing_phrase_list = inspect_phrase.inspectReplacingPhrase()
        for inspect_replacing_phrase in inspect_replacing_phrase_list:
            inspect_replacing_phrase_dict = self.extract_inspect_replacing_phrase(
                inspect_replacing_phrase
            )
            inspect_tallying_replacing_phrase_dict["replacing"].append(
                inspect_replacing_phrase_dict
            )

        return inspect_tallying_replacing_phrase_dict

    def extract_inspect_replacing_phrase(
        self, inspect_phrase: DNPParser.InspectReplacingPhraseContext
    ):
        inspect_replacing_phrase_dict = {"replacements": []}

        for child in inspect_phrase.getChildren():
            if isinstance(child, DNPParser.InspectReplacingCharactersContext):
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
            elif isinstance(child, DNPParser.InspectReplacingAllLeadingsContext):
                leading_type = child.getChild(0).getText().upper()
                inspect_replacing_all_leadings_dict = {
                    "leading_type": leading_type,
                    "replacements": [],
                }
                inspect_replacing_phrase_dict["replacements"].append(
                    inspect_replacing_all_leadings_dict
                )

                inspect_replacing_all_leading_list: List[
                    DNPParser.InspectReplacingAllLeadingContext
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
        self, inspect_tallying: DNPParser.InspectTallyingPhraseContext
    ):
        inspect_tallying_phrase_dict = {"tallying": []}
        inspect_for_list: List[DNPParser.InspectForContext] = (
            inspect_tallying.inspectFor()
        )

        for inspect_for in inspect_for_list:
            inspect_for_dict = self.extract_inspect_for(inspect_for)
            inspect_tallying_phrase_dict["tallying"].append(inspect_for_dict)

        return inspect_tallying_phrase_dict

    def extract_inspect_for(self, inspect_for: DNPParser.InspectForContext):
        identifier = inspect_for.identifier()
        inspect_for_dict = {
            "identifier": identifier.getText(),
            "for_targets": [],
        }

        for child in inspect_for.getChildren():
            if isinstance(child, DNPParser.InspectCharactersContext):
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
            elif isinstance(child, DNPParser.InspectAllLeadingsContext):
                leading_type = child.getChild(0).getText().upper()
                inspect_all_leadings_dict = {
                    "leading_type": leading_type,
                    "inspect_all_leading": [],
                }
                inspect_for_dict["for_targets"].append(inspect_all_leadings_dict)

                inspect_all_leading_list: List[DNPParser.InspectAllLeadingContext] = (
                    child.inspectAllLeading()
                )

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
        self, inspect_before_after: DNPParser.InspectBeforeAfterContext
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

    def assessMoveStatement(self, ctx: DNPParser.MoveStatementContext):
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

        move_to_statement: Optional[DNPParser.MoveToStatementContext] = (
            ctx.moveToStatement()
        )

        if move_to_statement:
            res["move_type"] = "TO"

            move_to_sending_area: DNPParser.MoveToSendingAreaContext = (
                move_to_statement.moveToSendingArea()
            )
            res["move_from"] = get_original_code_content(
                self.parser,
                move_to_sending_area.start.tokenIndex,
                move_to_sending_area.stop.tokenIndex,
            )

            move_to_sending_area_child = move_to_sending_area.getChild(0)
            if isinstance(move_to_sending_area_child, DNPParser.IdentifierContext):
                res["from_identifier"] = move_to_sending_area_child.getText()
            elif isinstance(
                move_to_sending_area_child, DNPParser.MoveAttributeClauseContext
            ):
                cobol_word = move_to_sending_area_child.cobolWord(1)
                if isinstance(cobol_word.getChild(0), DNPParser.CharDataKeywordContext):
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

        elif isinstance(
            move_to_statement, DNPParser.MoveCorrespondingToStatementContext
        ):
            res["move_type"] = "CORRESPONDING"
            res["from_identifier"] = (
                move_to_statement.moveCorrespondingToSendingArea.getText()
            )
            res["move_from"] = (
                move_to_statement.moveCorrespondingToSendingArea.getText()
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

        return res

    def visitMoveStatement(self, ctx: DNPParser.MoveStatementContext):
        res = self.assessMoveStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessPerformStatement(self, ctx: DNPParser.PerformStatementContext):
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
                ctx, DNPParser.PerformTimesContext
            )

            perform_until = recursive_find_first_child_by_type(
                ctx, DNPParser.PerformUntilContext
            )

            perform_varying = recursive_find_first_child_by_type(
                ctx, DNPParser.PerformVaryingContext
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
                    DNPParser.ConditionContext,
                )
                res["condition"] = get_original_code_content(
                    self.parser,
                    condition.start.tokenIndex,
                    condition.stop.tokenIndex,
                )
                sub_tags.append("UNTIL")

            if perform_varying:
                perform_varying_clause = recursive_find_first_child_by_type(
                    perform_varying, DNPParser.PerformVaryingClauseContext
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
                performInlineStatement, DNPParser.PerformTimesContext
            )

            perform_until = recursive_find_first_child_by_type(
                performInlineStatement, DNPParser.PerformUntilContext
            )

            perform_varying = recursive_find_first_child_by_type(
                performInlineStatement, DNPParser.PerformVaryingContext
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
                    DNPParser.ConditionContext,
                )
                res["condition"] = get_original_code_content(
                    self.parser,
                    condition.start.tokenIndex,
                    condition.stop.tokenIndex,
                )
                sub_tags.append("UNTIL")

            if perform_varying:
                perform_varying_clause = recursive_find_first_child_by_type(
                    perform_varying, DNPParser.PerformVaryingClauseContext
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

    def visitPerformStatement(self, ctx: DNPParser.PerformStatementContext):
        res = self.assessPerformStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessReadStatement(self, ctx: DNPParser.ReadStatementContext):
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

    def visitReadStatement(self, ctx: DNPParser.ReadStatementContext):
        res = self.assessReadStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessRewriteStatement(self, ctx: DNPParser.RewriteStatementContext):
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

    def visitRewriteStatement(self, ctx: DNPParser.RewriteStatementContext):
        res = self.assessRewriteStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessStringStatement(self, ctx: DNPParser.StringStatementContext):
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

        string_sending_phrase_list: List[DNPParser.StringSendingPhraseContext] = (
            ctx.stringSendingPhrase()
        )

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

            string_sending_list: List[DNPParser.StringSendingContext] = (
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
                DNPParser.StringDelimitedByPhraseContext
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

            string_for_phrase: Optional[DNPParser.StringForPhraseContext] = (
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

        string_into_phrase: DNPParser.StringIntoPhraseContext = ctx.stringIntoPhrase()

        into_identifier = string_into_phrase.identifier()
        res["destination_identifier"] = into_identifier.getText()

        string_pointer_phrase: Optional[DNPParser.StringWithPointerPhraseContext] = (
            ctx.stringWithPointerPhrase()
        )

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

    def visitStringStatement(self, ctx: DNPParser.StringStatementContext):
        res = self.assessStringStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessSubtractStatement(self, ctx: DNPParser.SubtractStatementContext):
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

        if isinstance(subtract_phrase, DNPParser.SubtractFromStatementContext):

            subtract_from_statement = subtract_phrase
            subtrahend_list = subtract_from_statement.subtractSubtrahend()

            for subtrahend in subtrahend_list:
                subtrahend = subtrahend.getChild(0)
                if isinstance(subtrahend, DNPParser.IdentifierContext):
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

        elif isinstance(subtract_phrase, DNPParser.SubtractFromGivingStatementContext):
            subtract_from_statement = subtract_phrase
            subtrahend_list = subtract_from_statement.subtractSubtrahend()

            for subtrahend in subtrahend_list:
                subtrahend = subtrahend.getChild(0)
                if isinstance(subtrahend, DNPParser.IdentifierContext):
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
            subtract_phrase, DNPParser.SubtractCorrespondingStatementContext
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

    def visitSubtractStatement(self, ctx: DNPParser.SubtractStatementContext):
        res = self.assessSubtractStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessSetStatement(self, ctx: DNPParser.SetStatementContext):
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
        if DNPParser.SetToStatementContext in children:
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
                    setToValue: DNPParser.SetToValueContext = setToValue[0]
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
            set_up_down_by_statement: DNPParser.SetUpDownByStatementContext = (
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

            set_by_value: DNPParser.SetByValueContext = (
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

    def visitSetStatement(self, ctx: DNPParser.SetStatementContext):
        res = self.assessSetStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def assessOpenStatement(self, ctx: DNPParser.OpenStatementContext):
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
            if isinstance(child, DNPParser.OpenInputStatementContext):
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

            elif isinstance(child, DNPParser.OpenOutputStatementContext):
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

            elif isinstance(child, DNPParser.OpenIOStatementContext):
                file_names = child.fileName()
                for file_name in file_names:
                    res["open_files"].append(
                        {
                            "file_name": file_name.getText(),
                            "open_type": "IO",
                            "on_exception_clause": [],
                        }
                    )
            elif isinstance(child, DNPParser.OpenInquiryContext):
                file_name = child.qualifiedDataName()
                on_exception_statements = []
                on_exception_clause = child.onExceptionClause()
                if on_exception_clause:
                    statements = on_exception_clause.statement()
                    for statement in statements:
                        child = statement.getChild(0)
                        type_ = type(child).__name__
                        if type_ in self.func:
                            f = self.func[type_]
                            on_exception_statements.append(f(child))

                res["open_files"].append(
                    {
                        "file_name": file_name.getText(),
                        "open_type": "INQUIRY",
                        "on_exception_clause": on_exception_statements,
                    }
                )

            elif isinstance(child, DNPParser.OpenExtendStatementContext):
                file_names = child.fileName()
                for file_name in file_names:
                    res["open_files"].append(
                        {
                            "file_name": file_name.getText(),
                            "open_type": "EXTEND",
                            "on_exception_clause": [],
                        }
                    )

            elif isinstance(child, DNPParser.OpenUpdateStatementContext):
                file_name = child.qualifiedDataName()

                on_exception_clause = child.onExceptionClause()
                on_exception_statements = []
                if on_exception_clause:
                    statements = on_exception_clause.statement()
                    for statement in statements:
                        child = statement.getChild(0)
                        type_ = type(child).__name__
                        if type_ in self.func:
                            f = self.func[type_]
                            on_exception_statements.append(f(child))

                res["open_files"].append(
                    {
                        "file_name": file_name.getText(),
                        "open_type": "UPDATE",
                        "on_exception_clause": on_exception_statements,
                    }
                )

        return res

    def visitOpenStatement(self, ctx: DNPParser.OpenStatementContext):
        res = self.assessOpenStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, DNPParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)
