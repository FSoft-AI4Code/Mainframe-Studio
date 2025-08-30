# Generated from ./src/parsers/grammar/dnp_cobol/DNP.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .DNPParser import DNPParser
else:
    from DNPParser import DNPParser

# This class defines a complete generic visitor for a parse tree produced by DNPParser.

class DNPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DNPParser#startRule.
    def visitStartRule(self, ctx:DNPParser.StartRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#compilationUnit.
    def visitCompilationUnit(self, ctx:DNPParser.CompilationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#programUnit.
    def visitProgramUnit(self, ctx:DNPParser.ProgramUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#endProgramStatement.
    def visitEndProgramStatement(self, ctx:DNPParser.EndProgramStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#identificationDivision.
    def visitIdentificationDivision(self, ctx:DNPParser.IdentificationDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#identificationDivisionBody.
    def visitIdentificationDivisionBody(self, ctx:DNPParser.IdentificationDivisionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#programIdParagraph.
    def visitProgramIdParagraph(self, ctx:DNPParser.ProgramIdParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#author_name.
    def visitAuthor_name(self, ctx:DNPParser.Author_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#authorParagraph.
    def visitAuthorParagraph(self, ctx:DNPParser.AuthorParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#installationParagraph.
    def visitInstallationParagraph(self, ctx:DNPParser.InstallationParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dateWrittenParagraph.
    def visitDateWrittenParagraph(self, ctx:DNPParser.DateWrittenParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dateCompiledParagraph.
    def visitDateCompiledParagraph(self, ctx:DNPParser.DateCompiledParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#securityParagraph.
    def visitSecurityParagraph(self, ctx:DNPParser.SecurityParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#remarksParagraph.
    def visitRemarksParagraph(self, ctx:DNPParser.RemarksParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#environmentDivision.
    def visitEnvironmentDivision(self, ctx:DNPParser.EnvironmentDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#environmentDivisionBody.
    def visitEnvironmentDivisionBody(self, ctx:DNPParser.EnvironmentDivisionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#configurationSection.
    def visitConfigurationSection(self, ctx:DNPParser.ConfigurationSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#configurationSectionParagraph.
    def visitConfigurationSectionParagraph(self, ctx:DNPParser.ConfigurationSectionParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#sourceComputerParagraph.
    def visitSourceComputerParagraph(self, ctx:DNPParser.SourceComputerParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#objectComputerParagraph.
    def visitObjectComputerParagraph(self, ctx:DNPParser.ObjectComputerParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#objectComputerClause.
    def visitObjectComputerClause(self, ctx:DNPParser.ObjectComputerClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#memorySizeClause.
    def visitMemorySizeClause(self, ctx:DNPParser.MemorySizeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#diskSizeClause.
    def visitDiskSizeClause(self, ctx:DNPParser.DiskSizeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#collatingSequenceClause.
    def visitCollatingSequenceClause(self, ctx:DNPParser.CollatingSequenceClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#collatingSequenceClauseAlphanumeric.
    def visitCollatingSequenceClauseAlphanumeric(self, ctx:DNPParser.CollatingSequenceClauseAlphanumericContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#collatingSequenceClauseNational.
    def visitCollatingSequenceClauseNational(self, ctx:DNPParser.CollatingSequenceClauseNationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#segmentLimitClause.
    def visitSegmentLimitClause(self, ctx:DNPParser.SegmentLimitClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#characterSetClause.
    def visitCharacterSetClause(self, ctx:DNPParser.CharacterSetClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#specialNamesParagraph.
    def visitSpecialNamesParagraph(self, ctx:DNPParser.SpecialNamesParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#specialNameClause.
    def visitSpecialNameClause(self, ctx:DNPParser.SpecialNameClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#alphabetClause.
    def visitAlphabetClause(self, ctx:DNPParser.AlphabetClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#alphabetClauseFormat1.
    def visitAlphabetClauseFormat1(self, ctx:DNPParser.AlphabetClauseFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#alphabetLiterals.
    def visitAlphabetLiterals(self, ctx:DNPParser.AlphabetLiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#alphabetThrough.
    def visitAlphabetThrough(self, ctx:DNPParser.AlphabetThroughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#alphabetAlso.
    def visitAlphabetAlso(self, ctx:DNPParser.AlphabetAlsoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#alphabetClauseFormat2.
    def visitAlphabetClauseFormat2(self, ctx:DNPParser.AlphabetClauseFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#channelClause.
    def visitChannelClause(self, ctx:DNPParser.ChannelClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#classClause.
    def visitClassClause(self, ctx:DNPParser.ClassClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#classClauseThrough.
    def visitClassClauseThrough(self, ctx:DNPParser.ClassClauseThroughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#classClauseFrom.
    def visitClassClauseFrom(self, ctx:DNPParser.ClassClauseFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#classClauseTo.
    def visitClassClauseTo(self, ctx:DNPParser.ClassClauseToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#currencySignClause.
    def visitCurrencySignClause(self, ctx:DNPParser.CurrencySignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#decimalPointClause.
    def visitDecimalPointClause(self, ctx:DNPParser.DecimalPointClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#defaultComputationalSignClause.
    def visitDefaultComputationalSignClause(self, ctx:DNPParser.DefaultComputationalSignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#defaultDisplaySignClause.
    def visitDefaultDisplaySignClause(self, ctx:DNPParser.DefaultDisplaySignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#environmentSwitchNameClause.
    def visitEnvironmentSwitchNameClause(self, ctx:DNPParser.EnvironmentSwitchNameClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#environmentSwitchNameSpecialNamesStatusPhrase.
    def visitEnvironmentSwitchNameSpecialNamesStatusPhrase(self, ctx:DNPParser.EnvironmentSwitchNameSpecialNamesStatusPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#odtClause.
    def visitOdtClause(self, ctx:DNPParser.OdtClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reserveNetworkClause.
    def visitReserveNetworkClause(self, ctx:DNPParser.ReserveNetworkClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#symbolicCharactersClause.
    def visitSymbolicCharactersClause(self, ctx:DNPParser.SymbolicCharactersClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#symbolicCharacters.
    def visitSymbolicCharacters(self, ctx:DNPParser.SymbolicCharactersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#inputOutputSection.
    def visitInputOutputSection(self, ctx:DNPParser.InputOutputSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#inputOutputSectionParagraph.
    def visitInputOutputSectionParagraph(self, ctx:DNPParser.InputOutputSectionParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#fileControlParagraph.
    def visitFileControlParagraph(self, ctx:DNPParser.FileControlParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#fileControlEntry.
    def visitFileControlEntry(self, ctx:DNPParser.FileControlEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#selectClause.
    def visitSelectClause(self, ctx:DNPParser.SelectClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#fileControlClause.
    def visitFileControlClause(self, ctx:DNPParser.FileControlClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#assignClause.
    def visitAssignClause(self, ctx:DNPParser.AssignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reserveClause.
    def visitReserveClause(self, ctx:DNPParser.ReserveClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#organizationClause.
    def visitOrganizationClause(self, ctx:DNPParser.OrganizationClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#paddingCharacterClause.
    def visitPaddingCharacterClause(self, ctx:DNPParser.PaddingCharacterClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#recordDelimiterClause.
    def visitRecordDelimiterClause(self, ctx:DNPParser.RecordDelimiterClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#accessModeClause.
    def visitAccessModeClause(self, ctx:DNPParser.AccessModeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#recordKeyClause.
    def visitRecordKeyClause(self, ctx:DNPParser.RecordKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#alternateRecordKeyClause.
    def visitAlternateRecordKeyClause(self, ctx:DNPParser.AlternateRecordKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#passwordClause.
    def visitPasswordClause(self, ctx:DNPParser.PasswordClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#fileStatusClause.
    def visitFileStatusClause(self, ctx:DNPParser.FileStatusClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#relativeKeyClause.
    def visitRelativeKeyClause(self, ctx:DNPParser.RelativeKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#ioControlParagraph.
    def visitIoControlParagraph(self, ctx:DNPParser.IoControlParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#ioControlClause.
    def visitIoControlClause(self, ctx:DNPParser.IoControlClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#rerunClause.
    def visitRerunClause(self, ctx:DNPParser.RerunClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#rerunEveryRecords.
    def visitRerunEveryRecords(self, ctx:DNPParser.RerunEveryRecordsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#rerunEveryOf.
    def visitRerunEveryOf(self, ctx:DNPParser.RerunEveryOfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#rerunEveryClock.
    def visitRerunEveryClock(self, ctx:DNPParser.RerunEveryClockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#sameClause.
    def visitSameClause(self, ctx:DNPParser.SameClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#multipleFileClause.
    def visitMultipleFileClause(self, ctx:DNPParser.MultipleFileClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#multipleFilePosition.
    def visitMultipleFilePosition(self, ctx:DNPParser.MultipleFilePositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#commitmentControlClause.
    def visitCommitmentControlClause(self, ctx:DNPParser.CommitmentControlClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataDivision.
    def visitDataDivision(self, ctx:DNPParser.DataDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataDivisionSection.
    def visitDataDivisionSection(self, ctx:DNPParser.DataDivisionSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#fileSection.
    def visitFileSection(self, ctx:DNPParser.FileSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#fileDescriptionEntry.
    def visitFileDescriptionEntry(self, ctx:DNPParser.FileDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#fileDescriptionEntryClause.
    def visitFileDescriptionEntryClause(self, ctx:DNPParser.FileDescriptionEntryClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#externalClause.
    def visitExternalClause(self, ctx:DNPParser.ExternalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#globalClause.
    def visitGlobalClause(self, ctx:DNPParser.GlobalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#blockContainsClause.
    def visitBlockContainsClause(self, ctx:DNPParser.BlockContainsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#blockContainsTo.
    def visitBlockContainsTo(self, ctx:DNPParser.BlockContainsToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#recordContainsClause.
    def visitRecordContainsClause(self, ctx:DNPParser.RecordContainsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#recordContainsClauseFormat1.
    def visitRecordContainsClauseFormat1(self, ctx:DNPParser.RecordContainsClauseFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#recordContainsClauseFormat2.
    def visitRecordContainsClauseFormat2(self, ctx:DNPParser.RecordContainsClauseFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#recordContainsClauseFormat3.
    def visitRecordContainsClauseFormat3(self, ctx:DNPParser.RecordContainsClauseFormat3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#recordContainsTo.
    def visitRecordContainsTo(self, ctx:DNPParser.RecordContainsToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#labelRecordsClause.
    def visitLabelRecordsClause(self, ctx:DNPParser.LabelRecordsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#valueOfClause.
    def visitValueOfClause(self, ctx:DNPParser.ValueOfClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#valuePair.
    def visitValuePair(self, ctx:DNPParser.ValuePairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataRecordsClause.
    def visitDataRecordsClause(self, ctx:DNPParser.DataRecordsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#linageClause.
    def visitLinageClause(self, ctx:DNPParser.LinageClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#linageAt.
    def visitLinageAt(self, ctx:DNPParser.LinageAtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#linageFootingAt.
    def visitLinageFootingAt(self, ctx:DNPParser.LinageFootingAtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#linageLinesAtTop.
    def visitLinageLinesAtTop(self, ctx:DNPParser.LinageLinesAtTopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#linageLinesAtBottom.
    def visitLinageLinesAtBottom(self, ctx:DNPParser.LinageLinesAtBottomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#recordingModeClause.
    def visitRecordingModeClause(self, ctx:DNPParser.RecordingModeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#modeStatement.
    def visitModeStatement(self, ctx:DNPParser.ModeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#codeSetClause.
    def visitCodeSetClause(self, ctx:DNPParser.CodeSetClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportClause.
    def visitReportClause(self, ctx:DNPParser.ReportClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataBaseSection.
    def visitDataBaseSection(self, ctx:DNPParser.DataBaseSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataBaseSectionEntry.
    def visitDataBaseSectionEntry(self, ctx:DNPParser.DataBaseSectionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataBaseDeclare.
    def visitDataBaseDeclare(self, ctx:DNPParser.DataBaseDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataBaseDatasetDeclare.
    def visitDataBaseDatasetDeclare(self, ctx:DNPParser.DataBaseDatasetDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#invokeClause.
    def visitInvokeClause(self, ctx:DNPParser.InvokeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#usingClause.
    def visitUsingClause(self, ctx:DNPParser.UsingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#workingStorageSection.
    def visitWorkingStorageSection(self, ctx:DNPParser.WorkingStorageSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#linkageSection.
    def visitLinkageSection(self, ctx:DNPParser.LinkageSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#communicationSection.
    def visitCommunicationSection(self, ctx:DNPParser.CommunicationSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#communicationDescriptionEntry.
    def visitCommunicationDescriptionEntry(self, ctx:DNPParser.CommunicationDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#communicationDescriptionEntryFormat1.
    def visitCommunicationDescriptionEntryFormat1(self, ctx:DNPParser.CommunicationDescriptionEntryFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#communicationDescriptionEntryFormat2.
    def visitCommunicationDescriptionEntryFormat2(self, ctx:DNPParser.CommunicationDescriptionEntryFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#communicationDescriptionEntryFormat3.
    def visitCommunicationDescriptionEntryFormat3(self, ctx:DNPParser.CommunicationDescriptionEntryFormat3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#communicationDescriptionEntryFormat4.
    def visitCommunicationDescriptionEntryFormat4(self, ctx:DNPParser.CommunicationDescriptionEntryFormat4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#communicationAttribute.
    def visitCommunicationAttribute(self, ctx:DNPParser.CommunicationAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#communicationIoHeader.
    def visitCommunicationIoHeader(self, ctx:DNPParser.CommunicationIoHeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#conversationClause.
    def visitConversationClause(self, ctx:DNPParser.ConversationClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#destinationCountClause.
    def visitDestinationCountClause(self, ctx:DNPParser.DestinationCountClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#destinationTableClause.
    def visitDestinationTableClause(self, ctx:DNPParser.DestinationTableClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#endKeyClause.
    def visitEndKeyClause(self, ctx:DNPParser.EndKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#errorKeyClause.
    def visitErrorKeyClause(self, ctx:DNPParser.ErrorKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#messageCountClause.
    def visitMessageCountClause(self, ctx:DNPParser.MessageCountClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#messageDateClause.
    def visitMessageDateClause(self, ctx:DNPParser.MessageDateClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#messageTimeClause.
    def visitMessageTimeClause(self, ctx:DNPParser.MessageTimeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#statusKeyClause.
    def visitStatusKeyClause(self, ctx:DNPParser.StatusKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#symbolicDestinationClause.
    def visitSymbolicDestinationClause(self, ctx:DNPParser.SymbolicDestinationClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#symbolicQueueClause.
    def visitSymbolicQueueClause(self, ctx:DNPParser.SymbolicQueueClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#symbolicSourceClause.
    def visitSymbolicSourceClause(self, ctx:DNPParser.SymbolicSourceClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#symbolicTerminalClause.
    def visitSymbolicTerminalClause(self, ctx:DNPParser.SymbolicTerminalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#symbolicSubQueueClause.
    def visitSymbolicSubQueueClause(self, ctx:DNPParser.SymbolicSubQueueClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#textLengthClause.
    def visitTextLengthClause(self, ctx:DNPParser.TextLengthClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#localStorageSection.
    def visitLocalStorageSection(self, ctx:DNPParser.LocalStorageSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenSection.
    def visitScreenSection(self, ctx:DNPParser.ScreenSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenDescriptionEntry.
    def visitScreenDescriptionEntry(self, ctx:DNPParser.ScreenDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenDescriptionBlankClause.
    def visitScreenDescriptionBlankClause(self, ctx:DNPParser.ScreenDescriptionBlankClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenDescriptionBellClause.
    def visitScreenDescriptionBellClause(self, ctx:DNPParser.ScreenDescriptionBellClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenDescriptionBlinkClause.
    def visitScreenDescriptionBlinkClause(self, ctx:DNPParser.ScreenDescriptionBlinkClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenDescriptionEraseClause.
    def visitScreenDescriptionEraseClause(self, ctx:DNPParser.ScreenDescriptionEraseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenDescriptionLightClause.
    def visitScreenDescriptionLightClause(self, ctx:DNPParser.ScreenDescriptionLightClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenDescriptionGridClause.
    def visitScreenDescriptionGridClause(self, ctx:DNPParser.ScreenDescriptionGridClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenDescriptionReverseVideoClause.
    def visitScreenDescriptionReverseVideoClause(self, ctx:DNPParser.ScreenDescriptionReverseVideoClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenDescriptionUnderlineClause.
    def visitScreenDescriptionUnderlineClause(self, ctx:DNPParser.ScreenDescriptionUnderlineClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenDescriptionSizeClause.
    def visitScreenDescriptionSizeClause(self, ctx:DNPParser.ScreenDescriptionSizeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenDescriptionLineClause.
    def visitScreenDescriptionLineClause(self, ctx:DNPParser.ScreenDescriptionLineClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenDescriptionColumnClause.
    def visitScreenDescriptionColumnClause(self, ctx:DNPParser.ScreenDescriptionColumnClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenDescriptionForegroundColorClause.
    def visitScreenDescriptionForegroundColorClause(self, ctx:DNPParser.ScreenDescriptionForegroundColorClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenDescriptionBackgroundColorClause.
    def visitScreenDescriptionBackgroundColorClause(self, ctx:DNPParser.ScreenDescriptionBackgroundColorClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenDescriptionControlClause.
    def visitScreenDescriptionControlClause(self, ctx:DNPParser.ScreenDescriptionControlClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenDescriptionValueClause.
    def visitScreenDescriptionValueClause(self, ctx:DNPParser.ScreenDescriptionValueClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenDescriptionPictureClause.
    def visitScreenDescriptionPictureClause(self, ctx:DNPParser.ScreenDescriptionPictureClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenDescriptionFromClause.
    def visitScreenDescriptionFromClause(self, ctx:DNPParser.ScreenDescriptionFromClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenDescriptionToClause.
    def visitScreenDescriptionToClause(self, ctx:DNPParser.ScreenDescriptionToClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenDescriptionUsingClause.
    def visitScreenDescriptionUsingClause(self, ctx:DNPParser.ScreenDescriptionUsingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenDescriptionUsageClause.
    def visitScreenDescriptionUsageClause(self, ctx:DNPParser.ScreenDescriptionUsageClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenDescriptionBlankWhenZeroClause.
    def visitScreenDescriptionBlankWhenZeroClause(self, ctx:DNPParser.ScreenDescriptionBlankWhenZeroClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenDescriptionJustifiedClause.
    def visitScreenDescriptionJustifiedClause(self, ctx:DNPParser.ScreenDescriptionJustifiedClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenDescriptionSignClause.
    def visitScreenDescriptionSignClause(self, ctx:DNPParser.ScreenDescriptionSignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenDescriptionAutoClause.
    def visitScreenDescriptionAutoClause(self, ctx:DNPParser.ScreenDescriptionAutoClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenDescriptionSecureClause.
    def visitScreenDescriptionSecureClause(self, ctx:DNPParser.ScreenDescriptionSecureClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenDescriptionRequiredClause.
    def visitScreenDescriptionRequiredClause(self, ctx:DNPParser.ScreenDescriptionRequiredClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenDescriptionPromptClause.
    def visitScreenDescriptionPromptClause(self, ctx:DNPParser.ScreenDescriptionPromptClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenDescriptionPromptOccursClause.
    def visitScreenDescriptionPromptOccursClause(self, ctx:DNPParser.ScreenDescriptionPromptOccursClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenDescriptionFullClause.
    def visitScreenDescriptionFullClause(self, ctx:DNPParser.ScreenDescriptionFullClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenDescriptionZeroFillClause.
    def visitScreenDescriptionZeroFillClause(self, ctx:DNPParser.ScreenDescriptionZeroFillClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportSection.
    def visitReportSection(self, ctx:DNPParser.ReportSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportDescription.
    def visitReportDescription(self, ctx:DNPParser.ReportDescriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportDescriptionEntry.
    def visitReportDescriptionEntry(self, ctx:DNPParser.ReportDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportDescriptionGlobalClause.
    def visitReportDescriptionGlobalClause(self, ctx:DNPParser.ReportDescriptionGlobalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportDescriptionPageLimitClause.
    def visitReportDescriptionPageLimitClause(self, ctx:DNPParser.ReportDescriptionPageLimitClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportDescriptionHeadingClause.
    def visitReportDescriptionHeadingClause(self, ctx:DNPParser.ReportDescriptionHeadingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportDescriptionFirstDetailClause.
    def visitReportDescriptionFirstDetailClause(self, ctx:DNPParser.ReportDescriptionFirstDetailClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportDescriptionLastDetailClause.
    def visitReportDescriptionLastDetailClause(self, ctx:DNPParser.ReportDescriptionLastDetailClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportDescriptionFootingClause.
    def visitReportDescriptionFootingClause(self, ctx:DNPParser.ReportDescriptionFootingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportGroupDescriptionEntry.
    def visitReportGroupDescriptionEntry(self, ctx:DNPParser.ReportGroupDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportGroupDescriptionEntryFormat1.
    def visitReportGroupDescriptionEntryFormat1(self, ctx:DNPParser.ReportGroupDescriptionEntryFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportGroupDescriptionEntryFormat2.
    def visitReportGroupDescriptionEntryFormat2(self, ctx:DNPParser.ReportGroupDescriptionEntryFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportGroupDescriptionEntryFormat3.
    def visitReportGroupDescriptionEntryFormat3(self, ctx:DNPParser.ReportGroupDescriptionEntryFormat3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportGroupBlankWhenZeroClause.
    def visitReportGroupBlankWhenZeroClause(self, ctx:DNPParser.ReportGroupBlankWhenZeroClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportGroupColumnNumberClause.
    def visitReportGroupColumnNumberClause(self, ctx:DNPParser.ReportGroupColumnNumberClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportGroupIndicateClause.
    def visitReportGroupIndicateClause(self, ctx:DNPParser.ReportGroupIndicateClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportGroupJustifiedClause.
    def visitReportGroupJustifiedClause(self, ctx:DNPParser.ReportGroupJustifiedClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportGroupLineNumberClause.
    def visitReportGroupLineNumberClause(self, ctx:DNPParser.ReportGroupLineNumberClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportGroupLineNumberNextPage.
    def visitReportGroupLineNumberNextPage(self, ctx:DNPParser.ReportGroupLineNumberNextPageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportGroupLineNumberPlus.
    def visitReportGroupLineNumberPlus(self, ctx:DNPParser.ReportGroupLineNumberPlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportGroupNextGroupClause.
    def visitReportGroupNextGroupClause(self, ctx:DNPParser.ReportGroupNextGroupClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportGroupNextGroupPlus.
    def visitReportGroupNextGroupPlus(self, ctx:DNPParser.ReportGroupNextGroupPlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportGroupNextGroupNextPage.
    def visitReportGroupNextGroupNextPage(self, ctx:DNPParser.ReportGroupNextGroupNextPageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportGroupPictureClause.
    def visitReportGroupPictureClause(self, ctx:DNPParser.ReportGroupPictureClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportGroupResetClause.
    def visitReportGroupResetClause(self, ctx:DNPParser.ReportGroupResetClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportGroupSignClause.
    def visitReportGroupSignClause(self, ctx:DNPParser.ReportGroupSignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportGroupSourceClause.
    def visitReportGroupSourceClause(self, ctx:DNPParser.ReportGroupSourceClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportGroupSumClause.
    def visitReportGroupSumClause(self, ctx:DNPParser.ReportGroupSumClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportGroupTypeClause.
    def visitReportGroupTypeClause(self, ctx:DNPParser.ReportGroupTypeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportGroupTypeReportHeading.
    def visitReportGroupTypeReportHeading(self, ctx:DNPParser.ReportGroupTypeReportHeadingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportGroupTypePageHeading.
    def visitReportGroupTypePageHeading(self, ctx:DNPParser.ReportGroupTypePageHeadingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportGroupTypeControlHeading.
    def visitReportGroupTypeControlHeading(self, ctx:DNPParser.ReportGroupTypeControlHeadingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportGroupTypeDetail.
    def visitReportGroupTypeDetail(self, ctx:DNPParser.ReportGroupTypeDetailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportGroupTypeControlFooting.
    def visitReportGroupTypeControlFooting(self, ctx:DNPParser.ReportGroupTypeControlFootingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportGroupUsageClause.
    def visitReportGroupUsageClause(self, ctx:DNPParser.ReportGroupUsageClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportGroupTypePageFooting.
    def visitReportGroupTypePageFooting(self, ctx:DNPParser.ReportGroupTypePageFootingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportGroupTypeReportFooting.
    def visitReportGroupTypeReportFooting(self, ctx:DNPParser.ReportGroupTypeReportFootingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportGroupValueClause.
    def visitReportGroupValueClause(self, ctx:DNPParser.ReportGroupValueClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#programLibrarySection.
    def visitProgramLibrarySection(self, ctx:DNPParser.ProgramLibrarySectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#libraryDescriptionEntry.
    def visitLibraryDescriptionEntry(self, ctx:DNPParser.LibraryDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#libraryDescriptionEntryFormat1.
    def visitLibraryDescriptionEntryFormat1(self, ctx:DNPParser.LibraryDescriptionEntryFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#libraryDescriptionEntryFormat2.
    def visitLibraryDescriptionEntryFormat2(self, ctx:DNPParser.LibraryDescriptionEntryFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#libraryAttributeClauseFormat1.
    def visitLibraryAttributeClauseFormat1(self, ctx:DNPParser.LibraryAttributeClauseFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#libraryAttributeClauseFormat2.
    def visitLibraryAttributeClauseFormat2(self, ctx:DNPParser.LibraryAttributeClauseFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#libraryAttributeFunction.
    def visitLibraryAttributeFunction(self, ctx:DNPParser.LibraryAttributeFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#libraryAttributeParameter.
    def visitLibraryAttributeParameter(self, ctx:DNPParser.LibraryAttributeParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#libraryAttributeTitle.
    def visitLibraryAttributeTitle(self, ctx:DNPParser.LibraryAttributeTitleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#libraryEntryProcedureClauseFormat1.
    def visitLibraryEntryProcedureClauseFormat1(self, ctx:DNPParser.LibraryEntryProcedureClauseFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#libraryEntryProcedureClauseFormat2.
    def visitLibraryEntryProcedureClauseFormat2(self, ctx:DNPParser.LibraryEntryProcedureClauseFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#libraryEntryProcedureForClause.
    def visitLibraryEntryProcedureForClause(self, ctx:DNPParser.LibraryEntryProcedureForClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#libraryEntryProcedureGivingClause.
    def visitLibraryEntryProcedureGivingClause(self, ctx:DNPParser.LibraryEntryProcedureGivingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#libraryEntryProcedureUsingClause.
    def visitLibraryEntryProcedureUsingClause(self, ctx:DNPParser.LibraryEntryProcedureUsingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#libraryEntryProcedureUsingName.
    def visitLibraryEntryProcedureUsingName(self, ctx:DNPParser.LibraryEntryProcedureUsingNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#libraryEntryProcedureWithClause.
    def visitLibraryEntryProcedureWithClause(self, ctx:DNPParser.LibraryEntryProcedureWithClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#libraryEntryProcedureWithName.
    def visitLibraryEntryProcedureWithName(self, ctx:DNPParser.LibraryEntryProcedureWithNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#libraryIsCommonClause.
    def visitLibraryIsCommonClause(self, ctx:DNPParser.LibraryIsCommonClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#libraryIsGlobalClause.
    def visitLibraryIsGlobalClause(self, ctx:DNPParser.LibraryIsGlobalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataDescriptionEntry.
    def visitDataDescriptionEntry(self, ctx:DNPParser.DataDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#copyStatement.
    def visitCopyStatement(self, ctx:DNPParser.CopyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#copySource.
    def visitCopySource(self, ctx:DNPParser.CopySourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#copyLibrary.
    def visitCopyLibrary(self, ctx:DNPParser.CopyLibraryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#replacingPhrase.
    def visitReplacingPhrase(self, ctx:DNPParser.ReplacingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#changeStatement.
    def visitChangeStatement(self, ctx:DNPParser.ChangeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#changeFileAttribute.
    def visitChangeFileAttribute(self, ctx:DNPParser.ChangeFileAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#changeLibraryAttribute.
    def visitChangeLibraryAttribute(self, ctx:DNPParser.ChangeLibraryAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#libraryAttributeName.
    def visitLibraryAttributeName(self, ctx:DNPParser.LibraryAttributeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#libraryValueOption.
    def visitLibraryValueOption(self, ctx:DNPParser.LibraryValueOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#toValueOption.
    def visitToValueOption(self, ctx:DNPParser.ToValueOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#createStatement.
    def visitCreateStatement(self, ctx:DNPParser.CreateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#replaceOffStatement.
    def visitReplaceOffStatement(self, ctx:DNPParser.ReplaceOffStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#replaceClause.
    def visitReplaceClause(self, ctx:DNPParser.ReplaceClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#directoryPhrase.
    def visitDirectoryPhrase(self, ctx:DNPParser.DirectoryPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#familyPhrase.
    def visitFamilyPhrase(self, ctx:DNPParser.FamilyPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#replaceable.
    def visitReplaceable(self, ctx:DNPParser.ReplaceableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#replacement.
    def visitReplacement(self, ctx:DNPParser.ReplacementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#ejectStatement.
    def visitEjectStatement(self, ctx:DNPParser.EjectStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#skipStatement.
    def visitSkipStatement(self, ctx:DNPParser.SkipStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#titleStatement.
    def visitTitleStatement(self, ctx:DNPParser.TitleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#pseudoText.
    def visitPseudoText(self, ctx:DNPParser.PseudoTextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#charData.
    def visitCharData(self, ctx:DNPParser.CharDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#charDataSql.
    def visitCharDataSql(self, ctx:DNPParser.CharDataSqlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#charDataLine.
    def visitCharDataLine(self, ctx:DNPParser.CharDataLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#cobolWord.
    def visitCobolWord(self, ctx:DNPParser.CobolWordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#literal.
    def visitLiteral(self, ctx:DNPParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#jpEncodingText.
    def visitJpEncodingText(self, ctx:DNPParser.JpEncodingTextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#filename.
    def visitFilename(self, ctx:DNPParser.FilenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataDescriptionEntryFormat1.
    def visitDataDescriptionEntryFormat1(self, ctx:DNPParser.DataDescriptionEntryFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataDescriptionEntryFormat2.
    def visitDataDescriptionEntryFormat2(self, ctx:DNPParser.DataDescriptionEntryFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataDescriptionEntryFormat3.
    def visitDataDescriptionEntryFormat3(self, ctx:DNPParser.DataDescriptionEntryFormat3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataDescriptionEntryExecSql.
    def visitDataDescriptionEntryExecSql(self, ctx:DNPParser.DataDescriptionEntryExecSqlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataAlignedClause.
    def visitDataAlignedClause(self, ctx:DNPParser.DataAlignedClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataBlankWhenZeroClause.
    def visitDataBlankWhenZeroClause(self, ctx:DNPParser.DataBlankWhenZeroClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataCommonOwnLocalClause.
    def visitDataCommonOwnLocalClause(self, ctx:DNPParser.DataCommonOwnLocalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataExternalClause.
    def visitDataExternalClause(self, ctx:DNPParser.DataExternalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataGlobalClause.
    def visitDataGlobalClause(self, ctx:DNPParser.DataGlobalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataIntegerStringClause.
    def visitDataIntegerStringClause(self, ctx:DNPParser.DataIntegerStringClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataJustifiedClause.
    def visitDataJustifiedClause(self, ctx:DNPParser.DataJustifiedClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataOccursClause.
    def visitDataOccursClause(self, ctx:DNPParser.DataOccursClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataOccursTo.
    def visitDataOccursTo(self, ctx:DNPParser.DataOccursToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataOccursSort.
    def visitDataOccursSort(self, ctx:DNPParser.DataOccursSortContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataPictureClause.
    def visitDataPictureClause(self, ctx:DNPParser.DataPictureClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#pictureString.
    def visitPictureString(self, ctx:DNPParser.PictureStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#pictureChars.
    def visitPictureChars(self, ctx:DNPParser.PictureCharsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#pictureCardinality.
    def visitPictureCardinality(self, ctx:DNPParser.PictureCardinalityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataReceivedByClause.
    def visitDataReceivedByClause(self, ctx:DNPParser.DataReceivedByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataRecordAreaClause.
    def visitDataRecordAreaClause(self, ctx:DNPParser.DataRecordAreaClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataRedefinesClause.
    def visitDataRedefinesClause(self, ctx:DNPParser.DataRedefinesClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataRenamesClause.
    def visitDataRenamesClause(self, ctx:DNPParser.DataRenamesClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataSignClause.
    def visitDataSignClause(self, ctx:DNPParser.DataSignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataSynchronizedClause.
    def visitDataSynchronizedClause(self, ctx:DNPParser.DataSynchronizedClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataThreadLocalClause.
    def visitDataThreadLocalClause(self, ctx:DNPParser.DataThreadLocalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataTypeClause.
    def visitDataTypeClause(self, ctx:DNPParser.DataTypeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataTypeDefClause.
    def visitDataTypeDefClause(self, ctx:DNPParser.DataTypeDefClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataUsageClause.
    def visitDataUsageClause(self, ctx:DNPParser.DataUsageClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataUsingClause.
    def visitDataUsingClause(self, ctx:DNPParser.DataUsingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataValueClause.
    def visitDataValueClause(self, ctx:DNPParser.DataValueClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataValueInterval.
    def visitDataValueInterval(self, ctx:DNPParser.DataValueIntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataValueIntervalFrom.
    def visitDataValueIntervalFrom(self, ctx:DNPParser.DataValueIntervalFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataValueIntervalTo.
    def visitDataValueIntervalTo(self, ctx:DNPParser.DataValueIntervalToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataWithLowerBoundsClause.
    def visitDataWithLowerBoundsClause(self, ctx:DNPParser.DataWithLowerBoundsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#procedureDivision.
    def visitProcedureDivision(self, ctx:DNPParser.ProcedureDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#procedureDivisionUsingClause.
    def visitProcedureDivisionUsingClause(self, ctx:DNPParser.ProcedureDivisionUsingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#procedureDivisionGivingClause.
    def visitProcedureDivisionGivingClause(self, ctx:DNPParser.ProcedureDivisionGivingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#procedureDivisionUsingParameter.
    def visitProcedureDivisionUsingParameter(self, ctx:DNPParser.ProcedureDivisionUsingParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#procedureDivisionByReferencePhrase.
    def visitProcedureDivisionByReferencePhrase(self, ctx:DNPParser.ProcedureDivisionByReferencePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#procedureDivisionByReference.
    def visitProcedureDivisionByReference(self, ctx:DNPParser.ProcedureDivisionByReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#procedureDivisionByValuePhrase.
    def visitProcedureDivisionByValuePhrase(self, ctx:DNPParser.ProcedureDivisionByValuePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#procedureDivisionByValue.
    def visitProcedureDivisionByValue(self, ctx:DNPParser.ProcedureDivisionByValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#procedureDeclaratives.
    def visitProcedureDeclaratives(self, ctx:DNPParser.ProcedureDeclarativesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#procedureDeclarative.
    def visitProcedureDeclarative(self, ctx:DNPParser.ProcedureDeclarativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#procedureSectionHeader.
    def visitProcedureSectionHeader(self, ctx:DNPParser.ProcedureSectionHeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#procedureDivisionBody.
    def visitProcedureDivisionBody(self, ctx:DNPParser.ProcedureDivisionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#procedureSection.
    def visitProcedureSection(self, ctx:DNPParser.ProcedureSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#paragraphs.
    def visitParagraphs(self, ctx:DNPParser.ParagraphsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#paragraph.
    def visitParagraph(self, ctx:DNPParser.ParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#sentence.
    def visitSentence(self, ctx:DNPParser.SentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#statement.
    def visitStatement(self, ctx:DNPParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#execCicsStatement2.
    def visitExecCicsStatement2(self, ctx:DNPParser.ExecCicsStatement2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#acceptStatement.
    def visitAcceptStatement(self, ctx:DNPParser.AcceptStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#acceptFromDateStatement.
    def visitAcceptFromDateStatement(self, ctx:DNPParser.AcceptFromDateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#acceptFromDatePhrase.
    def visitAcceptFromDatePhrase(self, ctx:DNPParser.AcceptFromDatePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#acceptFromMnemonicStatement.
    def visitAcceptFromMnemonicStatement(self, ctx:DNPParser.AcceptFromMnemonicStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#acceptFromEscapeKeyStatement.
    def visitAcceptFromEscapeKeyStatement(self, ctx:DNPParser.AcceptFromEscapeKeyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#acceptMessageCountStatement.
    def visitAcceptMessageCountStatement(self, ctx:DNPParser.AcceptMessageCountStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#addStatement.
    def visitAddStatement(self, ctx:DNPParser.AddStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#addToStatement.
    def visitAddToStatement(self, ctx:DNPParser.AddToStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#addToGivingStatement.
    def visitAddToGivingStatement(self, ctx:DNPParser.AddToGivingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#addCorrespondingStatement.
    def visitAddCorrespondingStatement(self, ctx:DNPParser.AddCorrespondingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#addFrom.
    def visitAddFrom(self, ctx:DNPParser.AddFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#addTo.
    def visitAddTo(self, ctx:DNPParser.AddToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#addToGiving.
    def visitAddToGiving(self, ctx:DNPParser.AddToGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#addGiving.
    def visitAddGiving(self, ctx:DNPParser.AddGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#alteredGoTo.
    def visitAlteredGoTo(self, ctx:DNPParser.AlteredGoToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#alterStatement.
    def visitAlterStatement(self, ctx:DNPParser.AlterStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#alterProceedTo.
    def visitAlterProceedTo(self, ctx:DNPParser.AlterProceedToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#attachStatement.
    def visitAttachStatement(self, ctx:DNPParser.AttachStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#callStatement.
    def visitCallStatement(self, ctx:DNPParser.CallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#callUsingPhrase.
    def visitCallUsingPhrase(self, ctx:DNPParser.CallUsingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#callUsingParameter.
    def visitCallUsingParameter(self, ctx:DNPParser.CallUsingParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#callByReferencePhrase.
    def visitCallByReferencePhrase(self, ctx:DNPParser.CallByReferencePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#callByReference.
    def visitCallByReference(self, ctx:DNPParser.CallByReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#callByValuePhrase.
    def visitCallByValuePhrase(self, ctx:DNPParser.CallByValuePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#callByValue.
    def visitCallByValue(self, ctx:DNPParser.CallByValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#callByContentPhrase.
    def visitCallByContentPhrase(self, ctx:DNPParser.CallByContentPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#callByContent.
    def visitCallByContent(self, ctx:DNPParser.CallByContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#callGivingPhrase.
    def visitCallGivingPhrase(self, ctx:DNPParser.CallGivingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#callSystem.
    def visitCallSystem(self, ctx:DNPParser.CallSystemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#cancelStatement.
    def visitCancelStatement(self, ctx:DNPParser.CancelStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#cancelCall.
    def visitCancelCall(self, ctx:DNPParser.CancelCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#closeStatement.
    def visitCloseStatement(self, ctx:DNPParser.CloseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#closePhrase.
    def visitClosePhrase(self, ctx:DNPParser.ClosePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#closeFile.
    def visitCloseFile(self, ctx:DNPParser.CloseFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#closeReelUnitStatement.
    def visitCloseReelUnitStatement(self, ctx:DNPParser.CloseReelUnitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#closeRelativeStatement.
    def visitCloseRelativeStatement(self, ctx:DNPParser.CloseRelativeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#closePortFileIOStatement.
    def visitClosePortFileIOStatement(self, ctx:DNPParser.ClosePortFileIOStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#closePortFileIOUsing.
    def visitClosePortFileIOUsing(self, ctx:DNPParser.ClosePortFileIOUsingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#closePortFileIOUsingCloseDisposition.
    def visitClosePortFileIOUsingCloseDisposition(self, ctx:DNPParser.ClosePortFileIOUsingCloseDispositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#closePortFileIOUsingAssociatedData.
    def visitClosePortFileIOUsingAssociatedData(self, ctx:DNPParser.ClosePortFileIOUsingAssociatedDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#closePortFileIOUsingAssociatedDataLength.
    def visitClosePortFileIOUsingAssociatedDataLength(self, ctx:DNPParser.ClosePortFileIOUsingAssociatedDataLengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#computeStatement.
    def visitComputeStatement(self, ctx:DNPParser.ComputeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#computeStore.
    def visitComputeStore(self, ctx:DNPParser.ComputeStoreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#continueStatement.
    def visitContinueStatement(self, ctx:DNPParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#continueIndicator.
    def visitContinueIndicator(self, ctx:DNPParser.ContinueIndicatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#deleteStatement.
    def visitDeleteStatement(self, ctx:DNPParser.DeleteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#disableStatement.
    def visitDisableStatement(self, ctx:DNPParser.DisableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#displayStatement.
    def visitDisplayStatement(self, ctx:DNPParser.DisplayStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#displayOperand.
    def visitDisplayOperand(self, ctx:DNPParser.DisplayOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#displayAt.
    def visitDisplayAt(self, ctx:DNPParser.DisplayAtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#displayUpon.
    def visitDisplayUpon(self, ctx:DNPParser.DisplayUponContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#displayWith.
    def visitDisplayWith(self, ctx:DNPParser.DisplayWithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#divideStatement.
    def visitDivideStatement(self, ctx:DNPParser.DivideStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#divideIntoStatement.
    def visitDivideIntoStatement(self, ctx:DNPParser.DivideIntoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#divideIntoGivingStatement.
    def visitDivideIntoGivingStatement(self, ctx:DNPParser.DivideIntoGivingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#divideByGivingStatement.
    def visitDivideByGivingStatement(self, ctx:DNPParser.DivideByGivingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#divideGivingPhrase.
    def visitDivideGivingPhrase(self, ctx:DNPParser.DivideGivingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#divideInto.
    def visitDivideInto(self, ctx:DNPParser.DivideIntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#divideGiving.
    def visitDivideGiving(self, ctx:DNPParser.DivideGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#divideRemainder.
    def visitDivideRemainder(self, ctx:DNPParser.DivideRemainderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#enableStatement.
    def visitEnableStatement(self, ctx:DNPParser.EnableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#entryStatement.
    def visitEntryStatement(self, ctx:DNPParser.EntryStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#evaluateStatement.
    def visitEvaluateStatement(self, ctx:DNPParser.EvaluateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#evaluateSelect.
    def visitEvaluateSelect(self, ctx:DNPParser.EvaluateSelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#evaluateAlsoSelect.
    def visitEvaluateAlsoSelect(self, ctx:DNPParser.EvaluateAlsoSelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#evaluateWhenPhrase.
    def visitEvaluateWhenPhrase(self, ctx:DNPParser.EvaluateWhenPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#evaluateWhen.
    def visitEvaluateWhen(self, ctx:DNPParser.EvaluateWhenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#evaluateCondition.
    def visitEvaluateCondition(self, ctx:DNPParser.EvaluateConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#evaluateThrough.
    def visitEvaluateThrough(self, ctx:DNPParser.EvaluateThroughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#evaluateAlsoCondition.
    def visitEvaluateAlsoCondition(self, ctx:DNPParser.EvaluateAlsoConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#evaluateWhenOther.
    def visitEvaluateWhenOther(self, ctx:DNPParser.EvaluateWhenOtherContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#evaluateValue.
    def visitEvaluateValue(self, ctx:DNPParser.EvaluateValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#execCicsStatement.
    def visitExecCicsStatement(self, ctx:DNPParser.ExecCicsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#execSqlStatement.
    def visitExecSqlStatement(self, ctx:DNPParser.ExecSqlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#execSqlImsStatement.
    def visitExecSqlImsStatement(self, ctx:DNPParser.ExecSqlImsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#exhibitStatement.
    def visitExhibitStatement(self, ctx:DNPParser.ExhibitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#exhibitOperand.
    def visitExhibitOperand(self, ctx:DNPParser.ExhibitOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#exitStatement.
    def visitExitStatement(self, ctx:DNPParser.ExitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#findStatement.
    def visitFindStatement(self, ctx:DNPParser.FindStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#viaClause.
    def visitViaClause(self, ctx:DNPParser.ViaClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#findOption.
    def visitFindOption(self, ctx:DNPParser.FindOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#freeStatement.
    def visitFreeStatement(self, ctx:DNPParser.FreeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#generateStatement.
    def visitGenerateStatement(self, ctx:DNPParser.GenerateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#gobackStatement.
    def visitGobackStatement(self, ctx:DNPParser.GobackStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#goToStatement.
    def visitGoToStatement(self, ctx:DNPParser.GoToStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#goToStatementSimple.
    def visitGoToStatementSimple(self, ctx:DNPParser.GoToStatementSimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#goToDependingOnStatement.
    def visitGoToDependingOnStatement(self, ctx:DNPParser.GoToDependingOnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#ifStatement.
    def visitIfStatement(self, ctx:DNPParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#ifThen.
    def visitIfThen(self, ctx:DNPParser.IfThenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#ifElse.
    def visitIfElse(self, ctx:DNPParser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#initializeStatement.
    def visitInitializeStatement(self, ctx:DNPParser.InitializeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#initializeReplacingPhrase.
    def visitInitializeReplacingPhrase(self, ctx:DNPParser.InitializeReplacingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#initializeReplacingBy.
    def visitInitializeReplacingBy(self, ctx:DNPParser.InitializeReplacingByContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#initiateStatement.
    def visitInitiateStatement(self, ctx:DNPParser.InitiateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#inspectStatement.
    def visitInspectStatement(self, ctx:DNPParser.InspectStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#inspectTallyingPhrase.
    def visitInspectTallyingPhrase(self, ctx:DNPParser.InspectTallyingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#inspectReplacingPhrase.
    def visitInspectReplacingPhrase(self, ctx:DNPParser.InspectReplacingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#inspectTallyingReplacingPhrase.
    def visitInspectTallyingReplacingPhrase(self, ctx:DNPParser.InspectTallyingReplacingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#inspectConvertingPhrase.
    def visitInspectConvertingPhrase(self, ctx:DNPParser.InspectConvertingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#inspectFor.
    def visitInspectFor(self, ctx:DNPParser.InspectForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#inspectCharacters.
    def visitInspectCharacters(self, ctx:DNPParser.InspectCharactersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#inspectReplacingCharacters.
    def visitInspectReplacingCharacters(self, ctx:DNPParser.InspectReplacingCharactersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#inspectAllLeadings.
    def visitInspectAllLeadings(self, ctx:DNPParser.InspectAllLeadingsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#inspectReplacingAllLeadings.
    def visitInspectReplacingAllLeadings(self, ctx:DNPParser.InspectReplacingAllLeadingsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#inspectAllLeading.
    def visitInspectAllLeading(self, ctx:DNPParser.InspectAllLeadingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#inspectReplacingAllLeading.
    def visitInspectReplacingAllLeading(self, ctx:DNPParser.InspectReplacingAllLeadingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#inspectBy.
    def visitInspectBy(self, ctx:DNPParser.InspectByContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#inspectTo.
    def visitInspectTo(self, ctx:DNPParser.InspectToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#inspectBeforeAfter.
    def visitInspectBeforeAfter(self, ctx:DNPParser.InspectBeforeAfterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#lockStatement.
    def visitLockStatement(self, ctx:DNPParser.LockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#mergeStatement.
    def visitMergeStatement(self, ctx:DNPParser.MergeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#mergeOnKeyClause.
    def visitMergeOnKeyClause(self, ctx:DNPParser.MergeOnKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#mergeCollatingSequencePhrase.
    def visitMergeCollatingSequencePhrase(self, ctx:DNPParser.MergeCollatingSequencePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#mergeCollatingAlphanumeric.
    def visitMergeCollatingAlphanumeric(self, ctx:DNPParser.MergeCollatingAlphanumericContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#mergeCollatingNational.
    def visitMergeCollatingNational(self, ctx:DNPParser.MergeCollatingNationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#mergeUsing.
    def visitMergeUsing(self, ctx:DNPParser.MergeUsingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#mergeOutputProcedurePhrase.
    def visitMergeOutputProcedurePhrase(self, ctx:DNPParser.MergeOutputProcedurePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#mergeOutputThrough.
    def visitMergeOutputThrough(self, ctx:DNPParser.MergeOutputThroughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#mergeGivingPhrase.
    def visitMergeGivingPhrase(self, ctx:DNPParser.MergeGivingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#mergeGiving.
    def visitMergeGiving(self, ctx:DNPParser.MergeGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#moveStatement.
    def visitMoveStatement(self, ctx:DNPParser.MoveStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#moveToStatement.
    def visitMoveToStatement(self, ctx:DNPParser.MoveToStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#moveToSendingArea.
    def visitMoveToSendingArea(self, ctx:DNPParser.MoveToSendingAreaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#moveCorrespondingToStatement.
    def visitMoveCorrespondingToStatement(self, ctx:DNPParser.MoveCorrespondingToStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#moveCorrespondingToSendingArea.
    def visitMoveCorrespondingToSendingArea(self, ctx:DNPParser.MoveCorrespondingToSendingAreaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#moveAttributeClause.
    def visitMoveAttributeClause(self, ctx:DNPParser.MoveAttributeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#modifyStatement.
    def visitModifyStatement(self, ctx:DNPParser.ModifyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#modifyTo.
    def visitModifyTo(self, ctx:DNPParser.ModifyToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#modifyOption.
    def visitModifyOption(self, ctx:DNPParser.ModifyOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#multiplyStatement.
    def visitMultiplyStatement(self, ctx:DNPParser.MultiplyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#multiplyRegular.
    def visitMultiplyRegular(self, ctx:DNPParser.MultiplyRegularContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#multiplyRegularOperand.
    def visitMultiplyRegularOperand(self, ctx:DNPParser.MultiplyRegularOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#multiplyGiving.
    def visitMultiplyGiving(self, ctx:DNPParser.MultiplyGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#multiplyGivingOperand.
    def visitMultiplyGivingOperand(self, ctx:DNPParser.MultiplyGivingOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#multiplyGivingResult.
    def visitMultiplyGivingResult(self, ctx:DNPParser.MultiplyGivingResultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#openStatement.
    def visitOpenStatement(self, ctx:DNPParser.OpenStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#openInputStatement.
    def visitOpenInputStatement(self, ctx:DNPParser.OpenInputStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#openInput.
    def visitOpenInput(self, ctx:DNPParser.OpenInputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#openUpdateStatement.
    def visitOpenUpdateStatement(self, ctx:DNPParser.OpenUpdateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#openOutputStatement.
    def visitOpenOutputStatement(self, ctx:DNPParser.OpenOutputStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#openOutput.
    def visitOpenOutput(self, ctx:DNPParser.OpenOutputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#openIOStatement.
    def visitOpenIOStatement(self, ctx:DNPParser.OpenIOStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#openInquiry.
    def visitOpenInquiry(self, ctx:DNPParser.OpenInquiryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#openExtendStatement.
    def visitOpenExtendStatement(self, ctx:DNPParser.OpenExtendStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#performStatement.
    def visitPerformStatement(self, ctx:DNPParser.PerformStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#performInlineStatement.
    def visitPerformInlineStatement(self, ctx:DNPParser.PerformInlineStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#performProcedureStatement.
    def visitPerformProcedureStatement(self, ctx:DNPParser.PerformProcedureStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#performType.
    def visitPerformType(self, ctx:DNPParser.PerformTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#performTimes.
    def visitPerformTimes(self, ctx:DNPParser.PerformTimesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#performUntil.
    def visitPerformUntil(self, ctx:DNPParser.PerformUntilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#performVarying.
    def visitPerformVarying(self, ctx:DNPParser.PerformVaryingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#performVaryingClause.
    def visitPerformVaryingClause(self, ctx:DNPParser.PerformVaryingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#performVaryingPhrase.
    def visitPerformVaryingPhrase(self, ctx:DNPParser.PerformVaryingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#performAfter.
    def visitPerformAfter(self, ctx:DNPParser.PerformAfterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#performFrom.
    def visitPerformFrom(self, ctx:DNPParser.PerformFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#performBy.
    def visitPerformBy(self, ctx:DNPParser.PerformByContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#performTestClause.
    def visitPerformTestClause(self, ctx:DNPParser.PerformTestClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#purgeStatement.
    def visitPurgeStatement(self, ctx:DNPParser.PurgeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#readStatement.
    def visitReadStatement(self, ctx:DNPParser.ReadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#readInto.
    def visitReadInto(self, ctx:DNPParser.ReadIntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#readWith.
    def visitReadWith(self, ctx:DNPParser.ReadWithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#readKey.
    def visitReadKey(self, ctx:DNPParser.ReadKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#receiveStatement.
    def visitReceiveStatement(self, ctx:DNPParser.ReceiveStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#receiveFromStatement.
    def visitReceiveFromStatement(self, ctx:DNPParser.ReceiveFromStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#receiveFrom.
    def visitReceiveFrom(self, ctx:DNPParser.ReceiveFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#receiveIntoStatement.
    def visitReceiveIntoStatement(self, ctx:DNPParser.ReceiveIntoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#receiveNoData.
    def visitReceiveNoData(self, ctx:DNPParser.ReceiveNoDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#receiveWithData.
    def visitReceiveWithData(self, ctx:DNPParser.ReceiveWithDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#receiveBefore.
    def visitReceiveBefore(self, ctx:DNPParser.ReceiveBeforeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#receiveWith.
    def visitReceiveWith(self, ctx:DNPParser.ReceiveWithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#receiveThread.
    def visitReceiveThread(self, ctx:DNPParser.ReceiveThreadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#receiveSize.
    def visitReceiveSize(self, ctx:DNPParser.ReceiveSizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#receiveStatus.
    def visitReceiveStatus(self, ctx:DNPParser.ReceiveStatusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#releaseStatement.
    def visitReleaseStatement(self, ctx:DNPParser.ReleaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#returnStatement.
    def visitReturnStatement(self, ctx:DNPParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#returnInto.
    def visitReturnInto(self, ctx:DNPParser.ReturnIntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#rewriteStatement.
    def visitRewriteStatement(self, ctx:DNPParser.RewriteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#rewriteFrom.
    def visitRewriteFrom(self, ctx:DNPParser.RewriteFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#searchStatement.
    def visitSearchStatement(self, ctx:DNPParser.SearchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#searchVarying.
    def visitSearchVarying(self, ctx:DNPParser.SearchVaryingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#searchWhen.
    def visitSearchWhen(self, ctx:DNPParser.SearchWhenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#sendStatement.
    def visitSendStatement(self, ctx:DNPParser.SendStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#sendStatementSync.
    def visitSendStatementSync(self, ctx:DNPParser.SendStatementSyncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#sendStatementAsync.
    def visitSendStatementAsync(self, ctx:DNPParser.SendStatementAsyncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#sendFromPhrase.
    def visitSendFromPhrase(self, ctx:DNPParser.SendFromPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#sendWithPhrase.
    def visitSendWithPhrase(self, ctx:DNPParser.SendWithPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#sendReplacingPhrase.
    def visitSendReplacingPhrase(self, ctx:DNPParser.SendReplacingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#sendAdvancingPhrase.
    def visitSendAdvancingPhrase(self, ctx:DNPParser.SendAdvancingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#sendAdvancingPage.
    def visitSendAdvancingPage(self, ctx:DNPParser.SendAdvancingPageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#sendAdvancingLines.
    def visitSendAdvancingLines(self, ctx:DNPParser.SendAdvancingLinesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#sendAdvancingMnemonic.
    def visitSendAdvancingMnemonic(self, ctx:DNPParser.SendAdvancingMnemonicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#setStatement.
    def visitSetStatement(self, ctx:DNPParser.SetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#setToStatement.
    def visitSetToStatement(self, ctx:DNPParser.SetToStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#setUpDownByStatement.
    def visitSetUpDownByStatement(self, ctx:DNPParser.SetUpDownByStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#setTo.
    def visitSetTo(self, ctx:DNPParser.SetToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#setToValue.
    def visitSetToValue(self, ctx:DNPParser.SetToValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#setByValue.
    def visitSetByValue(self, ctx:DNPParser.SetByValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#sortStatement.
    def visitSortStatement(self, ctx:DNPParser.SortStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#sortOptional.
    def visitSortOptional(self, ctx:DNPParser.SortOptionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#sortOnKeyClause.
    def visitSortOnKeyClause(self, ctx:DNPParser.SortOnKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#sortDuplicatesPhrase.
    def visitSortDuplicatesPhrase(self, ctx:DNPParser.SortDuplicatesPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#sortCollatingSequencePhrase.
    def visitSortCollatingSequencePhrase(self, ctx:DNPParser.SortCollatingSequencePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#sortCollatingAlphanumeric.
    def visitSortCollatingAlphanumeric(self, ctx:DNPParser.SortCollatingAlphanumericContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#sortCollatingNational.
    def visitSortCollatingNational(self, ctx:DNPParser.SortCollatingNationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#sortInputProcedurePhrase.
    def visitSortInputProcedurePhrase(self, ctx:DNPParser.SortInputProcedurePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#sortInputThrough.
    def visitSortInputThrough(self, ctx:DNPParser.SortInputThroughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#sortUsing.
    def visitSortUsing(self, ctx:DNPParser.SortUsingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#sortOutputProcedurePhrase.
    def visitSortOutputProcedurePhrase(self, ctx:DNPParser.SortOutputProcedurePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#sortOutputThrough.
    def visitSortOutputThrough(self, ctx:DNPParser.SortOutputThroughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#sortGivingPhrase.
    def visitSortGivingPhrase(self, ctx:DNPParser.SortGivingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#sortGiving.
    def visitSortGiving(self, ctx:DNPParser.SortGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#startStatement.
    def visitStartStatement(self, ctx:DNPParser.StartStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#startKey.
    def visitStartKey(self, ctx:DNPParser.StartKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#stopStatement.
    def visitStopStatement(self, ctx:DNPParser.StopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#stopOption.
    def visitStopOption(self, ctx:DNPParser.StopOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#storeStatement.
    def visitStoreStatement(self, ctx:DNPParser.StoreStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#stringStatement.
    def visitStringStatement(self, ctx:DNPParser.StringStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#stringSendingPhrase.
    def visitStringSendingPhrase(self, ctx:DNPParser.StringSendingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#stringSending.
    def visitStringSending(self, ctx:DNPParser.StringSendingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#stringDelimitedByPhrase.
    def visitStringDelimitedByPhrase(self, ctx:DNPParser.StringDelimitedByPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#stringForPhrase.
    def visitStringForPhrase(self, ctx:DNPParser.StringForPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#stringIntoPhrase.
    def visitStringIntoPhrase(self, ctx:DNPParser.StringIntoPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#stringWithPointerPhrase.
    def visitStringWithPointerPhrase(self, ctx:DNPParser.StringWithPointerPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#subtractStatement.
    def visitSubtractStatement(self, ctx:DNPParser.SubtractStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#subtractFromStatement.
    def visitSubtractFromStatement(self, ctx:DNPParser.SubtractFromStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#subtractFromGivingStatement.
    def visitSubtractFromGivingStatement(self, ctx:DNPParser.SubtractFromGivingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#subtractCorrespondingStatement.
    def visitSubtractCorrespondingStatement(self, ctx:DNPParser.SubtractCorrespondingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#subtractSubtrahend.
    def visitSubtractSubtrahend(self, ctx:DNPParser.SubtractSubtrahendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#subtractMinuend.
    def visitSubtractMinuend(self, ctx:DNPParser.SubtractMinuendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#subtractMinuendGiving.
    def visitSubtractMinuendGiving(self, ctx:DNPParser.SubtractMinuendGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#subtractGiving.
    def visitSubtractGiving(self, ctx:DNPParser.SubtractGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#subtractMinuendCorresponding.
    def visitSubtractMinuendCorresponding(self, ctx:DNPParser.SubtractMinuendCorrespondingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#transactionStatement.
    def visitTransactionStatement(self, ctx:DNPParser.TransactionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#transactionBegin.
    def visitTransactionBegin(self, ctx:DNPParser.TransactionBeginContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#transactionCancel.
    def visitTransactionCancel(self, ctx:DNPParser.TransactionCancelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#transactionEnd.
    def visitTransactionEnd(self, ctx:DNPParser.TransactionEndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#terminateStatement.
    def visitTerminateStatement(self, ctx:DNPParser.TerminateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#unstringStatement.
    def visitUnstringStatement(self, ctx:DNPParser.UnstringStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#unstringSendingPhrase.
    def visitUnstringSendingPhrase(self, ctx:DNPParser.UnstringSendingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#unstringDelimitedByPhrase.
    def visitUnstringDelimitedByPhrase(self, ctx:DNPParser.UnstringDelimitedByPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#unstringOrAllPhrase.
    def visitUnstringOrAllPhrase(self, ctx:DNPParser.UnstringOrAllPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#unstringIntoPhrase.
    def visitUnstringIntoPhrase(self, ctx:DNPParser.UnstringIntoPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#unstringInto.
    def visitUnstringInto(self, ctx:DNPParser.UnstringIntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#unstringDelimiterIn.
    def visitUnstringDelimiterIn(self, ctx:DNPParser.UnstringDelimiterInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#unstringCountIn.
    def visitUnstringCountIn(self, ctx:DNPParser.UnstringCountInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#unstringWithPointerPhrase.
    def visitUnstringWithPointerPhrase(self, ctx:DNPParser.UnstringWithPointerPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#unstringTallyingPhrase.
    def visitUnstringTallyingPhrase(self, ctx:DNPParser.UnstringTallyingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#useStatement.
    def visitUseStatement(self, ctx:DNPParser.UseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#useAfterClause.
    def visitUseAfterClause(self, ctx:DNPParser.UseAfterClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#useAfterOn.
    def visitUseAfterOn(self, ctx:DNPParser.UseAfterOnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#useDebugClause.
    def visitUseDebugClause(self, ctx:DNPParser.UseDebugClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#useDebugOn.
    def visitUseDebugOn(self, ctx:DNPParser.UseDebugOnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#useDeadLock.
    def visitUseDeadLock(self, ctx:DNPParser.UseDeadLockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#useProcedure.
    def visitUseProcedure(self, ctx:DNPParser.UseProcedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#waitStatement.
    def visitWaitStatement(self, ctx:DNPParser.WaitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#waitArithmeticExpression.
    def visitWaitArithmeticExpression(self, ctx:DNPParser.WaitArithmeticExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#attributeChangeEvent.
    def visitAttributeChangeEvent(self, ctx:DNPParser.AttributeChangeEventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#attributeInputEvent.
    def visitAttributeInputEvent(self, ctx:DNPParser.AttributeInputEventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#attributeOutputEvent.
    def visitAttributeOutputEvent(self, ctx:DNPParser.AttributeOutputEventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#attributeAcceptEvent.
    def visitAttributeAcceptEvent(self, ctx:DNPParser.AttributeAcceptEventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#attributeExceptionEvent.
    def visitAttributeExceptionEvent(self, ctx:DNPParser.AttributeExceptionEventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#eventIdentifier.
    def visitEventIdentifier(self, ctx:DNPParser.EventIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#crcrEvent.
    def visitCrcrEvent(self, ctx:DNPParser.CrcrEventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#odtInputPresent.
    def visitOdtInputPresent(self, ctx:DNPParser.OdtInputPresentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#readOk.
    def visitReadOk(self, ctx:DNPParser.ReadOkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#writeOk.
    def visitWriteOk(self, ctx:DNPParser.WriteOkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#stoqEvent.
    def visitStoqEvent(self, ctx:DNPParser.StoqEventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#writeStatement.
    def visitWriteStatement(self, ctx:DNPParser.WriteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#writeFromPhrase.
    def visitWriteFromPhrase(self, ctx:DNPParser.WriteFromPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#writeAdvancingPhrase.
    def visitWriteAdvancingPhrase(self, ctx:DNPParser.WriteAdvancingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#writeAdvancingPage.
    def visitWriteAdvancingPage(self, ctx:DNPParser.WriteAdvancingPageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#writeAdvancingLines.
    def visitWriteAdvancingLines(self, ctx:DNPParser.WriteAdvancingLinesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#writeAdvancingMnemonic.
    def visitWriteAdvancingMnemonic(self, ctx:DNPParser.WriteAdvancingMnemonicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#writeAtEndOfPagePhrase.
    def visitWriteAtEndOfPagePhrase(self, ctx:DNPParser.WriteAtEndOfPagePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#writeNotAtEndOfPagePhrase.
    def visitWriteNotAtEndOfPagePhrase(self, ctx:DNPParser.WriteNotAtEndOfPagePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#atEndPhrase.
    def visitAtEndPhrase(self, ctx:DNPParser.AtEndPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#notAtEndPhrase.
    def visitNotAtEndPhrase(self, ctx:DNPParser.NotAtEndPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#invalidKeyPhrase.
    def visitInvalidKeyPhrase(self, ctx:DNPParser.InvalidKeyPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#notInvalidKeyPhrase.
    def visitNotInvalidKeyPhrase(self, ctx:DNPParser.NotInvalidKeyPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#onOverflowPhrase.
    def visitOnOverflowPhrase(self, ctx:DNPParser.OnOverflowPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#notOnOverflowPhrase.
    def visitNotOnOverflowPhrase(self, ctx:DNPParser.NotOnOverflowPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#onSizeErrorPhrase.
    def visitOnSizeErrorPhrase(self, ctx:DNPParser.OnSizeErrorPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#notOnSizeErrorPhrase.
    def visitNotOnSizeErrorPhrase(self, ctx:DNPParser.NotOnSizeErrorPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#onExceptionClause.
    def visitOnExceptionClause(self, ctx:DNPParser.OnExceptionClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#notOnExceptionClause.
    def visitNotOnExceptionClause(self, ctx:DNPParser.NotOnExceptionClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#arithmeticExpression.
    def visitArithmeticExpression(self, ctx:DNPParser.ArithmeticExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#plusMinus.
    def visitPlusMinus(self, ctx:DNPParser.PlusMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#multDivs.
    def visitMultDivs(self, ctx:DNPParser.MultDivsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#multDiv.
    def visitMultDiv(self, ctx:DNPParser.MultDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#powers.
    def visitPowers(self, ctx:DNPParser.PowersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#power.
    def visitPower(self, ctx:DNPParser.PowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#basis.
    def visitBasis(self, ctx:DNPParser.BasisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#condition.
    def visitCondition(self, ctx:DNPParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#andOrCondition.
    def visitAndOrCondition(self, ctx:DNPParser.AndOrConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#combinableCondition.
    def visitCombinableCondition(self, ctx:DNPParser.CombinableConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#simpleCondition.
    def visitSimpleCondition(self, ctx:DNPParser.SimpleConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#classCondition.
    def visitClassCondition(self, ctx:DNPParser.ClassConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#conditionNameReference.
    def visitConditionNameReference(self, ctx:DNPParser.ConditionNameReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#conditionNameSubscriptReference.
    def visitConditionNameSubscriptReference(self, ctx:DNPParser.ConditionNameSubscriptReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#attributeCondition.
    def visitAttributeCondition(self, ctx:DNPParser.AttributeConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#attributeConditionExpr.
    def visitAttributeConditionExpr(self, ctx:DNPParser.AttributeConditionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#relationCondition.
    def visitRelationCondition(self, ctx:DNPParser.RelationConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#relationSignCondition.
    def visitRelationSignCondition(self, ctx:DNPParser.RelationSignConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#relationArithmeticComparison.
    def visitRelationArithmeticComparison(self, ctx:DNPParser.RelationArithmeticComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#relationCombinedComparison.
    def visitRelationCombinedComparison(self, ctx:DNPParser.RelationCombinedComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#relationCombinedCondition.
    def visitRelationCombinedCondition(self, ctx:DNPParser.RelationCombinedConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#relationalOperator.
    def visitRelationalOperator(self, ctx:DNPParser.RelationalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#abbreviation.
    def visitAbbreviation(self, ctx:DNPParser.AbbreviationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#identifier.
    def visitIdentifier(self, ctx:DNPParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#tableCall.
    def visitTableCall(self, ctx:DNPParser.TableCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#functionCall.
    def visitFunctionCall(self, ctx:DNPParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#referenceModifier.
    def visitReferenceModifier(self, ctx:DNPParser.ReferenceModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#characterPosition.
    def visitCharacterPosition(self, ctx:DNPParser.CharacterPositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#length.
    def visitLength(self, ctx:DNPParser.LengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#subscript_.
    def visitSubscript_(self, ctx:DNPParser.Subscript_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#argument.
    def visitArgument(self, ctx:DNPParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#qualifiedDataName.
    def visitQualifiedDataName(self, ctx:DNPParser.QualifiedDataNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#qualifiedDataNameFormat1.
    def visitQualifiedDataNameFormat1(self, ctx:DNPParser.QualifiedDataNameFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#qualifiedDataNameFormat2.
    def visitQualifiedDataNameFormat2(self, ctx:DNPParser.QualifiedDataNameFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#qualifiedDataNameFormat3.
    def visitQualifiedDataNameFormat3(self, ctx:DNPParser.QualifiedDataNameFormat3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#qualifiedDataNameFormat4.
    def visitQualifiedDataNameFormat4(self, ctx:DNPParser.QualifiedDataNameFormat4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#qualifiedInData.
    def visitQualifiedInData(self, ctx:DNPParser.QualifiedInDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#inData.
    def visitInData(self, ctx:DNPParser.InDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#inFile.
    def visitInFile(self, ctx:DNPParser.InFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#inMnemonic.
    def visitInMnemonic(self, ctx:DNPParser.InMnemonicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#inSection.
    def visitInSection(self, ctx:DNPParser.InSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#inLibrary.
    def visitInLibrary(self, ctx:DNPParser.InLibraryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#inTable.
    def visitInTable(self, ctx:DNPParser.InTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#alphabetName.
    def visitAlphabetName(self, ctx:DNPParser.AlphabetNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#assignmentName.
    def visitAssignmentName(self, ctx:DNPParser.AssignmentNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#basisName.
    def visitBasisName(self, ctx:DNPParser.BasisNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#cdName.
    def visitCdName(self, ctx:DNPParser.CdNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#className.
    def visitClassName(self, ctx:DNPParser.ClassNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#computerName.
    def visitComputerName(self, ctx:DNPParser.ComputerNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#conditionName.
    def visitConditionName(self, ctx:DNPParser.ConditionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataName.
    def visitDataName(self, ctx:DNPParser.DataNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#dataDescName.
    def visitDataDescName(self, ctx:DNPParser.DataDescNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#environmentName.
    def visitEnvironmentName(self, ctx:DNPParser.EnvironmentNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#fileAttribute.
    def visitFileAttribute(self, ctx:DNPParser.FileAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#fileName.
    def visitFileName(self, ctx:DNPParser.FileNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#functionName.
    def visitFunctionName(self, ctx:DNPParser.FunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#indexName.
    def visitIndexName(self, ctx:DNPParser.IndexNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#languageName.
    def visitLanguageName(self, ctx:DNPParser.LanguageNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#libraryName.
    def visitLibraryName(self, ctx:DNPParser.LibraryNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#localName.
    def visitLocalName(self, ctx:DNPParser.LocalNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#mnemonicName.
    def visitMnemonicName(self, ctx:DNPParser.MnemonicNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#paragraphName.
    def visitParagraphName(self, ctx:DNPParser.ParagraphNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#procedureName.
    def visitProcedureName(self, ctx:DNPParser.ProcedureNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#programName.
    def visitProgramName(self, ctx:DNPParser.ProgramNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#recordName.
    def visitRecordName(self, ctx:DNPParser.RecordNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#reportName.
    def visitReportName(self, ctx:DNPParser.ReportNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#routineName.
    def visitRoutineName(self, ctx:DNPParser.RoutineNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#screenName.
    def visitScreenName(self, ctx:DNPParser.ScreenNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#sectionName.
    def visitSectionName(self, ctx:DNPParser.SectionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#systemName.
    def visitSystemName(self, ctx:DNPParser.SystemNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#symbolicCharacter.
    def visitSymbolicCharacter(self, ctx:DNPParser.SymbolicCharacterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#textName.
    def visitTextName(self, ctx:DNPParser.TextNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#booleanLiteral.
    def visitBooleanLiteral(self, ctx:DNPParser.BooleanLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#numericLiteral.
    def visitNumericLiteral(self, ctx:DNPParser.NumericLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#integerLiteral.
    def visitIntegerLiteral(self, ctx:DNPParser.IntegerLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#cicsDfhRespLiteral.
    def visitCicsDfhRespLiteral(self, ctx:DNPParser.CicsDfhRespLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#cicsDfhValueLiteral.
    def visitCicsDfhValueLiteral(self, ctx:DNPParser.CicsDfhValueLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#figurativeConstant.
    def visitFigurativeConstant(self, ctx:DNPParser.FigurativeConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#specialRegister.
    def visitSpecialRegister(self, ctx:DNPParser.SpecialRegisterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#commentEntry.
    def visitCommentEntry(self, ctx:DNPParser.CommentEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNPParser#charDataKeyword.
    def visitCharDataKeyword(self, ctx:DNPParser.CharDataKeywordContext):
        return self.visitChildren(ctx)



del DNPParser