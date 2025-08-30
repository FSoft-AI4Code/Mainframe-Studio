# Generated from src/parsers/grammar/copybook/CopyBook.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CopyBookParser import CopyBookParser
else:
    from CopyBookParser import CopyBookParser

# This class defines a complete generic visitor for a parse tree produced by CopyBookParser.

class CopyBookVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CopyBookParser#startRule.
    def visitStartRule(self, ctx:CopyBookParser.StartRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#compilationUnit.
    def visitCompilationUnit(self, ctx:CopyBookParser.CompilationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#programUnit.
    def visitProgramUnit(self, ctx:CopyBookParser.ProgramUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#endProgramStatement.
    def visitEndProgramStatement(self, ctx:CopyBookParser.EndProgramStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#identificationDivision.
    def visitIdentificationDivision(self, ctx:CopyBookParser.IdentificationDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#identificationDivisionBody.
    def visitIdentificationDivisionBody(self, ctx:CopyBookParser.IdentificationDivisionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#programIdParagraph.
    def visitProgramIdParagraph(self, ctx:CopyBookParser.ProgramIdParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#author_name.
    def visitAuthor_name(self, ctx:CopyBookParser.Author_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#authorParagraph.
    def visitAuthorParagraph(self, ctx:CopyBookParser.AuthorParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#installationParagraph.
    def visitInstallationParagraph(self, ctx:CopyBookParser.InstallationParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dateWrittenParagraph.
    def visitDateWrittenParagraph(self, ctx:CopyBookParser.DateWrittenParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dateCompiledParagraph.
    def visitDateCompiledParagraph(self, ctx:CopyBookParser.DateCompiledParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#securityParagraph.
    def visitSecurityParagraph(self, ctx:CopyBookParser.SecurityParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#remarksParagraph.
    def visitRemarksParagraph(self, ctx:CopyBookParser.RemarksParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#environmentDivision.
    def visitEnvironmentDivision(self, ctx:CopyBookParser.EnvironmentDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#environmentDivisionBody.
    def visitEnvironmentDivisionBody(self, ctx:CopyBookParser.EnvironmentDivisionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#configurationSection.
    def visitConfigurationSection(self, ctx:CopyBookParser.ConfigurationSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#configurationSectionParagraph.
    def visitConfigurationSectionParagraph(self, ctx:CopyBookParser.ConfigurationSectionParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#sourceComputerParagraph.
    def visitSourceComputerParagraph(self, ctx:CopyBookParser.SourceComputerParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#objectComputerParagraph.
    def visitObjectComputerParagraph(self, ctx:CopyBookParser.ObjectComputerParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#objectComputerClause.
    def visitObjectComputerClause(self, ctx:CopyBookParser.ObjectComputerClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#memorySizeClause.
    def visitMemorySizeClause(self, ctx:CopyBookParser.MemorySizeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#diskSizeClause.
    def visitDiskSizeClause(self, ctx:CopyBookParser.DiskSizeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#collatingSequenceClause.
    def visitCollatingSequenceClause(self, ctx:CopyBookParser.CollatingSequenceClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#collatingSequenceClauseAlphanumeric.
    def visitCollatingSequenceClauseAlphanumeric(self, ctx:CopyBookParser.CollatingSequenceClauseAlphanumericContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#collatingSequenceClauseNational.
    def visitCollatingSequenceClauseNational(self, ctx:CopyBookParser.CollatingSequenceClauseNationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#segmentLimitClause.
    def visitSegmentLimitClause(self, ctx:CopyBookParser.SegmentLimitClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#characterSetClause.
    def visitCharacterSetClause(self, ctx:CopyBookParser.CharacterSetClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#specialNamesParagraph.
    def visitSpecialNamesParagraph(self, ctx:CopyBookParser.SpecialNamesParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#specialNameClause.
    def visitSpecialNameClause(self, ctx:CopyBookParser.SpecialNameClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#alphabetClause.
    def visitAlphabetClause(self, ctx:CopyBookParser.AlphabetClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#alphabetClauseFormat1.
    def visitAlphabetClauseFormat1(self, ctx:CopyBookParser.AlphabetClauseFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#alphabetLiterals.
    def visitAlphabetLiterals(self, ctx:CopyBookParser.AlphabetLiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#alphabetThrough.
    def visitAlphabetThrough(self, ctx:CopyBookParser.AlphabetThroughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#alphabetAlso.
    def visitAlphabetAlso(self, ctx:CopyBookParser.AlphabetAlsoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#alphabetClauseFormat2.
    def visitAlphabetClauseFormat2(self, ctx:CopyBookParser.AlphabetClauseFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#channelClause.
    def visitChannelClause(self, ctx:CopyBookParser.ChannelClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#classClause.
    def visitClassClause(self, ctx:CopyBookParser.ClassClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#classClauseThrough.
    def visitClassClauseThrough(self, ctx:CopyBookParser.ClassClauseThroughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#classClauseFrom.
    def visitClassClauseFrom(self, ctx:CopyBookParser.ClassClauseFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#classClauseTo.
    def visitClassClauseTo(self, ctx:CopyBookParser.ClassClauseToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#currencySignClause.
    def visitCurrencySignClause(self, ctx:CopyBookParser.CurrencySignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#decimalPointClause.
    def visitDecimalPointClause(self, ctx:CopyBookParser.DecimalPointClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#defaultComputationalSignClause.
    def visitDefaultComputationalSignClause(self, ctx:CopyBookParser.DefaultComputationalSignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#defaultDisplaySignClause.
    def visitDefaultDisplaySignClause(self, ctx:CopyBookParser.DefaultDisplaySignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#environmentSwitchNameClause.
    def visitEnvironmentSwitchNameClause(self, ctx:CopyBookParser.EnvironmentSwitchNameClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#environmentSwitchNameSpecialNamesStatusPhrase.
    def visitEnvironmentSwitchNameSpecialNamesStatusPhrase(self, ctx:CopyBookParser.EnvironmentSwitchNameSpecialNamesStatusPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#odtClause.
    def visitOdtClause(self, ctx:CopyBookParser.OdtClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reserveNetworkClause.
    def visitReserveNetworkClause(self, ctx:CopyBookParser.ReserveNetworkClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#symbolicCharactersClause.
    def visitSymbolicCharactersClause(self, ctx:CopyBookParser.SymbolicCharactersClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#symbolicCharacters.
    def visitSymbolicCharacters(self, ctx:CopyBookParser.SymbolicCharactersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#inputOutputSection.
    def visitInputOutputSection(self, ctx:CopyBookParser.InputOutputSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#inputOutputSectionParagraph.
    def visitInputOutputSectionParagraph(self, ctx:CopyBookParser.InputOutputSectionParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#fileControlParagraph.
    def visitFileControlParagraph(self, ctx:CopyBookParser.FileControlParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#fileControlEntry.
    def visitFileControlEntry(self, ctx:CopyBookParser.FileControlEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#selectClause.
    def visitSelectClause(self, ctx:CopyBookParser.SelectClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#fileControlClause.
    def visitFileControlClause(self, ctx:CopyBookParser.FileControlClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#assignClause.
    def visitAssignClause(self, ctx:CopyBookParser.AssignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reserveClause.
    def visitReserveClause(self, ctx:CopyBookParser.ReserveClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#organizationClause.
    def visitOrganizationClause(self, ctx:CopyBookParser.OrganizationClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#paddingCharacterClause.
    def visitPaddingCharacterClause(self, ctx:CopyBookParser.PaddingCharacterClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#recordDelimiterClause.
    def visitRecordDelimiterClause(self, ctx:CopyBookParser.RecordDelimiterClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#accessModeClause.
    def visitAccessModeClause(self, ctx:CopyBookParser.AccessModeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#recordKeyClause.
    def visitRecordKeyClause(self, ctx:CopyBookParser.RecordKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#alternateRecordKeyClause.
    def visitAlternateRecordKeyClause(self, ctx:CopyBookParser.AlternateRecordKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#passwordClause.
    def visitPasswordClause(self, ctx:CopyBookParser.PasswordClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#fileStatusClause.
    def visitFileStatusClause(self, ctx:CopyBookParser.FileStatusClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#relativeKeyClause.
    def visitRelativeKeyClause(self, ctx:CopyBookParser.RelativeKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#ioControlParagraph.
    def visitIoControlParagraph(self, ctx:CopyBookParser.IoControlParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#ioControlClause.
    def visitIoControlClause(self, ctx:CopyBookParser.IoControlClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#rerunClause.
    def visitRerunClause(self, ctx:CopyBookParser.RerunClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#rerunEveryRecords.
    def visitRerunEveryRecords(self, ctx:CopyBookParser.RerunEveryRecordsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#rerunEveryOf.
    def visitRerunEveryOf(self, ctx:CopyBookParser.RerunEveryOfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#rerunEveryClock.
    def visitRerunEveryClock(self, ctx:CopyBookParser.RerunEveryClockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#sameClause.
    def visitSameClause(self, ctx:CopyBookParser.SameClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#multipleFileClause.
    def visitMultipleFileClause(self, ctx:CopyBookParser.MultipleFileClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#multipleFilePosition.
    def visitMultipleFilePosition(self, ctx:CopyBookParser.MultipleFilePositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#commitmentControlClause.
    def visitCommitmentControlClause(self, ctx:CopyBookParser.CommitmentControlClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataDivision.
    def visitDataDivision(self, ctx:CopyBookParser.DataDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataDivisionSection.
    def visitDataDivisionSection(self, ctx:CopyBookParser.DataDivisionSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#fileSection.
    def visitFileSection(self, ctx:CopyBookParser.FileSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#fileDescriptionEntry.
    def visitFileDescriptionEntry(self, ctx:CopyBookParser.FileDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#fileDescriptionEntryClause.
    def visitFileDescriptionEntryClause(self, ctx:CopyBookParser.FileDescriptionEntryClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#externalClause.
    def visitExternalClause(self, ctx:CopyBookParser.ExternalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#globalClause.
    def visitGlobalClause(self, ctx:CopyBookParser.GlobalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#blockContainsClause.
    def visitBlockContainsClause(self, ctx:CopyBookParser.BlockContainsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#blockContainsTo.
    def visitBlockContainsTo(self, ctx:CopyBookParser.BlockContainsToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#recordContainsClause.
    def visitRecordContainsClause(self, ctx:CopyBookParser.RecordContainsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#recordContainsClauseFormat1.
    def visitRecordContainsClauseFormat1(self, ctx:CopyBookParser.RecordContainsClauseFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#recordContainsClauseFormat2.
    def visitRecordContainsClauseFormat2(self, ctx:CopyBookParser.RecordContainsClauseFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#recordContainsClauseFormat3.
    def visitRecordContainsClauseFormat3(self, ctx:CopyBookParser.RecordContainsClauseFormat3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#recordContainsTo.
    def visitRecordContainsTo(self, ctx:CopyBookParser.RecordContainsToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#labelRecordsClause.
    def visitLabelRecordsClause(self, ctx:CopyBookParser.LabelRecordsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#valueOfClause.
    def visitValueOfClause(self, ctx:CopyBookParser.ValueOfClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#valuePair.
    def visitValuePair(self, ctx:CopyBookParser.ValuePairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataRecordsClause.
    def visitDataRecordsClause(self, ctx:CopyBookParser.DataRecordsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#linageClause.
    def visitLinageClause(self, ctx:CopyBookParser.LinageClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#linageAt.
    def visitLinageAt(self, ctx:CopyBookParser.LinageAtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#linageFootingAt.
    def visitLinageFootingAt(self, ctx:CopyBookParser.LinageFootingAtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#linageLinesAtTop.
    def visitLinageLinesAtTop(self, ctx:CopyBookParser.LinageLinesAtTopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#linageLinesAtBottom.
    def visitLinageLinesAtBottom(self, ctx:CopyBookParser.LinageLinesAtBottomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#recordingModeClause.
    def visitRecordingModeClause(self, ctx:CopyBookParser.RecordingModeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#modeStatement.
    def visitModeStatement(self, ctx:CopyBookParser.ModeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#codeSetClause.
    def visitCodeSetClause(self, ctx:CopyBookParser.CodeSetClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportClause.
    def visitReportClause(self, ctx:CopyBookParser.ReportClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataBaseSection.
    def visitDataBaseSection(self, ctx:CopyBookParser.DataBaseSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataBaseSectionEntry.
    def visitDataBaseSectionEntry(self, ctx:CopyBookParser.DataBaseSectionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#workingStorageSection.
    def visitWorkingStorageSection(self, ctx:CopyBookParser.WorkingStorageSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#linkageSection.
    def visitLinkageSection(self, ctx:CopyBookParser.LinkageSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#communicationSection.
    def visitCommunicationSection(self, ctx:CopyBookParser.CommunicationSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#communicationDescriptionEntry.
    def visitCommunicationDescriptionEntry(self, ctx:CopyBookParser.CommunicationDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#communicationDescriptionEntryFormat1.
    def visitCommunicationDescriptionEntryFormat1(self, ctx:CopyBookParser.CommunicationDescriptionEntryFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#communicationDescriptionEntryFormat2.
    def visitCommunicationDescriptionEntryFormat2(self, ctx:CopyBookParser.CommunicationDescriptionEntryFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#communicationDescriptionEntryFormat3.
    def visitCommunicationDescriptionEntryFormat3(self, ctx:CopyBookParser.CommunicationDescriptionEntryFormat3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#destinationCountClause.
    def visitDestinationCountClause(self, ctx:CopyBookParser.DestinationCountClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#destinationTableClause.
    def visitDestinationTableClause(self, ctx:CopyBookParser.DestinationTableClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#endKeyClause.
    def visitEndKeyClause(self, ctx:CopyBookParser.EndKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#errorKeyClause.
    def visitErrorKeyClause(self, ctx:CopyBookParser.ErrorKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#messageCountClause.
    def visitMessageCountClause(self, ctx:CopyBookParser.MessageCountClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#messageDateClause.
    def visitMessageDateClause(self, ctx:CopyBookParser.MessageDateClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#messageTimeClause.
    def visitMessageTimeClause(self, ctx:CopyBookParser.MessageTimeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#statusKeyClause.
    def visitStatusKeyClause(self, ctx:CopyBookParser.StatusKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#symbolicDestinationClause.
    def visitSymbolicDestinationClause(self, ctx:CopyBookParser.SymbolicDestinationClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#symbolicQueueClause.
    def visitSymbolicQueueClause(self, ctx:CopyBookParser.SymbolicQueueClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#symbolicSourceClause.
    def visitSymbolicSourceClause(self, ctx:CopyBookParser.SymbolicSourceClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#symbolicTerminalClause.
    def visitSymbolicTerminalClause(self, ctx:CopyBookParser.SymbolicTerminalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#symbolicSubQueueClause.
    def visitSymbolicSubQueueClause(self, ctx:CopyBookParser.SymbolicSubQueueClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#textLengthClause.
    def visitTextLengthClause(self, ctx:CopyBookParser.TextLengthClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#localStorageSection.
    def visitLocalStorageSection(self, ctx:CopyBookParser.LocalStorageSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenSection.
    def visitScreenSection(self, ctx:CopyBookParser.ScreenSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenDescriptionEntry.
    def visitScreenDescriptionEntry(self, ctx:CopyBookParser.ScreenDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenDescriptionBlankClause.
    def visitScreenDescriptionBlankClause(self, ctx:CopyBookParser.ScreenDescriptionBlankClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenDescriptionBellClause.
    def visitScreenDescriptionBellClause(self, ctx:CopyBookParser.ScreenDescriptionBellClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenDescriptionBlinkClause.
    def visitScreenDescriptionBlinkClause(self, ctx:CopyBookParser.ScreenDescriptionBlinkClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenDescriptionEraseClause.
    def visitScreenDescriptionEraseClause(self, ctx:CopyBookParser.ScreenDescriptionEraseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenDescriptionLightClause.
    def visitScreenDescriptionLightClause(self, ctx:CopyBookParser.ScreenDescriptionLightClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenDescriptionGridClause.
    def visitScreenDescriptionGridClause(self, ctx:CopyBookParser.ScreenDescriptionGridClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenDescriptionReverseVideoClause.
    def visitScreenDescriptionReverseVideoClause(self, ctx:CopyBookParser.ScreenDescriptionReverseVideoClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenDescriptionUnderlineClause.
    def visitScreenDescriptionUnderlineClause(self, ctx:CopyBookParser.ScreenDescriptionUnderlineClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenDescriptionSizeClause.
    def visitScreenDescriptionSizeClause(self, ctx:CopyBookParser.ScreenDescriptionSizeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenDescriptionLineClause.
    def visitScreenDescriptionLineClause(self, ctx:CopyBookParser.ScreenDescriptionLineClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenDescriptionColumnClause.
    def visitScreenDescriptionColumnClause(self, ctx:CopyBookParser.ScreenDescriptionColumnClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenDescriptionForegroundColorClause.
    def visitScreenDescriptionForegroundColorClause(self, ctx:CopyBookParser.ScreenDescriptionForegroundColorClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenDescriptionBackgroundColorClause.
    def visitScreenDescriptionBackgroundColorClause(self, ctx:CopyBookParser.ScreenDescriptionBackgroundColorClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenDescriptionControlClause.
    def visitScreenDescriptionControlClause(self, ctx:CopyBookParser.ScreenDescriptionControlClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenDescriptionValueClause.
    def visitScreenDescriptionValueClause(self, ctx:CopyBookParser.ScreenDescriptionValueClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenDescriptionPictureClause.
    def visitScreenDescriptionPictureClause(self, ctx:CopyBookParser.ScreenDescriptionPictureClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenDescriptionFromClause.
    def visitScreenDescriptionFromClause(self, ctx:CopyBookParser.ScreenDescriptionFromClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenDescriptionToClause.
    def visitScreenDescriptionToClause(self, ctx:CopyBookParser.ScreenDescriptionToClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenDescriptionUsingClause.
    def visitScreenDescriptionUsingClause(self, ctx:CopyBookParser.ScreenDescriptionUsingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenDescriptionUsageClause.
    def visitScreenDescriptionUsageClause(self, ctx:CopyBookParser.ScreenDescriptionUsageClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenDescriptionBlankWhenZeroClause.
    def visitScreenDescriptionBlankWhenZeroClause(self, ctx:CopyBookParser.ScreenDescriptionBlankWhenZeroClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenDescriptionJustifiedClause.
    def visitScreenDescriptionJustifiedClause(self, ctx:CopyBookParser.ScreenDescriptionJustifiedClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenDescriptionSignClause.
    def visitScreenDescriptionSignClause(self, ctx:CopyBookParser.ScreenDescriptionSignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenDescriptionAutoClause.
    def visitScreenDescriptionAutoClause(self, ctx:CopyBookParser.ScreenDescriptionAutoClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenDescriptionSecureClause.
    def visitScreenDescriptionSecureClause(self, ctx:CopyBookParser.ScreenDescriptionSecureClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenDescriptionRequiredClause.
    def visitScreenDescriptionRequiredClause(self, ctx:CopyBookParser.ScreenDescriptionRequiredClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenDescriptionPromptClause.
    def visitScreenDescriptionPromptClause(self, ctx:CopyBookParser.ScreenDescriptionPromptClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenDescriptionPromptOccursClause.
    def visitScreenDescriptionPromptOccursClause(self, ctx:CopyBookParser.ScreenDescriptionPromptOccursClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenDescriptionFullClause.
    def visitScreenDescriptionFullClause(self, ctx:CopyBookParser.ScreenDescriptionFullClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenDescriptionZeroFillClause.
    def visitScreenDescriptionZeroFillClause(self, ctx:CopyBookParser.ScreenDescriptionZeroFillClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportSection.
    def visitReportSection(self, ctx:CopyBookParser.ReportSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportDescription.
    def visitReportDescription(self, ctx:CopyBookParser.ReportDescriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportDescriptionEntry.
    def visitReportDescriptionEntry(self, ctx:CopyBookParser.ReportDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportDescriptionGlobalClause.
    def visitReportDescriptionGlobalClause(self, ctx:CopyBookParser.ReportDescriptionGlobalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportDescriptionPageLimitClause.
    def visitReportDescriptionPageLimitClause(self, ctx:CopyBookParser.ReportDescriptionPageLimitClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportDescriptionHeadingClause.
    def visitReportDescriptionHeadingClause(self, ctx:CopyBookParser.ReportDescriptionHeadingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportDescriptionFirstDetailClause.
    def visitReportDescriptionFirstDetailClause(self, ctx:CopyBookParser.ReportDescriptionFirstDetailClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportDescriptionLastDetailClause.
    def visitReportDescriptionLastDetailClause(self, ctx:CopyBookParser.ReportDescriptionLastDetailClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportDescriptionFootingClause.
    def visitReportDescriptionFootingClause(self, ctx:CopyBookParser.ReportDescriptionFootingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportGroupDescriptionEntry.
    def visitReportGroupDescriptionEntry(self, ctx:CopyBookParser.ReportGroupDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportGroupDescriptionEntryFormat1.
    def visitReportGroupDescriptionEntryFormat1(self, ctx:CopyBookParser.ReportGroupDescriptionEntryFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportGroupDescriptionEntryFormat2.
    def visitReportGroupDescriptionEntryFormat2(self, ctx:CopyBookParser.ReportGroupDescriptionEntryFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportGroupDescriptionEntryFormat3.
    def visitReportGroupDescriptionEntryFormat3(self, ctx:CopyBookParser.ReportGroupDescriptionEntryFormat3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportGroupBlankWhenZeroClause.
    def visitReportGroupBlankWhenZeroClause(self, ctx:CopyBookParser.ReportGroupBlankWhenZeroClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportGroupColumnNumberClause.
    def visitReportGroupColumnNumberClause(self, ctx:CopyBookParser.ReportGroupColumnNumberClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportGroupIndicateClause.
    def visitReportGroupIndicateClause(self, ctx:CopyBookParser.ReportGroupIndicateClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportGroupJustifiedClause.
    def visitReportGroupJustifiedClause(self, ctx:CopyBookParser.ReportGroupJustifiedClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportGroupLineNumberClause.
    def visitReportGroupLineNumberClause(self, ctx:CopyBookParser.ReportGroupLineNumberClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportGroupLineNumberNextPage.
    def visitReportGroupLineNumberNextPage(self, ctx:CopyBookParser.ReportGroupLineNumberNextPageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportGroupLineNumberPlus.
    def visitReportGroupLineNumberPlus(self, ctx:CopyBookParser.ReportGroupLineNumberPlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportGroupNextGroupClause.
    def visitReportGroupNextGroupClause(self, ctx:CopyBookParser.ReportGroupNextGroupClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportGroupNextGroupPlus.
    def visitReportGroupNextGroupPlus(self, ctx:CopyBookParser.ReportGroupNextGroupPlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportGroupNextGroupNextPage.
    def visitReportGroupNextGroupNextPage(self, ctx:CopyBookParser.ReportGroupNextGroupNextPageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportGroupPictureClause.
    def visitReportGroupPictureClause(self, ctx:CopyBookParser.ReportGroupPictureClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportGroupResetClause.
    def visitReportGroupResetClause(self, ctx:CopyBookParser.ReportGroupResetClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportGroupSignClause.
    def visitReportGroupSignClause(self, ctx:CopyBookParser.ReportGroupSignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportGroupSourceClause.
    def visitReportGroupSourceClause(self, ctx:CopyBookParser.ReportGroupSourceClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportGroupSumClause.
    def visitReportGroupSumClause(self, ctx:CopyBookParser.ReportGroupSumClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportGroupTypeClause.
    def visitReportGroupTypeClause(self, ctx:CopyBookParser.ReportGroupTypeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportGroupTypeReportHeading.
    def visitReportGroupTypeReportHeading(self, ctx:CopyBookParser.ReportGroupTypeReportHeadingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportGroupTypePageHeading.
    def visitReportGroupTypePageHeading(self, ctx:CopyBookParser.ReportGroupTypePageHeadingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportGroupTypeControlHeading.
    def visitReportGroupTypeControlHeading(self, ctx:CopyBookParser.ReportGroupTypeControlHeadingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportGroupTypeDetail.
    def visitReportGroupTypeDetail(self, ctx:CopyBookParser.ReportGroupTypeDetailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportGroupTypeControlFooting.
    def visitReportGroupTypeControlFooting(self, ctx:CopyBookParser.ReportGroupTypeControlFootingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportGroupUsageClause.
    def visitReportGroupUsageClause(self, ctx:CopyBookParser.ReportGroupUsageClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportGroupTypePageFooting.
    def visitReportGroupTypePageFooting(self, ctx:CopyBookParser.ReportGroupTypePageFootingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportGroupTypeReportFooting.
    def visitReportGroupTypeReportFooting(self, ctx:CopyBookParser.ReportGroupTypeReportFootingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportGroupValueClause.
    def visitReportGroupValueClause(self, ctx:CopyBookParser.ReportGroupValueClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#programLibrarySection.
    def visitProgramLibrarySection(self, ctx:CopyBookParser.ProgramLibrarySectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#libraryDescriptionEntry.
    def visitLibraryDescriptionEntry(self, ctx:CopyBookParser.LibraryDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#libraryDescriptionEntryFormat1.
    def visitLibraryDescriptionEntryFormat1(self, ctx:CopyBookParser.LibraryDescriptionEntryFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#libraryDescriptionEntryFormat2.
    def visitLibraryDescriptionEntryFormat2(self, ctx:CopyBookParser.LibraryDescriptionEntryFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#libraryAttributeClauseFormat1.
    def visitLibraryAttributeClauseFormat1(self, ctx:CopyBookParser.LibraryAttributeClauseFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#libraryAttributeClauseFormat2.
    def visitLibraryAttributeClauseFormat2(self, ctx:CopyBookParser.LibraryAttributeClauseFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#libraryAttributeFunction.
    def visitLibraryAttributeFunction(self, ctx:CopyBookParser.LibraryAttributeFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#libraryAttributeParameter.
    def visitLibraryAttributeParameter(self, ctx:CopyBookParser.LibraryAttributeParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#libraryAttributeTitle.
    def visitLibraryAttributeTitle(self, ctx:CopyBookParser.LibraryAttributeTitleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#libraryEntryProcedureClauseFormat1.
    def visitLibraryEntryProcedureClauseFormat1(self, ctx:CopyBookParser.LibraryEntryProcedureClauseFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#libraryEntryProcedureClauseFormat2.
    def visitLibraryEntryProcedureClauseFormat2(self, ctx:CopyBookParser.LibraryEntryProcedureClauseFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#libraryEntryProcedureForClause.
    def visitLibraryEntryProcedureForClause(self, ctx:CopyBookParser.LibraryEntryProcedureForClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#libraryEntryProcedureGivingClause.
    def visitLibraryEntryProcedureGivingClause(self, ctx:CopyBookParser.LibraryEntryProcedureGivingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#libraryEntryProcedureUsingClause.
    def visitLibraryEntryProcedureUsingClause(self, ctx:CopyBookParser.LibraryEntryProcedureUsingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#libraryEntryProcedureUsingName.
    def visitLibraryEntryProcedureUsingName(self, ctx:CopyBookParser.LibraryEntryProcedureUsingNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#libraryEntryProcedureWithClause.
    def visitLibraryEntryProcedureWithClause(self, ctx:CopyBookParser.LibraryEntryProcedureWithClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#libraryEntryProcedureWithName.
    def visitLibraryEntryProcedureWithName(self, ctx:CopyBookParser.LibraryEntryProcedureWithNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#libraryIsCommonClause.
    def visitLibraryIsCommonClause(self, ctx:CopyBookParser.LibraryIsCommonClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#libraryIsGlobalClause.
    def visitLibraryIsGlobalClause(self, ctx:CopyBookParser.LibraryIsGlobalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataDescriptionEntry.
    def visitDataDescriptionEntry(self, ctx:CopyBookParser.DataDescriptionEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#copyStatement.
    def visitCopyStatement(self, ctx:CopyBookParser.CopyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#disjoinPhrase.
    def visitDisjoinPhrase(self, ctx:CopyBookParser.DisjoinPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#joinPhrase.
    def visitJoinPhrase(self, ctx:CopyBookParser.JoinPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#copySource.
    def visitCopySource(self, ctx:CopyBookParser.CopySourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#copyLibrary.
    def visitCopyLibrary(self, ctx:CopyBookParser.CopyLibraryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#replacingPhrase.
    def visitReplacingPhrase(self, ctx:CopyBookParser.ReplacingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#replaceArea.
    def visitReplaceArea(self, ctx:CopyBookParser.ReplaceAreaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#replaceByStatement.
    def visitReplaceByStatement(self, ctx:CopyBookParser.ReplaceByStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#replaceOffStatement.
    def visitReplaceOffStatement(self, ctx:CopyBookParser.ReplaceOffStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#replaceClause.
    def visitReplaceClause(self, ctx:CopyBookParser.ReplaceClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#directoryPhrase.
    def visitDirectoryPhrase(self, ctx:CopyBookParser.DirectoryPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#familyPhrase.
    def visitFamilyPhrase(self, ctx:CopyBookParser.FamilyPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#replaceable.
    def visitReplaceable(self, ctx:CopyBookParser.ReplaceableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#replacement.
    def visitReplacement(self, ctx:CopyBookParser.ReplacementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#ejectStatement.
    def visitEjectStatement(self, ctx:CopyBookParser.EjectStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#skipStatement.
    def visitSkipStatement(self, ctx:CopyBookParser.SkipStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#titleStatement.
    def visitTitleStatement(self, ctx:CopyBookParser.TitleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#pseudoText.
    def visitPseudoText(self, ctx:CopyBookParser.PseudoTextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#charData.
    def visitCharData(self, ctx:CopyBookParser.CharDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#charDataSql.
    def visitCharDataSql(self, ctx:CopyBookParser.CharDataSqlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#charDataLine.
    def visitCharDataLine(self, ctx:CopyBookParser.CharDataLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#cobolWord.
    def visitCobolWord(self, ctx:CopyBookParser.CobolWordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#literal.
    def visitLiteral(self, ctx:CopyBookParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#jpEncodingText.
    def visitJpEncodingText(self, ctx:CopyBookParser.JpEncodingTextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#filename.
    def visitFilename(self, ctx:CopyBookParser.FilenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataDescriptionEntryFormat1.
    def visitDataDescriptionEntryFormat1(self, ctx:CopyBookParser.DataDescriptionEntryFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataSqlTypeClause.
    def visitDataSqlTypeClause(self, ctx:CopyBookParser.DataSqlTypeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#sqlDataType.
    def visitSqlDataType(self, ctx:CopyBookParser.SqlDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#sqlDataLenght.
    def visitSqlDataLenght(self, ctx:CopyBookParser.SqlDataLenghtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataCharacterClause.
    def visitDataCharacterClause(self, ctx:CopyBookParser.DataCharacterClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataDescriptionEntryFormat2.
    def visitDataDescriptionEntryFormat2(self, ctx:CopyBookParser.DataDescriptionEntryFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataDescriptionEntryFormat3.
    def visitDataDescriptionEntryFormat3(self, ctx:CopyBookParser.DataDescriptionEntryFormat3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataDescriptionEntryExecSql.
    def visitDataDescriptionEntryExecSql(self, ctx:CopyBookParser.DataDescriptionEntryExecSqlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataAlignedClause.
    def visitDataAlignedClause(self, ctx:CopyBookParser.DataAlignedClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataBlankWhenZeroClause.
    def visitDataBlankWhenZeroClause(self, ctx:CopyBookParser.DataBlankWhenZeroClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataCommonOwnLocalClause.
    def visitDataCommonOwnLocalClause(self, ctx:CopyBookParser.DataCommonOwnLocalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataExternalClause.
    def visitDataExternalClause(self, ctx:CopyBookParser.DataExternalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataGlobalClause.
    def visitDataGlobalClause(self, ctx:CopyBookParser.DataGlobalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataIntegerStringClause.
    def visitDataIntegerStringClause(self, ctx:CopyBookParser.DataIntegerStringClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataJustifiedClause.
    def visitDataJustifiedClause(self, ctx:CopyBookParser.DataJustifiedClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataOccursClause.
    def visitDataOccursClause(self, ctx:CopyBookParser.DataOccursClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataOccursTo.
    def visitDataOccursTo(self, ctx:CopyBookParser.DataOccursToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataOccursSort.
    def visitDataOccursSort(self, ctx:CopyBookParser.DataOccursSortContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataPictureClause.
    def visitDataPictureClause(self, ctx:CopyBookParser.DataPictureClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#pictureString.
    def visitPictureString(self, ctx:CopyBookParser.PictureStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#pictureChars.
    def visitPictureChars(self, ctx:CopyBookParser.PictureCharsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#pictureCardinality.
    def visitPictureCardinality(self, ctx:CopyBookParser.PictureCardinalityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataReceivedByClause.
    def visitDataReceivedByClause(self, ctx:CopyBookParser.DataReceivedByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataRecordAreaClause.
    def visitDataRecordAreaClause(self, ctx:CopyBookParser.DataRecordAreaClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataRedefinesClause.
    def visitDataRedefinesClause(self, ctx:CopyBookParser.DataRedefinesClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataRenamesClause.
    def visitDataRenamesClause(self, ctx:CopyBookParser.DataRenamesClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataSignClause.
    def visitDataSignClause(self, ctx:CopyBookParser.DataSignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataSynchronizedClause.
    def visitDataSynchronizedClause(self, ctx:CopyBookParser.DataSynchronizedClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataThreadLocalClause.
    def visitDataThreadLocalClause(self, ctx:CopyBookParser.DataThreadLocalClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataTypeClause.
    def visitDataTypeClause(self, ctx:CopyBookParser.DataTypeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataTypeDefClause.
    def visitDataTypeDefClause(self, ctx:CopyBookParser.DataTypeDefClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataUsageClause.
    def visitDataUsageClause(self, ctx:CopyBookParser.DataUsageClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataUsingClause.
    def visitDataUsingClause(self, ctx:CopyBookParser.DataUsingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataValueClause.
    def visitDataValueClause(self, ctx:CopyBookParser.DataValueClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataValueInterval.
    def visitDataValueInterval(self, ctx:CopyBookParser.DataValueIntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataValueIntervalFrom.
    def visitDataValueIntervalFrom(self, ctx:CopyBookParser.DataValueIntervalFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataValueIntervalTo.
    def visitDataValueIntervalTo(self, ctx:CopyBookParser.DataValueIntervalToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataWithLowerBoundsClause.
    def visitDataWithLowerBoundsClause(self, ctx:CopyBookParser.DataWithLowerBoundsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#procedureDivision.
    def visitProcedureDivision(self, ctx:CopyBookParser.ProcedureDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#procedureDivisionUsingClause.
    def visitProcedureDivisionUsingClause(self, ctx:CopyBookParser.ProcedureDivisionUsingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#procedureDivisionGivingClause.
    def visitProcedureDivisionGivingClause(self, ctx:CopyBookParser.ProcedureDivisionGivingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#procedureDivisionUsingParameter.
    def visitProcedureDivisionUsingParameter(self, ctx:CopyBookParser.ProcedureDivisionUsingParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#procedureDivisionByReferencePhrase.
    def visitProcedureDivisionByReferencePhrase(self, ctx:CopyBookParser.ProcedureDivisionByReferencePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#procedureDivisionByReference.
    def visitProcedureDivisionByReference(self, ctx:CopyBookParser.ProcedureDivisionByReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#procedureDivisionByValuePhrase.
    def visitProcedureDivisionByValuePhrase(self, ctx:CopyBookParser.ProcedureDivisionByValuePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#procedureDivisionByValue.
    def visitProcedureDivisionByValue(self, ctx:CopyBookParser.ProcedureDivisionByValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#procedureDeclaratives.
    def visitProcedureDeclaratives(self, ctx:CopyBookParser.ProcedureDeclarativesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#procedureDeclarative.
    def visitProcedureDeclarative(self, ctx:CopyBookParser.ProcedureDeclarativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#procedureSectionHeader.
    def visitProcedureSectionHeader(self, ctx:CopyBookParser.ProcedureSectionHeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#procedureDivisionBody.
    def visitProcedureDivisionBody(self, ctx:CopyBookParser.ProcedureDivisionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#procedureSection.
    def visitProcedureSection(self, ctx:CopyBookParser.ProcedureSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#paragraphs.
    def visitParagraphs(self, ctx:CopyBookParser.ParagraphsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#paragraph.
    def visitParagraph(self, ctx:CopyBookParser.ParagraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#sentence.
    def visitSentence(self, ctx:CopyBookParser.SentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#statement.
    def visitStatement(self, ctx:CopyBookParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#xmlParseStatement.
    def visitXmlParseStatement(self, ctx:CopyBookParser.XmlParseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#xmlDataname.
    def visitXmlDataname(self, ctx:CopyBookParser.XmlDatanameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#xmlProcessingProcedure.
    def visitXmlProcessingProcedure(self, ctx:CopyBookParser.XmlProcessingProcedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#endXml.
    def visitEndXml(self, ctx:CopyBookParser.EndXmlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#execSqlStatement2.
    def visitExecSqlStatement2(self, ctx:CopyBookParser.ExecSqlStatement2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#sqlCode.
    def visitSqlCode(self, ctx:CopyBookParser.SqlCodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#execCicsStatement2.
    def visitExecCicsStatement2(self, ctx:CopyBookParser.ExecCicsStatement2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#commandName.
    def visitCommandName(self, ctx:CopyBookParser.CommandNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#commandBody.
    def visitCommandBody(self, ctx:CopyBookParser.CommandBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#commandParameter.
    def visitCommandParameter(self, ctx:CopyBookParser.CommandParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#parameterName.
    def visitParameterName(self, ctx:CopyBookParser.ParameterNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#parameterNameWithIndex.
    def visitParameterNameWithIndex(self, ctx:CopyBookParser.ParameterNameWithIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#parameterValueWithIndex.
    def visitParameterValueWithIndex(self, ctx:CopyBookParser.ParameterValueWithIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#parameterValue.
    def visitParameterValue(self, ctx:CopyBookParser.ParameterValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#acceptStatement.
    def visitAcceptStatement(self, ctx:CopyBookParser.AcceptStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#acceptFromDateStatement.
    def visitAcceptFromDateStatement(self, ctx:CopyBookParser.AcceptFromDateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#acceptFromMnemonicStatement.
    def visitAcceptFromMnemonicStatement(self, ctx:CopyBookParser.AcceptFromMnemonicStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#acceptFromEscapeKeyStatement.
    def visitAcceptFromEscapeKeyStatement(self, ctx:CopyBookParser.AcceptFromEscapeKeyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#acceptMessageCountStatement.
    def visitAcceptMessageCountStatement(self, ctx:CopyBookParser.AcceptMessageCountStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#addStatement.
    def visitAddStatement(self, ctx:CopyBookParser.AddStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#addToStatement.
    def visitAddToStatement(self, ctx:CopyBookParser.AddToStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#addToGivingStatement.
    def visitAddToGivingStatement(self, ctx:CopyBookParser.AddToGivingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#addCorrespondingStatement.
    def visitAddCorrespondingStatement(self, ctx:CopyBookParser.AddCorrespondingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#addFrom.
    def visitAddFrom(self, ctx:CopyBookParser.AddFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#addTo.
    def visitAddTo(self, ctx:CopyBookParser.AddToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#addToGiving.
    def visitAddToGiving(self, ctx:CopyBookParser.AddToGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#addGiving.
    def visitAddGiving(self, ctx:CopyBookParser.AddGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#alteredGoTo.
    def visitAlteredGoTo(self, ctx:CopyBookParser.AlteredGoToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#alterStatement.
    def visitAlterStatement(self, ctx:CopyBookParser.AlterStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#alterProceedTo.
    def visitAlterProceedTo(self, ctx:CopyBookParser.AlterProceedToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#callStatement.
    def visitCallStatement(self, ctx:CopyBookParser.CallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#callUsingPhrase.
    def visitCallUsingPhrase(self, ctx:CopyBookParser.CallUsingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#callUsingParameter.
    def visitCallUsingParameter(self, ctx:CopyBookParser.CallUsingParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#callByReferencePhrase.
    def visitCallByReferencePhrase(self, ctx:CopyBookParser.CallByReferencePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#callByReference.
    def visitCallByReference(self, ctx:CopyBookParser.CallByReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#callByValuePhrase.
    def visitCallByValuePhrase(self, ctx:CopyBookParser.CallByValuePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#callByValue.
    def visitCallByValue(self, ctx:CopyBookParser.CallByValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#callByContentPhrase.
    def visitCallByContentPhrase(self, ctx:CopyBookParser.CallByContentPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#callByContent.
    def visitCallByContent(self, ctx:CopyBookParser.CallByContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#callGivingPhrase.
    def visitCallGivingPhrase(self, ctx:CopyBookParser.CallGivingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#cancelStatement.
    def visitCancelStatement(self, ctx:CopyBookParser.CancelStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#cancelCall.
    def visitCancelCall(self, ctx:CopyBookParser.CancelCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#closeStatement.
    def visitCloseStatement(self, ctx:CopyBookParser.CloseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#closeFile.
    def visitCloseFile(self, ctx:CopyBookParser.CloseFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#closeReelUnitStatement.
    def visitCloseReelUnitStatement(self, ctx:CopyBookParser.CloseReelUnitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#closeRelativeStatement.
    def visitCloseRelativeStatement(self, ctx:CopyBookParser.CloseRelativeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#closePortFileIOStatement.
    def visitClosePortFileIOStatement(self, ctx:CopyBookParser.ClosePortFileIOStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#closePortFileIOUsing.
    def visitClosePortFileIOUsing(self, ctx:CopyBookParser.ClosePortFileIOUsingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#closePortFileIOUsingCloseDisposition.
    def visitClosePortFileIOUsingCloseDisposition(self, ctx:CopyBookParser.ClosePortFileIOUsingCloseDispositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#closePortFileIOUsingAssociatedData.
    def visitClosePortFileIOUsingAssociatedData(self, ctx:CopyBookParser.ClosePortFileIOUsingAssociatedDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#closePortFileIOUsingAssociatedDataLength.
    def visitClosePortFileIOUsingAssociatedDataLength(self, ctx:CopyBookParser.ClosePortFileIOUsingAssociatedDataLengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#computeStatement.
    def visitComputeStatement(self, ctx:CopyBookParser.ComputeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#computeStore.
    def visitComputeStore(self, ctx:CopyBookParser.ComputeStoreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#continueStatement.
    def visitContinueStatement(self, ctx:CopyBookParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#deleteStatement.
    def visitDeleteStatement(self, ctx:CopyBookParser.DeleteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#disableStatement.
    def visitDisableStatement(self, ctx:CopyBookParser.DisableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#displayStatement.
    def visitDisplayStatement(self, ctx:CopyBookParser.DisplayStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#displayOperand.
    def visitDisplayOperand(self, ctx:CopyBookParser.DisplayOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#displayAt.
    def visitDisplayAt(self, ctx:CopyBookParser.DisplayAtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#displayUpon.
    def visitDisplayUpon(self, ctx:CopyBookParser.DisplayUponContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#displayWith.
    def visitDisplayWith(self, ctx:CopyBookParser.DisplayWithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#divideStatement.
    def visitDivideStatement(self, ctx:CopyBookParser.DivideStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#divideIntoStatement.
    def visitDivideIntoStatement(self, ctx:CopyBookParser.DivideIntoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#divideIntoGivingStatement.
    def visitDivideIntoGivingStatement(self, ctx:CopyBookParser.DivideIntoGivingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#divideByGivingStatement.
    def visitDivideByGivingStatement(self, ctx:CopyBookParser.DivideByGivingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#divideGivingPhrase.
    def visitDivideGivingPhrase(self, ctx:CopyBookParser.DivideGivingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#divideInto.
    def visitDivideInto(self, ctx:CopyBookParser.DivideIntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#divideGiving.
    def visitDivideGiving(self, ctx:CopyBookParser.DivideGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#divideRemainder.
    def visitDivideRemainder(self, ctx:CopyBookParser.DivideRemainderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#enableStatement.
    def visitEnableStatement(self, ctx:CopyBookParser.EnableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#entryStatement.
    def visitEntryStatement(self, ctx:CopyBookParser.EntryStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#evaluateStatement.
    def visitEvaluateStatement(self, ctx:CopyBookParser.EvaluateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#evaluateSelect.
    def visitEvaluateSelect(self, ctx:CopyBookParser.EvaluateSelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#evaluateAlsoSelect.
    def visitEvaluateAlsoSelect(self, ctx:CopyBookParser.EvaluateAlsoSelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#evaluateWhenPhrase.
    def visitEvaluateWhenPhrase(self, ctx:CopyBookParser.EvaluateWhenPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#evaluateWhen.
    def visitEvaluateWhen(self, ctx:CopyBookParser.EvaluateWhenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#evaluateCondition.
    def visitEvaluateCondition(self, ctx:CopyBookParser.EvaluateConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#evaluateThrough.
    def visitEvaluateThrough(self, ctx:CopyBookParser.EvaluateThroughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#evaluateAlsoCondition.
    def visitEvaluateAlsoCondition(self, ctx:CopyBookParser.EvaluateAlsoConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#evaluateWhenOther.
    def visitEvaluateWhenOther(self, ctx:CopyBookParser.EvaluateWhenOtherContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#evaluateValue.
    def visitEvaluateValue(self, ctx:CopyBookParser.EvaluateValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#execCicsStatement.
    def visitExecCicsStatement(self, ctx:CopyBookParser.ExecCicsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#execSqlStatement.
    def visitExecSqlStatement(self, ctx:CopyBookParser.ExecSqlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#execSqlImsStatement.
    def visitExecSqlImsStatement(self, ctx:CopyBookParser.ExecSqlImsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#exhibitStatement.
    def visitExhibitStatement(self, ctx:CopyBookParser.ExhibitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#exhibitOperand.
    def visitExhibitOperand(self, ctx:CopyBookParser.ExhibitOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#exitStatement.
    def visitExitStatement(self, ctx:CopyBookParser.ExitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#generateStatement.
    def visitGenerateStatement(self, ctx:CopyBookParser.GenerateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#gobackStatement.
    def visitGobackStatement(self, ctx:CopyBookParser.GobackStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#goToStatement.
    def visitGoToStatement(self, ctx:CopyBookParser.GoToStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#goToStatementSimple.
    def visitGoToStatementSimple(self, ctx:CopyBookParser.GoToStatementSimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#goToDependingOnStatement.
    def visitGoToDependingOnStatement(self, ctx:CopyBookParser.GoToDependingOnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#ifStatement.
    def visitIfStatement(self, ctx:CopyBookParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#ifThen.
    def visitIfThen(self, ctx:CopyBookParser.IfThenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#ifElse.
    def visitIfElse(self, ctx:CopyBookParser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#initializeStatement.
    def visitInitializeStatement(self, ctx:CopyBookParser.InitializeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#initializeReplacingPhrase.
    def visitInitializeReplacingPhrase(self, ctx:CopyBookParser.InitializeReplacingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#initializeReplacingBy.
    def visitInitializeReplacingBy(self, ctx:CopyBookParser.InitializeReplacingByContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#initiateStatement.
    def visitInitiateStatement(self, ctx:CopyBookParser.InitiateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#inspectStatement.
    def visitInspectStatement(self, ctx:CopyBookParser.InspectStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#inspectTallyingPhrase.
    def visitInspectTallyingPhrase(self, ctx:CopyBookParser.InspectTallyingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#inspectReplacingPhrase.
    def visitInspectReplacingPhrase(self, ctx:CopyBookParser.InspectReplacingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#inspectTallyingReplacingPhrase.
    def visitInspectTallyingReplacingPhrase(self, ctx:CopyBookParser.InspectTallyingReplacingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#inspectConvertingPhrase.
    def visitInspectConvertingPhrase(self, ctx:CopyBookParser.InspectConvertingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#inspectFor.
    def visitInspectFor(self, ctx:CopyBookParser.InspectForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#inspectCharacters.
    def visitInspectCharacters(self, ctx:CopyBookParser.InspectCharactersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#inspectReplacingCharacters.
    def visitInspectReplacingCharacters(self, ctx:CopyBookParser.InspectReplacingCharactersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#inspectAllLeadings.
    def visitInspectAllLeadings(self, ctx:CopyBookParser.InspectAllLeadingsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#inspectReplacingAllLeadings.
    def visitInspectReplacingAllLeadings(self, ctx:CopyBookParser.InspectReplacingAllLeadingsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#inspectAllLeading.
    def visitInspectAllLeading(self, ctx:CopyBookParser.InspectAllLeadingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#inspectReplacingAllLeading.
    def visitInspectReplacingAllLeading(self, ctx:CopyBookParser.InspectReplacingAllLeadingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#inspectBy.
    def visitInspectBy(self, ctx:CopyBookParser.InspectByContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#inspectTo.
    def visitInspectTo(self, ctx:CopyBookParser.InspectToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#inspectBeforeAfter.
    def visitInspectBeforeAfter(self, ctx:CopyBookParser.InspectBeforeAfterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#mergeStatement.
    def visitMergeStatement(self, ctx:CopyBookParser.MergeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#mergeOnKeyClause.
    def visitMergeOnKeyClause(self, ctx:CopyBookParser.MergeOnKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#mergeCollatingSequencePhrase.
    def visitMergeCollatingSequencePhrase(self, ctx:CopyBookParser.MergeCollatingSequencePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#mergeCollatingAlphanumeric.
    def visitMergeCollatingAlphanumeric(self, ctx:CopyBookParser.MergeCollatingAlphanumericContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#mergeCollatingNational.
    def visitMergeCollatingNational(self, ctx:CopyBookParser.MergeCollatingNationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#mergeUsing.
    def visitMergeUsing(self, ctx:CopyBookParser.MergeUsingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#mergeOutputProcedurePhrase.
    def visitMergeOutputProcedurePhrase(self, ctx:CopyBookParser.MergeOutputProcedurePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#mergeOutputThrough.
    def visitMergeOutputThrough(self, ctx:CopyBookParser.MergeOutputThroughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#mergeGivingPhrase.
    def visitMergeGivingPhrase(self, ctx:CopyBookParser.MergeGivingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#mergeGiving.
    def visitMergeGiving(self, ctx:CopyBookParser.MergeGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#moveStatement.
    def visitMoveStatement(self, ctx:CopyBookParser.MoveStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#moveToStatement.
    def visitMoveToStatement(self, ctx:CopyBookParser.MoveToStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#moveToSendingArea.
    def visitMoveToSendingArea(self, ctx:CopyBookParser.MoveToSendingAreaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#moveCorrespondingToStatement.
    def visitMoveCorrespondingToStatement(self, ctx:CopyBookParser.MoveCorrespondingToStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#moveCorrespondingToSendingArea.
    def visitMoveCorrespondingToSendingArea(self, ctx:CopyBookParser.MoveCorrespondingToSendingAreaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#multiplyStatement.
    def visitMultiplyStatement(self, ctx:CopyBookParser.MultiplyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#multiplyRegular.
    def visitMultiplyRegular(self, ctx:CopyBookParser.MultiplyRegularContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#multiplyRegularOperand.
    def visitMultiplyRegularOperand(self, ctx:CopyBookParser.MultiplyRegularOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#multiplyGiving.
    def visitMultiplyGiving(self, ctx:CopyBookParser.MultiplyGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#multiplyGivingOperand.
    def visitMultiplyGivingOperand(self, ctx:CopyBookParser.MultiplyGivingOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#multiplyGivingResult.
    def visitMultiplyGivingResult(self, ctx:CopyBookParser.MultiplyGivingResultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#openStatement.
    def visitOpenStatement(self, ctx:CopyBookParser.OpenStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#openInputStatement.
    def visitOpenInputStatement(self, ctx:CopyBookParser.OpenInputStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#openInput.
    def visitOpenInput(self, ctx:CopyBookParser.OpenInputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#openOutputStatement.
    def visitOpenOutputStatement(self, ctx:CopyBookParser.OpenOutputStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#openOutput.
    def visitOpenOutput(self, ctx:CopyBookParser.OpenOutputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#openIOStatement.
    def visitOpenIOStatement(self, ctx:CopyBookParser.OpenIOStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#openExtendStatement.
    def visitOpenExtendStatement(self, ctx:CopyBookParser.OpenExtendStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#performStatement.
    def visitPerformStatement(self, ctx:CopyBookParser.PerformStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#performInlineStatement.
    def visitPerformInlineStatement(self, ctx:CopyBookParser.PerformInlineStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#performProcedureStatement.
    def visitPerformProcedureStatement(self, ctx:CopyBookParser.PerformProcedureStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#performType.
    def visitPerformType(self, ctx:CopyBookParser.PerformTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#performTimes.
    def visitPerformTimes(self, ctx:CopyBookParser.PerformTimesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#performUntil.
    def visitPerformUntil(self, ctx:CopyBookParser.PerformUntilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#performVarying.
    def visitPerformVarying(self, ctx:CopyBookParser.PerformVaryingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#performVaryingClause.
    def visitPerformVaryingClause(self, ctx:CopyBookParser.PerformVaryingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#performVaryingPhrase.
    def visitPerformVaryingPhrase(self, ctx:CopyBookParser.PerformVaryingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#performAfter.
    def visitPerformAfter(self, ctx:CopyBookParser.PerformAfterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#performFrom.
    def visitPerformFrom(self, ctx:CopyBookParser.PerformFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#performBy.
    def visitPerformBy(self, ctx:CopyBookParser.PerformByContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#performTestClause.
    def visitPerformTestClause(self, ctx:CopyBookParser.PerformTestClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#purgeStatement.
    def visitPurgeStatement(self, ctx:CopyBookParser.PurgeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#readStatement.
    def visitReadStatement(self, ctx:CopyBookParser.ReadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#readInto.
    def visitReadInto(self, ctx:CopyBookParser.ReadIntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#readWith.
    def visitReadWith(self, ctx:CopyBookParser.ReadWithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#readKey.
    def visitReadKey(self, ctx:CopyBookParser.ReadKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#receiveStatement.
    def visitReceiveStatement(self, ctx:CopyBookParser.ReceiveStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#receiveFromStatement.
    def visitReceiveFromStatement(self, ctx:CopyBookParser.ReceiveFromStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#receiveFrom.
    def visitReceiveFrom(self, ctx:CopyBookParser.ReceiveFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#receiveIntoStatement.
    def visitReceiveIntoStatement(self, ctx:CopyBookParser.ReceiveIntoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#receiveNoData.
    def visitReceiveNoData(self, ctx:CopyBookParser.ReceiveNoDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#receiveWithData.
    def visitReceiveWithData(self, ctx:CopyBookParser.ReceiveWithDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#receiveBefore.
    def visitReceiveBefore(self, ctx:CopyBookParser.ReceiveBeforeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#receiveWith.
    def visitReceiveWith(self, ctx:CopyBookParser.ReceiveWithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#receiveThread.
    def visitReceiveThread(self, ctx:CopyBookParser.ReceiveThreadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#receiveSize.
    def visitReceiveSize(self, ctx:CopyBookParser.ReceiveSizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#receiveStatus.
    def visitReceiveStatus(self, ctx:CopyBookParser.ReceiveStatusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#releaseStatement.
    def visitReleaseStatement(self, ctx:CopyBookParser.ReleaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#returnStatement.
    def visitReturnStatement(self, ctx:CopyBookParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#returnInto.
    def visitReturnInto(self, ctx:CopyBookParser.ReturnIntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#rewriteStatement.
    def visitRewriteStatement(self, ctx:CopyBookParser.RewriteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#rewriteFrom.
    def visitRewriteFrom(self, ctx:CopyBookParser.RewriteFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#searchStatement.
    def visitSearchStatement(self, ctx:CopyBookParser.SearchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#searchVarying.
    def visitSearchVarying(self, ctx:CopyBookParser.SearchVaryingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#searchWhen.
    def visitSearchWhen(self, ctx:CopyBookParser.SearchWhenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#sendStatement.
    def visitSendStatement(self, ctx:CopyBookParser.SendStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#sendStatementSync.
    def visitSendStatementSync(self, ctx:CopyBookParser.SendStatementSyncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#sendStatementAsync.
    def visitSendStatementAsync(self, ctx:CopyBookParser.SendStatementAsyncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#sendFromPhrase.
    def visitSendFromPhrase(self, ctx:CopyBookParser.SendFromPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#sendWithPhrase.
    def visitSendWithPhrase(self, ctx:CopyBookParser.SendWithPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#sendReplacingPhrase.
    def visitSendReplacingPhrase(self, ctx:CopyBookParser.SendReplacingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#sendAdvancingPhrase.
    def visitSendAdvancingPhrase(self, ctx:CopyBookParser.SendAdvancingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#sendAdvancingPage.
    def visitSendAdvancingPage(self, ctx:CopyBookParser.SendAdvancingPageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#sendAdvancingLines.
    def visitSendAdvancingLines(self, ctx:CopyBookParser.SendAdvancingLinesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#sendAdvancingMnemonic.
    def visitSendAdvancingMnemonic(self, ctx:CopyBookParser.SendAdvancingMnemonicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#setStatement.
    def visitSetStatement(self, ctx:CopyBookParser.SetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#setToStatement.
    def visitSetToStatement(self, ctx:CopyBookParser.SetToStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#setUpDownByStatement.
    def visitSetUpDownByStatement(self, ctx:CopyBookParser.SetUpDownByStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#setTo.
    def visitSetTo(self, ctx:CopyBookParser.SetToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#setToValue.
    def visitSetToValue(self, ctx:CopyBookParser.SetToValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#setByValue.
    def visitSetByValue(self, ctx:CopyBookParser.SetByValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#sortStatement.
    def visitSortStatement(self, ctx:CopyBookParser.SortStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#sortOnKeyClause.
    def visitSortOnKeyClause(self, ctx:CopyBookParser.SortOnKeyClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#sortDuplicatesPhrase.
    def visitSortDuplicatesPhrase(self, ctx:CopyBookParser.SortDuplicatesPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#sortCollatingSequencePhrase.
    def visitSortCollatingSequencePhrase(self, ctx:CopyBookParser.SortCollatingSequencePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#sortCollatingAlphanumeric.
    def visitSortCollatingAlphanumeric(self, ctx:CopyBookParser.SortCollatingAlphanumericContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#sortCollatingNational.
    def visitSortCollatingNational(self, ctx:CopyBookParser.SortCollatingNationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#sortInputProcedurePhrase.
    def visitSortInputProcedurePhrase(self, ctx:CopyBookParser.SortInputProcedurePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#sortInputThrough.
    def visitSortInputThrough(self, ctx:CopyBookParser.SortInputThroughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#sortUsing.
    def visitSortUsing(self, ctx:CopyBookParser.SortUsingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#sortOutputProcedurePhrase.
    def visitSortOutputProcedurePhrase(self, ctx:CopyBookParser.SortOutputProcedurePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#sortOutputThrough.
    def visitSortOutputThrough(self, ctx:CopyBookParser.SortOutputThroughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#sortGivingPhrase.
    def visitSortGivingPhrase(self, ctx:CopyBookParser.SortGivingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#sortGiving.
    def visitSortGiving(self, ctx:CopyBookParser.SortGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#startStatement.
    def visitStartStatement(self, ctx:CopyBookParser.StartStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#startKey.
    def visitStartKey(self, ctx:CopyBookParser.StartKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#stopStatement.
    def visitStopStatement(self, ctx:CopyBookParser.StopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#stringStatement.
    def visitStringStatement(self, ctx:CopyBookParser.StringStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#stringSendingPhrase.
    def visitStringSendingPhrase(self, ctx:CopyBookParser.StringSendingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#stringSending.
    def visitStringSending(self, ctx:CopyBookParser.StringSendingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#stringDelimitedByPhrase.
    def visitStringDelimitedByPhrase(self, ctx:CopyBookParser.StringDelimitedByPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#stringForPhrase.
    def visitStringForPhrase(self, ctx:CopyBookParser.StringForPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#stringIntoPhrase.
    def visitStringIntoPhrase(self, ctx:CopyBookParser.StringIntoPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#stringWithPointerPhrase.
    def visitStringWithPointerPhrase(self, ctx:CopyBookParser.StringWithPointerPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#subtractStatement.
    def visitSubtractStatement(self, ctx:CopyBookParser.SubtractStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#subtractFromStatement.
    def visitSubtractFromStatement(self, ctx:CopyBookParser.SubtractFromStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#subtractFromGivingStatement.
    def visitSubtractFromGivingStatement(self, ctx:CopyBookParser.SubtractFromGivingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#subtractCorrespondingStatement.
    def visitSubtractCorrespondingStatement(self, ctx:CopyBookParser.SubtractCorrespondingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#subtractSubtrahend.
    def visitSubtractSubtrahend(self, ctx:CopyBookParser.SubtractSubtrahendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#subtractMinuend.
    def visitSubtractMinuend(self, ctx:CopyBookParser.SubtractMinuendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#subtractMinuendGiving.
    def visitSubtractMinuendGiving(self, ctx:CopyBookParser.SubtractMinuendGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#subtractGiving.
    def visitSubtractGiving(self, ctx:CopyBookParser.SubtractGivingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#subtractMinuendCorresponding.
    def visitSubtractMinuendCorresponding(self, ctx:CopyBookParser.SubtractMinuendCorrespondingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#transactionStatement.
    def visitTransactionStatement(self, ctx:CopyBookParser.TransactionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#transactionStart.
    def visitTransactionStart(self, ctx:CopyBookParser.TransactionStartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#transactionBody.
    def visitTransactionBody(self, ctx:CopyBookParser.TransactionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#transactionEnd.
    def visitTransactionEnd(self, ctx:CopyBookParser.TransactionEndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#transactionCancelStatement.
    def visitTransactionCancelStatement(self, ctx:CopyBookParser.TransactionCancelStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#terminateStatement.
    def visitTerminateStatement(self, ctx:CopyBookParser.TerminateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#unstringStatement.
    def visitUnstringStatement(self, ctx:CopyBookParser.UnstringStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#unstringSendingPhrase.
    def visitUnstringSendingPhrase(self, ctx:CopyBookParser.UnstringSendingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#unstringDelimitedByPhrase.
    def visitUnstringDelimitedByPhrase(self, ctx:CopyBookParser.UnstringDelimitedByPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#unstringOrAllPhrase.
    def visitUnstringOrAllPhrase(self, ctx:CopyBookParser.UnstringOrAllPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#unstringIntoPhrase.
    def visitUnstringIntoPhrase(self, ctx:CopyBookParser.UnstringIntoPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#unstringInto.
    def visitUnstringInto(self, ctx:CopyBookParser.UnstringIntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#unstringDelimiterIn.
    def visitUnstringDelimiterIn(self, ctx:CopyBookParser.UnstringDelimiterInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#unstringCountIn.
    def visitUnstringCountIn(self, ctx:CopyBookParser.UnstringCountInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#unstringWithPointerPhrase.
    def visitUnstringWithPointerPhrase(self, ctx:CopyBookParser.UnstringWithPointerPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#unstringTallyingPhrase.
    def visitUnstringTallyingPhrase(self, ctx:CopyBookParser.UnstringTallyingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#useStatement.
    def visitUseStatement(self, ctx:CopyBookParser.UseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#useFor.
    def visitUseFor(self, ctx:CopyBookParser.UseForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#useAfterClause.
    def visitUseAfterClause(self, ctx:CopyBookParser.UseAfterClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#useAfterOn.
    def visitUseAfterOn(self, ctx:CopyBookParser.UseAfterOnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#useDebugClause.
    def visitUseDebugClause(self, ctx:CopyBookParser.UseDebugClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#useDebugOn.
    def visitUseDebugOn(self, ctx:CopyBookParser.UseDebugOnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#useDeadLock.
    def visitUseDeadLock(self, ctx:CopyBookParser.UseDeadLockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#writeStatement.
    def visitWriteStatement(self, ctx:CopyBookParser.WriteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#writeFromPhrase.
    def visitWriteFromPhrase(self, ctx:CopyBookParser.WriteFromPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#writeAdvancingPhrase.
    def visitWriteAdvancingPhrase(self, ctx:CopyBookParser.WriteAdvancingPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#writeAdvancingPage.
    def visitWriteAdvancingPage(self, ctx:CopyBookParser.WriteAdvancingPageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#writeAdvancingLines.
    def visitWriteAdvancingLines(self, ctx:CopyBookParser.WriteAdvancingLinesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#writeAdvancingMnemonic.
    def visitWriteAdvancingMnemonic(self, ctx:CopyBookParser.WriteAdvancingMnemonicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#writeAtEndOfPagePhrase.
    def visitWriteAtEndOfPagePhrase(self, ctx:CopyBookParser.WriteAtEndOfPagePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#writeNotAtEndOfPagePhrase.
    def visitWriteNotAtEndOfPagePhrase(self, ctx:CopyBookParser.WriteNotAtEndOfPagePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#atEndPhrase.
    def visitAtEndPhrase(self, ctx:CopyBookParser.AtEndPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#notAtEndPhrase.
    def visitNotAtEndPhrase(self, ctx:CopyBookParser.NotAtEndPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#invalidKeyPhrase.
    def visitInvalidKeyPhrase(self, ctx:CopyBookParser.InvalidKeyPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#notInvalidKeyPhrase.
    def visitNotInvalidKeyPhrase(self, ctx:CopyBookParser.NotInvalidKeyPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#onOverflowPhrase.
    def visitOnOverflowPhrase(self, ctx:CopyBookParser.OnOverflowPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#notOnOverflowPhrase.
    def visitNotOnOverflowPhrase(self, ctx:CopyBookParser.NotOnOverflowPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#onSizeErrorPhrase.
    def visitOnSizeErrorPhrase(self, ctx:CopyBookParser.OnSizeErrorPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#notOnSizeErrorPhrase.
    def visitNotOnSizeErrorPhrase(self, ctx:CopyBookParser.NotOnSizeErrorPhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#onExceptionClause.
    def visitOnExceptionClause(self, ctx:CopyBookParser.OnExceptionClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#notOnExceptionClause.
    def visitNotOnExceptionClause(self, ctx:CopyBookParser.NotOnExceptionClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#arithmeticExpression.
    def visitArithmeticExpression(self, ctx:CopyBookParser.ArithmeticExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#plusMinus.
    def visitPlusMinus(self, ctx:CopyBookParser.PlusMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#multDivs.
    def visitMultDivs(self, ctx:CopyBookParser.MultDivsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#multDiv.
    def visitMultDiv(self, ctx:CopyBookParser.MultDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#powers.
    def visitPowers(self, ctx:CopyBookParser.PowersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#power.
    def visitPower(self, ctx:CopyBookParser.PowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#basis.
    def visitBasis(self, ctx:CopyBookParser.BasisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#condition.
    def visitCondition(self, ctx:CopyBookParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#andOrCondition.
    def visitAndOrCondition(self, ctx:CopyBookParser.AndOrConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#combinableCondition.
    def visitCombinableCondition(self, ctx:CopyBookParser.CombinableConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#simpleCondition.
    def visitSimpleCondition(self, ctx:CopyBookParser.SimpleConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#classCondition.
    def visitClassCondition(self, ctx:CopyBookParser.ClassConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#conditionNameReference.
    def visitConditionNameReference(self, ctx:CopyBookParser.ConditionNameReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#conditionNameSubscriptReference.
    def visitConditionNameSubscriptReference(self, ctx:CopyBookParser.ConditionNameSubscriptReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#relationCondition.
    def visitRelationCondition(self, ctx:CopyBookParser.RelationConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#relationSignCondition.
    def visitRelationSignCondition(self, ctx:CopyBookParser.RelationSignConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#relationArithmeticComparison.
    def visitRelationArithmeticComparison(self, ctx:CopyBookParser.RelationArithmeticComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#relationCombinedComparison.
    def visitRelationCombinedComparison(self, ctx:CopyBookParser.RelationCombinedComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#relationCombinedCondition.
    def visitRelationCombinedCondition(self, ctx:CopyBookParser.RelationCombinedConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#relationalOperator.
    def visitRelationalOperator(self, ctx:CopyBookParser.RelationalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#abbreviation.
    def visitAbbreviation(self, ctx:CopyBookParser.AbbreviationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#identifier.
    def visitIdentifier(self, ctx:CopyBookParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#tableCall.
    def visitTableCall(self, ctx:CopyBookParser.TableCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#functionCall.
    def visitFunctionCall(self, ctx:CopyBookParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#referenceModifier.
    def visitReferenceModifier(self, ctx:CopyBookParser.ReferenceModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#characterPosition.
    def visitCharacterPosition(self, ctx:CopyBookParser.CharacterPositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#length.
    def visitLength(self, ctx:CopyBookParser.LengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#subscript_.
    def visitSubscript_(self, ctx:CopyBookParser.Subscript_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#argument.
    def visitArgument(self, ctx:CopyBookParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#qualifiedDataName.
    def visitQualifiedDataName(self, ctx:CopyBookParser.QualifiedDataNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#qualifiedDataNameFormat1.
    def visitQualifiedDataNameFormat1(self, ctx:CopyBookParser.QualifiedDataNameFormat1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#qualifiedDataNameFormat2.
    def visitQualifiedDataNameFormat2(self, ctx:CopyBookParser.QualifiedDataNameFormat2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#qualifiedDataNameFormat3.
    def visitQualifiedDataNameFormat3(self, ctx:CopyBookParser.QualifiedDataNameFormat3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#qualifiedDataNameFormat4.
    def visitQualifiedDataNameFormat4(self, ctx:CopyBookParser.QualifiedDataNameFormat4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#qualifiedInData.
    def visitQualifiedInData(self, ctx:CopyBookParser.QualifiedInDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#inData.
    def visitInData(self, ctx:CopyBookParser.InDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#inFile.
    def visitInFile(self, ctx:CopyBookParser.InFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#inMnemonic.
    def visitInMnemonic(self, ctx:CopyBookParser.InMnemonicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#inSection.
    def visitInSection(self, ctx:CopyBookParser.InSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#inLibrary.
    def visitInLibrary(self, ctx:CopyBookParser.InLibraryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#inTable.
    def visitInTable(self, ctx:CopyBookParser.InTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#alphabetName.
    def visitAlphabetName(self, ctx:CopyBookParser.AlphabetNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#assignmentName.
    def visitAssignmentName(self, ctx:CopyBookParser.AssignmentNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#basisName.
    def visitBasisName(self, ctx:CopyBookParser.BasisNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#cdName.
    def visitCdName(self, ctx:CopyBookParser.CdNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#className.
    def visitClassName(self, ctx:CopyBookParser.ClassNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#computerName.
    def visitComputerName(self, ctx:CopyBookParser.ComputerNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#conditionName.
    def visitConditionName(self, ctx:CopyBookParser.ConditionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataName.
    def visitDataName(self, ctx:CopyBookParser.DataNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#dataDescName.
    def visitDataDescName(self, ctx:CopyBookParser.DataDescNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#environmentName.
    def visitEnvironmentName(self, ctx:CopyBookParser.EnvironmentNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#fileName.
    def visitFileName(self, ctx:CopyBookParser.FileNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#functionName.
    def visitFunctionName(self, ctx:CopyBookParser.FunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#indexName.
    def visitIndexName(self, ctx:CopyBookParser.IndexNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#languageName.
    def visitLanguageName(self, ctx:CopyBookParser.LanguageNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#libraryName.
    def visitLibraryName(self, ctx:CopyBookParser.LibraryNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#localName.
    def visitLocalName(self, ctx:CopyBookParser.LocalNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#mnemonicName.
    def visitMnemonicName(self, ctx:CopyBookParser.MnemonicNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#paragraphName.
    def visitParagraphName(self, ctx:CopyBookParser.ParagraphNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#procedureName.
    def visitProcedureName(self, ctx:CopyBookParser.ProcedureNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#programName.
    def visitProgramName(self, ctx:CopyBookParser.ProgramNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#recordName.
    def visitRecordName(self, ctx:CopyBookParser.RecordNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#reportName.
    def visitReportName(self, ctx:CopyBookParser.ReportNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#routineName.
    def visitRoutineName(self, ctx:CopyBookParser.RoutineNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#screenName.
    def visitScreenName(self, ctx:CopyBookParser.ScreenNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#sectionName.
    def visitSectionName(self, ctx:CopyBookParser.SectionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#systemName.
    def visitSystemName(self, ctx:CopyBookParser.SystemNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#symbolicCharacter.
    def visitSymbolicCharacter(self, ctx:CopyBookParser.SymbolicCharacterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#textName.
    def visitTextName(self, ctx:CopyBookParser.TextNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#booleanLiteral.
    def visitBooleanLiteral(self, ctx:CopyBookParser.BooleanLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#numericLiteral.
    def visitNumericLiteral(self, ctx:CopyBookParser.NumericLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#integerLiteral.
    def visitIntegerLiteral(self, ctx:CopyBookParser.IntegerLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#cicsDfhRespLiteral.
    def visitCicsDfhRespLiteral(self, ctx:CopyBookParser.CicsDfhRespLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#cicsDfhValueLiteral.
    def visitCicsDfhValueLiteral(self, ctx:CopyBookParser.CicsDfhValueLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#figurativeConstant.
    def visitFigurativeConstant(self, ctx:CopyBookParser.FigurativeConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#specialRegister.
    def visitSpecialRegister(self, ctx:CopyBookParser.SpecialRegisterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#commentEntry.
    def visitCommentEntry(self, ctx:CopyBookParser.CommentEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CopyBookParser#charDataKeyword.
    def visitCharDataKeyword(self, ctx:CopyBookParser.CharDataKeywordContext):
        return self.visitChildren(ctx)



del CopyBookParser