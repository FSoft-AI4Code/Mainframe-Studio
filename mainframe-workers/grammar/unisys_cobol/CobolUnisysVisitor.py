# Generated from ./app/tasks/grammar/unisys_cobol/CobolUnisys.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CobolUnisysParser import CobolUnisysParser
else:
    from CobolUnisysParser import CobolUnisysParser

# This class defines a complete generic visitor for a parse tree produced by CobolUnisysParser.

class CobolUnisysVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CobolUnisysParser#startRule.
    def visitStartRule(self, ctx:CobolUnisysParser.StartRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#compilationUnit.
    def visitCompilationUnit(self, ctx:CobolUnisysParser.CompilationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#programUnit.
    def visitProgramUnit(self, ctx:CobolUnisysParser.ProgramUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#endProgramStatement.
    def visitEndProgramStatement(self, ctx:CobolUnisysParser.EndProgramStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#identificationDivision.
    def visitIdentificationDivision(self, ctx:CobolUnisysParser.IdentificationDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#identificationDivisionBody.
    def visitIdentificationDivisionBody(self, ctx:CobolUnisysParser.IdentificationDivisionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#programIdParagraph.
    def visitProgramIdParagraph(self, ctx:CobolUnisysParser.ProgramIdParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#author_name.
    def visitAuthor_name(self, ctx:CobolUnisysParser.Author_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#authorParagraph.
    def visitAuthorParagraph(self, ctx:CobolUnisysParser.AuthorParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#installationParagraph.
    def visitInstallationParagraph(self, ctx:CobolUnisysParser.InstallationParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dateWrittenParagraph.
    def visitDateWrittenParagraph(self, ctx:CobolUnisysParser.DateWrittenParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dateCompiledParagraph.
    def visitDateCompiledParagraph(self, ctx:CobolUnisysParser.DateCompiledParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#securityParagraph.
    def visitSecurityParagraph(self, ctx:CobolUnisysParser.SecurityParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#remarksParagraph.
    def visitRemarksParagraph(self, ctx:CobolUnisysParser.RemarksParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#environmentDivision.
    def visitEnvironmentDivision(self, ctx:CobolUnisysParser.EnvironmentDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#environmentDivisionBody.
    def visitEnvironmentDivisionBody(self, ctx:CobolUnisysParser.EnvironmentDivisionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#configurationSection.
    def visitConfigurationSection(self, ctx:CobolUnisysParser.ConfigurationSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#configurationSectionParagraph.
    def visitConfigurationSectionParagraph(self, ctx:CobolUnisysParser.ConfigurationSectionParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#sourceComputerParagraph.
    def visitSourceComputerParagraph(self, ctx:CobolUnisysParser.SourceComputerParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#objectComputerParagraph.
    def visitObjectComputerParagraph(self, ctx:CobolUnisysParser.ObjectComputerParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#objectComputerClause.
    def visitObjectComputerClause(self, ctx:CobolUnisysParser.ObjectComputerClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#memorySizeClause.
    def visitMemorySizeClause(self, ctx:CobolUnisysParser.MemorySizeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#diskSizeClause.
    def visitDiskSizeClause(self, ctx:CobolUnisysParser.DiskSizeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#collatingSequenceClause.
    def visitCollatingSequenceClause(self, ctx:CobolUnisysParser.CollatingSequenceClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#collatingSequenceClauseAlphanumeric.
    def visitCollatingSequenceClauseAlphanumeric(self, ctx:CobolUnisysParser.CollatingSequenceClauseAlphanumericContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#collatingSequenceClauseNational.
    def visitCollatingSequenceClauseNational(self, ctx:CobolUnisysParser.CollatingSequenceClauseNationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#segmentLimitClause.
    def visitSegmentLimitClause(self, ctx:CobolUnisysParser.SegmentLimitClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#characterSetClause.
    def visitCharacterSetClause(self, ctx:CobolUnisysParser.CharacterSetClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#specialNamesParagraph.
    def visitSpecialNamesParagraph(self, ctx:CobolUnisysParser.SpecialNamesParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#specialNameClause.
    def visitSpecialNameClause(self, ctx:CobolUnisysParser.SpecialNameClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#alphabetClause.
    def visitAlphabetClause(self, ctx:CobolUnisysParser.AlphabetClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#alphabetClauseFormat1.
    def visitAlphabetClauseFormat1(self, ctx:CobolUnisysParser.AlphabetClauseFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#alphabetLiterals.
    def visitAlphabetLiterals(self, ctx:CobolUnisysParser.AlphabetLiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#alphabetThrough.
    def visitAlphabetThrough(self, ctx:CobolUnisysParser.AlphabetThroughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#alphabetAlso.
    def visitAlphabetAlso(self, ctx:CobolUnisysParser.AlphabetAlsoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#alphabetClauseFormat2.
    def visitAlphabetClauseFormat2(self, ctx:CobolUnisysParser.AlphabetClauseFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#channelClause.
    def visitChannelClause(self, ctx:CobolUnisysParser.ChannelClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#classClause.
    def visitClassClause(self, ctx:CobolUnisysParser.ClassClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#classClauseThrough.
    def visitClassClauseThrough(self, ctx:CobolUnisysParser.ClassClauseThroughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#classClauseFrom.
    def visitClassClauseFrom(self, ctx:CobolUnisysParser.ClassClauseFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#classClauseTo.
    def visitClassClauseTo(self, ctx:CobolUnisysParser.ClassClauseToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#currencySignClause.
    def visitCurrencySignClause(self, ctx:CobolUnisysParser.CurrencySignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#decimalPointClause.
    def visitDecimalPointClause(self, ctx:CobolUnisysParser.DecimalPointClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#defaultComputationalSignClause.
    def visitDefaultComputationalSignClause(self, ctx:CobolUnisysParser.DefaultComputationalSignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#defaultDisplaySignClause.
    def visitDefaultDisplaySignClause(self, ctx:CobolUnisysParser.DefaultDisplaySignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#environmentSwitchNameClause.
    def visitEnvironmentSwitchNameClause(self, ctx:CobolUnisysParser.EnvironmentSwitchNameClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#environmentSwitchNameSpecialNamesStatusPhrase.
    def visitEnvironmentSwitchNameSpecialNamesStatusPhrase(self, ctx:CobolUnisysParser.EnvironmentSwitchNameSpecialNamesStatusPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#odtClause.
    def visitOdtClause(self, ctx:CobolUnisysParser.OdtClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reserveNetworkClause.
    def visitReserveNetworkClause(self, ctx:CobolUnisysParser.ReserveNetworkClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#symbolicCharactersClause.
    def visitSymbolicCharactersClause(self, ctx:CobolUnisysParser.SymbolicCharactersClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#symbolicCharacters.
    def visitSymbolicCharacters(self, ctx:CobolUnisysParser.SymbolicCharactersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#inputOutputSection.
    def visitInputOutputSection(self, ctx:CobolUnisysParser.InputOutputSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#inputOutputSectionParagraph.
    def visitInputOutputSectionParagraph(self, ctx:CobolUnisysParser.InputOutputSectionParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#fileControlParagraph.
    def visitFileControlParagraph(self, ctx:CobolUnisysParser.FileControlParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#fileControlEntry.
    def visitFileControlEntry(self, ctx:CobolUnisysParser.FileControlEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#selectClause.
    def visitSelectClause(self, ctx:CobolUnisysParser.SelectClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#fileControlClause.
    def visitFileControlClause(self, ctx:CobolUnisysParser.FileControlClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#assignClause.
    def visitAssignClause(self, ctx:CobolUnisysParser.AssignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reserveClause.
    def visitReserveClause(self, ctx:CobolUnisysParser.ReserveClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#organizationClause.
    def visitOrganizationClause(self, ctx:CobolUnisysParser.OrganizationClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#paddingCharacterClause.
    def visitPaddingCharacterClause(self, ctx:CobolUnisysParser.PaddingCharacterClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#recordDelimiterClause.
    def visitRecordDelimiterClause(self, ctx:CobolUnisysParser.RecordDelimiterClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#accessModeClause.
    def visitAccessModeClause(self, ctx:CobolUnisysParser.AccessModeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#recordKeyClause.
    def visitRecordKeyClause(self, ctx:CobolUnisysParser.RecordKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#alternateRecordKeyClause.
    def visitAlternateRecordKeyClause(self, ctx:CobolUnisysParser.AlternateRecordKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#passwordClause.
    def visitPasswordClause(self, ctx:CobolUnisysParser.PasswordClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#fileStatusClause.
    def visitFileStatusClause(self, ctx:CobolUnisysParser.FileStatusClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#relativeKeyClause.
    def visitRelativeKeyClause(self, ctx:CobolUnisysParser.RelativeKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#ioControlParagraph.
    def visitIoControlParagraph(self, ctx:CobolUnisysParser.IoControlParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#ioControlClause.
    def visitIoControlClause(self, ctx:CobolUnisysParser.IoControlClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#rerunClause.
    def visitRerunClause(self, ctx:CobolUnisysParser.RerunClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#rerunEveryRecords.
    def visitRerunEveryRecords(self, ctx:CobolUnisysParser.RerunEveryRecordsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#rerunEveryOf.
    def visitRerunEveryOf(self, ctx:CobolUnisysParser.RerunEveryOfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#rerunEveryClock.
    def visitRerunEveryClock(self, ctx:CobolUnisysParser.RerunEveryClockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#sameClause.
    def visitSameClause(self, ctx:CobolUnisysParser.SameClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#multipleFileClause.
    def visitMultipleFileClause(self, ctx:CobolUnisysParser.MultipleFileClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#multipleFilePosition.
    def visitMultipleFilePosition(self, ctx:CobolUnisysParser.MultipleFilePositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#commitmentControlClause.
    def visitCommitmentControlClause(self, ctx:CobolUnisysParser.CommitmentControlClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataDivision.
    def visitDataDivision(self, ctx:CobolUnisysParser.DataDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataDivisionSection.
    def visitDataDivisionSection(self, ctx:CobolUnisysParser.DataDivisionSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#fileSection.
    def visitFileSection(self, ctx:CobolUnisysParser.FileSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#fileDescriptionEntry.
    def visitFileDescriptionEntry(self, ctx:CobolUnisysParser.FileDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#fileDescriptionEntryClause.
    def visitFileDescriptionEntryClause(self, ctx:CobolUnisysParser.FileDescriptionEntryClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#externalClause.
    def visitExternalClause(self, ctx:CobolUnisysParser.ExternalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#globalClause.
    def visitGlobalClause(self, ctx:CobolUnisysParser.GlobalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#blockContainsClause.
    def visitBlockContainsClause(self, ctx:CobolUnisysParser.BlockContainsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#blockContainsTo.
    def visitBlockContainsTo(self, ctx:CobolUnisysParser.BlockContainsToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#recordContainsClause.
    def visitRecordContainsClause(self, ctx:CobolUnisysParser.RecordContainsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#recordContainsClauseFormat1.
    def visitRecordContainsClauseFormat1(self, ctx:CobolUnisysParser.RecordContainsClauseFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#recordContainsClauseFormat2.
    def visitRecordContainsClauseFormat2(self, ctx:CobolUnisysParser.RecordContainsClauseFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#recordContainsClauseFormat3.
    def visitRecordContainsClauseFormat3(self, ctx:CobolUnisysParser.RecordContainsClauseFormat3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#recordContainsTo.
    def visitRecordContainsTo(self, ctx:CobolUnisysParser.RecordContainsToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#labelRecordsClause.
    def visitLabelRecordsClause(self, ctx:CobolUnisysParser.LabelRecordsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#valueOfClause.
    def visitValueOfClause(self, ctx:CobolUnisysParser.ValueOfClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#valuePair.
    def visitValuePair(self, ctx:CobolUnisysParser.ValuePairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataRecordsClause.
    def visitDataRecordsClause(self, ctx:CobolUnisysParser.DataRecordsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#linageClause.
    def visitLinageClause(self, ctx:CobolUnisysParser.LinageClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#linageAt.
    def visitLinageAt(self, ctx:CobolUnisysParser.LinageAtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#linageFootingAt.
    def visitLinageFootingAt(self, ctx:CobolUnisysParser.LinageFootingAtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#linageLinesAtTop.
    def visitLinageLinesAtTop(self, ctx:CobolUnisysParser.LinageLinesAtTopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#linageLinesAtBottom.
    def visitLinageLinesAtBottom(self, ctx:CobolUnisysParser.LinageLinesAtBottomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#recordingModeClause.
    def visitRecordingModeClause(self, ctx:CobolUnisysParser.RecordingModeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#modeStatement.
    def visitModeStatement(self, ctx:CobolUnisysParser.ModeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#codeSetClause.
    def visitCodeSetClause(self, ctx:CobolUnisysParser.CodeSetClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportClause.
    def visitReportClause(self, ctx:CobolUnisysParser.ReportClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataBaseSection.
    def visitDataBaseSection(self, ctx:CobolUnisysParser.DataBaseSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataBaseSectionEntry.
    def visitDataBaseSectionEntry(self, ctx:CobolUnisysParser.DataBaseSectionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataBaseDeclare.
    def visitDataBaseDeclare(self, ctx:CobolUnisysParser.DataBaseDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataBaseDatasetDeclare.
    def visitDataBaseDatasetDeclare(self, ctx:CobolUnisysParser.DataBaseDatasetDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#invokeClause.
    def visitInvokeClause(self, ctx:CobolUnisysParser.InvokeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#usingClause.
    def visitUsingClause(self, ctx:CobolUnisysParser.UsingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#workingStorageSection.
    def visitWorkingStorageSection(self, ctx:CobolUnisysParser.WorkingStorageSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#linkageSection.
    def visitLinkageSection(self, ctx:CobolUnisysParser.LinkageSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#communicationSection.
    def visitCommunicationSection(self, ctx:CobolUnisysParser.CommunicationSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#communicationDescriptionEntry.
    def visitCommunicationDescriptionEntry(self, ctx:CobolUnisysParser.CommunicationDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#communicationDescriptionEntryFormat1.
    def visitCommunicationDescriptionEntryFormat1(self, ctx:CobolUnisysParser.CommunicationDescriptionEntryFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#communicationDescriptionEntryFormat2.
    def visitCommunicationDescriptionEntryFormat2(self, ctx:CobolUnisysParser.CommunicationDescriptionEntryFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#communicationDescriptionEntryFormat3.
    def visitCommunicationDescriptionEntryFormat3(self, ctx:CobolUnisysParser.CommunicationDescriptionEntryFormat3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#communicationDescriptionEntryFormat4.
    def visitCommunicationDescriptionEntryFormat4(self, ctx:CobolUnisysParser.CommunicationDescriptionEntryFormat4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#communicationAttribute.
    def visitCommunicationAttribute(self, ctx:CobolUnisysParser.CommunicationAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#communicationIoHeader.
    def visitCommunicationIoHeader(self, ctx:CobolUnisysParser.CommunicationIoHeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#conversationClause.
    def visitConversationClause(self, ctx:CobolUnisysParser.ConversationClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#destinationCountClause.
    def visitDestinationCountClause(self, ctx:CobolUnisysParser.DestinationCountClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#destinationTableClause.
    def visitDestinationTableClause(self, ctx:CobolUnisysParser.DestinationTableClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#endKeyClause.
    def visitEndKeyClause(self, ctx:CobolUnisysParser.EndKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#errorKeyClause.
    def visitErrorKeyClause(self, ctx:CobolUnisysParser.ErrorKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#messageCountClause.
    def visitMessageCountClause(self, ctx:CobolUnisysParser.MessageCountClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#messageDateClause.
    def visitMessageDateClause(self, ctx:CobolUnisysParser.MessageDateClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#messageTimeClause.
    def visitMessageTimeClause(self, ctx:CobolUnisysParser.MessageTimeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#statusKeyClause.
    def visitStatusKeyClause(self, ctx:CobolUnisysParser.StatusKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#symbolicDestinationClause.
    def visitSymbolicDestinationClause(self, ctx:CobolUnisysParser.SymbolicDestinationClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#symbolicQueueClause.
    def visitSymbolicQueueClause(self, ctx:CobolUnisysParser.SymbolicQueueClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#symbolicSourceClause.
    def visitSymbolicSourceClause(self, ctx:CobolUnisysParser.SymbolicSourceClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#symbolicTerminalClause.
    def visitSymbolicTerminalClause(self, ctx:CobolUnisysParser.SymbolicTerminalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#symbolicSubQueueClause.
    def visitSymbolicSubQueueClause(self, ctx:CobolUnisysParser.SymbolicSubQueueClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#textLengthClause.
    def visitTextLengthClause(self, ctx:CobolUnisysParser.TextLengthClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#localStorageSection.
    def visitLocalStorageSection(self, ctx:CobolUnisysParser.LocalStorageSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenSection.
    def visitScreenSection(self, ctx:CobolUnisysParser.ScreenSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionEntry.
    def visitScreenDescriptionEntry(self, ctx:CobolUnisysParser.ScreenDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionBlankClause.
    def visitScreenDescriptionBlankClause(self, ctx:CobolUnisysParser.ScreenDescriptionBlankClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionBellClause.
    def visitScreenDescriptionBellClause(self, ctx:CobolUnisysParser.ScreenDescriptionBellClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionBlinkClause.
    def visitScreenDescriptionBlinkClause(self, ctx:CobolUnisysParser.ScreenDescriptionBlinkClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionEraseClause.
    def visitScreenDescriptionEraseClause(self, ctx:CobolUnisysParser.ScreenDescriptionEraseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionLightClause.
    def visitScreenDescriptionLightClause(self, ctx:CobolUnisysParser.ScreenDescriptionLightClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionGridClause.
    def visitScreenDescriptionGridClause(self, ctx:CobolUnisysParser.ScreenDescriptionGridClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionReverseVideoClause.
    def visitScreenDescriptionReverseVideoClause(self, ctx:CobolUnisysParser.ScreenDescriptionReverseVideoClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionUnderlineClause.
    def visitScreenDescriptionUnderlineClause(self, ctx:CobolUnisysParser.ScreenDescriptionUnderlineClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionSizeClause.
    def visitScreenDescriptionSizeClause(self, ctx:CobolUnisysParser.ScreenDescriptionSizeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionLineClause.
    def visitScreenDescriptionLineClause(self, ctx:CobolUnisysParser.ScreenDescriptionLineClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionColumnClause.
    def visitScreenDescriptionColumnClause(self, ctx:CobolUnisysParser.ScreenDescriptionColumnClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionForegroundColorClause.
    def visitScreenDescriptionForegroundColorClause(self, ctx:CobolUnisysParser.ScreenDescriptionForegroundColorClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionBackgroundColorClause.
    def visitScreenDescriptionBackgroundColorClause(self, ctx:CobolUnisysParser.ScreenDescriptionBackgroundColorClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionControlClause.
    def visitScreenDescriptionControlClause(self, ctx:CobolUnisysParser.ScreenDescriptionControlClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionValueClause.
    def visitScreenDescriptionValueClause(self, ctx:CobolUnisysParser.ScreenDescriptionValueClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionPictureClause.
    def visitScreenDescriptionPictureClause(self, ctx:CobolUnisysParser.ScreenDescriptionPictureClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionFromClause.
    def visitScreenDescriptionFromClause(self, ctx:CobolUnisysParser.ScreenDescriptionFromClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionToClause.
    def visitScreenDescriptionToClause(self, ctx:CobolUnisysParser.ScreenDescriptionToClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionUsingClause.
    def visitScreenDescriptionUsingClause(self, ctx:CobolUnisysParser.ScreenDescriptionUsingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionUsageClause.
    def visitScreenDescriptionUsageClause(self, ctx:CobolUnisysParser.ScreenDescriptionUsageClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionBlankWhenZeroClause.
    def visitScreenDescriptionBlankWhenZeroClause(self, ctx:CobolUnisysParser.ScreenDescriptionBlankWhenZeroClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionJustifiedClause.
    def visitScreenDescriptionJustifiedClause(self, ctx:CobolUnisysParser.ScreenDescriptionJustifiedClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionSignClause.
    def visitScreenDescriptionSignClause(self, ctx:CobolUnisysParser.ScreenDescriptionSignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionAutoClause.
    def visitScreenDescriptionAutoClause(self, ctx:CobolUnisysParser.ScreenDescriptionAutoClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionSecureClause.
    def visitScreenDescriptionSecureClause(self, ctx:CobolUnisysParser.ScreenDescriptionSecureClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionRequiredClause.
    def visitScreenDescriptionRequiredClause(self, ctx:CobolUnisysParser.ScreenDescriptionRequiredClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionPromptClause.
    def visitScreenDescriptionPromptClause(self, ctx:CobolUnisysParser.ScreenDescriptionPromptClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionPromptOccursClause.
    def visitScreenDescriptionPromptOccursClause(self, ctx:CobolUnisysParser.ScreenDescriptionPromptOccursClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionFullClause.
    def visitScreenDescriptionFullClause(self, ctx:CobolUnisysParser.ScreenDescriptionFullClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionZeroFillClause.
    def visitScreenDescriptionZeroFillClause(self, ctx:CobolUnisysParser.ScreenDescriptionZeroFillClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportSection.
    def visitReportSection(self, ctx:CobolUnisysParser.ReportSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportDescription.
    def visitReportDescription(self, ctx:CobolUnisysParser.ReportDescriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportDescriptionEntry.
    def visitReportDescriptionEntry(self, ctx:CobolUnisysParser.ReportDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportDescriptionGlobalClause.
    def visitReportDescriptionGlobalClause(self, ctx:CobolUnisysParser.ReportDescriptionGlobalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportDescriptionPageLimitClause.
    def visitReportDescriptionPageLimitClause(self, ctx:CobolUnisysParser.ReportDescriptionPageLimitClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportDescriptionHeadingClause.
    def visitReportDescriptionHeadingClause(self, ctx:CobolUnisysParser.ReportDescriptionHeadingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportDescriptionFirstDetailClause.
    def visitReportDescriptionFirstDetailClause(self, ctx:CobolUnisysParser.ReportDescriptionFirstDetailClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportDescriptionLastDetailClause.
    def visitReportDescriptionLastDetailClause(self, ctx:CobolUnisysParser.ReportDescriptionLastDetailClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportDescriptionFootingClause.
    def visitReportDescriptionFootingClause(self, ctx:CobolUnisysParser.ReportDescriptionFootingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportGroupDescriptionEntry.
    def visitReportGroupDescriptionEntry(self, ctx:CobolUnisysParser.ReportGroupDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportGroupDescriptionEntryFormat1.
    def visitReportGroupDescriptionEntryFormat1(self, ctx:CobolUnisysParser.ReportGroupDescriptionEntryFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportGroupDescriptionEntryFormat2.
    def visitReportGroupDescriptionEntryFormat2(self, ctx:CobolUnisysParser.ReportGroupDescriptionEntryFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportGroupDescriptionEntryFormat3.
    def visitReportGroupDescriptionEntryFormat3(self, ctx:CobolUnisysParser.ReportGroupDescriptionEntryFormat3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportGroupBlankWhenZeroClause.
    def visitReportGroupBlankWhenZeroClause(self, ctx:CobolUnisysParser.ReportGroupBlankWhenZeroClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportGroupColumnNumberClause.
    def visitReportGroupColumnNumberClause(self, ctx:CobolUnisysParser.ReportGroupColumnNumberClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportGroupIndicateClause.
    def visitReportGroupIndicateClause(self, ctx:CobolUnisysParser.ReportGroupIndicateClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportGroupJustifiedClause.
    def visitReportGroupJustifiedClause(self, ctx:CobolUnisysParser.ReportGroupJustifiedClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportGroupLineNumberClause.
    def visitReportGroupLineNumberClause(self, ctx:CobolUnisysParser.ReportGroupLineNumberClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportGroupLineNumberNextPage.
    def visitReportGroupLineNumberNextPage(self, ctx:CobolUnisysParser.ReportGroupLineNumberNextPageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportGroupLineNumberPlus.
    def visitReportGroupLineNumberPlus(self, ctx:CobolUnisysParser.ReportGroupLineNumberPlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportGroupNextGroupClause.
    def visitReportGroupNextGroupClause(self, ctx:CobolUnisysParser.ReportGroupNextGroupClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportGroupNextGroupPlus.
    def visitReportGroupNextGroupPlus(self, ctx:CobolUnisysParser.ReportGroupNextGroupPlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportGroupNextGroupNextPage.
    def visitReportGroupNextGroupNextPage(self, ctx:CobolUnisysParser.ReportGroupNextGroupNextPageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportGroupPictureClause.
    def visitReportGroupPictureClause(self, ctx:CobolUnisysParser.ReportGroupPictureClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportGroupResetClause.
    def visitReportGroupResetClause(self, ctx:CobolUnisysParser.ReportGroupResetClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportGroupSignClause.
    def visitReportGroupSignClause(self, ctx:CobolUnisysParser.ReportGroupSignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportGroupSourceClause.
    def visitReportGroupSourceClause(self, ctx:CobolUnisysParser.ReportGroupSourceClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportGroupSumClause.
    def visitReportGroupSumClause(self, ctx:CobolUnisysParser.ReportGroupSumClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportGroupTypeClause.
    def visitReportGroupTypeClause(self, ctx:CobolUnisysParser.ReportGroupTypeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportGroupTypeReportHeading.
    def visitReportGroupTypeReportHeading(self, ctx:CobolUnisysParser.ReportGroupTypeReportHeadingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportGroupTypePageHeading.
    def visitReportGroupTypePageHeading(self, ctx:CobolUnisysParser.ReportGroupTypePageHeadingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportGroupTypeControlHeading.
    def visitReportGroupTypeControlHeading(self, ctx:CobolUnisysParser.ReportGroupTypeControlHeadingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportGroupTypeDetail.
    def visitReportGroupTypeDetail(self, ctx:CobolUnisysParser.ReportGroupTypeDetailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportGroupTypeControlFooting.
    def visitReportGroupTypeControlFooting(self, ctx:CobolUnisysParser.ReportGroupTypeControlFootingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportGroupUsageClause.
    def visitReportGroupUsageClause(self, ctx:CobolUnisysParser.ReportGroupUsageClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportGroupTypePageFooting.
    def visitReportGroupTypePageFooting(self, ctx:CobolUnisysParser.ReportGroupTypePageFootingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportGroupTypeReportFooting.
    def visitReportGroupTypeReportFooting(self, ctx:CobolUnisysParser.ReportGroupTypeReportFootingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportGroupValueClause.
    def visitReportGroupValueClause(self, ctx:CobolUnisysParser.ReportGroupValueClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#programLibrarySection.
    def visitProgramLibrarySection(self, ctx:CobolUnisysParser.ProgramLibrarySectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#libraryDescriptionEntry.
    def visitLibraryDescriptionEntry(self, ctx:CobolUnisysParser.LibraryDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#libraryDescriptionEntryFormat1.
    def visitLibraryDescriptionEntryFormat1(self, ctx:CobolUnisysParser.LibraryDescriptionEntryFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#libraryDescriptionEntryFormat2.
    def visitLibraryDescriptionEntryFormat2(self, ctx:CobolUnisysParser.LibraryDescriptionEntryFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#libraryAttributeClauseFormat1.
    def visitLibraryAttributeClauseFormat1(self, ctx:CobolUnisysParser.LibraryAttributeClauseFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#libraryAttributeClauseFormat2.
    def visitLibraryAttributeClauseFormat2(self, ctx:CobolUnisysParser.LibraryAttributeClauseFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#libraryAttributeFunction.
    def visitLibraryAttributeFunction(self, ctx:CobolUnisysParser.LibraryAttributeFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#libraryAttributeParameter.
    def visitLibraryAttributeParameter(self, ctx:CobolUnisysParser.LibraryAttributeParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#libraryAttributeTitle.
    def visitLibraryAttributeTitle(self, ctx:CobolUnisysParser.LibraryAttributeTitleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#libraryEntryProcedureClauseFormat1.
    def visitLibraryEntryProcedureClauseFormat1(self, ctx:CobolUnisysParser.LibraryEntryProcedureClauseFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#libraryEntryProcedureClauseFormat2.
    def visitLibraryEntryProcedureClauseFormat2(self, ctx:CobolUnisysParser.LibraryEntryProcedureClauseFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#libraryEntryProcedureForClause.
    def visitLibraryEntryProcedureForClause(self, ctx:CobolUnisysParser.LibraryEntryProcedureForClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#libraryEntryProcedureGivingClause.
    def visitLibraryEntryProcedureGivingClause(self, ctx:CobolUnisysParser.LibraryEntryProcedureGivingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#libraryEntryProcedureUsingClause.
    def visitLibraryEntryProcedureUsingClause(self, ctx:CobolUnisysParser.LibraryEntryProcedureUsingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#libraryEntryProcedureUsingName.
    def visitLibraryEntryProcedureUsingName(self, ctx:CobolUnisysParser.LibraryEntryProcedureUsingNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#libraryEntryProcedureWithClause.
    def visitLibraryEntryProcedureWithClause(self, ctx:CobolUnisysParser.LibraryEntryProcedureWithClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#libraryEntryProcedureWithName.
    def visitLibraryEntryProcedureWithName(self, ctx:CobolUnisysParser.LibraryEntryProcedureWithNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#libraryIsCommonClause.
    def visitLibraryIsCommonClause(self, ctx:CobolUnisysParser.LibraryIsCommonClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#libraryIsGlobalClause.
    def visitLibraryIsGlobalClause(self, ctx:CobolUnisysParser.LibraryIsGlobalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataDescriptionEntry.
    def visitDataDescriptionEntry(self, ctx:CobolUnisysParser.DataDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#copyStatement.
    def visitCopyStatement(self, ctx:CobolUnisysParser.CopyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#copySource.
    def visitCopySource(self, ctx:CobolUnisysParser.CopySourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#copyLibrary.
    def visitCopyLibrary(self, ctx:CobolUnisysParser.CopyLibraryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#replacingPhrase.
    def visitReplacingPhrase(self, ctx:CobolUnisysParser.ReplacingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#changeStatement.
    def visitChangeStatement(self, ctx:CobolUnisysParser.ChangeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#changeFileAttribute.
    def visitChangeFileAttribute(self, ctx:CobolUnisysParser.ChangeFileAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#changeLibraryAttribute.
    def visitChangeLibraryAttribute(self, ctx:CobolUnisysParser.ChangeLibraryAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#libraryAttributeName.
    def visitLibraryAttributeName(self, ctx:CobolUnisysParser.LibraryAttributeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#libraryValueOption.
    def visitLibraryValueOption(self, ctx:CobolUnisysParser.LibraryValueOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#toValueOption.
    def visitToValueOption(self, ctx:CobolUnisysParser.ToValueOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#createStatement.
    def visitCreateStatement(self, ctx:CobolUnisysParser.CreateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#replaceOffStatement.
    def visitReplaceOffStatement(self, ctx:CobolUnisysParser.ReplaceOffStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#replaceClause.
    def visitReplaceClause(self, ctx:CobolUnisysParser.ReplaceClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#directoryPhrase.
    def visitDirectoryPhrase(self, ctx:CobolUnisysParser.DirectoryPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#familyPhrase.
    def visitFamilyPhrase(self, ctx:CobolUnisysParser.FamilyPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#replaceable.
    def visitReplaceable(self, ctx:CobolUnisysParser.ReplaceableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#replacement.
    def visitReplacement(self, ctx:CobolUnisysParser.ReplacementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#ejectStatement.
    def visitEjectStatement(self, ctx:CobolUnisysParser.EjectStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#skipStatement.
    def visitSkipStatement(self, ctx:CobolUnisysParser.SkipStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#titleStatement.
    def visitTitleStatement(self, ctx:CobolUnisysParser.TitleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#pseudoText.
    def visitPseudoText(self, ctx:CobolUnisysParser.PseudoTextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#charData.
    def visitCharData(self, ctx:CobolUnisysParser.CharDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#charDataSql.
    def visitCharDataSql(self, ctx:CobolUnisysParser.CharDataSqlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#charDataLine.
    def visitCharDataLine(self, ctx:CobolUnisysParser.CharDataLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#cobolWord.
    def visitCobolWord(self, ctx:CobolUnisysParser.CobolWordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#literal.
    def visitLiteral(self, ctx:CobolUnisysParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#jpEncodingText.
    def visitJpEncodingText(self, ctx:CobolUnisysParser.JpEncodingTextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#filename.
    def visitFilename(self, ctx:CobolUnisysParser.FilenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataDescriptionEntryFormat1.
    def visitDataDescriptionEntryFormat1(self, ctx:CobolUnisysParser.DataDescriptionEntryFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataDescriptionEntryFormat2.
    def visitDataDescriptionEntryFormat2(self, ctx:CobolUnisysParser.DataDescriptionEntryFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataDescriptionEntryFormat3.
    def visitDataDescriptionEntryFormat3(self, ctx:CobolUnisysParser.DataDescriptionEntryFormat3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataDescriptionEntryExecSql.
    def visitDataDescriptionEntryExecSql(self, ctx:CobolUnisysParser.DataDescriptionEntryExecSqlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataAlignedClause.
    def visitDataAlignedClause(self, ctx:CobolUnisysParser.DataAlignedClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataBlankWhenZeroClause.
    def visitDataBlankWhenZeroClause(self, ctx:CobolUnisysParser.DataBlankWhenZeroClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataCommonOwnLocalClause.
    def visitDataCommonOwnLocalClause(self, ctx:CobolUnisysParser.DataCommonOwnLocalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataExternalClause.
    def visitDataExternalClause(self, ctx:CobolUnisysParser.DataExternalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataGlobalClause.
    def visitDataGlobalClause(self, ctx:CobolUnisysParser.DataGlobalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataIntegerStringClause.
    def visitDataIntegerStringClause(self, ctx:CobolUnisysParser.DataIntegerStringClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataJustifiedClause.
    def visitDataJustifiedClause(self, ctx:CobolUnisysParser.DataJustifiedClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataOccursClause.
    def visitDataOccursClause(self, ctx:CobolUnisysParser.DataOccursClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataOccursTo.
    def visitDataOccursTo(self, ctx:CobolUnisysParser.DataOccursToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataOccursSort.
    def visitDataOccursSort(self, ctx:CobolUnisysParser.DataOccursSortContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataPictureClause.
    def visitDataPictureClause(self, ctx:CobolUnisysParser.DataPictureClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#pictureString.
    def visitPictureString(self, ctx:CobolUnisysParser.PictureStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#pictureChars.
    def visitPictureChars(self, ctx:CobolUnisysParser.PictureCharsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#pictureCardinality.
    def visitPictureCardinality(self, ctx:CobolUnisysParser.PictureCardinalityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataReceivedByClause.
    def visitDataReceivedByClause(self, ctx:CobolUnisysParser.DataReceivedByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataRecordAreaClause.
    def visitDataRecordAreaClause(self, ctx:CobolUnisysParser.DataRecordAreaClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataRedefinesClause.
    def visitDataRedefinesClause(self, ctx:CobolUnisysParser.DataRedefinesClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataRenamesClause.
    def visitDataRenamesClause(self, ctx:CobolUnisysParser.DataRenamesClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataSignClause.
    def visitDataSignClause(self, ctx:CobolUnisysParser.DataSignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataSynchronizedClause.
    def visitDataSynchronizedClause(self, ctx:CobolUnisysParser.DataSynchronizedClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataThreadLocalClause.
    def visitDataThreadLocalClause(self, ctx:CobolUnisysParser.DataThreadLocalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataTypeClause.
    def visitDataTypeClause(self, ctx:CobolUnisysParser.DataTypeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataTypeDefClause.
    def visitDataTypeDefClause(self, ctx:CobolUnisysParser.DataTypeDefClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataUsageClause.
    def visitDataUsageClause(self, ctx:CobolUnisysParser.DataUsageClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataUsingClause.
    def visitDataUsingClause(self, ctx:CobolUnisysParser.DataUsingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataValueClause.
    def visitDataValueClause(self, ctx:CobolUnisysParser.DataValueClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataValueInterval.
    def visitDataValueInterval(self, ctx:CobolUnisysParser.DataValueIntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataValueIntervalFrom.
    def visitDataValueIntervalFrom(self, ctx:CobolUnisysParser.DataValueIntervalFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataValueIntervalTo.
    def visitDataValueIntervalTo(self, ctx:CobolUnisysParser.DataValueIntervalToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataWithLowerBoundsClause.
    def visitDataWithLowerBoundsClause(self, ctx:CobolUnisysParser.DataWithLowerBoundsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#procedureDivision.
    def visitProcedureDivision(self, ctx:CobolUnisysParser.ProcedureDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#procedureDivisionUsingClause.
    def visitProcedureDivisionUsingClause(self, ctx:CobolUnisysParser.ProcedureDivisionUsingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#procedureDivisionGivingClause.
    def visitProcedureDivisionGivingClause(self, ctx:CobolUnisysParser.ProcedureDivisionGivingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#procedureDivisionUsingParameter.
    def visitProcedureDivisionUsingParameter(self, ctx:CobolUnisysParser.ProcedureDivisionUsingParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#procedureDivisionByReferencePhrase.
    def visitProcedureDivisionByReferencePhrase(self, ctx:CobolUnisysParser.ProcedureDivisionByReferencePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#procedureDivisionByReference.
    def visitProcedureDivisionByReference(self, ctx:CobolUnisysParser.ProcedureDivisionByReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#procedureDivisionByValuePhrase.
    def visitProcedureDivisionByValuePhrase(self, ctx:CobolUnisysParser.ProcedureDivisionByValuePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#procedureDivisionByValue.
    def visitProcedureDivisionByValue(self, ctx:CobolUnisysParser.ProcedureDivisionByValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#procedureDeclaratives.
    def visitProcedureDeclaratives(self, ctx:CobolUnisysParser.ProcedureDeclarativesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#procedureDeclarative.
    def visitProcedureDeclarative(self, ctx:CobolUnisysParser.ProcedureDeclarativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#procedureSectionHeader.
    def visitProcedureSectionHeader(self, ctx:CobolUnisysParser.ProcedureSectionHeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#procedureDivisionBody.
    def visitProcedureDivisionBody(self, ctx:CobolUnisysParser.ProcedureDivisionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#procedureSection.
    def visitProcedureSection(self, ctx:CobolUnisysParser.ProcedureSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#paragraphs.
    def visitParagraphs(self, ctx:CobolUnisysParser.ParagraphsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#paragraph.
    def visitParagraph(self, ctx:CobolUnisysParser.ParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#sentence.
    def visitSentence(self, ctx:CobolUnisysParser.SentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#statement.
    def visitStatement(self, ctx:CobolUnisysParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#execCicsStatement2.
    def visitExecCicsStatement2(self, ctx:CobolUnisysParser.ExecCicsStatement2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#acceptStatement.
    def visitAcceptStatement(self, ctx:CobolUnisysParser.AcceptStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#acceptFromDateStatement.
    def visitAcceptFromDateStatement(self, ctx:CobolUnisysParser.AcceptFromDateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#acceptFromDatePhrase.
    def visitAcceptFromDatePhrase(self, ctx:CobolUnisysParser.AcceptFromDatePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#acceptFromMnemonicStatement.
    def visitAcceptFromMnemonicStatement(self, ctx:CobolUnisysParser.AcceptFromMnemonicStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#acceptFromEscapeKeyStatement.
    def visitAcceptFromEscapeKeyStatement(self, ctx:CobolUnisysParser.AcceptFromEscapeKeyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#acceptMessageCountStatement.
    def visitAcceptMessageCountStatement(self, ctx:CobolUnisysParser.AcceptMessageCountStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#addStatement.
    def visitAddStatement(self, ctx:CobolUnisysParser.AddStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#addToStatement.
    def visitAddToStatement(self, ctx:CobolUnisysParser.AddToStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#addToGivingStatement.
    def visitAddToGivingStatement(self, ctx:CobolUnisysParser.AddToGivingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#addCorrespondingStatement.
    def visitAddCorrespondingStatement(self, ctx:CobolUnisysParser.AddCorrespondingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#addFrom.
    def visitAddFrom(self, ctx:CobolUnisysParser.AddFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#addTo.
    def visitAddTo(self, ctx:CobolUnisysParser.AddToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#addToGiving.
    def visitAddToGiving(self, ctx:CobolUnisysParser.AddToGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#addGiving.
    def visitAddGiving(self, ctx:CobolUnisysParser.AddGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#alteredGoTo.
    def visitAlteredGoTo(self, ctx:CobolUnisysParser.AlteredGoToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#alterStatement.
    def visitAlterStatement(self, ctx:CobolUnisysParser.AlterStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#alterProceedTo.
    def visitAlterProceedTo(self, ctx:CobolUnisysParser.AlterProceedToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#attachStatement.
    def visitAttachStatement(self, ctx:CobolUnisysParser.AttachStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#callStatement.
    def visitCallStatement(self, ctx:CobolUnisysParser.CallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#callUsingPhrase.
    def visitCallUsingPhrase(self, ctx:CobolUnisysParser.CallUsingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#callUsingParameter.
    def visitCallUsingParameter(self, ctx:CobolUnisysParser.CallUsingParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#callByReferencePhrase.
    def visitCallByReferencePhrase(self, ctx:CobolUnisysParser.CallByReferencePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#callByReference.
    def visitCallByReference(self, ctx:CobolUnisysParser.CallByReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#callByValuePhrase.
    def visitCallByValuePhrase(self, ctx:CobolUnisysParser.CallByValuePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#callByValue.
    def visitCallByValue(self, ctx:CobolUnisysParser.CallByValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#callByContentPhrase.
    def visitCallByContentPhrase(self, ctx:CobolUnisysParser.CallByContentPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#callByContent.
    def visitCallByContent(self, ctx:CobolUnisysParser.CallByContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#callGivingPhrase.
    def visitCallGivingPhrase(self, ctx:CobolUnisysParser.CallGivingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#callSystem.
    def visitCallSystem(self, ctx:CobolUnisysParser.CallSystemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#cancelStatement.
    def visitCancelStatement(self, ctx:CobolUnisysParser.CancelStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#cancelCall.
    def visitCancelCall(self, ctx:CobolUnisysParser.CancelCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#closeStatement.
    def visitCloseStatement(self, ctx:CobolUnisysParser.CloseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#closePhrase.
    def visitClosePhrase(self, ctx:CobolUnisysParser.ClosePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#closeFile.
    def visitCloseFile(self, ctx:CobolUnisysParser.CloseFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#closeReelUnitStatement.
    def visitCloseReelUnitStatement(self, ctx:CobolUnisysParser.CloseReelUnitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#closeRelativeStatement.
    def visitCloseRelativeStatement(self, ctx:CobolUnisysParser.CloseRelativeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#closePortFileIOStatement.
    def visitClosePortFileIOStatement(self, ctx:CobolUnisysParser.ClosePortFileIOStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#closePortFileIOUsing.
    def visitClosePortFileIOUsing(self, ctx:CobolUnisysParser.ClosePortFileIOUsingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#closePortFileIOUsingCloseDisposition.
    def visitClosePortFileIOUsingCloseDisposition(self, ctx:CobolUnisysParser.ClosePortFileIOUsingCloseDispositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#closePortFileIOUsingAssociatedData.
    def visitClosePortFileIOUsingAssociatedData(self, ctx:CobolUnisysParser.ClosePortFileIOUsingAssociatedDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#closePortFileIOUsingAssociatedDataLength.
    def visitClosePortFileIOUsingAssociatedDataLength(self, ctx:CobolUnisysParser.ClosePortFileIOUsingAssociatedDataLengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#computeStatement.
    def visitComputeStatement(self, ctx:CobolUnisysParser.ComputeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#computeStore.
    def visitComputeStore(self, ctx:CobolUnisysParser.ComputeStoreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#continueStatement.
    def visitContinueStatement(self, ctx:CobolUnisysParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#continueIndicator.
    def visitContinueIndicator(self, ctx:CobolUnisysParser.ContinueIndicatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#deleteStatement.
    def visitDeleteStatement(self, ctx:CobolUnisysParser.DeleteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#disableStatement.
    def visitDisableStatement(self, ctx:CobolUnisysParser.DisableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#displayStatement.
    def visitDisplayStatement(self, ctx:CobolUnisysParser.DisplayStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#displayOperand.
    def visitDisplayOperand(self, ctx:CobolUnisysParser.DisplayOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#displayAt.
    def visitDisplayAt(self, ctx:CobolUnisysParser.DisplayAtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#displayUpon.
    def visitDisplayUpon(self, ctx:CobolUnisysParser.DisplayUponContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#displayWith.
    def visitDisplayWith(self, ctx:CobolUnisysParser.DisplayWithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#divideStatement.
    def visitDivideStatement(self, ctx:CobolUnisysParser.DivideStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#divideIntoStatement.
    def visitDivideIntoStatement(self, ctx:CobolUnisysParser.DivideIntoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#divideIntoGivingStatement.
    def visitDivideIntoGivingStatement(self, ctx:CobolUnisysParser.DivideIntoGivingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#divideByGivingStatement.
    def visitDivideByGivingStatement(self, ctx:CobolUnisysParser.DivideByGivingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#divideGivingPhrase.
    def visitDivideGivingPhrase(self, ctx:CobolUnisysParser.DivideGivingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#divideInto.
    def visitDivideInto(self, ctx:CobolUnisysParser.DivideIntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#divideGiving.
    def visitDivideGiving(self, ctx:CobolUnisysParser.DivideGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#divideRemainder.
    def visitDivideRemainder(self, ctx:CobolUnisysParser.DivideRemainderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#enableStatement.
    def visitEnableStatement(self, ctx:CobolUnisysParser.EnableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#entryStatement.
    def visitEntryStatement(self, ctx:CobolUnisysParser.EntryStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#evaluateStatement.
    def visitEvaluateStatement(self, ctx:CobolUnisysParser.EvaluateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#evaluateSelect.
    def visitEvaluateSelect(self, ctx:CobolUnisysParser.EvaluateSelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#evaluateAlsoSelect.
    def visitEvaluateAlsoSelect(self, ctx:CobolUnisysParser.EvaluateAlsoSelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#evaluateWhenPhrase.
    def visitEvaluateWhenPhrase(self, ctx:CobolUnisysParser.EvaluateWhenPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#evaluateWhen.
    def visitEvaluateWhen(self, ctx:CobolUnisysParser.EvaluateWhenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#evaluateCondition.
    def visitEvaluateCondition(self, ctx:CobolUnisysParser.EvaluateConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#evaluateThrough.
    def visitEvaluateThrough(self, ctx:CobolUnisysParser.EvaluateThroughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#evaluateAlsoCondition.
    def visitEvaluateAlsoCondition(self, ctx:CobolUnisysParser.EvaluateAlsoConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#evaluateWhenOther.
    def visitEvaluateWhenOther(self, ctx:CobolUnisysParser.EvaluateWhenOtherContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#evaluateValue.
    def visitEvaluateValue(self, ctx:CobolUnisysParser.EvaluateValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#execCicsStatement.
    def visitExecCicsStatement(self, ctx:CobolUnisysParser.ExecCicsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#execSqlStatement.
    def visitExecSqlStatement(self, ctx:CobolUnisysParser.ExecSqlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#execSqlImsStatement.
    def visitExecSqlImsStatement(self, ctx:CobolUnisysParser.ExecSqlImsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#exhibitStatement.
    def visitExhibitStatement(self, ctx:CobolUnisysParser.ExhibitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#exhibitOperand.
    def visitExhibitOperand(self, ctx:CobolUnisysParser.ExhibitOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#exitStatement.
    def visitExitStatement(self, ctx:CobolUnisysParser.ExitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#findStatement.
    def visitFindStatement(self, ctx:CobolUnisysParser.FindStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#viaClause.
    def visitViaClause(self, ctx:CobolUnisysParser.ViaClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#findOption.
    def visitFindOption(self, ctx:CobolUnisysParser.FindOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#freeStatement.
    def visitFreeStatement(self, ctx:CobolUnisysParser.FreeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#generateStatement.
    def visitGenerateStatement(self, ctx:CobolUnisysParser.GenerateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#gobackStatement.
    def visitGobackStatement(self, ctx:CobolUnisysParser.GobackStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#goToStatement.
    def visitGoToStatement(self, ctx:CobolUnisysParser.GoToStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#goToStatementSimple.
    def visitGoToStatementSimple(self, ctx:CobolUnisysParser.GoToStatementSimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#goToDependingOnStatement.
    def visitGoToDependingOnStatement(self, ctx:CobolUnisysParser.GoToDependingOnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#ifStatement.
    def visitIfStatement(self, ctx:CobolUnisysParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#ifThen.
    def visitIfThen(self, ctx:CobolUnisysParser.IfThenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#ifElse.
    def visitIfElse(self, ctx:CobolUnisysParser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#initializeStatement.
    def visitInitializeStatement(self, ctx:CobolUnisysParser.InitializeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#initializeReplacingPhrase.
    def visitInitializeReplacingPhrase(self, ctx:CobolUnisysParser.InitializeReplacingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#initializeReplacingBy.
    def visitInitializeReplacingBy(self, ctx:CobolUnisysParser.InitializeReplacingByContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#initiateStatement.
    def visitInitiateStatement(self, ctx:CobolUnisysParser.InitiateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#inspectStatement.
    def visitInspectStatement(self, ctx:CobolUnisysParser.InspectStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#inspectTallyingPhrase.
    def visitInspectTallyingPhrase(self, ctx:CobolUnisysParser.InspectTallyingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#inspectReplacingPhrase.
    def visitInspectReplacingPhrase(self, ctx:CobolUnisysParser.InspectReplacingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#inspectTallyingReplacingPhrase.
    def visitInspectTallyingReplacingPhrase(self, ctx:CobolUnisysParser.InspectTallyingReplacingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#inspectConvertingPhrase.
    def visitInspectConvertingPhrase(self, ctx:CobolUnisysParser.InspectConvertingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#inspectFor.
    def visitInspectFor(self, ctx:CobolUnisysParser.InspectForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#inspectCharacters.
    def visitInspectCharacters(self, ctx:CobolUnisysParser.InspectCharactersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#inspectReplacingCharacters.
    def visitInspectReplacingCharacters(self, ctx:CobolUnisysParser.InspectReplacingCharactersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#inspectAllLeadings.
    def visitInspectAllLeadings(self, ctx:CobolUnisysParser.InspectAllLeadingsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#inspectReplacingAllLeadings.
    def visitInspectReplacingAllLeadings(self, ctx:CobolUnisysParser.InspectReplacingAllLeadingsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#inspectAllLeading.
    def visitInspectAllLeading(self, ctx:CobolUnisysParser.InspectAllLeadingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#inspectReplacingAllLeading.
    def visitInspectReplacingAllLeading(self, ctx:CobolUnisysParser.InspectReplacingAllLeadingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#inspectBy.
    def visitInspectBy(self, ctx:CobolUnisysParser.InspectByContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#inspectTo.
    def visitInspectTo(self, ctx:CobolUnisysParser.InspectToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#inspectBeforeAfter.
    def visitInspectBeforeAfter(self, ctx:CobolUnisysParser.InspectBeforeAfterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#lockStatement.
    def visitLockStatement(self, ctx:CobolUnisysParser.LockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#mergeStatement.
    def visitMergeStatement(self, ctx:CobolUnisysParser.MergeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#mergeOnKeyClause.
    def visitMergeOnKeyClause(self, ctx:CobolUnisysParser.MergeOnKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#mergeCollatingSequencePhrase.
    def visitMergeCollatingSequencePhrase(self, ctx:CobolUnisysParser.MergeCollatingSequencePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#mergeCollatingAlphanumeric.
    def visitMergeCollatingAlphanumeric(self, ctx:CobolUnisysParser.MergeCollatingAlphanumericContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#mergeCollatingNational.
    def visitMergeCollatingNational(self, ctx:CobolUnisysParser.MergeCollatingNationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#mergeUsing.
    def visitMergeUsing(self, ctx:CobolUnisysParser.MergeUsingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#mergeOutputProcedurePhrase.
    def visitMergeOutputProcedurePhrase(self, ctx:CobolUnisysParser.MergeOutputProcedurePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#mergeOutputThrough.
    def visitMergeOutputThrough(self, ctx:CobolUnisysParser.MergeOutputThroughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#mergeGivingPhrase.
    def visitMergeGivingPhrase(self, ctx:CobolUnisysParser.MergeGivingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#mergeGiving.
    def visitMergeGiving(self, ctx:CobolUnisysParser.MergeGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#moveStatement.
    def visitMoveStatement(self, ctx:CobolUnisysParser.MoveStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#moveToStatement.
    def visitMoveToStatement(self, ctx:CobolUnisysParser.MoveToStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#moveToSendingArea.
    def visitMoveToSendingArea(self, ctx:CobolUnisysParser.MoveToSendingAreaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#moveCorrespondingToStatement.
    def visitMoveCorrespondingToStatement(self, ctx:CobolUnisysParser.MoveCorrespondingToStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#moveCorrespondingToSendingArea.
    def visitMoveCorrespondingToSendingArea(self, ctx:CobolUnisysParser.MoveCorrespondingToSendingAreaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#moveAttributeClause.
    def visitMoveAttributeClause(self, ctx:CobolUnisysParser.MoveAttributeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#modifyStatement.
    def visitModifyStatement(self, ctx:CobolUnisysParser.ModifyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#modifyTo.
    def visitModifyTo(self, ctx:CobolUnisysParser.ModifyToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#modifyOption.
    def visitModifyOption(self, ctx:CobolUnisysParser.ModifyOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#multiplyStatement.
    def visitMultiplyStatement(self, ctx:CobolUnisysParser.MultiplyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#multiplyRegular.
    def visitMultiplyRegular(self, ctx:CobolUnisysParser.MultiplyRegularContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#multiplyRegularOperand.
    def visitMultiplyRegularOperand(self, ctx:CobolUnisysParser.MultiplyRegularOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#multiplyGiving.
    def visitMultiplyGiving(self, ctx:CobolUnisysParser.MultiplyGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#multiplyGivingOperand.
    def visitMultiplyGivingOperand(self, ctx:CobolUnisysParser.MultiplyGivingOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#multiplyGivingResult.
    def visitMultiplyGivingResult(self, ctx:CobolUnisysParser.MultiplyGivingResultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#openStatement.
    def visitOpenStatement(self, ctx:CobolUnisysParser.OpenStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#openInputStatement.
    def visitOpenInputStatement(self, ctx:CobolUnisysParser.OpenInputStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#openInput.
    def visitOpenInput(self, ctx:CobolUnisysParser.OpenInputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#openUpdateStatement.
    def visitOpenUpdateStatement(self, ctx:CobolUnisysParser.OpenUpdateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#openOutputStatement.
    def visitOpenOutputStatement(self, ctx:CobolUnisysParser.OpenOutputStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#openOutput.
    def visitOpenOutput(self, ctx:CobolUnisysParser.OpenOutputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#openIOStatement.
    def visitOpenIOStatement(self, ctx:CobolUnisysParser.OpenIOStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#openInquiry.
    def visitOpenInquiry(self, ctx:CobolUnisysParser.OpenInquiryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#openExtendStatement.
    def visitOpenExtendStatement(self, ctx:CobolUnisysParser.OpenExtendStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#performStatement.
    def visitPerformStatement(self, ctx:CobolUnisysParser.PerformStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#performInlineStatement.
    def visitPerformInlineStatement(self, ctx:CobolUnisysParser.PerformInlineStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#performProcedureStatement.
    def visitPerformProcedureStatement(self, ctx:CobolUnisysParser.PerformProcedureStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#performType.
    def visitPerformType(self, ctx:CobolUnisysParser.PerformTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#performTimes.
    def visitPerformTimes(self, ctx:CobolUnisysParser.PerformTimesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#performUntil.
    def visitPerformUntil(self, ctx:CobolUnisysParser.PerformUntilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#performVarying.
    def visitPerformVarying(self, ctx:CobolUnisysParser.PerformVaryingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#performVaryingClause.
    def visitPerformVaryingClause(self, ctx:CobolUnisysParser.PerformVaryingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#performVaryingPhrase.
    def visitPerformVaryingPhrase(self, ctx:CobolUnisysParser.PerformVaryingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#performAfter.
    def visitPerformAfter(self, ctx:CobolUnisysParser.PerformAfterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#performFrom.
    def visitPerformFrom(self, ctx:CobolUnisysParser.PerformFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#performBy.
    def visitPerformBy(self, ctx:CobolUnisysParser.PerformByContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#performTestClause.
    def visitPerformTestClause(self, ctx:CobolUnisysParser.PerformTestClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#purgeStatement.
    def visitPurgeStatement(self, ctx:CobolUnisysParser.PurgeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#readStatement.
    def visitReadStatement(self, ctx:CobolUnisysParser.ReadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#readInto.
    def visitReadInto(self, ctx:CobolUnisysParser.ReadIntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#readWith.
    def visitReadWith(self, ctx:CobolUnisysParser.ReadWithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#readKey.
    def visitReadKey(self, ctx:CobolUnisysParser.ReadKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#receiveStatement.
    def visitReceiveStatement(self, ctx:CobolUnisysParser.ReceiveStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#receiveFromStatement.
    def visitReceiveFromStatement(self, ctx:CobolUnisysParser.ReceiveFromStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#receiveFrom.
    def visitReceiveFrom(self, ctx:CobolUnisysParser.ReceiveFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#receiveIntoStatement.
    def visitReceiveIntoStatement(self, ctx:CobolUnisysParser.ReceiveIntoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#receiveNoData.
    def visitReceiveNoData(self, ctx:CobolUnisysParser.ReceiveNoDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#receiveWithData.
    def visitReceiveWithData(self, ctx:CobolUnisysParser.ReceiveWithDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#receiveBefore.
    def visitReceiveBefore(self, ctx:CobolUnisysParser.ReceiveBeforeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#receiveWith.
    def visitReceiveWith(self, ctx:CobolUnisysParser.ReceiveWithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#receiveThread.
    def visitReceiveThread(self, ctx:CobolUnisysParser.ReceiveThreadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#receiveSize.
    def visitReceiveSize(self, ctx:CobolUnisysParser.ReceiveSizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#receiveStatus.
    def visitReceiveStatus(self, ctx:CobolUnisysParser.ReceiveStatusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#releaseStatement.
    def visitReleaseStatement(self, ctx:CobolUnisysParser.ReleaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#returnStatement.
    def visitReturnStatement(self, ctx:CobolUnisysParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#returnInto.
    def visitReturnInto(self, ctx:CobolUnisysParser.ReturnIntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#rewriteStatement.
    def visitRewriteStatement(self, ctx:CobolUnisysParser.RewriteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#rewriteFrom.
    def visitRewriteFrom(self, ctx:CobolUnisysParser.RewriteFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#searchStatement.
    def visitSearchStatement(self, ctx:CobolUnisysParser.SearchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#searchVarying.
    def visitSearchVarying(self, ctx:CobolUnisysParser.SearchVaryingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#searchWhen.
    def visitSearchWhen(self, ctx:CobolUnisysParser.SearchWhenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#sendStatement.
    def visitSendStatement(self, ctx:CobolUnisysParser.SendStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#sendStatementSync.
    def visitSendStatementSync(self, ctx:CobolUnisysParser.SendStatementSyncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#sendStatementAsync.
    def visitSendStatementAsync(self, ctx:CobolUnisysParser.SendStatementAsyncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#sendFromPhrase.
    def visitSendFromPhrase(self, ctx:CobolUnisysParser.SendFromPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#sendWithPhrase.
    def visitSendWithPhrase(self, ctx:CobolUnisysParser.SendWithPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#sendReplacingPhrase.
    def visitSendReplacingPhrase(self, ctx:CobolUnisysParser.SendReplacingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#sendAdvancingPhrase.
    def visitSendAdvancingPhrase(self, ctx:CobolUnisysParser.SendAdvancingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#sendAdvancingPage.
    def visitSendAdvancingPage(self, ctx:CobolUnisysParser.SendAdvancingPageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#sendAdvancingLines.
    def visitSendAdvancingLines(self, ctx:CobolUnisysParser.SendAdvancingLinesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#sendAdvancingMnemonic.
    def visitSendAdvancingMnemonic(self, ctx:CobolUnisysParser.SendAdvancingMnemonicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#setStatement.
    def visitSetStatement(self, ctx:CobolUnisysParser.SetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#setToStatement.
    def visitSetToStatement(self, ctx:CobolUnisysParser.SetToStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#setUpDownByStatement.
    def visitSetUpDownByStatement(self, ctx:CobolUnisysParser.SetUpDownByStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#setTo.
    def visitSetTo(self, ctx:CobolUnisysParser.SetToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#setToValue.
    def visitSetToValue(self, ctx:CobolUnisysParser.SetToValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#setByValue.
    def visitSetByValue(self, ctx:CobolUnisysParser.SetByValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#sortStatement.
    def visitSortStatement(self, ctx:CobolUnisysParser.SortStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#sortOptional.
    def visitSortOptional(self, ctx:CobolUnisysParser.SortOptionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#sortOnKeyClause.
    def visitSortOnKeyClause(self, ctx:CobolUnisysParser.SortOnKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#sortDuplicatesPhrase.
    def visitSortDuplicatesPhrase(self, ctx:CobolUnisysParser.SortDuplicatesPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#sortCollatingSequencePhrase.
    def visitSortCollatingSequencePhrase(self, ctx:CobolUnisysParser.SortCollatingSequencePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#sortCollatingAlphanumeric.
    def visitSortCollatingAlphanumeric(self, ctx:CobolUnisysParser.SortCollatingAlphanumericContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#sortCollatingNational.
    def visitSortCollatingNational(self, ctx:CobolUnisysParser.SortCollatingNationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#sortInputProcedurePhrase.
    def visitSortInputProcedurePhrase(self, ctx:CobolUnisysParser.SortInputProcedurePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#sortInputThrough.
    def visitSortInputThrough(self, ctx:CobolUnisysParser.SortInputThroughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#sortUsing.
    def visitSortUsing(self, ctx:CobolUnisysParser.SortUsingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#sortOutputProcedurePhrase.
    def visitSortOutputProcedurePhrase(self, ctx:CobolUnisysParser.SortOutputProcedurePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#sortOutputThrough.
    def visitSortOutputThrough(self, ctx:CobolUnisysParser.SortOutputThroughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#sortGivingPhrase.
    def visitSortGivingPhrase(self, ctx:CobolUnisysParser.SortGivingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#sortGiving.
    def visitSortGiving(self, ctx:CobolUnisysParser.SortGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#startStatement.
    def visitStartStatement(self, ctx:CobolUnisysParser.StartStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#startKey.
    def visitStartKey(self, ctx:CobolUnisysParser.StartKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#stopStatement.
    def visitStopStatement(self, ctx:CobolUnisysParser.StopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#stopOption.
    def visitStopOption(self, ctx:CobolUnisysParser.StopOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#storeStatement.
    def visitStoreStatement(self, ctx:CobolUnisysParser.StoreStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#stringStatement.
    def visitStringStatement(self, ctx:CobolUnisysParser.StringStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#stringSendingPhrase.
    def visitStringSendingPhrase(self, ctx:CobolUnisysParser.StringSendingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#stringSending.
    def visitStringSending(self, ctx:CobolUnisysParser.StringSendingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#stringDelimitedByPhrase.
    def visitStringDelimitedByPhrase(self, ctx:CobolUnisysParser.StringDelimitedByPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#stringForPhrase.
    def visitStringForPhrase(self, ctx:CobolUnisysParser.StringForPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#stringIntoPhrase.
    def visitStringIntoPhrase(self, ctx:CobolUnisysParser.StringIntoPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#stringWithPointerPhrase.
    def visitStringWithPointerPhrase(self, ctx:CobolUnisysParser.StringWithPointerPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#subtractStatement.
    def visitSubtractStatement(self, ctx:CobolUnisysParser.SubtractStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#subtractFromStatement.
    def visitSubtractFromStatement(self, ctx:CobolUnisysParser.SubtractFromStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#subtractFromGivingStatement.
    def visitSubtractFromGivingStatement(self, ctx:CobolUnisysParser.SubtractFromGivingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#subtractCorrespondingStatement.
    def visitSubtractCorrespondingStatement(self, ctx:CobolUnisysParser.SubtractCorrespondingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#subtractSubtrahend.
    def visitSubtractSubtrahend(self, ctx:CobolUnisysParser.SubtractSubtrahendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#subtractMinuend.
    def visitSubtractMinuend(self, ctx:CobolUnisysParser.SubtractMinuendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#subtractMinuendGiving.
    def visitSubtractMinuendGiving(self, ctx:CobolUnisysParser.SubtractMinuendGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#subtractGiving.
    def visitSubtractGiving(self, ctx:CobolUnisysParser.SubtractGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#subtractMinuendCorresponding.
    def visitSubtractMinuendCorresponding(self, ctx:CobolUnisysParser.SubtractMinuendCorrespondingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#transactionStatement.
    def visitTransactionStatement(self, ctx:CobolUnisysParser.TransactionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#transactionBegin.
    def visitTransactionBegin(self, ctx:CobolUnisysParser.TransactionBeginContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#transactionCancel.
    def visitTransactionCancel(self, ctx:CobolUnisysParser.TransactionCancelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#transactionEnd.
    def visitTransactionEnd(self, ctx:CobolUnisysParser.TransactionEndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#terminateStatement.
    def visitTerminateStatement(self, ctx:CobolUnisysParser.TerminateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#unstringStatement.
    def visitUnstringStatement(self, ctx:CobolUnisysParser.UnstringStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#unstringSendingPhrase.
    def visitUnstringSendingPhrase(self, ctx:CobolUnisysParser.UnstringSendingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#unstringDelimitedByPhrase.
    def visitUnstringDelimitedByPhrase(self, ctx:CobolUnisysParser.UnstringDelimitedByPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#unstringOrAllPhrase.
    def visitUnstringOrAllPhrase(self, ctx:CobolUnisysParser.UnstringOrAllPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#unstringIntoPhrase.
    def visitUnstringIntoPhrase(self, ctx:CobolUnisysParser.UnstringIntoPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#unstringInto.
    def visitUnstringInto(self, ctx:CobolUnisysParser.UnstringIntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#unstringDelimiterIn.
    def visitUnstringDelimiterIn(self, ctx:CobolUnisysParser.UnstringDelimiterInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#unstringCountIn.
    def visitUnstringCountIn(self, ctx:CobolUnisysParser.UnstringCountInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#unstringWithPointerPhrase.
    def visitUnstringWithPointerPhrase(self, ctx:CobolUnisysParser.UnstringWithPointerPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#unstringTallyingPhrase.
    def visitUnstringTallyingPhrase(self, ctx:CobolUnisysParser.UnstringTallyingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#useStatement.
    def visitUseStatement(self, ctx:CobolUnisysParser.UseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#useAfterClause.
    def visitUseAfterClause(self, ctx:CobolUnisysParser.UseAfterClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#useAfterOn.
    def visitUseAfterOn(self, ctx:CobolUnisysParser.UseAfterOnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#useDebugClause.
    def visitUseDebugClause(self, ctx:CobolUnisysParser.UseDebugClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#useDebugOn.
    def visitUseDebugOn(self, ctx:CobolUnisysParser.UseDebugOnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#useDeadLock.
    def visitUseDeadLock(self, ctx:CobolUnisysParser.UseDeadLockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#useProcedure.
    def visitUseProcedure(self, ctx:CobolUnisysParser.UseProcedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#waitStatement.
    def visitWaitStatement(self, ctx:CobolUnisysParser.WaitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#waitArithmeticExpression.
    def visitWaitArithmeticExpression(self, ctx:CobolUnisysParser.WaitArithmeticExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#attributeChangeEvent.
    def visitAttributeChangeEvent(self, ctx:CobolUnisysParser.AttributeChangeEventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#attributeInputEvent.
    def visitAttributeInputEvent(self, ctx:CobolUnisysParser.AttributeInputEventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#attributeOutputEvent.
    def visitAttributeOutputEvent(self, ctx:CobolUnisysParser.AttributeOutputEventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#attributeAcceptEvent.
    def visitAttributeAcceptEvent(self, ctx:CobolUnisysParser.AttributeAcceptEventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#attributeExceptionEvent.
    def visitAttributeExceptionEvent(self, ctx:CobolUnisysParser.AttributeExceptionEventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#eventIdentifier.
    def visitEventIdentifier(self, ctx:CobolUnisysParser.EventIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#crcrEvent.
    def visitCrcrEvent(self, ctx:CobolUnisysParser.CrcrEventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#odtInputPresent.
    def visitOdtInputPresent(self, ctx:CobolUnisysParser.OdtInputPresentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#readOk.
    def visitReadOk(self, ctx:CobolUnisysParser.ReadOkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#writeOk.
    def visitWriteOk(self, ctx:CobolUnisysParser.WriteOkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#stoqEvent.
    def visitStoqEvent(self, ctx:CobolUnisysParser.StoqEventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#writeStatement.
    def visitWriteStatement(self, ctx:CobolUnisysParser.WriteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#writeFromPhrase.
    def visitWriteFromPhrase(self, ctx:CobolUnisysParser.WriteFromPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#writeAdvancingPhrase.
    def visitWriteAdvancingPhrase(self, ctx:CobolUnisysParser.WriteAdvancingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#writeAdvancingPage.
    def visitWriteAdvancingPage(self, ctx:CobolUnisysParser.WriteAdvancingPageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#writeAdvancingLines.
    def visitWriteAdvancingLines(self, ctx:CobolUnisysParser.WriteAdvancingLinesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#writeAdvancingMnemonic.
    def visitWriteAdvancingMnemonic(self, ctx:CobolUnisysParser.WriteAdvancingMnemonicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#writeAtEndOfPagePhrase.
    def visitWriteAtEndOfPagePhrase(self, ctx:CobolUnisysParser.WriteAtEndOfPagePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#writeNotAtEndOfPagePhrase.
    def visitWriteNotAtEndOfPagePhrase(self, ctx:CobolUnisysParser.WriteNotAtEndOfPagePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#atEndPhrase.
    def visitAtEndPhrase(self, ctx:CobolUnisysParser.AtEndPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#notAtEndPhrase.
    def visitNotAtEndPhrase(self, ctx:CobolUnisysParser.NotAtEndPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#invalidKeyPhrase.
    def visitInvalidKeyPhrase(self, ctx:CobolUnisysParser.InvalidKeyPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#notInvalidKeyPhrase.
    def visitNotInvalidKeyPhrase(self, ctx:CobolUnisysParser.NotInvalidKeyPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#onOverflowPhrase.
    def visitOnOverflowPhrase(self, ctx:CobolUnisysParser.OnOverflowPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#notOnOverflowPhrase.
    def visitNotOnOverflowPhrase(self, ctx:CobolUnisysParser.NotOnOverflowPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#onSizeErrorPhrase.
    def visitOnSizeErrorPhrase(self, ctx:CobolUnisysParser.OnSizeErrorPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#notOnSizeErrorPhrase.
    def visitNotOnSizeErrorPhrase(self, ctx:CobolUnisysParser.NotOnSizeErrorPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#onExceptionClause.
    def visitOnExceptionClause(self, ctx:CobolUnisysParser.OnExceptionClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#notOnExceptionClause.
    def visitNotOnExceptionClause(self, ctx:CobolUnisysParser.NotOnExceptionClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#arithmeticExpression.
    def visitArithmeticExpression(self, ctx:CobolUnisysParser.ArithmeticExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#plusMinus.
    def visitPlusMinus(self, ctx:CobolUnisysParser.PlusMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#multDivs.
    def visitMultDivs(self, ctx:CobolUnisysParser.MultDivsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#multDiv.
    def visitMultDiv(self, ctx:CobolUnisysParser.MultDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#powers.
    def visitPowers(self, ctx:CobolUnisysParser.PowersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#power.
    def visitPower(self, ctx:CobolUnisysParser.PowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#basis.
    def visitBasis(self, ctx:CobolUnisysParser.BasisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#condition.
    def visitCondition(self, ctx:CobolUnisysParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#andOrCondition.
    def visitAndOrCondition(self, ctx:CobolUnisysParser.AndOrConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#combinableCondition.
    def visitCombinableCondition(self, ctx:CobolUnisysParser.CombinableConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#simpleCondition.
    def visitSimpleCondition(self, ctx:CobolUnisysParser.SimpleConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#classCondition.
    def visitClassCondition(self, ctx:CobolUnisysParser.ClassConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#conditionNameReference.
    def visitConditionNameReference(self, ctx:CobolUnisysParser.ConditionNameReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#conditionNameSubscriptReference.
    def visitConditionNameSubscriptReference(self, ctx:CobolUnisysParser.ConditionNameSubscriptReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#attributeCondition.
    def visitAttributeCondition(self, ctx:CobolUnisysParser.AttributeConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#attributeConditionExpr.
    def visitAttributeConditionExpr(self, ctx:CobolUnisysParser.AttributeConditionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#relationCondition.
    def visitRelationCondition(self, ctx:CobolUnisysParser.RelationConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#relationSignCondition.
    def visitRelationSignCondition(self, ctx:CobolUnisysParser.RelationSignConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#relationArithmeticComparison.
    def visitRelationArithmeticComparison(self, ctx:CobolUnisysParser.RelationArithmeticComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#relationCombinedComparison.
    def visitRelationCombinedComparison(self, ctx:CobolUnisysParser.RelationCombinedComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#relationCombinedCondition.
    def visitRelationCombinedCondition(self, ctx:CobolUnisysParser.RelationCombinedConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#relationalOperator.
    def visitRelationalOperator(self, ctx:CobolUnisysParser.RelationalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#abbreviation.
    def visitAbbreviation(self, ctx:CobolUnisysParser.AbbreviationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#identifier.
    def visitIdentifier(self, ctx:CobolUnisysParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#tableCall.
    def visitTableCall(self, ctx:CobolUnisysParser.TableCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#functionCall.
    def visitFunctionCall(self, ctx:CobolUnisysParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#referenceModifier.
    def visitReferenceModifier(self, ctx:CobolUnisysParser.ReferenceModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#characterPosition.
    def visitCharacterPosition(self, ctx:CobolUnisysParser.CharacterPositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#length.
    def visitLength(self, ctx:CobolUnisysParser.LengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#subscript_.
    def visitSubscript_(self, ctx:CobolUnisysParser.Subscript_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#argument.
    def visitArgument(self, ctx:CobolUnisysParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#qualifiedDataName.
    def visitQualifiedDataName(self, ctx:CobolUnisysParser.QualifiedDataNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#qualifiedDataNameFormat1.
    def visitQualifiedDataNameFormat1(self, ctx:CobolUnisysParser.QualifiedDataNameFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#qualifiedDataNameFormat2.
    def visitQualifiedDataNameFormat2(self, ctx:CobolUnisysParser.QualifiedDataNameFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#qualifiedDataNameFormat3.
    def visitQualifiedDataNameFormat3(self, ctx:CobolUnisysParser.QualifiedDataNameFormat3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#qualifiedDataNameFormat4.
    def visitQualifiedDataNameFormat4(self, ctx:CobolUnisysParser.QualifiedDataNameFormat4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#qualifiedInData.
    def visitQualifiedInData(self, ctx:CobolUnisysParser.QualifiedInDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#inData.
    def visitInData(self, ctx:CobolUnisysParser.InDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#inFile.
    def visitInFile(self, ctx:CobolUnisysParser.InFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#inMnemonic.
    def visitInMnemonic(self, ctx:CobolUnisysParser.InMnemonicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#inSection.
    def visitInSection(self, ctx:CobolUnisysParser.InSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#inLibrary.
    def visitInLibrary(self, ctx:CobolUnisysParser.InLibraryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#inTable.
    def visitInTable(self, ctx:CobolUnisysParser.InTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#alphabetName.
    def visitAlphabetName(self, ctx:CobolUnisysParser.AlphabetNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#assignmentName.
    def visitAssignmentName(self, ctx:CobolUnisysParser.AssignmentNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#basisName.
    def visitBasisName(self, ctx:CobolUnisysParser.BasisNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#cdName.
    def visitCdName(self, ctx:CobolUnisysParser.CdNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#className.
    def visitClassName(self, ctx:CobolUnisysParser.ClassNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#computerName.
    def visitComputerName(self, ctx:CobolUnisysParser.ComputerNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#conditionName.
    def visitConditionName(self, ctx:CobolUnisysParser.ConditionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataName.
    def visitDataName(self, ctx:CobolUnisysParser.DataNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#dataDescName.
    def visitDataDescName(self, ctx:CobolUnisysParser.DataDescNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#environmentName.
    def visitEnvironmentName(self, ctx:CobolUnisysParser.EnvironmentNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#fileAttribute.
    def visitFileAttribute(self, ctx:CobolUnisysParser.FileAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#fileName.
    def visitFileName(self, ctx:CobolUnisysParser.FileNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#functionName.
    def visitFunctionName(self, ctx:CobolUnisysParser.FunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#indexName.
    def visitIndexName(self, ctx:CobolUnisysParser.IndexNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#languageName.
    def visitLanguageName(self, ctx:CobolUnisysParser.LanguageNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#libraryName.
    def visitLibraryName(self, ctx:CobolUnisysParser.LibraryNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#localName.
    def visitLocalName(self, ctx:CobolUnisysParser.LocalNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#mnemonicName.
    def visitMnemonicName(self, ctx:CobolUnisysParser.MnemonicNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#paragraphName.
    def visitParagraphName(self, ctx:CobolUnisysParser.ParagraphNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#procedureName.
    def visitProcedureName(self, ctx:CobolUnisysParser.ProcedureNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#programName.
    def visitProgramName(self, ctx:CobolUnisysParser.ProgramNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#recordName.
    def visitRecordName(self, ctx:CobolUnisysParser.RecordNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#reportName.
    def visitReportName(self, ctx:CobolUnisysParser.ReportNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#routineName.
    def visitRoutineName(self, ctx:CobolUnisysParser.RoutineNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#screenName.
    def visitScreenName(self, ctx:CobolUnisysParser.ScreenNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#sectionName.
    def visitSectionName(self, ctx:CobolUnisysParser.SectionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#systemName.
    def visitSystemName(self, ctx:CobolUnisysParser.SystemNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#symbolicCharacter.
    def visitSymbolicCharacter(self, ctx:CobolUnisysParser.SymbolicCharacterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#textName.
    def visitTextName(self, ctx:CobolUnisysParser.TextNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#booleanLiteral.
    def visitBooleanLiteral(self, ctx:CobolUnisysParser.BooleanLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#numericLiteral.
    def visitNumericLiteral(self, ctx:CobolUnisysParser.NumericLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#integerLiteral.
    def visitIntegerLiteral(self, ctx:CobolUnisysParser.IntegerLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#cicsDfhRespLiteral.
    def visitCicsDfhRespLiteral(self, ctx:CobolUnisysParser.CicsDfhRespLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#cicsDfhValueLiteral.
    def visitCicsDfhValueLiteral(self, ctx:CobolUnisysParser.CicsDfhValueLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#figurativeConstant.
    def visitFigurativeConstant(self, ctx:CobolUnisysParser.FigurativeConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#specialRegister.
    def visitSpecialRegister(self, ctx:CobolUnisysParser.SpecialRegisterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#commentEntry.
    def visitCommentEntry(self, ctx:CobolUnisysParser.CommentEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CobolUnisysParser#charDataKeyword.
    def visitCharDataKeyword(self, ctx:CobolUnisysParser.CharDataKeywordContext):
        return self.visitChildren(ctx)



del CobolUnisysParser