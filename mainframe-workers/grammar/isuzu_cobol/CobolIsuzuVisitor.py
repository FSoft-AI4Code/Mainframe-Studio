# Generated from grammar/isuzu_cobol/CobolIsuzu.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CobolIsuzuParser import CobolIsuzuParser
else:
    from CobolIsuzuParser import CobolIsuzuParser

# This class defines a complete generic visitor for a parse tree produced by CobolIsuzuParser.

class CobolIsuzuVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CobolIsuzuParser#startRule.
    def visitStartRule(self, ctx:CobolIsuzuParser.StartRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#compilationUnit.
    def visitCompilationUnit(self, ctx:CobolIsuzuParser.CompilationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#programUnit.
    def visitProgramUnit(self, ctx:CobolIsuzuParser.ProgramUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#endProgramStatement.
    def visitEndProgramStatement(self, ctx:CobolIsuzuParser.EndProgramStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#identificationDivision.
    def visitIdentificationDivision(self, ctx:CobolIsuzuParser.IdentificationDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#identificationDivisionBody.
    def visitIdentificationDivisionBody(self, ctx:CobolIsuzuParser.IdentificationDivisionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#programIdParagraph.
    def visitProgramIdParagraph(self, ctx:CobolIsuzuParser.ProgramIdParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#author_name.
    def visitAuthor_name(self, ctx:CobolIsuzuParser.Author_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#authorParagraph.
    def visitAuthorParagraph(self, ctx:CobolIsuzuParser.AuthorParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#installationParagraph.
    def visitInstallationParagraph(self, ctx:CobolIsuzuParser.InstallationParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dateWrittenParagraph.
    def visitDateWrittenParagraph(self, ctx:CobolIsuzuParser.DateWrittenParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dateCompiledParagraph.
    def visitDateCompiledParagraph(self, ctx:CobolIsuzuParser.DateCompiledParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#securityParagraph.
    def visitSecurityParagraph(self, ctx:CobolIsuzuParser.SecurityParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#remarksParagraph.
    def visitRemarksParagraph(self, ctx:CobolIsuzuParser.RemarksParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#environmentDivision.
    def visitEnvironmentDivision(self, ctx:CobolIsuzuParser.EnvironmentDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#environmentDivisionBody.
    def visitEnvironmentDivisionBody(self, ctx:CobolIsuzuParser.EnvironmentDivisionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#configurationSection.
    def visitConfigurationSection(self, ctx:CobolIsuzuParser.ConfigurationSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#configurationSectionParagraph.
    def visitConfigurationSectionParagraph(self, ctx:CobolIsuzuParser.ConfigurationSectionParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#subSchemaParagraph.
    def visitSubSchemaParagraph(self, ctx:CobolIsuzuParser.SubSchemaParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#sourceComputerParagraph.
    def visitSourceComputerParagraph(self, ctx:CobolIsuzuParser.SourceComputerParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#objectComputerParagraph.
    def visitObjectComputerParagraph(self, ctx:CobolIsuzuParser.ObjectComputerParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#objectComputerClause.
    def visitObjectComputerClause(self, ctx:CobolIsuzuParser.ObjectComputerClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#memorySizeClause.
    def visitMemorySizeClause(self, ctx:CobolIsuzuParser.MemorySizeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#diskSizeClause.
    def visitDiskSizeClause(self, ctx:CobolIsuzuParser.DiskSizeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#collatingSequenceClause.
    def visitCollatingSequenceClause(self, ctx:CobolIsuzuParser.CollatingSequenceClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#collatingSequenceClauseAlphanumeric.
    def visitCollatingSequenceClauseAlphanumeric(self, ctx:CobolIsuzuParser.CollatingSequenceClauseAlphanumericContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#collatingSequenceClauseNational.
    def visitCollatingSequenceClauseNational(self, ctx:CobolIsuzuParser.CollatingSequenceClauseNationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#segmentLimitClause.
    def visitSegmentLimitClause(self, ctx:CobolIsuzuParser.SegmentLimitClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#characterSetClause.
    def visitCharacterSetClause(self, ctx:CobolIsuzuParser.CharacterSetClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#specialNamesParagraph.
    def visitSpecialNamesParagraph(self, ctx:CobolIsuzuParser.SpecialNamesParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#specialNameClause.
    def visitSpecialNameClause(self, ctx:CobolIsuzuParser.SpecialNameClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#alphabetClause.
    def visitAlphabetClause(self, ctx:CobolIsuzuParser.AlphabetClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#alphabetClauseFormat1.
    def visitAlphabetClauseFormat1(self, ctx:CobolIsuzuParser.AlphabetClauseFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#alphabetLiterals.
    def visitAlphabetLiterals(self, ctx:CobolIsuzuParser.AlphabetLiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#alphabetThrough.
    def visitAlphabetThrough(self, ctx:CobolIsuzuParser.AlphabetThroughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#alphabetAlso.
    def visitAlphabetAlso(self, ctx:CobolIsuzuParser.AlphabetAlsoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#alphabetClauseFormat2.
    def visitAlphabetClauseFormat2(self, ctx:CobolIsuzuParser.AlphabetClauseFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#channelClause.
    def visitChannelClause(self, ctx:CobolIsuzuParser.ChannelClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#classClause.
    def visitClassClause(self, ctx:CobolIsuzuParser.ClassClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#classClauseThrough.
    def visitClassClauseThrough(self, ctx:CobolIsuzuParser.ClassClauseThroughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#classClauseFrom.
    def visitClassClauseFrom(self, ctx:CobolIsuzuParser.ClassClauseFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#classClauseTo.
    def visitClassClauseTo(self, ctx:CobolIsuzuParser.ClassClauseToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#currencySignClause.
    def visitCurrencySignClause(self, ctx:CobolIsuzuParser.CurrencySignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#decimalPointClause.
    def visitDecimalPointClause(self, ctx:CobolIsuzuParser.DecimalPointClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#defaultComputationalSignClause.
    def visitDefaultComputationalSignClause(self, ctx:CobolIsuzuParser.DefaultComputationalSignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#defaultDisplaySignClause.
    def visitDefaultDisplaySignClause(self, ctx:CobolIsuzuParser.DefaultDisplaySignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#environmentSwitchNameClause.
    def visitEnvironmentSwitchNameClause(self, ctx:CobolIsuzuParser.EnvironmentSwitchNameClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#environmentSwitchNameSpecialNamesStatusPhrase.
    def visitEnvironmentSwitchNameSpecialNamesStatusPhrase(self, ctx:CobolIsuzuParser.EnvironmentSwitchNameSpecialNamesStatusPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#odtClause.
    def visitOdtClause(self, ctx:CobolIsuzuParser.OdtClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reserveNetworkClause.
    def visitReserveNetworkClause(self, ctx:CobolIsuzuParser.ReserveNetworkClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#symbolicCharactersClause.
    def visitSymbolicCharactersClause(self, ctx:CobolIsuzuParser.SymbolicCharactersClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#symbolicCharacters.
    def visitSymbolicCharacters(self, ctx:CobolIsuzuParser.SymbolicCharactersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#inputOutputSection.
    def visitInputOutputSection(self, ctx:CobolIsuzuParser.InputOutputSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#inputOutputSectionParagraph.
    def visitInputOutputSectionParagraph(self, ctx:CobolIsuzuParser.InputOutputSectionParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#fileControlParagraph.
    def visitFileControlParagraph(self, ctx:CobolIsuzuParser.FileControlParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#fileControlEntry.
    def visitFileControlEntry(self, ctx:CobolIsuzuParser.FileControlEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#selectClause.
    def visitSelectClause(self, ctx:CobolIsuzuParser.SelectClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#fileControlClause.
    def visitFileControlClause(self, ctx:CobolIsuzuParser.FileControlClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#selectedFunctionClause.
    def visitSelectedFunctionClause(self, ctx:CobolIsuzuParser.SelectedFunctionClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#assignClause.
    def visitAssignClause(self, ctx:CobolIsuzuParser.AssignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reserveClause.
    def visitReserveClause(self, ctx:CobolIsuzuParser.ReserveClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#organizationClause.
    def visitOrganizationClause(self, ctx:CobolIsuzuParser.OrganizationClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#destinationClause.
    def visitDestinationClause(self, ctx:CobolIsuzuParser.DestinationClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#formatClause.
    def visitFormatClause(self, ctx:CobolIsuzuParser.FormatClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#messageModeClause.
    def visitMessageModeClause(self, ctx:CobolIsuzuParser.MessageModeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#paddingCharacterClause.
    def visitPaddingCharacterClause(self, ctx:CobolIsuzuParser.PaddingCharacterClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#recordDelimiterClause.
    def visitRecordDelimiterClause(self, ctx:CobolIsuzuParser.RecordDelimiterClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#accessModeClause.
    def visitAccessModeClause(self, ctx:CobolIsuzuParser.AccessModeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#recordKeyClause.
    def visitRecordKeyClause(self, ctx:CobolIsuzuParser.RecordKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#alternateRecordKeyClause.
    def visitAlternateRecordKeyClause(self, ctx:CobolIsuzuParser.AlternateRecordKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#passwordClause.
    def visitPasswordClause(self, ctx:CobolIsuzuParser.PasswordClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#fileStatusClause.
    def visitFileStatusClause(self, ctx:CobolIsuzuParser.FileStatusClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#relativeKeyClause.
    def visitRelativeKeyClause(self, ctx:CobolIsuzuParser.RelativeKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#sessionControlClause.
    def visitSessionControlClause(self, ctx:CobolIsuzuParser.SessionControlClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#ioControlParagraph.
    def visitIoControlParagraph(self, ctx:CobolIsuzuParser.IoControlParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#ioControlClause.
    def visitIoControlClause(self, ctx:CobolIsuzuParser.IoControlClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#applyClause.
    def visitApplyClause(self, ctx:CobolIsuzuParser.ApplyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#rerunClause.
    def visitRerunClause(self, ctx:CobolIsuzuParser.RerunClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#rerunEveryRecords.
    def visitRerunEveryRecords(self, ctx:CobolIsuzuParser.RerunEveryRecordsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#rerunEveryOf.
    def visitRerunEveryOf(self, ctx:CobolIsuzuParser.RerunEveryOfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#rerunEveryClock.
    def visitRerunEveryClock(self, ctx:CobolIsuzuParser.RerunEveryClockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#sameClause.
    def visitSameClause(self, ctx:CobolIsuzuParser.SameClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#multipleFileClause.
    def visitMultipleFileClause(self, ctx:CobolIsuzuParser.MultipleFileClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#multipleFilePosition.
    def visitMultipleFilePosition(self, ctx:CobolIsuzuParser.MultipleFilePositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#commitmentControlClause.
    def visitCommitmentControlClause(self, ctx:CobolIsuzuParser.CommitmentControlClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataDivision.
    def visitDataDivision(self, ctx:CobolIsuzuParser.DataDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataDivisionSection.
    def visitDataDivisionSection(self, ctx:CobolIsuzuParser.DataDivisionSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#fileSection.
    def visitFileSection(self, ctx:CobolIsuzuParser.FileSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#fileDescriptionEntry.
    def visitFileDescriptionEntry(self, ctx:CobolIsuzuParser.FileDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#fileDescriptionEntryClause.
    def visitFileDescriptionEntryClause(self, ctx:CobolIsuzuParser.FileDescriptionEntryClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#externalClause.
    def visitExternalClause(self, ctx:CobolIsuzuParser.ExternalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#globalClause.
    def visitGlobalClause(self, ctx:CobolIsuzuParser.GlobalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#blockContainsClause.
    def visitBlockContainsClause(self, ctx:CobolIsuzuParser.BlockContainsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#blockContainsTo.
    def visitBlockContainsTo(self, ctx:CobolIsuzuParser.BlockContainsToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#recordContainsClause.
    def visitRecordContainsClause(self, ctx:CobolIsuzuParser.RecordContainsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#recordContainsClauseFormat1.
    def visitRecordContainsClauseFormat1(self, ctx:CobolIsuzuParser.RecordContainsClauseFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#recordContainsClauseFormat2.
    def visitRecordContainsClauseFormat2(self, ctx:CobolIsuzuParser.RecordContainsClauseFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#recordContainsClauseFormat3.
    def visitRecordContainsClauseFormat3(self, ctx:CobolIsuzuParser.RecordContainsClauseFormat3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#recordContainsTo.
    def visitRecordContainsTo(self, ctx:CobolIsuzuParser.RecordContainsToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#labelRecordsClause.
    def visitLabelRecordsClause(self, ctx:CobolIsuzuParser.LabelRecordsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#valueOfClause.
    def visitValueOfClause(self, ctx:CobolIsuzuParser.ValueOfClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#valuePair.
    def visitValuePair(self, ctx:CobolIsuzuParser.ValuePairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataRecordsClause.
    def visitDataRecordsClause(self, ctx:CobolIsuzuParser.DataRecordsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#linageClause.
    def visitLinageClause(self, ctx:CobolIsuzuParser.LinageClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#linageAt.
    def visitLinageAt(self, ctx:CobolIsuzuParser.LinageAtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#linageFootingAt.
    def visitLinageFootingAt(self, ctx:CobolIsuzuParser.LinageFootingAtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#linageLinesAtTop.
    def visitLinageLinesAtTop(self, ctx:CobolIsuzuParser.LinageLinesAtTopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#linageLinesAtBottom.
    def visitLinageLinesAtBottom(self, ctx:CobolIsuzuParser.LinageLinesAtBottomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#recordingModeClause.
    def visitRecordingModeClause(self, ctx:CobolIsuzuParser.RecordingModeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#modeStatement.
    def visitModeStatement(self, ctx:CobolIsuzuParser.ModeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#codeSetClause.
    def visitCodeSetClause(self, ctx:CobolIsuzuParser.CodeSetClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportClause.
    def visitReportClause(self, ctx:CobolIsuzuParser.ReportClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataBaseSection.
    def visitDataBaseSection(self, ctx:CobolIsuzuParser.DataBaseSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataBaseSectionEntry.
    def visitDataBaseSectionEntry(self, ctx:CobolIsuzuParser.DataBaseSectionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#workingStorageSection.
    def visitWorkingStorageSection(self, ctx:CobolIsuzuParser.WorkingStorageSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#constantSection.
    def visitConstantSection(self, ctx:CobolIsuzuParser.ConstantSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#linkageSection.
    def visitLinkageSection(self, ctx:CobolIsuzuParser.LinkageSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#communicationSection.
    def visitCommunicationSection(self, ctx:CobolIsuzuParser.CommunicationSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#communicationDescriptionEntry.
    def visitCommunicationDescriptionEntry(self, ctx:CobolIsuzuParser.CommunicationDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#communicationDescriptionEntryFormat1.
    def visitCommunicationDescriptionEntryFormat1(self, ctx:CobolIsuzuParser.CommunicationDescriptionEntryFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#communicationDescriptionEntryFormat2.
    def visitCommunicationDescriptionEntryFormat2(self, ctx:CobolIsuzuParser.CommunicationDescriptionEntryFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#communicationDescriptionEntryFormat3.
    def visitCommunicationDescriptionEntryFormat3(self, ctx:CobolIsuzuParser.CommunicationDescriptionEntryFormat3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#destinationCountClause.
    def visitDestinationCountClause(self, ctx:CobolIsuzuParser.DestinationCountClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#destinationTableClause.
    def visitDestinationTableClause(self, ctx:CobolIsuzuParser.DestinationTableClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#endKeyClause.
    def visitEndKeyClause(self, ctx:CobolIsuzuParser.EndKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#errorKeyClause.
    def visitErrorKeyClause(self, ctx:CobolIsuzuParser.ErrorKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#messageCountClause.
    def visitMessageCountClause(self, ctx:CobolIsuzuParser.MessageCountClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#messageDateClause.
    def visitMessageDateClause(self, ctx:CobolIsuzuParser.MessageDateClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#messageTimeClause.
    def visitMessageTimeClause(self, ctx:CobolIsuzuParser.MessageTimeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#statusKeyClause.
    def visitStatusKeyClause(self, ctx:CobolIsuzuParser.StatusKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#symbolicDestinationClause.
    def visitSymbolicDestinationClause(self, ctx:CobolIsuzuParser.SymbolicDestinationClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#symbolicQueueClause.
    def visitSymbolicQueueClause(self, ctx:CobolIsuzuParser.SymbolicQueueClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#symbolicSourceClause.
    def visitSymbolicSourceClause(self, ctx:CobolIsuzuParser.SymbolicSourceClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#symbolicTerminalClause.
    def visitSymbolicTerminalClause(self, ctx:CobolIsuzuParser.SymbolicTerminalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#symbolicSubQueueClause.
    def visitSymbolicSubQueueClause(self, ctx:CobolIsuzuParser.SymbolicSubQueueClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#textLengthClause.
    def visitTextLengthClause(self, ctx:CobolIsuzuParser.TextLengthClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#localStorageSection.
    def visitLocalStorageSection(self, ctx:CobolIsuzuParser.LocalStorageSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenSection.
    def visitScreenSection(self, ctx:CobolIsuzuParser.ScreenSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenDescriptionEntry.
    def visitScreenDescriptionEntry(self, ctx:CobolIsuzuParser.ScreenDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenDescriptionBlankClause.
    def visitScreenDescriptionBlankClause(self, ctx:CobolIsuzuParser.ScreenDescriptionBlankClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenDescriptionBellClause.
    def visitScreenDescriptionBellClause(self, ctx:CobolIsuzuParser.ScreenDescriptionBellClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenDescriptionBlinkClause.
    def visitScreenDescriptionBlinkClause(self, ctx:CobolIsuzuParser.ScreenDescriptionBlinkClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenDescriptionEraseClause.
    def visitScreenDescriptionEraseClause(self, ctx:CobolIsuzuParser.ScreenDescriptionEraseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenDescriptionLightClause.
    def visitScreenDescriptionLightClause(self, ctx:CobolIsuzuParser.ScreenDescriptionLightClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenDescriptionGridClause.
    def visitScreenDescriptionGridClause(self, ctx:CobolIsuzuParser.ScreenDescriptionGridClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenDescriptionReverseVideoClause.
    def visitScreenDescriptionReverseVideoClause(self, ctx:CobolIsuzuParser.ScreenDescriptionReverseVideoClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenDescriptionUnderlineClause.
    def visitScreenDescriptionUnderlineClause(self, ctx:CobolIsuzuParser.ScreenDescriptionUnderlineClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenDescriptionSizeClause.
    def visitScreenDescriptionSizeClause(self, ctx:CobolIsuzuParser.ScreenDescriptionSizeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenDescriptionLineClause.
    def visitScreenDescriptionLineClause(self, ctx:CobolIsuzuParser.ScreenDescriptionLineClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenDescriptionColumnClause.
    def visitScreenDescriptionColumnClause(self, ctx:CobolIsuzuParser.ScreenDescriptionColumnClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenDescriptionForegroundColorClause.
    def visitScreenDescriptionForegroundColorClause(self, ctx:CobolIsuzuParser.ScreenDescriptionForegroundColorClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenDescriptionBackgroundColorClause.
    def visitScreenDescriptionBackgroundColorClause(self, ctx:CobolIsuzuParser.ScreenDescriptionBackgroundColorClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenDescriptionControlClause.
    def visitScreenDescriptionControlClause(self, ctx:CobolIsuzuParser.ScreenDescriptionControlClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenDescriptionValueClause.
    def visitScreenDescriptionValueClause(self, ctx:CobolIsuzuParser.ScreenDescriptionValueClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenDescriptionPictureClause.
    def visitScreenDescriptionPictureClause(self, ctx:CobolIsuzuParser.ScreenDescriptionPictureClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenDescriptionFromClause.
    def visitScreenDescriptionFromClause(self, ctx:CobolIsuzuParser.ScreenDescriptionFromClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenDescriptionToClause.
    def visitScreenDescriptionToClause(self, ctx:CobolIsuzuParser.ScreenDescriptionToClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenDescriptionUsingClause.
    def visitScreenDescriptionUsingClause(self, ctx:CobolIsuzuParser.ScreenDescriptionUsingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenDescriptionUsageClause.
    def visitScreenDescriptionUsageClause(self, ctx:CobolIsuzuParser.ScreenDescriptionUsageClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenDescriptionBlankWhenZeroClause.
    def visitScreenDescriptionBlankWhenZeroClause(self, ctx:CobolIsuzuParser.ScreenDescriptionBlankWhenZeroClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenDescriptionJustifiedClause.
    def visitScreenDescriptionJustifiedClause(self, ctx:CobolIsuzuParser.ScreenDescriptionJustifiedClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenDescriptionSignClause.
    def visitScreenDescriptionSignClause(self, ctx:CobolIsuzuParser.ScreenDescriptionSignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenDescriptionAutoClause.
    def visitScreenDescriptionAutoClause(self, ctx:CobolIsuzuParser.ScreenDescriptionAutoClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenDescriptionSecureClause.
    def visitScreenDescriptionSecureClause(self, ctx:CobolIsuzuParser.ScreenDescriptionSecureClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenDescriptionRequiredClause.
    def visitScreenDescriptionRequiredClause(self, ctx:CobolIsuzuParser.ScreenDescriptionRequiredClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenDescriptionPromptClause.
    def visitScreenDescriptionPromptClause(self, ctx:CobolIsuzuParser.ScreenDescriptionPromptClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenDescriptionPromptOccursClause.
    def visitScreenDescriptionPromptOccursClause(self, ctx:CobolIsuzuParser.ScreenDescriptionPromptOccursClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenDescriptionFullClause.
    def visitScreenDescriptionFullClause(self, ctx:CobolIsuzuParser.ScreenDescriptionFullClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenDescriptionZeroFillClause.
    def visitScreenDescriptionZeroFillClause(self, ctx:CobolIsuzuParser.ScreenDescriptionZeroFillClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportSection.
    def visitReportSection(self, ctx:CobolIsuzuParser.ReportSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportDescription.
    def visitReportDescription(self, ctx:CobolIsuzuParser.ReportDescriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportDescriptionEntry.
    def visitReportDescriptionEntry(self, ctx:CobolIsuzuParser.ReportDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportDescriptionGlobalClause.
    def visitReportDescriptionGlobalClause(self, ctx:CobolIsuzuParser.ReportDescriptionGlobalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportDescriptionPageLimitClause.
    def visitReportDescriptionPageLimitClause(self, ctx:CobolIsuzuParser.ReportDescriptionPageLimitClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportDescriptionHeadingClause.
    def visitReportDescriptionHeadingClause(self, ctx:CobolIsuzuParser.ReportDescriptionHeadingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportDescriptionFirstDetailClause.
    def visitReportDescriptionFirstDetailClause(self, ctx:CobolIsuzuParser.ReportDescriptionFirstDetailClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportDescriptionLastDetailClause.
    def visitReportDescriptionLastDetailClause(self, ctx:CobolIsuzuParser.ReportDescriptionLastDetailClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportDescriptionFootingClause.
    def visitReportDescriptionFootingClause(self, ctx:CobolIsuzuParser.ReportDescriptionFootingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportGroupDescriptionEntry.
    def visitReportGroupDescriptionEntry(self, ctx:CobolIsuzuParser.ReportGroupDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportGroupDescriptionEntryFormat1.
    def visitReportGroupDescriptionEntryFormat1(self, ctx:CobolIsuzuParser.ReportGroupDescriptionEntryFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportGroupDescriptionEntryFormat2.
    def visitReportGroupDescriptionEntryFormat2(self, ctx:CobolIsuzuParser.ReportGroupDescriptionEntryFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportGroupDescriptionEntryFormat3.
    def visitReportGroupDescriptionEntryFormat3(self, ctx:CobolIsuzuParser.ReportGroupDescriptionEntryFormat3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportGroupBlankWhenZeroClause.
    def visitReportGroupBlankWhenZeroClause(self, ctx:CobolIsuzuParser.ReportGroupBlankWhenZeroClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportGroupColumnNumberClause.
    def visitReportGroupColumnNumberClause(self, ctx:CobolIsuzuParser.ReportGroupColumnNumberClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportGroupIndicateClause.
    def visitReportGroupIndicateClause(self, ctx:CobolIsuzuParser.ReportGroupIndicateClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportGroupJustifiedClause.
    def visitReportGroupJustifiedClause(self, ctx:CobolIsuzuParser.ReportGroupJustifiedClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportGroupLineNumberClause.
    def visitReportGroupLineNumberClause(self, ctx:CobolIsuzuParser.ReportGroupLineNumberClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportGroupLineNumberNextPage.
    def visitReportGroupLineNumberNextPage(self, ctx:CobolIsuzuParser.ReportGroupLineNumberNextPageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportGroupLineNumberPlus.
    def visitReportGroupLineNumberPlus(self, ctx:CobolIsuzuParser.ReportGroupLineNumberPlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportGroupNextGroupClause.
    def visitReportGroupNextGroupClause(self, ctx:CobolIsuzuParser.ReportGroupNextGroupClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportGroupNextGroupPlus.
    def visitReportGroupNextGroupPlus(self, ctx:CobolIsuzuParser.ReportGroupNextGroupPlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportGroupNextGroupNextPage.
    def visitReportGroupNextGroupNextPage(self, ctx:CobolIsuzuParser.ReportGroupNextGroupNextPageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportGroupPictureClause.
    def visitReportGroupPictureClause(self, ctx:CobolIsuzuParser.ReportGroupPictureClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportGroupResetClause.
    def visitReportGroupResetClause(self, ctx:CobolIsuzuParser.ReportGroupResetClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportGroupSignClause.
    def visitReportGroupSignClause(self, ctx:CobolIsuzuParser.ReportGroupSignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportGroupSourceClause.
    def visitReportGroupSourceClause(self, ctx:CobolIsuzuParser.ReportGroupSourceClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportGroupSumClause.
    def visitReportGroupSumClause(self, ctx:CobolIsuzuParser.ReportGroupSumClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportGroupTypeClause.
    def visitReportGroupTypeClause(self, ctx:CobolIsuzuParser.ReportGroupTypeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportGroupTypeReportHeading.
    def visitReportGroupTypeReportHeading(self, ctx:CobolIsuzuParser.ReportGroupTypeReportHeadingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportGroupTypePageHeading.
    def visitReportGroupTypePageHeading(self, ctx:CobolIsuzuParser.ReportGroupTypePageHeadingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportGroupTypeControlHeading.
    def visitReportGroupTypeControlHeading(self, ctx:CobolIsuzuParser.ReportGroupTypeControlHeadingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportGroupTypeDetail.
    def visitReportGroupTypeDetail(self, ctx:CobolIsuzuParser.ReportGroupTypeDetailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportGroupTypeControlFooting.
    def visitReportGroupTypeControlFooting(self, ctx:CobolIsuzuParser.ReportGroupTypeControlFootingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportGroupUsageClause.
    def visitReportGroupUsageClause(self, ctx:CobolIsuzuParser.ReportGroupUsageClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportGroupTypePageFooting.
    def visitReportGroupTypePageFooting(self, ctx:CobolIsuzuParser.ReportGroupTypePageFootingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportGroupTypeReportFooting.
    def visitReportGroupTypeReportFooting(self, ctx:CobolIsuzuParser.ReportGroupTypeReportFootingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportGroupValueClause.
    def visitReportGroupValueClause(self, ctx:CobolIsuzuParser.ReportGroupValueClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#programLibrarySection.
    def visitProgramLibrarySection(self, ctx:CobolIsuzuParser.ProgramLibrarySectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#libraryDescriptionEntry.
    def visitLibraryDescriptionEntry(self, ctx:CobolIsuzuParser.LibraryDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#libraryDescriptionEntryFormat1.
    def visitLibraryDescriptionEntryFormat1(self, ctx:CobolIsuzuParser.LibraryDescriptionEntryFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#libraryDescriptionEntryFormat2.
    def visitLibraryDescriptionEntryFormat2(self, ctx:CobolIsuzuParser.LibraryDescriptionEntryFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#libraryAttributeClauseFormat1.
    def visitLibraryAttributeClauseFormat1(self, ctx:CobolIsuzuParser.LibraryAttributeClauseFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#libraryAttributeClauseFormat2.
    def visitLibraryAttributeClauseFormat2(self, ctx:CobolIsuzuParser.LibraryAttributeClauseFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#libraryAttributeFunction.
    def visitLibraryAttributeFunction(self, ctx:CobolIsuzuParser.LibraryAttributeFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#libraryAttributeParameter.
    def visitLibraryAttributeParameter(self, ctx:CobolIsuzuParser.LibraryAttributeParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#libraryAttributeTitle.
    def visitLibraryAttributeTitle(self, ctx:CobolIsuzuParser.LibraryAttributeTitleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#libraryEntryProcedureClauseFormat1.
    def visitLibraryEntryProcedureClauseFormat1(self, ctx:CobolIsuzuParser.LibraryEntryProcedureClauseFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#libraryEntryProcedureClauseFormat2.
    def visitLibraryEntryProcedureClauseFormat2(self, ctx:CobolIsuzuParser.LibraryEntryProcedureClauseFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#libraryEntryProcedureForClause.
    def visitLibraryEntryProcedureForClause(self, ctx:CobolIsuzuParser.LibraryEntryProcedureForClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#libraryEntryProcedureGivingClause.
    def visitLibraryEntryProcedureGivingClause(self, ctx:CobolIsuzuParser.LibraryEntryProcedureGivingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#libraryEntryProcedureUsingClause.
    def visitLibraryEntryProcedureUsingClause(self, ctx:CobolIsuzuParser.LibraryEntryProcedureUsingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#libraryEntryProcedureUsingName.
    def visitLibraryEntryProcedureUsingName(self, ctx:CobolIsuzuParser.LibraryEntryProcedureUsingNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#libraryEntryProcedureWithClause.
    def visitLibraryEntryProcedureWithClause(self, ctx:CobolIsuzuParser.LibraryEntryProcedureWithClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#libraryEntryProcedureWithName.
    def visitLibraryEntryProcedureWithName(self, ctx:CobolIsuzuParser.LibraryEntryProcedureWithNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#libraryIsCommonClause.
    def visitLibraryIsCommonClause(self, ctx:CobolIsuzuParser.LibraryIsCommonClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#libraryIsGlobalClause.
    def visitLibraryIsGlobalClause(self, ctx:CobolIsuzuParser.LibraryIsGlobalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataDescriptionEntry.
    def visitDataDescriptionEntry(self, ctx:CobolIsuzuParser.DataDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#copyStatement.
    def visitCopyStatement(self, ctx:CobolIsuzuParser.CopyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#disjoinPhrase.
    def visitDisjoinPhrase(self, ctx:CobolIsuzuParser.DisjoinPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#joinPhrase.
    def visitJoinPhrase(self, ctx:CobolIsuzuParser.JoinPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#copySource.
    def visitCopySource(self, ctx:CobolIsuzuParser.CopySourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#copyLibrary.
    def visitCopyLibrary(self, ctx:CobolIsuzuParser.CopyLibraryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#replacingPhrase.
    def visitReplacingPhrase(self, ctx:CobolIsuzuParser.ReplacingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#replaceArea.
    def visitReplaceArea(self, ctx:CobolIsuzuParser.ReplaceAreaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#replaceByStatement.
    def visitReplaceByStatement(self, ctx:CobolIsuzuParser.ReplaceByStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#replaceOffStatement.
    def visitReplaceOffStatement(self, ctx:CobolIsuzuParser.ReplaceOffStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#replaceClause.
    def visitReplaceClause(self, ctx:CobolIsuzuParser.ReplaceClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#directoryPhrase.
    def visitDirectoryPhrase(self, ctx:CobolIsuzuParser.DirectoryPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#familyPhrase.
    def visitFamilyPhrase(self, ctx:CobolIsuzuParser.FamilyPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#replaceable.
    def visitReplaceable(self, ctx:CobolIsuzuParser.ReplaceableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#replacement.
    def visitReplacement(self, ctx:CobolIsuzuParser.ReplacementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#ejectStatement.
    def visitEjectStatement(self, ctx:CobolIsuzuParser.EjectStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#skipStatement.
    def visitSkipStatement(self, ctx:CobolIsuzuParser.SkipStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#titleStatement.
    def visitTitleStatement(self, ctx:CobolIsuzuParser.TitleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#pseudoText.
    def visitPseudoText(self, ctx:CobolIsuzuParser.PseudoTextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#charData.
    def visitCharData(self, ctx:CobolIsuzuParser.CharDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#charDataSql.
    def visitCharDataSql(self, ctx:CobolIsuzuParser.CharDataSqlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#charDataLine.
    def visitCharDataLine(self, ctx:CobolIsuzuParser.CharDataLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#cobolWord.
    def visitCobolWord(self, ctx:CobolIsuzuParser.CobolWordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#literal.
    def visitLiteral(self, ctx:CobolIsuzuParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#jpEncodingText.
    def visitJpEncodingText(self, ctx:CobolIsuzuParser.JpEncodingTextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#filename.
    def visitFilename(self, ctx:CobolIsuzuParser.FilenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataDescriptionEntryFormat1.
    def visitDataDescriptionEntryFormat1(self, ctx:CobolIsuzuParser.DataDescriptionEntryFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataPrintClause.
    def visitDataPrintClause(self, ctx:CobolIsuzuParser.DataPrintClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataCharacterClause.
    def visitDataCharacterClause(self, ctx:CobolIsuzuParser.DataCharacterClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataDescriptionEntryFormat3.
    def visitDataDescriptionEntryFormat3(self, ctx:CobolIsuzuParser.DataDescriptionEntryFormat3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataDescriptionEntryFormat2.
    def visitDataDescriptionEntryFormat2(self, ctx:CobolIsuzuParser.DataDescriptionEntryFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataDescriptionEntryExecSql.
    def visitDataDescriptionEntryExecSql(self, ctx:CobolIsuzuParser.DataDescriptionEntryExecSqlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataAlignedClause.
    def visitDataAlignedClause(self, ctx:CobolIsuzuParser.DataAlignedClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataBlankWhenZeroClause.
    def visitDataBlankWhenZeroClause(self, ctx:CobolIsuzuParser.DataBlankWhenZeroClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataCommonOwnLocalClause.
    def visitDataCommonOwnLocalClause(self, ctx:CobolIsuzuParser.DataCommonOwnLocalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataExternalClause.
    def visitDataExternalClause(self, ctx:CobolIsuzuParser.DataExternalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataGlobalClause.
    def visitDataGlobalClause(self, ctx:CobolIsuzuParser.DataGlobalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataIntegerStringClause.
    def visitDataIntegerStringClause(self, ctx:CobolIsuzuParser.DataIntegerStringClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataJustifiedClause.
    def visitDataJustifiedClause(self, ctx:CobolIsuzuParser.DataJustifiedClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataOccursClause.
    def visitDataOccursClause(self, ctx:CobolIsuzuParser.DataOccursClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataOccursTo.
    def visitDataOccursTo(self, ctx:CobolIsuzuParser.DataOccursToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataOccursSort.
    def visitDataOccursSort(self, ctx:CobolIsuzuParser.DataOccursSortContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataPictureClause.
    def visitDataPictureClause(self, ctx:CobolIsuzuParser.DataPictureClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#pictureString.
    def visitPictureString(self, ctx:CobolIsuzuParser.PictureStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#pictureChars.
    def visitPictureChars(self, ctx:CobolIsuzuParser.PictureCharsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#pictureCardinality.
    def visitPictureCardinality(self, ctx:CobolIsuzuParser.PictureCardinalityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataReceivedByClause.
    def visitDataReceivedByClause(self, ctx:CobolIsuzuParser.DataReceivedByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataRecordAreaClause.
    def visitDataRecordAreaClause(self, ctx:CobolIsuzuParser.DataRecordAreaClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataRedefinesClause.
    def visitDataRedefinesClause(self, ctx:CobolIsuzuParser.DataRedefinesClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataRenamesClause.
    def visitDataRenamesClause(self, ctx:CobolIsuzuParser.DataRenamesClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataSignClause.
    def visitDataSignClause(self, ctx:CobolIsuzuParser.DataSignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataSynchronizedClause.
    def visitDataSynchronizedClause(self, ctx:CobolIsuzuParser.DataSynchronizedClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataThreadLocalClause.
    def visitDataThreadLocalClause(self, ctx:CobolIsuzuParser.DataThreadLocalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataTypeClause.
    def visitDataTypeClause(self, ctx:CobolIsuzuParser.DataTypeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataTypeDefClause.
    def visitDataTypeDefClause(self, ctx:CobolIsuzuParser.DataTypeDefClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataUsageClause.
    def visitDataUsageClause(self, ctx:CobolIsuzuParser.DataUsageClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataUsingClause.
    def visitDataUsingClause(self, ctx:CobolIsuzuParser.DataUsingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataValueClause.
    def visitDataValueClause(self, ctx:CobolIsuzuParser.DataValueClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataValueInterval.
    def visitDataValueInterval(self, ctx:CobolIsuzuParser.DataValueIntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataValueIntervalFrom.
    def visitDataValueIntervalFrom(self, ctx:CobolIsuzuParser.DataValueIntervalFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataValueIntervalTo.
    def visitDataValueIntervalTo(self, ctx:CobolIsuzuParser.DataValueIntervalToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataWithLowerBoundsClause.
    def visitDataWithLowerBoundsClause(self, ctx:CobolIsuzuParser.DataWithLowerBoundsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#procedureDivision.
    def visitProcedureDivision(self, ctx:CobolIsuzuParser.ProcedureDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#procedureDivisionUsingClause.
    def visitProcedureDivisionUsingClause(self, ctx:CobolIsuzuParser.ProcedureDivisionUsingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#procedureDivisionGivingClause.
    def visitProcedureDivisionGivingClause(self, ctx:CobolIsuzuParser.ProcedureDivisionGivingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#procedureDivisionUsingParameter.
    def visitProcedureDivisionUsingParameter(self, ctx:CobolIsuzuParser.ProcedureDivisionUsingParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#procedureDivisionByReferencePhrase.
    def visitProcedureDivisionByReferencePhrase(self, ctx:CobolIsuzuParser.ProcedureDivisionByReferencePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#procedureDivisionByReference.
    def visitProcedureDivisionByReference(self, ctx:CobolIsuzuParser.ProcedureDivisionByReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#procedureDivisionByValuePhrase.
    def visitProcedureDivisionByValuePhrase(self, ctx:CobolIsuzuParser.ProcedureDivisionByValuePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#procedureDivisionByValue.
    def visitProcedureDivisionByValue(self, ctx:CobolIsuzuParser.ProcedureDivisionByValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#procedureDeclaratives.
    def visitProcedureDeclaratives(self, ctx:CobolIsuzuParser.ProcedureDeclarativesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#procedureDeclarative.
    def visitProcedureDeclarative(self, ctx:CobolIsuzuParser.ProcedureDeclarativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#procedureSectionHeader.
    def visitProcedureSectionHeader(self, ctx:CobolIsuzuParser.ProcedureSectionHeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#procedureDivisionBody.
    def visitProcedureDivisionBody(self, ctx:CobolIsuzuParser.ProcedureDivisionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#procedureSection.
    def visitProcedureSection(self, ctx:CobolIsuzuParser.ProcedureSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#paragraphs.
    def visitParagraphs(self, ctx:CobolIsuzuParser.ParagraphsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#paragraph.
    def visitParagraph(self, ctx:CobolIsuzuParser.ParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#sentence.
    def visitSentence(self, ctx:CobolIsuzuParser.SentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#statement.
    def visitStatement(self, ctx:CobolIsuzuParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#findStatement.
    def visitFindStatement(self, ctx:CobolIsuzuParser.FindStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#viaClause.
    def visitViaClause(self, ctx:CobolIsuzuParser.ViaClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#findOption.
    def visitFindOption(self, ctx:CobolIsuzuParser.FindOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#getStatement.
    def visitGetStatement(self, ctx:CobolIsuzuParser.GetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#finishStatement.
    def visitFinishStatement(self, ctx:CobolIsuzuParser.FinishStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#eraseStatement.
    def visitEraseStatement(self, ctx:CobolIsuzuParser.EraseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#storeStatement.
    def visitStoreStatement(self, ctx:CobolIsuzuParser.StoreStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#storeSendingArea.
    def visitStoreSendingArea(self, ctx:CobolIsuzuParser.StoreSendingAreaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#storeToArea.
    def visitStoreToArea(self, ctx:CobolIsuzuParser.StoreToAreaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#modifyStatement.
    def visitModifyStatement(self, ctx:CobolIsuzuParser.ModifyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#readyStatement.
    def visitReadyStatement(self, ctx:CobolIsuzuParser.ReadyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#transactionEndStatement.
    def visitTransactionEndStatement(self, ctx:CobolIsuzuParser.TransactionEndStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#execCicsStatement2.
    def visitExecCicsStatement2(self, ctx:CobolIsuzuParser.ExecCicsStatement2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#acceptStatement.
    def visitAcceptStatement(self, ctx:CobolIsuzuParser.AcceptStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#acceptFromDateStatement.
    def visitAcceptFromDateStatement(self, ctx:CobolIsuzuParser.AcceptFromDateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#acceptFromMnemonicStatement.
    def visitAcceptFromMnemonicStatement(self, ctx:CobolIsuzuParser.AcceptFromMnemonicStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#acceptFromEscapeKeyStatement.
    def visitAcceptFromEscapeKeyStatement(self, ctx:CobolIsuzuParser.AcceptFromEscapeKeyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#acceptMessageCountStatement.
    def visitAcceptMessageCountStatement(self, ctx:CobolIsuzuParser.AcceptMessageCountStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#addStatement.
    def visitAddStatement(self, ctx:CobolIsuzuParser.AddStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#addToStatement.
    def visitAddToStatement(self, ctx:CobolIsuzuParser.AddToStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#addToGivingStatement.
    def visitAddToGivingStatement(self, ctx:CobolIsuzuParser.AddToGivingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#addCorrespondingStatement.
    def visitAddCorrespondingStatement(self, ctx:CobolIsuzuParser.AddCorrespondingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#addFrom.
    def visitAddFrom(self, ctx:CobolIsuzuParser.AddFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#addTo.
    def visitAddTo(self, ctx:CobolIsuzuParser.AddToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#addToGiving.
    def visitAddToGiving(self, ctx:CobolIsuzuParser.AddToGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#addGiving.
    def visitAddGiving(self, ctx:CobolIsuzuParser.AddGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#alteredGoTo.
    def visitAlteredGoTo(self, ctx:CobolIsuzuParser.AlteredGoToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#alterStatement.
    def visitAlterStatement(self, ctx:CobolIsuzuParser.AlterStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#alterProceedTo.
    def visitAlterProceedTo(self, ctx:CobolIsuzuParser.AlterProceedToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#callStatement.
    def visitCallStatement(self, ctx:CobolIsuzuParser.CallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#callUsingPhrase.
    def visitCallUsingPhrase(self, ctx:CobolIsuzuParser.CallUsingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#callUsingParameter.
    def visitCallUsingParameter(self, ctx:CobolIsuzuParser.CallUsingParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#callByReferencePhrase.
    def visitCallByReferencePhrase(self, ctx:CobolIsuzuParser.CallByReferencePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#callByReference.
    def visitCallByReference(self, ctx:CobolIsuzuParser.CallByReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#callByValuePhrase.
    def visitCallByValuePhrase(self, ctx:CobolIsuzuParser.CallByValuePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#callByValue.
    def visitCallByValue(self, ctx:CobolIsuzuParser.CallByValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#callByContentPhrase.
    def visitCallByContentPhrase(self, ctx:CobolIsuzuParser.CallByContentPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#callByContent.
    def visitCallByContent(self, ctx:CobolIsuzuParser.CallByContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#callGivingPhrase.
    def visitCallGivingPhrase(self, ctx:CobolIsuzuParser.CallGivingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#callSystem.
    def visitCallSystem(self, ctx:CobolIsuzuParser.CallSystemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#cancelStatement.
    def visitCancelStatement(self, ctx:CobolIsuzuParser.CancelStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#cancelCall.
    def visitCancelCall(self, ctx:CobolIsuzuParser.CancelCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#closeStatement.
    def visitCloseStatement(self, ctx:CobolIsuzuParser.CloseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#closePhrase.
    def visitClosePhrase(self, ctx:CobolIsuzuParser.ClosePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#closeFile.
    def visitCloseFile(self, ctx:CobolIsuzuParser.CloseFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#closeReelUnitStatement.
    def visitCloseReelUnitStatement(self, ctx:CobolIsuzuParser.CloseReelUnitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#closeRelativeStatement.
    def visitCloseRelativeStatement(self, ctx:CobolIsuzuParser.CloseRelativeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#closePortFileIOStatement.
    def visitClosePortFileIOStatement(self, ctx:CobolIsuzuParser.ClosePortFileIOStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#closePortFileIOUsing.
    def visitClosePortFileIOUsing(self, ctx:CobolIsuzuParser.ClosePortFileIOUsingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#closePortFileIOUsingCloseDisposition.
    def visitClosePortFileIOUsingCloseDisposition(self, ctx:CobolIsuzuParser.ClosePortFileIOUsingCloseDispositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#closePortFileIOUsingAssociatedData.
    def visitClosePortFileIOUsingAssociatedData(self, ctx:CobolIsuzuParser.ClosePortFileIOUsingAssociatedDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#closePortFileIOUsingAssociatedDataLength.
    def visitClosePortFileIOUsingAssociatedDataLength(self, ctx:CobolIsuzuParser.ClosePortFileIOUsingAssociatedDataLengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#computeStatement.
    def visitComputeStatement(self, ctx:CobolIsuzuParser.ComputeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#computeStore.
    def visitComputeStore(self, ctx:CobolIsuzuParser.ComputeStoreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#continueStatement.
    def visitContinueStatement(self, ctx:CobolIsuzuParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#deleteStatement.
    def visitDeleteStatement(self, ctx:CobolIsuzuParser.DeleteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#disableStatement.
    def visitDisableStatement(self, ctx:CobolIsuzuParser.DisableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#displayStatement.
    def visitDisplayStatement(self, ctx:CobolIsuzuParser.DisplayStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#displayOperand.
    def visitDisplayOperand(self, ctx:CobolIsuzuParser.DisplayOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#displayAt.
    def visitDisplayAt(self, ctx:CobolIsuzuParser.DisplayAtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#displayUpon.
    def visitDisplayUpon(self, ctx:CobolIsuzuParser.DisplayUponContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#displayWith.
    def visitDisplayWith(self, ctx:CobolIsuzuParser.DisplayWithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#divideStatement.
    def visitDivideStatement(self, ctx:CobolIsuzuParser.DivideStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#divideIntoStatement.
    def visitDivideIntoStatement(self, ctx:CobolIsuzuParser.DivideIntoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#divideIntoGivingStatement.
    def visitDivideIntoGivingStatement(self, ctx:CobolIsuzuParser.DivideIntoGivingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#divideByGivingStatement.
    def visitDivideByGivingStatement(self, ctx:CobolIsuzuParser.DivideByGivingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#divideGivingPhrase.
    def visitDivideGivingPhrase(self, ctx:CobolIsuzuParser.DivideGivingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#divideInto.
    def visitDivideInto(self, ctx:CobolIsuzuParser.DivideIntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#divideGiving.
    def visitDivideGiving(self, ctx:CobolIsuzuParser.DivideGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#divideRemainder.
    def visitDivideRemainder(self, ctx:CobolIsuzuParser.DivideRemainderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#enableStatement.
    def visitEnableStatement(self, ctx:CobolIsuzuParser.EnableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#entryStatement.
    def visitEntryStatement(self, ctx:CobolIsuzuParser.EntryStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#evaluateStatement.
    def visitEvaluateStatement(self, ctx:CobolIsuzuParser.EvaluateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#evaluateSelect.
    def visitEvaluateSelect(self, ctx:CobolIsuzuParser.EvaluateSelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#evaluateAlsoSelect.
    def visitEvaluateAlsoSelect(self, ctx:CobolIsuzuParser.EvaluateAlsoSelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#evaluateWhenPhrase.
    def visitEvaluateWhenPhrase(self, ctx:CobolIsuzuParser.EvaluateWhenPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#evaluateWhen.
    def visitEvaluateWhen(self, ctx:CobolIsuzuParser.EvaluateWhenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#evaluateCondition.
    def visitEvaluateCondition(self, ctx:CobolIsuzuParser.EvaluateConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#evaluateThrough.
    def visitEvaluateThrough(self, ctx:CobolIsuzuParser.EvaluateThroughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#evaluateAlsoCondition.
    def visitEvaluateAlsoCondition(self, ctx:CobolIsuzuParser.EvaluateAlsoConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#evaluateWhenOther.
    def visitEvaluateWhenOther(self, ctx:CobolIsuzuParser.EvaluateWhenOtherContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#evaluateValue.
    def visitEvaluateValue(self, ctx:CobolIsuzuParser.EvaluateValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#execCicsStatement.
    def visitExecCicsStatement(self, ctx:CobolIsuzuParser.ExecCicsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#execSqlStatement.
    def visitExecSqlStatement(self, ctx:CobolIsuzuParser.ExecSqlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#execSqlImsStatement.
    def visitExecSqlImsStatement(self, ctx:CobolIsuzuParser.ExecSqlImsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#exhibitStatement.
    def visitExhibitStatement(self, ctx:CobolIsuzuParser.ExhibitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#exhibitOperand.
    def visitExhibitOperand(self, ctx:CobolIsuzuParser.ExhibitOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#exitStatement.
    def visitExitStatement(self, ctx:CobolIsuzuParser.ExitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#generateStatement.
    def visitGenerateStatement(self, ctx:CobolIsuzuParser.GenerateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#gobackStatement.
    def visitGobackStatement(self, ctx:CobolIsuzuParser.GobackStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#goToStatement.
    def visitGoToStatement(self, ctx:CobolIsuzuParser.GoToStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#goToStatementSimple.
    def visitGoToStatementSimple(self, ctx:CobolIsuzuParser.GoToStatementSimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#goToDependingOnStatement.
    def visitGoToDependingOnStatement(self, ctx:CobolIsuzuParser.GoToDependingOnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#ifStatement.
    def visitIfStatement(self, ctx:CobolIsuzuParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#ifThen.
    def visitIfThen(self, ctx:CobolIsuzuParser.IfThenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#ifElse.
    def visitIfElse(self, ctx:CobolIsuzuParser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#initializeStatement.
    def visitInitializeStatement(self, ctx:CobolIsuzuParser.InitializeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#initializeReplacingPhrase.
    def visitInitializeReplacingPhrase(self, ctx:CobolIsuzuParser.InitializeReplacingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#initializeReplacingBy.
    def visitInitializeReplacingBy(self, ctx:CobolIsuzuParser.InitializeReplacingByContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#initiateStatement.
    def visitInitiateStatement(self, ctx:CobolIsuzuParser.InitiateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#inspectStatement.
    def visitInspectStatement(self, ctx:CobolIsuzuParser.InspectStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#inspectTallyingPhrase.
    def visitInspectTallyingPhrase(self, ctx:CobolIsuzuParser.InspectTallyingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#inspectReplacingPhrase.
    def visitInspectReplacingPhrase(self, ctx:CobolIsuzuParser.InspectReplacingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#inspectTallyingReplacingPhrase.
    def visitInspectTallyingReplacingPhrase(self, ctx:CobolIsuzuParser.InspectTallyingReplacingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#inspectConvertingPhrase.
    def visitInspectConvertingPhrase(self, ctx:CobolIsuzuParser.InspectConvertingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#inspectFor.
    def visitInspectFor(self, ctx:CobolIsuzuParser.InspectForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#inspectCharacters.
    def visitInspectCharacters(self, ctx:CobolIsuzuParser.InspectCharactersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#inspectReplacingCharacters.
    def visitInspectReplacingCharacters(self, ctx:CobolIsuzuParser.InspectReplacingCharactersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#inspectAllLeadings.
    def visitInspectAllLeadings(self, ctx:CobolIsuzuParser.InspectAllLeadingsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#inspectReplacingAllLeadings.
    def visitInspectReplacingAllLeadings(self, ctx:CobolIsuzuParser.InspectReplacingAllLeadingsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#inspectAllLeading.
    def visitInspectAllLeading(self, ctx:CobolIsuzuParser.InspectAllLeadingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#inspectReplacingAllLeading.
    def visitInspectReplacingAllLeading(self, ctx:CobolIsuzuParser.InspectReplacingAllLeadingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#inspectBy.
    def visitInspectBy(self, ctx:CobolIsuzuParser.InspectByContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#inspectTo.
    def visitInspectTo(self, ctx:CobolIsuzuParser.InspectToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#inspectBeforeAfter.
    def visitInspectBeforeAfter(self, ctx:CobolIsuzuParser.InspectBeforeAfterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#mergeStatement.
    def visitMergeStatement(self, ctx:CobolIsuzuParser.MergeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#mergeOnKeyClause.
    def visitMergeOnKeyClause(self, ctx:CobolIsuzuParser.MergeOnKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#mergeCollatingSequencePhrase.
    def visitMergeCollatingSequencePhrase(self, ctx:CobolIsuzuParser.MergeCollatingSequencePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#mergeCollatingAlphanumeric.
    def visitMergeCollatingAlphanumeric(self, ctx:CobolIsuzuParser.MergeCollatingAlphanumericContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#mergeCollatingNational.
    def visitMergeCollatingNational(self, ctx:CobolIsuzuParser.MergeCollatingNationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#mergeUsing.
    def visitMergeUsing(self, ctx:CobolIsuzuParser.MergeUsingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#mergeOutputProcedurePhrase.
    def visitMergeOutputProcedurePhrase(self, ctx:CobolIsuzuParser.MergeOutputProcedurePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#mergeOutputThrough.
    def visitMergeOutputThrough(self, ctx:CobolIsuzuParser.MergeOutputThroughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#mergeGivingPhrase.
    def visitMergeGivingPhrase(self, ctx:CobolIsuzuParser.MergeGivingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#mergeGiving.
    def visitMergeGiving(self, ctx:CobolIsuzuParser.MergeGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#moveStatement.
    def visitMoveStatement(self, ctx:CobolIsuzuParser.MoveStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#moveToStatement.
    def visitMoveToStatement(self, ctx:CobolIsuzuParser.MoveToStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#moveToSendingArea.
    def visitMoveToSendingArea(self, ctx:CobolIsuzuParser.MoveToSendingAreaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#moveCorrespondingToStatement.
    def visitMoveCorrespondingToStatement(self, ctx:CobolIsuzuParser.MoveCorrespondingToStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#moveCorrespondingToSendingArea.
    def visitMoveCorrespondingToSendingArea(self, ctx:CobolIsuzuParser.MoveCorrespondingToSendingAreaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#moveAttributeClause.
    def visitMoveAttributeClause(self, ctx:CobolIsuzuParser.MoveAttributeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#multiplyStatement.
    def visitMultiplyStatement(self, ctx:CobolIsuzuParser.MultiplyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#multiplyRegular.
    def visitMultiplyRegular(self, ctx:CobolIsuzuParser.MultiplyRegularContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#multiplyRegularOperand.
    def visitMultiplyRegularOperand(self, ctx:CobolIsuzuParser.MultiplyRegularOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#multiplyGiving.
    def visitMultiplyGiving(self, ctx:CobolIsuzuParser.MultiplyGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#multiplyGivingOperand.
    def visitMultiplyGivingOperand(self, ctx:CobolIsuzuParser.MultiplyGivingOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#multiplyGivingResult.
    def visitMultiplyGivingResult(self, ctx:CobolIsuzuParser.MultiplyGivingResultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#openStatement.
    def visitOpenStatement(self, ctx:CobolIsuzuParser.OpenStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#openInputStatement.
    def visitOpenInputStatement(self, ctx:CobolIsuzuParser.OpenInputStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#openInput.
    def visitOpenInput(self, ctx:CobolIsuzuParser.OpenInputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#openOutputStatement.
    def visitOpenOutputStatement(self, ctx:CobolIsuzuParser.OpenOutputStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#openOutput.
    def visitOpenOutput(self, ctx:CobolIsuzuParser.OpenOutputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#openIOStatement.
    def visitOpenIOStatement(self, ctx:CobolIsuzuParser.OpenIOStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#openExtendStatement.
    def visitOpenExtendStatement(self, ctx:CobolIsuzuParser.OpenExtendStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#performStatement.
    def visitPerformStatement(self, ctx:CobolIsuzuParser.PerformStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#performInlineStatement.
    def visitPerformInlineStatement(self, ctx:CobolIsuzuParser.PerformInlineStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#performProcedureStatement.
    def visitPerformProcedureStatement(self, ctx:CobolIsuzuParser.PerformProcedureStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#performType.
    def visitPerformType(self, ctx:CobolIsuzuParser.PerformTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#performTimes.
    def visitPerformTimes(self, ctx:CobolIsuzuParser.PerformTimesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#performUntil.
    def visitPerformUntil(self, ctx:CobolIsuzuParser.PerformUntilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#performVarying.
    def visitPerformVarying(self, ctx:CobolIsuzuParser.PerformVaryingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#performVaryingClause.
    def visitPerformVaryingClause(self, ctx:CobolIsuzuParser.PerformVaryingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#performVaryingPhrase.
    def visitPerformVaryingPhrase(self, ctx:CobolIsuzuParser.PerformVaryingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#performAfter.
    def visitPerformAfter(self, ctx:CobolIsuzuParser.PerformAfterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#performFrom.
    def visitPerformFrom(self, ctx:CobolIsuzuParser.PerformFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#performBy.
    def visitPerformBy(self, ctx:CobolIsuzuParser.PerformByContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#performTestClause.
    def visitPerformTestClause(self, ctx:CobolIsuzuParser.PerformTestClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#purgeStatement.
    def visitPurgeStatement(self, ctx:CobolIsuzuParser.PurgeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#readStatement.
    def visitReadStatement(self, ctx:CobolIsuzuParser.ReadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#readInto.
    def visitReadInto(self, ctx:CobolIsuzuParser.ReadIntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#readWith.
    def visitReadWith(self, ctx:CobolIsuzuParser.ReadWithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#readKey.
    def visitReadKey(self, ctx:CobolIsuzuParser.ReadKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#receiveStatement.
    def visitReceiveStatement(self, ctx:CobolIsuzuParser.ReceiveStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#receiveFromStatement.
    def visitReceiveFromStatement(self, ctx:CobolIsuzuParser.ReceiveFromStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#receiveFrom.
    def visitReceiveFrom(self, ctx:CobolIsuzuParser.ReceiveFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#receiveIntoStatement.
    def visitReceiveIntoStatement(self, ctx:CobolIsuzuParser.ReceiveIntoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#receiveNoData.
    def visitReceiveNoData(self, ctx:CobolIsuzuParser.ReceiveNoDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#receiveWithData.
    def visitReceiveWithData(self, ctx:CobolIsuzuParser.ReceiveWithDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#receiveBefore.
    def visitReceiveBefore(self, ctx:CobolIsuzuParser.ReceiveBeforeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#receiveWith.
    def visitReceiveWith(self, ctx:CobolIsuzuParser.ReceiveWithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#receiveThread.
    def visitReceiveThread(self, ctx:CobolIsuzuParser.ReceiveThreadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#receiveSize.
    def visitReceiveSize(self, ctx:CobolIsuzuParser.ReceiveSizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#receiveStatus.
    def visitReceiveStatus(self, ctx:CobolIsuzuParser.ReceiveStatusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#releaseStatement.
    def visitReleaseStatement(self, ctx:CobolIsuzuParser.ReleaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#returnStatement.
    def visitReturnStatement(self, ctx:CobolIsuzuParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#returnInto.
    def visitReturnInto(self, ctx:CobolIsuzuParser.ReturnIntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#rewriteStatement.
    def visitRewriteStatement(self, ctx:CobolIsuzuParser.RewriteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#rewriteFrom.
    def visitRewriteFrom(self, ctx:CobolIsuzuParser.RewriteFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#searchStatement.
    def visitSearchStatement(self, ctx:CobolIsuzuParser.SearchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#searchVarying.
    def visitSearchVarying(self, ctx:CobolIsuzuParser.SearchVaryingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#searchWhen.
    def visitSearchWhen(self, ctx:CobolIsuzuParser.SearchWhenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#sendStatement.
    def visitSendStatement(self, ctx:CobolIsuzuParser.SendStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#sendStatementSync.
    def visitSendStatementSync(self, ctx:CobolIsuzuParser.SendStatementSyncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#sendStatementAsync.
    def visitSendStatementAsync(self, ctx:CobolIsuzuParser.SendStatementAsyncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#sendFromPhrase.
    def visitSendFromPhrase(self, ctx:CobolIsuzuParser.SendFromPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#sendWithPhrase.
    def visitSendWithPhrase(self, ctx:CobolIsuzuParser.SendWithPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#sendReplacingPhrase.
    def visitSendReplacingPhrase(self, ctx:CobolIsuzuParser.SendReplacingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#sendAdvancingPhrase.
    def visitSendAdvancingPhrase(self, ctx:CobolIsuzuParser.SendAdvancingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#sendAdvancingPage.
    def visitSendAdvancingPage(self, ctx:CobolIsuzuParser.SendAdvancingPageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#sendAdvancingLines.
    def visitSendAdvancingLines(self, ctx:CobolIsuzuParser.SendAdvancingLinesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#sendAdvancingMnemonic.
    def visitSendAdvancingMnemonic(self, ctx:CobolIsuzuParser.SendAdvancingMnemonicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#setStatement.
    def visitSetStatement(self, ctx:CobolIsuzuParser.SetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#setToStatement.
    def visitSetToStatement(self, ctx:CobolIsuzuParser.SetToStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#setUpDownByStatement.
    def visitSetUpDownByStatement(self, ctx:CobolIsuzuParser.SetUpDownByStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#setTo.
    def visitSetTo(self, ctx:CobolIsuzuParser.SetToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#setToValue.
    def visitSetToValue(self, ctx:CobolIsuzuParser.SetToValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#setByValue.
    def visitSetByValue(self, ctx:CobolIsuzuParser.SetByValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#sortStatement.
    def visitSortStatement(self, ctx:CobolIsuzuParser.SortStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#sortOnKeyClause.
    def visitSortOnKeyClause(self, ctx:CobolIsuzuParser.SortOnKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#sortDuplicatesPhrase.
    def visitSortDuplicatesPhrase(self, ctx:CobolIsuzuParser.SortDuplicatesPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#sortCollatingSequencePhrase.
    def visitSortCollatingSequencePhrase(self, ctx:CobolIsuzuParser.SortCollatingSequencePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#sortCollatingAlphanumeric.
    def visitSortCollatingAlphanumeric(self, ctx:CobolIsuzuParser.SortCollatingAlphanumericContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#sortCollatingNational.
    def visitSortCollatingNational(self, ctx:CobolIsuzuParser.SortCollatingNationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#sortInputProcedurePhrase.
    def visitSortInputProcedurePhrase(self, ctx:CobolIsuzuParser.SortInputProcedurePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#sortInputThrough.
    def visitSortInputThrough(self, ctx:CobolIsuzuParser.SortInputThroughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#sortUsing.
    def visitSortUsing(self, ctx:CobolIsuzuParser.SortUsingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#sortOutputProcedurePhrase.
    def visitSortOutputProcedurePhrase(self, ctx:CobolIsuzuParser.SortOutputProcedurePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#sortOutputThrough.
    def visitSortOutputThrough(self, ctx:CobolIsuzuParser.SortOutputThroughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#sortGivingPhrase.
    def visitSortGivingPhrase(self, ctx:CobolIsuzuParser.SortGivingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#sortGiving.
    def visitSortGiving(self, ctx:CobolIsuzuParser.SortGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#startStatement.
    def visitStartStatement(self, ctx:CobolIsuzuParser.StartStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#startKey.
    def visitStartKey(self, ctx:CobolIsuzuParser.StartKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#stopStatement.
    def visitStopStatement(self, ctx:CobolIsuzuParser.StopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#stringStatement.
    def visitStringStatement(self, ctx:CobolIsuzuParser.StringStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#stringSendingPhrase.
    def visitStringSendingPhrase(self, ctx:CobolIsuzuParser.StringSendingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#stringSending.
    def visitStringSending(self, ctx:CobolIsuzuParser.StringSendingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#stringDelimitedByPhrase.
    def visitStringDelimitedByPhrase(self, ctx:CobolIsuzuParser.StringDelimitedByPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#stringForPhrase.
    def visitStringForPhrase(self, ctx:CobolIsuzuParser.StringForPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#stringIntoPhrase.
    def visitStringIntoPhrase(self, ctx:CobolIsuzuParser.StringIntoPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#stringWithPointerPhrase.
    def visitStringWithPointerPhrase(self, ctx:CobolIsuzuParser.StringWithPointerPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#subtractStatement.
    def visitSubtractStatement(self, ctx:CobolIsuzuParser.SubtractStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#subtractFromStatement.
    def visitSubtractFromStatement(self, ctx:CobolIsuzuParser.SubtractFromStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#subtractFromGivingStatement.
    def visitSubtractFromGivingStatement(self, ctx:CobolIsuzuParser.SubtractFromGivingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#subtractCorrespondingStatement.
    def visitSubtractCorrespondingStatement(self, ctx:CobolIsuzuParser.SubtractCorrespondingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#subtractSubtrahend.
    def visitSubtractSubtrahend(self, ctx:CobolIsuzuParser.SubtractSubtrahendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#subtractMinuend.
    def visitSubtractMinuend(self, ctx:CobolIsuzuParser.SubtractMinuendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#subtractMinuendGiving.
    def visitSubtractMinuendGiving(self, ctx:CobolIsuzuParser.SubtractMinuendGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#subtractGiving.
    def visitSubtractGiving(self, ctx:CobolIsuzuParser.SubtractGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#subtractMinuendCorresponding.
    def visitSubtractMinuendCorresponding(self, ctx:CobolIsuzuParser.SubtractMinuendCorrespondingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#transactionStatement.
    def visitTransactionStatement(self, ctx:CobolIsuzuParser.TransactionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#transactionStart.
    def visitTransactionStart(self, ctx:CobolIsuzuParser.TransactionStartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#transactionBody.
    def visitTransactionBody(self, ctx:CobolIsuzuParser.TransactionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#transactionEnd.
    def visitTransactionEnd(self, ctx:CobolIsuzuParser.TransactionEndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#transactionCancelStatement.
    def visitTransactionCancelStatement(self, ctx:CobolIsuzuParser.TransactionCancelStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#terminateStatement.
    def visitTerminateStatement(self, ctx:CobolIsuzuParser.TerminateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#unstringStatement.
    def visitUnstringStatement(self, ctx:CobolIsuzuParser.UnstringStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#unstringSendingPhrase.
    def visitUnstringSendingPhrase(self, ctx:CobolIsuzuParser.UnstringSendingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#unstringDelimitedByPhrase.
    def visitUnstringDelimitedByPhrase(self, ctx:CobolIsuzuParser.UnstringDelimitedByPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#unstringOrAllPhrase.
    def visitUnstringOrAllPhrase(self, ctx:CobolIsuzuParser.UnstringOrAllPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#unstringIntoPhrase.
    def visitUnstringIntoPhrase(self, ctx:CobolIsuzuParser.UnstringIntoPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#unstringInto.
    def visitUnstringInto(self, ctx:CobolIsuzuParser.UnstringIntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#unstringDelimiterIn.
    def visitUnstringDelimiterIn(self, ctx:CobolIsuzuParser.UnstringDelimiterInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#unstringCountIn.
    def visitUnstringCountIn(self, ctx:CobolIsuzuParser.UnstringCountInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#unstringWithPointerPhrase.
    def visitUnstringWithPointerPhrase(self, ctx:CobolIsuzuParser.UnstringWithPointerPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#unstringTallyingPhrase.
    def visitUnstringTallyingPhrase(self, ctx:CobolIsuzuParser.UnstringTallyingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#useStatement.
    def visitUseStatement(self, ctx:CobolIsuzuParser.UseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#useFor.
    def visitUseFor(self, ctx:CobolIsuzuParser.UseForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#useAfterClause.
    def visitUseAfterClause(self, ctx:CobolIsuzuParser.UseAfterClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#useAfterOn.
    def visitUseAfterOn(self, ctx:CobolIsuzuParser.UseAfterOnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#useDebugClause.
    def visitUseDebugClause(self, ctx:CobolIsuzuParser.UseDebugClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#useDebugOn.
    def visitUseDebugOn(self, ctx:CobolIsuzuParser.UseDebugOnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#useDeadLock.
    def visitUseDeadLock(self, ctx:CobolIsuzuParser.UseDeadLockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#writeStatement.
    def visitWriteStatement(self, ctx:CobolIsuzuParser.WriteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#writeFromPhrase.
    def visitWriteFromPhrase(self, ctx:CobolIsuzuParser.WriteFromPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#writeAdvancingPhrase.
    def visitWriteAdvancingPhrase(self, ctx:CobolIsuzuParser.WriteAdvancingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#writeAdvancingPage.
    def visitWriteAdvancingPage(self, ctx:CobolIsuzuParser.WriteAdvancingPageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#writeAdvancingLines.
    def visitWriteAdvancingLines(self, ctx:CobolIsuzuParser.WriteAdvancingLinesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#writeAdvancingMnemonic.
    def visitWriteAdvancingMnemonic(self, ctx:CobolIsuzuParser.WriteAdvancingMnemonicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#writeAtEndOfPagePhrase.
    def visitWriteAtEndOfPagePhrase(self, ctx:CobolIsuzuParser.WriteAtEndOfPagePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#writeNotAtEndOfPagePhrase.
    def visitWriteNotAtEndOfPagePhrase(self, ctx:CobolIsuzuParser.WriteNotAtEndOfPagePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#atEndPhrase.
    def visitAtEndPhrase(self, ctx:CobolIsuzuParser.AtEndPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#notAtEndPhrase.
    def visitNotAtEndPhrase(self, ctx:CobolIsuzuParser.NotAtEndPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#invalidKeyPhrase.
    def visitInvalidKeyPhrase(self, ctx:CobolIsuzuParser.InvalidKeyPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#notInvalidKeyPhrase.
    def visitNotInvalidKeyPhrase(self, ctx:CobolIsuzuParser.NotInvalidKeyPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#onOverflowPhrase.
    def visitOnOverflowPhrase(self, ctx:CobolIsuzuParser.OnOverflowPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#notOnOverflowPhrase.
    def visitNotOnOverflowPhrase(self, ctx:CobolIsuzuParser.NotOnOverflowPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#onSizeErrorPhrase.
    def visitOnSizeErrorPhrase(self, ctx:CobolIsuzuParser.OnSizeErrorPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#notOnSizeErrorPhrase.
    def visitNotOnSizeErrorPhrase(self, ctx:CobolIsuzuParser.NotOnSizeErrorPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#onExceptionClause.
    def visitOnExceptionClause(self, ctx:CobolIsuzuParser.OnExceptionClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#notOnExceptionClause.
    def visitNotOnExceptionClause(self, ctx:CobolIsuzuParser.NotOnExceptionClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#arithmeticExpression.
    def visitArithmeticExpression(self, ctx:CobolIsuzuParser.ArithmeticExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#plusMinus.
    def visitPlusMinus(self, ctx:CobolIsuzuParser.PlusMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#multDivs.
    def visitMultDivs(self, ctx:CobolIsuzuParser.MultDivsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#multDiv.
    def visitMultDiv(self, ctx:CobolIsuzuParser.MultDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#powers.
    def visitPowers(self, ctx:CobolIsuzuParser.PowersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#power.
    def visitPower(self, ctx:CobolIsuzuParser.PowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#basis.
    def visitBasis(self, ctx:CobolIsuzuParser.BasisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#condition.
    def visitCondition(self, ctx:CobolIsuzuParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#andOrCondition.
    def visitAndOrCondition(self, ctx:CobolIsuzuParser.AndOrConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#combinableCondition.
    def visitCombinableCondition(self, ctx:CobolIsuzuParser.CombinableConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#simpleCondition.
    def visitSimpleCondition(self, ctx:CobolIsuzuParser.SimpleConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#classCondition.
    def visitClassCondition(self, ctx:CobolIsuzuParser.ClassConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#conditionNameReference.
    def visitConditionNameReference(self, ctx:CobolIsuzuParser.ConditionNameReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#conditionNameSubscriptReference.
    def visitConditionNameSubscriptReference(self, ctx:CobolIsuzuParser.ConditionNameSubscriptReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#relationCondition.
    def visitRelationCondition(self, ctx:CobolIsuzuParser.RelationConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#relationSignCondition.
    def visitRelationSignCondition(self, ctx:CobolIsuzuParser.RelationSignConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#relationArithmeticComparison.
    def visitRelationArithmeticComparison(self, ctx:CobolIsuzuParser.RelationArithmeticComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#relationCombinedComparison.
    def visitRelationCombinedComparison(self, ctx:CobolIsuzuParser.RelationCombinedComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#relationCombinedCondition.
    def visitRelationCombinedCondition(self, ctx:CobolIsuzuParser.RelationCombinedConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#relationalOperator.
    def visitRelationalOperator(self, ctx:CobolIsuzuParser.RelationalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#abbreviation.
    def visitAbbreviation(self, ctx:CobolIsuzuParser.AbbreviationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#identifier.
    def visitIdentifier(self, ctx:CobolIsuzuParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#tableCall.
    def visitTableCall(self, ctx:CobolIsuzuParser.TableCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#functionCall.
    def visitFunctionCall(self, ctx:CobolIsuzuParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#referenceModifier.
    def visitReferenceModifier(self, ctx:CobolIsuzuParser.ReferenceModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#characterPosition.
    def visitCharacterPosition(self, ctx:CobolIsuzuParser.CharacterPositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#length.
    def visitLength(self, ctx:CobolIsuzuParser.LengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#subscript_.
    def visitSubscript_(self, ctx:CobolIsuzuParser.Subscript_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#argument.
    def visitArgument(self, ctx:CobolIsuzuParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#qualifiedDataName.
    def visitQualifiedDataName(self, ctx:CobolIsuzuParser.QualifiedDataNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#qualifiedDataNameFormat1.
    def visitQualifiedDataNameFormat1(self, ctx:CobolIsuzuParser.QualifiedDataNameFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#qualifiedDataNameFormat2.
    def visitQualifiedDataNameFormat2(self, ctx:CobolIsuzuParser.QualifiedDataNameFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#qualifiedDataNameFormat3.
    def visitQualifiedDataNameFormat3(self, ctx:CobolIsuzuParser.QualifiedDataNameFormat3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#qualifiedDataNameFormat4.
    def visitQualifiedDataNameFormat4(self, ctx:CobolIsuzuParser.QualifiedDataNameFormat4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#qualifiedInData.
    def visitQualifiedInData(self, ctx:CobolIsuzuParser.QualifiedInDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#inData.
    def visitInData(self, ctx:CobolIsuzuParser.InDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#inFile.
    def visitInFile(self, ctx:CobolIsuzuParser.InFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#inMnemonic.
    def visitInMnemonic(self, ctx:CobolIsuzuParser.InMnemonicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#inSection.
    def visitInSection(self, ctx:CobolIsuzuParser.InSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#inLibrary.
    def visitInLibrary(self, ctx:CobolIsuzuParser.InLibraryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#inTable.
    def visitInTable(self, ctx:CobolIsuzuParser.InTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#alphabetName.
    def visitAlphabetName(self, ctx:CobolIsuzuParser.AlphabetNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#assignmentName.
    def visitAssignmentName(self, ctx:CobolIsuzuParser.AssignmentNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#basisName.
    def visitBasisName(self, ctx:CobolIsuzuParser.BasisNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#cdName.
    def visitCdName(self, ctx:CobolIsuzuParser.CdNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#className.
    def visitClassName(self, ctx:CobolIsuzuParser.ClassNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#computerName.
    def visitComputerName(self, ctx:CobolIsuzuParser.ComputerNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#conditionName.
    def visitConditionName(self, ctx:CobolIsuzuParser.ConditionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataName.
    def visitDataName(self, ctx:CobolIsuzuParser.DataNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#dataDescName.
    def visitDataDescName(self, ctx:CobolIsuzuParser.DataDescNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#environmentName.
    def visitEnvironmentName(self, ctx:CobolIsuzuParser.EnvironmentNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#fileName.
    def visitFileName(self, ctx:CobolIsuzuParser.FileNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#functionName.
    def visitFunctionName(self, ctx:CobolIsuzuParser.FunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#indexName.
    def visitIndexName(self, ctx:CobolIsuzuParser.IndexNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#languageName.
    def visitLanguageName(self, ctx:CobolIsuzuParser.LanguageNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#libraryName.
    def visitLibraryName(self, ctx:CobolIsuzuParser.LibraryNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#localName.
    def visitLocalName(self, ctx:CobolIsuzuParser.LocalNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#mnemonicName.
    def visitMnemonicName(self, ctx:CobolIsuzuParser.MnemonicNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#paragraphName.
    def visitParagraphName(self, ctx:CobolIsuzuParser.ParagraphNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#procedureName.
    def visitProcedureName(self, ctx:CobolIsuzuParser.ProcedureNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#programName.
    def visitProgramName(self, ctx:CobolIsuzuParser.ProgramNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#recordName.
    def visitRecordName(self, ctx:CobolIsuzuParser.RecordNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#reportName.
    def visitReportName(self, ctx:CobolIsuzuParser.ReportNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#routineName.
    def visitRoutineName(self, ctx:CobolIsuzuParser.RoutineNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#screenName.
    def visitScreenName(self, ctx:CobolIsuzuParser.ScreenNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#schemaName.
    def visitSchemaName(self, ctx:CobolIsuzuParser.SchemaNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#sectionName.
    def visitSectionName(self, ctx:CobolIsuzuParser.SectionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#systemName.
    def visitSystemName(self, ctx:CobolIsuzuParser.SystemNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#symbolicCharacter.
    def visitSymbolicCharacter(self, ctx:CobolIsuzuParser.SymbolicCharacterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#textName.
    def visitTextName(self, ctx:CobolIsuzuParser.TextNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#booleanLiteral.
    def visitBooleanLiteral(self, ctx:CobolIsuzuParser.BooleanLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#numericLiteral.
    def visitNumericLiteral(self, ctx:CobolIsuzuParser.NumericLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#integerLiteral.
    def visitIntegerLiteral(self, ctx:CobolIsuzuParser.IntegerLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#cicsDfhRespLiteral.
    def visitCicsDfhRespLiteral(self, ctx:CobolIsuzuParser.CicsDfhRespLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#cicsDfhValueLiteral.
    def visitCicsDfhValueLiteral(self, ctx:CobolIsuzuParser.CicsDfhValueLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#figurativeConstant.
    def visitFigurativeConstant(self, ctx:CobolIsuzuParser.FigurativeConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#specialRegister.
    def visitSpecialRegister(self, ctx:CobolIsuzuParser.SpecialRegisterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#commentEntry.
    def visitCommentEntry(self, ctx:CobolIsuzuParser.CommentEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolIsuzuParser#charDataKeyword.
    def visitCharDataKeyword(self, ctx:CobolIsuzuParser.CharDataKeywordContext):
        return self.visitChildren(ctx)



del CobolIsuzuParser