# Generated from grammar/copybook/CopyBook.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CopyBookParser import CopyBookParser
else:
    from CopyBookParser import CopyBookParser

# This class defines a complete listener for a parse tree produced by CopyBookParser.
class CopyBookListener(ParseTreeListener):

    # Enter a parse tree produced by CopyBookParser#startRule.
    def enterStartRule(self, ctx:CopyBookParser.StartRuleContext):
        pass

    # Exit a parse tree produced by CopyBookParser#startRule.
    def exitStartRule(self, ctx:CopyBookParser.StartRuleContext):
        pass


    # Enter a parse tree produced by CopyBookParser#compilationUnit.
    def enterCompilationUnit(self, ctx:CopyBookParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by CopyBookParser#compilationUnit.
    def exitCompilationUnit(self, ctx:CopyBookParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by CopyBookParser#programUnit.
    def enterProgramUnit(self, ctx:CopyBookParser.ProgramUnitContext):
        pass

    # Exit a parse tree produced by CopyBookParser#programUnit.
    def exitProgramUnit(self, ctx:CopyBookParser.ProgramUnitContext):
        pass


    # Enter a parse tree produced by CopyBookParser#endProgramStatement.
    def enterEndProgramStatement(self, ctx:CopyBookParser.EndProgramStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#endProgramStatement.
    def exitEndProgramStatement(self, ctx:CopyBookParser.EndProgramStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#identificationDivision.
    def enterIdentificationDivision(self, ctx:CopyBookParser.IdentificationDivisionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#identificationDivision.
    def exitIdentificationDivision(self, ctx:CopyBookParser.IdentificationDivisionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#identificationDivisionBody.
    def enterIdentificationDivisionBody(self, ctx:CopyBookParser.IdentificationDivisionBodyContext):
        pass

    # Exit a parse tree produced by CopyBookParser#identificationDivisionBody.
    def exitIdentificationDivisionBody(self, ctx:CopyBookParser.IdentificationDivisionBodyContext):
        pass


    # Enter a parse tree produced by CopyBookParser#programIdParagraph.
    def enterProgramIdParagraph(self, ctx:CopyBookParser.ProgramIdParagraphContext):
        pass

    # Exit a parse tree produced by CopyBookParser#programIdParagraph.
    def exitProgramIdParagraph(self, ctx:CopyBookParser.ProgramIdParagraphContext):
        pass


    # Enter a parse tree produced by CopyBookParser#author_name.
    def enterAuthor_name(self, ctx:CopyBookParser.Author_nameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#author_name.
    def exitAuthor_name(self, ctx:CopyBookParser.Author_nameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#authorParagraph.
    def enterAuthorParagraph(self, ctx:CopyBookParser.AuthorParagraphContext):
        pass

    # Exit a parse tree produced by CopyBookParser#authorParagraph.
    def exitAuthorParagraph(self, ctx:CopyBookParser.AuthorParagraphContext):
        pass


    # Enter a parse tree produced by CopyBookParser#installationParagraph.
    def enterInstallationParagraph(self, ctx:CopyBookParser.InstallationParagraphContext):
        pass

    # Exit a parse tree produced by CopyBookParser#installationParagraph.
    def exitInstallationParagraph(self, ctx:CopyBookParser.InstallationParagraphContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dateWrittenParagraph.
    def enterDateWrittenParagraph(self, ctx:CopyBookParser.DateWrittenParagraphContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dateWrittenParagraph.
    def exitDateWrittenParagraph(self, ctx:CopyBookParser.DateWrittenParagraphContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dateCompiledParagraph.
    def enterDateCompiledParagraph(self, ctx:CopyBookParser.DateCompiledParagraphContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dateCompiledParagraph.
    def exitDateCompiledParagraph(self, ctx:CopyBookParser.DateCompiledParagraphContext):
        pass


    # Enter a parse tree produced by CopyBookParser#securityParagraph.
    def enterSecurityParagraph(self, ctx:CopyBookParser.SecurityParagraphContext):
        pass

    # Exit a parse tree produced by CopyBookParser#securityParagraph.
    def exitSecurityParagraph(self, ctx:CopyBookParser.SecurityParagraphContext):
        pass


    # Enter a parse tree produced by CopyBookParser#remarksParagraph.
    def enterRemarksParagraph(self, ctx:CopyBookParser.RemarksParagraphContext):
        pass

    # Exit a parse tree produced by CopyBookParser#remarksParagraph.
    def exitRemarksParagraph(self, ctx:CopyBookParser.RemarksParagraphContext):
        pass


    # Enter a parse tree produced by CopyBookParser#environmentDivision.
    def enterEnvironmentDivision(self, ctx:CopyBookParser.EnvironmentDivisionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#environmentDivision.
    def exitEnvironmentDivision(self, ctx:CopyBookParser.EnvironmentDivisionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#environmentDivisionBody.
    def enterEnvironmentDivisionBody(self, ctx:CopyBookParser.EnvironmentDivisionBodyContext):
        pass

    # Exit a parse tree produced by CopyBookParser#environmentDivisionBody.
    def exitEnvironmentDivisionBody(self, ctx:CopyBookParser.EnvironmentDivisionBodyContext):
        pass


    # Enter a parse tree produced by CopyBookParser#configurationSection.
    def enterConfigurationSection(self, ctx:CopyBookParser.ConfigurationSectionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#configurationSection.
    def exitConfigurationSection(self, ctx:CopyBookParser.ConfigurationSectionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#configurationSectionParagraph.
    def enterConfigurationSectionParagraph(self, ctx:CopyBookParser.ConfigurationSectionParagraphContext):
        pass

    # Exit a parse tree produced by CopyBookParser#configurationSectionParagraph.
    def exitConfigurationSectionParagraph(self, ctx:CopyBookParser.ConfigurationSectionParagraphContext):
        pass


    # Enter a parse tree produced by CopyBookParser#sourceComputerParagraph.
    def enterSourceComputerParagraph(self, ctx:CopyBookParser.SourceComputerParagraphContext):
        pass

    # Exit a parse tree produced by CopyBookParser#sourceComputerParagraph.
    def exitSourceComputerParagraph(self, ctx:CopyBookParser.SourceComputerParagraphContext):
        pass


    # Enter a parse tree produced by CopyBookParser#objectComputerParagraph.
    def enterObjectComputerParagraph(self, ctx:CopyBookParser.ObjectComputerParagraphContext):
        pass

    # Exit a parse tree produced by CopyBookParser#objectComputerParagraph.
    def exitObjectComputerParagraph(self, ctx:CopyBookParser.ObjectComputerParagraphContext):
        pass


    # Enter a parse tree produced by CopyBookParser#objectComputerClause.
    def enterObjectComputerClause(self, ctx:CopyBookParser.ObjectComputerClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#objectComputerClause.
    def exitObjectComputerClause(self, ctx:CopyBookParser.ObjectComputerClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#memorySizeClause.
    def enterMemorySizeClause(self, ctx:CopyBookParser.MemorySizeClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#memorySizeClause.
    def exitMemorySizeClause(self, ctx:CopyBookParser.MemorySizeClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#diskSizeClause.
    def enterDiskSizeClause(self, ctx:CopyBookParser.DiskSizeClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#diskSizeClause.
    def exitDiskSizeClause(self, ctx:CopyBookParser.DiskSizeClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#collatingSequenceClause.
    def enterCollatingSequenceClause(self, ctx:CopyBookParser.CollatingSequenceClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#collatingSequenceClause.
    def exitCollatingSequenceClause(self, ctx:CopyBookParser.CollatingSequenceClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#collatingSequenceClauseAlphanumeric.
    def enterCollatingSequenceClauseAlphanumeric(self, ctx:CopyBookParser.CollatingSequenceClauseAlphanumericContext):
        pass

    # Exit a parse tree produced by CopyBookParser#collatingSequenceClauseAlphanumeric.
    def exitCollatingSequenceClauseAlphanumeric(self, ctx:CopyBookParser.CollatingSequenceClauseAlphanumericContext):
        pass


    # Enter a parse tree produced by CopyBookParser#collatingSequenceClauseNational.
    def enterCollatingSequenceClauseNational(self, ctx:CopyBookParser.CollatingSequenceClauseNationalContext):
        pass

    # Exit a parse tree produced by CopyBookParser#collatingSequenceClauseNational.
    def exitCollatingSequenceClauseNational(self, ctx:CopyBookParser.CollatingSequenceClauseNationalContext):
        pass


    # Enter a parse tree produced by CopyBookParser#segmentLimitClause.
    def enterSegmentLimitClause(self, ctx:CopyBookParser.SegmentLimitClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#segmentLimitClause.
    def exitSegmentLimitClause(self, ctx:CopyBookParser.SegmentLimitClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#characterSetClause.
    def enterCharacterSetClause(self, ctx:CopyBookParser.CharacterSetClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#characterSetClause.
    def exitCharacterSetClause(self, ctx:CopyBookParser.CharacterSetClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#specialNamesParagraph.
    def enterSpecialNamesParagraph(self, ctx:CopyBookParser.SpecialNamesParagraphContext):
        pass

    # Exit a parse tree produced by CopyBookParser#specialNamesParagraph.
    def exitSpecialNamesParagraph(self, ctx:CopyBookParser.SpecialNamesParagraphContext):
        pass


    # Enter a parse tree produced by CopyBookParser#specialNameClause.
    def enterSpecialNameClause(self, ctx:CopyBookParser.SpecialNameClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#specialNameClause.
    def exitSpecialNameClause(self, ctx:CopyBookParser.SpecialNameClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#alphabetClause.
    def enterAlphabetClause(self, ctx:CopyBookParser.AlphabetClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#alphabetClause.
    def exitAlphabetClause(self, ctx:CopyBookParser.AlphabetClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#alphabetClauseFormat1.
    def enterAlphabetClauseFormat1(self, ctx:CopyBookParser.AlphabetClauseFormat1Context):
        pass

    # Exit a parse tree produced by CopyBookParser#alphabetClauseFormat1.
    def exitAlphabetClauseFormat1(self, ctx:CopyBookParser.AlphabetClauseFormat1Context):
        pass


    # Enter a parse tree produced by CopyBookParser#alphabetLiterals.
    def enterAlphabetLiterals(self, ctx:CopyBookParser.AlphabetLiteralsContext):
        pass

    # Exit a parse tree produced by CopyBookParser#alphabetLiterals.
    def exitAlphabetLiterals(self, ctx:CopyBookParser.AlphabetLiteralsContext):
        pass


    # Enter a parse tree produced by CopyBookParser#alphabetThrough.
    def enterAlphabetThrough(self, ctx:CopyBookParser.AlphabetThroughContext):
        pass

    # Exit a parse tree produced by CopyBookParser#alphabetThrough.
    def exitAlphabetThrough(self, ctx:CopyBookParser.AlphabetThroughContext):
        pass


    # Enter a parse tree produced by CopyBookParser#alphabetAlso.
    def enterAlphabetAlso(self, ctx:CopyBookParser.AlphabetAlsoContext):
        pass

    # Exit a parse tree produced by CopyBookParser#alphabetAlso.
    def exitAlphabetAlso(self, ctx:CopyBookParser.AlphabetAlsoContext):
        pass


    # Enter a parse tree produced by CopyBookParser#alphabetClauseFormat2.
    def enterAlphabetClauseFormat2(self, ctx:CopyBookParser.AlphabetClauseFormat2Context):
        pass

    # Exit a parse tree produced by CopyBookParser#alphabetClauseFormat2.
    def exitAlphabetClauseFormat2(self, ctx:CopyBookParser.AlphabetClauseFormat2Context):
        pass


    # Enter a parse tree produced by CopyBookParser#channelClause.
    def enterChannelClause(self, ctx:CopyBookParser.ChannelClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#channelClause.
    def exitChannelClause(self, ctx:CopyBookParser.ChannelClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#classClause.
    def enterClassClause(self, ctx:CopyBookParser.ClassClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#classClause.
    def exitClassClause(self, ctx:CopyBookParser.ClassClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#classClauseThrough.
    def enterClassClauseThrough(self, ctx:CopyBookParser.ClassClauseThroughContext):
        pass

    # Exit a parse tree produced by CopyBookParser#classClauseThrough.
    def exitClassClauseThrough(self, ctx:CopyBookParser.ClassClauseThroughContext):
        pass


    # Enter a parse tree produced by CopyBookParser#classClauseFrom.
    def enterClassClauseFrom(self, ctx:CopyBookParser.ClassClauseFromContext):
        pass

    # Exit a parse tree produced by CopyBookParser#classClauseFrom.
    def exitClassClauseFrom(self, ctx:CopyBookParser.ClassClauseFromContext):
        pass


    # Enter a parse tree produced by CopyBookParser#classClauseTo.
    def enterClassClauseTo(self, ctx:CopyBookParser.ClassClauseToContext):
        pass

    # Exit a parse tree produced by CopyBookParser#classClauseTo.
    def exitClassClauseTo(self, ctx:CopyBookParser.ClassClauseToContext):
        pass


    # Enter a parse tree produced by CopyBookParser#currencySignClause.
    def enterCurrencySignClause(self, ctx:CopyBookParser.CurrencySignClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#currencySignClause.
    def exitCurrencySignClause(self, ctx:CopyBookParser.CurrencySignClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#decimalPointClause.
    def enterDecimalPointClause(self, ctx:CopyBookParser.DecimalPointClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#decimalPointClause.
    def exitDecimalPointClause(self, ctx:CopyBookParser.DecimalPointClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#defaultComputationalSignClause.
    def enterDefaultComputationalSignClause(self, ctx:CopyBookParser.DefaultComputationalSignClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#defaultComputationalSignClause.
    def exitDefaultComputationalSignClause(self, ctx:CopyBookParser.DefaultComputationalSignClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#defaultDisplaySignClause.
    def enterDefaultDisplaySignClause(self, ctx:CopyBookParser.DefaultDisplaySignClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#defaultDisplaySignClause.
    def exitDefaultDisplaySignClause(self, ctx:CopyBookParser.DefaultDisplaySignClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#environmentSwitchNameClause.
    def enterEnvironmentSwitchNameClause(self, ctx:CopyBookParser.EnvironmentSwitchNameClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#environmentSwitchNameClause.
    def exitEnvironmentSwitchNameClause(self, ctx:CopyBookParser.EnvironmentSwitchNameClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#environmentSwitchNameSpecialNamesStatusPhrase.
    def enterEnvironmentSwitchNameSpecialNamesStatusPhrase(self, ctx:CopyBookParser.EnvironmentSwitchNameSpecialNamesStatusPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#environmentSwitchNameSpecialNamesStatusPhrase.
    def exitEnvironmentSwitchNameSpecialNamesStatusPhrase(self, ctx:CopyBookParser.EnvironmentSwitchNameSpecialNamesStatusPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#odtClause.
    def enterOdtClause(self, ctx:CopyBookParser.OdtClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#odtClause.
    def exitOdtClause(self, ctx:CopyBookParser.OdtClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reserveNetworkClause.
    def enterReserveNetworkClause(self, ctx:CopyBookParser.ReserveNetworkClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reserveNetworkClause.
    def exitReserveNetworkClause(self, ctx:CopyBookParser.ReserveNetworkClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#symbolicCharactersClause.
    def enterSymbolicCharactersClause(self, ctx:CopyBookParser.SymbolicCharactersClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#symbolicCharactersClause.
    def exitSymbolicCharactersClause(self, ctx:CopyBookParser.SymbolicCharactersClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#symbolicCharacters.
    def enterSymbolicCharacters(self, ctx:CopyBookParser.SymbolicCharactersContext):
        pass

    # Exit a parse tree produced by CopyBookParser#symbolicCharacters.
    def exitSymbolicCharacters(self, ctx:CopyBookParser.SymbolicCharactersContext):
        pass


    # Enter a parse tree produced by CopyBookParser#inputOutputSection.
    def enterInputOutputSection(self, ctx:CopyBookParser.InputOutputSectionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#inputOutputSection.
    def exitInputOutputSection(self, ctx:CopyBookParser.InputOutputSectionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#inputOutputSectionParagraph.
    def enterInputOutputSectionParagraph(self, ctx:CopyBookParser.InputOutputSectionParagraphContext):
        pass

    # Exit a parse tree produced by CopyBookParser#inputOutputSectionParagraph.
    def exitInputOutputSectionParagraph(self, ctx:CopyBookParser.InputOutputSectionParagraphContext):
        pass


    # Enter a parse tree produced by CopyBookParser#fileControlParagraph.
    def enterFileControlParagraph(self, ctx:CopyBookParser.FileControlParagraphContext):
        pass

    # Exit a parse tree produced by CopyBookParser#fileControlParagraph.
    def exitFileControlParagraph(self, ctx:CopyBookParser.FileControlParagraphContext):
        pass


    # Enter a parse tree produced by CopyBookParser#fileControlEntry.
    def enterFileControlEntry(self, ctx:CopyBookParser.FileControlEntryContext):
        pass

    # Exit a parse tree produced by CopyBookParser#fileControlEntry.
    def exitFileControlEntry(self, ctx:CopyBookParser.FileControlEntryContext):
        pass


    # Enter a parse tree produced by CopyBookParser#selectClause.
    def enterSelectClause(self, ctx:CopyBookParser.SelectClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#selectClause.
    def exitSelectClause(self, ctx:CopyBookParser.SelectClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#fileControlClause.
    def enterFileControlClause(self, ctx:CopyBookParser.FileControlClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#fileControlClause.
    def exitFileControlClause(self, ctx:CopyBookParser.FileControlClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#assignClause.
    def enterAssignClause(self, ctx:CopyBookParser.AssignClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#assignClause.
    def exitAssignClause(self, ctx:CopyBookParser.AssignClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reserveClause.
    def enterReserveClause(self, ctx:CopyBookParser.ReserveClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reserveClause.
    def exitReserveClause(self, ctx:CopyBookParser.ReserveClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#organizationClause.
    def enterOrganizationClause(self, ctx:CopyBookParser.OrganizationClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#organizationClause.
    def exitOrganizationClause(self, ctx:CopyBookParser.OrganizationClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#paddingCharacterClause.
    def enterPaddingCharacterClause(self, ctx:CopyBookParser.PaddingCharacterClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#paddingCharacterClause.
    def exitPaddingCharacterClause(self, ctx:CopyBookParser.PaddingCharacterClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#recordDelimiterClause.
    def enterRecordDelimiterClause(self, ctx:CopyBookParser.RecordDelimiterClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#recordDelimiterClause.
    def exitRecordDelimiterClause(self, ctx:CopyBookParser.RecordDelimiterClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#accessModeClause.
    def enterAccessModeClause(self, ctx:CopyBookParser.AccessModeClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#accessModeClause.
    def exitAccessModeClause(self, ctx:CopyBookParser.AccessModeClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#recordKeyClause.
    def enterRecordKeyClause(self, ctx:CopyBookParser.RecordKeyClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#recordKeyClause.
    def exitRecordKeyClause(self, ctx:CopyBookParser.RecordKeyClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#alternateRecordKeyClause.
    def enterAlternateRecordKeyClause(self, ctx:CopyBookParser.AlternateRecordKeyClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#alternateRecordKeyClause.
    def exitAlternateRecordKeyClause(self, ctx:CopyBookParser.AlternateRecordKeyClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#passwordClause.
    def enterPasswordClause(self, ctx:CopyBookParser.PasswordClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#passwordClause.
    def exitPasswordClause(self, ctx:CopyBookParser.PasswordClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#fileStatusClause.
    def enterFileStatusClause(self, ctx:CopyBookParser.FileStatusClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#fileStatusClause.
    def exitFileStatusClause(self, ctx:CopyBookParser.FileStatusClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#relativeKeyClause.
    def enterRelativeKeyClause(self, ctx:CopyBookParser.RelativeKeyClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#relativeKeyClause.
    def exitRelativeKeyClause(self, ctx:CopyBookParser.RelativeKeyClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#ioControlParagraph.
    def enterIoControlParagraph(self, ctx:CopyBookParser.IoControlParagraphContext):
        pass

    # Exit a parse tree produced by CopyBookParser#ioControlParagraph.
    def exitIoControlParagraph(self, ctx:CopyBookParser.IoControlParagraphContext):
        pass


    # Enter a parse tree produced by CopyBookParser#ioControlClause.
    def enterIoControlClause(self, ctx:CopyBookParser.IoControlClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#ioControlClause.
    def exitIoControlClause(self, ctx:CopyBookParser.IoControlClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#rerunClause.
    def enterRerunClause(self, ctx:CopyBookParser.RerunClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#rerunClause.
    def exitRerunClause(self, ctx:CopyBookParser.RerunClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#rerunEveryRecords.
    def enterRerunEveryRecords(self, ctx:CopyBookParser.RerunEveryRecordsContext):
        pass

    # Exit a parse tree produced by CopyBookParser#rerunEveryRecords.
    def exitRerunEveryRecords(self, ctx:CopyBookParser.RerunEveryRecordsContext):
        pass


    # Enter a parse tree produced by CopyBookParser#rerunEveryOf.
    def enterRerunEveryOf(self, ctx:CopyBookParser.RerunEveryOfContext):
        pass

    # Exit a parse tree produced by CopyBookParser#rerunEveryOf.
    def exitRerunEveryOf(self, ctx:CopyBookParser.RerunEveryOfContext):
        pass


    # Enter a parse tree produced by CopyBookParser#rerunEveryClock.
    def enterRerunEveryClock(self, ctx:CopyBookParser.RerunEveryClockContext):
        pass

    # Exit a parse tree produced by CopyBookParser#rerunEveryClock.
    def exitRerunEveryClock(self, ctx:CopyBookParser.RerunEveryClockContext):
        pass


    # Enter a parse tree produced by CopyBookParser#sameClause.
    def enterSameClause(self, ctx:CopyBookParser.SameClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#sameClause.
    def exitSameClause(self, ctx:CopyBookParser.SameClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#multipleFileClause.
    def enterMultipleFileClause(self, ctx:CopyBookParser.MultipleFileClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#multipleFileClause.
    def exitMultipleFileClause(self, ctx:CopyBookParser.MultipleFileClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#multipleFilePosition.
    def enterMultipleFilePosition(self, ctx:CopyBookParser.MultipleFilePositionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#multipleFilePosition.
    def exitMultipleFilePosition(self, ctx:CopyBookParser.MultipleFilePositionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#commitmentControlClause.
    def enterCommitmentControlClause(self, ctx:CopyBookParser.CommitmentControlClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#commitmentControlClause.
    def exitCommitmentControlClause(self, ctx:CopyBookParser.CommitmentControlClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataDivision.
    def enterDataDivision(self, ctx:CopyBookParser.DataDivisionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataDivision.
    def exitDataDivision(self, ctx:CopyBookParser.DataDivisionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataDivisionSection.
    def enterDataDivisionSection(self, ctx:CopyBookParser.DataDivisionSectionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataDivisionSection.
    def exitDataDivisionSection(self, ctx:CopyBookParser.DataDivisionSectionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#fileSection.
    def enterFileSection(self, ctx:CopyBookParser.FileSectionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#fileSection.
    def exitFileSection(self, ctx:CopyBookParser.FileSectionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#fileDescriptionEntry.
    def enterFileDescriptionEntry(self, ctx:CopyBookParser.FileDescriptionEntryContext):
        pass

    # Exit a parse tree produced by CopyBookParser#fileDescriptionEntry.
    def exitFileDescriptionEntry(self, ctx:CopyBookParser.FileDescriptionEntryContext):
        pass


    # Enter a parse tree produced by CopyBookParser#fileDescriptionEntryClause.
    def enterFileDescriptionEntryClause(self, ctx:CopyBookParser.FileDescriptionEntryClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#fileDescriptionEntryClause.
    def exitFileDescriptionEntryClause(self, ctx:CopyBookParser.FileDescriptionEntryClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#externalClause.
    def enterExternalClause(self, ctx:CopyBookParser.ExternalClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#externalClause.
    def exitExternalClause(self, ctx:CopyBookParser.ExternalClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#globalClause.
    def enterGlobalClause(self, ctx:CopyBookParser.GlobalClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#globalClause.
    def exitGlobalClause(self, ctx:CopyBookParser.GlobalClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#blockContainsClause.
    def enterBlockContainsClause(self, ctx:CopyBookParser.BlockContainsClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#blockContainsClause.
    def exitBlockContainsClause(self, ctx:CopyBookParser.BlockContainsClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#blockContainsTo.
    def enterBlockContainsTo(self, ctx:CopyBookParser.BlockContainsToContext):
        pass

    # Exit a parse tree produced by CopyBookParser#blockContainsTo.
    def exitBlockContainsTo(self, ctx:CopyBookParser.BlockContainsToContext):
        pass


    # Enter a parse tree produced by CopyBookParser#recordContainsClause.
    def enterRecordContainsClause(self, ctx:CopyBookParser.RecordContainsClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#recordContainsClause.
    def exitRecordContainsClause(self, ctx:CopyBookParser.RecordContainsClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#recordContainsClauseFormat1.
    def enterRecordContainsClauseFormat1(self, ctx:CopyBookParser.RecordContainsClauseFormat1Context):
        pass

    # Exit a parse tree produced by CopyBookParser#recordContainsClauseFormat1.
    def exitRecordContainsClauseFormat1(self, ctx:CopyBookParser.RecordContainsClauseFormat1Context):
        pass


    # Enter a parse tree produced by CopyBookParser#recordContainsClauseFormat2.
    def enterRecordContainsClauseFormat2(self, ctx:CopyBookParser.RecordContainsClauseFormat2Context):
        pass

    # Exit a parse tree produced by CopyBookParser#recordContainsClauseFormat2.
    def exitRecordContainsClauseFormat2(self, ctx:CopyBookParser.RecordContainsClauseFormat2Context):
        pass


    # Enter a parse tree produced by CopyBookParser#recordContainsClauseFormat3.
    def enterRecordContainsClauseFormat3(self, ctx:CopyBookParser.RecordContainsClauseFormat3Context):
        pass

    # Exit a parse tree produced by CopyBookParser#recordContainsClauseFormat3.
    def exitRecordContainsClauseFormat3(self, ctx:CopyBookParser.RecordContainsClauseFormat3Context):
        pass


    # Enter a parse tree produced by CopyBookParser#recordContainsTo.
    def enterRecordContainsTo(self, ctx:CopyBookParser.RecordContainsToContext):
        pass

    # Exit a parse tree produced by CopyBookParser#recordContainsTo.
    def exitRecordContainsTo(self, ctx:CopyBookParser.RecordContainsToContext):
        pass


    # Enter a parse tree produced by CopyBookParser#labelRecordsClause.
    def enterLabelRecordsClause(self, ctx:CopyBookParser.LabelRecordsClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#labelRecordsClause.
    def exitLabelRecordsClause(self, ctx:CopyBookParser.LabelRecordsClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#valueOfClause.
    def enterValueOfClause(self, ctx:CopyBookParser.ValueOfClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#valueOfClause.
    def exitValueOfClause(self, ctx:CopyBookParser.ValueOfClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#valuePair.
    def enterValuePair(self, ctx:CopyBookParser.ValuePairContext):
        pass

    # Exit a parse tree produced by CopyBookParser#valuePair.
    def exitValuePair(self, ctx:CopyBookParser.ValuePairContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataRecordsClause.
    def enterDataRecordsClause(self, ctx:CopyBookParser.DataRecordsClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataRecordsClause.
    def exitDataRecordsClause(self, ctx:CopyBookParser.DataRecordsClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#linageClause.
    def enterLinageClause(self, ctx:CopyBookParser.LinageClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#linageClause.
    def exitLinageClause(self, ctx:CopyBookParser.LinageClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#linageAt.
    def enterLinageAt(self, ctx:CopyBookParser.LinageAtContext):
        pass

    # Exit a parse tree produced by CopyBookParser#linageAt.
    def exitLinageAt(self, ctx:CopyBookParser.LinageAtContext):
        pass


    # Enter a parse tree produced by CopyBookParser#linageFootingAt.
    def enterLinageFootingAt(self, ctx:CopyBookParser.LinageFootingAtContext):
        pass

    # Exit a parse tree produced by CopyBookParser#linageFootingAt.
    def exitLinageFootingAt(self, ctx:CopyBookParser.LinageFootingAtContext):
        pass


    # Enter a parse tree produced by CopyBookParser#linageLinesAtTop.
    def enterLinageLinesAtTop(self, ctx:CopyBookParser.LinageLinesAtTopContext):
        pass

    # Exit a parse tree produced by CopyBookParser#linageLinesAtTop.
    def exitLinageLinesAtTop(self, ctx:CopyBookParser.LinageLinesAtTopContext):
        pass


    # Enter a parse tree produced by CopyBookParser#linageLinesAtBottom.
    def enterLinageLinesAtBottom(self, ctx:CopyBookParser.LinageLinesAtBottomContext):
        pass

    # Exit a parse tree produced by CopyBookParser#linageLinesAtBottom.
    def exitLinageLinesAtBottom(self, ctx:CopyBookParser.LinageLinesAtBottomContext):
        pass


    # Enter a parse tree produced by CopyBookParser#recordingModeClause.
    def enterRecordingModeClause(self, ctx:CopyBookParser.RecordingModeClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#recordingModeClause.
    def exitRecordingModeClause(self, ctx:CopyBookParser.RecordingModeClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#modeStatement.
    def enterModeStatement(self, ctx:CopyBookParser.ModeStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#modeStatement.
    def exitModeStatement(self, ctx:CopyBookParser.ModeStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#codeSetClause.
    def enterCodeSetClause(self, ctx:CopyBookParser.CodeSetClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#codeSetClause.
    def exitCodeSetClause(self, ctx:CopyBookParser.CodeSetClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportClause.
    def enterReportClause(self, ctx:CopyBookParser.ReportClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportClause.
    def exitReportClause(self, ctx:CopyBookParser.ReportClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataBaseSection.
    def enterDataBaseSection(self, ctx:CopyBookParser.DataBaseSectionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataBaseSection.
    def exitDataBaseSection(self, ctx:CopyBookParser.DataBaseSectionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataBaseSectionEntry.
    def enterDataBaseSectionEntry(self, ctx:CopyBookParser.DataBaseSectionEntryContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataBaseSectionEntry.
    def exitDataBaseSectionEntry(self, ctx:CopyBookParser.DataBaseSectionEntryContext):
        pass


    # Enter a parse tree produced by CopyBookParser#workingStorageSection.
    def enterWorkingStorageSection(self, ctx:CopyBookParser.WorkingStorageSectionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#workingStorageSection.
    def exitWorkingStorageSection(self, ctx:CopyBookParser.WorkingStorageSectionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#linkageSection.
    def enterLinkageSection(self, ctx:CopyBookParser.LinkageSectionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#linkageSection.
    def exitLinkageSection(self, ctx:CopyBookParser.LinkageSectionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#communicationSection.
    def enterCommunicationSection(self, ctx:CopyBookParser.CommunicationSectionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#communicationSection.
    def exitCommunicationSection(self, ctx:CopyBookParser.CommunicationSectionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#communicationDescriptionEntry.
    def enterCommunicationDescriptionEntry(self, ctx:CopyBookParser.CommunicationDescriptionEntryContext):
        pass

    # Exit a parse tree produced by CopyBookParser#communicationDescriptionEntry.
    def exitCommunicationDescriptionEntry(self, ctx:CopyBookParser.CommunicationDescriptionEntryContext):
        pass


    # Enter a parse tree produced by CopyBookParser#communicationDescriptionEntryFormat1.
    def enterCommunicationDescriptionEntryFormat1(self, ctx:CopyBookParser.CommunicationDescriptionEntryFormat1Context):
        pass

    # Exit a parse tree produced by CopyBookParser#communicationDescriptionEntryFormat1.
    def exitCommunicationDescriptionEntryFormat1(self, ctx:CopyBookParser.CommunicationDescriptionEntryFormat1Context):
        pass


    # Enter a parse tree produced by CopyBookParser#communicationDescriptionEntryFormat2.
    def enterCommunicationDescriptionEntryFormat2(self, ctx:CopyBookParser.CommunicationDescriptionEntryFormat2Context):
        pass

    # Exit a parse tree produced by CopyBookParser#communicationDescriptionEntryFormat2.
    def exitCommunicationDescriptionEntryFormat2(self, ctx:CopyBookParser.CommunicationDescriptionEntryFormat2Context):
        pass


    # Enter a parse tree produced by CopyBookParser#communicationDescriptionEntryFormat3.
    def enterCommunicationDescriptionEntryFormat3(self, ctx:CopyBookParser.CommunicationDescriptionEntryFormat3Context):
        pass

    # Exit a parse tree produced by CopyBookParser#communicationDescriptionEntryFormat3.
    def exitCommunicationDescriptionEntryFormat3(self, ctx:CopyBookParser.CommunicationDescriptionEntryFormat3Context):
        pass


    # Enter a parse tree produced by CopyBookParser#destinationCountClause.
    def enterDestinationCountClause(self, ctx:CopyBookParser.DestinationCountClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#destinationCountClause.
    def exitDestinationCountClause(self, ctx:CopyBookParser.DestinationCountClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#destinationTableClause.
    def enterDestinationTableClause(self, ctx:CopyBookParser.DestinationTableClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#destinationTableClause.
    def exitDestinationTableClause(self, ctx:CopyBookParser.DestinationTableClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#endKeyClause.
    def enterEndKeyClause(self, ctx:CopyBookParser.EndKeyClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#endKeyClause.
    def exitEndKeyClause(self, ctx:CopyBookParser.EndKeyClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#errorKeyClause.
    def enterErrorKeyClause(self, ctx:CopyBookParser.ErrorKeyClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#errorKeyClause.
    def exitErrorKeyClause(self, ctx:CopyBookParser.ErrorKeyClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#messageCountClause.
    def enterMessageCountClause(self, ctx:CopyBookParser.MessageCountClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#messageCountClause.
    def exitMessageCountClause(self, ctx:CopyBookParser.MessageCountClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#messageDateClause.
    def enterMessageDateClause(self, ctx:CopyBookParser.MessageDateClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#messageDateClause.
    def exitMessageDateClause(self, ctx:CopyBookParser.MessageDateClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#messageTimeClause.
    def enterMessageTimeClause(self, ctx:CopyBookParser.MessageTimeClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#messageTimeClause.
    def exitMessageTimeClause(self, ctx:CopyBookParser.MessageTimeClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#statusKeyClause.
    def enterStatusKeyClause(self, ctx:CopyBookParser.StatusKeyClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#statusKeyClause.
    def exitStatusKeyClause(self, ctx:CopyBookParser.StatusKeyClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#symbolicDestinationClause.
    def enterSymbolicDestinationClause(self, ctx:CopyBookParser.SymbolicDestinationClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#symbolicDestinationClause.
    def exitSymbolicDestinationClause(self, ctx:CopyBookParser.SymbolicDestinationClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#symbolicQueueClause.
    def enterSymbolicQueueClause(self, ctx:CopyBookParser.SymbolicQueueClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#symbolicQueueClause.
    def exitSymbolicQueueClause(self, ctx:CopyBookParser.SymbolicQueueClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#symbolicSourceClause.
    def enterSymbolicSourceClause(self, ctx:CopyBookParser.SymbolicSourceClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#symbolicSourceClause.
    def exitSymbolicSourceClause(self, ctx:CopyBookParser.SymbolicSourceClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#symbolicTerminalClause.
    def enterSymbolicTerminalClause(self, ctx:CopyBookParser.SymbolicTerminalClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#symbolicTerminalClause.
    def exitSymbolicTerminalClause(self, ctx:CopyBookParser.SymbolicTerminalClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#symbolicSubQueueClause.
    def enterSymbolicSubQueueClause(self, ctx:CopyBookParser.SymbolicSubQueueClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#symbolicSubQueueClause.
    def exitSymbolicSubQueueClause(self, ctx:CopyBookParser.SymbolicSubQueueClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#textLengthClause.
    def enterTextLengthClause(self, ctx:CopyBookParser.TextLengthClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#textLengthClause.
    def exitTextLengthClause(self, ctx:CopyBookParser.TextLengthClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#localStorageSection.
    def enterLocalStorageSection(self, ctx:CopyBookParser.LocalStorageSectionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#localStorageSection.
    def exitLocalStorageSection(self, ctx:CopyBookParser.LocalStorageSectionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenSection.
    def enterScreenSection(self, ctx:CopyBookParser.ScreenSectionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenSection.
    def exitScreenSection(self, ctx:CopyBookParser.ScreenSectionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenDescriptionEntry.
    def enterScreenDescriptionEntry(self, ctx:CopyBookParser.ScreenDescriptionEntryContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenDescriptionEntry.
    def exitScreenDescriptionEntry(self, ctx:CopyBookParser.ScreenDescriptionEntryContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenDescriptionBlankClause.
    def enterScreenDescriptionBlankClause(self, ctx:CopyBookParser.ScreenDescriptionBlankClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenDescriptionBlankClause.
    def exitScreenDescriptionBlankClause(self, ctx:CopyBookParser.ScreenDescriptionBlankClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenDescriptionBellClause.
    def enterScreenDescriptionBellClause(self, ctx:CopyBookParser.ScreenDescriptionBellClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenDescriptionBellClause.
    def exitScreenDescriptionBellClause(self, ctx:CopyBookParser.ScreenDescriptionBellClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenDescriptionBlinkClause.
    def enterScreenDescriptionBlinkClause(self, ctx:CopyBookParser.ScreenDescriptionBlinkClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenDescriptionBlinkClause.
    def exitScreenDescriptionBlinkClause(self, ctx:CopyBookParser.ScreenDescriptionBlinkClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenDescriptionEraseClause.
    def enterScreenDescriptionEraseClause(self, ctx:CopyBookParser.ScreenDescriptionEraseClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenDescriptionEraseClause.
    def exitScreenDescriptionEraseClause(self, ctx:CopyBookParser.ScreenDescriptionEraseClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenDescriptionLightClause.
    def enterScreenDescriptionLightClause(self, ctx:CopyBookParser.ScreenDescriptionLightClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenDescriptionLightClause.
    def exitScreenDescriptionLightClause(self, ctx:CopyBookParser.ScreenDescriptionLightClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenDescriptionGridClause.
    def enterScreenDescriptionGridClause(self, ctx:CopyBookParser.ScreenDescriptionGridClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenDescriptionGridClause.
    def exitScreenDescriptionGridClause(self, ctx:CopyBookParser.ScreenDescriptionGridClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenDescriptionReverseVideoClause.
    def enterScreenDescriptionReverseVideoClause(self, ctx:CopyBookParser.ScreenDescriptionReverseVideoClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenDescriptionReverseVideoClause.
    def exitScreenDescriptionReverseVideoClause(self, ctx:CopyBookParser.ScreenDescriptionReverseVideoClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenDescriptionUnderlineClause.
    def enterScreenDescriptionUnderlineClause(self, ctx:CopyBookParser.ScreenDescriptionUnderlineClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenDescriptionUnderlineClause.
    def exitScreenDescriptionUnderlineClause(self, ctx:CopyBookParser.ScreenDescriptionUnderlineClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenDescriptionSizeClause.
    def enterScreenDescriptionSizeClause(self, ctx:CopyBookParser.ScreenDescriptionSizeClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenDescriptionSizeClause.
    def exitScreenDescriptionSizeClause(self, ctx:CopyBookParser.ScreenDescriptionSizeClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenDescriptionLineClause.
    def enterScreenDescriptionLineClause(self, ctx:CopyBookParser.ScreenDescriptionLineClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenDescriptionLineClause.
    def exitScreenDescriptionLineClause(self, ctx:CopyBookParser.ScreenDescriptionLineClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenDescriptionColumnClause.
    def enterScreenDescriptionColumnClause(self, ctx:CopyBookParser.ScreenDescriptionColumnClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenDescriptionColumnClause.
    def exitScreenDescriptionColumnClause(self, ctx:CopyBookParser.ScreenDescriptionColumnClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenDescriptionForegroundColorClause.
    def enterScreenDescriptionForegroundColorClause(self, ctx:CopyBookParser.ScreenDescriptionForegroundColorClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenDescriptionForegroundColorClause.
    def exitScreenDescriptionForegroundColorClause(self, ctx:CopyBookParser.ScreenDescriptionForegroundColorClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenDescriptionBackgroundColorClause.
    def enterScreenDescriptionBackgroundColorClause(self, ctx:CopyBookParser.ScreenDescriptionBackgroundColorClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenDescriptionBackgroundColorClause.
    def exitScreenDescriptionBackgroundColorClause(self, ctx:CopyBookParser.ScreenDescriptionBackgroundColorClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenDescriptionControlClause.
    def enterScreenDescriptionControlClause(self, ctx:CopyBookParser.ScreenDescriptionControlClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenDescriptionControlClause.
    def exitScreenDescriptionControlClause(self, ctx:CopyBookParser.ScreenDescriptionControlClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenDescriptionValueClause.
    def enterScreenDescriptionValueClause(self, ctx:CopyBookParser.ScreenDescriptionValueClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenDescriptionValueClause.
    def exitScreenDescriptionValueClause(self, ctx:CopyBookParser.ScreenDescriptionValueClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenDescriptionPictureClause.
    def enterScreenDescriptionPictureClause(self, ctx:CopyBookParser.ScreenDescriptionPictureClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenDescriptionPictureClause.
    def exitScreenDescriptionPictureClause(self, ctx:CopyBookParser.ScreenDescriptionPictureClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenDescriptionFromClause.
    def enterScreenDescriptionFromClause(self, ctx:CopyBookParser.ScreenDescriptionFromClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenDescriptionFromClause.
    def exitScreenDescriptionFromClause(self, ctx:CopyBookParser.ScreenDescriptionFromClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenDescriptionToClause.
    def enterScreenDescriptionToClause(self, ctx:CopyBookParser.ScreenDescriptionToClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenDescriptionToClause.
    def exitScreenDescriptionToClause(self, ctx:CopyBookParser.ScreenDescriptionToClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenDescriptionUsingClause.
    def enterScreenDescriptionUsingClause(self, ctx:CopyBookParser.ScreenDescriptionUsingClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenDescriptionUsingClause.
    def exitScreenDescriptionUsingClause(self, ctx:CopyBookParser.ScreenDescriptionUsingClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenDescriptionUsageClause.
    def enterScreenDescriptionUsageClause(self, ctx:CopyBookParser.ScreenDescriptionUsageClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenDescriptionUsageClause.
    def exitScreenDescriptionUsageClause(self, ctx:CopyBookParser.ScreenDescriptionUsageClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenDescriptionBlankWhenZeroClause.
    def enterScreenDescriptionBlankWhenZeroClause(self, ctx:CopyBookParser.ScreenDescriptionBlankWhenZeroClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenDescriptionBlankWhenZeroClause.
    def exitScreenDescriptionBlankWhenZeroClause(self, ctx:CopyBookParser.ScreenDescriptionBlankWhenZeroClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenDescriptionJustifiedClause.
    def enterScreenDescriptionJustifiedClause(self, ctx:CopyBookParser.ScreenDescriptionJustifiedClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenDescriptionJustifiedClause.
    def exitScreenDescriptionJustifiedClause(self, ctx:CopyBookParser.ScreenDescriptionJustifiedClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenDescriptionSignClause.
    def enterScreenDescriptionSignClause(self, ctx:CopyBookParser.ScreenDescriptionSignClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenDescriptionSignClause.
    def exitScreenDescriptionSignClause(self, ctx:CopyBookParser.ScreenDescriptionSignClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenDescriptionAutoClause.
    def enterScreenDescriptionAutoClause(self, ctx:CopyBookParser.ScreenDescriptionAutoClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenDescriptionAutoClause.
    def exitScreenDescriptionAutoClause(self, ctx:CopyBookParser.ScreenDescriptionAutoClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenDescriptionSecureClause.
    def enterScreenDescriptionSecureClause(self, ctx:CopyBookParser.ScreenDescriptionSecureClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenDescriptionSecureClause.
    def exitScreenDescriptionSecureClause(self, ctx:CopyBookParser.ScreenDescriptionSecureClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenDescriptionRequiredClause.
    def enterScreenDescriptionRequiredClause(self, ctx:CopyBookParser.ScreenDescriptionRequiredClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenDescriptionRequiredClause.
    def exitScreenDescriptionRequiredClause(self, ctx:CopyBookParser.ScreenDescriptionRequiredClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenDescriptionPromptClause.
    def enterScreenDescriptionPromptClause(self, ctx:CopyBookParser.ScreenDescriptionPromptClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenDescriptionPromptClause.
    def exitScreenDescriptionPromptClause(self, ctx:CopyBookParser.ScreenDescriptionPromptClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenDescriptionPromptOccursClause.
    def enterScreenDescriptionPromptOccursClause(self, ctx:CopyBookParser.ScreenDescriptionPromptOccursClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenDescriptionPromptOccursClause.
    def exitScreenDescriptionPromptOccursClause(self, ctx:CopyBookParser.ScreenDescriptionPromptOccursClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenDescriptionFullClause.
    def enterScreenDescriptionFullClause(self, ctx:CopyBookParser.ScreenDescriptionFullClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenDescriptionFullClause.
    def exitScreenDescriptionFullClause(self, ctx:CopyBookParser.ScreenDescriptionFullClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenDescriptionZeroFillClause.
    def enterScreenDescriptionZeroFillClause(self, ctx:CopyBookParser.ScreenDescriptionZeroFillClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenDescriptionZeroFillClause.
    def exitScreenDescriptionZeroFillClause(self, ctx:CopyBookParser.ScreenDescriptionZeroFillClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportSection.
    def enterReportSection(self, ctx:CopyBookParser.ReportSectionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportSection.
    def exitReportSection(self, ctx:CopyBookParser.ReportSectionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportDescription.
    def enterReportDescription(self, ctx:CopyBookParser.ReportDescriptionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportDescription.
    def exitReportDescription(self, ctx:CopyBookParser.ReportDescriptionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportDescriptionEntry.
    def enterReportDescriptionEntry(self, ctx:CopyBookParser.ReportDescriptionEntryContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportDescriptionEntry.
    def exitReportDescriptionEntry(self, ctx:CopyBookParser.ReportDescriptionEntryContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportDescriptionGlobalClause.
    def enterReportDescriptionGlobalClause(self, ctx:CopyBookParser.ReportDescriptionGlobalClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportDescriptionGlobalClause.
    def exitReportDescriptionGlobalClause(self, ctx:CopyBookParser.ReportDescriptionGlobalClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportDescriptionPageLimitClause.
    def enterReportDescriptionPageLimitClause(self, ctx:CopyBookParser.ReportDescriptionPageLimitClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportDescriptionPageLimitClause.
    def exitReportDescriptionPageLimitClause(self, ctx:CopyBookParser.ReportDescriptionPageLimitClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportDescriptionHeadingClause.
    def enterReportDescriptionHeadingClause(self, ctx:CopyBookParser.ReportDescriptionHeadingClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportDescriptionHeadingClause.
    def exitReportDescriptionHeadingClause(self, ctx:CopyBookParser.ReportDescriptionHeadingClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportDescriptionFirstDetailClause.
    def enterReportDescriptionFirstDetailClause(self, ctx:CopyBookParser.ReportDescriptionFirstDetailClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportDescriptionFirstDetailClause.
    def exitReportDescriptionFirstDetailClause(self, ctx:CopyBookParser.ReportDescriptionFirstDetailClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportDescriptionLastDetailClause.
    def enterReportDescriptionLastDetailClause(self, ctx:CopyBookParser.ReportDescriptionLastDetailClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportDescriptionLastDetailClause.
    def exitReportDescriptionLastDetailClause(self, ctx:CopyBookParser.ReportDescriptionLastDetailClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportDescriptionFootingClause.
    def enterReportDescriptionFootingClause(self, ctx:CopyBookParser.ReportDescriptionFootingClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportDescriptionFootingClause.
    def exitReportDescriptionFootingClause(self, ctx:CopyBookParser.ReportDescriptionFootingClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportGroupDescriptionEntry.
    def enterReportGroupDescriptionEntry(self, ctx:CopyBookParser.ReportGroupDescriptionEntryContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportGroupDescriptionEntry.
    def exitReportGroupDescriptionEntry(self, ctx:CopyBookParser.ReportGroupDescriptionEntryContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportGroupDescriptionEntryFormat1.
    def enterReportGroupDescriptionEntryFormat1(self, ctx:CopyBookParser.ReportGroupDescriptionEntryFormat1Context):
        pass

    # Exit a parse tree produced by CopyBookParser#reportGroupDescriptionEntryFormat1.
    def exitReportGroupDescriptionEntryFormat1(self, ctx:CopyBookParser.ReportGroupDescriptionEntryFormat1Context):
        pass


    # Enter a parse tree produced by CopyBookParser#reportGroupDescriptionEntryFormat2.
    def enterReportGroupDescriptionEntryFormat2(self, ctx:CopyBookParser.ReportGroupDescriptionEntryFormat2Context):
        pass

    # Exit a parse tree produced by CopyBookParser#reportGroupDescriptionEntryFormat2.
    def exitReportGroupDescriptionEntryFormat2(self, ctx:CopyBookParser.ReportGroupDescriptionEntryFormat2Context):
        pass


    # Enter a parse tree produced by CopyBookParser#reportGroupDescriptionEntryFormat3.
    def enterReportGroupDescriptionEntryFormat3(self, ctx:CopyBookParser.ReportGroupDescriptionEntryFormat3Context):
        pass

    # Exit a parse tree produced by CopyBookParser#reportGroupDescriptionEntryFormat3.
    def exitReportGroupDescriptionEntryFormat3(self, ctx:CopyBookParser.ReportGroupDescriptionEntryFormat3Context):
        pass


    # Enter a parse tree produced by CopyBookParser#reportGroupBlankWhenZeroClause.
    def enterReportGroupBlankWhenZeroClause(self, ctx:CopyBookParser.ReportGroupBlankWhenZeroClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportGroupBlankWhenZeroClause.
    def exitReportGroupBlankWhenZeroClause(self, ctx:CopyBookParser.ReportGroupBlankWhenZeroClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportGroupColumnNumberClause.
    def enterReportGroupColumnNumberClause(self, ctx:CopyBookParser.ReportGroupColumnNumberClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportGroupColumnNumberClause.
    def exitReportGroupColumnNumberClause(self, ctx:CopyBookParser.ReportGroupColumnNumberClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportGroupIndicateClause.
    def enterReportGroupIndicateClause(self, ctx:CopyBookParser.ReportGroupIndicateClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportGroupIndicateClause.
    def exitReportGroupIndicateClause(self, ctx:CopyBookParser.ReportGroupIndicateClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportGroupJustifiedClause.
    def enterReportGroupJustifiedClause(self, ctx:CopyBookParser.ReportGroupJustifiedClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportGroupJustifiedClause.
    def exitReportGroupJustifiedClause(self, ctx:CopyBookParser.ReportGroupJustifiedClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportGroupLineNumberClause.
    def enterReportGroupLineNumberClause(self, ctx:CopyBookParser.ReportGroupLineNumberClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportGroupLineNumberClause.
    def exitReportGroupLineNumberClause(self, ctx:CopyBookParser.ReportGroupLineNumberClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportGroupLineNumberNextPage.
    def enterReportGroupLineNumberNextPage(self, ctx:CopyBookParser.ReportGroupLineNumberNextPageContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportGroupLineNumberNextPage.
    def exitReportGroupLineNumberNextPage(self, ctx:CopyBookParser.ReportGroupLineNumberNextPageContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportGroupLineNumberPlus.
    def enterReportGroupLineNumberPlus(self, ctx:CopyBookParser.ReportGroupLineNumberPlusContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportGroupLineNumberPlus.
    def exitReportGroupLineNumberPlus(self, ctx:CopyBookParser.ReportGroupLineNumberPlusContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportGroupNextGroupClause.
    def enterReportGroupNextGroupClause(self, ctx:CopyBookParser.ReportGroupNextGroupClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportGroupNextGroupClause.
    def exitReportGroupNextGroupClause(self, ctx:CopyBookParser.ReportGroupNextGroupClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportGroupNextGroupPlus.
    def enterReportGroupNextGroupPlus(self, ctx:CopyBookParser.ReportGroupNextGroupPlusContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportGroupNextGroupPlus.
    def exitReportGroupNextGroupPlus(self, ctx:CopyBookParser.ReportGroupNextGroupPlusContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportGroupNextGroupNextPage.
    def enterReportGroupNextGroupNextPage(self, ctx:CopyBookParser.ReportGroupNextGroupNextPageContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportGroupNextGroupNextPage.
    def exitReportGroupNextGroupNextPage(self, ctx:CopyBookParser.ReportGroupNextGroupNextPageContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportGroupPictureClause.
    def enterReportGroupPictureClause(self, ctx:CopyBookParser.ReportGroupPictureClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportGroupPictureClause.
    def exitReportGroupPictureClause(self, ctx:CopyBookParser.ReportGroupPictureClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportGroupResetClause.
    def enterReportGroupResetClause(self, ctx:CopyBookParser.ReportGroupResetClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportGroupResetClause.
    def exitReportGroupResetClause(self, ctx:CopyBookParser.ReportGroupResetClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportGroupSignClause.
    def enterReportGroupSignClause(self, ctx:CopyBookParser.ReportGroupSignClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportGroupSignClause.
    def exitReportGroupSignClause(self, ctx:CopyBookParser.ReportGroupSignClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportGroupSourceClause.
    def enterReportGroupSourceClause(self, ctx:CopyBookParser.ReportGroupSourceClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportGroupSourceClause.
    def exitReportGroupSourceClause(self, ctx:CopyBookParser.ReportGroupSourceClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportGroupSumClause.
    def enterReportGroupSumClause(self, ctx:CopyBookParser.ReportGroupSumClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportGroupSumClause.
    def exitReportGroupSumClause(self, ctx:CopyBookParser.ReportGroupSumClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportGroupTypeClause.
    def enterReportGroupTypeClause(self, ctx:CopyBookParser.ReportGroupTypeClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportGroupTypeClause.
    def exitReportGroupTypeClause(self, ctx:CopyBookParser.ReportGroupTypeClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportGroupTypeReportHeading.
    def enterReportGroupTypeReportHeading(self, ctx:CopyBookParser.ReportGroupTypeReportHeadingContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportGroupTypeReportHeading.
    def exitReportGroupTypeReportHeading(self, ctx:CopyBookParser.ReportGroupTypeReportHeadingContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportGroupTypePageHeading.
    def enterReportGroupTypePageHeading(self, ctx:CopyBookParser.ReportGroupTypePageHeadingContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportGroupTypePageHeading.
    def exitReportGroupTypePageHeading(self, ctx:CopyBookParser.ReportGroupTypePageHeadingContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportGroupTypeControlHeading.
    def enterReportGroupTypeControlHeading(self, ctx:CopyBookParser.ReportGroupTypeControlHeadingContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportGroupTypeControlHeading.
    def exitReportGroupTypeControlHeading(self, ctx:CopyBookParser.ReportGroupTypeControlHeadingContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportGroupTypeDetail.
    def enterReportGroupTypeDetail(self, ctx:CopyBookParser.ReportGroupTypeDetailContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportGroupTypeDetail.
    def exitReportGroupTypeDetail(self, ctx:CopyBookParser.ReportGroupTypeDetailContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportGroupTypeControlFooting.
    def enterReportGroupTypeControlFooting(self, ctx:CopyBookParser.ReportGroupTypeControlFootingContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportGroupTypeControlFooting.
    def exitReportGroupTypeControlFooting(self, ctx:CopyBookParser.ReportGroupTypeControlFootingContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportGroupUsageClause.
    def enterReportGroupUsageClause(self, ctx:CopyBookParser.ReportGroupUsageClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportGroupUsageClause.
    def exitReportGroupUsageClause(self, ctx:CopyBookParser.ReportGroupUsageClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportGroupTypePageFooting.
    def enterReportGroupTypePageFooting(self, ctx:CopyBookParser.ReportGroupTypePageFootingContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportGroupTypePageFooting.
    def exitReportGroupTypePageFooting(self, ctx:CopyBookParser.ReportGroupTypePageFootingContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportGroupTypeReportFooting.
    def enterReportGroupTypeReportFooting(self, ctx:CopyBookParser.ReportGroupTypeReportFootingContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportGroupTypeReportFooting.
    def exitReportGroupTypeReportFooting(self, ctx:CopyBookParser.ReportGroupTypeReportFootingContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportGroupValueClause.
    def enterReportGroupValueClause(self, ctx:CopyBookParser.ReportGroupValueClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportGroupValueClause.
    def exitReportGroupValueClause(self, ctx:CopyBookParser.ReportGroupValueClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#programLibrarySection.
    def enterProgramLibrarySection(self, ctx:CopyBookParser.ProgramLibrarySectionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#programLibrarySection.
    def exitProgramLibrarySection(self, ctx:CopyBookParser.ProgramLibrarySectionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#libraryDescriptionEntry.
    def enterLibraryDescriptionEntry(self, ctx:CopyBookParser.LibraryDescriptionEntryContext):
        pass

    # Exit a parse tree produced by CopyBookParser#libraryDescriptionEntry.
    def exitLibraryDescriptionEntry(self, ctx:CopyBookParser.LibraryDescriptionEntryContext):
        pass


    # Enter a parse tree produced by CopyBookParser#libraryDescriptionEntryFormat1.
    def enterLibraryDescriptionEntryFormat1(self, ctx:CopyBookParser.LibraryDescriptionEntryFormat1Context):
        pass

    # Exit a parse tree produced by CopyBookParser#libraryDescriptionEntryFormat1.
    def exitLibraryDescriptionEntryFormat1(self, ctx:CopyBookParser.LibraryDescriptionEntryFormat1Context):
        pass


    # Enter a parse tree produced by CopyBookParser#libraryDescriptionEntryFormat2.
    def enterLibraryDescriptionEntryFormat2(self, ctx:CopyBookParser.LibraryDescriptionEntryFormat2Context):
        pass

    # Exit a parse tree produced by CopyBookParser#libraryDescriptionEntryFormat2.
    def exitLibraryDescriptionEntryFormat2(self, ctx:CopyBookParser.LibraryDescriptionEntryFormat2Context):
        pass


    # Enter a parse tree produced by CopyBookParser#libraryAttributeClauseFormat1.
    def enterLibraryAttributeClauseFormat1(self, ctx:CopyBookParser.LibraryAttributeClauseFormat1Context):
        pass

    # Exit a parse tree produced by CopyBookParser#libraryAttributeClauseFormat1.
    def exitLibraryAttributeClauseFormat1(self, ctx:CopyBookParser.LibraryAttributeClauseFormat1Context):
        pass


    # Enter a parse tree produced by CopyBookParser#libraryAttributeClauseFormat2.
    def enterLibraryAttributeClauseFormat2(self, ctx:CopyBookParser.LibraryAttributeClauseFormat2Context):
        pass

    # Exit a parse tree produced by CopyBookParser#libraryAttributeClauseFormat2.
    def exitLibraryAttributeClauseFormat2(self, ctx:CopyBookParser.LibraryAttributeClauseFormat2Context):
        pass


    # Enter a parse tree produced by CopyBookParser#libraryAttributeFunction.
    def enterLibraryAttributeFunction(self, ctx:CopyBookParser.LibraryAttributeFunctionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#libraryAttributeFunction.
    def exitLibraryAttributeFunction(self, ctx:CopyBookParser.LibraryAttributeFunctionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#libraryAttributeParameter.
    def enterLibraryAttributeParameter(self, ctx:CopyBookParser.LibraryAttributeParameterContext):
        pass

    # Exit a parse tree produced by CopyBookParser#libraryAttributeParameter.
    def exitLibraryAttributeParameter(self, ctx:CopyBookParser.LibraryAttributeParameterContext):
        pass


    # Enter a parse tree produced by CopyBookParser#libraryAttributeTitle.
    def enterLibraryAttributeTitle(self, ctx:CopyBookParser.LibraryAttributeTitleContext):
        pass

    # Exit a parse tree produced by CopyBookParser#libraryAttributeTitle.
    def exitLibraryAttributeTitle(self, ctx:CopyBookParser.LibraryAttributeTitleContext):
        pass


    # Enter a parse tree produced by CopyBookParser#libraryEntryProcedureClauseFormat1.
    def enterLibraryEntryProcedureClauseFormat1(self, ctx:CopyBookParser.LibraryEntryProcedureClauseFormat1Context):
        pass

    # Exit a parse tree produced by CopyBookParser#libraryEntryProcedureClauseFormat1.
    def exitLibraryEntryProcedureClauseFormat1(self, ctx:CopyBookParser.LibraryEntryProcedureClauseFormat1Context):
        pass


    # Enter a parse tree produced by CopyBookParser#libraryEntryProcedureClauseFormat2.
    def enterLibraryEntryProcedureClauseFormat2(self, ctx:CopyBookParser.LibraryEntryProcedureClauseFormat2Context):
        pass

    # Exit a parse tree produced by CopyBookParser#libraryEntryProcedureClauseFormat2.
    def exitLibraryEntryProcedureClauseFormat2(self, ctx:CopyBookParser.LibraryEntryProcedureClauseFormat2Context):
        pass


    # Enter a parse tree produced by CopyBookParser#libraryEntryProcedureForClause.
    def enterLibraryEntryProcedureForClause(self, ctx:CopyBookParser.LibraryEntryProcedureForClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#libraryEntryProcedureForClause.
    def exitLibraryEntryProcedureForClause(self, ctx:CopyBookParser.LibraryEntryProcedureForClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#libraryEntryProcedureGivingClause.
    def enterLibraryEntryProcedureGivingClause(self, ctx:CopyBookParser.LibraryEntryProcedureGivingClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#libraryEntryProcedureGivingClause.
    def exitLibraryEntryProcedureGivingClause(self, ctx:CopyBookParser.LibraryEntryProcedureGivingClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#libraryEntryProcedureUsingClause.
    def enterLibraryEntryProcedureUsingClause(self, ctx:CopyBookParser.LibraryEntryProcedureUsingClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#libraryEntryProcedureUsingClause.
    def exitLibraryEntryProcedureUsingClause(self, ctx:CopyBookParser.LibraryEntryProcedureUsingClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#libraryEntryProcedureUsingName.
    def enterLibraryEntryProcedureUsingName(self, ctx:CopyBookParser.LibraryEntryProcedureUsingNameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#libraryEntryProcedureUsingName.
    def exitLibraryEntryProcedureUsingName(self, ctx:CopyBookParser.LibraryEntryProcedureUsingNameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#libraryEntryProcedureWithClause.
    def enterLibraryEntryProcedureWithClause(self, ctx:CopyBookParser.LibraryEntryProcedureWithClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#libraryEntryProcedureWithClause.
    def exitLibraryEntryProcedureWithClause(self, ctx:CopyBookParser.LibraryEntryProcedureWithClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#libraryEntryProcedureWithName.
    def enterLibraryEntryProcedureWithName(self, ctx:CopyBookParser.LibraryEntryProcedureWithNameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#libraryEntryProcedureWithName.
    def exitLibraryEntryProcedureWithName(self, ctx:CopyBookParser.LibraryEntryProcedureWithNameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#libraryIsCommonClause.
    def enterLibraryIsCommonClause(self, ctx:CopyBookParser.LibraryIsCommonClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#libraryIsCommonClause.
    def exitLibraryIsCommonClause(self, ctx:CopyBookParser.LibraryIsCommonClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#libraryIsGlobalClause.
    def enterLibraryIsGlobalClause(self, ctx:CopyBookParser.LibraryIsGlobalClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#libraryIsGlobalClause.
    def exitLibraryIsGlobalClause(self, ctx:CopyBookParser.LibraryIsGlobalClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataDescriptionEntry.
    def enterDataDescriptionEntry(self, ctx:CopyBookParser.DataDescriptionEntryContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataDescriptionEntry.
    def exitDataDescriptionEntry(self, ctx:CopyBookParser.DataDescriptionEntryContext):
        pass


    # Enter a parse tree produced by CopyBookParser#copyStatement.
    def enterCopyStatement(self, ctx:CopyBookParser.CopyStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#copyStatement.
    def exitCopyStatement(self, ctx:CopyBookParser.CopyStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#disjoinPhrase.
    def enterDisjoinPhrase(self, ctx:CopyBookParser.DisjoinPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#disjoinPhrase.
    def exitDisjoinPhrase(self, ctx:CopyBookParser.DisjoinPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#joinPhrase.
    def enterJoinPhrase(self, ctx:CopyBookParser.JoinPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#joinPhrase.
    def exitJoinPhrase(self, ctx:CopyBookParser.JoinPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#copySource.
    def enterCopySource(self, ctx:CopyBookParser.CopySourceContext):
        pass

    # Exit a parse tree produced by CopyBookParser#copySource.
    def exitCopySource(self, ctx:CopyBookParser.CopySourceContext):
        pass


    # Enter a parse tree produced by CopyBookParser#copyLibrary.
    def enterCopyLibrary(self, ctx:CopyBookParser.CopyLibraryContext):
        pass

    # Exit a parse tree produced by CopyBookParser#copyLibrary.
    def exitCopyLibrary(self, ctx:CopyBookParser.CopyLibraryContext):
        pass


    # Enter a parse tree produced by CopyBookParser#replacingPhrase.
    def enterReplacingPhrase(self, ctx:CopyBookParser.ReplacingPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#replacingPhrase.
    def exitReplacingPhrase(self, ctx:CopyBookParser.ReplacingPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#replaceArea.
    def enterReplaceArea(self, ctx:CopyBookParser.ReplaceAreaContext):
        pass

    # Exit a parse tree produced by CopyBookParser#replaceArea.
    def exitReplaceArea(self, ctx:CopyBookParser.ReplaceAreaContext):
        pass


    # Enter a parse tree produced by CopyBookParser#replaceByStatement.
    def enterReplaceByStatement(self, ctx:CopyBookParser.ReplaceByStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#replaceByStatement.
    def exitReplaceByStatement(self, ctx:CopyBookParser.ReplaceByStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#replaceOffStatement.
    def enterReplaceOffStatement(self, ctx:CopyBookParser.ReplaceOffStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#replaceOffStatement.
    def exitReplaceOffStatement(self, ctx:CopyBookParser.ReplaceOffStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#replaceClause.
    def enterReplaceClause(self, ctx:CopyBookParser.ReplaceClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#replaceClause.
    def exitReplaceClause(self, ctx:CopyBookParser.ReplaceClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#directoryPhrase.
    def enterDirectoryPhrase(self, ctx:CopyBookParser.DirectoryPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#directoryPhrase.
    def exitDirectoryPhrase(self, ctx:CopyBookParser.DirectoryPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#familyPhrase.
    def enterFamilyPhrase(self, ctx:CopyBookParser.FamilyPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#familyPhrase.
    def exitFamilyPhrase(self, ctx:CopyBookParser.FamilyPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#replaceable.
    def enterReplaceable(self, ctx:CopyBookParser.ReplaceableContext):
        pass

    # Exit a parse tree produced by CopyBookParser#replaceable.
    def exitReplaceable(self, ctx:CopyBookParser.ReplaceableContext):
        pass


    # Enter a parse tree produced by CopyBookParser#replacement.
    def enterReplacement(self, ctx:CopyBookParser.ReplacementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#replacement.
    def exitReplacement(self, ctx:CopyBookParser.ReplacementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#ejectStatement.
    def enterEjectStatement(self, ctx:CopyBookParser.EjectStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#ejectStatement.
    def exitEjectStatement(self, ctx:CopyBookParser.EjectStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#skipStatement.
    def enterSkipStatement(self, ctx:CopyBookParser.SkipStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#skipStatement.
    def exitSkipStatement(self, ctx:CopyBookParser.SkipStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#titleStatement.
    def enterTitleStatement(self, ctx:CopyBookParser.TitleStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#titleStatement.
    def exitTitleStatement(self, ctx:CopyBookParser.TitleStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#pseudoText.
    def enterPseudoText(self, ctx:CopyBookParser.PseudoTextContext):
        pass

    # Exit a parse tree produced by CopyBookParser#pseudoText.
    def exitPseudoText(self, ctx:CopyBookParser.PseudoTextContext):
        pass


    # Enter a parse tree produced by CopyBookParser#charData.
    def enterCharData(self, ctx:CopyBookParser.CharDataContext):
        pass

    # Exit a parse tree produced by CopyBookParser#charData.
    def exitCharData(self, ctx:CopyBookParser.CharDataContext):
        pass


    # Enter a parse tree produced by CopyBookParser#charDataSql.
    def enterCharDataSql(self, ctx:CopyBookParser.CharDataSqlContext):
        pass

    # Exit a parse tree produced by CopyBookParser#charDataSql.
    def exitCharDataSql(self, ctx:CopyBookParser.CharDataSqlContext):
        pass


    # Enter a parse tree produced by CopyBookParser#charDataLine.
    def enterCharDataLine(self, ctx:CopyBookParser.CharDataLineContext):
        pass

    # Exit a parse tree produced by CopyBookParser#charDataLine.
    def exitCharDataLine(self, ctx:CopyBookParser.CharDataLineContext):
        pass


    # Enter a parse tree produced by CopyBookParser#cobolWord.
    def enterCobolWord(self, ctx:CopyBookParser.CobolWordContext):
        pass

    # Exit a parse tree produced by CopyBookParser#cobolWord.
    def exitCobolWord(self, ctx:CopyBookParser.CobolWordContext):
        pass


    # Enter a parse tree produced by CopyBookParser#literal.
    def enterLiteral(self, ctx:CopyBookParser.LiteralContext):
        pass

    # Exit a parse tree produced by CopyBookParser#literal.
    def exitLiteral(self, ctx:CopyBookParser.LiteralContext):
        pass


    # Enter a parse tree produced by CopyBookParser#jpEncodingText.
    def enterJpEncodingText(self, ctx:CopyBookParser.JpEncodingTextContext):
        pass

    # Exit a parse tree produced by CopyBookParser#jpEncodingText.
    def exitJpEncodingText(self, ctx:CopyBookParser.JpEncodingTextContext):
        pass


    # Enter a parse tree produced by CopyBookParser#filename.
    def enterFilename(self, ctx:CopyBookParser.FilenameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#filename.
    def exitFilename(self, ctx:CopyBookParser.FilenameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataDescriptionEntryFormat1.
    def enterDataDescriptionEntryFormat1(self, ctx:CopyBookParser.DataDescriptionEntryFormat1Context):
        pass

    # Exit a parse tree produced by CopyBookParser#dataDescriptionEntryFormat1.
    def exitDataDescriptionEntryFormat1(self, ctx:CopyBookParser.DataDescriptionEntryFormat1Context):
        pass


    # Enter a parse tree produced by CopyBookParser#dataSqlTypeClause.
    def enterDataSqlTypeClause(self, ctx:CopyBookParser.DataSqlTypeClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataSqlTypeClause.
    def exitDataSqlTypeClause(self, ctx:CopyBookParser.DataSqlTypeClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#sqlDataType.
    def enterSqlDataType(self, ctx:CopyBookParser.SqlDataTypeContext):
        pass

    # Exit a parse tree produced by CopyBookParser#sqlDataType.
    def exitSqlDataType(self, ctx:CopyBookParser.SqlDataTypeContext):
        pass


    # Enter a parse tree produced by CopyBookParser#sqlDataLenght.
    def enterSqlDataLenght(self, ctx:CopyBookParser.SqlDataLenghtContext):
        pass

    # Exit a parse tree produced by CopyBookParser#sqlDataLenght.
    def exitSqlDataLenght(self, ctx:CopyBookParser.SqlDataLenghtContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataCharacterClause.
    def enterDataCharacterClause(self, ctx:CopyBookParser.DataCharacterClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataCharacterClause.
    def exitDataCharacterClause(self, ctx:CopyBookParser.DataCharacterClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataDescriptionEntryFormat2.
    def enterDataDescriptionEntryFormat2(self, ctx:CopyBookParser.DataDescriptionEntryFormat2Context):
        pass

    # Exit a parse tree produced by CopyBookParser#dataDescriptionEntryFormat2.
    def exitDataDescriptionEntryFormat2(self, ctx:CopyBookParser.DataDescriptionEntryFormat2Context):
        pass


    # Enter a parse tree produced by CopyBookParser#dataDescriptionEntryFormat3.
    def enterDataDescriptionEntryFormat3(self, ctx:CopyBookParser.DataDescriptionEntryFormat3Context):
        pass

    # Exit a parse tree produced by CopyBookParser#dataDescriptionEntryFormat3.
    def exitDataDescriptionEntryFormat3(self, ctx:CopyBookParser.DataDescriptionEntryFormat3Context):
        pass


    # Enter a parse tree produced by CopyBookParser#dataDescriptionEntryExecSql.
    def enterDataDescriptionEntryExecSql(self, ctx:CopyBookParser.DataDescriptionEntryExecSqlContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataDescriptionEntryExecSql.
    def exitDataDescriptionEntryExecSql(self, ctx:CopyBookParser.DataDescriptionEntryExecSqlContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataAlignedClause.
    def enterDataAlignedClause(self, ctx:CopyBookParser.DataAlignedClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataAlignedClause.
    def exitDataAlignedClause(self, ctx:CopyBookParser.DataAlignedClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataBlankWhenZeroClause.
    def enterDataBlankWhenZeroClause(self, ctx:CopyBookParser.DataBlankWhenZeroClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataBlankWhenZeroClause.
    def exitDataBlankWhenZeroClause(self, ctx:CopyBookParser.DataBlankWhenZeroClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataCommonOwnLocalClause.
    def enterDataCommonOwnLocalClause(self, ctx:CopyBookParser.DataCommonOwnLocalClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataCommonOwnLocalClause.
    def exitDataCommonOwnLocalClause(self, ctx:CopyBookParser.DataCommonOwnLocalClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataExternalClause.
    def enterDataExternalClause(self, ctx:CopyBookParser.DataExternalClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataExternalClause.
    def exitDataExternalClause(self, ctx:CopyBookParser.DataExternalClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataGlobalClause.
    def enterDataGlobalClause(self, ctx:CopyBookParser.DataGlobalClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataGlobalClause.
    def exitDataGlobalClause(self, ctx:CopyBookParser.DataGlobalClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataIntegerStringClause.
    def enterDataIntegerStringClause(self, ctx:CopyBookParser.DataIntegerStringClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataIntegerStringClause.
    def exitDataIntegerStringClause(self, ctx:CopyBookParser.DataIntegerStringClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataJustifiedClause.
    def enterDataJustifiedClause(self, ctx:CopyBookParser.DataJustifiedClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataJustifiedClause.
    def exitDataJustifiedClause(self, ctx:CopyBookParser.DataJustifiedClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataOccursClause.
    def enterDataOccursClause(self, ctx:CopyBookParser.DataOccursClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataOccursClause.
    def exitDataOccursClause(self, ctx:CopyBookParser.DataOccursClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataOccursTo.
    def enterDataOccursTo(self, ctx:CopyBookParser.DataOccursToContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataOccursTo.
    def exitDataOccursTo(self, ctx:CopyBookParser.DataOccursToContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataOccursSort.
    def enterDataOccursSort(self, ctx:CopyBookParser.DataOccursSortContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataOccursSort.
    def exitDataOccursSort(self, ctx:CopyBookParser.DataOccursSortContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataPictureClause.
    def enterDataPictureClause(self, ctx:CopyBookParser.DataPictureClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataPictureClause.
    def exitDataPictureClause(self, ctx:CopyBookParser.DataPictureClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#pictureString.
    def enterPictureString(self, ctx:CopyBookParser.PictureStringContext):
        pass

    # Exit a parse tree produced by CopyBookParser#pictureString.
    def exitPictureString(self, ctx:CopyBookParser.PictureStringContext):
        pass


    # Enter a parse tree produced by CopyBookParser#pictureChars.
    def enterPictureChars(self, ctx:CopyBookParser.PictureCharsContext):
        pass

    # Exit a parse tree produced by CopyBookParser#pictureChars.
    def exitPictureChars(self, ctx:CopyBookParser.PictureCharsContext):
        pass


    # Enter a parse tree produced by CopyBookParser#pictureCardinality.
    def enterPictureCardinality(self, ctx:CopyBookParser.PictureCardinalityContext):
        pass

    # Exit a parse tree produced by CopyBookParser#pictureCardinality.
    def exitPictureCardinality(self, ctx:CopyBookParser.PictureCardinalityContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataReceivedByClause.
    def enterDataReceivedByClause(self, ctx:CopyBookParser.DataReceivedByClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataReceivedByClause.
    def exitDataReceivedByClause(self, ctx:CopyBookParser.DataReceivedByClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataRecordAreaClause.
    def enterDataRecordAreaClause(self, ctx:CopyBookParser.DataRecordAreaClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataRecordAreaClause.
    def exitDataRecordAreaClause(self, ctx:CopyBookParser.DataRecordAreaClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataRedefinesClause.
    def enterDataRedefinesClause(self, ctx:CopyBookParser.DataRedefinesClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataRedefinesClause.
    def exitDataRedefinesClause(self, ctx:CopyBookParser.DataRedefinesClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataRenamesClause.
    def enterDataRenamesClause(self, ctx:CopyBookParser.DataRenamesClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataRenamesClause.
    def exitDataRenamesClause(self, ctx:CopyBookParser.DataRenamesClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataSignClause.
    def enterDataSignClause(self, ctx:CopyBookParser.DataSignClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataSignClause.
    def exitDataSignClause(self, ctx:CopyBookParser.DataSignClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataSynchronizedClause.
    def enterDataSynchronizedClause(self, ctx:CopyBookParser.DataSynchronizedClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataSynchronizedClause.
    def exitDataSynchronizedClause(self, ctx:CopyBookParser.DataSynchronizedClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataThreadLocalClause.
    def enterDataThreadLocalClause(self, ctx:CopyBookParser.DataThreadLocalClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataThreadLocalClause.
    def exitDataThreadLocalClause(self, ctx:CopyBookParser.DataThreadLocalClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataTypeClause.
    def enterDataTypeClause(self, ctx:CopyBookParser.DataTypeClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataTypeClause.
    def exitDataTypeClause(self, ctx:CopyBookParser.DataTypeClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataTypeDefClause.
    def enterDataTypeDefClause(self, ctx:CopyBookParser.DataTypeDefClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataTypeDefClause.
    def exitDataTypeDefClause(self, ctx:CopyBookParser.DataTypeDefClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataUsageClause.
    def enterDataUsageClause(self, ctx:CopyBookParser.DataUsageClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataUsageClause.
    def exitDataUsageClause(self, ctx:CopyBookParser.DataUsageClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataUsingClause.
    def enterDataUsingClause(self, ctx:CopyBookParser.DataUsingClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataUsingClause.
    def exitDataUsingClause(self, ctx:CopyBookParser.DataUsingClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataValueClause.
    def enterDataValueClause(self, ctx:CopyBookParser.DataValueClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataValueClause.
    def exitDataValueClause(self, ctx:CopyBookParser.DataValueClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataValueInterval.
    def enterDataValueInterval(self, ctx:CopyBookParser.DataValueIntervalContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataValueInterval.
    def exitDataValueInterval(self, ctx:CopyBookParser.DataValueIntervalContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataValueIntervalFrom.
    def enterDataValueIntervalFrom(self, ctx:CopyBookParser.DataValueIntervalFromContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataValueIntervalFrom.
    def exitDataValueIntervalFrom(self, ctx:CopyBookParser.DataValueIntervalFromContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataValueIntervalTo.
    def enterDataValueIntervalTo(self, ctx:CopyBookParser.DataValueIntervalToContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataValueIntervalTo.
    def exitDataValueIntervalTo(self, ctx:CopyBookParser.DataValueIntervalToContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataWithLowerBoundsClause.
    def enterDataWithLowerBoundsClause(self, ctx:CopyBookParser.DataWithLowerBoundsClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataWithLowerBoundsClause.
    def exitDataWithLowerBoundsClause(self, ctx:CopyBookParser.DataWithLowerBoundsClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#procedureDivision.
    def enterProcedureDivision(self, ctx:CopyBookParser.ProcedureDivisionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#procedureDivision.
    def exitProcedureDivision(self, ctx:CopyBookParser.ProcedureDivisionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#procedureDivisionUsingClause.
    def enterProcedureDivisionUsingClause(self, ctx:CopyBookParser.ProcedureDivisionUsingClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#procedureDivisionUsingClause.
    def exitProcedureDivisionUsingClause(self, ctx:CopyBookParser.ProcedureDivisionUsingClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#procedureDivisionGivingClause.
    def enterProcedureDivisionGivingClause(self, ctx:CopyBookParser.ProcedureDivisionGivingClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#procedureDivisionGivingClause.
    def exitProcedureDivisionGivingClause(self, ctx:CopyBookParser.ProcedureDivisionGivingClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#procedureDivisionUsingParameter.
    def enterProcedureDivisionUsingParameter(self, ctx:CopyBookParser.ProcedureDivisionUsingParameterContext):
        pass

    # Exit a parse tree produced by CopyBookParser#procedureDivisionUsingParameter.
    def exitProcedureDivisionUsingParameter(self, ctx:CopyBookParser.ProcedureDivisionUsingParameterContext):
        pass


    # Enter a parse tree produced by CopyBookParser#procedureDivisionByReferencePhrase.
    def enterProcedureDivisionByReferencePhrase(self, ctx:CopyBookParser.ProcedureDivisionByReferencePhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#procedureDivisionByReferencePhrase.
    def exitProcedureDivisionByReferencePhrase(self, ctx:CopyBookParser.ProcedureDivisionByReferencePhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#procedureDivisionByReference.
    def enterProcedureDivisionByReference(self, ctx:CopyBookParser.ProcedureDivisionByReferenceContext):
        pass

    # Exit a parse tree produced by CopyBookParser#procedureDivisionByReference.
    def exitProcedureDivisionByReference(self, ctx:CopyBookParser.ProcedureDivisionByReferenceContext):
        pass


    # Enter a parse tree produced by CopyBookParser#procedureDivisionByValuePhrase.
    def enterProcedureDivisionByValuePhrase(self, ctx:CopyBookParser.ProcedureDivisionByValuePhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#procedureDivisionByValuePhrase.
    def exitProcedureDivisionByValuePhrase(self, ctx:CopyBookParser.ProcedureDivisionByValuePhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#procedureDivisionByValue.
    def enterProcedureDivisionByValue(self, ctx:CopyBookParser.ProcedureDivisionByValueContext):
        pass

    # Exit a parse tree produced by CopyBookParser#procedureDivisionByValue.
    def exitProcedureDivisionByValue(self, ctx:CopyBookParser.ProcedureDivisionByValueContext):
        pass


    # Enter a parse tree produced by CopyBookParser#procedureDeclaratives.
    def enterProcedureDeclaratives(self, ctx:CopyBookParser.ProcedureDeclarativesContext):
        pass

    # Exit a parse tree produced by CopyBookParser#procedureDeclaratives.
    def exitProcedureDeclaratives(self, ctx:CopyBookParser.ProcedureDeclarativesContext):
        pass


    # Enter a parse tree produced by CopyBookParser#procedureDeclarative.
    def enterProcedureDeclarative(self, ctx:CopyBookParser.ProcedureDeclarativeContext):
        pass

    # Exit a parse tree produced by CopyBookParser#procedureDeclarative.
    def exitProcedureDeclarative(self, ctx:CopyBookParser.ProcedureDeclarativeContext):
        pass


    # Enter a parse tree produced by CopyBookParser#procedureSectionHeader.
    def enterProcedureSectionHeader(self, ctx:CopyBookParser.ProcedureSectionHeaderContext):
        pass

    # Exit a parse tree produced by CopyBookParser#procedureSectionHeader.
    def exitProcedureSectionHeader(self, ctx:CopyBookParser.ProcedureSectionHeaderContext):
        pass


    # Enter a parse tree produced by CopyBookParser#procedureDivisionBody.
    def enterProcedureDivisionBody(self, ctx:CopyBookParser.ProcedureDivisionBodyContext):
        pass

    # Exit a parse tree produced by CopyBookParser#procedureDivisionBody.
    def exitProcedureDivisionBody(self, ctx:CopyBookParser.ProcedureDivisionBodyContext):
        pass


    # Enter a parse tree produced by CopyBookParser#procedureSection.
    def enterProcedureSection(self, ctx:CopyBookParser.ProcedureSectionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#procedureSection.
    def exitProcedureSection(self, ctx:CopyBookParser.ProcedureSectionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#paragraphs.
    def enterParagraphs(self, ctx:CopyBookParser.ParagraphsContext):
        pass

    # Exit a parse tree produced by CopyBookParser#paragraphs.
    def exitParagraphs(self, ctx:CopyBookParser.ParagraphsContext):
        pass


    # Enter a parse tree produced by CopyBookParser#paragraph.
    def enterParagraph(self, ctx:CopyBookParser.ParagraphContext):
        pass

    # Exit a parse tree produced by CopyBookParser#paragraph.
    def exitParagraph(self, ctx:CopyBookParser.ParagraphContext):
        pass


    # Enter a parse tree produced by CopyBookParser#sentence.
    def enterSentence(self, ctx:CopyBookParser.SentenceContext):
        pass

    # Exit a parse tree produced by CopyBookParser#sentence.
    def exitSentence(self, ctx:CopyBookParser.SentenceContext):
        pass


    # Enter a parse tree produced by CopyBookParser#statement.
    def enterStatement(self, ctx:CopyBookParser.StatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#statement.
    def exitStatement(self, ctx:CopyBookParser.StatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#xmlParseStatement.
    def enterXmlParseStatement(self, ctx:CopyBookParser.XmlParseStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#xmlParseStatement.
    def exitXmlParseStatement(self, ctx:CopyBookParser.XmlParseStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#xmlDataname.
    def enterXmlDataname(self, ctx:CopyBookParser.XmlDatanameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#xmlDataname.
    def exitXmlDataname(self, ctx:CopyBookParser.XmlDatanameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#xmlProcessingProcedure.
    def enterXmlProcessingProcedure(self, ctx:CopyBookParser.XmlProcessingProcedureContext):
        pass

    # Exit a parse tree produced by CopyBookParser#xmlProcessingProcedure.
    def exitXmlProcessingProcedure(self, ctx:CopyBookParser.XmlProcessingProcedureContext):
        pass


    # Enter a parse tree produced by CopyBookParser#endXml.
    def enterEndXml(self, ctx:CopyBookParser.EndXmlContext):
        pass

    # Exit a parse tree produced by CopyBookParser#endXml.
    def exitEndXml(self, ctx:CopyBookParser.EndXmlContext):
        pass


    # Enter a parse tree produced by CopyBookParser#execSqlStatement2.
    def enterExecSqlStatement2(self, ctx:CopyBookParser.ExecSqlStatement2Context):
        pass

    # Exit a parse tree produced by CopyBookParser#execSqlStatement2.
    def exitExecSqlStatement2(self, ctx:CopyBookParser.ExecSqlStatement2Context):
        pass


    # Enter a parse tree produced by CopyBookParser#sqlCode.
    def enterSqlCode(self, ctx:CopyBookParser.SqlCodeContext):
        pass

    # Exit a parse tree produced by CopyBookParser#sqlCode.
    def exitSqlCode(self, ctx:CopyBookParser.SqlCodeContext):
        pass


    # Enter a parse tree produced by CopyBookParser#execCicsStatement2.
    def enterExecCicsStatement2(self, ctx:CopyBookParser.ExecCicsStatement2Context):
        pass

    # Exit a parse tree produced by CopyBookParser#execCicsStatement2.
    def exitExecCicsStatement2(self, ctx:CopyBookParser.ExecCicsStatement2Context):
        pass


    # Enter a parse tree produced by CopyBookParser#commandName.
    def enterCommandName(self, ctx:CopyBookParser.CommandNameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#commandName.
    def exitCommandName(self, ctx:CopyBookParser.CommandNameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#commandBody.
    def enterCommandBody(self, ctx:CopyBookParser.CommandBodyContext):
        pass

    # Exit a parse tree produced by CopyBookParser#commandBody.
    def exitCommandBody(self, ctx:CopyBookParser.CommandBodyContext):
        pass


    # Enter a parse tree produced by CopyBookParser#commandParameter.
    def enterCommandParameter(self, ctx:CopyBookParser.CommandParameterContext):
        pass

    # Exit a parse tree produced by CopyBookParser#commandParameter.
    def exitCommandParameter(self, ctx:CopyBookParser.CommandParameterContext):
        pass


    # Enter a parse tree produced by CopyBookParser#parameterName.
    def enterParameterName(self, ctx:CopyBookParser.ParameterNameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#parameterName.
    def exitParameterName(self, ctx:CopyBookParser.ParameterNameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#parameterNameWithIndex.
    def enterParameterNameWithIndex(self, ctx:CopyBookParser.ParameterNameWithIndexContext):
        pass

    # Exit a parse tree produced by CopyBookParser#parameterNameWithIndex.
    def exitParameterNameWithIndex(self, ctx:CopyBookParser.ParameterNameWithIndexContext):
        pass


    # Enter a parse tree produced by CopyBookParser#parameterValueWithIndex.
    def enterParameterValueWithIndex(self, ctx:CopyBookParser.ParameterValueWithIndexContext):
        pass

    # Exit a parse tree produced by CopyBookParser#parameterValueWithIndex.
    def exitParameterValueWithIndex(self, ctx:CopyBookParser.ParameterValueWithIndexContext):
        pass


    # Enter a parse tree produced by CopyBookParser#parameterValue.
    def enterParameterValue(self, ctx:CopyBookParser.ParameterValueContext):
        pass

    # Exit a parse tree produced by CopyBookParser#parameterValue.
    def exitParameterValue(self, ctx:CopyBookParser.ParameterValueContext):
        pass


    # Enter a parse tree produced by CopyBookParser#acceptStatement.
    def enterAcceptStatement(self, ctx:CopyBookParser.AcceptStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#acceptStatement.
    def exitAcceptStatement(self, ctx:CopyBookParser.AcceptStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#acceptFromDateStatement.
    def enterAcceptFromDateStatement(self, ctx:CopyBookParser.AcceptFromDateStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#acceptFromDateStatement.
    def exitAcceptFromDateStatement(self, ctx:CopyBookParser.AcceptFromDateStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#acceptFromMnemonicStatement.
    def enterAcceptFromMnemonicStatement(self, ctx:CopyBookParser.AcceptFromMnemonicStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#acceptFromMnemonicStatement.
    def exitAcceptFromMnemonicStatement(self, ctx:CopyBookParser.AcceptFromMnemonicStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#acceptFromEscapeKeyStatement.
    def enterAcceptFromEscapeKeyStatement(self, ctx:CopyBookParser.AcceptFromEscapeKeyStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#acceptFromEscapeKeyStatement.
    def exitAcceptFromEscapeKeyStatement(self, ctx:CopyBookParser.AcceptFromEscapeKeyStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#acceptMessageCountStatement.
    def enterAcceptMessageCountStatement(self, ctx:CopyBookParser.AcceptMessageCountStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#acceptMessageCountStatement.
    def exitAcceptMessageCountStatement(self, ctx:CopyBookParser.AcceptMessageCountStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#addStatement.
    def enterAddStatement(self, ctx:CopyBookParser.AddStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#addStatement.
    def exitAddStatement(self, ctx:CopyBookParser.AddStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#addToStatement.
    def enterAddToStatement(self, ctx:CopyBookParser.AddToStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#addToStatement.
    def exitAddToStatement(self, ctx:CopyBookParser.AddToStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#addToGivingStatement.
    def enterAddToGivingStatement(self, ctx:CopyBookParser.AddToGivingStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#addToGivingStatement.
    def exitAddToGivingStatement(self, ctx:CopyBookParser.AddToGivingStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#addCorrespondingStatement.
    def enterAddCorrespondingStatement(self, ctx:CopyBookParser.AddCorrespondingStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#addCorrespondingStatement.
    def exitAddCorrespondingStatement(self, ctx:CopyBookParser.AddCorrespondingStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#addFrom.
    def enterAddFrom(self, ctx:CopyBookParser.AddFromContext):
        pass

    # Exit a parse tree produced by CopyBookParser#addFrom.
    def exitAddFrom(self, ctx:CopyBookParser.AddFromContext):
        pass


    # Enter a parse tree produced by CopyBookParser#addTo.
    def enterAddTo(self, ctx:CopyBookParser.AddToContext):
        pass

    # Exit a parse tree produced by CopyBookParser#addTo.
    def exitAddTo(self, ctx:CopyBookParser.AddToContext):
        pass


    # Enter a parse tree produced by CopyBookParser#addToGiving.
    def enterAddToGiving(self, ctx:CopyBookParser.AddToGivingContext):
        pass

    # Exit a parse tree produced by CopyBookParser#addToGiving.
    def exitAddToGiving(self, ctx:CopyBookParser.AddToGivingContext):
        pass


    # Enter a parse tree produced by CopyBookParser#addGiving.
    def enterAddGiving(self, ctx:CopyBookParser.AddGivingContext):
        pass

    # Exit a parse tree produced by CopyBookParser#addGiving.
    def exitAddGiving(self, ctx:CopyBookParser.AddGivingContext):
        pass


    # Enter a parse tree produced by CopyBookParser#alteredGoTo.
    def enterAlteredGoTo(self, ctx:CopyBookParser.AlteredGoToContext):
        pass

    # Exit a parse tree produced by CopyBookParser#alteredGoTo.
    def exitAlteredGoTo(self, ctx:CopyBookParser.AlteredGoToContext):
        pass


    # Enter a parse tree produced by CopyBookParser#alterStatement.
    def enterAlterStatement(self, ctx:CopyBookParser.AlterStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#alterStatement.
    def exitAlterStatement(self, ctx:CopyBookParser.AlterStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#alterProceedTo.
    def enterAlterProceedTo(self, ctx:CopyBookParser.AlterProceedToContext):
        pass

    # Exit a parse tree produced by CopyBookParser#alterProceedTo.
    def exitAlterProceedTo(self, ctx:CopyBookParser.AlterProceedToContext):
        pass


    # Enter a parse tree produced by CopyBookParser#callStatement.
    def enterCallStatement(self, ctx:CopyBookParser.CallStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#callStatement.
    def exitCallStatement(self, ctx:CopyBookParser.CallStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#callUsingPhrase.
    def enterCallUsingPhrase(self, ctx:CopyBookParser.CallUsingPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#callUsingPhrase.
    def exitCallUsingPhrase(self, ctx:CopyBookParser.CallUsingPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#callUsingParameter.
    def enterCallUsingParameter(self, ctx:CopyBookParser.CallUsingParameterContext):
        pass

    # Exit a parse tree produced by CopyBookParser#callUsingParameter.
    def exitCallUsingParameter(self, ctx:CopyBookParser.CallUsingParameterContext):
        pass


    # Enter a parse tree produced by CopyBookParser#callByReferencePhrase.
    def enterCallByReferencePhrase(self, ctx:CopyBookParser.CallByReferencePhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#callByReferencePhrase.
    def exitCallByReferencePhrase(self, ctx:CopyBookParser.CallByReferencePhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#callByReference.
    def enterCallByReference(self, ctx:CopyBookParser.CallByReferenceContext):
        pass

    # Exit a parse tree produced by CopyBookParser#callByReference.
    def exitCallByReference(self, ctx:CopyBookParser.CallByReferenceContext):
        pass


    # Enter a parse tree produced by CopyBookParser#callByValuePhrase.
    def enterCallByValuePhrase(self, ctx:CopyBookParser.CallByValuePhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#callByValuePhrase.
    def exitCallByValuePhrase(self, ctx:CopyBookParser.CallByValuePhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#callByValue.
    def enterCallByValue(self, ctx:CopyBookParser.CallByValueContext):
        pass

    # Exit a parse tree produced by CopyBookParser#callByValue.
    def exitCallByValue(self, ctx:CopyBookParser.CallByValueContext):
        pass


    # Enter a parse tree produced by CopyBookParser#callByContentPhrase.
    def enterCallByContentPhrase(self, ctx:CopyBookParser.CallByContentPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#callByContentPhrase.
    def exitCallByContentPhrase(self, ctx:CopyBookParser.CallByContentPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#callByContent.
    def enterCallByContent(self, ctx:CopyBookParser.CallByContentContext):
        pass

    # Exit a parse tree produced by CopyBookParser#callByContent.
    def exitCallByContent(self, ctx:CopyBookParser.CallByContentContext):
        pass


    # Enter a parse tree produced by CopyBookParser#callGivingPhrase.
    def enterCallGivingPhrase(self, ctx:CopyBookParser.CallGivingPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#callGivingPhrase.
    def exitCallGivingPhrase(self, ctx:CopyBookParser.CallGivingPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#cancelStatement.
    def enterCancelStatement(self, ctx:CopyBookParser.CancelStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#cancelStatement.
    def exitCancelStatement(self, ctx:CopyBookParser.CancelStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#cancelCall.
    def enterCancelCall(self, ctx:CopyBookParser.CancelCallContext):
        pass

    # Exit a parse tree produced by CopyBookParser#cancelCall.
    def exitCancelCall(self, ctx:CopyBookParser.CancelCallContext):
        pass


    # Enter a parse tree produced by CopyBookParser#closeStatement.
    def enterCloseStatement(self, ctx:CopyBookParser.CloseStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#closeStatement.
    def exitCloseStatement(self, ctx:CopyBookParser.CloseStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#closeFile.
    def enterCloseFile(self, ctx:CopyBookParser.CloseFileContext):
        pass

    # Exit a parse tree produced by CopyBookParser#closeFile.
    def exitCloseFile(self, ctx:CopyBookParser.CloseFileContext):
        pass


    # Enter a parse tree produced by CopyBookParser#closeReelUnitStatement.
    def enterCloseReelUnitStatement(self, ctx:CopyBookParser.CloseReelUnitStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#closeReelUnitStatement.
    def exitCloseReelUnitStatement(self, ctx:CopyBookParser.CloseReelUnitStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#closeRelativeStatement.
    def enterCloseRelativeStatement(self, ctx:CopyBookParser.CloseRelativeStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#closeRelativeStatement.
    def exitCloseRelativeStatement(self, ctx:CopyBookParser.CloseRelativeStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#closePortFileIOStatement.
    def enterClosePortFileIOStatement(self, ctx:CopyBookParser.ClosePortFileIOStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#closePortFileIOStatement.
    def exitClosePortFileIOStatement(self, ctx:CopyBookParser.ClosePortFileIOStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#closePortFileIOUsing.
    def enterClosePortFileIOUsing(self, ctx:CopyBookParser.ClosePortFileIOUsingContext):
        pass

    # Exit a parse tree produced by CopyBookParser#closePortFileIOUsing.
    def exitClosePortFileIOUsing(self, ctx:CopyBookParser.ClosePortFileIOUsingContext):
        pass


    # Enter a parse tree produced by CopyBookParser#closePortFileIOUsingCloseDisposition.
    def enterClosePortFileIOUsingCloseDisposition(self, ctx:CopyBookParser.ClosePortFileIOUsingCloseDispositionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#closePortFileIOUsingCloseDisposition.
    def exitClosePortFileIOUsingCloseDisposition(self, ctx:CopyBookParser.ClosePortFileIOUsingCloseDispositionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#closePortFileIOUsingAssociatedData.
    def enterClosePortFileIOUsingAssociatedData(self, ctx:CopyBookParser.ClosePortFileIOUsingAssociatedDataContext):
        pass

    # Exit a parse tree produced by CopyBookParser#closePortFileIOUsingAssociatedData.
    def exitClosePortFileIOUsingAssociatedData(self, ctx:CopyBookParser.ClosePortFileIOUsingAssociatedDataContext):
        pass


    # Enter a parse tree produced by CopyBookParser#closePortFileIOUsingAssociatedDataLength.
    def enterClosePortFileIOUsingAssociatedDataLength(self, ctx:CopyBookParser.ClosePortFileIOUsingAssociatedDataLengthContext):
        pass

    # Exit a parse tree produced by CopyBookParser#closePortFileIOUsingAssociatedDataLength.
    def exitClosePortFileIOUsingAssociatedDataLength(self, ctx:CopyBookParser.ClosePortFileIOUsingAssociatedDataLengthContext):
        pass


    # Enter a parse tree produced by CopyBookParser#computeStatement.
    def enterComputeStatement(self, ctx:CopyBookParser.ComputeStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#computeStatement.
    def exitComputeStatement(self, ctx:CopyBookParser.ComputeStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#computeStore.
    def enterComputeStore(self, ctx:CopyBookParser.ComputeStoreContext):
        pass

    # Exit a parse tree produced by CopyBookParser#computeStore.
    def exitComputeStore(self, ctx:CopyBookParser.ComputeStoreContext):
        pass


    # Enter a parse tree produced by CopyBookParser#continueStatement.
    def enterContinueStatement(self, ctx:CopyBookParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#continueStatement.
    def exitContinueStatement(self, ctx:CopyBookParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#deleteStatement.
    def enterDeleteStatement(self, ctx:CopyBookParser.DeleteStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#deleteStatement.
    def exitDeleteStatement(self, ctx:CopyBookParser.DeleteStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#disableStatement.
    def enterDisableStatement(self, ctx:CopyBookParser.DisableStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#disableStatement.
    def exitDisableStatement(self, ctx:CopyBookParser.DisableStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#displayStatement.
    def enterDisplayStatement(self, ctx:CopyBookParser.DisplayStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#displayStatement.
    def exitDisplayStatement(self, ctx:CopyBookParser.DisplayStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#displayOperand.
    def enterDisplayOperand(self, ctx:CopyBookParser.DisplayOperandContext):
        pass

    # Exit a parse tree produced by CopyBookParser#displayOperand.
    def exitDisplayOperand(self, ctx:CopyBookParser.DisplayOperandContext):
        pass


    # Enter a parse tree produced by CopyBookParser#displayAt.
    def enterDisplayAt(self, ctx:CopyBookParser.DisplayAtContext):
        pass

    # Exit a parse tree produced by CopyBookParser#displayAt.
    def exitDisplayAt(self, ctx:CopyBookParser.DisplayAtContext):
        pass


    # Enter a parse tree produced by CopyBookParser#displayUpon.
    def enterDisplayUpon(self, ctx:CopyBookParser.DisplayUponContext):
        pass

    # Exit a parse tree produced by CopyBookParser#displayUpon.
    def exitDisplayUpon(self, ctx:CopyBookParser.DisplayUponContext):
        pass


    # Enter a parse tree produced by CopyBookParser#displayWith.
    def enterDisplayWith(self, ctx:CopyBookParser.DisplayWithContext):
        pass

    # Exit a parse tree produced by CopyBookParser#displayWith.
    def exitDisplayWith(self, ctx:CopyBookParser.DisplayWithContext):
        pass


    # Enter a parse tree produced by CopyBookParser#divideStatement.
    def enterDivideStatement(self, ctx:CopyBookParser.DivideStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#divideStatement.
    def exitDivideStatement(self, ctx:CopyBookParser.DivideStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#divideIntoStatement.
    def enterDivideIntoStatement(self, ctx:CopyBookParser.DivideIntoStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#divideIntoStatement.
    def exitDivideIntoStatement(self, ctx:CopyBookParser.DivideIntoStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#divideIntoGivingStatement.
    def enterDivideIntoGivingStatement(self, ctx:CopyBookParser.DivideIntoGivingStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#divideIntoGivingStatement.
    def exitDivideIntoGivingStatement(self, ctx:CopyBookParser.DivideIntoGivingStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#divideByGivingStatement.
    def enterDivideByGivingStatement(self, ctx:CopyBookParser.DivideByGivingStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#divideByGivingStatement.
    def exitDivideByGivingStatement(self, ctx:CopyBookParser.DivideByGivingStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#divideGivingPhrase.
    def enterDivideGivingPhrase(self, ctx:CopyBookParser.DivideGivingPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#divideGivingPhrase.
    def exitDivideGivingPhrase(self, ctx:CopyBookParser.DivideGivingPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#divideInto.
    def enterDivideInto(self, ctx:CopyBookParser.DivideIntoContext):
        pass

    # Exit a parse tree produced by CopyBookParser#divideInto.
    def exitDivideInto(self, ctx:CopyBookParser.DivideIntoContext):
        pass


    # Enter a parse tree produced by CopyBookParser#divideGiving.
    def enterDivideGiving(self, ctx:CopyBookParser.DivideGivingContext):
        pass

    # Exit a parse tree produced by CopyBookParser#divideGiving.
    def exitDivideGiving(self, ctx:CopyBookParser.DivideGivingContext):
        pass


    # Enter a parse tree produced by CopyBookParser#divideRemainder.
    def enterDivideRemainder(self, ctx:CopyBookParser.DivideRemainderContext):
        pass

    # Exit a parse tree produced by CopyBookParser#divideRemainder.
    def exitDivideRemainder(self, ctx:CopyBookParser.DivideRemainderContext):
        pass


    # Enter a parse tree produced by CopyBookParser#enableStatement.
    def enterEnableStatement(self, ctx:CopyBookParser.EnableStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#enableStatement.
    def exitEnableStatement(self, ctx:CopyBookParser.EnableStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#entryStatement.
    def enterEntryStatement(self, ctx:CopyBookParser.EntryStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#entryStatement.
    def exitEntryStatement(self, ctx:CopyBookParser.EntryStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#evaluateStatement.
    def enterEvaluateStatement(self, ctx:CopyBookParser.EvaluateStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#evaluateStatement.
    def exitEvaluateStatement(self, ctx:CopyBookParser.EvaluateStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#evaluateSelect.
    def enterEvaluateSelect(self, ctx:CopyBookParser.EvaluateSelectContext):
        pass

    # Exit a parse tree produced by CopyBookParser#evaluateSelect.
    def exitEvaluateSelect(self, ctx:CopyBookParser.EvaluateSelectContext):
        pass


    # Enter a parse tree produced by CopyBookParser#evaluateAlsoSelect.
    def enterEvaluateAlsoSelect(self, ctx:CopyBookParser.EvaluateAlsoSelectContext):
        pass

    # Exit a parse tree produced by CopyBookParser#evaluateAlsoSelect.
    def exitEvaluateAlsoSelect(self, ctx:CopyBookParser.EvaluateAlsoSelectContext):
        pass


    # Enter a parse tree produced by CopyBookParser#evaluateWhenPhrase.
    def enterEvaluateWhenPhrase(self, ctx:CopyBookParser.EvaluateWhenPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#evaluateWhenPhrase.
    def exitEvaluateWhenPhrase(self, ctx:CopyBookParser.EvaluateWhenPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#evaluateWhen.
    def enterEvaluateWhen(self, ctx:CopyBookParser.EvaluateWhenContext):
        pass

    # Exit a parse tree produced by CopyBookParser#evaluateWhen.
    def exitEvaluateWhen(self, ctx:CopyBookParser.EvaluateWhenContext):
        pass


    # Enter a parse tree produced by CopyBookParser#evaluateCondition.
    def enterEvaluateCondition(self, ctx:CopyBookParser.EvaluateConditionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#evaluateCondition.
    def exitEvaluateCondition(self, ctx:CopyBookParser.EvaluateConditionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#evaluateThrough.
    def enterEvaluateThrough(self, ctx:CopyBookParser.EvaluateThroughContext):
        pass

    # Exit a parse tree produced by CopyBookParser#evaluateThrough.
    def exitEvaluateThrough(self, ctx:CopyBookParser.EvaluateThroughContext):
        pass


    # Enter a parse tree produced by CopyBookParser#evaluateAlsoCondition.
    def enterEvaluateAlsoCondition(self, ctx:CopyBookParser.EvaluateAlsoConditionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#evaluateAlsoCondition.
    def exitEvaluateAlsoCondition(self, ctx:CopyBookParser.EvaluateAlsoConditionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#evaluateWhenOther.
    def enterEvaluateWhenOther(self, ctx:CopyBookParser.EvaluateWhenOtherContext):
        pass

    # Exit a parse tree produced by CopyBookParser#evaluateWhenOther.
    def exitEvaluateWhenOther(self, ctx:CopyBookParser.EvaluateWhenOtherContext):
        pass


    # Enter a parse tree produced by CopyBookParser#evaluateValue.
    def enterEvaluateValue(self, ctx:CopyBookParser.EvaluateValueContext):
        pass

    # Exit a parse tree produced by CopyBookParser#evaluateValue.
    def exitEvaluateValue(self, ctx:CopyBookParser.EvaluateValueContext):
        pass


    # Enter a parse tree produced by CopyBookParser#execCicsStatement.
    def enterExecCicsStatement(self, ctx:CopyBookParser.ExecCicsStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#execCicsStatement.
    def exitExecCicsStatement(self, ctx:CopyBookParser.ExecCicsStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#execSqlStatement.
    def enterExecSqlStatement(self, ctx:CopyBookParser.ExecSqlStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#execSqlStatement.
    def exitExecSqlStatement(self, ctx:CopyBookParser.ExecSqlStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#execSqlImsStatement.
    def enterExecSqlImsStatement(self, ctx:CopyBookParser.ExecSqlImsStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#execSqlImsStatement.
    def exitExecSqlImsStatement(self, ctx:CopyBookParser.ExecSqlImsStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#exhibitStatement.
    def enterExhibitStatement(self, ctx:CopyBookParser.ExhibitStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#exhibitStatement.
    def exitExhibitStatement(self, ctx:CopyBookParser.ExhibitStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#exhibitOperand.
    def enterExhibitOperand(self, ctx:CopyBookParser.ExhibitOperandContext):
        pass

    # Exit a parse tree produced by CopyBookParser#exhibitOperand.
    def exitExhibitOperand(self, ctx:CopyBookParser.ExhibitOperandContext):
        pass


    # Enter a parse tree produced by CopyBookParser#exitStatement.
    def enterExitStatement(self, ctx:CopyBookParser.ExitStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#exitStatement.
    def exitExitStatement(self, ctx:CopyBookParser.ExitStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#generateStatement.
    def enterGenerateStatement(self, ctx:CopyBookParser.GenerateStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#generateStatement.
    def exitGenerateStatement(self, ctx:CopyBookParser.GenerateStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#gobackStatement.
    def enterGobackStatement(self, ctx:CopyBookParser.GobackStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#gobackStatement.
    def exitGobackStatement(self, ctx:CopyBookParser.GobackStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#goToStatement.
    def enterGoToStatement(self, ctx:CopyBookParser.GoToStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#goToStatement.
    def exitGoToStatement(self, ctx:CopyBookParser.GoToStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#goToStatementSimple.
    def enterGoToStatementSimple(self, ctx:CopyBookParser.GoToStatementSimpleContext):
        pass

    # Exit a parse tree produced by CopyBookParser#goToStatementSimple.
    def exitGoToStatementSimple(self, ctx:CopyBookParser.GoToStatementSimpleContext):
        pass


    # Enter a parse tree produced by CopyBookParser#goToDependingOnStatement.
    def enterGoToDependingOnStatement(self, ctx:CopyBookParser.GoToDependingOnStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#goToDependingOnStatement.
    def exitGoToDependingOnStatement(self, ctx:CopyBookParser.GoToDependingOnStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#ifStatement.
    def enterIfStatement(self, ctx:CopyBookParser.IfStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#ifStatement.
    def exitIfStatement(self, ctx:CopyBookParser.IfStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#ifThen.
    def enterIfThen(self, ctx:CopyBookParser.IfThenContext):
        pass

    # Exit a parse tree produced by CopyBookParser#ifThen.
    def exitIfThen(self, ctx:CopyBookParser.IfThenContext):
        pass


    # Enter a parse tree produced by CopyBookParser#ifElse.
    def enterIfElse(self, ctx:CopyBookParser.IfElseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#ifElse.
    def exitIfElse(self, ctx:CopyBookParser.IfElseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#initializeStatement.
    def enterInitializeStatement(self, ctx:CopyBookParser.InitializeStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#initializeStatement.
    def exitInitializeStatement(self, ctx:CopyBookParser.InitializeStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#initializeReplacingPhrase.
    def enterInitializeReplacingPhrase(self, ctx:CopyBookParser.InitializeReplacingPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#initializeReplacingPhrase.
    def exitInitializeReplacingPhrase(self, ctx:CopyBookParser.InitializeReplacingPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#initializeReplacingBy.
    def enterInitializeReplacingBy(self, ctx:CopyBookParser.InitializeReplacingByContext):
        pass

    # Exit a parse tree produced by CopyBookParser#initializeReplacingBy.
    def exitInitializeReplacingBy(self, ctx:CopyBookParser.InitializeReplacingByContext):
        pass


    # Enter a parse tree produced by CopyBookParser#initiateStatement.
    def enterInitiateStatement(self, ctx:CopyBookParser.InitiateStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#initiateStatement.
    def exitInitiateStatement(self, ctx:CopyBookParser.InitiateStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#inspectStatement.
    def enterInspectStatement(self, ctx:CopyBookParser.InspectStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#inspectStatement.
    def exitInspectStatement(self, ctx:CopyBookParser.InspectStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#inspectTallyingPhrase.
    def enterInspectTallyingPhrase(self, ctx:CopyBookParser.InspectTallyingPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#inspectTallyingPhrase.
    def exitInspectTallyingPhrase(self, ctx:CopyBookParser.InspectTallyingPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#inspectReplacingPhrase.
    def enterInspectReplacingPhrase(self, ctx:CopyBookParser.InspectReplacingPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#inspectReplacingPhrase.
    def exitInspectReplacingPhrase(self, ctx:CopyBookParser.InspectReplacingPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#inspectTallyingReplacingPhrase.
    def enterInspectTallyingReplacingPhrase(self, ctx:CopyBookParser.InspectTallyingReplacingPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#inspectTallyingReplacingPhrase.
    def exitInspectTallyingReplacingPhrase(self, ctx:CopyBookParser.InspectTallyingReplacingPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#inspectConvertingPhrase.
    def enterInspectConvertingPhrase(self, ctx:CopyBookParser.InspectConvertingPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#inspectConvertingPhrase.
    def exitInspectConvertingPhrase(self, ctx:CopyBookParser.InspectConvertingPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#inspectFor.
    def enterInspectFor(self, ctx:CopyBookParser.InspectForContext):
        pass

    # Exit a parse tree produced by CopyBookParser#inspectFor.
    def exitInspectFor(self, ctx:CopyBookParser.InspectForContext):
        pass


    # Enter a parse tree produced by CopyBookParser#inspectCharacters.
    def enterInspectCharacters(self, ctx:CopyBookParser.InspectCharactersContext):
        pass

    # Exit a parse tree produced by CopyBookParser#inspectCharacters.
    def exitInspectCharacters(self, ctx:CopyBookParser.InspectCharactersContext):
        pass


    # Enter a parse tree produced by CopyBookParser#inspectReplacingCharacters.
    def enterInspectReplacingCharacters(self, ctx:CopyBookParser.InspectReplacingCharactersContext):
        pass

    # Exit a parse tree produced by CopyBookParser#inspectReplacingCharacters.
    def exitInspectReplacingCharacters(self, ctx:CopyBookParser.InspectReplacingCharactersContext):
        pass


    # Enter a parse tree produced by CopyBookParser#inspectAllLeadings.
    def enterInspectAllLeadings(self, ctx:CopyBookParser.InspectAllLeadingsContext):
        pass

    # Exit a parse tree produced by CopyBookParser#inspectAllLeadings.
    def exitInspectAllLeadings(self, ctx:CopyBookParser.InspectAllLeadingsContext):
        pass


    # Enter a parse tree produced by CopyBookParser#inspectReplacingAllLeadings.
    def enterInspectReplacingAllLeadings(self, ctx:CopyBookParser.InspectReplacingAllLeadingsContext):
        pass

    # Exit a parse tree produced by CopyBookParser#inspectReplacingAllLeadings.
    def exitInspectReplacingAllLeadings(self, ctx:CopyBookParser.InspectReplacingAllLeadingsContext):
        pass


    # Enter a parse tree produced by CopyBookParser#inspectAllLeading.
    def enterInspectAllLeading(self, ctx:CopyBookParser.InspectAllLeadingContext):
        pass

    # Exit a parse tree produced by CopyBookParser#inspectAllLeading.
    def exitInspectAllLeading(self, ctx:CopyBookParser.InspectAllLeadingContext):
        pass


    # Enter a parse tree produced by CopyBookParser#inspectReplacingAllLeading.
    def enterInspectReplacingAllLeading(self, ctx:CopyBookParser.InspectReplacingAllLeadingContext):
        pass

    # Exit a parse tree produced by CopyBookParser#inspectReplacingAllLeading.
    def exitInspectReplacingAllLeading(self, ctx:CopyBookParser.InspectReplacingAllLeadingContext):
        pass


    # Enter a parse tree produced by CopyBookParser#inspectBy.
    def enterInspectBy(self, ctx:CopyBookParser.InspectByContext):
        pass

    # Exit a parse tree produced by CopyBookParser#inspectBy.
    def exitInspectBy(self, ctx:CopyBookParser.InspectByContext):
        pass


    # Enter a parse tree produced by CopyBookParser#inspectTo.
    def enterInspectTo(self, ctx:CopyBookParser.InspectToContext):
        pass

    # Exit a parse tree produced by CopyBookParser#inspectTo.
    def exitInspectTo(self, ctx:CopyBookParser.InspectToContext):
        pass


    # Enter a parse tree produced by CopyBookParser#inspectBeforeAfter.
    def enterInspectBeforeAfter(self, ctx:CopyBookParser.InspectBeforeAfterContext):
        pass

    # Exit a parse tree produced by CopyBookParser#inspectBeforeAfter.
    def exitInspectBeforeAfter(self, ctx:CopyBookParser.InspectBeforeAfterContext):
        pass


    # Enter a parse tree produced by CopyBookParser#mergeStatement.
    def enterMergeStatement(self, ctx:CopyBookParser.MergeStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#mergeStatement.
    def exitMergeStatement(self, ctx:CopyBookParser.MergeStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#mergeOnKeyClause.
    def enterMergeOnKeyClause(self, ctx:CopyBookParser.MergeOnKeyClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#mergeOnKeyClause.
    def exitMergeOnKeyClause(self, ctx:CopyBookParser.MergeOnKeyClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#mergeCollatingSequencePhrase.
    def enterMergeCollatingSequencePhrase(self, ctx:CopyBookParser.MergeCollatingSequencePhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#mergeCollatingSequencePhrase.
    def exitMergeCollatingSequencePhrase(self, ctx:CopyBookParser.MergeCollatingSequencePhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#mergeCollatingAlphanumeric.
    def enterMergeCollatingAlphanumeric(self, ctx:CopyBookParser.MergeCollatingAlphanumericContext):
        pass

    # Exit a parse tree produced by CopyBookParser#mergeCollatingAlphanumeric.
    def exitMergeCollatingAlphanumeric(self, ctx:CopyBookParser.MergeCollatingAlphanumericContext):
        pass


    # Enter a parse tree produced by CopyBookParser#mergeCollatingNational.
    def enterMergeCollatingNational(self, ctx:CopyBookParser.MergeCollatingNationalContext):
        pass

    # Exit a parse tree produced by CopyBookParser#mergeCollatingNational.
    def exitMergeCollatingNational(self, ctx:CopyBookParser.MergeCollatingNationalContext):
        pass


    # Enter a parse tree produced by CopyBookParser#mergeUsing.
    def enterMergeUsing(self, ctx:CopyBookParser.MergeUsingContext):
        pass

    # Exit a parse tree produced by CopyBookParser#mergeUsing.
    def exitMergeUsing(self, ctx:CopyBookParser.MergeUsingContext):
        pass


    # Enter a parse tree produced by CopyBookParser#mergeOutputProcedurePhrase.
    def enterMergeOutputProcedurePhrase(self, ctx:CopyBookParser.MergeOutputProcedurePhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#mergeOutputProcedurePhrase.
    def exitMergeOutputProcedurePhrase(self, ctx:CopyBookParser.MergeOutputProcedurePhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#mergeOutputThrough.
    def enterMergeOutputThrough(self, ctx:CopyBookParser.MergeOutputThroughContext):
        pass

    # Exit a parse tree produced by CopyBookParser#mergeOutputThrough.
    def exitMergeOutputThrough(self, ctx:CopyBookParser.MergeOutputThroughContext):
        pass


    # Enter a parse tree produced by CopyBookParser#mergeGivingPhrase.
    def enterMergeGivingPhrase(self, ctx:CopyBookParser.MergeGivingPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#mergeGivingPhrase.
    def exitMergeGivingPhrase(self, ctx:CopyBookParser.MergeGivingPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#mergeGiving.
    def enterMergeGiving(self, ctx:CopyBookParser.MergeGivingContext):
        pass

    # Exit a parse tree produced by CopyBookParser#mergeGiving.
    def exitMergeGiving(self, ctx:CopyBookParser.MergeGivingContext):
        pass


    # Enter a parse tree produced by CopyBookParser#moveStatement.
    def enterMoveStatement(self, ctx:CopyBookParser.MoveStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#moveStatement.
    def exitMoveStatement(self, ctx:CopyBookParser.MoveStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#moveToStatement.
    def enterMoveToStatement(self, ctx:CopyBookParser.MoveToStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#moveToStatement.
    def exitMoveToStatement(self, ctx:CopyBookParser.MoveToStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#moveToSendingArea.
    def enterMoveToSendingArea(self, ctx:CopyBookParser.MoveToSendingAreaContext):
        pass

    # Exit a parse tree produced by CopyBookParser#moveToSendingArea.
    def exitMoveToSendingArea(self, ctx:CopyBookParser.MoveToSendingAreaContext):
        pass


    # Enter a parse tree produced by CopyBookParser#moveCorrespondingToStatement.
    def enterMoveCorrespondingToStatement(self, ctx:CopyBookParser.MoveCorrespondingToStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#moveCorrespondingToStatement.
    def exitMoveCorrespondingToStatement(self, ctx:CopyBookParser.MoveCorrespondingToStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#moveCorrespondingToSendingArea.
    def enterMoveCorrespondingToSendingArea(self, ctx:CopyBookParser.MoveCorrespondingToSendingAreaContext):
        pass

    # Exit a parse tree produced by CopyBookParser#moveCorrespondingToSendingArea.
    def exitMoveCorrespondingToSendingArea(self, ctx:CopyBookParser.MoveCorrespondingToSendingAreaContext):
        pass


    # Enter a parse tree produced by CopyBookParser#multiplyStatement.
    def enterMultiplyStatement(self, ctx:CopyBookParser.MultiplyStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#multiplyStatement.
    def exitMultiplyStatement(self, ctx:CopyBookParser.MultiplyStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#multiplyRegular.
    def enterMultiplyRegular(self, ctx:CopyBookParser.MultiplyRegularContext):
        pass

    # Exit a parse tree produced by CopyBookParser#multiplyRegular.
    def exitMultiplyRegular(self, ctx:CopyBookParser.MultiplyRegularContext):
        pass


    # Enter a parse tree produced by CopyBookParser#multiplyRegularOperand.
    def enterMultiplyRegularOperand(self, ctx:CopyBookParser.MultiplyRegularOperandContext):
        pass

    # Exit a parse tree produced by CopyBookParser#multiplyRegularOperand.
    def exitMultiplyRegularOperand(self, ctx:CopyBookParser.MultiplyRegularOperandContext):
        pass


    # Enter a parse tree produced by CopyBookParser#multiplyGiving.
    def enterMultiplyGiving(self, ctx:CopyBookParser.MultiplyGivingContext):
        pass

    # Exit a parse tree produced by CopyBookParser#multiplyGiving.
    def exitMultiplyGiving(self, ctx:CopyBookParser.MultiplyGivingContext):
        pass


    # Enter a parse tree produced by CopyBookParser#multiplyGivingOperand.
    def enterMultiplyGivingOperand(self, ctx:CopyBookParser.MultiplyGivingOperandContext):
        pass

    # Exit a parse tree produced by CopyBookParser#multiplyGivingOperand.
    def exitMultiplyGivingOperand(self, ctx:CopyBookParser.MultiplyGivingOperandContext):
        pass


    # Enter a parse tree produced by CopyBookParser#multiplyGivingResult.
    def enterMultiplyGivingResult(self, ctx:CopyBookParser.MultiplyGivingResultContext):
        pass

    # Exit a parse tree produced by CopyBookParser#multiplyGivingResult.
    def exitMultiplyGivingResult(self, ctx:CopyBookParser.MultiplyGivingResultContext):
        pass


    # Enter a parse tree produced by CopyBookParser#openStatement.
    def enterOpenStatement(self, ctx:CopyBookParser.OpenStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#openStatement.
    def exitOpenStatement(self, ctx:CopyBookParser.OpenStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#openInputStatement.
    def enterOpenInputStatement(self, ctx:CopyBookParser.OpenInputStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#openInputStatement.
    def exitOpenInputStatement(self, ctx:CopyBookParser.OpenInputStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#openInput.
    def enterOpenInput(self, ctx:CopyBookParser.OpenInputContext):
        pass

    # Exit a parse tree produced by CopyBookParser#openInput.
    def exitOpenInput(self, ctx:CopyBookParser.OpenInputContext):
        pass


    # Enter a parse tree produced by CopyBookParser#openOutputStatement.
    def enterOpenOutputStatement(self, ctx:CopyBookParser.OpenOutputStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#openOutputStatement.
    def exitOpenOutputStatement(self, ctx:CopyBookParser.OpenOutputStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#openOutput.
    def enterOpenOutput(self, ctx:CopyBookParser.OpenOutputContext):
        pass

    # Exit a parse tree produced by CopyBookParser#openOutput.
    def exitOpenOutput(self, ctx:CopyBookParser.OpenOutputContext):
        pass


    # Enter a parse tree produced by CopyBookParser#openIOStatement.
    def enterOpenIOStatement(self, ctx:CopyBookParser.OpenIOStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#openIOStatement.
    def exitOpenIOStatement(self, ctx:CopyBookParser.OpenIOStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#openExtendStatement.
    def enterOpenExtendStatement(self, ctx:CopyBookParser.OpenExtendStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#openExtendStatement.
    def exitOpenExtendStatement(self, ctx:CopyBookParser.OpenExtendStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#performStatement.
    def enterPerformStatement(self, ctx:CopyBookParser.PerformStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#performStatement.
    def exitPerformStatement(self, ctx:CopyBookParser.PerformStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#performInlineStatement.
    def enterPerformInlineStatement(self, ctx:CopyBookParser.PerformInlineStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#performInlineStatement.
    def exitPerformInlineStatement(self, ctx:CopyBookParser.PerformInlineStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#performProcedureStatement.
    def enterPerformProcedureStatement(self, ctx:CopyBookParser.PerformProcedureStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#performProcedureStatement.
    def exitPerformProcedureStatement(self, ctx:CopyBookParser.PerformProcedureStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#performType.
    def enterPerformType(self, ctx:CopyBookParser.PerformTypeContext):
        pass

    # Exit a parse tree produced by CopyBookParser#performType.
    def exitPerformType(self, ctx:CopyBookParser.PerformTypeContext):
        pass


    # Enter a parse tree produced by CopyBookParser#performTimes.
    def enterPerformTimes(self, ctx:CopyBookParser.PerformTimesContext):
        pass

    # Exit a parse tree produced by CopyBookParser#performTimes.
    def exitPerformTimes(self, ctx:CopyBookParser.PerformTimesContext):
        pass


    # Enter a parse tree produced by CopyBookParser#performUntil.
    def enterPerformUntil(self, ctx:CopyBookParser.PerformUntilContext):
        pass

    # Exit a parse tree produced by CopyBookParser#performUntil.
    def exitPerformUntil(self, ctx:CopyBookParser.PerformUntilContext):
        pass


    # Enter a parse tree produced by CopyBookParser#performVarying.
    def enterPerformVarying(self, ctx:CopyBookParser.PerformVaryingContext):
        pass

    # Exit a parse tree produced by CopyBookParser#performVarying.
    def exitPerformVarying(self, ctx:CopyBookParser.PerformVaryingContext):
        pass


    # Enter a parse tree produced by CopyBookParser#performVaryingClause.
    def enterPerformVaryingClause(self, ctx:CopyBookParser.PerformVaryingClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#performVaryingClause.
    def exitPerformVaryingClause(self, ctx:CopyBookParser.PerformVaryingClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#performVaryingPhrase.
    def enterPerformVaryingPhrase(self, ctx:CopyBookParser.PerformVaryingPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#performVaryingPhrase.
    def exitPerformVaryingPhrase(self, ctx:CopyBookParser.PerformVaryingPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#performAfter.
    def enterPerformAfter(self, ctx:CopyBookParser.PerformAfterContext):
        pass

    # Exit a parse tree produced by CopyBookParser#performAfter.
    def exitPerformAfter(self, ctx:CopyBookParser.PerformAfterContext):
        pass


    # Enter a parse tree produced by CopyBookParser#performFrom.
    def enterPerformFrom(self, ctx:CopyBookParser.PerformFromContext):
        pass

    # Exit a parse tree produced by CopyBookParser#performFrom.
    def exitPerformFrom(self, ctx:CopyBookParser.PerformFromContext):
        pass


    # Enter a parse tree produced by CopyBookParser#performBy.
    def enterPerformBy(self, ctx:CopyBookParser.PerformByContext):
        pass

    # Exit a parse tree produced by CopyBookParser#performBy.
    def exitPerformBy(self, ctx:CopyBookParser.PerformByContext):
        pass


    # Enter a parse tree produced by CopyBookParser#performTestClause.
    def enterPerformTestClause(self, ctx:CopyBookParser.PerformTestClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#performTestClause.
    def exitPerformTestClause(self, ctx:CopyBookParser.PerformTestClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#purgeStatement.
    def enterPurgeStatement(self, ctx:CopyBookParser.PurgeStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#purgeStatement.
    def exitPurgeStatement(self, ctx:CopyBookParser.PurgeStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#readStatement.
    def enterReadStatement(self, ctx:CopyBookParser.ReadStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#readStatement.
    def exitReadStatement(self, ctx:CopyBookParser.ReadStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#readInto.
    def enterReadInto(self, ctx:CopyBookParser.ReadIntoContext):
        pass

    # Exit a parse tree produced by CopyBookParser#readInto.
    def exitReadInto(self, ctx:CopyBookParser.ReadIntoContext):
        pass


    # Enter a parse tree produced by CopyBookParser#readWith.
    def enterReadWith(self, ctx:CopyBookParser.ReadWithContext):
        pass

    # Exit a parse tree produced by CopyBookParser#readWith.
    def exitReadWith(self, ctx:CopyBookParser.ReadWithContext):
        pass


    # Enter a parse tree produced by CopyBookParser#readKey.
    def enterReadKey(self, ctx:CopyBookParser.ReadKeyContext):
        pass

    # Exit a parse tree produced by CopyBookParser#readKey.
    def exitReadKey(self, ctx:CopyBookParser.ReadKeyContext):
        pass


    # Enter a parse tree produced by CopyBookParser#receiveStatement.
    def enterReceiveStatement(self, ctx:CopyBookParser.ReceiveStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#receiveStatement.
    def exitReceiveStatement(self, ctx:CopyBookParser.ReceiveStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#receiveFromStatement.
    def enterReceiveFromStatement(self, ctx:CopyBookParser.ReceiveFromStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#receiveFromStatement.
    def exitReceiveFromStatement(self, ctx:CopyBookParser.ReceiveFromStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#receiveFrom.
    def enterReceiveFrom(self, ctx:CopyBookParser.ReceiveFromContext):
        pass

    # Exit a parse tree produced by CopyBookParser#receiveFrom.
    def exitReceiveFrom(self, ctx:CopyBookParser.ReceiveFromContext):
        pass


    # Enter a parse tree produced by CopyBookParser#receiveIntoStatement.
    def enterReceiveIntoStatement(self, ctx:CopyBookParser.ReceiveIntoStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#receiveIntoStatement.
    def exitReceiveIntoStatement(self, ctx:CopyBookParser.ReceiveIntoStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#receiveNoData.
    def enterReceiveNoData(self, ctx:CopyBookParser.ReceiveNoDataContext):
        pass

    # Exit a parse tree produced by CopyBookParser#receiveNoData.
    def exitReceiveNoData(self, ctx:CopyBookParser.ReceiveNoDataContext):
        pass


    # Enter a parse tree produced by CopyBookParser#receiveWithData.
    def enterReceiveWithData(self, ctx:CopyBookParser.ReceiveWithDataContext):
        pass

    # Exit a parse tree produced by CopyBookParser#receiveWithData.
    def exitReceiveWithData(self, ctx:CopyBookParser.ReceiveWithDataContext):
        pass


    # Enter a parse tree produced by CopyBookParser#receiveBefore.
    def enterReceiveBefore(self, ctx:CopyBookParser.ReceiveBeforeContext):
        pass

    # Exit a parse tree produced by CopyBookParser#receiveBefore.
    def exitReceiveBefore(self, ctx:CopyBookParser.ReceiveBeforeContext):
        pass


    # Enter a parse tree produced by CopyBookParser#receiveWith.
    def enterReceiveWith(self, ctx:CopyBookParser.ReceiveWithContext):
        pass

    # Exit a parse tree produced by CopyBookParser#receiveWith.
    def exitReceiveWith(self, ctx:CopyBookParser.ReceiveWithContext):
        pass


    # Enter a parse tree produced by CopyBookParser#receiveThread.
    def enterReceiveThread(self, ctx:CopyBookParser.ReceiveThreadContext):
        pass

    # Exit a parse tree produced by CopyBookParser#receiveThread.
    def exitReceiveThread(self, ctx:CopyBookParser.ReceiveThreadContext):
        pass


    # Enter a parse tree produced by CopyBookParser#receiveSize.
    def enterReceiveSize(self, ctx:CopyBookParser.ReceiveSizeContext):
        pass

    # Exit a parse tree produced by CopyBookParser#receiveSize.
    def exitReceiveSize(self, ctx:CopyBookParser.ReceiveSizeContext):
        pass


    # Enter a parse tree produced by CopyBookParser#receiveStatus.
    def enterReceiveStatus(self, ctx:CopyBookParser.ReceiveStatusContext):
        pass

    # Exit a parse tree produced by CopyBookParser#receiveStatus.
    def exitReceiveStatus(self, ctx:CopyBookParser.ReceiveStatusContext):
        pass


    # Enter a parse tree produced by CopyBookParser#releaseStatement.
    def enterReleaseStatement(self, ctx:CopyBookParser.ReleaseStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#releaseStatement.
    def exitReleaseStatement(self, ctx:CopyBookParser.ReleaseStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#returnStatement.
    def enterReturnStatement(self, ctx:CopyBookParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#returnStatement.
    def exitReturnStatement(self, ctx:CopyBookParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#returnInto.
    def enterReturnInto(self, ctx:CopyBookParser.ReturnIntoContext):
        pass

    # Exit a parse tree produced by CopyBookParser#returnInto.
    def exitReturnInto(self, ctx:CopyBookParser.ReturnIntoContext):
        pass


    # Enter a parse tree produced by CopyBookParser#rewriteStatement.
    def enterRewriteStatement(self, ctx:CopyBookParser.RewriteStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#rewriteStatement.
    def exitRewriteStatement(self, ctx:CopyBookParser.RewriteStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#rewriteFrom.
    def enterRewriteFrom(self, ctx:CopyBookParser.RewriteFromContext):
        pass

    # Exit a parse tree produced by CopyBookParser#rewriteFrom.
    def exitRewriteFrom(self, ctx:CopyBookParser.RewriteFromContext):
        pass


    # Enter a parse tree produced by CopyBookParser#searchStatement.
    def enterSearchStatement(self, ctx:CopyBookParser.SearchStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#searchStatement.
    def exitSearchStatement(self, ctx:CopyBookParser.SearchStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#searchVarying.
    def enterSearchVarying(self, ctx:CopyBookParser.SearchVaryingContext):
        pass

    # Exit a parse tree produced by CopyBookParser#searchVarying.
    def exitSearchVarying(self, ctx:CopyBookParser.SearchVaryingContext):
        pass


    # Enter a parse tree produced by CopyBookParser#searchWhen.
    def enterSearchWhen(self, ctx:CopyBookParser.SearchWhenContext):
        pass

    # Exit a parse tree produced by CopyBookParser#searchWhen.
    def exitSearchWhen(self, ctx:CopyBookParser.SearchWhenContext):
        pass


    # Enter a parse tree produced by CopyBookParser#sendStatement.
    def enterSendStatement(self, ctx:CopyBookParser.SendStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#sendStatement.
    def exitSendStatement(self, ctx:CopyBookParser.SendStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#sendStatementSync.
    def enterSendStatementSync(self, ctx:CopyBookParser.SendStatementSyncContext):
        pass

    # Exit a parse tree produced by CopyBookParser#sendStatementSync.
    def exitSendStatementSync(self, ctx:CopyBookParser.SendStatementSyncContext):
        pass


    # Enter a parse tree produced by CopyBookParser#sendStatementAsync.
    def enterSendStatementAsync(self, ctx:CopyBookParser.SendStatementAsyncContext):
        pass

    # Exit a parse tree produced by CopyBookParser#sendStatementAsync.
    def exitSendStatementAsync(self, ctx:CopyBookParser.SendStatementAsyncContext):
        pass


    # Enter a parse tree produced by CopyBookParser#sendFromPhrase.
    def enterSendFromPhrase(self, ctx:CopyBookParser.SendFromPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#sendFromPhrase.
    def exitSendFromPhrase(self, ctx:CopyBookParser.SendFromPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#sendWithPhrase.
    def enterSendWithPhrase(self, ctx:CopyBookParser.SendWithPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#sendWithPhrase.
    def exitSendWithPhrase(self, ctx:CopyBookParser.SendWithPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#sendReplacingPhrase.
    def enterSendReplacingPhrase(self, ctx:CopyBookParser.SendReplacingPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#sendReplacingPhrase.
    def exitSendReplacingPhrase(self, ctx:CopyBookParser.SendReplacingPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#sendAdvancingPhrase.
    def enterSendAdvancingPhrase(self, ctx:CopyBookParser.SendAdvancingPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#sendAdvancingPhrase.
    def exitSendAdvancingPhrase(self, ctx:CopyBookParser.SendAdvancingPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#sendAdvancingPage.
    def enterSendAdvancingPage(self, ctx:CopyBookParser.SendAdvancingPageContext):
        pass

    # Exit a parse tree produced by CopyBookParser#sendAdvancingPage.
    def exitSendAdvancingPage(self, ctx:CopyBookParser.SendAdvancingPageContext):
        pass


    # Enter a parse tree produced by CopyBookParser#sendAdvancingLines.
    def enterSendAdvancingLines(self, ctx:CopyBookParser.SendAdvancingLinesContext):
        pass

    # Exit a parse tree produced by CopyBookParser#sendAdvancingLines.
    def exitSendAdvancingLines(self, ctx:CopyBookParser.SendAdvancingLinesContext):
        pass


    # Enter a parse tree produced by CopyBookParser#sendAdvancingMnemonic.
    def enterSendAdvancingMnemonic(self, ctx:CopyBookParser.SendAdvancingMnemonicContext):
        pass

    # Exit a parse tree produced by CopyBookParser#sendAdvancingMnemonic.
    def exitSendAdvancingMnemonic(self, ctx:CopyBookParser.SendAdvancingMnemonicContext):
        pass


    # Enter a parse tree produced by CopyBookParser#setStatement.
    def enterSetStatement(self, ctx:CopyBookParser.SetStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#setStatement.
    def exitSetStatement(self, ctx:CopyBookParser.SetStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#setToStatement.
    def enterSetToStatement(self, ctx:CopyBookParser.SetToStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#setToStatement.
    def exitSetToStatement(self, ctx:CopyBookParser.SetToStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#setUpDownByStatement.
    def enterSetUpDownByStatement(self, ctx:CopyBookParser.SetUpDownByStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#setUpDownByStatement.
    def exitSetUpDownByStatement(self, ctx:CopyBookParser.SetUpDownByStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#setTo.
    def enterSetTo(self, ctx:CopyBookParser.SetToContext):
        pass

    # Exit a parse tree produced by CopyBookParser#setTo.
    def exitSetTo(self, ctx:CopyBookParser.SetToContext):
        pass


    # Enter a parse tree produced by CopyBookParser#setToValue.
    def enterSetToValue(self, ctx:CopyBookParser.SetToValueContext):
        pass

    # Exit a parse tree produced by CopyBookParser#setToValue.
    def exitSetToValue(self, ctx:CopyBookParser.SetToValueContext):
        pass


    # Enter a parse tree produced by CopyBookParser#setByValue.
    def enterSetByValue(self, ctx:CopyBookParser.SetByValueContext):
        pass

    # Exit a parse tree produced by CopyBookParser#setByValue.
    def exitSetByValue(self, ctx:CopyBookParser.SetByValueContext):
        pass


    # Enter a parse tree produced by CopyBookParser#sortStatement.
    def enterSortStatement(self, ctx:CopyBookParser.SortStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#sortStatement.
    def exitSortStatement(self, ctx:CopyBookParser.SortStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#sortOnKeyClause.
    def enterSortOnKeyClause(self, ctx:CopyBookParser.SortOnKeyClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#sortOnKeyClause.
    def exitSortOnKeyClause(self, ctx:CopyBookParser.SortOnKeyClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#sortDuplicatesPhrase.
    def enterSortDuplicatesPhrase(self, ctx:CopyBookParser.SortDuplicatesPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#sortDuplicatesPhrase.
    def exitSortDuplicatesPhrase(self, ctx:CopyBookParser.SortDuplicatesPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#sortCollatingSequencePhrase.
    def enterSortCollatingSequencePhrase(self, ctx:CopyBookParser.SortCollatingSequencePhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#sortCollatingSequencePhrase.
    def exitSortCollatingSequencePhrase(self, ctx:CopyBookParser.SortCollatingSequencePhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#sortCollatingAlphanumeric.
    def enterSortCollatingAlphanumeric(self, ctx:CopyBookParser.SortCollatingAlphanumericContext):
        pass

    # Exit a parse tree produced by CopyBookParser#sortCollatingAlphanumeric.
    def exitSortCollatingAlphanumeric(self, ctx:CopyBookParser.SortCollatingAlphanumericContext):
        pass


    # Enter a parse tree produced by CopyBookParser#sortCollatingNational.
    def enterSortCollatingNational(self, ctx:CopyBookParser.SortCollatingNationalContext):
        pass

    # Exit a parse tree produced by CopyBookParser#sortCollatingNational.
    def exitSortCollatingNational(self, ctx:CopyBookParser.SortCollatingNationalContext):
        pass


    # Enter a parse tree produced by CopyBookParser#sortInputProcedurePhrase.
    def enterSortInputProcedurePhrase(self, ctx:CopyBookParser.SortInputProcedurePhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#sortInputProcedurePhrase.
    def exitSortInputProcedurePhrase(self, ctx:CopyBookParser.SortInputProcedurePhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#sortInputThrough.
    def enterSortInputThrough(self, ctx:CopyBookParser.SortInputThroughContext):
        pass

    # Exit a parse tree produced by CopyBookParser#sortInputThrough.
    def exitSortInputThrough(self, ctx:CopyBookParser.SortInputThroughContext):
        pass


    # Enter a parse tree produced by CopyBookParser#sortUsing.
    def enterSortUsing(self, ctx:CopyBookParser.SortUsingContext):
        pass

    # Exit a parse tree produced by CopyBookParser#sortUsing.
    def exitSortUsing(self, ctx:CopyBookParser.SortUsingContext):
        pass


    # Enter a parse tree produced by CopyBookParser#sortOutputProcedurePhrase.
    def enterSortOutputProcedurePhrase(self, ctx:CopyBookParser.SortOutputProcedurePhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#sortOutputProcedurePhrase.
    def exitSortOutputProcedurePhrase(self, ctx:CopyBookParser.SortOutputProcedurePhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#sortOutputThrough.
    def enterSortOutputThrough(self, ctx:CopyBookParser.SortOutputThroughContext):
        pass

    # Exit a parse tree produced by CopyBookParser#sortOutputThrough.
    def exitSortOutputThrough(self, ctx:CopyBookParser.SortOutputThroughContext):
        pass


    # Enter a parse tree produced by CopyBookParser#sortGivingPhrase.
    def enterSortGivingPhrase(self, ctx:CopyBookParser.SortGivingPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#sortGivingPhrase.
    def exitSortGivingPhrase(self, ctx:CopyBookParser.SortGivingPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#sortGiving.
    def enterSortGiving(self, ctx:CopyBookParser.SortGivingContext):
        pass

    # Exit a parse tree produced by CopyBookParser#sortGiving.
    def exitSortGiving(self, ctx:CopyBookParser.SortGivingContext):
        pass


    # Enter a parse tree produced by CopyBookParser#startStatement.
    def enterStartStatement(self, ctx:CopyBookParser.StartStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#startStatement.
    def exitStartStatement(self, ctx:CopyBookParser.StartStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#startKey.
    def enterStartKey(self, ctx:CopyBookParser.StartKeyContext):
        pass

    # Exit a parse tree produced by CopyBookParser#startKey.
    def exitStartKey(self, ctx:CopyBookParser.StartKeyContext):
        pass


    # Enter a parse tree produced by CopyBookParser#stopStatement.
    def enterStopStatement(self, ctx:CopyBookParser.StopStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#stopStatement.
    def exitStopStatement(self, ctx:CopyBookParser.StopStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#stringStatement.
    def enterStringStatement(self, ctx:CopyBookParser.StringStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#stringStatement.
    def exitStringStatement(self, ctx:CopyBookParser.StringStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#stringSendingPhrase.
    def enterStringSendingPhrase(self, ctx:CopyBookParser.StringSendingPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#stringSendingPhrase.
    def exitStringSendingPhrase(self, ctx:CopyBookParser.StringSendingPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#stringSending.
    def enterStringSending(self, ctx:CopyBookParser.StringSendingContext):
        pass

    # Exit a parse tree produced by CopyBookParser#stringSending.
    def exitStringSending(self, ctx:CopyBookParser.StringSendingContext):
        pass


    # Enter a parse tree produced by CopyBookParser#stringDelimitedByPhrase.
    def enterStringDelimitedByPhrase(self, ctx:CopyBookParser.StringDelimitedByPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#stringDelimitedByPhrase.
    def exitStringDelimitedByPhrase(self, ctx:CopyBookParser.StringDelimitedByPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#stringForPhrase.
    def enterStringForPhrase(self, ctx:CopyBookParser.StringForPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#stringForPhrase.
    def exitStringForPhrase(self, ctx:CopyBookParser.StringForPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#stringIntoPhrase.
    def enterStringIntoPhrase(self, ctx:CopyBookParser.StringIntoPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#stringIntoPhrase.
    def exitStringIntoPhrase(self, ctx:CopyBookParser.StringIntoPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#stringWithPointerPhrase.
    def enterStringWithPointerPhrase(self, ctx:CopyBookParser.StringWithPointerPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#stringWithPointerPhrase.
    def exitStringWithPointerPhrase(self, ctx:CopyBookParser.StringWithPointerPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#subtractStatement.
    def enterSubtractStatement(self, ctx:CopyBookParser.SubtractStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#subtractStatement.
    def exitSubtractStatement(self, ctx:CopyBookParser.SubtractStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#subtractFromStatement.
    def enterSubtractFromStatement(self, ctx:CopyBookParser.SubtractFromStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#subtractFromStatement.
    def exitSubtractFromStatement(self, ctx:CopyBookParser.SubtractFromStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#subtractFromGivingStatement.
    def enterSubtractFromGivingStatement(self, ctx:CopyBookParser.SubtractFromGivingStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#subtractFromGivingStatement.
    def exitSubtractFromGivingStatement(self, ctx:CopyBookParser.SubtractFromGivingStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#subtractCorrespondingStatement.
    def enterSubtractCorrespondingStatement(self, ctx:CopyBookParser.SubtractCorrespondingStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#subtractCorrespondingStatement.
    def exitSubtractCorrespondingStatement(self, ctx:CopyBookParser.SubtractCorrespondingStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#subtractSubtrahend.
    def enterSubtractSubtrahend(self, ctx:CopyBookParser.SubtractSubtrahendContext):
        pass

    # Exit a parse tree produced by CopyBookParser#subtractSubtrahend.
    def exitSubtractSubtrahend(self, ctx:CopyBookParser.SubtractSubtrahendContext):
        pass


    # Enter a parse tree produced by CopyBookParser#subtractMinuend.
    def enterSubtractMinuend(self, ctx:CopyBookParser.SubtractMinuendContext):
        pass

    # Exit a parse tree produced by CopyBookParser#subtractMinuend.
    def exitSubtractMinuend(self, ctx:CopyBookParser.SubtractMinuendContext):
        pass


    # Enter a parse tree produced by CopyBookParser#subtractMinuendGiving.
    def enterSubtractMinuendGiving(self, ctx:CopyBookParser.SubtractMinuendGivingContext):
        pass

    # Exit a parse tree produced by CopyBookParser#subtractMinuendGiving.
    def exitSubtractMinuendGiving(self, ctx:CopyBookParser.SubtractMinuendGivingContext):
        pass


    # Enter a parse tree produced by CopyBookParser#subtractGiving.
    def enterSubtractGiving(self, ctx:CopyBookParser.SubtractGivingContext):
        pass

    # Exit a parse tree produced by CopyBookParser#subtractGiving.
    def exitSubtractGiving(self, ctx:CopyBookParser.SubtractGivingContext):
        pass


    # Enter a parse tree produced by CopyBookParser#subtractMinuendCorresponding.
    def enterSubtractMinuendCorresponding(self, ctx:CopyBookParser.SubtractMinuendCorrespondingContext):
        pass

    # Exit a parse tree produced by CopyBookParser#subtractMinuendCorresponding.
    def exitSubtractMinuendCorresponding(self, ctx:CopyBookParser.SubtractMinuendCorrespondingContext):
        pass


    # Enter a parse tree produced by CopyBookParser#transactionStatement.
    def enterTransactionStatement(self, ctx:CopyBookParser.TransactionStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#transactionStatement.
    def exitTransactionStatement(self, ctx:CopyBookParser.TransactionStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#transactionStart.
    def enterTransactionStart(self, ctx:CopyBookParser.TransactionStartContext):
        pass

    # Exit a parse tree produced by CopyBookParser#transactionStart.
    def exitTransactionStart(self, ctx:CopyBookParser.TransactionStartContext):
        pass


    # Enter a parse tree produced by CopyBookParser#transactionBody.
    def enterTransactionBody(self, ctx:CopyBookParser.TransactionBodyContext):
        pass

    # Exit a parse tree produced by CopyBookParser#transactionBody.
    def exitTransactionBody(self, ctx:CopyBookParser.TransactionBodyContext):
        pass


    # Enter a parse tree produced by CopyBookParser#transactionEnd.
    def enterTransactionEnd(self, ctx:CopyBookParser.TransactionEndContext):
        pass

    # Exit a parse tree produced by CopyBookParser#transactionEnd.
    def exitTransactionEnd(self, ctx:CopyBookParser.TransactionEndContext):
        pass


    # Enter a parse tree produced by CopyBookParser#transactionCancelStatement.
    def enterTransactionCancelStatement(self, ctx:CopyBookParser.TransactionCancelStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#transactionCancelStatement.
    def exitTransactionCancelStatement(self, ctx:CopyBookParser.TransactionCancelStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#terminateStatement.
    def enterTerminateStatement(self, ctx:CopyBookParser.TerminateStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#terminateStatement.
    def exitTerminateStatement(self, ctx:CopyBookParser.TerminateStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#unstringStatement.
    def enterUnstringStatement(self, ctx:CopyBookParser.UnstringStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#unstringStatement.
    def exitUnstringStatement(self, ctx:CopyBookParser.UnstringStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#unstringSendingPhrase.
    def enterUnstringSendingPhrase(self, ctx:CopyBookParser.UnstringSendingPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#unstringSendingPhrase.
    def exitUnstringSendingPhrase(self, ctx:CopyBookParser.UnstringSendingPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#unstringDelimitedByPhrase.
    def enterUnstringDelimitedByPhrase(self, ctx:CopyBookParser.UnstringDelimitedByPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#unstringDelimitedByPhrase.
    def exitUnstringDelimitedByPhrase(self, ctx:CopyBookParser.UnstringDelimitedByPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#unstringOrAllPhrase.
    def enterUnstringOrAllPhrase(self, ctx:CopyBookParser.UnstringOrAllPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#unstringOrAllPhrase.
    def exitUnstringOrAllPhrase(self, ctx:CopyBookParser.UnstringOrAllPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#unstringIntoPhrase.
    def enterUnstringIntoPhrase(self, ctx:CopyBookParser.UnstringIntoPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#unstringIntoPhrase.
    def exitUnstringIntoPhrase(self, ctx:CopyBookParser.UnstringIntoPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#unstringInto.
    def enterUnstringInto(self, ctx:CopyBookParser.UnstringIntoContext):
        pass

    # Exit a parse tree produced by CopyBookParser#unstringInto.
    def exitUnstringInto(self, ctx:CopyBookParser.UnstringIntoContext):
        pass


    # Enter a parse tree produced by CopyBookParser#unstringDelimiterIn.
    def enterUnstringDelimiterIn(self, ctx:CopyBookParser.UnstringDelimiterInContext):
        pass

    # Exit a parse tree produced by CopyBookParser#unstringDelimiterIn.
    def exitUnstringDelimiterIn(self, ctx:CopyBookParser.UnstringDelimiterInContext):
        pass


    # Enter a parse tree produced by CopyBookParser#unstringCountIn.
    def enterUnstringCountIn(self, ctx:CopyBookParser.UnstringCountInContext):
        pass

    # Exit a parse tree produced by CopyBookParser#unstringCountIn.
    def exitUnstringCountIn(self, ctx:CopyBookParser.UnstringCountInContext):
        pass


    # Enter a parse tree produced by CopyBookParser#unstringWithPointerPhrase.
    def enterUnstringWithPointerPhrase(self, ctx:CopyBookParser.UnstringWithPointerPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#unstringWithPointerPhrase.
    def exitUnstringWithPointerPhrase(self, ctx:CopyBookParser.UnstringWithPointerPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#unstringTallyingPhrase.
    def enterUnstringTallyingPhrase(self, ctx:CopyBookParser.UnstringTallyingPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#unstringTallyingPhrase.
    def exitUnstringTallyingPhrase(self, ctx:CopyBookParser.UnstringTallyingPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#useStatement.
    def enterUseStatement(self, ctx:CopyBookParser.UseStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#useStatement.
    def exitUseStatement(self, ctx:CopyBookParser.UseStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#useFor.
    def enterUseFor(self, ctx:CopyBookParser.UseForContext):
        pass

    # Exit a parse tree produced by CopyBookParser#useFor.
    def exitUseFor(self, ctx:CopyBookParser.UseForContext):
        pass


    # Enter a parse tree produced by CopyBookParser#useAfterClause.
    def enterUseAfterClause(self, ctx:CopyBookParser.UseAfterClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#useAfterClause.
    def exitUseAfterClause(self, ctx:CopyBookParser.UseAfterClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#useAfterOn.
    def enterUseAfterOn(self, ctx:CopyBookParser.UseAfterOnContext):
        pass

    # Exit a parse tree produced by CopyBookParser#useAfterOn.
    def exitUseAfterOn(self, ctx:CopyBookParser.UseAfterOnContext):
        pass


    # Enter a parse tree produced by CopyBookParser#useDebugClause.
    def enterUseDebugClause(self, ctx:CopyBookParser.UseDebugClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#useDebugClause.
    def exitUseDebugClause(self, ctx:CopyBookParser.UseDebugClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#useDebugOn.
    def enterUseDebugOn(self, ctx:CopyBookParser.UseDebugOnContext):
        pass

    # Exit a parse tree produced by CopyBookParser#useDebugOn.
    def exitUseDebugOn(self, ctx:CopyBookParser.UseDebugOnContext):
        pass


    # Enter a parse tree produced by CopyBookParser#useDeadLock.
    def enterUseDeadLock(self, ctx:CopyBookParser.UseDeadLockContext):
        pass

    # Exit a parse tree produced by CopyBookParser#useDeadLock.
    def exitUseDeadLock(self, ctx:CopyBookParser.UseDeadLockContext):
        pass


    # Enter a parse tree produced by CopyBookParser#writeStatement.
    def enterWriteStatement(self, ctx:CopyBookParser.WriteStatementContext):
        pass

    # Exit a parse tree produced by CopyBookParser#writeStatement.
    def exitWriteStatement(self, ctx:CopyBookParser.WriteStatementContext):
        pass


    # Enter a parse tree produced by CopyBookParser#writeFromPhrase.
    def enterWriteFromPhrase(self, ctx:CopyBookParser.WriteFromPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#writeFromPhrase.
    def exitWriteFromPhrase(self, ctx:CopyBookParser.WriteFromPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#writeAdvancingPhrase.
    def enterWriteAdvancingPhrase(self, ctx:CopyBookParser.WriteAdvancingPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#writeAdvancingPhrase.
    def exitWriteAdvancingPhrase(self, ctx:CopyBookParser.WriteAdvancingPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#writeAdvancingPage.
    def enterWriteAdvancingPage(self, ctx:CopyBookParser.WriteAdvancingPageContext):
        pass

    # Exit a parse tree produced by CopyBookParser#writeAdvancingPage.
    def exitWriteAdvancingPage(self, ctx:CopyBookParser.WriteAdvancingPageContext):
        pass


    # Enter a parse tree produced by CopyBookParser#writeAdvancingLines.
    def enterWriteAdvancingLines(self, ctx:CopyBookParser.WriteAdvancingLinesContext):
        pass

    # Exit a parse tree produced by CopyBookParser#writeAdvancingLines.
    def exitWriteAdvancingLines(self, ctx:CopyBookParser.WriteAdvancingLinesContext):
        pass


    # Enter a parse tree produced by CopyBookParser#writeAdvancingMnemonic.
    def enterWriteAdvancingMnemonic(self, ctx:CopyBookParser.WriteAdvancingMnemonicContext):
        pass

    # Exit a parse tree produced by CopyBookParser#writeAdvancingMnemonic.
    def exitWriteAdvancingMnemonic(self, ctx:CopyBookParser.WriteAdvancingMnemonicContext):
        pass


    # Enter a parse tree produced by CopyBookParser#writeAtEndOfPagePhrase.
    def enterWriteAtEndOfPagePhrase(self, ctx:CopyBookParser.WriteAtEndOfPagePhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#writeAtEndOfPagePhrase.
    def exitWriteAtEndOfPagePhrase(self, ctx:CopyBookParser.WriteAtEndOfPagePhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#writeNotAtEndOfPagePhrase.
    def enterWriteNotAtEndOfPagePhrase(self, ctx:CopyBookParser.WriteNotAtEndOfPagePhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#writeNotAtEndOfPagePhrase.
    def exitWriteNotAtEndOfPagePhrase(self, ctx:CopyBookParser.WriteNotAtEndOfPagePhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#atEndPhrase.
    def enterAtEndPhrase(self, ctx:CopyBookParser.AtEndPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#atEndPhrase.
    def exitAtEndPhrase(self, ctx:CopyBookParser.AtEndPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#notAtEndPhrase.
    def enterNotAtEndPhrase(self, ctx:CopyBookParser.NotAtEndPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#notAtEndPhrase.
    def exitNotAtEndPhrase(self, ctx:CopyBookParser.NotAtEndPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#invalidKeyPhrase.
    def enterInvalidKeyPhrase(self, ctx:CopyBookParser.InvalidKeyPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#invalidKeyPhrase.
    def exitInvalidKeyPhrase(self, ctx:CopyBookParser.InvalidKeyPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#notInvalidKeyPhrase.
    def enterNotInvalidKeyPhrase(self, ctx:CopyBookParser.NotInvalidKeyPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#notInvalidKeyPhrase.
    def exitNotInvalidKeyPhrase(self, ctx:CopyBookParser.NotInvalidKeyPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#onOverflowPhrase.
    def enterOnOverflowPhrase(self, ctx:CopyBookParser.OnOverflowPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#onOverflowPhrase.
    def exitOnOverflowPhrase(self, ctx:CopyBookParser.OnOverflowPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#notOnOverflowPhrase.
    def enterNotOnOverflowPhrase(self, ctx:CopyBookParser.NotOnOverflowPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#notOnOverflowPhrase.
    def exitNotOnOverflowPhrase(self, ctx:CopyBookParser.NotOnOverflowPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#onSizeErrorPhrase.
    def enterOnSizeErrorPhrase(self, ctx:CopyBookParser.OnSizeErrorPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#onSizeErrorPhrase.
    def exitOnSizeErrorPhrase(self, ctx:CopyBookParser.OnSizeErrorPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#notOnSizeErrorPhrase.
    def enterNotOnSizeErrorPhrase(self, ctx:CopyBookParser.NotOnSizeErrorPhraseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#notOnSizeErrorPhrase.
    def exitNotOnSizeErrorPhrase(self, ctx:CopyBookParser.NotOnSizeErrorPhraseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#onExceptionClause.
    def enterOnExceptionClause(self, ctx:CopyBookParser.OnExceptionClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#onExceptionClause.
    def exitOnExceptionClause(self, ctx:CopyBookParser.OnExceptionClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#notOnExceptionClause.
    def enterNotOnExceptionClause(self, ctx:CopyBookParser.NotOnExceptionClauseContext):
        pass

    # Exit a parse tree produced by CopyBookParser#notOnExceptionClause.
    def exitNotOnExceptionClause(self, ctx:CopyBookParser.NotOnExceptionClauseContext):
        pass


    # Enter a parse tree produced by CopyBookParser#arithmeticExpression.
    def enterArithmeticExpression(self, ctx:CopyBookParser.ArithmeticExpressionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#arithmeticExpression.
    def exitArithmeticExpression(self, ctx:CopyBookParser.ArithmeticExpressionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#plusMinus.
    def enterPlusMinus(self, ctx:CopyBookParser.PlusMinusContext):
        pass

    # Exit a parse tree produced by CopyBookParser#plusMinus.
    def exitPlusMinus(self, ctx:CopyBookParser.PlusMinusContext):
        pass


    # Enter a parse tree produced by CopyBookParser#multDivs.
    def enterMultDivs(self, ctx:CopyBookParser.MultDivsContext):
        pass

    # Exit a parse tree produced by CopyBookParser#multDivs.
    def exitMultDivs(self, ctx:CopyBookParser.MultDivsContext):
        pass


    # Enter a parse tree produced by CopyBookParser#multDiv.
    def enterMultDiv(self, ctx:CopyBookParser.MultDivContext):
        pass

    # Exit a parse tree produced by CopyBookParser#multDiv.
    def exitMultDiv(self, ctx:CopyBookParser.MultDivContext):
        pass


    # Enter a parse tree produced by CopyBookParser#powers.
    def enterPowers(self, ctx:CopyBookParser.PowersContext):
        pass

    # Exit a parse tree produced by CopyBookParser#powers.
    def exitPowers(self, ctx:CopyBookParser.PowersContext):
        pass


    # Enter a parse tree produced by CopyBookParser#power.
    def enterPower(self, ctx:CopyBookParser.PowerContext):
        pass

    # Exit a parse tree produced by CopyBookParser#power.
    def exitPower(self, ctx:CopyBookParser.PowerContext):
        pass


    # Enter a parse tree produced by CopyBookParser#basis.
    def enterBasis(self, ctx:CopyBookParser.BasisContext):
        pass

    # Exit a parse tree produced by CopyBookParser#basis.
    def exitBasis(self, ctx:CopyBookParser.BasisContext):
        pass


    # Enter a parse tree produced by CopyBookParser#condition.
    def enterCondition(self, ctx:CopyBookParser.ConditionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#condition.
    def exitCondition(self, ctx:CopyBookParser.ConditionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#andOrCondition.
    def enterAndOrCondition(self, ctx:CopyBookParser.AndOrConditionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#andOrCondition.
    def exitAndOrCondition(self, ctx:CopyBookParser.AndOrConditionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#combinableCondition.
    def enterCombinableCondition(self, ctx:CopyBookParser.CombinableConditionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#combinableCondition.
    def exitCombinableCondition(self, ctx:CopyBookParser.CombinableConditionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#simpleCondition.
    def enterSimpleCondition(self, ctx:CopyBookParser.SimpleConditionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#simpleCondition.
    def exitSimpleCondition(self, ctx:CopyBookParser.SimpleConditionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#classCondition.
    def enterClassCondition(self, ctx:CopyBookParser.ClassConditionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#classCondition.
    def exitClassCondition(self, ctx:CopyBookParser.ClassConditionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#conditionNameReference.
    def enterConditionNameReference(self, ctx:CopyBookParser.ConditionNameReferenceContext):
        pass

    # Exit a parse tree produced by CopyBookParser#conditionNameReference.
    def exitConditionNameReference(self, ctx:CopyBookParser.ConditionNameReferenceContext):
        pass


    # Enter a parse tree produced by CopyBookParser#conditionNameSubscriptReference.
    def enterConditionNameSubscriptReference(self, ctx:CopyBookParser.ConditionNameSubscriptReferenceContext):
        pass

    # Exit a parse tree produced by CopyBookParser#conditionNameSubscriptReference.
    def exitConditionNameSubscriptReference(self, ctx:CopyBookParser.ConditionNameSubscriptReferenceContext):
        pass


    # Enter a parse tree produced by CopyBookParser#relationCondition.
    def enterRelationCondition(self, ctx:CopyBookParser.RelationConditionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#relationCondition.
    def exitRelationCondition(self, ctx:CopyBookParser.RelationConditionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#relationSignCondition.
    def enterRelationSignCondition(self, ctx:CopyBookParser.RelationSignConditionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#relationSignCondition.
    def exitRelationSignCondition(self, ctx:CopyBookParser.RelationSignConditionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#relationArithmeticComparison.
    def enterRelationArithmeticComparison(self, ctx:CopyBookParser.RelationArithmeticComparisonContext):
        pass

    # Exit a parse tree produced by CopyBookParser#relationArithmeticComparison.
    def exitRelationArithmeticComparison(self, ctx:CopyBookParser.RelationArithmeticComparisonContext):
        pass


    # Enter a parse tree produced by CopyBookParser#relationCombinedComparison.
    def enterRelationCombinedComparison(self, ctx:CopyBookParser.RelationCombinedComparisonContext):
        pass

    # Exit a parse tree produced by CopyBookParser#relationCombinedComparison.
    def exitRelationCombinedComparison(self, ctx:CopyBookParser.RelationCombinedComparisonContext):
        pass


    # Enter a parse tree produced by CopyBookParser#relationCombinedCondition.
    def enterRelationCombinedCondition(self, ctx:CopyBookParser.RelationCombinedConditionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#relationCombinedCondition.
    def exitRelationCombinedCondition(self, ctx:CopyBookParser.RelationCombinedConditionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#relationalOperator.
    def enterRelationalOperator(self, ctx:CopyBookParser.RelationalOperatorContext):
        pass

    # Exit a parse tree produced by CopyBookParser#relationalOperator.
    def exitRelationalOperator(self, ctx:CopyBookParser.RelationalOperatorContext):
        pass


    # Enter a parse tree produced by CopyBookParser#abbreviation.
    def enterAbbreviation(self, ctx:CopyBookParser.AbbreviationContext):
        pass

    # Exit a parse tree produced by CopyBookParser#abbreviation.
    def exitAbbreviation(self, ctx:CopyBookParser.AbbreviationContext):
        pass


    # Enter a parse tree produced by CopyBookParser#identifier.
    def enterIdentifier(self, ctx:CopyBookParser.IdentifierContext):
        pass

    # Exit a parse tree produced by CopyBookParser#identifier.
    def exitIdentifier(self, ctx:CopyBookParser.IdentifierContext):
        pass


    # Enter a parse tree produced by CopyBookParser#tableCall.
    def enterTableCall(self, ctx:CopyBookParser.TableCallContext):
        pass

    # Exit a parse tree produced by CopyBookParser#tableCall.
    def exitTableCall(self, ctx:CopyBookParser.TableCallContext):
        pass


    # Enter a parse tree produced by CopyBookParser#functionCall.
    def enterFunctionCall(self, ctx:CopyBookParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by CopyBookParser#functionCall.
    def exitFunctionCall(self, ctx:CopyBookParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by CopyBookParser#referenceModifier.
    def enterReferenceModifier(self, ctx:CopyBookParser.ReferenceModifierContext):
        pass

    # Exit a parse tree produced by CopyBookParser#referenceModifier.
    def exitReferenceModifier(self, ctx:CopyBookParser.ReferenceModifierContext):
        pass


    # Enter a parse tree produced by CopyBookParser#characterPosition.
    def enterCharacterPosition(self, ctx:CopyBookParser.CharacterPositionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#characterPosition.
    def exitCharacterPosition(self, ctx:CopyBookParser.CharacterPositionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#length.
    def enterLength(self, ctx:CopyBookParser.LengthContext):
        pass

    # Exit a parse tree produced by CopyBookParser#length.
    def exitLength(self, ctx:CopyBookParser.LengthContext):
        pass


    # Enter a parse tree produced by CopyBookParser#subscript_.
    def enterSubscript_(self, ctx:CopyBookParser.Subscript_Context):
        pass

    # Exit a parse tree produced by CopyBookParser#subscript_.
    def exitSubscript_(self, ctx:CopyBookParser.Subscript_Context):
        pass


    # Enter a parse tree produced by CopyBookParser#argument.
    def enterArgument(self, ctx:CopyBookParser.ArgumentContext):
        pass

    # Exit a parse tree produced by CopyBookParser#argument.
    def exitArgument(self, ctx:CopyBookParser.ArgumentContext):
        pass


    # Enter a parse tree produced by CopyBookParser#qualifiedDataName.
    def enterQualifiedDataName(self, ctx:CopyBookParser.QualifiedDataNameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#qualifiedDataName.
    def exitQualifiedDataName(self, ctx:CopyBookParser.QualifiedDataNameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#qualifiedDataNameFormat1.
    def enterQualifiedDataNameFormat1(self, ctx:CopyBookParser.QualifiedDataNameFormat1Context):
        pass

    # Exit a parse tree produced by CopyBookParser#qualifiedDataNameFormat1.
    def exitQualifiedDataNameFormat1(self, ctx:CopyBookParser.QualifiedDataNameFormat1Context):
        pass


    # Enter a parse tree produced by CopyBookParser#qualifiedDataNameFormat2.
    def enterQualifiedDataNameFormat2(self, ctx:CopyBookParser.QualifiedDataNameFormat2Context):
        pass

    # Exit a parse tree produced by CopyBookParser#qualifiedDataNameFormat2.
    def exitQualifiedDataNameFormat2(self, ctx:CopyBookParser.QualifiedDataNameFormat2Context):
        pass


    # Enter a parse tree produced by CopyBookParser#qualifiedDataNameFormat3.
    def enterQualifiedDataNameFormat3(self, ctx:CopyBookParser.QualifiedDataNameFormat3Context):
        pass

    # Exit a parse tree produced by CopyBookParser#qualifiedDataNameFormat3.
    def exitQualifiedDataNameFormat3(self, ctx:CopyBookParser.QualifiedDataNameFormat3Context):
        pass


    # Enter a parse tree produced by CopyBookParser#qualifiedDataNameFormat4.
    def enterQualifiedDataNameFormat4(self, ctx:CopyBookParser.QualifiedDataNameFormat4Context):
        pass

    # Exit a parse tree produced by CopyBookParser#qualifiedDataNameFormat4.
    def exitQualifiedDataNameFormat4(self, ctx:CopyBookParser.QualifiedDataNameFormat4Context):
        pass


    # Enter a parse tree produced by CopyBookParser#qualifiedInData.
    def enterQualifiedInData(self, ctx:CopyBookParser.QualifiedInDataContext):
        pass

    # Exit a parse tree produced by CopyBookParser#qualifiedInData.
    def exitQualifiedInData(self, ctx:CopyBookParser.QualifiedInDataContext):
        pass


    # Enter a parse tree produced by CopyBookParser#inData.
    def enterInData(self, ctx:CopyBookParser.InDataContext):
        pass

    # Exit a parse tree produced by CopyBookParser#inData.
    def exitInData(self, ctx:CopyBookParser.InDataContext):
        pass


    # Enter a parse tree produced by CopyBookParser#inFile.
    def enterInFile(self, ctx:CopyBookParser.InFileContext):
        pass

    # Exit a parse tree produced by CopyBookParser#inFile.
    def exitInFile(self, ctx:CopyBookParser.InFileContext):
        pass


    # Enter a parse tree produced by CopyBookParser#inMnemonic.
    def enterInMnemonic(self, ctx:CopyBookParser.InMnemonicContext):
        pass

    # Exit a parse tree produced by CopyBookParser#inMnemonic.
    def exitInMnemonic(self, ctx:CopyBookParser.InMnemonicContext):
        pass


    # Enter a parse tree produced by CopyBookParser#inSection.
    def enterInSection(self, ctx:CopyBookParser.InSectionContext):
        pass

    # Exit a parse tree produced by CopyBookParser#inSection.
    def exitInSection(self, ctx:CopyBookParser.InSectionContext):
        pass


    # Enter a parse tree produced by CopyBookParser#inLibrary.
    def enterInLibrary(self, ctx:CopyBookParser.InLibraryContext):
        pass

    # Exit a parse tree produced by CopyBookParser#inLibrary.
    def exitInLibrary(self, ctx:CopyBookParser.InLibraryContext):
        pass


    # Enter a parse tree produced by CopyBookParser#inTable.
    def enterInTable(self, ctx:CopyBookParser.InTableContext):
        pass

    # Exit a parse tree produced by CopyBookParser#inTable.
    def exitInTable(self, ctx:CopyBookParser.InTableContext):
        pass


    # Enter a parse tree produced by CopyBookParser#alphabetName.
    def enterAlphabetName(self, ctx:CopyBookParser.AlphabetNameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#alphabetName.
    def exitAlphabetName(self, ctx:CopyBookParser.AlphabetNameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#assignmentName.
    def enterAssignmentName(self, ctx:CopyBookParser.AssignmentNameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#assignmentName.
    def exitAssignmentName(self, ctx:CopyBookParser.AssignmentNameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#basisName.
    def enterBasisName(self, ctx:CopyBookParser.BasisNameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#basisName.
    def exitBasisName(self, ctx:CopyBookParser.BasisNameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#cdName.
    def enterCdName(self, ctx:CopyBookParser.CdNameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#cdName.
    def exitCdName(self, ctx:CopyBookParser.CdNameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#className.
    def enterClassName(self, ctx:CopyBookParser.ClassNameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#className.
    def exitClassName(self, ctx:CopyBookParser.ClassNameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#computerName.
    def enterComputerName(self, ctx:CopyBookParser.ComputerNameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#computerName.
    def exitComputerName(self, ctx:CopyBookParser.ComputerNameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#conditionName.
    def enterConditionName(self, ctx:CopyBookParser.ConditionNameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#conditionName.
    def exitConditionName(self, ctx:CopyBookParser.ConditionNameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataName.
    def enterDataName(self, ctx:CopyBookParser.DataNameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataName.
    def exitDataName(self, ctx:CopyBookParser.DataNameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#dataDescName.
    def enterDataDescName(self, ctx:CopyBookParser.DataDescNameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#dataDescName.
    def exitDataDescName(self, ctx:CopyBookParser.DataDescNameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#environmentName.
    def enterEnvironmentName(self, ctx:CopyBookParser.EnvironmentNameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#environmentName.
    def exitEnvironmentName(self, ctx:CopyBookParser.EnvironmentNameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#fileName.
    def enterFileName(self, ctx:CopyBookParser.FileNameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#fileName.
    def exitFileName(self, ctx:CopyBookParser.FileNameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#functionName.
    def enterFunctionName(self, ctx:CopyBookParser.FunctionNameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#functionName.
    def exitFunctionName(self, ctx:CopyBookParser.FunctionNameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#indexName.
    def enterIndexName(self, ctx:CopyBookParser.IndexNameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#indexName.
    def exitIndexName(self, ctx:CopyBookParser.IndexNameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#languageName.
    def enterLanguageName(self, ctx:CopyBookParser.LanguageNameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#languageName.
    def exitLanguageName(self, ctx:CopyBookParser.LanguageNameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#libraryName.
    def enterLibraryName(self, ctx:CopyBookParser.LibraryNameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#libraryName.
    def exitLibraryName(self, ctx:CopyBookParser.LibraryNameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#localName.
    def enterLocalName(self, ctx:CopyBookParser.LocalNameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#localName.
    def exitLocalName(self, ctx:CopyBookParser.LocalNameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#mnemonicName.
    def enterMnemonicName(self, ctx:CopyBookParser.MnemonicNameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#mnemonicName.
    def exitMnemonicName(self, ctx:CopyBookParser.MnemonicNameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#paragraphName.
    def enterParagraphName(self, ctx:CopyBookParser.ParagraphNameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#paragraphName.
    def exitParagraphName(self, ctx:CopyBookParser.ParagraphNameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#procedureName.
    def enterProcedureName(self, ctx:CopyBookParser.ProcedureNameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#procedureName.
    def exitProcedureName(self, ctx:CopyBookParser.ProcedureNameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#programName.
    def enterProgramName(self, ctx:CopyBookParser.ProgramNameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#programName.
    def exitProgramName(self, ctx:CopyBookParser.ProgramNameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#recordName.
    def enterRecordName(self, ctx:CopyBookParser.RecordNameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#recordName.
    def exitRecordName(self, ctx:CopyBookParser.RecordNameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#reportName.
    def enterReportName(self, ctx:CopyBookParser.ReportNameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#reportName.
    def exitReportName(self, ctx:CopyBookParser.ReportNameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#routineName.
    def enterRoutineName(self, ctx:CopyBookParser.RoutineNameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#routineName.
    def exitRoutineName(self, ctx:CopyBookParser.RoutineNameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#screenName.
    def enterScreenName(self, ctx:CopyBookParser.ScreenNameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#screenName.
    def exitScreenName(self, ctx:CopyBookParser.ScreenNameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#sectionName.
    def enterSectionName(self, ctx:CopyBookParser.SectionNameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#sectionName.
    def exitSectionName(self, ctx:CopyBookParser.SectionNameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#systemName.
    def enterSystemName(self, ctx:CopyBookParser.SystemNameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#systemName.
    def exitSystemName(self, ctx:CopyBookParser.SystemNameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#symbolicCharacter.
    def enterSymbolicCharacter(self, ctx:CopyBookParser.SymbolicCharacterContext):
        pass

    # Exit a parse tree produced by CopyBookParser#symbolicCharacter.
    def exitSymbolicCharacter(self, ctx:CopyBookParser.SymbolicCharacterContext):
        pass


    # Enter a parse tree produced by CopyBookParser#textName.
    def enterTextName(self, ctx:CopyBookParser.TextNameContext):
        pass

    # Exit a parse tree produced by CopyBookParser#textName.
    def exitTextName(self, ctx:CopyBookParser.TextNameContext):
        pass


    # Enter a parse tree produced by CopyBookParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:CopyBookParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by CopyBookParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:CopyBookParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by CopyBookParser#numericLiteral.
    def enterNumericLiteral(self, ctx:CopyBookParser.NumericLiteralContext):
        pass

    # Exit a parse tree produced by CopyBookParser#numericLiteral.
    def exitNumericLiteral(self, ctx:CopyBookParser.NumericLiteralContext):
        pass


    # Enter a parse tree produced by CopyBookParser#integerLiteral.
    def enterIntegerLiteral(self, ctx:CopyBookParser.IntegerLiteralContext):
        pass

    # Exit a parse tree produced by CopyBookParser#integerLiteral.
    def exitIntegerLiteral(self, ctx:CopyBookParser.IntegerLiteralContext):
        pass


    # Enter a parse tree produced by CopyBookParser#cicsDfhRespLiteral.
    def enterCicsDfhRespLiteral(self, ctx:CopyBookParser.CicsDfhRespLiteralContext):
        pass

    # Exit a parse tree produced by CopyBookParser#cicsDfhRespLiteral.
    def exitCicsDfhRespLiteral(self, ctx:CopyBookParser.CicsDfhRespLiteralContext):
        pass


    # Enter a parse tree produced by CopyBookParser#cicsDfhValueLiteral.
    def enterCicsDfhValueLiteral(self, ctx:CopyBookParser.CicsDfhValueLiteralContext):
        pass

    # Exit a parse tree produced by CopyBookParser#cicsDfhValueLiteral.
    def exitCicsDfhValueLiteral(self, ctx:CopyBookParser.CicsDfhValueLiteralContext):
        pass


    # Enter a parse tree produced by CopyBookParser#figurativeConstant.
    def enterFigurativeConstant(self, ctx:CopyBookParser.FigurativeConstantContext):
        pass

    # Exit a parse tree produced by CopyBookParser#figurativeConstant.
    def exitFigurativeConstant(self, ctx:CopyBookParser.FigurativeConstantContext):
        pass


    # Enter a parse tree produced by CopyBookParser#specialRegister.
    def enterSpecialRegister(self, ctx:CopyBookParser.SpecialRegisterContext):
        pass

    # Exit a parse tree produced by CopyBookParser#specialRegister.
    def exitSpecialRegister(self, ctx:CopyBookParser.SpecialRegisterContext):
        pass


    # Enter a parse tree produced by CopyBookParser#commentEntry.
    def enterCommentEntry(self, ctx:CopyBookParser.CommentEntryContext):
        pass

    # Exit a parse tree produced by CopyBookParser#commentEntry.
    def exitCommentEntry(self, ctx:CopyBookParser.CommentEntryContext):
        pass


    # Enter a parse tree produced by CopyBookParser#charDataKeyword.
    def enterCharDataKeyword(self, ctx:CopyBookParser.CharDataKeywordContext):
        pass

    # Exit a parse tree produced by CopyBookParser#charDataKeyword.
    def exitCharDataKeyword(self, ctx:CopyBookParser.CharDataKeywordContext):
        pass



del CopyBookParser