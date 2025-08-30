# Generated from ./app/tasks/grammar/dnp/DNP.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .DNPParser import DNPParser
else:
    from DNPParser import DNPParser

# This class defines a complete listener for a parse tree produced by DNPParser.
class DNPListener(ParseTreeListener):

    # Enter a parse tree produced by DNPParser#startRule.
    def enterStartRule(self, ctx:DNPParser.StartRuleContext):
        pass

    # Exit a parse tree produced by DNPParser#startRule.
    def exitStartRule(self, ctx:DNPParser.StartRuleContext):
        pass


    # Enter a parse tree produced by DNPParser#compilationUnit.
    def enterCompilationUnit(self, ctx:DNPParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by DNPParser#compilationUnit.
    def exitCompilationUnit(self, ctx:DNPParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by DNPParser#programUnit.
    def enterProgramUnit(self, ctx:DNPParser.ProgramUnitContext):
        pass

    # Exit a parse tree produced by DNPParser#programUnit.
    def exitProgramUnit(self, ctx:DNPParser.ProgramUnitContext):
        pass


    # Enter a parse tree produced by DNPParser#endProgramStatement.
    def enterEndProgramStatement(self, ctx:DNPParser.EndProgramStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#endProgramStatement.
    def exitEndProgramStatement(self, ctx:DNPParser.EndProgramStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#identificationDivision.
    def enterIdentificationDivision(self, ctx:DNPParser.IdentificationDivisionContext):
        pass

    # Exit a parse tree produced by DNPParser#identificationDivision.
    def exitIdentificationDivision(self, ctx:DNPParser.IdentificationDivisionContext):
        pass


    # Enter a parse tree produced by DNPParser#identificationDivisionBody.
    def enterIdentificationDivisionBody(self, ctx:DNPParser.IdentificationDivisionBodyContext):
        pass

    # Exit a parse tree produced by DNPParser#identificationDivisionBody.
    def exitIdentificationDivisionBody(self, ctx:DNPParser.IdentificationDivisionBodyContext):
        pass


    # Enter a parse tree produced by DNPParser#programIdParagraph.
    def enterProgramIdParagraph(self, ctx:DNPParser.ProgramIdParagraphContext):
        pass

    # Exit a parse tree produced by DNPParser#programIdParagraph.
    def exitProgramIdParagraph(self, ctx:DNPParser.ProgramIdParagraphContext):
        pass


    # Enter a parse tree produced by DNPParser#author_name.
    def enterAuthor_name(self, ctx:DNPParser.Author_nameContext):
        pass

    # Exit a parse tree produced by DNPParser#author_name.
    def exitAuthor_name(self, ctx:DNPParser.Author_nameContext):
        pass


    # Enter a parse tree produced by DNPParser#authorParagraph.
    def enterAuthorParagraph(self, ctx:DNPParser.AuthorParagraphContext):
        pass

    # Exit a parse tree produced by DNPParser#authorParagraph.
    def exitAuthorParagraph(self, ctx:DNPParser.AuthorParagraphContext):
        pass


    # Enter a parse tree produced by DNPParser#installationParagraph.
    def enterInstallationParagraph(self, ctx:DNPParser.InstallationParagraphContext):
        pass

    # Exit a parse tree produced by DNPParser#installationParagraph.
    def exitInstallationParagraph(self, ctx:DNPParser.InstallationParagraphContext):
        pass


    # Enter a parse tree produced by DNPParser#dateWrittenParagraph.
    def enterDateWrittenParagraph(self, ctx:DNPParser.DateWrittenParagraphContext):
        pass

    # Exit a parse tree produced by DNPParser#dateWrittenParagraph.
    def exitDateWrittenParagraph(self, ctx:DNPParser.DateWrittenParagraphContext):
        pass


    # Enter a parse tree produced by DNPParser#dateCompiledParagraph.
    def enterDateCompiledParagraph(self, ctx:DNPParser.DateCompiledParagraphContext):
        pass

    # Exit a parse tree produced by DNPParser#dateCompiledParagraph.
    def exitDateCompiledParagraph(self, ctx:DNPParser.DateCompiledParagraphContext):
        pass


    # Enter a parse tree produced by DNPParser#securityParagraph.
    def enterSecurityParagraph(self, ctx:DNPParser.SecurityParagraphContext):
        pass

    # Exit a parse tree produced by DNPParser#securityParagraph.
    def exitSecurityParagraph(self, ctx:DNPParser.SecurityParagraphContext):
        pass


    # Enter a parse tree produced by DNPParser#remarksParagraph.
    def enterRemarksParagraph(self, ctx:DNPParser.RemarksParagraphContext):
        pass

    # Exit a parse tree produced by DNPParser#remarksParagraph.
    def exitRemarksParagraph(self, ctx:DNPParser.RemarksParagraphContext):
        pass


    # Enter a parse tree produced by DNPParser#environmentDivision.
    def enterEnvironmentDivision(self, ctx:DNPParser.EnvironmentDivisionContext):
        pass

    # Exit a parse tree produced by DNPParser#environmentDivision.
    def exitEnvironmentDivision(self, ctx:DNPParser.EnvironmentDivisionContext):
        pass


    # Enter a parse tree produced by DNPParser#environmentDivisionBody.
    def enterEnvironmentDivisionBody(self, ctx:DNPParser.EnvironmentDivisionBodyContext):
        pass

    # Exit a parse tree produced by DNPParser#environmentDivisionBody.
    def exitEnvironmentDivisionBody(self, ctx:DNPParser.EnvironmentDivisionBodyContext):
        pass


    # Enter a parse tree produced by DNPParser#configurationSection.
    def enterConfigurationSection(self, ctx:DNPParser.ConfigurationSectionContext):
        pass

    # Exit a parse tree produced by DNPParser#configurationSection.
    def exitConfigurationSection(self, ctx:DNPParser.ConfigurationSectionContext):
        pass


    # Enter a parse tree produced by DNPParser#configurationSectionParagraph.
    def enterConfigurationSectionParagraph(self, ctx:DNPParser.ConfigurationSectionParagraphContext):
        pass

    # Exit a parse tree produced by DNPParser#configurationSectionParagraph.
    def exitConfigurationSectionParagraph(self, ctx:DNPParser.ConfigurationSectionParagraphContext):
        pass


    # Enter a parse tree produced by DNPParser#sourceComputerParagraph.
    def enterSourceComputerParagraph(self, ctx:DNPParser.SourceComputerParagraphContext):
        pass

    # Exit a parse tree produced by DNPParser#sourceComputerParagraph.
    def exitSourceComputerParagraph(self, ctx:DNPParser.SourceComputerParagraphContext):
        pass


    # Enter a parse tree produced by DNPParser#objectComputerParagraph.
    def enterObjectComputerParagraph(self, ctx:DNPParser.ObjectComputerParagraphContext):
        pass

    # Exit a parse tree produced by DNPParser#objectComputerParagraph.
    def exitObjectComputerParagraph(self, ctx:DNPParser.ObjectComputerParagraphContext):
        pass


    # Enter a parse tree produced by DNPParser#objectComputerClause.
    def enterObjectComputerClause(self, ctx:DNPParser.ObjectComputerClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#objectComputerClause.
    def exitObjectComputerClause(self, ctx:DNPParser.ObjectComputerClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#memorySizeClause.
    def enterMemorySizeClause(self, ctx:DNPParser.MemorySizeClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#memorySizeClause.
    def exitMemorySizeClause(self, ctx:DNPParser.MemorySizeClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#diskSizeClause.
    def enterDiskSizeClause(self, ctx:DNPParser.DiskSizeClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#diskSizeClause.
    def exitDiskSizeClause(self, ctx:DNPParser.DiskSizeClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#collatingSequenceClause.
    def enterCollatingSequenceClause(self, ctx:DNPParser.CollatingSequenceClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#collatingSequenceClause.
    def exitCollatingSequenceClause(self, ctx:DNPParser.CollatingSequenceClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#collatingSequenceClauseAlphanumeric.
    def enterCollatingSequenceClauseAlphanumeric(self, ctx:DNPParser.CollatingSequenceClauseAlphanumericContext):
        pass

    # Exit a parse tree produced by DNPParser#collatingSequenceClauseAlphanumeric.
    def exitCollatingSequenceClauseAlphanumeric(self, ctx:DNPParser.CollatingSequenceClauseAlphanumericContext):
        pass


    # Enter a parse tree produced by DNPParser#collatingSequenceClauseNational.
    def enterCollatingSequenceClauseNational(self, ctx:DNPParser.CollatingSequenceClauseNationalContext):
        pass

    # Exit a parse tree produced by DNPParser#collatingSequenceClauseNational.
    def exitCollatingSequenceClauseNational(self, ctx:DNPParser.CollatingSequenceClauseNationalContext):
        pass


    # Enter a parse tree produced by DNPParser#segmentLimitClause.
    def enterSegmentLimitClause(self, ctx:DNPParser.SegmentLimitClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#segmentLimitClause.
    def exitSegmentLimitClause(self, ctx:DNPParser.SegmentLimitClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#characterSetClause.
    def enterCharacterSetClause(self, ctx:DNPParser.CharacterSetClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#characterSetClause.
    def exitCharacterSetClause(self, ctx:DNPParser.CharacterSetClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#specialNamesParagraph.
    def enterSpecialNamesParagraph(self, ctx:DNPParser.SpecialNamesParagraphContext):
        pass

    # Exit a parse tree produced by DNPParser#specialNamesParagraph.
    def exitSpecialNamesParagraph(self, ctx:DNPParser.SpecialNamesParagraphContext):
        pass


    # Enter a parse tree produced by DNPParser#specialNameClause.
    def enterSpecialNameClause(self, ctx:DNPParser.SpecialNameClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#specialNameClause.
    def exitSpecialNameClause(self, ctx:DNPParser.SpecialNameClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#alphabetClause.
    def enterAlphabetClause(self, ctx:DNPParser.AlphabetClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#alphabetClause.
    def exitAlphabetClause(self, ctx:DNPParser.AlphabetClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#alphabetClauseFormat1.
    def enterAlphabetClauseFormat1(self, ctx:DNPParser.AlphabetClauseFormat1Context):
        pass

    # Exit a parse tree produced by DNPParser#alphabetClauseFormat1.
    def exitAlphabetClauseFormat1(self, ctx:DNPParser.AlphabetClauseFormat1Context):
        pass


    # Enter a parse tree produced by DNPParser#alphabetLiterals.
    def enterAlphabetLiterals(self, ctx:DNPParser.AlphabetLiteralsContext):
        pass

    # Exit a parse tree produced by DNPParser#alphabetLiterals.
    def exitAlphabetLiterals(self, ctx:DNPParser.AlphabetLiteralsContext):
        pass


    # Enter a parse tree produced by DNPParser#alphabetThrough.
    def enterAlphabetThrough(self, ctx:DNPParser.AlphabetThroughContext):
        pass

    # Exit a parse tree produced by DNPParser#alphabetThrough.
    def exitAlphabetThrough(self, ctx:DNPParser.AlphabetThroughContext):
        pass


    # Enter a parse tree produced by DNPParser#alphabetAlso.
    def enterAlphabetAlso(self, ctx:DNPParser.AlphabetAlsoContext):
        pass

    # Exit a parse tree produced by DNPParser#alphabetAlso.
    def exitAlphabetAlso(self, ctx:DNPParser.AlphabetAlsoContext):
        pass


    # Enter a parse tree produced by DNPParser#alphabetClauseFormat2.
    def enterAlphabetClauseFormat2(self, ctx:DNPParser.AlphabetClauseFormat2Context):
        pass

    # Exit a parse tree produced by DNPParser#alphabetClauseFormat2.
    def exitAlphabetClauseFormat2(self, ctx:DNPParser.AlphabetClauseFormat2Context):
        pass


    # Enter a parse tree produced by DNPParser#channelClause.
    def enterChannelClause(self, ctx:DNPParser.ChannelClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#channelClause.
    def exitChannelClause(self, ctx:DNPParser.ChannelClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#classClause.
    def enterClassClause(self, ctx:DNPParser.ClassClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#classClause.
    def exitClassClause(self, ctx:DNPParser.ClassClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#classClauseThrough.
    def enterClassClauseThrough(self, ctx:DNPParser.ClassClauseThroughContext):
        pass

    # Exit a parse tree produced by DNPParser#classClauseThrough.
    def exitClassClauseThrough(self, ctx:DNPParser.ClassClauseThroughContext):
        pass


    # Enter a parse tree produced by DNPParser#classClauseFrom.
    def enterClassClauseFrom(self, ctx:DNPParser.ClassClauseFromContext):
        pass

    # Exit a parse tree produced by DNPParser#classClauseFrom.
    def exitClassClauseFrom(self, ctx:DNPParser.ClassClauseFromContext):
        pass


    # Enter a parse tree produced by DNPParser#classClauseTo.
    def enterClassClauseTo(self, ctx:DNPParser.ClassClauseToContext):
        pass

    # Exit a parse tree produced by DNPParser#classClauseTo.
    def exitClassClauseTo(self, ctx:DNPParser.ClassClauseToContext):
        pass


    # Enter a parse tree produced by DNPParser#currencySignClause.
    def enterCurrencySignClause(self, ctx:DNPParser.CurrencySignClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#currencySignClause.
    def exitCurrencySignClause(self, ctx:DNPParser.CurrencySignClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#decimalPointClause.
    def enterDecimalPointClause(self, ctx:DNPParser.DecimalPointClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#decimalPointClause.
    def exitDecimalPointClause(self, ctx:DNPParser.DecimalPointClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#defaultComputationalSignClause.
    def enterDefaultComputationalSignClause(self, ctx:DNPParser.DefaultComputationalSignClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#defaultComputationalSignClause.
    def exitDefaultComputationalSignClause(self, ctx:DNPParser.DefaultComputationalSignClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#defaultDisplaySignClause.
    def enterDefaultDisplaySignClause(self, ctx:DNPParser.DefaultDisplaySignClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#defaultDisplaySignClause.
    def exitDefaultDisplaySignClause(self, ctx:DNPParser.DefaultDisplaySignClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#environmentSwitchNameClause.
    def enterEnvironmentSwitchNameClause(self, ctx:DNPParser.EnvironmentSwitchNameClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#environmentSwitchNameClause.
    def exitEnvironmentSwitchNameClause(self, ctx:DNPParser.EnvironmentSwitchNameClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#environmentSwitchNameSpecialNamesStatusPhrase.
    def enterEnvironmentSwitchNameSpecialNamesStatusPhrase(self, ctx:DNPParser.EnvironmentSwitchNameSpecialNamesStatusPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#environmentSwitchNameSpecialNamesStatusPhrase.
    def exitEnvironmentSwitchNameSpecialNamesStatusPhrase(self, ctx:DNPParser.EnvironmentSwitchNameSpecialNamesStatusPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#odtClause.
    def enterOdtClause(self, ctx:DNPParser.OdtClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#odtClause.
    def exitOdtClause(self, ctx:DNPParser.OdtClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#reserveNetworkClause.
    def enterReserveNetworkClause(self, ctx:DNPParser.ReserveNetworkClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#reserveNetworkClause.
    def exitReserveNetworkClause(self, ctx:DNPParser.ReserveNetworkClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#symbolicCharactersClause.
    def enterSymbolicCharactersClause(self, ctx:DNPParser.SymbolicCharactersClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#symbolicCharactersClause.
    def exitSymbolicCharactersClause(self, ctx:DNPParser.SymbolicCharactersClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#symbolicCharacters.
    def enterSymbolicCharacters(self, ctx:DNPParser.SymbolicCharactersContext):
        pass

    # Exit a parse tree produced by DNPParser#symbolicCharacters.
    def exitSymbolicCharacters(self, ctx:DNPParser.SymbolicCharactersContext):
        pass


    # Enter a parse tree produced by DNPParser#inputOutputSection.
    def enterInputOutputSection(self, ctx:DNPParser.InputOutputSectionContext):
        pass

    # Exit a parse tree produced by DNPParser#inputOutputSection.
    def exitInputOutputSection(self, ctx:DNPParser.InputOutputSectionContext):
        pass


    # Enter a parse tree produced by DNPParser#inputOutputSectionParagraph.
    def enterInputOutputSectionParagraph(self, ctx:DNPParser.InputOutputSectionParagraphContext):
        pass

    # Exit a parse tree produced by DNPParser#inputOutputSectionParagraph.
    def exitInputOutputSectionParagraph(self, ctx:DNPParser.InputOutputSectionParagraphContext):
        pass


    # Enter a parse tree produced by DNPParser#fileControlParagraph.
    def enterFileControlParagraph(self, ctx:DNPParser.FileControlParagraphContext):
        pass

    # Exit a parse tree produced by DNPParser#fileControlParagraph.
    def exitFileControlParagraph(self, ctx:DNPParser.FileControlParagraphContext):
        pass


    # Enter a parse tree produced by DNPParser#fileControlEntry.
    def enterFileControlEntry(self, ctx:DNPParser.FileControlEntryContext):
        pass

    # Exit a parse tree produced by DNPParser#fileControlEntry.
    def exitFileControlEntry(self, ctx:DNPParser.FileControlEntryContext):
        pass


    # Enter a parse tree produced by DNPParser#selectClause.
    def enterSelectClause(self, ctx:DNPParser.SelectClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#selectClause.
    def exitSelectClause(self, ctx:DNPParser.SelectClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#fileControlClause.
    def enterFileControlClause(self, ctx:DNPParser.FileControlClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#fileControlClause.
    def exitFileControlClause(self, ctx:DNPParser.FileControlClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#assignClause.
    def enterAssignClause(self, ctx:DNPParser.AssignClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#assignClause.
    def exitAssignClause(self, ctx:DNPParser.AssignClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#reserveClause.
    def enterReserveClause(self, ctx:DNPParser.ReserveClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#reserveClause.
    def exitReserveClause(self, ctx:DNPParser.ReserveClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#organizationClause.
    def enterOrganizationClause(self, ctx:DNPParser.OrganizationClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#organizationClause.
    def exitOrganizationClause(self, ctx:DNPParser.OrganizationClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#paddingCharacterClause.
    def enterPaddingCharacterClause(self, ctx:DNPParser.PaddingCharacterClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#paddingCharacterClause.
    def exitPaddingCharacterClause(self, ctx:DNPParser.PaddingCharacterClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#recordDelimiterClause.
    def enterRecordDelimiterClause(self, ctx:DNPParser.RecordDelimiterClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#recordDelimiterClause.
    def exitRecordDelimiterClause(self, ctx:DNPParser.RecordDelimiterClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#accessModeClause.
    def enterAccessModeClause(self, ctx:DNPParser.AccessModeClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#accessModeClause.
    def exitAccessModeClause(self, ctx:DNPParser.AccessModeClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#recordKeyClause.
    def enterRecordKeyClause(self, ctx:DNPParser.RecordKeyClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#recordKeyClause.
    def exitRecordKeyClause(self, ctx:DNPParser.RecordKeyClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#alternateRecordKeyClause.
    def enterAlternateRecordKeyClause(self, ctx:DNPParser.AlternateRecordKeyClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#alternateRecordKeyClause.
    def exitAlternateRecordKeyClause(self, ctx:DNPParser.AlternateRecordKeyClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#passwordClause.
    def enterPasswordClause(self, ctx:DNPParser.PasswordClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#passwordClause.
    def exitPasswordClause(self, ctx:DNPParser.PasswordClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#fileStatusClause.
    def enterFileStatusClause(self, ctx:DNPParser.FileStatusClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#fileStatusClause.
    def exitFileStatusClause(self, ctx:DNPParser.FileStatusClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#relativeKeyClause.
    def enterRelativeKeyClause(self, ctx:DNPParser.RelativeKeyClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#relativeKeyClause.
    def exitRelativeKeyClause(self, ctx:DNPParser.RelativeKeyClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#ioControlParagraph.
    def enterIoControlParagraph(self, ctx:DNPParser.IoControlParagraphContext):
        pass

    # Exit a parse tree produced by DNPParser#ioControlParagraph.
    def exitIoControlParagraph(self, ctx:DNPParser.IoControlParagraphContext):
        pass


    # Enter a parse tree produced by DNPParser#ioControlClause.
    def enterIoControlClause(self, ctx:DNPParser.IoControlClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#ioControlClause.
    def exitIoControlClause(self, ctx:DNPParser.IoControlClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#rerunClause.
    def enterRerunClause(self, ctx:DNPParser.RerunClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#rerunClause.
    def exitRerunClause(self, ctx:DNPParser.RerunClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#rerunEveryRecords.
    def enterRerunEveryRecords(self, ctx:DNPParser.RerunEveryRecordsContext):
        pass

    # Exit a parse tree produced by DNPParser#rerunEveryRecords.
    def exitRerunEveryRecords(self, ctx:DNPParser.RerunEveryRecordsContext):
        pass


    # Enter a parse tree produced by DNPParser#rerunEveryOf.
    def enterRerunEveryOf(self, ctx:DNPParser.RerunEveryOfContext):
        pass

    # Exit a parse tree produced by DNPParser#rerunEveryOf.
    def exitRerunEveryOf(self, ctx:DNPParser.RerunEveryOfContext):
        pass


    # Enter a parse tree produced by DNPParser#rerunEveryClock.
    def enterRerunEveryClock(self, ctx:DNPParser.RerunEveryClockContext):
        pass

    # Exit a parse tree produced by DNPParser#rerunEveryClock.
    def exitRerunEveryClock(self, ctx:DNPParser.RerunEveryClockContext):
        pass


    # Enter a parse tree produced by DNPParser#sameClause.
    def enterSameClause(self, ctx:DNPParser.SameClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#sameClause.
    def exitSameClause(self, ctx:DNPParser.SameClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#multipleFileClause.
    def enterMultipleFileClause(self, ctx:DNPParser.MultipleFileClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#multipleFileClause.
    def exitMultipleFileClause(self, ctx:DNPParser.MultipleFileClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#multipleFilePosition.
    def enterMultipleFilePosition(self, ctx:DNPParser.MultipleFilePositionContext):
        pass

    # Exit a parse tree produced by DNPParser#multipleFilePosition.
    def exitMultipleFilePosition(self, ctx:DNPParser.MultipleFilePositionContext):
        pass


    # Enter a parse tree produced by DNPParser#commitmentControlClause.
    def enterCommitmentControlClause(self, ctx:DNPParser.CommitmentControlClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#commitmentControlClause.
    def exitCommitmentControlClause(self, ctx:DNPParser.CommitmentControlClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#dataDivision.
    def enterDataDivision(self, ctx:DNPParser.DataDivisionContext):
        pass

    # Exit a parse tree produced by DNPParser#dataDivision.
    def exitDataDivision(self, ctx:DNPParser.DataDivisionContext):
        pass


    # Enter a parse tree produced by DNPParser#dataDivisionSection.
    def enterDataDivisionSection(self, ctx:DNPParser.DataDivisionSectionContext):
        pass

    # Exit a parse tree produced by DNPParser#dataDivisionSection.
    def exitDataDivisionSection(self, ctx:DNPParser.DataDivisionSectionContext):
        pass


    # Enter a parse tree produced by DNPParser#fileSection.
    def enterFileSection(self, ctx:DNPParser.FileSectionContext):
        pass

    # Exit a parse tree produced by DNPParser#fileSection.
    def exitFileSection(self, ctx:DNPParser.FileSectionContext):
        pass


    # Enter a parse tree produced by DNPParser#fileDescriptionEntry.
    def enterFileDescriptionEntry(self, ctx:DNPParser.FileDescriptionEntryContext):
        pass

    # Exit a parse tree produced by DNPParser#fileDescriptionEntry.
    def exitFileDescriptionEntry(self, ctx:DNPParser.FileDescriptionEntryContext):
        pass


    # Enter a parse tree produced by DNPParser#fileDescriptionEntryClause.
    def enterFileDescriptionEntryClause(self, ctx:DNPParser.FileDescriptionEntryClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#fileDescriptionEntryClause.
    def exitFileDescriptionEntryClause(self, ctx:DNPParser.FileDescriptionEntryClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#externalClause.
    def enterExternalClause(self, ctx:DNPParser.ExternalClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#externalClause.
    def exitExternalClause(self, ctx:DNPParser.ExternalClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#globalClause.
    def enterGlobalClause(self, ctx:DNPParser.GlobalClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#globalClause.
    def exitGlobalClause(self, ctx:DNPParser.GlobalClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#blockContainsClause.
    def enterBlockContainsClause(self, ctx:DNPParser.BlockContainsClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#blockContainsClause.
    def exitBlockContainsClause(self, ctx:DNPParser.BlockContainsClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#blockContainsTo.
    def enterBlockContainsTo(self, ctx:DNPParser.BlockContainsToContext):
        pass

    # Exit a parse tree produced by DNPParser#blockContainsTo.
    def exitBlockContainsTo(self, ctx:DNPParser.BlockContainsToContext):
        pass


    # Enter a parse tree produced by DNPParser#recordContainsClause.
    def enterRecordContainsClause(self, ctx:DNPParser.RecordContainsClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#recordContainsClause.
    def exitRecordContainsClause(self, ctx:DNPParser.RecordContainsClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#recordContainsClauseFormat1.
    def enterRecordContainsClauseFormat1(self, ctx:DNPParser.RecordContainsClauseFormat1Context):
        pass

    # Exit a parse tree produced by DNPParser#recordContainsClauseFormat1.
    def exitRecordContainsClauseFormat1(self, ctx:DNPParser.RecordContainsClauseFormat1Context):
        pass


    # Enter a parse tree produced by DNPParser#recordContainsClauseFormat2.
    def enterRecordContainsClauseFormat2(self, ctx:DNPParser.RecordContainsClauseFormat2Context):
        pass

    # Exit a parse tree produced by DNPParser#recordContainsClauseFormat2.
    def exitRecordContainsClauseFormat2(self, ctx:DNPParser.RecordContainsClauseFormat2Context):
        pass


    # Enter a parse tree produced by DNPParser#recordContainsClauseFormat3.
    def enterRecordContainsClauseFormat3(self, ctx:DNPParser.RecordContainsClauseFormat3Context):
        pass

    # Exit a parse tree produced by DNPParser#recordContainsClauseFormat3.
    def exitRecordContainsClauseFormat3(self, ctx:DNPParser.RecordContainsClauseFormat3Context):
        pass


    # Enter a parse tree produced by DNPParser#recordContainsTo.
    def enterRecordContainsTo(self, ctx:DNPParser.RecordContainsToContext):
        pass

    # Exit a parse tree produced by DNPParser#recordContainsTo.
    def exitRecordContainsTo(self, ctx:DNPParser.RecordContainsToContext):
        pass


    # Enter a parse tree produced by DNPParser#labelRecordsClause.
    def enterLabelRecordsClause(self, ctx:DNPParser.LabelRecordsClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#labelRecordsClause.
    def exitLabelRecordsClause(self, ctx:DNPParser.LabelRecordsClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#valueOfClause.
    def enterValueOfClause(self, ctx:DNPParser.ValueOfClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#valueOfClause.
    def exitValueOfClause(self, ctx:DNPParser.ValueOfClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#valuePair.
    def enterValuePair(self, ctx:DNPParser.ValuePairContext):
        pass

    # Exit a parse tree produced by DNPParser#valuePair.
    def exitValuePair(self, ctx:DNPParser.ValuePairContext):
        pass


    # Enter a parse tree produced by DNPParser#dataRecordsClause.
    def enterDataRecordsClause(self, ctx:DNPParser.DataRecordsClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#dataRecordsClause.
    def exitDataRecordsClause(self, ctx:DNPParser.DataRecordsClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#linageClause.
    def enterLinageClause(self, ctx:DNPParser.LinageClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#linageClause.
    def exitLinageClause(self, ctx:DNPParser.LinageClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#linageAt.
    def enterLinageAt(self, ctx:DNPParser.LinageAtContext):
        pass

    # Exit a parse tree produced by DNPParser#linageAt.
    def exitLinageAt(self, ctx:DNPParser.LinageAtContext):
        pass


    # Enter a parse tree produced by DNPParser#linageFootingAt.
    def enterLinageFootingAt(self, ctx:DNPParser.LinageFootingAtContext):
        pass

    # Exit a parse tree produced by DNPParser#linageFootingAt.
    def exitLinageFootingAt(self, ctx:DNPParser.LinageFootingAtContext):
        pass


    # Enter a parse tree produced by DNPParser#linageLinesAtTop.
    def enterLinageLinesAtTop(self, ctx:DNPParser.LinageLinesAtTopContext):
        pass

    # Exit a parse tree produced by DNPParser#linageLinesAtTop.
    def exitLinageLinesAtTop(self, ctx:DNPParser.LinageLinesAtTopContext):
        pass


    # Enter a parse tree produced by DNPParser#linageLinesAtBottom.
    def enterLinageLinesAtBottom(self, ctx:DNPParser.LinageLinesAtBottomContext):
        pass

    # Exit a parse tree produced by DNPParser#linageLinesAtBottom.
    def exitLinageLinesAtBottom(self, ctx:DNPParser.LinageLinesAtBottomContext):
        pass


    # Enter a parse tree produced by DNPParser#recordingModeClause.
    def enterRecordingModeClause(self, ctx:DNPParser.RecordingModeClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#recordingModeClause.
    def exitRecordingModeClause(self, ctx:DNPParser.RecordingModeClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#modeStatement.
    def enterModeStatement(self, ctx:DNPParser.ModeStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#modeStatement.
    def exitModeStatement(self, ctx:DNPParser.ModeStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#codeSetClause.
    def enterCodeSetClause(self, ctx:DNPParser.CodeSetClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#codeSetClause.
    def exitCodeSetClause(self, ctx:DNPParser.CodeSetClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#reportClause.
    def enterReportClause(self, ctx:DNPParser.ReportClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#reportClause.
    def exitReportClause(self, ctx:DNPParser.ReportClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#dataBaseSection.
    def enterDataBaseSection(self, ctx:DNPParser.DataBaseSectionContext):
        pass

    # Exit a parse tree produced by DNPParser#dataBaseSection.
    def exitDataBaseSection(self, ctx:DNPParser.DataBaseSectionContext):
        pass


    # Enter a parse tree produced by DNPParser#dataBaseSectionEntry.
    def enterDataBaseSectionEntry(self, ctx:DNPParser.DataBaseSectionEntryContext):
        pass

    # Exit a parse tree produced by DNPParser#dataBaseSectionEntry.
    def exitDataBaseSectionEntry(self, ctx:DNPParser.DataBaseSectionEntryContext):
        pass


    # Enter a parse tree produced by DNPParser#dataBaseDeclare.
    def enterDataBaseDeclare(self, ctx:DNPParser.DataBaseDeclareContext):
        pass

    # Exit a parse tree produced by DNPParser#dataBaseDeclare.
    def exitDataBaseDeclare(self, ctx:DNPParser.DataBaseDeclareContext):
        pass


    # Enter a parse tree produced by DNPParser#dataBaseDatasetDeclare.
    def enterDataBaseDatasetDeclare(self, ctx:DNPParser.DataBaseDatasetDeclareContext):
        pass

    # Exit a parse tree produced by DNPParser#dataBaseDatasetDeclare.
    def exitDataBaseDatasetDeclare(self, ctx:DNPParser.DataBaseDatasetDeclareContext):
        pass


    # Enter a parse tree produced by DNPParser#invokeClause.
    def enterInvokeClause(self, ctx:DNPParser.InvokeClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#invokeClause.
    def exitInvokeClause(self, ctx:DNPParser.InvokeClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#usingClause.
    def enterUsingClause(self, ctx:DNPParser.UsingClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#usingClause.
    def exitUsingClause(self, ctx:DNPParser.UsingClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#workingStorageSection.
    def enterWorkingStorageSection(self, ctx:DNPParser.WorkingStorageSectionContext):
        pass

    # Exit a parse tree produced by DNPParser#workingStorageSection.
    def exitWorkingStorageSection(self, ctx:DNPParser.WorkingStorageSectionContext):
        pass


    # Enter a parse tree produced by DNPParser#linkageSection.
    def enterLinkageSection(self, ctx:DNPParser.LinkageSectionContext):
        pass

    # Exit a parse tree produced by DNPParser#linkageSection.
    def exitLinkageSection(self, ctx:DNPParser.LinkageSectionContext):
        pass


    # Enter a parse tree produced by DNPParser#communicationSection.
    def enterCommunicationSection(self, ctx:DNPParser.CommunicationSectionContext):
        pass

    # Exit a parse tree produced by DNPParser#communicationSection.
    def exitCommunicationSection(self, ctx:DNPParser.CommunicationSectionContext):
        pass


    # Enter a parse tree produced by DNPParser#communicationDescriptionEntry.
    def enterCommunicationDescriptionEntry(self, ctx:DNPParser.CommunicationDescriptionEntryContext):
        pass

    # Exit a parse tree produced by DNPParser#communicationDescriptionEntry.
    def exitCommunicationDescriptionEntry(self, ctx:DNPParser.CommunicationDescriptionEntryContext):
        pass


    # Enter a parse tree produced by DNPParser#communicationDescriptionEntryFormat1.
    def enterCommunicationDescriptionEntryFormat1(self, ctx:DNPParser.CommunicationDescriptionEntryFormat1Context):
        pass

    # Exit a parse tree produced by DNPParser#communicationDescriptionEntryFormat1.
    def exitCommunicationDescriptionEntryFormat1(self, ctx:DNPParser.CommunicationDescriptionEntryFormat1Context):
        pass


    # Enter a parse tree produced by DNPParser#communicationDescriptionEntryFormat2.
    def enterCommunicationDescriptionEntryFormat2(self, ctx:DNPParser.CommunicationDescriptionEntryFormat2Context):
        pass

    # Exit a parse tree produced by DNPParser#communicationDescriptionEntryFormat2.
    def exitCommunicationDescriptionEntryFormat2(self, ctx:DNPParser.CommunicationDescriptionEntryFormat2Context):
        pass


    # Enter a parse tree produced by DNPParser#communicationDescriptionEntryFormat3.
    def enterCommunicationDescriptionEntryFormat3(self, ctx:DNPParser.CommunicationDescriptionEntryFormat3Context):
        pass

    # Exit a parse tree produced by DNPParser#communicationDescriptionEntryFormat3.
    def exitCommunicationDescriptionEntryFormat3(self, ctx:DNPParser.CommunicationDescriptionEntryFormat3Context):
        pass


    # Enter a parse tree produced by DNPParser#communicationDescriptionEntryFormat4.
    def enterCommunicationDescriptionEntryFormat4(self, ctx:DNPParser.CommunicationDescriptionEntryFormat4Context):
        pass

    # Exit a parse tree produced by DNPParser#communicationDescriptionEntryFormat4.
    def exitCommunicationDescriptionEntryFormat4(self, ctx:DNPParser.CommunicationDescriptionEntryFormat4Context):
        pass


    # Enter a parse tree produced by DNPParser#communicationAttribute.
    def enterCommunicationAttribute(self, ctx:DNPParser.CommunicationAttributeContext):
        pass

    # Exit a parse tree produced by DNPParser#communicationAttribute.
    def exitCommunicationAttribute(self, ctx:DNPParser.CommunicationAttributeContext):
        pass


    # Enter a parse tree produced by DNPParser#communicationIoHeader.
    def enterCommunicationIoHeader(self, ctx:DNPParser.CommunicationIoHeaderContext):
        pass

    # Exit a parse tree produced by DNPParser#communicationIoHeader.
    def exitCommunicationIoHeader(self, ctx:DNPParser.CommunicationIoHeaderContext):
        pass


    # Enter a parse tree produced by DNPParser#conversationClause.
    def enterConversationClause(self, ctx:DNPParser.ConversationClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#conversationClause.
    def exitConversationClause(self, ctx:DNPParser.ConversationClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#destinationCountClause.
    def enterDestinationCountClause(self, ctx:DNPParser.DestinationCountClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#destinationCountClause.
    def exitDestinationCountClause(self, ctx:DNPParser.DestinationCountClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#destinationTableClause.
    def enterDestinationTableClause(self, ctx:DNPParser.DestinationTableClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#destinationTableClause.
    def exitDestinationTableClause(self, ctx:DNPParser.DestinationTableClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#endKeyClause.
    def enterEndKeyClause(self, ctx:DNPParser.EndKeyClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#endKeyClause.
    def exitEndKeyClause(self, ctx:DNPParser.EndKeyClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#errorKeyClause.
    def enterErrorKeyClause(self, ctx:DNPParser.ErrorKeyClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#errorKeyClause.
    def exitErrorKeyClause(self, ctx:DNPParser.ErrorKeyClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#messageCountClause.
    def enterMessageCountClause(self, ctx:DNPParser.MessageCountClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#messageCountClause.
    def exitMessageCountClause(self, ctx:DNPParser.MessageCountClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#messageDateClause.
    def enterMessageDateClause(self, ctx:DNPParser.MessageDateClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#messageDateClause.
    def exitMessageDateClause(self, ctx:DNPParser.MessageDateClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#messageTimeClause.
    def enterMessageTimeClause(self, ctx:DNPParser.MessageTimeClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#messageTimeClause.
    def exitMessageTimeClause(self, ctx:DNPParser.MessageTimeClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#statusKeyClause.
    def enterStatusKeyClause(self, ctx:DNPParser.StatusKeyClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#statusKeyClause.
    def exitStatusKeyClause(self, ctx:DNPParser.StatusKeyClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#symbolicDestinationClause.
    def enterSymbolicDestinationClause(self, ctx:DNPParser.SymbolicDestinationClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#symbolicDestinationClause.
    def exitSymbolicDestinationClause(self, ctx:DNPParser.SymbolicDestinationClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#symbolicQueueClause.
    def enterSymbolicQueueClause(self, ctx:DNPParser.SymbolicQueueClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#symbolicQueueClause.
    def exitSymbolicQueueClause(self, ctx:DNPParser.SymbolicQueueClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#symbolicSourceClause.
    def enterSymbolicSourceClause(self, ctx:DNPParser.SymbolicSourceClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#symbolicSourceClause.
    def exitSymbolicSourceClause(self, ctx:DNPParser.SymbolicSourceClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#symbolicTerminalClause.
    def enterSymbolicTerminalClause(self, ctx:DNPParser.SymbolicTerminalClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#symbolicTerminalClause.
    def exitSymbolicTerminalClause(self, ctx:DNPParser.SymbolicTerminalClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#symbolicSubQueueClause.
    def enterSymbolicSubQueueClause(self, ctx:DNPParser.SymbolicSubQueueClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#symbolicSubQueueClause.
    def exitSymbolicSubQueueClause(self, ctx:DNPParser.SymbolicSubQueueClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#textLengthClause.
    def enterTextLengthClause(self, ctx:DNPParser.TextLengthClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#textLengthClause.
    def exitTextLengthClause(self, ctx:DNPParser.TextLengthClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#localStorageSection.
    def enterLocalStorageSection(self, ctx:DNPParser.LocalStorageSectionContext):
        pass

    # Exit a parse tree produced by DNPParser#localStorageSection.
    def exitLocalStorageSection(self, ctx:DNPParser.LocalStorageSectionContext):
        pass


    # Enter a parse tree produced by DNPParser#screenSection.
    def enterScreenSection(self, ctx:DNPParser.ScreenSectionContext):
        pass

    # Exit a parse tree produced by DNPParser#screenSection.
    def exitScreenSection(self, ctx:DNPParser.ScreenSectionContext):
        pass


    # Enter a parse tree produced by DNPParser#screenDescriptionEntry.
    def enterScreenDescriptionEntry(self, ctx:DNPParser.ScreenDescriptionEntryContext):
        pass

    # Exit a parse tree produced by DNPParser#screenDescriptionEntry.
    def exitScreenDescriptionEntry(self, ctx:DNPParser.ScreenDescriptionEntryContext):
        pass


    # Enter a parse tree produced by DNPParser#screenDescriptionBlankClause.
    def enterScreenDescriptionBlankClause(self, ctx:DNPParser.ScreenDescriptionBlankClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#screenDescriptionBlankClause.
    def exitScreenDescriptionBlankClause(self, ctx:DNPParser.ScreenDescriptionBlankClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#screenDescriptionBellClause.
    def enterScreenDescriptionBellClause(self, ctx:DNPParser.ScreenDescriptionBellClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#screenDescriptionBellClause.
    def exitScreenDescriptionBellClause(self, ctx:DNPParser.ScreenDescriptionBellClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#screenDescriptionBlinkClause.
    def enterScreenDescriptionBlinkClause(self, ctx:DNPParser.ScreenDescriptionBlinkClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#screenDescriptionBlinkClause.
    def exitScreenDescriptionBlinkClause(self, ctx:DNPParser.ScreenDescriptionBlinkClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#screenDescriptionEraseClause.
    def enterScreenDescriptionEraseClause(self, ctx:DNPParser.ScreenDescriptionEraseClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#screenDescriptionEraseClause.
    def exitScreenDescriptionEraseClause(self, ctx:DNPParser.ScreenDescriptionEraseClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#screenDescriptionLightClause.
    def enterScreenDescriptionLightClause(self, ctx:DNPParser.ScreenDescriptionLightClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#screenDescriptionLightClause.
    def exitScreenDescriptionLightClause(self, ctx:DNPParser.ScreenDescriptionLightClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#screenDescriptionGridClause.
    def enterScreenDescriptionGridClause(self, ctx:DNPParser.ScreenDescriptionGridClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#screenDescriptionGridClause.
    def exitScreenDescriptionGridClause(self, ctx:DNPParser.ScreenDescriptionGridClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#screenDescriptionReverseVideoClause.
    def enterScreenDescriptionReverseVideoClause(self, ctx:DNPParser.ScreenDescriptionReverseVideoClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#screenDescriptionReverseVideoClause.
    def exitScreenDescriptionReverseVideoClause(self, ctx:DNPParser.ScreenDescriptionReverseVideoClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#screenDescriptionUnderlineClause.
    def enterScreenDescriptionUnderlineClause(self, ctx:DNPParser.ScreenDescriptionUnderlineClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#screenDescriptionUnderlineClause.
    def exitScreenDescriptionUnderlineClause(self, ctx:DNPParser.ScreenDescriptionUnderlineClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#screenDescriptionSizeClause.
    def enterScreenDescriptionSizeClause(self, ctx:DNPParser.ScreenDescriptionSizeClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#screenDescriptionSizeClause.
    def exitScreenDescriptionSizeClause(self, ctx:DNPParser.ScreenDescriptionSizeClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#screenDescriptionLineClause.
    def enterScreenDescriptionLineClause(self, ctx:DNPParser.ScreenDescriptionLineClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#screenDescriptionLineClause.
    def exitScreenDescriptionLineClause(self, ctx:DNPParser.ScreenDescriptionLineClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#screenDescriptionColumnClause.
    def enterScreenDescriptionColumnClause(self, ctx:DNPParser.ScreenDescriptionColumnClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#screenDescriptionColumnClause.
    def exitScreenDescriptionColumnClause(self, ctx:DNPParser.ScreenDescriptionColumnClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#screenDescriptionForegroundColorClause.
    def enterScreenDescriptionForegroundColorClause(self, ctx:DNPParser.ScreenDescriptionForegroundColorClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#screenDescriptionForegroundColorClause.
    def exitScreenDescriptionForegroundColorClause(self, ctx:DNPParser.ScreenDescriptionForegroundColorClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#screenDescriptionBackgroundColorClause.
    def enterScreenDescriptionBackgroundColorClause(self, ctx:DNPParser.ScreenDescriptionBackgroundColorClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#screenDescriptionBackgroundColorClause.
    def exitScreenDescriptionBackgroundColorClause(self, ctx:DNPParser.ScreenDescriptionBackgroundColorClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#screenDescriptionControlClause.
    def enterScreenDescriptionControlClause(self, ctx:DNPParser.ScreenDescriptionControlClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#screenDescriptionControlClause.
    def exitScreenDescriptionControlClause(self, ctx:DNPParser.ScreenDescriptionControlClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#screenDescriptionValueClause.
    def enterScreenDescriptionValueClause(self, ctx:DNPParser.ScreenDescriptionValueClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#screenDescriptionValueClause.
    def exitScreenDescriptionValueClause(self, ctx:DNPParser.ScreenDescriptionValueClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#screenDescriptionPictureClause.
    def enterScreenDescriptionPictureClause(self, ctx:DNPParser.ScreenDescriptionPictureClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#screenDescriptionPictureClause.
    def exitScreenDescriptionPictureClause(self, ctx:DNPParser.ScreenDescriptionPictureClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#screenDescriptionFromClause.
    def enterScreenDescriptionFromClause(self, ctx:DNPParser.ScreenDescriptionFromClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#screenDescriptionFromClause.
    def exitScreenDescriptionFromClause(self, ctx:DNPParser.ScreenDescriptionFromClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#screenDescriptionToClause.
    def enterScreenDescriptionToClause(self, ctx:DNPParser.ScreenDescriptionToClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#screenDescriptionToClause.
    def exitScreenDescriptionToClause(self, ctx:DNPParser.ScreenDescriptionToClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#screenDescriptionUsingClause.
    def enterScreenDescriptionUsingClause(self, ctx:DNPParser.ScreenDescriptionUsingClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#screenDescriptionUsingClause.
    def exitScreenDescriptionUsingClause(self, ctx:DNPParser.ScreenDescriptionUsingClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#screenDescriptionUsageClause.
    def enterScreenDescriptionUsageClause(self, ctx:DNPParser.ScreenDescriptionUsageClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#screenDescriptionUsageClause.
    def exitScreenDescriptionUsageClause(self, ctx:DNPParser.ScreenDescriptionUsageClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#screenDescriptionBlankWhenZeroClause.
    def enterScreenDescriptionBlankWhenZeroClause(self, ctx:DNPParser.ScreenDescriptionBlankWhenZeroClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#screenDescriptionBlankWhenZeroClause.
    def exitScreenDescriptionBlankWhenZeroClause(self, ctx:DNPParser.ScreenDescriptionBlankWhenZeroClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#screenDescriptionJustifiedClause.
    def enterScreenDescriptionJustifiedClause(self, ctx:DNPParser.ScreenDescriptionJustifiedClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#screenDescriptionJustifiedClause.
    def exitScreenDescriptionJustifiedClause(self, ctx:DNPParser.ScreenDescriptionJustifiedClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#screenDescriptionSignClause.
    def enterScreenDescriptionSignClause(self, ctx:DNPParser.ScreenDescriptionSignClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#screenDescriptionSignClause.
    def exitScreenDescriptionSignClause(self, ctx:DNPParser.ScreenDescriptionSignClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#screenDescriptionAutoClause.
    def enterScreenDescriptionAutoClause(self, ctx:DNPParser.ScreenDescriptionAutoClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#screenDescriptionAutoClause.
    def exitScreenDescriptionAutoClause(self, ctx:DNPParser.ScreenDescriptionAutoClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#screenDescriptionSecureClause.
    def enterScreenDescriptionSecureClause(self, ctx:DNPParser.ScreenDescriptionSecureClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#screenDescriptionSecureClause.
    def exitScreenDescriptionSecureClause(self, ctx:DNPParser.ScreenDescriptionSecureClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#screenDescriptionRequiredClause.
    def enterScreenDescriptionRequiredClause(self, ctx:DNPParser.ScreenDescriptionRequiredClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#screenDescriptionRequiredClause.
    def exitScreenDescriptionRequiredClause(self, ctx:DNPParser.ScreenDescriptionRequiredClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#screenDescriptionPromptClause.
    def enterScreenDescriptionPromptClause(self, ctx:DNPParser.ScreenDescriptionPromptClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#screenDescriptionPromptClause.
    def exitScreenDescriptionPromptClause(self, ctx:DNPParser.ScreenDescriptionPromptClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#screenDescriptionPromptOccursClause.
    def enterScreenDescriptionPromptOccursClause(self, ctx:DNPParser.ScreenDescriptionPromptOccursClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#screenDescriptionPromptOccursClause.
    def exitScreenDescriptionPromptOccursClause(self, ctx:DNPParser.ScreenDescriptionPromptOccursClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#screenDescriptionFullClause.
    def enterScreenDescriptionFullClause(self, ctx:DNPParser.ScreenDescriptionFullClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#screenDescriptionFullClause.
    def exitScreenDescriptionFullClause(self, ctx:DNPParser.ScreenDescriptionFullClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#screenDescriptionZeroFillClause.
    def enterScreenDescriptionZeroFillClause(self, ctx:DNPParser.ScreenDescriptionZeroFillClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#screenDescriptionZeroFillClause.
    def exitScreenDescriptionZeroFillClause(self, ctx:DNPParser.ScreenDescriptionZeroFillClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#reportSection.
    def enterReportSection(self, ctx:DNPParser.ReportSectionContext):
        pass

    # Exit a parse tree produced by DNPParser#reportSection.
    def exitReportSection(self, ctx:DNPParser.ReportSectionContext):
        pass


    # Enter a parse tree produced by DNPParser#reportDescription.
    def enterReportDescription(self, ctx:DNPParser.ReportDescriptionContext):
        pass

    # Exit a parse tree produced by DNPParser#reportDescription.
    def exitReportDescription(self, ctx:DNPParser.ReportDescriptionContext):
        pass


    # Enter a parse tree produced by DNPParser#reportDescriptionEntry.
    def enterReportDescriptionEntry(self, ctx:DNPParser.ReportDescriptionEntryContext):
        pass

    # Exit a parse tree produced by DNPParser#reportDescriptionEntry.
    def exitReportDescriptionEntry(self, ctx:DNPParser.ReportDescriptionEntryContext):
        pass


    # Enter a parse tree produced by DNPParser#reportDescriptionGlobalClause.
    def enterReportDescriptionGlobalClause(self, ctx:DNPParser.ReportDescriptionGlobalClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#reportDescriptionGlobalClause.
    def exitReportDescriptionGlobalClause(self, ctx:DNPParser.ReportDescriptionGlobalClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#reportDescriptionPageLimitClause.
    def enterReportDescriptionPageLimitClause(self, ctx:DNPParser.ReportDescriptionPageLimitClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#reportDescriptionPageLimitClause.
    def exitReportDescriptionPageLimitClause(self, ctx:DNPParser.ReportDescriptionPageLimitClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#reportDescriptionHeadingClause.
    def enterReportDescriptionHeadingClause(self, ctx:DNPParser.ReportDescriptionHeadingClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#reportDescriptionHeadingClause.
    def exitReportDescriptionHeadingClause(self, ctx:DNPParser.ReportDescriptionHeadingClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#reportDescriptionFirstDetailClause.
    def enterReportDescriptionFirstDetailClause(self, ctx:DNPParser.ReportDescriptionFirstDetailClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#reportDescriptionFirstDetailClause.
    def exitReportDescriptionFirstDetailClause(self, ctx:DNPParser.ReportDescriptionFirstDetailClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#reportDescriptionLastDetailClause.
    def enterReportDescriptionLastDetailClause(self, ctx:DNPParser.ReportDescriptionLastDetailClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#reportDescriptionLastDetailClause.
    def exitReportDescriptionLastDetailClause(self, ctx:DNPParser.ReportDescriptionLastDetailClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#reportDescriptionFootingClause.
    def enterReportDescriptionFootingClause(self, ctx:DNPParser.ReportDescriptionFootingClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#reportDescriptionFootingClause.
    def exitReportDescriptionFootingClause(self, ctx:DNPParser.ReportDescriptionFootingClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#reportGroupDescriptionEntry.
    def enterReportGroupDescriptionEntry(self, ctx:DNPParser.ReportGroupDescriptionEntryContext):
        pass

    # Exit a parse tree produced by DNPParser#reportGroupDescriptionEntry.
    def exitReportGroupDescriptionEntry(self, ctx:DNPParser.ReportGroupDescriptionEntryContext):
        pass


    # Enter a parse tree produced by DNPParser#reportGroupDescriptionEntryFormat1.
    def enterReportGroupDescriptionEntryFormat1(self, ctx:DNPParser.ReportGroupDescriptionEntryFormat1Context):
        pass

    # Exit a parse tree produced by DNPParser#reportGroupDescriptionEntryFormat1.
    def exitReportGroupDescriptionEntryFormat1(self, ctx:DNPParser.ReportGroupDescriptionEntryFormat1Context):
        pass


    # Enter a parse tree produced by DNPParser#reportGroupDescriptionEntryFormat2.
    def enterReportGroupDescriptionEntryFormat2(self, ctx:DNPParser.ReportGroupDescriptionEntryFormat2Context):
        pass

    # Exit a parse tree produced by DNPParser#reportGroupDescriptionEntryFormat2.
    def exitReportGroupDescriptionEntryFormat2(self, ctx:DNPParser.ReportGroupDescriptionEntryFormat2Context):
        pass


    # Enter a parse tree produced by DNPParser#reportGroupDescriptionEntryFormat3.
    def enterReportGroupDescriptionEntryFormat3(self, ctx:DNPParser.ReportGroupDescriptionEntryFormat3Context):
        pass

    # Exit a parse tree produced by DNPParser#reportGroupDescriptionEntryFormat3.
    def exitReportGroupDescriptionEntryFormat3(self, ctx:DNPParser.ReportGroupDescriptionEntryFormat3Context):
        pass


    # Enter a parse tree produced by DNPParser#reportGroupBlankWhenZeroClause.
    def enterReportGroupBlankWhenZeroClause(self, ctx:DNPParser.ReportGroupBlankWhenZeroClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#reportGroupBlankWhenZeroClause.
    def exitReportGroupBlankWhenZeroClause(self, ctx:DNPParser.ReportGroupBlankWhenZeroClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#reportGroupColumnNumberClause.
    def enterReportGroupColumnNumberClause(self, ctx:DNPParser.ReportGroupColumnNumberClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#reportGroupColumnNumberClause.
    def exitReportGroupColumnNumberClause(self, ctx:DNPParser.ReportGroupColumnNumberClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#reportGroupIndicateClause.
    def enterReportGroupIndicateClause(self, ctx:DNPParser.ReportGroupIndicateClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#reportGroupIndicateClause.
    def exitReportGroupIndicateClause(self, ctx:DNPParser.ReportGroupIndicateClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#reportGroupJustifiedClause.
    def enterReportGroupJustifiedClause(self, ctx:DNPParser.ReportGroupJustifiedClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#reportGroupJustifiedClause.
    def exitReportGroupJustifiedClause(self, ctx:DNPParser.ReportGroupJustifiedClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#reportGroupLineNumberClause.
    def enterReportGroupLineNumberClause(self, ctx:DNPParser.ReportGroupLineNumberClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#reportGroupLineNumberClause.
    def exitReportGroupLineNumberClause(self, ctx:DNPParser.ReportGroupLineNumberClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#reportGroupLineNumberNextPage.
    def enterReportGroupLineNumberNextPage(self, ctx:DNPParser.ReportGroupLineNumberNextPageContext):
        pass

    # Exit a parse tree produced by DNPParser#reportGroupLineNumberNextPage.
    def exitReportGroupLineNumberNextPage(self, ctx:DNPParser.ReportGroupLineNumberNextPageContext):
        pass


    # Enter a parse tree produced by DNPParser#reportGroupLineNumberPlus.
    def enterReportGroupLineNumberPlus(self, ctx:DNPParser.ReportGroupLineNumberPlusContext):
        pass

    # Exit a parse tree produced by DNPParser#reportGroupLineNumberPlus.
    def exitReportGroupLineNumberPlus(self, ctx:DNPParser.ReportGroupLineNumberPlusContext):
        pass


    # Enter a parse tree produced by DNPParser#reportGroupNextGroupClause.
    def enterReportGroupNextGroupClause(self, ctx:DNPParser.ReportGroupNextGroupClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#reportGroupNextGroupClause.
    def exitReportGroupNextGroupClause(self, ctx:DNPParser.ReportGroupNextGroupClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#reportGroupNextGroupPlus.
    def enterReportGroupNextGroupPlus(self, ctx:DNPParser.ReportGroupNextGroupPlusContext):
        pass

    # Exit a parse tree produced by DNPParser#reportGroupNextGroupPlus.
    def exitReportGroupNextGroupPlus(self, ctx:DNPParser.ReportGroupNextGroupPlusContext):
        pass


    # Enter a parse tree produced by DNPParser#reportGroupNextGroupNextPage.
    def enterReportGroupNextGroupNextPage(self, ctx:DNPParser.ReportGroupNextGroupNextPageContext):
        pass

    # Exit a parse tree produced by DNPParser#reportGroupNextGroupNextPage.
    def exitReportGroupNextGroupNextPage(self, ctx:DNPParser.ReportGroupNextGroupNextPageContext):
        pass


    # Enter a parse tree produced by DNPParser#reportGroupPictureClause.
    def enterReportGroupPictureClause(self, ctx:DNPParser.ReportGroupPictureClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#reportGroupPictureClause.
    def exitReportGroupPictureClause(self, ctx:DNPParser.ReportGroupPictureClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#reportGroupResetClause.
    def enterReportGroupResetClause(self, ctx:DNPParser.ReportGroupResetClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#reportGroupResetClause.
    def exitReportGroupResetClause(self, ctx:DNPParser.ReportGroupResetClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#reportGroupSignClause.
    def enterReportGroupSignClause(self, ctx:DNPParser.ReportGroupSignClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#reportGroupSignClause.
    def exitReportGroupSignClause(self, ctx:DNPParser.ReportGroupSignClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#reportGroupSourceClause.
    def enterReportGroupSourceClause(self, ctx:DNPParser.ReportGroupSourceClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#reportGroupSourceClause.
    def exitReportGroupSourceClause(self, ctx:DNPParser.ReportGroupSourceClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#reportGroupSumClause.
    def enterReportGroupSumClause(self, ctx:DNPParser.ReportGroupSumClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#reportGroupSumClause.
    def exitReportGroupSumClause(self, ctx:DNPParser.ReportGroupSumClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#reportGroupTypeClause.
    def enterReportGroupTypeClause(self, ctx:DNPParser.ReportGroupTypeClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#reportGroupTypeClause.
    def exitReportGroupTypeClause(self, ctx:DNPParser.ReportGroupTypeClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#reportGroupTypeReportHeading.
    def enterReportGroupTypeReportHeading(self, ctx:DNPParser.ReportGroupTypeReportHeadingContext):
        pass

    # Exit a parse tree produced by DNPParser#reportGroupTypeReportHeading.
    def exitReportGroupTypeReportHeading(self, ctx:DNPParser.ReportGroupTypeReportHeadingContext):
        pass


    # Enter a parse tree produced by DNPParser#reportGroupTypePageHeading.
    def enterReportGroupTypePageHeading(self, ctx:DNPParser.ReportGroupTypePageHeadingContext):
        pass

    # Exit a parse tree produced by DNPParser#reportGroupTypePageHeading.
    def exitReportGroupTypePageHeading(self, ctx:DNPParser.ReportGroupTypePageHeadingContext):
        pass


    # Enter a parse tree produced by DNPParser#reportGroupTypeControlHeading.
    def enterReportGroupTypeControlHeading(self, ctx:DNPParser.ReportGroupTypeControlHeadingContext):
        pass

    # Exit a parse tree produced by DNPParser#reportGroupTypeControlHeading.
    def exitReportGroupTypeControlHeading(self, ctx:DNPParser.ReportGroupTypeControlHeadingContext):
        pass


    # Enter a parse tree produced by DNPParser#reportGroupTypeDetail.
    def enterReportGroupTypeDetail(self, ctx:DNPParser.ReportGroupTypeDetailContext):
        pass

    # Exit a parse tree produced by DNPParser#reportGroupTypeDetail.
    def exitReportGroupTypeDetail(self, ctx:DNPParser.ReportGroupTypeDetailContext):
        pass


    # Enter a parse tree produced by DNPParser#reportGroupTypeControlFooting.
    def enterReportGroupTypeControlFooting(self, ctx:DNPParser.ReportGroupTypeControlFootingContext):
        pass

    # Exit a parse tree produced by DNPParser#reportGroupTypeControlFooting.
    def exitReportGroupTypeControlFooting(self, ctx:DNPParser.ReportGroupTypeControlFootingContext):
        pass


    # Enter a parse tree produced by DNPParser#reportGroupUsageClause.
    def enterReportGroupUsageClause(self, ctx:DNPParser.ReportGroupUsageClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#reportGroupUsageClause.
    def exitReportGroupUsageClause(self, ctx:DNPParser.ReportGroupUsageClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#reportGroupTypePageFooting.
    def enterReportGroupTypePageFooting(self, ctx:DNPParser.ReportGroupTypePageFootingContext):
        pass

    # Exit a parse tree produced by DNPParser#reportGroupTypePageFooting.
    def exitReportGroupTypePageFooting(self, ctx:DNPParser.ReportGroupTypePageFootingContext):
        pass


    # Enter a parse tree produced by DNPParser#reportGroupTypeReportFooting.
    def enterReportGroupTypeReportFooting(self, ctx:DNPParser.ReportGroupTypeReportFootingContext):
        pass

    # Exit a parse tree produced by DNPParser#reportGroupTypeReportFooting.
    def exitReportGroupTypeReportFooting(self, ctx:DNPParser.ReportGroupTypeReportFootingContext):
        pass


    # Enter a parse tree produced by DNPParser#reportGroupValueClause.
    def enterReportGroupValueClause(self, ctx:DNPParser.ReportGroupValueClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#reportGroupValueClause.
    def exitReportGroupValueClause(self, ctx:DNPParser.ReportGroupValueClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#programLibrarySection.
    def enterProgramLibrarySection(self, ctx:DNPParser.ProgramLibrarySectionContext):
        pass

    # Exit a parse tree produced by DNPParser#programLibrarySection.
    def exitProgramLibrarySection(self, ctx:DNPParser.ProgramLibrarySectionContext):
        pass


    # Enter a parse tree produced by DNPParser#libraryDescriptionEntry.
    def enterLibraryDescriptionEntry(self, ctx:DNPParser.LibraryDescriptionEntryContext):
        pass

    # Exit a parse tree produced by DNPParser#libraryDescriptionEntry.
    def exitLibraryDescriptionEntry(self, ctx:DNPParser.LibraryDescriptionEntryContext):
        pass


    # Enter a parse tree produced by DNPParser#libraryDescriptionEntryFormat1.
    def enterLibraryDescriptionEntryFormat1(self, ctx:DNPParser.LibraryDescriptionEntryFormat1Context):
        pass

    # Exit a parse tree produced by DNPParser#libraryDescriptionEntryFormat1.
    def exitLibraryDescriptionEntryFormat1(self, ctx:DNPParser.LibraryDescriptionEntryFormat1Context):
        pass


    # Enter a parse tree produced by DNPParser#libraryDescriptionEntryFormat2.
    def enterLibraryDescriptionEntryFormat2(self, ctx:DNPParser.LibraryDescriptionEntryFormat2Context):
        pass

    # Exit a parse tree produced by DNPParser#libraryDescriptionEntryFormat2.
    def exitLibraryDescriptionEntryFormat2(self, ctx:DNPParser.LibraryDescriptionEntryFormat2Context):
        pass


    # Enter a parse tree produced by DNPParser#libraryAttributeClauseFormat1.
    def enterLibraryAttributeClauseFormat1(self, ctx:DNPParser.LibraryAttributeClauseFormat1Context):
        pass

    # Exit a parse tree produced by DNPParser#libraryAttributeClauseFormat1.
    def exitLibraryAttributeClauseFormat1(self, ctx:DNPParser.LibraryAttributeClauseFormat1Context):
        pass


    # Enter a parse tree produced by DNPParser#libraryAttributeClauseFormat2.
    def enterLibraryAttributeClauseFormat2(self, ctx:DNPParser.LibraryAttributeClauseFormat2Context):
        pass

    # Exit a parse tree produced by DNPParser#libraryAttributeClauseFormat2.
    def exitLibraryAttributeClauseFormat2(self, ctx:DNPParser.LibraryAttributeClauseFormat2Context):
        pass


    # Enter a parse tree produced by DNPParser#libraryAttributeFunction.
    def enterLibraryAttributeFunction(self, ctx:DNPParser.LibraryAttributeFunctionContext):
        pass

    # Exit a parse tree produced by DNPParser#libraryAttributeFunction.
    def exitLibraryAttributeFunction(self, ctx:DNPParser.LibraryAttributeFunctionContext):
        pass


    # Enter a parse tree produced by DNPParser#libraryAttributeParameter.
    def enterLibraryAttributeParameter(self, ctx:DNPParser.LibraryAttributeParameterContext):
        pass

    # Exit a parse tree produced by DNPParser#libraryAttributeParameter.
    def exitLibraryAttributeParameter(self, ctx:DNPParser.LibraryAttributeParameterContext):
        pass


    # Enter a parse tree produced by DNPParser#libraryAttributeTitle.
    def enterLibraryAttributeTitle(self, ctx:DNPParser.LibraryAttributeTitleContext):
        pass

    # Exit a parse tree produced by DNPParser#libraryAttributeTitle.
    def exitLibraryAttributeTitle(self, ctx:DNPParser.LibraryAttributeTitleContext):
        pass


    # Enter a parse tree produced by DNPParser#libraryEntryProcedureClauseFormat1.
    def enterLibraryEntryProcedureClauseFormat1(self, ctx:DNPParser.LibraryEntryProcedureClauseFormat1Context):
        pass

    # Exit a parse tree produced by DNPParser#libraryEntryProcedureClauseFormat1.
    def exitLibraryEntryProcedureClauseFormat1(self, ctx:DNPParser.LibraryEntryProcedureClauseFormat1Context):
        pass


    # Enter a parse tree produced by DNPParser#libraryEntryProcedureClauseFormat2.
    def enterLibraryEntryProcedureClauseFormat2(self, ctx:DNPParser.LibraryEntryProcedureClauseFormat2Context):
        pass

    # Exit a parse tree produced by DNPParser#libraryEntryProcedureClauseFormat2.
    def exitLibraryEntryProcedureClauseFormat2(self, ctx:DNPParser.LibraryEntryProcedureClauseFormat2Context):
        pass


    # Enter a parse tree produced by DNPParser#libraryEntryProcedureForClause.
    def enterLibraryEntryProcedureForClause(self, ctx:DNPParser.LibraryEntryProcedureForClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#libraryEntryProcedureForClause.
    def exitLibraryEntryProcedureForClause(self, ctx:DNPParser.LibraryEntryProcedureForClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#libraryEntryProcedureGivingClause.
    def enterLibraryEntryProcedureGivingClause(self, ctx:DNPParser.LibraryEntryProcedureGivingClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#libraryEntryProcedureGivingClause.
    def exitLibraryEntryProcedureGivingClause(self, ctx:DNPParser.LibraryEntryProcedureGivingClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#libraryEntryProcedureUsingClause.
    def enterLibraryEntryProcedureUsingClause(self, ctx:DNPParser.LibraryEntryProcedureUsingClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#libraryEntryProcedureUsingClause.
    def exitLibraryEntryProcedureUsingClause(self, ctx:DNPParser.LibraryEntryProcedureUsingClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#libraryEntryProcedureUsingName.
    def enterLibraryEntryProcedureUsingName(self, ctx:DNPParser.LibraryEntryProcedureUsingNameContext):
        pass

    # Exit a parse tree produced by DNPParser#libraryEntryProcedureUsingName.
    def exitLibraryEntryProcedureUsingName(self, ctx:DNPParser.LibraryEntryProcedureUsingNameContext):
        pass


    # Enter a parse tree produced by DNPParser#libraryEntryProcedureWithClause.
    def enterLibraryEntryProcedureWithClause(self, ctx:DNPParser.LibraryEntryProcedureWithClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#libraryEntryProcedureWithClause.
    def exitLibraryEntryProcedureWithClause(self, ctx:DNPParser.LibraryEntryProcedureWithClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#libraryEntryProcedureWithName.
    def enterLibraryEntryProcedureWithName(self, ctx:DNPParser.LibraryEntryProcedureWithNameContext):
        pass

    # Exit a parse tree produced by DNPParser#libraryEntryProcedureWithName.
    def exitLibraryEntryProcedureWithName(self, ctx:DNPParser.LibraryEntryProcedureWithNameContext):
        pass


    # Enter a parse tree produced by DNPParser#libraryIsCommonClause.
    def enterLibraryIsCommonClause(self, ctx:DNPParser.LibraryIsCommonClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#libraryIsCommonClause.
    def exitLibraryIsCommonClause(self, ctx:DNPParser.LibraryIsCommonClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#libraryIsGlobalClause.
    def enterLibraryIsGlobalClause(self, ctx:DNPParser.LibraryIsGlobalClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#libraryIsGlobalClause.
    def exitLibraryIsGlobalClause(self, ctx:DNPParser.LibraryIsGlobalClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#dataDescriptionEntry.
    def enterDataDescriptionEntry(self, ctx:DNPParser.DataDescriptionEntryContext):
        pass

    # Exit a parse tree produced by DNPParser#dataDescriptionEntry.
    def exitDataDescriptionEntry(self, ctx:DNPParser.DataDescriptionEntryContext):
        pass


    # Enter a parse tree produced by DNPParser#copyStatement.
    def enterCopyStatement(self, ctx:DNPParser.CopyStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#copyStatement.
    def exitCopyStatement(self, ctx:DNPParser.CopyStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#copySource.
    def enterCopySource(self, ctx:DNPParser.CopySourceContext):
        pass

    # Exit a parse tree produced by DNPParser#copySource.
    def exitCopySource(self, ctx:DNPParser.CopySourceContext):
        pass


    # Enter a parse tree produced by DNPParser#copyLibrary.
    def enterCopyLibrary(self, ctx:DNPParser.CopyLibraryContext):
        pass

    # Exit a parse tree produced by DNPParser#copyLibrary.
    def exitCopyLibrary(self, ctx:DNPParser.CopyLibraryContext):
        pass


    # Enter a parse tree produced by DNPParser#replacingPhrase.
    def enterReplacingPhrase(self, ctx:DNPParser.ReplacingPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#replacingPhrase.
    def exitReplacingPhrase(self, ctx:DNPParser.ReplacingPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#changeStatement.
    def enterChangeStatement(self, ctx:DNPParser.ChangeStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#changeStatement.
    def exitChangeStatement(self, ctx:DNPParser.ChangeStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#changeFileAttribute.
    def enterChangeFileAttribute(self, ctx:DNPParser.ChangeFileAttributeContext):
        pass

    # Exit a parse tree produced by DNPParser#changeFileAttribute.
    def exitChangeFileAttribute(self, ctx:DNPParser.ChangeFileAttributeContext):
        pass


    # Enter a parse tree produced by DNPParser#changeLibraryAttribute.
    def enterChangeLibraryAttribute(self, ctx:DNPParser.ChangeLibraryAttributeContext):
        pass

    # Exit a parse tree produced by DNPParser#changeLibraryAttribute.
    def exitChangeLibraryAttribute(self, ctx:DNPParser.ChangeLibraryAttributeContext):
        pass


    # Enter a parse tree produced by DNPParser#libraryAttributeName.
    def enterLibraryAttributeName(self, ctx:DNPParser.LibraryAttributeNameContext):
        pass

    # Exit a parse tree produced by DNPParser#libraryAttributeName.
    def exitLibraryAttributeName(self, ctx:DNPParser.LibraryAttributeNameContext):
        pass


    # Enter a parse tree produced by DNPParser#libraryValueOption.
    def enterLibraryValueOption(self, ctx:DNPParser.LibraryValueOptionContext):
        pass

    # Exit a parse tree produced by DNPParser#libraryValueOption.
    def exitLibraryValueOption(self, ctx:DNPParser.LibraryValueOptionContext):
        pass


    # Enter a parse tree produced by DNPParser#toValueOption.
    def enterToValueOption(self, ctx:DNPParser.ToValueOptionContext):
        pass

    # Exit a parse tree produced by DNPParser#toValueOption.
    def exitToValueOption(self, ctx:DNPParser.ToValueOptionContext):
        pass


    # Enter a parse tree produced by DNPParser#createStatement.
    def enterCreateStatement(self, ctx:DNPParser.CreateStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#createStatement.
    def exitCreateStatement(self, ctx:DNPParser.CreateStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#replaceOffStatement.
    def enterReplaceOffStatement(self, ctx:DNPParser.ReplaceOffStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#replaceOffStatement.
    def exitReplaceOffStatement(self, ctx:DNPParser.ReplaceOffStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#replaceClause.
    def enterReplaceClause(self, ctx:DNPParser.ReplaceClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#replaceClause.
    def exitReplaceClause(self, ctx:DNPParser.ReplaceClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#directoryPhrase.
    def enterDirectoryPhrase(self, ctx:DNPParser.DirectoryPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#directoryPhrase.
    def exitDirectoryPhrase(self, ctx:DNPParser.DirectoryPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#familyPhrase.
    def enterFamilyPhrase(self, ctx:DNPParser.FamilyPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#familyPhrase.
    def exitFamilyPhrase(self, ctx:DNPParser.FamilyPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#replaceable.
    def enterReplaceable(self, ctx:DNPParser.ReplaceableContext):
        pass

    # Exit a parse tree produced by DNPParser#replaceable.
    def exitReplaceable(self, ctx:DNPParser.ReplaceableContext):
        pass


    # Enter a parse tree produced by DNPParser#replacement.
    def enterReplacement(self, ctx:DNPParser.ReplacementContext):
        pass

    # Exit a parse tree produced by DNPParser#replacement.
    def exitReplacement(self, ctx:DNPParser.ReplacementContext):
        pass


    # Enter a parse tree produced by DNPParser#ejectStatement.
    def enterEjectStatement(self, ctx:DNPParser.EjectStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#ejectStatement.
    def exitEjectStatement(self, ctx:DNPParser.EjectStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#skipStatement.
    def enterSkipStatement(self, ctx:DNPParser.SkipStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#skipStatement.
    def exitSkipStatement(self, ctx:DNPParser.SkipStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#titleStatement.
    def enterTitleStatement(self, ctx:DNPParser.TitleStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#titleStatement.
    def exitTitleStatement(self, ctx:DNPParser.TitleStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#pseudoText.
    def enterPseudoText(self, ctx:DNPParser.PseudoTextContext):
        pass

    # Exit a parse tree produced by DNPParser#pseudoText.
    def exitPseudoText(self, ctx:DNPParser.PseudoTextContext):
        pass


    # Enter a parse tree produced by DNPParser#charData.
    def enterCharData(self, ctx:DNPParser.CharDataContext):
        pass

    # Exit a parse tree produced by DNPParser#charData.
    def exitCharData(self, ctx:DNPParser.CharDataContext):
        pass


    # Enter a parse tree produced by DNPParser#charDataSql.
    def enterCharDataSql(self, ctx:DNPParser.CharDataSqlContext):
        pass

    # Exit a parse tree produced by DNPParser#charDataSql.
    def exitCharDataSql(self, ctx:DNPParser.CharDataSqlContext):
        pass


    # Enter a parse tree produced by DNPParser#charDataLine.
    def enterCharDataLine(self, ctx:DNPParser.CharDataLineContext):
        pass

    # Exit a parse tree produced by DNPParser#charDataLine.
    def exitCharDataLine(self, ctx:DNPParser.CharDataLineContext):
        pass


    # Enter a parse tree produced by DNPParser#cobolWord.
    def enterCobolWord(self, ctx:DNPParser.CobolWordContext):
        pass

    # Exit a parse tree produced by DNPParser#cobolWord.
    def exitCobolWord(self, ctx:DNPParser.CobolWordContext):
        pass


    # Enter a parse tree produced by DNPParser#literal.
    def enterLiteral(self, ctx:DNPParser.LiteralContext):
        pass

    # Exit a parse tree produced by DNPParser#literal.
    def exitLiteral(self, ctx:DNPParser.LiteralContext):
        pass


    # Enter a parse tree produced by DNPParser#jpEncodingText.
    def enterJpEncodingText(self, ctx:DNPParser.JpEncodingTextContext):
        pass

    # Exit a parse tree produced by DNPParser#jpEncodingText.
    def exitJpEncodingText(self, ctx:DNPParser.JpEncodingTextContext):
        pass


    # Enter a parse tree produced by DNPParser#filename.
    def enterFilename(self, ctx:DNPParser.FilenameContext):
        pass

    # Exit a parse tree produced by DNPParser#filename.
    def exitFilename(self, ctx:DNPParser.FilenameContext):
        pass


    # Enter a parse tree produced by DNPParser#dataDescriptionEntryFormat1.
    def enterDataDescriptionEntryFormat1(self, ctx:DNPParser.DataDescriptionEntryFormat1Context):
        pass

    # Exit a parse tree produced by DNPParser#dataDescriptionEntryFormat1.
    def exitDataDescriptionEntryFormat1(self, ctx:DNPParser.DataDescriptionEntryFormat1Context):
        pass


    # Enter a parse tree produced by DNPParser#dataDescriptionEntryFormat2.
    def enterDataDescriptionEntryFormat2(self, ctx:DNPParser.DataDescriptionEntryFormat2Context):
        pass

    # Exit a parse tree produced by DNPParser#dataDescriptionEntryFormat2.
    def exitDataDescriptionEntryFormat2(self, ctx:DNPParser.DataDescriptionEntryFormat2Context):
        pass


    # Enter a parse tree produced by DNPParser#dataDescriptionEntryFormat3.
    def enterDataDescriptionEntryFormat3(self, ctx:DNPParser.DataDescriptionEntryFormat3Context):
        pass

    # Exit a parse tree produced by DNPParser#dataDescriptionEntryFormat3.
    def exitDataDescriptionEntryFormat3(self, ctx:DNPParser.DataDescriptionEntryFormat3Context):
        pass


    # Enter a parse tree produced by DNPParser#dataDescriptionEntryExecSql.
    def enterDataDescriptionEntryExecSql(self, ctx:DNPParser.DataDescriptionEntryExecSqlContext):
        pass

    # Exit a parse tree produced by DNPParser#dataDescriptionEntryExecSql.
    def exitDataDescriptionEntryExecSql(self, ctx:DNPParser.DataDescriptionEntryExecSqlContext):
        pass


    # Enter a parse tree produced by DNPParser#dataAlignedClause.
    def enterDataAlignedClause(self, ctx:DNPParser.DataAlignedClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#dataAlignedClause.
    def exitDataAlignedClause(self, ctx:DNPParser.DataAlignedClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#dataBlankWhenZeroClause.
    def enterDataBlankWhenZeroClause(self, ctx:DNPParser.DataBlankWhenZeroClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#dataBlankWhenZeroClause.
    def exitDataBlankWhenZeroClause(self, ctx:DNPParser.DataBlankWhenZeroClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#dataCommonOwnLocalClause.
    def enterDataCommonOwnLocalClause(self, ctx:DNPParser.DataCommonOwnLocalClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#dataCommonOwnLocalClause.
    def exitDataCommonOwnLocalClause(self, ctx:DNPParser.DataCommonOwnLocalClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#dataExternalClause.
    def enterDataExternalClause(self, ctx:DNPParser.DataExternalClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#dataExternalClause.
    def exitDataExternalClause(self, ctx:DNPParser.DataExternalClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#dataGlobalClause.
    def enterDataGlobalClause(self, ctx:DNPParser.DataGlobalClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#dataGlobalClause.
    def exitDataGlobalClause(self, ctx:DNPParser.DataGlobalClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#dataIntegerStringClause.
    def enterDataIntegerStringClause(self, ctx:DNPParser.DataIntegerStringClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#dataIntegerStringClause.
    def exitDataIntegerStringClause(self, ctx:DNPParser.DataIntegerStringClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#dataJustifiedClause.
    def enterDataJustifiedClause(self, ctx:DNPParser.DataJustifiedClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#dataJustifiedClause.
    def exitDataJustifiedClause(self, ctx:DNPParser.DataJustifiedClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#dataOccursClause.
    def enterDataOccursClause(self, ctx:DNPParser.DataOccursClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#dataOccursClause.
    def exitDataOccursClause(self, ctx:DNPParser.DataOccursClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#dataOccursTo.
    def enterDataOccursTo(self, ctx:DNPParser.DataOccursToContext):
        pass

    # Exit a parse tree produced by DNPParser#dataOccursTo.
    def exitDataOccursTo(self, ctx:DNPParser.DataOccursToContext):
        pass


    # Enter a parse tree produced by DNPParser#dataOccursSort.
    def enterDataOccursSort(self, ctx:DNPParser.DataOccursSortContext):
        pass

    # Exit a parse tree produced by DNPParser#dataOccursSort.
    def exitDataOccursSort(self, ctx:DNPParser.DataOccursSortContext):
        pass


    # Enter a parse tree produced by DNPParser#dataPictureClause.
    def enterDataPictureClause(self, ctx:DNPParser.DataPictureClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#dataPictureClause.
    def exitDataPictureClause(self, ctx:DNPParser.DataPictureClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#pictureString.
    def enterPictureString(self, ctx:DNPParser.PictureStringContext):
        pass

    # Exit a parse tree produced by DNPParser#pictureString.
    def exitPictureString(self, ctx:DNPParser.PictureStringContext):
        pass


    # Enter a parse tree produced by DNPParser#pictureChars.
    def enterPictureChars(self, ctx:DNPParser.PictureCharsContext):
        pass

    # Exit a parse tree produced by DNPParser#pictureChars.
    def exitPictureChars(self, ctx:DNPParser.PictureCharsContext):
        pass


    # Enter a parse tree produced by DNPParser#pictureCardinality.
    def enterPictureCardinality(self, ctx:DNPParser.PictureCardinalityContext):
        pass

    # Exit a parse tree produced by DNPParser#pictureCardinality.
    def exitPictureCardinality(self, ctx:DNPParser.PictureCardinalityContext):
        pass


    # Enter a parse tree produced by DNPParser#dataReceivedByClause.
    def enterDataReceivedByClause(self, ctx:DNPParser.DataReceivedByClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#dataReceivedByClause.
    def exitDataReceivedByClause(self, ctx:DNPParser.DataReceivedByClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#dataRecordAreaClause.
    def enterDataRecordAreaClause(self, ctx:DNPParser.DataRecordAreaClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#dataRecordAreaClause.
    def exitDataRecordAreaClause(self, ctx:DNPParser.DataRecordAreaClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#dataRedefinesClause.
    def enterDataRedefinesClause(self, ctx:DNPParser.DataRedefinesClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#dataRedefinesClause.
    def exitDataRedefinesClause(self, ctx:DNPParser.DataRedefinesClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#dataRenamesClause.
    def enterDataRenamesClause(self, ctx:DNPParser.DataRenamesClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#dataRenamesClause.
    def exitDataRenamesClause(self, ctx:DNPParser.DataRenamesClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#dataSignClause.
    def enterDataSignClause(self, ctx:DNPParser.DataSignClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#dataSignClause.
    def exitDataSignClause(self, ctx:DNPParser.DataSignClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#dataSynchronizedClause.
    def enterDataSynchronizedClause(self, ctx:DNPParser.DataSynchronizedClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#dataSynchronizedClause.
    def exitDataSynchronizedClause(self, ctx:DNPParser.DataSynchronizedClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#dataThreadLocalClause.
    def enterDataThreadLocalClause(self, ctx:DNPParser.DataThreadLocalClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#dataThreadLocalClause.
    def exitDataThreadLocalClause(self, ctx:DNPParser.DataThreadLocalClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#dataTypeClause.
    def enterDataTypeClause(self, ctx:DNPParser.DataTypeClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#dataTypeClause.
    def exitDataTypeClause(self, ctx:DNPParser.DataTypeClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#dataTypeDefClause.
    def enterDataTypeDefClause(self, ctx:DNPParser.DataTypeDefClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#dataTypeDefClause.
    def exitDataTypeDefClause(self, ctx:DNPParser.DataTypeDefClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#dataUsageClause.
    def enterDataUsageClause(self, ctx:DNPParser.DataUsageClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#dataUsageClause.
    def exitDataUsageClause(self, ctx:DNPParser.DataUsageClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#dataUsingClause.
    def enterDataUsingClause(self, ctx:DNPParser.DataUsingClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#dataUsingClause.
    def exitDataUsingClause(self, ctx:DNPParser.DataUsingClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#dataValueClause.
    def enterDataValueClause(self, ctx:DNPParser.DataValueClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#dataValueClause.
    def exitDataValueClause(self, ctx:DNPParser.DataValueClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#dataValueInterval.
    def enterDataValueInterval(self, ctx:DNPParser.DataValueIntervalContext):
        pass

    # Exit a parse tree produced by DNPParser#dataValueInterval.
    def exitDataValueInterval(self, ctx:DNPParser.DataValueIntervalContext):
        pass


    # Enter a parse tree produced by DNPParser#dataValueIntervalFrom.
    def enterDataValueIntervalFrom(self, ctx:DNPParser.DataValueIntervalFromContext):
        pass

    # Exit a parse tree produced by DNPParser#dataValueIntervalFrom.
    def exitDataValueIntervalFrom(self, ctx:DNPParser.DataValueIntervalFromContext):
        pass


    # Enter a parse tree produced by DNPParser#dataValueIntervalTo.
    def enterDataValueIntervalTo(self, ctx:DNPParser.DataValueIntervalToContext):
        pass

    # Exit a parse tree produced by DNPParser#dataValueIntervalTo.
    def exitDataValueIntervalTo(self, ctx:DNPParser.DataValueIntervalToContext):
        pass


    # Enter a parse tree produced by DNPParser#dataWithLowerBoundsClause.
    def enterDataWithLowerBoundsClause(self, ctx:DNPParser.DataWithLowerBoundsClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#dataWithLowerBoundsClause.
    def exitDataWithLowerBoundsClause(self, ctx:DNPParser.DataWithLowerBoundsClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#procedureDivision.
    def enterProcedureDivision(self, ctx:DNPParser.ProcedureDivisionContext):
        pass

    # Exit a parse tree produced by DNPParser#procedureDivision.
    def exitProcedureDivision(self, ctx:DNPParser.ProcedureDivisionContext):
        pass


    # Enter a parse tree produced by DNPParser#procedureDivisionUsingClause.
    def enterProcedureDivisionUsingClause(self, ctx:DNPParser.ProcedureDivisionUsingClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#procedureDivisionUsingClause.
    def exitProcedureDivisionUsingClause(self, ctx:DNPParser.ProcedureDivisionUsingClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#procedureDivisionGivingClause.
    def enterProcedureDivisionGivingClause(self, ctx:DNPParser.ProcedureDivisionGivingClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#procedureDivisionGivingClause.
    def exitProcedureDivisionGivingClause(self, ctx:DNPParser.ProcedureDivisionGivingClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#procedureDivisionUsingParameter.
    def enterProcedureDivisionUsingParameter(self, ctx:DNPParser.ProcedureDivisionUsingParameterContext):
        pass

    # Exit a parse tree produced by DNPParser#procedureDivisionUsingParameter.
    def exitProcedureDivisionUsingParameter(self, ctx:DNPParser.ProcedureDivisionUsingParameterContext):
        pass


    # Enter a parse tree produced by DNPParser#procedureDivisionByReferencePhrase.
    def enterProcedureDivisionByReferencePhrase(self, ctx:DNPParser.ProcedureDivisionByReferencePhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#procedureDivisionByReferencePhrase.
    def exitProcedureDivisionByReferencePhrase(self, ctx:DNPParser.ProcedureDivisionByReferencePhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#procedureDivisionByReference.
    def enterProcedureDivisionByReference(self, ctx:DNPParser.ProcedureDivisionByReferenceContext):
        pass

    # Exit a parse tree produced by DNPParser#procedureDivisionByReference.
    def exitProcedureDivisionByReference(self, ctx:DNPParser.ProcedureDivisionByReferenceContext):
        pass


    # Enter a parse tree produced by DNPParser#procedureDivisionByValuePhrase.
    def enterProcedureDivisionByValuePhrase(self, ctx:DNPParser.ProcedureDivisionByValuePhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#procedureDivisionByValuePhrase.
    def exitProcedureDivisionByValuePhrase(self, ctx:DNPParser.ProcedureDivisionByValuePhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#procedureDivisionByValue.
    def enterProcedureDivisionByValue(self, ctx:DNPParser.ProcedureDivisionByValueContext):
        pass

    # Exit a parse tree produced by DNPParser#procedureDivisionByValue.
    def exitProcedureDivisionByValue(self, ctx:DNPParser.ProcedureDivisionByValueContext):
        pass


    # Enter a parse tree produced by DNPParser#procedureDeclaratives.
    def enterProcedureDeclaratives(self, ctx:DNPParser.ProcedureDeclarativesContext):
        pass

    # Exit a parse tree produced by DNPParser#procedureDeclaratives.
    def exitProcedureDeclaratives(self, ctx:DNPParser.ProcedureDeclarativesContext):
        pass


    # Enter a parse tree produced by DNPParser#procedureDeclarative.
    def enterProcedureDeclarative(self, ctx:DNPParser.ProcedureDeclarativeContext):
        pass

    # Exit a parse tree produced by DNPParser#procedureDeclarative.
    def exitProcedureDeclarative(self, ctx:DNPParser.ProcedureDeclarativeContext):
        pass


    # Enter a parse tree produced by DNPParser#procedureSectionHeader.
    def enterProcedureSectionHeader(self, ctx:DNPParser.ProcedureSectionHeaderContext):
        pass

    # Exit a parse tree produced by DNPParser#procedureSectionHeader.
    def exitProcedureSectionHeader(self, ctx:DNPParser.ProcedureSectionHeaderContext):
        pass


    # Enter a parse tree produced by DNPParser#procedureDivisionBody.
    def enterProcedureDivisionBody(self, ctx:DNPParser.ProcedureDivisionBodyContext):
        pass

    # Exit a parse tree produced by DNPParser#procedureDivisionBody.
    def exitProcedureDivisionBody(self, ctx:DNPParser.ProcedureDivisionBodyContext):
        pass


    # Enter a parse tree produced by DNPParser#procedureSection.
    def enterProcedureSection(self, ctx:DNPParser.ProcedureSectionContext):
        pass

    # Exit a parse tree produced by DNPParser#procedureSection.
    def exitProcedureSection(self, ctx:DNPParser.ProcedureSectionContext):
        pass


    # Enter a parse tree produced by DNPParser#paragraphs.
    def enterParagraphs(self, ctx:DNPParser.ParagraphsContext):
        pass

    # Exit a parse tree produced by DNPParser#paragraphs.
    def exitParagraphs(self, ctx:DNPParser.ParagraphsContext):
        pass


    # Enter a parse tree produced by DNPParser#paragraph.
    def enterParagraph(self, ctx:DNPParser.ParagraphContext):
        pass

    # Exit a parse tree produced by DNPParser#paragraph.
    def exitParagraph(self, ctx:DNPParser.ParagraphContext):
        pass


    # Enter a parse tree produced by DNPParser#sentence.
    def enterSentence(self, ctx:DNPParser.SentenceContext):
        pass

    # Exit a parse tree produced by DNPParser#sentence.
    def exitSentence(self, ctx:DNPParser.SentenceContext):
        pass


    # Enter a parse tree produced by DNPParser#statement.
    def enterStatement(self, ctx:DNPParser.StatementContext):
        pass

    # Exit a parse tree produced by DNPParser#statement.
    def exitStatement(self, ctx:DNPParser.StatementContext):
        pass


    # Enter a parse tree produced by DNPParser#execCicsStatement2.
    def enterExecCicsStatement2(self, ctx:DNPParser.ExecCicsStatement2Context):
        pass

    # Exit a parse tree produced by DNPParser#execCicsStatement2.
    def exitExecCicsStatement2(self, ctx:DNPParser.ExecCicsStatement2Context):
        pass


    # Enter a parse tree produced by DNPParser#acceptStatement.
    def enterAcceptStatement(self, ctx:DNPParser.AcceptStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#acceptStatement.
    def exitAcceptStatement(self, ctx:DNPParser.AcceptStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#acceptFromDateStatement.
    def enterAcceptFromDateStatement(self, ctx:DNPParser.AcceptFromDateStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#acceptFromDateStatement.
    def exitAcceptFromDateStatement(self, ctx:DNPParser.AcceptFromDateStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#acceptFromDatePhrase.
    def enterAcceptFromDatePhrase(self, ctx:DNPParser.AcceptFromDatePhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#acceptFromDatePhrase.
    def exitAcceptFromDatePhrase(self, ctx:DNPParser.AcceptFromDatePhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#acceptFromMnemonicStatement.
    def enterAcceptFromMnemonicStatement(self, ctx:DNPParser.AcceptFromMnemonicStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#acceptFromMnemonicStatement.
    def exitAcceptFromMnemonicStatement(self, ctx:DNPParser.AcceptFromMnemonicStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#acceptFromEscapeKeyStatement.
    def enterAcceptFromEscapeKeyStatement(self, ctx:DNPParser.AcceptFromEscapeKeyStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#acceptFromEscapeKeyStatement.
    def exitAcceptFromEscapeKeyStatement(self, ctx:DNPParser.AcceptFromEscapeKeyStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#acceptMessageCountStatement.
    def enterAcceptMessageCountStatement(self, ctx:DNPParser.AcceptMessageCountStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#acceptMessageCountStatement.
    def exitAcceptMessageCountStatement(self, ctx:DNPParser.AcceptMessageCountStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#addStatement.
    def enterAddStatement(self, ctx:DNPParser.AddStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#addStatement.
    def exitAddStatement(self, ctx:DNPParser.AddStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#addToStatement.
    def enterAddToStatement(self, ctx:DNPParser.AddToStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#addToStatement.
    def exitAddToStatement(self, ctx:DNPParser.AddToStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#addToGivingStatement.
    def enterAddToGivingStatement(self, ctx:DNPParser.AddToGivingStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#addToGivingStatement.
    def exitAddToGivingStatement(self, ctx:DNPParser.AddToGivingStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#addCorrespondingStatement.
    def enterAddCorrespondingStatement(self, ctx:DNPParser.AddCorrespondingStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#addCorrespondingStatement.
    def exitAddCorrespondingStatement(self, ctx:DNPParser.AddCorrespondingStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#addFrom.
    def enterAddFrom(self, ctx:DNPParser.AddFromContext):
        pass

    # Exit a parse tree produced by DNPParser#addFrom.
    def exitAddFrom(self, ctx:DNPParser.AddFromContext):
        pass


    # Enter a parse tree produced by DNPParser#addTo.
    def enterAddTo(self, ctx:DNPParser.AddToContext):
        pass

    # Exit a parse tree produced by DNPParser#addTo.
    def exitAddTo(self, ctx:DNPParser.AddToContext):
        pass


    # Enter a parse tree produced by DNPParser#addToGiving.
    def enterAddToGiving(self, ctx:DNPParser.AddToGivingContext):
        pass

    # Exit a parse tree produced by DNPParser#addToGiving.
    def exitAddToGiving(self, ctx:DNPParser.AddToGivingContext):
        pass


    # Enter a parse tree produced by DNPParser#addGiving.
    def enterAddGiving(self, ctx:DNPParser.AddGivingContext):
        pass

    # Exit a parse tree produced by DNPParser#addGiving.
    def exitAddGiving(self, ctx:DNPParser.AddGivingContext):
        pass


    # Enter a parse tree produced by DNPParser#alteredGoTo.
    def enterAlteredGoTo(self, ctx:DNPParser.AlteredGoToContext):
        pass

    # Exit a parse tree produced by DNPParser#alteredGoTo.
    def exitAlteredGoTo(self, ctx:DNPParser.AlteredGoToContext):
        pass


    # Enter a parse tree produced by DNPParser#alterStatement.
    def enterAlterStatement(self, ctx:DNPParser.AlterStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#alterStatement.
    def exitAlterStatement(self, ctx:DNPParser.AlterStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#alterProceedTo.
    def enterAlterProceedTo(self, ctx:DNPParser.AlterProceedToContext):
        pass

    # Exit a parse tree produced by DNPParser#alterProceedTo.
    def exitAlterProceedTo(self, ctx:DNPParser.AlterProceedToContext):
        pass


    # Enter a parse tree produced by DNPParser#attachStatement.
    def enterAttachStatement(self, ctx:DNPParser.AttachStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#attachStatement.
    def exitAttachStatement(self, ctx:DNPParser.AttachStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#callStatement.
    def enterCallStatement(self, ctx:DNPParser.CallStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#callStatement.
    def exitCallStatement(self, ctx:DNPParser.CallStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#callUsingPhrase.
    def enterCallUsingPhrase(self, ctx:DNPParser.CallUsingPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#callUsingPhrase.
    def exitCallUsingPhrase(self, ctx:DNPParser.CallUsingPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#callUsingParameter.
    def enterCallUsingParameter(self, ctx:DNPParser.CallUsingParameterContext):
        pass

    # Exit a parse tree produced by DNPParser#callUsingParameter.
    def exitCallUsingParameter(self, ctx:DNPParser.CallUsingParameterContext):
        pass


    # Enter a parse tree produced by DNPParser#callByReferencePhrase.
    def enterCallByReferencePhrase(self, ctx:DNPParser.CallByReferencePhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#callByReferencePhrase.
    def exitCallByReferencePhrase(self, ctx:DNPParser.CallByReferencePhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#callByReference.
    def enterCallByReference(self, ctx:DNPParser.CallByReferenceContext):
        pass

    # Exit a parse tree produced by DNPParser#callByReference.
    def exitCallByReference(self, ctx:DNPParser.CallByReferenceContext):
        pass


    # Enter a parse tree produced by DNPParser#callByValuePhrase.
    def enterCallByValuePhrase(self, ctx:DNPParser.CallByValuePhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#callByValuePhrase.
    def exitCallByValuePhrase(self, ctx:DNPParser.CallByValuePhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#callByValue.
    def enterCallByValue(self, ctx:DNPParser.CallByValueContext):
        pass

    # Exit a parse tree produced by DNPParser#callByValue.
    def exitCallByValue(self, ctx:DNPParser.CallByValueContext):
        pass


    # Enter a parse tree produced by DNPParser#callByContentPhrase.
    def enterCallByContentPhrase(self, ctx:DNPParser.CallByContentPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#callByContentPhrase.
    def exitCallByContentPhrase(self, ctx:DNPParser.CallByContentPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#callByContent.
    def enterCallByContent(self, ctx:DNPParser.CallByContentContext):
        pass

    # Exit a parse tree produced by DNPParser#callByContent.
    def exitCallByContent(self, ctx:DNPParser.CallByContentContext):
        pass


    # Enter a parse tree produced by DNPParser#callGivingPhrase.
    def enterCallGivingPhrase(self, ctx:DNPParser.CallGivingPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#callGivingPhrase.
    def exitCallGivingPhrase(self, ctx:DNPParser.CallGivingPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#callSystem.
    def enterCallSystem(self, ctx:DNPParser.CallSystemContext):
        pass

    # Exit a parse tree produced by DNPParser#callSystem.
    def exitCallSystem(self, ctx:DNPParser.CallSystemContext):
        pass


    # Enter a parse tree produced by DNPParser#cancelStatement.
    def enterCancelStatement(self, ctx:DNPParser.CancelStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#cancelStatement.
    def exitCancelStatement(self, ctx:DNPParser.CancelStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#cancelCall.
    def enterCancelCall(self, ctx:DNPParser.CancelCallContext):
        pass

    # Exit a parse tree produced by DNPParser#cancelCall.
    def exitCancelCall(self, ctx:DNPParser.CancelCallContext):
        pass


    # Enter a parse tree produced by DNPParser#closeStatement.
    def enterCloseStatement(self, ctx:DNPParser.CloseStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#closeStatement.
    def exitCloseStatement(self, ctx:DNPParser.CloseStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#closePhrase.
    def enterClosePhrase(self, ctx:DNPParser.ClosePhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#closePhrase.
    def exitClosePhrase(self, ctx:DNPParser.ClosePhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#closeFile.
    def enterCloseFile(self, ctx:DNPParser.CloseFileContext):
        pass

    # Exit a parse tree produced by DNPParser#closeFile.
    def exitCloseFile(self, ctx:DNPParser.CloseFileContext):
        pass


    # Enter a parse tree produced by DNPParser#closeReelUnitStatement.
    def enterCloseReelUnitStatement(self, ctx:DNPParser.CloseReelUnitStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#closeReelUnitStatement.
    def exitCloseReelUnitStatement(self, ctx:DNPParser.CloseReelUnitStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#closeRelativeStatement.
    def enterCloseRelativeStatement(self, ctx:DNPParser.CloseRelativeStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#closeRelativeStatement.
    def exitCloseRelativeStatement(self, ctx:DNPParser.CloseRelativeStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#closePortFileIOStatement.
    def enterClosePortFileIOStatement(self, ctx:DNPParser.ClosePortFileIOStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#closePortFileIOStatement.
    def exitClosePortFileIOStatement(self, ctx:DNPParser.ClosePortFileIOStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#closePortFileIOUsing.
    def enterClosePortFileIOUsing(self, ctx:DNPParser.ClosePortFileIOUsingContext):
        pass

    # Exit a parse tree produced by DNPParser#closePortFileIOUsing.
    def exitClosePortFileIOUsing(self, ctx:DNPParser.ClosePortFileIOUsingContext):
        pass


    # Enter a parse tree produced by DNPParser#closePortFileIOUsingCloseDisposition.
    def enterClosePortFileIOUsingCloseDisposition(self, ctx:DNPParser.ClosePortFileIOUsingCloseDispositionContext):
        pass

    # Exit a parse tree produced by DNPParser#closePortFileIOUsingCloseDisposition.
    def exitClosePortFileIOUsingCloseDisposition(self, ctx:DNPParser.ClosePortFileIOUsingCloseDispositionContext):
        pass


    # Enter a parse tree produced by DNPParser#closePortFileIOUsingAssociatedData.
    def enterClosePortFileIOUsingAssociatedData(self, ctx:DNPParser.ClosePortFileIOUsingAssociatedDataContext):
        pass

    # Exit a parse tree produced by DNPParser#closePortFileIOUsingAssociatedData.
    def exitClosePortFileIOUsingAssociatedData(self, ctx:DNPParser.ClosePortFileIOUsingAssociatedDataContext):
        pass


    # Enter a parse tree produced by DNPParser#closePortFileIOUsingAssociatedDataLength.
    def enterClosePortFileIOUsingAssociatedDataLength(self, ctx:DNPParser.ClosePortFileIOUsingAssociatedDataLengthContext):
        pass

    # Exit a parse tree produced by DNPParser#closePortFileIOUsingAssociatedDataLength.
    def exitClosePortFileIOUsingAssociatedDataLength(self, ctx:DNPParser.ClosePortFileIOUsingAssociatedDataLengthContext):
        pass


    # Enter a parse tree produced by DNPParser#computeStatement.
    def enterComputeStatement(self, ctx:DNPParser.ComputeStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#computeStatement.
    def exitComputeStatement(self, ctx:DNPParser.ComputeStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#computeStore.
    def enterComputeStore(self, ctx:DNPParser.ComputeStoreContext):
        pass

    # Exit a parse tree produced by DNPParser#computeStore.
    def exitComputeStore(self, ctx:DNPParser.ComputeStoreContext):
        pass


    # Enter a parse tree produced by DNPParser#continueStatement.
    def enterContinueStatement(self, ctx:DNPParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#continueStatement.
    def exitContinueStatement(self, ctx:DNPParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#continueIndicator.
    def enterContinueIndicator(self, ctx:DNPParser.ContinueIndicatorContext):
        pass

    # Exit a parse tree produced by DNPParser#continueIndicator.
    def exitContinueIndicator(self, ctx:DNPParser.ContinueIndicatorContext):
        pass


    # Enter a parse tree produced by DNPParser#deleteStatement.
    def enterDeleteStatement(self, ctx:DNPParser.DeleteStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#deleteStatement.
    def exitDeleteStatement(self, ctx:DNPParser.DeleteStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#disableStatement.
    def enterDisableStatement(self, ctx:DNPParser.DisableStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#disableStatement.
    def exitDisableStatement(self, ctx:DNPParser.DisableStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#displayStatement.
    def enterDisplayStatement(self, ctx:DNPParser.DisplayStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#displayStatement.
    def exitDisplayStatement(self, ctx:DNPParser.DisplayStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#displayOperand.
    def enterDisplayOperand(self, ctx:DNPParser.DisplayOperandContext):
        pass

    # Exit a parse tree produced by DNPParser#displayOperand.
    def exitDisplayOperand(self, ctx:DNPParser.DisplayOperandContext):
        pass


    # Enter a parse tree produced by DNPParser#displayAt.
    def enterDisplayAt(self, ctx:DNPParser.DisplayAtContext):
        pass

    # Exit a parse tree produced by DNPParser#displayAt.
    def exitDisplayAt(self, ctx:DNPParser.DisplayAtContext):
        pass


    # Enter a parse tree produced by DNPParser#displayUpon.
    def enterDisplayUpon(self, ctx:DNPParser.DisplayUponContext):
        pass

    # Exit a parse tree produced by DNPParser#displayUpon.
    def exitDisplayUpon(self, ctx:DNPParser.DisplayUponContext):
        pass


    # Enter a parse tree produced by DNPParser#displayWith.
    def enterDisplayWith(self, ctx:DNPParser.DisplayWithContext):
        pass

    # Exit a parse tree produced by DNPParser#displayWith.
    def exitDisplayWith(self, ctx:DNPParser.DisplayWithContext):
        pass


    # Enter a parse tree produced by DNPParser#divideStatement.
    def enterDivideStatement(self, ctx:DNPParser.DivideStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#divideStatement.
    def exitDivideStatement(self, ctx:DNPParser.DivideStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#divideIntoStatement.
    def enterDivideIntoStatement(self, ctx:DNPParser.DivideIntoStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#divideIntoStatement.
    def exitDivideIntoStatement(self, ctx:DNPParser.DivideIntoStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#divideIntoGivingStatement.
    def enterDivideIntoGivingStatement(self, ctx:DNPParser.DivideIntoGivingStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#divideIntoGivingStatement.
    def exitDivideIntoGivingStatement(self, ctx:DNPParser.DivideIntoGivingStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#divideByGivingStatement.
    def enterDivideByGivingStatement(self, ctx:DNPParser.DivideByGivingStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#divideByGivingStatement.
    def exitDivideByGivingStatement(self, ctx:DNPParser.DivideByGivingStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#divideGivingPhrase.
    def enterDivideGivingPhrase(self, ctx:DNPParser.DivideGivingPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#divideGivingPhrase.
    def exitDivideGivingPhrase(self, ctx:DNPParser.DivideGivingPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#divideInto.
    def enterDivideInto(self, ctx:DNPParser.DivideIntoContext):
        pass

    # Exit a parse tree produced by DNPParser#divideInto.
    def exitDivideInto(self, ctx:DNPParser.DivideIntoContext):
        pass


    # Enter a parse tree produced by DNPParser#divideGiving.
    def enterDivideGiving(self, ctx:DNPParser.DivideGivingContext):
        pass

    # Exit a parse tree produced by DNPParser#divideGiving.
    def exitDivideGiving(self, ctx:DNPParser.DivideGivingContext):
        pass


    # Enter a parse tree produced by DNPParser#divideRemainder.
    def enterDivideRemainder(self, ctx:DNPParser.DivideRemainderContext):
        pass

    # Exit a parse tree produced by DNPParser#divideRemainder.
    def exitDivideRemainder(self, ctx:DNPParser.DivideRemainderContext):
        pass


    # Enter a parse tree produced by DNPParser#enableStatement.
    def enterEnableStatement(self, ctx:DNPParser.EnableStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#enableStatement.
    def exitEnableStatement(self, ctx:DNPParser.EnableStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#entryStatement.
    def enterEntryStatement(self, ctx:DNPParser.EntryStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#entryStatement.
    def exitEntryStatement(self, ctx:DNPParser.EntryStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#evaluateStatement.
    def enterEvaluateStatement(self, ctx:DNPParser.EvaluateStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#evaluateStatement.
    def exitEvaluateStatement(self, ctx:DNPParser.EvaluateStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#evaluateSelect.
    def enterEvaluateSelect(self, ctx:DNPParser.EvaluateSelectContext):
        pass

    # Exit a parse tree produced by DNPParser#evaluateSelect.
    def exitEvaluateSelect(self, ctx:DNPParser.EvaluateSelectContext):
        pass


    # Enter a parse tree produced by DNPParser#evaluateAlsoSelect.
    def enterEvaluateAlsoSelect(self, ctx:DNPParser.EvaluateAlsoSelectContext):
        pass

    # Exit a parse tree produced by DNPParser#evaluateAlsoSelect.
    def exitEvaluateAlsoSelect(self, ctx:DNPParser.EvaluateAlsoSelectContext):
        pass


    # Enter a parse tree produced by DNPParser#evaluateWhenPhrase.
    def enterEvaluateWhenPhrase(self, ctx:DNPParser.EvaluateWhenPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#evaluateWhenPhrase.
    def exitEvaluateWhenPhrase(self, ctx:DNPParser.EvaluateWhenPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#evaluateWhen.
    def enterEvaluateWhen(self, ctx:DNPParser.EvaluateWhenContext):
        pass

    # Exit a parse tree produced by DNPParser#evaluateWhen.
    def exitEvaluateWhen(self, ctx:DNPParser.EvaluateWhenContext):
        pass


    # Enter a parse tree produced by DNPParser#evaluateCondition.
    def enterEvaluateCondition(self, ctx:DNPParser.EvaluateConditionContext):
        pass

    # Exit a parse tree produced by DNPParser#evaluateCondition.
    def exitEvaluateCondition(self, ctx:DNPParser.EvaluateConditionContext):
        pass


    # Enter a parse tree produced by DNPParser#evaluateThrough.
    def enterEvaluateThrough(self, ctx:DNPParser.EvaluateThroughContext):
        pass

    # Exit a parse tree produced by DNPParser#evaluateThrough.
    def exitEvaluateThrough(self, ctx:DNPParser.EvaluateThroughContext):
        pass


    # Enter a parse tree produced by DNPParser#evaluateAlsoCondition.
    def enterEvaluateAlsoCondition(self, ctx:DNPParser.EvaluateAlsoConditionContext):
        pass

    # Exit a parse tree produced by DNPParser#evaluateAlsoCondition.
    def exitEvaluateAlsoCondition(self, ctx:DNPParser.EvaluateAlsoConditionContext):
        pass


    # Enter a parse tree produced by DNPParser#evaluateWhenOther.
    def enterEvaluateWhenOther(self, ctx:DNPParser.EvaluateWhenOtherContext):
        pass

    # Exit a parse tree produced by DNPParser#evaluateWhenOther.
    def exitEvaluateWhenOther(self, ctx:DNPParser.EvaluateWhenOtherContext):
        pass


    # Enter a parse tree produced by DNPParser#evaluateValue.
    def enterEvaluateValue(self, ctx:DNPParser.EvaluateValueContext):
        pass

    # Exit a parse tree produced by DNPParser#evaluateValue.
    def exitEvaluateValue(self, ctx:DNPParser.EvaluateValueContext):
        pass


    # Enter a parse tree produced by DNPParser#execCicsStatement.
    def enterExecCicsStatement(self, ctx:DNPParser.ExecCicsStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#execCicsStatement.
    def exitExecCicsStatement(self, ctx:DNPParser.ExecCicsStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#execSqlStatement.
    def enterExecSqlStatement(self, ctx:DNPParser.ExecSqlStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#execSqlStatement.
    def exitExecSqlStatement(self, ctx:DNPParser.ExecSqlStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#execSqlImsStatement.
    def enterExecSqlImsStatement(self, ctx:DNPParser.ExecSqlImsStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#execSqlImsStatement.
    def exitExecSqlImsStatement(self, ctx:DNPParser.ExecSqlImsStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#exhibitStatement.
    def enterExhibitStatement(self, ctx:DNPParser.ExhibitStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#exhibitStatement.
    def exitExhibitStatement(self, ctx:DNPParser.ExhibitStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#exhibitOperand.
    def enterExhibitOperand(self, ctx:DNPParser.ExhibitOperandContext):
        pass

    # Exit a parse tree produced by DNPParser#exhibitOperand.
    def exitExhibitOperand(self, ctx:DNPParser.ExhibitOperandContext):
        pass


    # Enter a parse tree produced by DNPParser#exitStatement.
    def enterExitStatement(self, ctx:DNPParser.ExitStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#exitStatement.
    def exitExitStatement(self, ctx:DNPParser.ExitStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#findStatement.
    def enterFindStatement(self, ctx:DNPParser.FindStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#findStatement.
    def exitFindStatement(self, ctx:DNPParser.FindStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#viaClause.
    def enterViaClause(self, ctx:DNPParser.ViaClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#viaClause.
    def exitViaClause(self, ctx:DNPParser.ViaClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#findOption.
    def enterFindOption(self, ctx:DNPParser.FindOptionContext):
        pass

    # Exit a parse tree produced by DNPParser#findOption.
    def exitFindOption(self, ctx:DNPParser.FindOptionContext):
        pass


    # Enter a parse tree produced by DNPParser#freeStatement.
    def enterFreeStatement(self, ctx:DNPParser.FreeStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#freeStatement.
    def exitFreeStatement(self, ctx:DNPParser.FreeStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#generateStatement.
    def enterGenerateStatement(self, ctx:DNPParser.GenerateStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#generateStatement.
    def exitGenerateStatement(self, ctx:DNPParser.GenerateStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#gobackStatement.
    def enterGobackStatement(self, ctx:DNPParser.GobackStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#gobackStatement.
    def exitGobackStatement(self, ctx:DNPParser.GobackStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#goToStatement.
    def enterGoToStatement(self, ctx:DNPParser.GoToStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#goToStatement.
    def exitGoToStatement(self, ctx:DNPParser.GoToStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#goToStatementSimple.
    def enterGoToStatementSimple(self, ctx:DNPParser.GoToStatementSimpleContext):
        pass

    # Exit a parse tree produced by DNPParser#goToStatementSimple.
    def exitGoToStatementSimple(self, ctx:DNPParser.GoToStatementSimpleContext):
        pass


    # Enter a parse tree produced by DNPParser#goToDependingOnStatement.
    def enterGoToDependingOnStatement(self, ctx:DNPParser.GoToDependingOnStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#goToDependingOnStatement.
    def exitGoToDependingOnStatement(self, ctx:DNPParser.GoToDependingOnStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#ifStatement.
    def enterIfStatement(self, ctx:DNPParser.IfStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#ifStatement.
    def exitIfStatement(self, ctx:DNPParser.IfStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#ifThen.
    def enterIfThen(self, ctx:DNPParser.IfThenContext):
        pass

    # Exit a parse tree produced by DNPParser#ifThen.
    def exitIfThen(self, ctx:DNPParser.IfThenContext):
        pass


    # Enter a parse tree produced by DNPParser#ifElse.
    def enterIfElse(self, ctx:DNPParser.IfElseContext):
        pass

    # Exit a parse tree produced by DNPParser#ifElse.
    def exitIfElse(self, ctx:DNPParser.IfElseContext):
        pass


    # Enter a parse tree produced by DNPParser#initializeStatement.
    def enterInitializeStatement(self, ctx:DNPParser.InitializeStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#initializeStatement.
    def exitInitializeStatement(self, ctx:DNPParser.InitializeStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#initializeReplacingPhrase.
    def enterInitializeReplacingPhrase(self, ctx:DNPParser.InitializeReplacingPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#initializeReplacingPhrase.
    def exitInitializeReplacingPhrase(self, ctx:DNPParser.InitializeReplacingPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#initializeReplacingBy.
    def enterInitializeReplacingBy(self, ctx:DNPParser.InitializeReplacingByContext):
        pass

    # Exit a parse tree produced by DNPParser#initializeReplacingBy.
    def exitInitializeReplacingBy(self, ctx:DNPParser.InitializeReplacingByContext):
        pass


    # Enter a parse tree produced by DNPParser#initiateStatement.
    def enterInitiateStatement(self, ctx:DNPParser.InitiateStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#initiateStatement.
    def exitInitiateStatement(self, ctx:DNPParser.InitiateStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#inspectStatement.
    def enterInspectStatement(self, ctx:DNPParser.InspectStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#inspectStatement.
    def exitInspectStatement(self, ctx:DNPParser.InspectStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#inspectTallyingPhrase.
    def enterInspectTallyingPhrase(self, ctx:DNPParser.InspectTallyingPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#inspectTallyingPhrase.
    def exitInspectTallyingPhrase(self, ctx:DNPParser.InspectTallyingPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#inspectReplacingPhrase.
    def enterInspectReplacingPhrase(self, ctx:DNPParser.InspectReplacingPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#inspectReplacingPhrase.
    def exitInspectReplacingPhrase(self, ctx:DNPParser.InspectReplacingPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#inspectTallyingReplacingPhrase.
    def enterInspectTallyingReplacingPhrase(self, ctx:DNPParser.InspectTallyingReplacingPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#inspectTallyingReplacingPhrase.
    def exitInspectTallyingReplacingPhrase(self, ctx:DNPParser.InspectTallyingReplacingPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#inspectConvertingPhrase.
    def enterInspectConvertingPhrase(self, ctx:DNPParser.InspectConvertingPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#inspectConvertingPhrase.
    def exitInspectConvertingPhrase(self, ctx:DNPParser.InspectConvertingPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#inspectFor.
    def enterInspectFor(self, ctx:DNPParser.InspectForContext):
        pass

    # Exit a parse tree produced by DNPParser#inspectFor.
    def exitInspectFor(self, ctx:DNPParser.InspectForContext):
        pass


    # Enter a parse tree produced by DNPParser#inspectCharacters.
    def enterInspectCharacters(self, ctx:DNPParser.InspectCharactersContext):
        pass

    # Exit a parse tree produced by DNPParser#inspectCharacters.
    def exitInspectCharacters(self, ctx:DNPParser.InspectCharactersContext):
        pass


    # Enter a parse tree produced by DNPParser#inspectReplacingCharacters.
    def enterInspectReplacingCharacters(self, ctx:DNPParser.InspectReplacingCharactersContext):
        pass

    # Exit a parse tree produced by DNPParser#inspectReplacingCharacters.
    def exitInspectReplacingCharacters(self, ctx:DNPParser.InspectReplacingCharactersContext):
        pass


    # Enter a parse tree produced by DNPParser#inspectAllLeadings.
    def enterInspectAllLeadings(self, ctx:DNPParser.InspectAllLeadingsContext):
        pass

    # Exit a parse tree produced by DNPParser#inspectAllLeadings.
    def exitInspectAllLeadings(self, ctx:DNPParser.InspectAllLeadingsContext):
        pass


    # Enter a parse tree produced by DNPParser#inspectReplacingAllLeadings.
    def enterInspectReplacingAllLeadings(self, ctx:DNPParser.InspectReplacingAllLeadingsContext):
        pass

    # Exit a parse tree produced by DNPParser#inspectReplacingAllLeadings.
    def exitInspectReplacingAllLeadings(self, ctx:DNPParser.InspectReplacingAllLeadingsContext):
        pass


    # Enter a parse tree produced by DNPParser#inspectAllLeading.
    def enterInspectAllLeading(self, ctx:DNPParser.InspectAllLeadingContext):
        pass

    # Exit a parse tree produced by DNPParser#inspectAllLeading.
    def exitInspectAllLeading(self, ctx:DNPParser.InspectAllLeadingContext):
        pass


    # Enter a parse tree produced by DNPParser#inspectReplacingAllLeading.
    def enterInspectReplacingAllLeading(self, ctx:DNPParser.InspectReplacingAllLeadingContext):
        pass

    # Exit a parse tree produced by DNPParser#inspectReplacingAllLeading.
    def exitInspectReplacingAllLeading(self, ctx:DNPParser.InspectReplacingAllLeadingContext):
        pass


    # Enter a parse tree produced by DNPParser#inspectBy.
    def enterInspectBy(self, ctx:DNPParser.InspectByContext):
        pass

    # Exit a parse tree produced by DNPParser#inspectBy.
    def exitInspectBy(self, ctx:DNPParser.InspectByContext):
        pass


    # Enter a parse tree produced by DNPParser#inspectTo.
    def enterInspectTo(self, ctx:DNPParser.InspectToContext):
        pass

    # Exit a parse tree produced by DNPParser#inspectTo.
    def exitInspectTo(self, ctx:DNPParser.InspectToContext):
        pass


    # Enter a parse tree produced by DNPParser#inspectBeforeAfter.
    def enterInspectBeforeAfter(self, ctx:DNPParser.InspectBeforeAfterContext):
        pass

    # Exit a parse tree produced by DNPParser#inspectBeforeAfter.
    def exitInspectBeforeAfter(self, ctx:DNPParser.InspectBeforeAfterContext):
        pass


    # Enter a parse tree produced by DNPParser#lockStatement.
    def enterLockStatement(self, ctx:DNPParser.LockStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#lockStatement.
    def exitLockStatement(self, ctx:DNPParser.LockStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#mergeStatement.
    def enterMergeStatement(self, ctx:DNPParser.MergeStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#mergeStatement.
    def exitMergeStatement(self, ctx:DNPParser.MergeStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#mergeOnKeyClause.
    def enterMergeOnKeyClause(self, ctx:DNPParser.MergeOnKeyClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#mergeOnKeyClause.
    def exitMergeOnKeyClause(self, ctx:DNPParser.MergeOnKeyClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#mergeCollatingSequencePhrase.
    def enterMergeCollatingSequencePhrase(self, ctx:DNPParser.MergeCollatingSequencePhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#mergeCollatingSequencePhrase.
    def exitMergeCollatingSequencePhrase(self, ctx:DNPParser.MergeCollatingSequencePhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#mergeCollatingAlphanumeric.
    def enterMergeCollatingAlphanumeric(self, ctx:DNPParser.MergeCollatingAlphanumericContext):
        pass

    # Exit a parse tree produced by DNPParser#mergeCollatingAlphanumeric.
    def exitMergeCollatingAlphanumeric(self, ctx:DNPParser.MergeCollatingAlphanumericContext):
        pass


    # Enter a parse tree produced by DNPParser#mergeCollatingNational.
    def enterMergeCollatingNational(self, ctx:DNPParser.MergeCollatingNationalContext):
        pass

    # Exit a parse tree produced by DNPParser#mergeCollatingNational.
    def exitMergeCollatingNational(self, ctx:DNPParser.MergeCollatingNationalContext):
        pass


    # Enter a parse tree produced by DNPParser#mergeUsing.
    def enterMergeUsing(self, ctx:DNPParser.MergeUsingContext):
        pass

    # Exit a parse tree produced by DNPParser#mergeUsing.
    def exitMergeUsing(self, ctx:DNPParser.MergeUsingContext):
        pass


    # Enter a parse tree produced by DNPParser#mergeOutputProcedurePhrase.
    def enterMergeOutputProcedurePhrase(self, ctx:DNPParser.MergeOutputProcedurePhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#mergeOutputProcedurePhrase.
    def exitMergeOutputProcedurePhrase(self, ctx:DNPParser.MergeOutputProcedurePhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#mergeOutputThrough.
    def enterMergeOutputThrough(self, ctx:DNPParser.MergeOutputThroughContext):
        pass

    # Exit a parse tree produced by DNPParser#mergeOutputThrough.
    def exitMergeOutputThrough(self, ctx:DNPParser.MergeOutputThroughContext):
        pass


    # Enter a parse tree produced by DNPParser#mergeGivingPhrase.
    def enterMergeGivingPhrase(self, ctx:DNPParser.MergeGivingPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#mergeGivingPhrase.
    def exitMergeGivingPhrase(self, ctx:DNPParser.MergeGivingPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#mergeGiving.
    def enterMergeGiving(self, ctx:DNPParser.MergeGivingContext):
        pass

    # Exit a parse tree produced by DNPParser#mergeGiving.
    def exitMergeGiving(self, ctx:DNPParser.MergeGivingContext):
        pass


    # Enter a parse tree produced by DNPParser#moveStatement.
    def enterMoveStatement(self, ctx:DNPParser.MoveStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#moveStatement.
    def exitMoveStatement(self, ctx:DNPParser.MoveStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#moveToStatement.
    def enterMoveToStatement(self, ctx:DNPParser.MoveToStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#moveToStatement.
    def exitMoveToStatement(self, ctx:DNPParser.MoveToStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#moveToSendingArea.
    def enterMoveToSendingArea(self, ctx:DNPParser.MoveToSendingAreaContext):
        pass

    # Exit a parse tree produced by DNPParser#moveToSendingArea.
    def exitMoveToSendingArea(self, ctx:DNPParser.MoveToSendingAreaContext):
        pass


    # Enter a parse tree produced by DNPParser#moveCorrespondingToStatement.
    def enterMoveCorrespondingToStatement(self, ctx:DNPParser.MoveCorrespondingToStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#moveCorrespondingToStatement.
    def exitMoveCorrespondingToStatement(self, ctx:DNPParser.MoveCorrespondingToStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#moveCorrespondingToSendingArea.
    def enterMoveCorrespondingToSendingArea(self, ctx:DNPParser.MoveCorrespondingToSendingAreaContext):
        pass

    # Exit a parse tree produced by DNPParser#moveCorrespondingToSendingArea.
    def exitMoveCorrespondingToSendingArea(self, ctx:DNPParser.MoveCorrespondingToSendingAreaContext):
        pass


    # Enter a parse tree produced by DNPParser#moveAttributeClause.
    def enterMoveAttributeClause(self, ctx:DNPParser.MoveAttributeClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#moveAttributeClause.
    def exitMoveAttributeClause(self, ctx:DNPParser.MoveAttributeClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#modifyStatement.
    def enterModifyStatement(self, ctx:DNPParser.ModifyStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#modifyStatement.
    def exitModifyStatement(self, ctx:DNPParser.ModifyStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#modifyTo.
    def enterModifyTo(self, ctx:DNPParser.ModifyToContext):
        pass

    # Exit a parse tree produced by DNPParser#modifyTo.
    def exitModifyTo(self, ctx:DNPParser.ModifyToContext):
        pass


    # Enter a parse tree produced by DNPParser#modifyOption.
    def enterModifyOption(self, ctx:DNPParser.ModifyOptionContext):
        pass

    # Exit a parse tree produced by DNPParser#modifyOption.
    def exitModifyOption(self, ctx:DNPParser.ModifyOptionContext):
        pass


    # Enter a parse tree produced by DNPParser#multiplyStatement.
    def enterMultiplyStatement(self, ctx:DNPParser.MultiplyStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#multiplyStatement.
    def exitMultiplyStatement(self, ctx:DNPParser.MultiplyStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#multiplyRegular.
    def enterMultiplyRegular(self, ctx:DNPParser.MultiplyRegularContext):
        pass

    # Exit a parse tree produced by DNPParser#multiplyRegular.
    def exitMultiplyRegular(self, ctx:DNPParser.MultiplyRegularContext):
        pass


    # Enter a parse tree produced by DNPParser#multiplyRegularOperand.
    def enterMultiplyRegularOperand(self, ctx:DNPParser.MultiplyRegularOperandContext):
        pass

    # Exit a parse tree produced by DNPParser#multiplyRegularOperand.
    def exitMultiplyRegularOperand(self, ctx:DNPParser.MultiplyRegularOperandContext):
        pass


    # Enter a parse tree produced by DNPParser#multiplyGiving.
    def enterMultiplyGiving(self, ctx:DNPParser.MultiplyGivingContext):
        pass

    # Exit a parse tree produced by DNPParser#multiplyGiving.
    def exitMultiplyGiving(self, ctx:DNPParser.MultiplyGivingContext):
        pass


    # Enter a parse tree produced by DNPParser#multiplyGivingOperand.
    def enterMultiplyGivingOperand(self, ctx:DNPParser.MultiplyGivingOperandContext):
        pass

    # Exit a parse tree produced by DNPParser#multiplyGivingOperand.
    def exitMultiplyGivingOperand(self, ctx:DNPParser.MultiplyGivingOperandContext):
        pass


    # Enter a parse tree produced by DNPParser#multiplyGivingResult.
    def enterMultiplyGivingResult(self, ctx:DNPParser.MultiplyGivingResultContext):
        pass

    # Exit a parse tree produced by DNPParser#multiplyGivingResult.
    def exitMultiplyGivingResult(self, ctx:DNPParser.MultiplyGivingResultContext):
        pass


    # Enter a parse tree produced by DNPParser#openStatement.
    def enterOpenStatement(self, ctx:DNPParser.OpenStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#openStatement.
    def exitOpenStatement(self, ctx:DNPParser.OpenStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#openInputStatement.
    def enterOpenInputStatement(self, ctx:DNPParser.OpenInputStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#openInputStatement.
    def exitOpenInputStatement(self, ctx:DNPParser.OpenInputStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#openInput.
    def enterOpenInput(self, ctx:DNPParser.OpenInputContext):
        pass

    # Exit a parse tree produced by DNPParser#openInput.
    def exitOpenInput(self, ctx:DNPParser.OpenInputContext):
        pass


    # Enter a parse tree produced by DNPParser#openUpdateStatement.
    def enterOpenUpdateStatement(self, ctx:DNPParser.OpenUpdateStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#openUpdateStatement.
    def exitOpenUpdateStatement(self, ctx:DNPParser.OpenUpdateStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#openOutputStatement.
    def enterOpenOutputStatement(self, ctx:DNPParser.OpenOutputStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#openOutputStatement.
    def exitOpenOutputStatement(self, ctx:DNPParser.OpenOutputStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#openOutput.
    def enterOpenOutput(self, ctx:DNPParser.OpenOutputContext):
        pass

    # Exit a parse tree produced by DNPParser#openOutput.
    def exitOpenOutput(self, ctx:DNPParser.OpenOutputContext):
        pass


    # Enter a parse tree produced by DNPParser#openIOStatement.
    def enterOpenIOStatement(self, ctx:DNPParser.OpenIOStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#openIOStatement.
    def exitOpenIOStatement(self, ctx:DNPParser.OpenIOStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#openInquiry.
    def enterOpenInquiry(self, ctx:DNPParser.OpenInquiryContext):
        pass

    # Exit a parse tree produced by DNPParser#openInquiry.
    def exitOpenInquiry(self, ctx:DNPParser.OpenInquiryContext):
        pass


    # Enter a parse tree produced by DNPParser#openExtendStatement.
    def enterOpenExtendStatement(self, ctx:DNPParser.OpenExtendStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#openExtendStatement.
    def exitOpenExtendStatement(self, ctx:DNPParser.OpenExtendStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#performStatement.
    def enterPerformStatement(self, ctx:DNPParser.PerformStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#performStatement.
    def exitPerformStatement(self, ctx:DNPParser.PerformStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#performInlineStatement.
    def enterPerformInlineStatement(self, ctx:DNPParser.PerformInlineStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#performInlineStatement.
    def exitPerformInlineStatement(self, ctx:DNPParser.PerformInlineStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#performProcedureStatement.
    def enterPerformProcedureStatement(self, ctx:DNPParser.PerformProcedureStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#performProcedureStatement.
    def exitPerformProcedureStatement(self, ctx:DNPParser.PerformProcedureStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#performType.
    def enterPerformType(self, ctx:DNPParser.PerformTypeContext):
        pass

    # Exit a parse tree produced by DNPParser#performType.
    def exitPerformType(self, ctx:DNPParser.PerformTypeContext):
        pass


    # Enter a parse tree produced by DNPParser#performTimes.
    def enterPerformTimes(self, ctx:DNPParser.PerformTimesContext):
        pass

    # Exit a parse tree produced by DNPParser#performTimes.
    def exitPerformTimes(self, ctx:DNPParser.PerformTimesContext):
        pass


    # Enter a parse tree produced by DNPParser#performUntil.
    def enterPerformUntil(self, ctx:DNPParser.PerformUntilContext):
        pass

    # Exit a parse tree produced by DNPParser#performUntil.
    def exitPerformUntil(self, ctx:DNPParser.PerformUntilContext):
        pass


    # Enter a parse tree produced by DNPParser#performVarying.
    def enterPerformVarying(self, ctx:DNPParser.PerformVaryingContext):
        pass

    # Exit a parse tree produced by DNPParser#performVarying.
    def exitPerformVarying(self, ctx:DNPParser.PerformVaryingContext):
        pass


    # Enter a parse tree produced by DNPParser#performVaryingClause.
    def enterPerformVaryingClause(self, ctx:DNPParser.PerformVaryingClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#performVaryingClause.
    def exitPerformVaryingClause(self, ctx:DNPParser.PerformVaryingClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#performVaryingPhrase.
    def enterPerformVaryingPhrase(self, ctx:DNPParser.PerformVaryingPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#performVaryingPhrase.
    def exitPerformVaryingPhrase(self, ctx:DNPParser.PerformVaryingPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#performAfter.
    def enterPerformAfter(self, ctx:DNPParser.PerformAfterContext):
        pass

    # Exit a parse tree produced by DNPParser#performAfter.
    def exitPerformAfter(self, ctx:DNPParser.PerformAfterContext):
        pass


    # Enter a parse tree produced by DNPParser#performFrom.
    def enterPerformFrom(self, ctx:DNPParser.PerformFromContext):
        pass

    # Exit a parse tree produced by DNPParser#performFrom.
    def exitPerformFrom(self, ctx:DNPParser.PerformFromContext):
        pass


    # Enter a parse tree produced by DNPParser#performBy.
    def enterPerformBy(self, ctx:DNPParser.PerformByContext):
        pass

    # Exit a parse tree produced by DNPParser#performBy.
    def exitPerformBy(self, ctx:DNPParser.PerformByContext):
        pass


    # Enter a parse tree produced by DNPParser#performTestClause.
    def enterPerformTestClause(self, ctx:DNPParser.PerformTestClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#performTestClause.
    def exitPerformTestClause(self, ctx:DNPParser.PerformTestClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#purgeStatement.
    def enterPurgeStatement(self, ctx:DNPParser.PurgeStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#purgeStatement.
    def exitPurgeStatement(self, ctx:DNPParser.PurgeStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#readStatement.
    def enterReadStatement(self, ctx:DNPParser.ReadStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#readStatement.
    def exitReadStatement(self, ctx:DNPParser.ReadStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#readInto.
    def enterReadInto(self, ctx:DNPParser.ReadIntoContext):
        pass

    # Exit a parse tree produced by DNPParser#readInto.
    def exitReadInto(self, ctx:DNPParser.ReadIntoContext):
        pass


    # Enter a parse tree produced by DNPParser#readWith.
    def enterReadWith(self, ctx:DNPParser.ReadWithContext):
        pass

    # Exit a parse tree produced by DNPParser#readWith.
    def exitReadWith(self, ctx:DNPParser.ReadWithContext):
        pass


    # Enter a parse tree produced by DNPParser#readKey.
    def enterReadKey(self, ctx:DNPParser.ReadKeyContext):
        pass

    # Exit a parse tree produced by DNPParser#readKey.
    def exitReadKey(self, ctx:DNPParser.ReadKeyContext):
        pass


    # Enter a parse tree produced by DNPParser#receiveStatement.
    def enterReceiveStatement(self, ctx:DNPParser.ReceiveStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#receiveStatement.
    def exitReceiveStatement(self, ctx:DNPParser.ReceiveStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#receiveFromStatement.
    def enterReceiveFromStatement(self, ctx:DNPParser.ReceiveFromStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#receiveFromStatement.
    def exitReceiveFromStatement(self, ctx:DNPParser.ReceiveFromStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#receiveFrom.
    def enterReceiveFrom(self, ctx:DNPParser.ReceiveFromContext):
        pass

    # Exit a parse tree produced by DNPParser#receiveFrom.
    def exitReceiveFrom(self, ctx:DNPParser.ReceiveFromContext):
        pass


    # Enter a parse tree produced by DNPParser#receiveIntoStatement.
    def enterReceiveIntoStatement(self, ctx:DNPParser.ReceiveIntoStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#receiveIntoStatement.
    def exitReceiveIntoStatement(self, ctx:DNPParser.ReceiveIntoStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#receiveNoData.
    def enterReceiveNoData(self, ctx:DNPParser.ReceiveNoDataContext):
        pass

    # Exit a parse tree produced by DNPParser#receiveNoData.
    def exitReceiveNoData(self, ctx:DNPParser.ReceiveNoDataContext):
        pass


    # Enter a parse tree produced by DNPParser#receiveWithData.
    def enterReceiveWithData(self, ctx:DNPParser.ReceiveWithDataContext):
        pass

    # Exit a parse tree produced by DNPParser#receiveWithData.
    def exitReceiveWithData(self, ctx:DNPParser.ReceiveWithDataContext):
        pass


    # Enter a parse tree produced by DNPParser#receiveBefore.
    def enterReceiveBefore(self, ctx:DNPParser.ReceiveBeforeContext):
        pass

    # Exit a parse tree produced by DNPParser#receiveBefore.
    def exitReceiveBefore(self, ctx:DNPParser.ReceiveBeforeContext):
        pass


    # Enter a parse tree produced by DNPParser#receiveWith.
    def enterReceiveWith(self, ctx:DNPParser.ReceiveWithContext):
        pass

    # Exit a parse tree produced by DNPParser#receiveWith.
    def exitReceiveWith(self, ctx:DNPParser.ReceiveWithContext):
        pass


    # Enter a parse tree produced by DNPParser#receiveThread.
    def enterReceiveThread(self, ctx:DNPParser.ReceiveThreadContext):
        pass

    # Exit a parse tree produced by DNPParser#receiveThread.
    def exitReceiveThread(self, ctx:DNPParser.ReceiveThreadContext):
        pass


    # Enter a parse tree produced by DNPParser#receiveSize.
    def enterReceiveSize(self, ctx:DNPParser.ReceiveSizeContext):
        pass

    # Exit a parse tree produced by DNPParser#receiveSize.
    def exitReceiveSize(self, ctx:DNPParser.ReceiveSizeContext):
        pass


    # Enter a parse tree produced by DNPParser#receiveStatus.
    def enterReceiveStatus(self, ctx:DNPParser.ReceiveStatusContext):
        pass

    # Exit a parse tree produced by DNPParser#receiveStatus.
    def exitReceiveStatus(self, ctx:DNPParser.ReceiveStatusContext):
        pass


    # Enter a parse tree produced by DNPParser#releaseStatement.
    def enterReleaseStatement(self, ctx:DNPParser.ReleaseStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#releaseStatement.
    def exitReleaseStatement(self, ctx:DNPParser.ReleaseStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#returnStatement.
    def enterReturnStatement(self, ctx:DNPParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#returnStatement.
    def exitReturnStatement(self, ctx:DNPParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#returnInto.
    def enterReturnInto(self, ctx:DNPParser.ReturnIntoContext):
        pass

    # Exit a parse tree produced by DNPParser#returnInto.
    def exitReturnInto(self, ctx:DNPParser.ReturnIntoContext):
        pass


    # Enter a parse tree produced by DNPParser#rewriteStatement.
    def enterRewriteStatement(self, ctx:DNPParser.RewriteStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#rewriteStatement.
    def exitRewriteStatement(self, ctx:DNPParser.RewriteStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#rewriteFrom.
    def enterRewriteFrom(self, ctx:DNPParser.RewriteFromContext):
        pass

    # Exit a parse tree produced by DNPParser#rewriteFrom.
    def exitRewriteFrom(self, ctx:DNPParser.RewriteFromContext):
        pass


    # Enter a parse tree produced by DNPParser#searchStatement.
    def enterSearchStatement(self, ctx:DNPParser.SearchStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#searchStatement.
    def exitSearchStatement(self, ctx:DNPParser.SearchStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#searchVarying.
    def enterSearchVarying(self, ctx:DNPParser.SearchVaryingContext):
        pass

    # Exit a parse tree produced by DNPParser#searchVarying.
    def exitSearchVarying(self, ctx:DNPParser.SearchVaryingContext):
        pass


    # Enter a parse tree produced by DNPParser#searchWhen.
    def enterSearchWhen(self, ctx:DNPParser.SearchWhenContext):
        pass

    # Exit a parse tree produced by DNPParser#searchWhen.
    def exitSearchWhen(self, ctx:DNPParser.SearchWhenContext):
        pass


    # Enter a parse tree produced by DNPParser#sendStatement.
    def enterSendStatement(self, ctx:DNPParser.SendStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#sendStatement.
    def exitSendStatement(self, ctx:DNPParser.SendStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#sendStatementSync.
    def enterSendStatementSync(self, ctx:DNPParser.SendStatementSyncContext):
        pass

    # Exit a parse tree produced by DNPParser#sendStatementSync.
    def exitSendStatementSync(self, ctx:DNPParser.SendStatementSyncContext):
        pass


    # Enter a parse tree produced by DNPParser#sendStatementAsync.
    def enterSendStatementAsync(self, ctx:DNPParser.SendStatementAsyncContext):
        pass

    # Exit a parse tree produced by DNPParser#sendStatementAsync.
    def exitSendStatementAsync(self, ctx:DNPParser.SendStatementAsyncContext):
        pass


    # Enter a parse tree produced by DNPParser#sendFromPhrase.
    def enterSendFromPhrase(self, ctx:DNPParser.SendFromPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#sendFromPhrase.
    def exitSendFromPhrase(self, ctx:DNPParser.SendFromPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#sendWithPhrase.
    def enterSendWithPhrase(self, ctx:DNPParser.SendWithPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#sendWithPhrase.
    def exitSendWithPhrase(self, ctx:DNPParser.SendWithPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#sendReplacingPhrase.
    def enterSendReplacingPhrase(self, ctx:DNPParser.SendReplacingPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#sendReplacingPhrase.
    def exitSendReplacingPhrase(self, ctx:DNPParser.SendReplacingPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#sendAdvancingPhrase.
    def enterSendAdvancingPhrase(self, ctx:DNPParser.SendAdvancingPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#sendAdvancingPhrase.
    def exitSendAdvancingPhrase(self, ctx:DNPParser.SendAdvancingPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#sendAdvancingPage.
    def enterSendAdvancingPage(self, ctx:DNPParser.SendAdvancingPageContext):
        pass

    # Exit a parse tree produced by DNPParser#sendAdvancingPage.
    def exitSendAdvancingPage(self, ctx:DNPParser.SendAdvancingPageContext):
        pass


    # Enter a parse tree produced by DNPParser#sendAdvancingLines.
    def enterSendAdvancingLines(self, ctx:DNPParser.SendAdvancingLinesContext):
        pass

    # Exit a parse tree produced by DNPParser#sendAdvancingLines.
    def exitSendAdvancingLines(self, ctx:DNPParser.SendAdvancingLinesContext):
        pass


    # Enter a parse tree produced by DNPParser#sendAdvancingMnemonic.
    def enterSendAdvancingMnemonic(self, ctx:DNPParser.SendAdvancingMnemonicContext):
        pass

    # Exit a parse tree produced by DNPParser#sendAdvancingMnemonic.
    def exitSendAdvancingMnemonic(self, ctx:DNPParser.SendAdvancingMnemonicContext):
        pass


    # Enter a parse tree produced by DNPParser#setStatement.
    def enterSetStatement(self, ctx:DNPParser.SetStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#setStatement.
    def exitSetStatement(self, ctx:DNPParser.SetStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#setToStatement.
    def enterSetToStatement(self, ctx:DNPParser.SetToStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#setToStatement.
    def exitSetToStatement(self, ctx:DNPParser.SetToStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#setUpDownByStatement.
    def enterSetUpDownByStatement(self, ctx:DNPParser.SetUpDownByStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#setUpDownByStatement.
    def exitSetUpDownByStatement(self, ctx:DNPParser.SetUpDownByStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#setTo.
    def enterSetTo(self, ctx:DNPParser.SetToContext):
        pass

    # Exit a parse tree produced by DNPParser#setTo.
    def exitSetTo(self, ctx:DNPParser.SetToContext):
        pass


    # Enter a parse tree produced by DNPParser#setToValue.
    def enterSetToValue(self, ctx:DNPParser.SetToValueContext):
        pass

    # Exit a parse tree produced by DNPParser#setToValue.
    def exitSetToValue(self, ctx:DNPParser.SetToValueContext):
        pass


    # Enter a parse tree produced by DNPParser#setByValue.
    def enterSetByValue(self, ctx:DNPParser.SetByValueContext):
        pass

    # Exit a parse tree produced by DNPParser#setByValue.
    def exitSetByValue(self, ctx:DNPParser.SetByValueContext):
        pass


    # Enter a parse tree produced by DNPParser#sortStatement.
    def enterSortStatement(self, ctx:DNPParser.SortStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#sortStatement.
    def exitSortStatement(self, ctx:DNPParser.SortStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#sortOptional.
    def enterSortOptional(self, ctx:DNPParser.SortOptionalContext):
        pass

    # Exit a parse tree produced by DNPParser#sortOptional.
    def exitSortOptional(self, ctx:DNPParser.SortOptionalContext):
        pass


    # Enter a parse tree produced by DNPParser#sortOnKeyClause.
    def enterSortOnKeyClause(self, ctx:DNPParser.SortOnKeyClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#sortOnKeyClause.
    def exitSortOnKeyClause(self, ctx:DNPParser.SortOnKeyClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#sortDuplicatesPhrase.
    def enterSortDuplicatesPhrase(self, ctx:DNPParser.SortDuplicatesPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#sortDuplicatesPhrase.
    def exitSortDuplicatesPhrase(self, ctx:DNPParser.SortDuplicatesPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#sortCollatingSequencePhrase.
    def enterSortCollatingSequencePhrase(self, ctx:DNPParser.SortCollatingSequencePhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#sortCollatingSequencePhrase.
    def exitSortCollatingSequencePhrase(self, ctx:DNPParser.SortCollatingSequencePhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#sortCollatingAlphanumeric.
    def enterSortCollatingAlphanumeric(self, ctx:DNPParser.SortCollatingAlphanumericContext):
        pass

    # Exit a parse tree produced by DNPParser#sortCollatingAlphanumeric.
    def exitSortCollatingAlphanumeric(self, ctx:DNPParser.SortCollatingAlphanumericContext):
        pass


    # Enter a parse tree produced by DNPParser#sortCollatingNational.
    def enterSortCollatingNational(self, ctx:DNPParser.SortCollatingNationalContext):
        pass

    # Exit a parse tree produced by DNPParser#sortCollatingNational.
    def exitSortCollatingNational(self, ctx:DNPParser.SortCollatingNationalContext):
        pass


    # Enter a parse tree produced by DNPParser#sortInputProcedurePhrase.
    def enterSortInputProcedurePhrase(self, ctx:DNPParser.SortInputProcedurePhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#sortInputProcedurePhrase.
    def exitSortInputProcedurePhrase(self, ctx:DNPParser.SortInputProcedurePhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#sortInputThrough.
    def enterSortInputThrough(self, ctx:DNPParser.SortInputThroughContext):
        pass

    # Exit a parse tree produced by DNPParser#sortInputThrough.
    def exitSortInputThrough(self, ctx:DNPParser.SortInputThroughContext):
        pass


    # Enter a parse tree produced by DNPParser#sortUsing.
    def enterSortUsing(self, ctx:DNPParser.SortUsingContext):
        pass

    # Exit a parse tree produced by DNPParser#sortUsing.
    def exitSortUsing(self, ctx:DNPParser.SortUsingContext):
        pass


    # Enter a parse tree produced by DNPParser#sortOutputProcedurePhrase.
    def enterSortOutputProcedurePhrase(self, ctx:DNPParser.SortOutputProcedurePhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#sortOutputProcedurePhrase.
    def exitSortOutputProcedurePhrase(self, ctx:DNPParser.SortOutputProcedurePhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#sortOutputThrough.
    def enterSortOutputThrough(self, ctx:DNPParser.SortOutputThroughContext):
        pass

    # Exit a parse tree produced by DNPParser#sortOutputThrough.
    def exitSortOutputThrough(self, ctx:DNPParser.SortOutputThroughContext):
        pass


    # Enter a parse tree produced by DNPParser#sortGivingPhrase.
    def enterSortGivingPhrase(self, ctx:DNPParser.SortGivingPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#sortGivingPhrase.
    def exitSortGivingPhrase(self, ctx:DNPParser.SortGivingPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#sortGiving.
    def enterSortGiving(self, ctx:DNPParser.SortGivingContext):
        pass

    # Exit a parse tree produced by DNPParser#sortGiving.
    def exitSortGiving(self, ctx:DNPParser.SortGivingContext):
        pass


    # Enter a parse tree produced by DNPParser#startStatement.
    def enterStartStatement(self, ctx:DNPParser.StartStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#startStatement.
    def exitStartStatement(self, ctx:DNPParser.StartStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#startKey.
    def enterStartKey(self, ctx:DNPParser.StartKeyContext):
        pass

    # Exit a parse tree produced by DNPParser#startKey.
    def exitStartKey(self, ctx:DNPParser.StartKeyContext):
        pass


    # Enter a parse tree produced by DNPParser#stopStatement.
    def enterStopStatement(self, ctx:DNPParser.StopStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#stopStatement.
    def exitStopStatement(self, ctx:DNPParser.StopStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#stopOption.
    def enterStopOption(self, ctx:DNPParser.StopOptionContext):
        pass

    # Exit a parse tree produced by DNPParser#stopOption.
    def exitStopOption(self, ctx:DNPParser.StopOptionContext):
        pass


    # Enter a parse tree produced by DNPParser#storeStatement.
    def enterStoreStatement(self, ctx:DNPParser.StoreStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#storeStatement.
    def exitStoreStatement(self, ctx:DNPParser.StoreStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#stringStatement.
    def enterStringStatement(self, ctx:DNPParser.StringStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#stringStatement.
    def exitStringStatement(self, ctx:DNPParser.StringStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#stringSendingPhrase.
    def enterStringSendingPhrase(self, ctx:DNPParser.StringSendingPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#stringSendingPhrase.
    def exitStringSendingPhrase(self, ctx:DNPParser.StringSendingPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#stringSending.
    def enterStringSending(self, ctx:DNPParser.StringSendingContext):
        pass

    # Exit a parse tree produced by DNPParser#stringSending.
    def exitStringSending(self, ctx:DNPParser.StringSendingContext):
        pass


    # Enter a parse tree produced by DNPParser#stringDelimitedByPhrase.
    def enterStringDelimitedByPhrase(self, ctx:DNPParser.StringDelimitedByPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#stringDelimitedByPhrase.
    def exitStringDelimitedByPhrase(self, ctx:DNPParser.StringDelimitedByPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#stringForPhrase.
    def enterStringForPhrase(self, ctx:DNPParser.StringForPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#stringForPhrase.
    def exitStringForPhrase(self, ctx:DNPParser.StringForPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#stringIntoPhrase.
    def enterStringIntoPhrase(self, ctx:DNPParser.StringIntoPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#stringIntoPhrase.
    def exitStringIntoPhrase(self, ctx:DNPParser.StringIntoPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#stringWithPointerPhrase.
    def enterStringWithPointerPhrase(self, ctx:DNPParser.StringWithPointerPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#stringWithPointerPhrase.
    def exitStringWithPointerPhrase(self, ctx:DNPParser.StringWithPointerPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#subtractStatement.
    def enterSubtractStatement(self, ctx:DNPParser.SubtractStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#subtractStatement.
    def exitSubtractStatement(self, ctx:DNPParser.SubtractStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#subtractFromStatement.
    def enterSubtractFromStatement(self, ctx:DNPParser.SubtractFromStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#subtractFromStatement.
    def exitSubtractFromStatement(self, ctx:DNPParser.SubtractFromStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#subtractFromGivingStatement.
    def enterSubtractFromGivingStatement(self, ctx:DNPParser.SubtractFromGivingStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#subtractFromGivingStatement.
    def exitSubtractFromGivingStatement(self, ctx:DNPParser.SubtractFromGivingStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#subtractCorrespondingStatement.
    def enterSubtractCorrespondingStatement(self, ctx:DNPParser.SubtractCorrespondingStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#subtractCorrespondingStatement.
    def exitSubtractCorrespondingStatement(self, ctx:DNPParser.SubtractCorrespondingStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#subtractSubtrahend.
    def enterSubtractSubtrahend(self, ctx:DNPParser.SubtractSubtrahendContext):
        pass

    # Exit a parse tree produced by DNPParser#subtractSubtrahend.
    def exitSubtractSubtrahend(self, ctx:DNPParser.SubtractSubtrahendContext):
        pass


    # Enter a parse tree produced by DNPParser#subtractMinuend.
    def enterSubtractMinuend(self, ctx:DNPParser.SubtractMinuendContext):
        pass

    # Exit a parse tree produced by DNPParser#subtractMinuend.
    def exitSubtractMinuend(self, ctx:DNPParser.SubtractMinuendContext):
        pass


    # Enter a parse tree produced by DNPParser#subtractMinuendGiving.
    def enterSubtractMinuendGiving(self, ctx:DNPParser.SubtractMinuendGivingContext):
        pass

    # Exit a parse tree produced by DNPParser#subtractMinuendGiving.
    def exitSubtractMinuendGiving(self, ctx:DNPParser.SubtractMinuendGivingContext):
        pass


    # Enter a parse tree produced by DNPParser#subtractGiving.
    def enterSubtractGiving(self, ctx:DNPParser.SubtractGivingContext):
        pass

    # Exit a parse tree produced by DNPParser#subtractGiving.
    def exitSubtractGiving(self, ctx:DNPParser.SubtractGivingContext):
        pass


    # Enter a parse tree produced by DNPParser#subtractMinuendCorresponding.
    def enterSubtractMinuendCorresponding(self, ctx:DNPParser.SubtractMinuendCorrespondingContext):
        pass

    # Exit a parse tree produced by DNPParser#subtractMinuendCorresponding.
    def exitSubtractMinuendCorresponding(self, ctx:DNPParser.SubtractMinuendCorrespondingContext):
        pass


    # Enter a parse tree produced by DNPParser#transactionStatement.
    def enterTransactionStatement(self, ctx:DNPParser.TransactionStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#transactionStatement.
    def exitTransactionStatement(self, ctx:DNPParser.TransactionStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#transactionBegin.
    def enterTransactionBegin(self, ctx:DNPParser.TransactionBeginContext):
        pass

    # Exit a parse tree produced by DNPParser#transactionBegin.
    def exitTransactionBegin(self, ctx:DNPParser.TransactionBeginContext):
        pass


    # Enter a parse tree produced by DNPParser#transactionCancel.
    def enterTransactionCancel(self, ctx:DNPParser.TransactionCancelContext):
        pass

    # Exit a parse tree produced by DNPParser#transactionCancel.
    def exitTransactionCancel(self, ctx:DNPParser.TransactionCancelContext):
        pass


    # Enter a parse tree produced by DNPParser#transactionEnd.
    def enterTransactionEnd(self, ctx:DNPParser.TransactionEndContext):
        pass

    # Exit a parse tree produced by DNPParser#transactionEnd.
    def exitTransactionEnd(self, ctx:DNPParser.TransactionEndContext):
        pass


    # Enter a parse tree produced by DNPParser#terminateStatement.
    def enterTerminateStatement(self, ctx:DNPParser.TerminateStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#terminateStatement.
    def exitTerminateStatement(self, ctx:DNPParser.TerminateStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#unstringStatement.
    def enterUnstringStatement(self, ctx:DNPParser.UnstringStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#unstringStatement.
    def exitUnstringStatement(self, ctx:DNPParser.UnstringStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#unstringSendingPhrase.
    def enterUnstringSendingPhrase(self, ctx:DNPParser.UnstringSendingPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#unstringSendingPhrase.
    def exitUnstringSendingPhrase(self, ctx:DNPParser.UnstringSendingPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#unstringDelimitedByPhrase.
    def enterUnstringDelimitedByPhrase(self, ctx:DNPParser.UnstringDelimitedByPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#unstringDelimitedByPhrase.
    def exitUnstringDelimitedByPhrase(self, ctx:DNPParser.UnstringDelimitedByPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#unstringOrAllPhrase.
    def enterUnstringOrAllPhrase(self, ctx:DNPParser.UnstringOrAllPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#unstringOrAllPhrase.
    def exitUnstringOrAllPhrase(self, ctx:DNPParser.UnstringOrAllPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#unstringIntoPhrase.
    def enterUnstringIntoPhrase(self, ctx:DNPParser.UnstringIntoPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#unstringIntoPhrase.
    def exitUnstringIntoPhrase(self, ctx:DNPParser.UnstringIntoPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#unstringInto.
    def enterUnstringInto(self, ctx:DNPParser.UnstringIntoContext):
        pass

    # Exit a parse tree produced by DNPParser#unstringInto.
    def exitUnstringInto(self, ctx:DNPParser.UnstringIntoContext):
        pass


    # Enter a parse tree produced by DNPParser#unstringDelimiterIn.
    def enterUnstringDelimiterIn(self, ctx:DNPParser.UnstringDelimiterInContext):
        pass

    # Exit a parse tree produced by DNPParser#unstringDelimiterIn.
    def exitUnstringDelimiterIn(self, ctx:DNPParser.UnstringDelimiterInContext):
        pass


    # Enter a parse tree produced by DNPParser#unstringCountIn.
    def enterUnstringCountIn(self, ctx:DNPParser.UnstringCountInContext):
        pass

    # Exit a parse tree produced by DNPParser#unstringCountIn.
    def exitUnstringCountIn(self, ctx:DNPParser.UnstringCountInContext):
        pass


    # Enter a parse tree produced by DNPParser#unstringWithPointerPhrase.
    def enterUnstringWithPointerPhrase(self, ctx:DNPParser.UnstringWithPointerPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#unstringWithPointerPhrase.
    def exitUnstringWithPointerPhrase(self, ctx:DNPParser.UnstringWithPointerPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#unstringTallyingPhrase.
    def enterUnstringTallyingPhrase(self, ctx:DNPParser.UnstringTallyingPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#unstringTallyingPhrase.
    def exitUnstringTallyingPhrase(self, ctx:DNPParser.UnstringTallyingPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#useStatement.
    def enterUseStatement(self, ctx:DNPParser.UseStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#useStatement.
    def exitUseStatement(self, ctx:DNPParser.UseStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#useAfterClause.
    def enterUseAfterClause(self, ctx:DNPParser.UseAfterClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#useAfterClause.
    def exitUseAfterClause(self, ctx:DNPParser.UseAfterClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#useAfterOn.
    def enterUseAfterOn(self, ctx:DNPParser.UseAfterOnContext):
        pass

    # Exit a parse tree produced by DNPParser#useAfterOn.
    def exitUseAfterOn(self, ctx:DNPParser.UseAfterOnContext):
        pass


    # Enter a parse tree produced by DNPParser#useDebugClause.
    def enterUseDebugClause(self, ctx:DNPParser.UseDebugClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#useDebugClause.
    def exitUseDebugClause(self, ctx:DNPParser.UseDebugClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#useDebugOn.
    def enterUseDebugOn(self, ctx:DNPParser.UseDebugOnContext):
        pass

    # Exit a parse tree produced by DNPParser#useDebugOn.
    def exitUseDebugOn(self, ctx:DNPParser.UseDebugOnContext):
        pass


    # Enter a parse tree produced by DNPParser#useDeadLock.
    def enterUseDeadLock(self, ctx:DNPParser.UseDeadLockContext):
        pass

    # Exit a parse tree produced by DNPParser#useDeadLock.
    def exitUseDeadLock(self, ctx:DNPParser.UseDeadLockContext):
        pass


    # Enter a parse tree produced by DNPParser#useProcedure.
    def enterUseProcedure(self, ctx:DNPParser.UseProcedureContext):
        pass

    # Exit a parse tree produced by DNPParser#useProcedure.
    def exitUseProcedure(self, ctx:DNPParser.UseProcedureContext):
        pass


    # Enter a parse tree produced by DNPParser#waitStatement.
    def enterWaitStatement(self, ctx:DNPParser.WaitStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#waitStatement.
    def exitWaitStatement(self, ctx:DNPParser.WaitStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#waitArithmeticExpression.
    def enterWaitArithmeticExpression(self, ctx:DNPParser.WaitArithmeticExpressionContext):
        pass

    # Exit a parse tree produced by DNPParser#waitArithmeticExpression.
    def exitWaitArithmeticExpression(self, ctx:DNPParser.WaitArithmeticExpressionContext):
        pass


    # Enter a parse tree produced by DNPParser#attributeChangeEvent.
    def enterAttributeChangeEvent(self, ctx:DNPParser.AttributeChangeEventContext):
        pass

    # Exit a parse tree produced by DNPParser#attributeChangeEvent.
    def exitAttributeChangeEvent(self, ctx:DNPParser.AttributeChangeEventContext):
        pass


    # Enter a parse tree produced by DNPParser#attributeInputEvent.
    def enterAttributeInputEvent(self, ctx:DNPParser.AttributeInputEventContext):
        pass

    # Exit a parse tree produced by DNPParser#attributeInputEvent.
    def exitAttributeInputEvent(self, ctx:DNPParser.AttributeInputEventContext):
        pass


    # Enter a parse tree produced by DNPParser#attributeOutputEvent.
    def enterAttributeOutputEvent(self, ctx:DNPParser.AttributeOutputEventContext):
        pass

    # Exit a parse tree produced by DNPParser#attributeOutputEvent.
    def exitAttributeOutputEvent(self, ctx:DNPParser.AttributeOutputEventContext):
        pass


    # Enter a parse tree produced by DNPParser#attributeAcceptEvent.
    def enterAttributeAcceptEvent(self, ctx:DNPParser.AttributeAcceptEventContext):
        pass

    # Exit a parse tree produced by DNPParser#attributeAcceptEvent.
    def exitAttributeAcceptEvent(self, ctx:DNPParser.AttributeAcceptEventContext):
        pass


    # Enter a parse tree produced by DNPParser#attributeExceptionEvent.
    def enterAttributeExceptionEvent(self, ctx:DNPParser.AttributeExceptionEventContext):
        pass

    # Exit a parse tree produced by DNPParser#attributeExceptionEvent.
    def exitAttributeExceptionEvent(self, ctx:DNPParser.AttributeExceptionEventContext):
        pass


    # Enter a parse tree produced by DNPParser#eventIdentifier.
    def enterEventIdentifier(self, ctx:DNPParser.EventIdentifierContext):
        pass

    # Exit a parse tree produced by DNPParser#eventIdentifier.
    def exitEventIdentifier(self, ctx:DNPParser.EventIdentifierContext):
        pass


    # Enter a parse tree produced by DNPParser#crcrEvent.
    def enterCrcrEvent(self, ctx:DNPParser.CrcrEventContext):
        pass

    # Exit a parse tree produced by DNPParser#crcrEvent.
    def exitCrcrEvent(self, ctx:DNPParser.CrcrEventContext):
        pass


    # Enter a parse tree produced by DNPParser#odtInputPresent.
    def enterOdtInputPresent(self, ctx:DNPParser.OdtInputPresentContext):
        pass

    # Exit a parse tree produced by DNPParser#odtInputPresent.
    def exitOdtInputPresent(self, ctx:DNPParser.OdtInputPresentContext):
        pass


    # Enter a parse tree produced by DNPParser#readOk.
    def enterReadOk(self, ctx:DNPParser.ReadOkContext):
        pass

    # Exit a parse tree produced by DNPParser#readOk.
    def exitReadOk(self, ctx:DNPParser.ReadOkContext):
        pass


    # Enter a parse tree produced by DNPParser#writeOk.
    def enterWriteOk(self, ctx:DNPParser.WriteOkContext):
        pass

    # Exit a parse tree produced by DNPParser#writeOk.
    def exitWriteOk(self, ctx:DNPParser.WriteOkContext):
        pass


    # Enter a parse tree produced by DNPParser#stoqEvent.
    def enterStoqEvent(self, ctx:DNPParser.StoqEventContext):
        pass

    # Exit a parse tree produced by DNPParser#stoqEvent.
    def exitStoqEvent(self, ctx:DNPParser.StoqEventContext):
        pass


    # Enter a parse tree produced by DNPParser#writeStatement.
    def enterWriteStatement(self, ctx:DNPParser.WriteStatementContext):
        pass

    # Exit a parse tree produced by DNPParser#writeStatement.
    def exitWriteStatement(self, ctx:DNPParser.WriteStatementContext):
        pass


    # Enter a parse tree produced by DNPParser#writeFromPhrase.
    def enterWriteFromPhrase(self, ctx:DNPParser.WriteFromPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#writeFromPhrase.
    def exitWriteFromPhrase(self, ctx:DNPParser.WriteFromPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#writeAdvancingPhrase.
    def enterWriteAdvancingPhrase(self, ctx:DNPParser.WriteAdvancingPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#writeAdvancingPhrase.
    def exitWriteAdvancingPhrase(self, ctx:DNPParser.WriteAdvancingPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#writeAdvancingPage.
    def enterWriteAdvancingPage(self, ctx:DNPParser.WriteAdvancingPageContext):
        pass

    # Exit a parse tree produced by DNPParser#writeAdvancingPage.
    def exitWriteAdvancingPage(self, ctx:DNPParser.WriteAdvancingPageContext):
        pass


    # Enter a parse tree produced by DNPParser#writeAdvancingLines.
    def enterWriteAdvancingLines(self, ctx:DNPParser.WriteAdvancingLinesContext):
        pass

    # Exit a parse tree produced by DNPParser#writeAdvancingLines.
    def exitWriteAdvancingLines(self, ctx:DNPParser.WriteAdvancingLinesContext):
        pass


    # Enter a parse tree produced by DNPParser#writeAdvancingMnemonic.
    def enterWriteAdvancingMnemonic(self, ctx:DNPParser.WriteAdvancingMnemonicContext):
        pass

    # Exit a parse tree produced by DNPParser#writeAdvancingMnemonic.
    def exitWriteAdvancingMnemonic(self, ctx:DNPParser.WriteAdvancingMnemonicContext):
        pass


    # Enter a parse tree produced by DNPParser#writeAtEndOfPagePhrase.
    def enterWriteAtEndOfPagePhrase(self, ctx:DNPParser.WriteAtEndOfPagePhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#writeAtEndOfPagePhrase.
    def exitWriteAtEndOfPagePhrase(self, ctx:DNPParser.WriteAtEndOfPagePhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#writeNotAtEndOfPagePhrase.
    def enterWriteNotAtEndOfPagePhrase(self, ctx:DNPParser.WriteNotAtEndOfPagePhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#writeNotAtEndOfPagePhrase.
    def exitWriteNotAtEndOfPagePhrase(self, ctx:DNPParser.WriteNotAtEndOfPagePhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#atEndPhrase.
    def enterAtEndPhrase(self, ctx:DNPParser.AtEndPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#atEndPhrase.
    def exitAtEndPhrase(self, ctx:DNPParser.AtEndPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#notAtEndPhrase.
    def enterNotAtEndPhrase(self, ctx:DNPParser.NotAtEndPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#notAtEndPhrase.
    def exitNotAtEndPhrase(self, ctx:DNPParser.NotAtEndPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#invalidKeyPhrase.
    def enterInvalidKeyPhrase(self, ctx:DNPParser.InvalidKeyPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#invalidKeyPhrase.
    def exitInvalidKeyPhrase(self, ctx:DNPParser.InvalidKeyPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#notInvalidKeyPhrase.
    def enterNotInvalidKeyPhrase(self, ctx:DNPParser.NotInvalidKeyPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#notInvalidKeyPhrase.
    def exitNotInvalidKeyPhrase(self, ctx:DNPParser.NotInvalidKeyPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#onOverflowPhrase.
    def enterOnOverflowPhrase(self, ctx:DNPParser.OnOverflowPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#onOverflowPhrase.
    def exitOnOverflowPhrase(self, ctx:DNPParser.OnOverflowPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#notOnOverflowPhrase.
    def enterNotOnOverflowPhrase(self, ctx:DNPParser.NotOnOverflowPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#notOnOverflowPhrase.
    def exitNotOnOverflowPhrase(self, ctx:DNPParser.NotOnOverflowPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#onSizeErrorPhrase.
    def enterOnSizeErrorPhrase(self, ctx:DNPParser.OnSizeErrorPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#onSizeErrorPhrase.
    def exitOnSizeErrorPhrase(self, ctx:DNPParser.OnSizeErrorPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#notOnSizeErrorPhrase.
    def enterNotOnSizeErrorPhrase(self, ctx:DNPParser.NotOnSizeErrorPhraseContext):
        pass

    # Exit a parse tree produced by DNPParser#notOnSizeErrorPhrase.
    def exitNotOnSizeErrorPhrase(self, ctx:DNPParser.NotOnSizeErrorPhraseContext):
        pass


    # Enter a parse tree produced by DNPParser#onExceptionClause.
    def enterOnExceptionClause(self, ctx:DNPParser.OnExceptionClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#onExceptionClause.
    def exitOnExceptionClause(self, ctx:DNPParser.OnExceptionClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#notOnExceptionClause.
    def enterNotOnExceptionClause(self, ctx:DNPParser.NotOnExceptionClauseContext):
        pass

    # Exit a parse tree produced by DNPParser#notOnExceptionClause.
    def exitNotOnExceptionClause(self, ctx:DNPParser.NotOnExceptionClauseContext):
        pass


    # Enter a parse tree produced by DNPParser#arithmeticExpression.
    def enterArithmeticExpression(self, ctx:DNPParser.ArithmeticExpressionContext):
        pass

    # Exit a parse tree produced by DNPParser#arithmeticExpression.
    def exitArithmeticExpression(self, ctx:DNPParser.ArithmeticExpressionContext):
        pass


    # Enter a parse tree produced by DNPParser#plusMinus.
    def enterPlusMinus(self, ctx:DNPParser.PlusMinusContext):
        pass

    # Exit a parse tree produced by DNPParser#plusMinus.
    def exitPlusMinus(self, ctx:DNPParser.PlusMinusContext):
        pass


    # Enter a parse tree produced by DNPParser#multDivs.
    def enterMultDivs(self, ctx:DNPParser.MultDivsContext):
        pass

    # Exit a parse tree produced by DNPParser#multDivs.
    def exitMultDivs(self, ctx:DNPParser.MultDivsContext):
        pass


    # Enter a parse tree produced by DNPParser#multDiv.
    def enterMultDiv(self, ctx:DNPParser.MultDivContext):
        pass

    # Exit a parse tree produced by DNPParser#multDiv.
    def exitMultDiv(self, ctx:DNPParser.MultDivContext):
        pass


    # Enter a parse tree produced by DNPParser#powers.
    def enterPowers(self, ctx:DNPParser.PowersContext):
        pass

    # Exit a parse tree produced by DNPParser#powers.
    def exitPowers(self, ctx:DNPParser.PowersContext):
        pass


    # Enter a parse tree produced by DNPParser#power.
    def enterPower(self, ctx:DNPParser.PowerContext):
        pass

    # Exit a parse tree produced by DNPParser#power.
    def exitPower(self, ctx:DNPParser.PowerContext):
        pass


    # Enter a parse tree produced by DNPParser#basis.
    def enterBasis(self, ctx:DNPParser.BasisContext):
        pass

    # Exit a parse tree produced by DNPParser#basis.
    def exitBasis(self, ctx:DNPParser.BasisContext):
        pass


    # Enter a parse tree produced by DNPParser#condition.
    def enterCondition(self, ctx:DNPParser.ConditionContext):
        pass

    # Exit a parse tree produced by DNPParser#condition.
    def exitCondition(self, ctx:DNPParser.ConditionContext):
        pass


    # Enter a parse tree produced by DNPParser#andOrCondition.
    def enterAndOrCondition(self, ctx:DNPParser.AndOrConditionContext):
        pass

    # Exit a parse tree produced by DNPParser#andOrCondition.
    def exitAndOrCondition(self, ctx:DNPParser.AndOrConditionContext):
        pass


    # Enter a parse tree produced by DNPParser#combinableCondition.
    def enterCombinableCondition(self, ctx:DNPParser.CombinableConditionContext):
        pass

    # Exit a parse tree produced by DNPParser#combinableCondition.
    def exitCombinableCondition(self, ctx:DNPParser.CombinableConditionContext):
        pass


    # Enter a parse tree produced by DNPParser#simpleCondition.
    def enterSimpleCondition(self, ctx:DNPParser.SimpleConditionContext):
        pass

    # Exit a parse tree produced by DNPParser#simpleCondition.
    def exitSimpleCondition(self, ctx:DNPParser.SimpleConditionContext):
        pass


    # Enter a parse tree produced by DNPParser#classCondition.
    def enterClassCondition(self, ctx:DNPParser.ClassConditionContext):
        pass

    # Exit a parse tree produced by DNPParser#classCondition.
    def exitClassCondition(self, ctx:DNPParser.ClassConditionContext):
        pass


    # Enter a parse tree produced by DNPParser#conditionNameReference.
    def enterConditionNameReference(self, ctx:DNPParser.ConditionNameReferenceContext):
        pass

    # Exit a parse tree produced by DNPParser#conditionNameReference.
    def exitConditionNameReference(self, ctx:DNPParser.ConditionNameReferenceContext):
        pass


    # Enter a parse tree produced by DNPParser#conditionNameSubscriptReference.
    def enterConditionNameSubscriptReference(self, ctx:DNPParser.ConditionNameSubscriptReferenceContext):
        pass

    # Exit a parse tree produced by DNPParser#conditionNameSubscriptReference.
    def exitConditionNameSubscriptReference(self, ctx:DNPParser.ConditionNameSubscriptReferenceContext):
        pass


    # Enter a parse tree produced by DNPParser#attributeCondition.
    def enterAttributeCondition(self, ctx:DNPParser.AttributeConditionContext):
        pass

    # Exit a parse tree produced by DNPParser#attributeCondition.
    def exitAttributeCondition(self, ctx:DNPParser.AttributeConditionContext):
        pass


    # Enter a parse tree produced by DNPParser#attributeConditionExpr.
    def enterAttributeConditionExpr(self, ctx:DNPParser.AttributeConditionExprContext):
        pass

    # Exit a parse tree produced by DNPParser#attributeConditionExpr.
    def exitAttributeConditionExpr(self, ctx:DNPParser.AttributeConditionExprContext):
        pass


    # Enter a parse tree produced by DNPParser#relationCondition.
    def enterRelationCondition(self, ctx:DNPParser.RelationConditionContext):
        pass

    # Exit a parse tree produced by DNPParser#relationCondition.
    def exitRelationCondition(self, ctx:DNPParser.RelationConditionContext):
        pass


    # Enter a parse tree produced by DNPParser#relationSignCondition.
    def enterRelationSignCondition(self, ctx:DNPParser.RelationSignConditionContext):
        pass

    # Exit a parse tree produced by DNPParser#relationSignCondition.
    def exitRelationSignCondition(self, ctx:DNPParser.RelationSignConditionContext):
        pass


    # Enter a parse tree produced by DNPParser#relationArithmeticComparison.
    def enterRelationArithmeticComparison(self, ctx:DNPParser.RelationArithmeticComparisonContext):
        pass

    # Exit a parse tree produced by DNPParser#relationArithmeticComparison.
    def exitRelationArithmeticComparison(self, ctx:DNPParser.RelationArithmeticComparisonContext):
        pass


    # Enter a parse tree produced by DNPParser#relationCombinedComparison.
    def enterRelationCombinedComparison(self, ctx:DNPParser.RelationCombinedComparisonContext):
        pass

    # Exit a parse tree produced by DNPParser#relationCombinedComparison.
    def exitRelationCombinedComparison(self, ctx:DNPParser.RelationCombinedComparisonContext):
        pass


    # Enter a parse tree produced by DNPParser#relationCombinedCondition.
    def enterRelationCombinedCondition(self, ctx:DNPParser.RelationCombinedConditionContext):
        pass

    # Exit a parse tree produced by DNPParser#relationCombinedCondition.
    def exitRelationCombinedCondition(self, ctx:DNPParser.RelationCombinedConditionContext):
        pass


    # Enter a parse tree produced by DNPParser#relationalOperator.
    def enterRelationalOperator(self, ctx:DNPParser.RelationalOperatorContext):
        pass

    # Exit a parse tree produced by DNPParser#relationalOperator.
    def exitRelationalOperator(self, ctx:DNPParser.RelationalOperatorContext):
        pass


    # Enter a parse tree produced by DNPParser#abbreviation.
    def enterAbbreviation(self, ctx:DNPParser.AbbreviationContext):
        pass

    # Exit a parse tree produced by DNPParser#abbreviation.
    def exitAbbreviation(self, ctx:DNPParser.AbbreviationContext):
        pass


    # Enter a parse tree produced by DNPParser#identifier.
    def enterIdentifier(self, ctx:DNPParser.IdentifierContext):
        pass

    # Exit a parse tree produced by DNPParser#identifier.
    def exitIdentifier(self, ctx:DNPParser.IdentifierContext):
        pass


    # Enter a parse tree produced by DNPParser#tableCall.
    def enterTableCall(self, ctx:DNPParser.TableCallContext):
        pass

    # Exit a parse tree produced by DNPParser#tableCall.
    def exitTableCall(self, ctx:DNPParser.TableCallContext):
        pass


    # Enter a parse tree produced by DNPParser#functionCall.
    def enterFunctionCall(self, ctx:DNPParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by DNPParser#functionCall.
    def exitFunctionCall(self, ctx:DNPParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by DNPParser#referenceModifier.
    def enterReferenceModifier(self, ctx:DNPParser.ReferenceModifierContext):
        pass

    # Exit a parse tree produced by DNPParser#referenceModifier.
    def exitReferenceModifier(self, ctx:DNPParser.ReferenceModifierContext):
        pass


    # Enter a parse tree produced by DNPParser#characterPosition.
    def enterCharacterPosition(self, ctx:DNPParser.CharacterPositionContext):
        pass

    # Exit a parse tree produced by DNPParser#characterPosition.
    def exitCharacterPosition(self, ctx:DNPParser.CharacterPositionContext):
        pass


    # Enter a parse tree produced by DNPParser#length.
    def enterLength(self, ctx:DNPParser.LengthContext):
        pass

    # Exit a parse tree produced by DNPParser#length.
    def exitLength(self, ctx:DNPParser.LengthContext):
        pass


    # Enter a parse tree produced by DNPParser#subscript_.
    def enterSubscript_(self, ctx:DNPParser.Subscript_Context):
        pass

    # Exit a parse tree produced by DNPParser#subscript_.
    def exitSubscript_(self, ctx:DNPParser.Subscript_Context):
        pass


    # Enter a parse tree produced by DNPParser#argument.
    def enterArgument(self, ctx:DNPParser.ArgumentContext):
        pass

    # Exit a parse tree produced by DNPParser#argument.
    def exitArgument(self, ctx:DNPParser.ArgumentContext):
        pass


    # Enter a parse tree produced by DNPParser#qualifiedDataName.
    def enterQualifiedDataName(self, ctx:DNPParser.QualifiedDataNameContext):
        pass

    # Exit a parse tree produced by DNPParser#qualifiedDataName.
    def exitQualifiedDataName(self, ctx:DNPParser.QualifiedDataNameContext):
        pass


    # Enter a parse tree produced by DNPParser#qualifiedDataNameFormat1.
    def enterQualifiedDataNameFormat1(self, ctx:DNPParser.QualifiedDataNameFormat1Context):
        pass

    # Exit a parse tree produced by DNPParser#qualifiedDataNameFormat1.
    def exitQualifiedDataNameFormat1(self, ctx:DNPParser.QualifiedDataNameFormat1Context):
        pass


    # Enter a parse tree produced by DNPParser#qualifiedDataNameFormat2.
    def enterQualifiedDataNameFormat2(self, ctx:DNPParser.QualifiedDataNameFormat2Context):
        pass

    # Exit a parse tree produced by DNPParser#qualifiedDataNameFormat2.
    def exitQualifiedDataNameFormat2(self, ctx:DNPParser.QualifiedDataNameFormat2Context):
        pass


    # Enter a parse tree produced by DNPParser#qualifiedDataNameFormat3.
    def enterQualifiedDataNameFormat3(self, ctx:DNPParser.QualifiedDataNameFormat3Context):
        pass

    # Exit a parse tree produced by DNPParser#qualifiedDataNameFormat3.
    def exitQualifiedDataNameFormat3(self, ctx:DNPParser.QualifiedDataNameFormat3Context):
        pass


    # Enter a parse tree produced by DNPParser#qualifiedDataNameFormat4.
    def enterQualifiedDataNameFormat4(self, ctx:DNPParser.QualifiedDataNameFormat4Context):
        pass

    # Exit a parse tree produced by DNPParser#qualifiedDataNameFormat4.
    def exitQualifiedDataNameFormat4(self, ctx:DNPParser.QualifiedDataNameFormat4Context):
        pass


    # Enter a parse tree produced by DNPParser#qualifiedInData.
    def enterQualifiedInData(self, ctx:DNPParser.QualifiedInDataContext):
        pass

    # Exit a parse tree produced by DNPParser#qualifiedInData.
    def exitQualifiedInData(self, ctx:DNPParser.QualifiedInDataContext):
        pass


    # Enter a parse tree produced by DNPParser#inData.
    def enterInData(self, ctx:DNPParser.InDataContext):
        pass

    # Exit a parse tree produced by DNPParser#inData.
    def exitInData(self, ctx:DNPParser.InDataContext):
        pass


    # Enter a parse tree produced by DNPParser#inFile.
    def enterInFile(self, ctx:DNPParser.InFileContext):
        pass

    # Exit a parse tree produced by DNPParser#inFile.
    def exitInFile(self, ctx:DNPParser.InFileContext):
        pass


    # Enter a parse tree produced by DNPParser#inMnemonic.
    def enterInMnemonic(self, ctx:DNPParser.InMnemonicContext):
        pass

    # Exit a parse tree produced by DNPParser#inMnemonic.
    def exitInMnemonic(self, ctx:DNPParser.InMnemonicContext):
        pass


    # Enter a parse tree produced by DNPParser#inSection.
    def enterInSection(self, ctx:DNPParser.InSectionContext):
        pass

    # Exit a parse tree produced by DNPParser#inSection.
    def exitInSection(self, ctx:DNPParser.InSectionContext):
        pass


    # Enter a parse tree produced by DNPParser#inLibrary.
    def enterInLibrary(self, ctx:DNPParser.InLibraryContext):
        pass

    # Exit a parse tree produced by DNPParser#inLibrary.
    def exitInLibrary(self, ctx:DNPParser.InLibraryContext):
        pass


    # Enter a parse tree produced by DNPParser#inTable.
    def enterInTable(self, ctx:DNPParser.InTableContext):
        pass

    # Exit a parse tree produced by DNPParser#inTable.
    def exitInTable(self, ctx:DNPParser.InTableContext):
        pass


    # Enter a parse tree produced by DNPParser#alphabetName.
    def enterAlphabetName(self, ctx:DNPParser.AlphabetNameContext):
        pass

    # Exit a parse tree produced by DNPParser#alphabetName.
    def exitAlphabetName(self, ctx:DNPParser.AlphabetNameContext):
        pass


    # Enter a parse tree produced by DNPParser#assignmentName.
    def enterAssignmentName(self, ctx:DNPParser.AssignmentNameContext):
        pass

    # Exit a parse tree produced by DNPParser#assignmentName.
    def exitAssignmentName(self, ctx:DNPParser.AssignmentNameContext):
        pass


    # Enter a parse tree produced by DNPParser#basisName.
    def enterBasisName(self, ctx:DNPParser.BasisNameContext):
        pass

    # Exit a parse tree produced by DNPParser#basisName.
    def exitBasisName(self, ctx:DNPParser.BasisNameContext):
        pass


    # Enter a parse tree produced by DNPParser#cdName.
    def enterCdName(self, ctx:DNPParser.CdNameContext):
        pass

    # Exit a parse tree produced by DNPParser#cdName.
    def exitCdName(self, ctx:DNPParser.CdNameContext):
        pass


    # Enter a parse tree produced by DNPParser#className.
    def enterClassName(self, ctx:DNPParser.ClassNameContext):
        pass

    # Exit a parse tree produced by DNPParser#className.
    def exitClassName(self, ctx:DNPParser.ClassNameContext):
        pass


    # Enter a parse tree produced by DNPParser#computerName.
    def enterComputerName(self, ctx:DNPParser.ComputerNameContext):
        pass

    # Exit a parse tree produced by DNPParser#computerName.
    def exitComputerName(self, ctx:DNPParser.ComputerNameContext):
        pass


    # Enter a parse tree produced by DNPParser#conditionName.
    def enterConditionName(self, ctx:DNPParser.ConditionNameContext):
        pass

    # Exit a parse tree produced by DNPParser#conditionName.
    def exitConditionName(self, ctx:DNPParser.ConditionNameContext):
        pass


    # Enter a parse tree produced by DNPParser#dataName.
    def enterDataName(self, ctx:DNPParser.DataNameContext):
        pass

    # Exit a parse tree produced by DNPParser#dataName.
    def exitDataName(self, ctx:DNPParser.DataNameContext):
        pass


    # Enter a parse tree produced by DNPParser#dataDescName.
    def enterDataDescName(self, ctx:DNPParser.DataDescNameContext):
        pass

    # Exit a parse tree produced by DNPParser#dataDescName.
    def exitDataDescName(self, ctx:DNPParser.DataDescNameContext):
        pass


    # Enter a parse tree produced by DNPParser#environmentName.
    def enterEnvironmentName(self, ctx:DNPParser.EnvironmentNameContext):
        pass

    # Exit a parse tree produced by DNPParser#environmentName.
    def exitEnvironmentName(self, ctx:DNPParser.EnvironmentNameContext):
        pass


    # Enter a parse tree produced by DNPParser#fileAttribute.
    def enterFileAttribute(self, ctx:DNPParser.FileAttributeContext):
        pass

    # Exit a parse tree produced by DNPParser#fileAttribute.
    def exitFileAttribute(self, ctx:DNPParser.FileAttributeContext):
        pass


    # Enter a parse tree produced by DNPParser#fileName.
    def enterFileName(self, ctx:DNPParser.FileNameContext):
        pass

    # Exit a parse tree produced by DNPParser#fileName.
    def exitFileName(self, ctx:DNPParser.FileNameContext):
        pass


    # Enter a parse tree produced by DNPParser#functionName.
    def enterFunctionName(self, ctx:DNPParser.FunctionNameContext):
        pass

    # Exit a parse tree produced by DNPParser#functionName.
    def exitFunctionName(self, ctx:DNPParser.FunctionNameContext):
        pass


    # Enter a parse tree produced by DNPParser#indexName.
    def enterIndexName(self, ctx:DNPParser.IndexNameContext):
        pass

    # Exit a parse tree produced by DNPParser#indexName.
    def exitIndexName(self, ctx:DNPParser.IndexNameContext):
        pass


    # Enter a parse tree produced by DNPParser#languageName.
    def enterLanguageName(self, ctx:DNPParser.LanguageNameContext):
        pass

    # Exit a parse tree produced by DNPParser#languageName.
    def exitLanguageName(self, ctx:DNPParser.LanguageNameContext):
        pass


    # Enter a parse tree produced by DNPParser#libraryName.
    def enterLibraryName(self, ctx:DNPParser.LibraryNameContext):
        pass

    # Exit a parse tree produced by DNPParser#libraryName.
    def exitLibraryName(self, ctx:DNPParser.LibraryNameContext):
        pass


    # Enter a parse tree produced by DNPParser#localName.
    def enterLocalName(self, ctx:DNPParser.LocalNameContext):
        pass

    # Exit a parse tree produced by DNPParser#localName.
    def exitLocalName(self, ctx:DNPParser.LocalNameContext):
        pass


    # Enter a parse tree produced by DNPParser#mnemonicName.
    def enterMnemonicName(self, ctx:DNPParser.MnemonicNameContext):
        pass

    # Exit a parse tree produced by DNPParser#mnemonicName.
    def exitMnemonicName(self, ctx:DNPParser.MnemonicNameContext):
        pass


    # Enter a parse tree produced by DNPParser#paragraphName.
    def enterParagraphName(self, ctx:DNPParser.ParagraphNameContext):
        pass

    # Exit a parse tree produced by DNPParser#paragraphName.
    def exitParagraphName(self, ctx:DNPParser.ParagraphNameContext):
        pass


    # Enter a parse tree produced by DNPParser#procedureName.
    def enterProcedureName(self, ctx:DNPParser.ProcedureNameContext):
        pass

    # Exit a parse tree produced by DNPParser#procedureName.
    def exitProcedureName(self, ctx:DNPParser.ProcedureNameContext):
        pass


    # Enter a parse tree produced by DNPParser#programName.
    def enterProgramName(self, ctx:DNPParser.ProgramNameContext):
        pass

    # Exit a parse tree produced by DNPParser#programName.
    def exitProgramName(self, ctx:DNPParser.ProgramNameContext):
        pass


    # Enter a parse tree produced by DNPParser#recordName.
    def enterRecordName(self, ctx:DNPParser.RecordNameContext):
        pass

    # Exit a parse tree produced by DNPParser#recordName.
    def exitRecordName(self, ctx:DNPParser.RecordNameContext):
        pass


    # Enter a parse tree produced by DNPParser#reportName.
    def enterReportName(self, ctx:DNPParser.ReportNameContext):
        pass

    # Exit a parse tree produced by DNPParser#reportName.
    def exitReportName(self, ctx:DNPParser.ReportNameContext):
        pass


    # Enter a parse tree produced by DNPParser#routineName.
    def enterRoutineName(self, ctx:DNPParser.RoutineNameContext):
        pass

    # Exit a parse tree produced by DNPParser#routineName.
    def exitRoutineName(self, ctx:DNPParser.RoutineNameContext):
        pass


    # Enter a parse tree produced by DNPParser#screenName.
    def enterScreenName(self, ctx:DNPParser.ScreenNameContext):
        pass

    # Exit a parse tree produced by DNPParser#screenName.
    def exitScreenName(self, ctx:DNPParser.ScreenNameContext):
        pass


    # Enter a parse tree produced by DNPParser#sectionName.
    def enterSectionName(self, ctx:DNPParser.SectionNameContext):
        pass

    # Exit a parse tree produced by DNPParser#sectionName.
    def exitSectionName(self, ctx:DNPParser.SectionNameContext):
        pass


    # Enter a parse tree produced by DNPParser#systemName.
    def enterSystemName(self, ctx:DNPParser.SystemNameContext):
        pass

    # Exit a parse tree produced by DNPParser#systemName.
    def exitSystemName(self, ctx:DNPParser.SystemNameContext):
        pass


    # Enter a parse tree produced by DNPParser#symbolicCharacter.
    def enterSymbolicCharacter(self, ctx:DNPParser.SymbolicCharacterContext):
        pass

    # Exit a parse tree produced by DNPParser#symbolicCharacter.
    def exitSymbolicCharacter(self, ctx:DNPParser.SymbolicCharacterContext):
        pass


    # Enter a parse tree produced by DNPParser#textName.
    def enterTextName(self, ctx:DNPParser.TextNameContext):
        pass

    # Exit a parse tree produced by DNPParser#textName.
    def exitTextName(self, ctx:DNPParser.TextNameContext):
        pass


    # Enter a parse tree produced by DNPParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:DNPParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by DNPParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:DNPParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by DNPParser#numericLiteral.
    def enterNumericLiteral(self, ctx:DNPParser.NumericLiteralContext):
        pass

    # Exit a parse tree produced by DNPParser#numericLiteral.
    def exitNumericLiteral(self, ctx:DNPParser.NumericLiteralContext):
        pass


    # Enter a parse tree produced by DNPParser#integerLiteral.
    def enterIntegerLiteral(self, ctx:DNPParser.IntegerLiteralContext):
        pass

    # Exit a parse tree produced by DNPParser#integerLiteral.
    def exitIntegerLiteral(self, ctx:DNPParser.IntegerLiteralContext):
        pass


    # Enter a parse tree produced by DNPParser#cicsDfhRespLiteral.
    def enterCicsDfhRespLiteral(self, ctx:DNPParser.CicsDfhRespLiteralContext):
        pass

    # Exit a parse tree produced by DNPParser#cicsDfhRespLiteral.
    def exitCicsDfhRespLiteral(self, ctx:DNPParser.CicsDfhRespLiteralContext):
        pass


    # Enter a parse tree produced by DNPParser#cicsDfhValueLiteral.
    def enterCicsDfhValueLiteral(self, ctx:DNPParser.CicsDfhValueLiteralContext):
        pass

    # Exit a parse tree produced by DNPParser#cicsDfhValueLiteral.
    def exitCicsDfhValueLiteral(self, ctx:DNPParser.CicsDfhValueLiteralContext):
        pass


    # Enter a parse tree produced by DNPParser#figurativeConstant.
    def enterFigurativeConstant(self, ctx:DNPParser.FigurativeConstantContext):
        pass

    # Exit a parse tree produced by DNPParser#figurativeConstant.
    def exitFigurativeConstant(self, ctx:DNPParser.FigurativeConstantContext):
        pass


    # Enter a parse tree produced by DNPParser#specialRegister.
    def enterSpecialRegister(self, ctx:DNPParser.SpecialRegisterContext):
        pass

    # Exit a parse tree produced by DNPParser#specialRegister.
    def exitSpecialRegister(self, ctx:DNPParser.SpecialRegisterContext):
        pass


    # Enter a parse tree produced by DNPParser#commentEntry.
    def enterCommentEntry(self, ctx:DNPParser.CommentEntryContext):
        pass

    # Exit a parse tree produced by DNPParser#commentEntry.
    def exitCommentEntry(self, ctx:DNPParser.CommentEntryContext):
        pass


    # Enter a parse tree produced by DNPParser#charDataKeyword.
    def enterCharDataKeyword(self, ctx:DNPParser.CharDataKeywordContext):
        pass

    # Exit a parse tree produced by DNPParser#charDataKeyword.
    def exitCharDataKeyword(self, ctx:DNPParser.CharDataKeywordContext):
        pass



del DNPParser