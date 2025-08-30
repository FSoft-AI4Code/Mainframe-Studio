# Generated from grammar/isuzu_cobol/CobolIsuzu.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CobolIsuzuParser import CobolIsuzuParser
else:
    from CobolIsuzuParser import CobolIsuzuParser

# This class defines a complete listener for a parse tree produced by CobolIsuzuParser.
class CobolIsuzuListener(ParseTreeListener):

    # Enter a parse tree produced by CobolIsuzuParser#startRule.
    def enterStartRule(self, ctx:CobolIsuzuParser.StartRuleContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#startRule.
    def exitStartRule(self, ctx:CobolIsuzuParser.StartRuleContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#compilationUnit.
    def enterCompilationUnit(self, ctx:CobolIsuzuParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#compilationUnit.
    def exitCompilationUnit(self, ctx:CobolIsuzuParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#programUnit.
    def enterProgramUnit(self, ctx:CobolIsuzuParser.ProgramUnitContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#programUnit.
    def exitProgramUnit(self, ctx:CobolIsuzuParser.ProgramUnitContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#endProgramStatement.
    def enterEndProgramStatement(self, ctx:CobolIsuzuParser.EndProgramStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#endProgramStatement.
    def exitEndProgramStatement(self, ctx:CobolIsuzuParser.EndProgramStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#identificationDivision.
    def enterIdentificationDivision(self, ctx:CobolIsuzuParser.IdentificationDivisionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#identificationDivision.
    def exitIdentificationDivision(self, ctx:CobolIsuzuParser.IdentificationDivisionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#identificationDivisionBody.
    def enterIdentificationDivisionBody(self, ctx:CobolIsuzuParser.IdentificationDivisionBodyContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#identificationDivisionBody.
    def exitIdentificationDivisionBody(self, ctx:CobolIsuzuParser.IdentificationDivisionBodyContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#programIdParagraph.
    def enterProgramIdParagraph(self, ctx:CobolIsuzuParser.ProgramIdParagraphContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#programIdParagraph.
    def exitProgramIdParagraph(self, ctx:CobolIsuzuParser.ProgramIdParagraphContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#author_name.
    def enterAuthor_name(self, ctx:CobolIsuzuParser.Author_nameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#author_name.
    def exitAuthor_name(self, ctx:CobolIsuzuParser.Author_nameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#authorParagraph.
    def enterAuthorParagraph(self, ctx:CobolIsuzuParser.AuthorParagraphContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#authorParagraph.
    def exitAuthorParagraph(self, ctx:CobolIsuzuParser.AuthorParagraphContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#installationParagraph.
    def enterInstallationParagraph(self, ctx:CobolIsuzuParser.InstallationParagraphContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#installationParagraph.
    def exitInstallationParagraph(self, ctx:CobolIsuzuParser.InstallationParagraphContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dateWrittenParagraph.
    def enterDateWrittenParagraph(self, ctx:CobolIsuzuParser.DateWrittenParagraphContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dateWrittenParagraph.
    def exitDateWrittenParagraph(self, ctx:CobolIsuzuParser.DateWrittenParagraphContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dateCompiledParagraph.
    def enterDateCompiledParagraph(self, ctx:CobolIsuzuParser.DateCompiledParagraphContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dateCompiledParagraph.
    def exitDateCompiledParagraph(self, ctx:CobolIsuzuParser.DateCompiledParagraphContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#securityParagraph.
    def enterSecurityParagraph(self, ctx:CobolIsuzuParser.SecurityParagraphContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#securityParagraph.
    def exitSecurityParagraph(self, ctx:CobolIsuzuParser.SecurityParagraphContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#remarksParagraph.
    def enterRemarksParagraph(self, ctx:CobolIsuzuParser.RemarksParagraphContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#remarksParagraph.
    def exitRemarksParagraph(self, ctx:CobolIsuzuParser.RemarksParagraphContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#environmentDivision.
    def enterEnvironmentDivision(self, ctx:CobolIsuzuParser.EnvironmentDivisionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#environmentDivision.
    def exitEnvironmentDivision(self, ctx:CobolIsuzuParser.EnvironmentDivisionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#environmentDivisionBody.
    def enterEnvironmentDivisionBody(self, ctx:CobolIsuzuParser.EnvironmentDivisionBodyContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#environmentDivisionBody.
    def exitEnvironmentDivisionBody(self, ctx:CobolIsuzuParser.EnvironmentDivisionBodyContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#configurationSection.
    def enterConfigurationSection(self, ctx:CobolIsuzuParser.ConfigurationSectionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#configurationSection.
    def exitConfigurationSection(self, ctx:CobolIsuzuParser.ConfigurationSectionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#configurationSectionParagraph.
    def enterConfigurationSectionParagraph(self, ctx:CobolIsuzuParser.ConfigurationSectionParagraphContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#configurationSectionParagraph.
    def exitConfigurationSectionParagraph(self, ctx:CobolIsuzuParser.ConfigurationSectionParagraphContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#subSchemaParagraph.
    def enterSubSchemaParagraph(self, ctx:CobolIsuzuParser.SubSchemaParagraphContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#subSchemaParagraph.
    def exitSubSchemaParagraph(self, ctx:CobolIsuzuParser.SubSchemaParagraphContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#sourceComputerParagraph.
    def enterSourceComputerParagraph(self, ctx:CobolIsuzuParser.SourceComputerParagraphContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#sourceComputerParagraph.
    def exitSourceComputerParagraph(self, ctx:CobolIsuzuParser.SourceComputerParagraphContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#objectComputerParagraph.
    def enterObjectComputerParagraph(self, ctx:CobolIsuzuParser.ObjectComputerParagraphContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#objectComputerParagraph.
    def exitObjectComputerParagraph(self, ctx:CobolIsuzuParser.ObjectComputerParagraphContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#objectComputerClause.
    def enterObjectComputerClause(self, ctx:CobolIsuzuParser.ObjectComputerClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#objectComputerClause.
    def exitObjectComputerClause(self, ctx:CobolIsuzuParser.ObjectComputerClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#memorySizeClause.
    def enterMemorySizeClause(self, ctx:CobolIsuzuParser.MemorySizeClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#memorySizeClause.
    def exitMemorySizeClause(self, ctx:CobolIsuzuParser.MemorySizeClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#diskSizeClause.
    def enterDiskSizeClause(self, ctx:CobolIsuzuParser.DiskSizeClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#diskSizeClause.
    def exitDiskSizeClause(self, ctx:CobolIsuzuParser.DiskSizeClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#collatingSequenceClause.
    def enterCollatingSequenceClause(self, ctx:CobolIsuzuParser.CollatingSequenceClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#collatingSequenceClause.
    def exitCollatingSequenceClause(self, ctx:CobolIsuzuParser.CollatingSequenceClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#collatingSequenceClauseAlphanumeric.
    def enterCollatingSequenceClauseAlphanumeric(self, ctx:CobolIsuzuParser.CollatingSequenceClauseAlphanumericContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#collatingSequenceClauseAlphanumeric.
    def exitCollatingSequenceClauseAlphanumeric(self, ctx:CobolIsuzuParser.CollatingSequenceClauseAlphanumericContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#collatingSequenceClauseNational.
    def enterCollatingSequenceClauseNational(self, ctx:CobolIsuzuParser.CollatingSequenceClauseNationalContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#collatingSequenceClauseNational.
    def exitCollatingSequenceClauseNational(self, ctx:CobolIsuzuParser.CollatingSequenceClauseNationalContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#segmentLimitClause.
    def enterSegmentLimitClause(self, ctx:CobolIsuzuParser.SegmentLimitClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#segmentLimitClause.
    def exitSegmentLimitClause(self, ctx:CobolIsuzuParser.SegmentLimitClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#characterSetClause.
    def enterCharacterSetClause(self, ctx:CobolIsuzuParser.CharacterSetClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#characterSetClause.
    def exitCharacterSetClause(self, ctx:CobolIsuzuParser.CharacterSetClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#specialNamesParagraph.
    def enterSpecialNamesParagraph(self, ctx:CobolIsuzuParser.SpecialNamesParagraphContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#specialNamesParagraph.
    def exitSpecialNamesParagraph(self, ctx:CobolIsuzuParser.SpecialNamesParagraphContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#specialNameClause.
    def enterSpecialNameClause(self, ctx:CobolIsuzuParser.SpecialNameClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#specialNameClause.
    def exitSpecialNameClause(self, ctx:CobolIsuzuParser.SpecialNameClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#alphabetClause.
    def enterAlphabetClause(self, ctx:CobolIsuzuParser.AlphabetClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#alphabetClause.
    def exitAlphabetClause(self, ctx:CobolIsuzuParser.AlphabetClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#alphabetClauseFormat1.
    def enterAlphabetClauseFormat1(self, ctx:CobolIsuzuParser.AlphabetClauseFormat1Context):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#alphabetClauseFormat1.
    def exitAlphabetClauseFormat1(self, ctx:CobolIsuzuParser.AlphabetClauseFormat1Context):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#alphabetLiterals.
    def enterAlphabetLiterals(self, ctx:CobolIsuzuParser.AlphabetLiteralsContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#alphabetLiterals.
    def exitAlphabetLiterals(self, ctx:CobolIsuzuParser.AlphabetLiteralsContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#alphabetThrough.
    def enterAlphabetThrough(self, ctx:CobolIsuzuParser.AlphabetThroughContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#alphabetThrough.
    def exitAlphabetThrough(self, ctx:CobolIsuzuParser.AlphabetThroughContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#alphabetAlso.
    def enterAlphabetAlso(self, ctx:CobolIsuzuParser.AlphabetAlsoContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#alphabetAlso.
    def exitAlphabetAlso(self, ctx:CobolIsuzuParser.AlphabetAlsoContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#alphabetClauseFormat2.
    def enterAlphabetClauseFormat2(self, ctx:CobolIsuzuParser.AlphabetClauseFormat2Context):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#alphabetClauseFormat2.
    def exitAlphabetClauseFormat2(self, ctx:CobolIsuzuParser.AlphabetClauseFormat2Context):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#channelClause.
    def enterChannelClause(self, ctx:CobolIsuzuParser.ChannelClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#channelClause.
    def exitChannelClause(self, ctx:CobolIsuzuParser.ChannelClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#classClause.
    def enterClassClause(self, ctx:CobolIsuzuParser.ClassClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#classClause.
    def exitClassClause(self, ctx:CobolIsuzuParser.ClassClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#classClauseThrough.
    def enterClassClauseThrough(self, ctx:CobolIsuzuParser.ClassClauseThroughContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#classClauseThrough.
    def exitClassClauseThrough(self, ctx:CobolIsuzuParser.ClassClauseThroughContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#classClauseFrom.
    def enterClassClauseFrom(self, ctx:CobolIsuzuParser.ClassClauseFromContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#classClauseFrom.
    def exitClassClauseFrom(self, ctx:CobolIsuzuParser.ClassClauseFromContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#classClauseTo.
    def enterClassClauseTo(self, ctx:CobolIsuzuParser.ClassClauseToContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#classClauseTo.
    def exitClassClauseTo(self, ctx:CobolIsuzuParser.ClassClauseToContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#currencySignClause.
    def enterCurrencySignClause(self, ctx:CobolIsuzuParser.CurrencySignClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#currencySignClause.
    def exitCurrencySignClause(self, ctx:CobolIsuzuParser.CurrencySignClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#decimalPointClause.
    def enterDecimalPointClause(self, ctx:CobolIsuzuParser.DecimalPointClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#decimalPointClause.
    def exitDecimalPointClause(self, ctx:CobolIsuzuParser.DecimalPointClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#defaultComputationalSignClause.
    def enterDefaultComputationalSignClause(self, ctx:CobolIsuzuParser.DefaultComputationalSignClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#defaultComputationalSignClause.
    def exitDefaultComputationalSignClause(self, ctx:CobolIsuzuParser.DefaultComputationalSignClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#defaultDisplaySignClause.
    def enterDefaultDisplaySignClause(self, ctx:CobolIsuzuParser.DefaultDisplaySignClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#defaultDisplaySignClause.
    def exitDefaultDisplaySignClause(self, ctx:CobolIsuzuParser.DefaultDisplaySignClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#environmentSwitchNameClause.
    def enterEnvironmentSwitchNameClause(self, ctx:CobolIsuzuParser.EnvironmentSwitchNameClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#environmentSwitchNameClause.
    def exitEnvironmentSwitchNameClause(self, ctx:CobolIsuzuParser.EnvironmentSwitchNameClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#environmentSwitchNameSpecialNamesStatusPhrase.
    def enterEnvironmentSwitchNameSpecialNamesStatusPhrase(self, ctx:CobolIsuzuParser.EnvironmentSwitchNameSpecialNamesStatusPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#environmentSwitchNameSpecialNamesStatusPhrase.
    def exitEnvironmentSwitchNameSpecialNamesStatusPhrase(self, ctx:CobolIsuzuParser.EnvironmentSwitchNameSpecialNamesStatusPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#odtClause.
    def enterOdtClause(self, ctx:CobolIsuzuParser.OdtClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#odtClause.
    def exitOdtClause(self, ctx:CobolIsuzuParser.OdtClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reserveNetworkClause.
    def enterReserveNetworkClause(self, ctx:CobolIsuzuParser.ReserveNetworkClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reserveNetworkClause.
    def exitReserveNetworkClause(self, ctx:CobolIsuzuParser.ReserveNetworkClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#symbolicCharactersClause.
    def enterSymbolicCharactersClause(self, ctx:CobolIsuzuParser.SymbolicCharactersClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#symbolicCharactersClause.
    def exitSymbolicCharactersClause(self, ctx:CobolIsuzuParser.SymbolicCharactersClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#symbolicCharacters.
    def enterSymbolicCharacters(self, ctx:CobolIsuzuParser.SymbolicCharactersContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#symbolicCharacters.
    def exitSymbolicCharacters(self, ctx:CobolIsuzuParser.SymbolicCharactersContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#inputOutputSection.
    def enterInputOutputSection(self, ctx:CobolIsuzuParser.InputOutputSectionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#inputOutputSection.
    def exitInputOutputSection(self, ctx:CobolIsuzuParser.InputOutputSectionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#inputOutputSectionParagraph.
    def enterInputOutputSectionParagraph(self, ctx:CobolIsuzuParser.InputOutputSectionParagraphContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#inputOutputSectionParagraph.
    def exitInputOutputSectionParagraph(self, ctx:CobolIsuzuParser.InputOutputSectionParagraphContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#fileControlParagraph.
    def enterFileControlParagraph(self, ctx:CobolIsuzuParser.FileControlParagraphContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#fileControlParagraph.
    def exitFileControlParagraph(self, ctx:CobolIsuzuParser.FileControlParagraphContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#fileControlEntry.
    def enterFileControlEntry(self, ctx:CobolIsuzuParser.FileControlEntryContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#fileControlEntry.
    def exitFileControlEntry(self, ctx:CobolIsuzuParser.FileControlEntryContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#selectClause.
    def enterSelectClause(self, ctx:CobolIsuzuParser.SelectClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#selectClause.
    def exitSelectClause(self, ctx:CobolIsuzuParser.SelectClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#fileControlClause.
    def enterFileControlClause(self, ctx:CobolIsuzuParser.FileControlClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#fileControlClause.
    def exitFileControlClause(self, ctx:CobolIsuzuParser.FileControlClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#selectedFunctionClause.
    def enterSelectedFunctionClause(self, ctx:CobolIsuzuParser.SelectedFunctionClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#selectedFunctionClause.
    def exitSelectedFunctionClause(self, ctx:CobolIsuzuParser.SelectedFunctionClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#assignClause.
    def enterAssignClause(self, ctx:CobolIsuzuParser.AssignClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#assignClause.
    def exitAssignClause(self, ctx:CobolIsuzuParser.AssignClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reserveClause.
    def enterReserveClause(self, ctx:CobolIsuzuParser.ReserveClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reserveClause.
    def exitReserveClause(self, ctx:CobolIsuzuParser.ReserveClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#organizationClause.
    def enterOrganizationClause(self, ctx:CobolIsuzuParser.OrganizationClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#organizationClause.
    def exitOrganizationClause(self, ctx:CobolIsuzuParser.OrganizationClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#destinationClause.
    def enterDestinationClause(self, ctx:CobolIsuzuParser.DestinationClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#destinationClause.
    def exitDestinationClause(self, ctx:CobolIsuzuParser.DestinationClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#formatClause.
    def enterFormatClause(self, ctx:CobolIsuzuParser.FormatClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#formatClause.
    def exitFormatClause(self, ctx:CobolIsuzuParser.FormatClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#messageModeClause.
    def enterMessageModeClause(self, ctx:CobolIsuzuParser.MessageModeClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#messageModeClause.
    def exitMessageModeClause(self, ctx:CobolIsuzuParser.MessageModeClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#paddingCharacterClause.
    def enterPaddingCharacterClause(self, ctx:CobolIsuzuParser.PaddingCharacterClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#paddingCharacterClause.
    def exitPaddingCharacterClause(self, ctx:CobolIsuzuParser.PaddingCharacterClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#recordDelimiterClause.
    def enterRecordDelimiterClause(self, ctx:CobolIsuzuParser.RecordDelimiterClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#recordDelimiterClause.
    def exitRecordDelimiterClause(self, ctx:CobolIsuzuParser.RecordDelimiterClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#accessModeClause.
    def enterAccessModeClause(self, ctx:CobolIsuzuParser.AccessModeClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#accessModeClause.
    def exitAccessModeClause(self, ctx:CobolIsuzuParser.AccessModeClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#recordKeyClause.
    def enterRecordKeyClause(self, ctx:CobolIsuzuParser.RecordKeyClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#recordKeyClause.
    def exitRecordKeyClause(self, ctx:CobolIsuzuParser.RecordKeyClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#alternateRecordKeyClause.
    def enterAlternateRecordKeyClause(self, ctx:CobolIsuzuParser.AlternateRecordKeyClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#alternateRecordKeyClause.
    def exitAlternateRecordKeyClause(self, ctx:CobolIsuzuParser.AlternateRecordKeyClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#passwordClause.
    def enterPasswordClause(self, ctx:CobolIsuzuParser.PasswordClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#passwordClause.
    def exitPasswordClause(self, ctx:CobolIsuzuParser.PasswordClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#fileStatusClause.
    def enterFileStatusClause(self, ctx:CobolIsuzuParser.FileStatusClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#fileStatusClause.
    def exitFileStatusClause(self, ctx:CobolIsuzuParser.FileStatusClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#relativeKeyClause.
    def enterRelativeKeyClause(self, ctx:CobolIsuzuParser.RelativeKeyClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#relativeKeyClause.
    def exitRelativeKeyClause(self, ctx:CobolIsuzuParser.RelativeKeyClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#sessionControlClause.
    def enterSessionControlClause(self, ctx:CobolIsuzuParser.SessionControlClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#sessionControlClause.
    def exitSessionControlClause(self, ctx:CobolIsuzuParser.SessionControlClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#ioControlParagraph.
    def enterIoControlParagraph(self, ctx:CobolIsuzuParser.IoControlParagraphContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#ioControlParagraph.
    def exitIoControlParagraph(self, ctx:CobolIsuzuParser.IoControlParagraphContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#ioControlClause.
    def enterIoControlClause(self, ctx:CobolIsuzuParser.IoControlClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#ioControlClause.
    def exitIoControlClause(self, ctx:CobolIsuzuParser.IoControlClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#applyClause.
    def enterApplyClause(self, ctx:CobolIsuzuParser.ApplyClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#applyClause.
    def exitApplyClause(self, ctx:CobolIsuzuParser.ApplyClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#rerunClause.
    def enterRerunClause(self, ctx:CobolIsuzuParser.RerunClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#rerunClause.
    def exitRerunClause(self, ctx:CobolIsuzuParser.RerunClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#rerunEveryRecords.
    def enterRerunEveryRecords(self, ctx:CobolIsuzuParser.RerunEveryRecordsContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#rerunEveryRecords.
    def exitRerunEveryRecords(self, ctx:CobolIsuzuParser.RerunEveryRecordsContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#rerunEveryOf.
    def enterRerunEveryOf(self, ctx:CobolIsuzuParser.RerunEveryOfContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#rerunEveryOf.
    def exitRerunEveryOf(self, ctx:CobolIsuzuParser.RerunEveryOfContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#rerunEveryClock.
    def enterRerunEveryClock(self, ctx:CobolIsuzuParser.RerunEveryClockContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#rerunEveryClock.
    def exitRerunEveryClock(self, ctx:CobolIsuzuParser.RerunEveryClockContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#sameClause.
    def enterSameClause(self, ctx:CobolIsuzuParser.SameClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#sameClause.
    def exitSameClause(self, ctx:CobolIsuzuParser.SameClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#multipleFileClause.
    def enterMultipleFileClause(self, ctx:CobolIsuzuParser.MultipleFileClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#multipleFileClause.
    def exitMultipleFileClause(self, ctx:CobolIsuzuParser.MultipleFileClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#multipleFilePosition.
    def enterMultipleFilePosition(self, ctx:CobolIsuzuParser.MultipleFilePositionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#multipleFilePosition.
    def exitMultipleFilePosition(self, ctx:CobolIsuzuParser.MultipleFilePositionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#commitmentControlClause.
    def enterCommitmentControlClause(self, ctx:CobolIsuzuParser.CommitmentControlClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#commitmentControlClause.
    def exitCommitmentControlClause(self, ctx:CobolIsuzuParser.CommitmentControlClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataDivision.
    def enterDataDivision(self, ctx:CobolIsuzuParser.DataDivisionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataDivision.
    def exitDataDivision(self, ctx:CobolIsuzuParser.DataDivisionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataDivisionSection.
    def enterDataDivisionSection(self, ctx:CobolIsuzuParser.DataDivisionSectionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataDivisionSection.
    def exitDataDivisionSection(self, ctx:CobolIsuzuParser.DataDivisionSectionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#fileSection.
    def enterFileSection(self, ctx:CobolIsuzuParser.FileSectionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#fileSection.
    def exitFileSection(self, ctx:CobolIsuzuParser.FileSectionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#fileDescriptionEntry.
    def enterFileDescriptionEntry(self, ctx:CobolIsuzuParser.FileDescriptionEntryContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#fileDescriptionEntry.
    def exitFileDescriptionEntry(self, ctx:CobolIsuzuParser.FileDescriptionEntryContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#fileDescriptionEntryClause.
    def enterFileDescriptionEntryClause(self, ctx:CobolIsuzuParser.FileDescriptionEntryClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#fileDescriptionEntryClause.
    def exitFileDescriptionEntryClause(self, ctx:CobolIsuzuParser.FileDescriptionEntryClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#externalClause.
    def enterExternalClause(self, ctx:CobolIsuzuParser.ExternalClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#externalClause.
    def exitExternalClause(self, ctx:CobolIsuzuParser.ExternalClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#globalClause.
    def enterGlobalClause(self, ctx:CobolIsuzuParser.GlobalClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#globalClause.
    def exitGlobalClause(self, ctx:CobolIsuzuParser.GlobalClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#blockContainsClause.
    def enterBlockContainsClause(self, ctx:CobolIsuzuParser.BlockContainsClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#blockContainsClause.
    def exitBlockContainsClause(self, ctx:CobolIsuzuParser.BlockContainsClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#blockContainsTo.
    def enterBlockContainsTo(self, ctx:CobolIsuzuParser.BlockContainsToContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#blockContainsTo.
    def exitBlockContainsTo(self, ctx:CobolIsuzuParser.BlockContainsToContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#recordContainsClause.
    def enterRecordContainsClause(self, ctx:CobolIsuzuParser.RecordContainsClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#recordContainsClause.
    def exitRecordContainsClause(self, ctx:CobolIsuzuParser.RecordContainsClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#recordContainsClauseFormat1.
    def enterRecordContainsClauseFormat1(self, ctx:CobolIsuzuParser.RecordContainsClauseFormat1Context):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#recordContainsClauseFormat1.
    def exitRecordContainsClauseFormat1(self, ctx:CobolIsuzuParser.RecordContainsClauseFormat1Context):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#recordContainsClauseFormat2.
    def enterRecordContainsClauseFormat2(self, ctx:CobolIsuzuParser.RecordContainsClauseFormat2Context):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#recordContainsClauseFormat2.
    def exitRecordContainsClauseFormat2(self, ctx:CobolIsuzuParser.RecordContainsClauseFormat2Context):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#recordContainsClauseFormat3.
    def enterRecordContainsClauseFormat3(self, ctx:CobolIsuzuParser.RecordContainsClauseFormat3Context):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#recordContainsClauseFormat3.
    def exitRecordContainsClauseFormat3(self, ctx:CobolIsuzuParser.RecordContainsClauseFormat3Context):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#recordContainsTo.
    def enterRecordContainsTo(self, ctx:CobolIsuzuParser.RecordContainsToContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#recordContainsTo.
    def exitRecordContainsTo(self, ctx:CobolIsuzuParser.RecordContainsToContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#labelRecordsClause.
    def enterLabelRecordsClause(self, ctx:CobolIsuzuParser.LabelRecordsClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#labelRecordsClause.
    def exitLabelRecordsClause(self, ctx:CobolIsuzuParser.LabelRecordsClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#valueOfClause.
    def enterValueOfClause(self, ctx:CobolIsuzuParser.ValueOfClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#valueOfClause.
    def exitValueOfClause(self, ctx:CobolIsuzuParser.ValueOfClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#valuePair.
    def enterValuePair(self, ctx:CobolIsuzuParser.ValuePairContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#valuePair.
    def exitValuePair(self, ctx:CobolIsuzuParser.ValuePairContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataRecordsClause.
    def enterDataRecordsClause(self, ctx:CobolIsuzuParser.DataRecordsClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataRecordsClause.
    def exitDataRecordsClause(self, ctx:CobolIsuzuParser.DataRecordsClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#linageClause.
    def enterLinageClause(self, ctx:CobolIsuzuParser.LinageClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#linageClause.
    def exitLinageClause(self, ctx:CobolIsuzuParser.LinageClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#linageAt.
    def enterLinageAt(self, ctx:CobolIsuzuParser.LinageAtContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#linageAt.
    def exitLinageAt(self, ctx:CobolIsuzuParser.LinageAtContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#linageFootingAt.
    def enterLinageFootingAt(self, ctx:CobolIsuzuParser.LinageFootingAtContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#linageFootingAt.
    def exitLinageFootingAt(self, ctx:CobolIsuzuParser.LinageFootingAtContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#linageLinesAtTop.
    def enterLinageLinesAtTop(self, ctx:CobolIsuzuParser.LinageLinesAtTopContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#linageLinesAtTop.
    def exitLinageLinesAtTop(self, ctx:CobolIsuzuParser.LinageLinesAtTopContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#linageLinesAtBottom.
    def enterLinageLinesAtBottom(self, ctx:CobolIsuzuParser.LinageLinesAtBottomContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#linageLinesAtBottom.
    def exitLinageLinesAtBottom(self, ctx:CobolIsuzuParser.LinageLinesAtBottomContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#recordingModeClause.
    def enterRecordingModeClause(self, ctx:CobolIsuzuParser.RecordingModeClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#recordingModeClause.
    def exitRecordingModeClause(self, ctx:CobolIsuzuParser.RecordingModeClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#modeStatement.
    def enterModeStatement(self, ctx:CobolIsuzuParser.ModeStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#modeStatement.
    def exitModeStatement(self, ctx:CobolIsuzuParser.ModeStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#codeSetClause.
    def enterCodeSetClause(self, ctx:CobolIsuzuParser.CodeSetClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#codeSetClause.
    def exitCodeSetClause(self, ctx:CobolIsuzuParser.CodeSetClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportClause.
    def enterReportClause(self, ctx:CobolIsuzuParser.ReportClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportClause.
    def exitReportClause(self, ctx:CobolIsuzuParser.ReportClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataBaseSection.
    def enterDataBaseSection(self, ctx:CobolIsuzuParser.DataBaseSectionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataBaseSection.
    def exitDataBaseSection(self, ctx:CobolIsuzuParser.DataBaseSectionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataBaseSectionEntry.
    def enterDataBaseSectionEntry(self, ctx:CobolIsuzuParser.DataBaseSectionEntryContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataBaseSectionEntry.
    def exitDataBaseSectionEntry(self, ctx:CobolIsuzuParser.DataBaseSectionEntryContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#workingStorageSection.
    def enterWorkingStorageSection(self, ctx:CobolIsuzuParser.WorkingStorageSectionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#workingStorageSection.
    def exitWorkingStorageSection(self, ctx:CobolIsuzuParser.WorkingStorageSectionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#constantSection.
    def enterConstantSection(self, ctx:CobolIsuzuParser.ConstantSectionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#constantSection.
    def exitConstantSection(self, ctx:CobolIsuzuParser.ConstantSectionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#linkageSection.
    def enterLinkageSection(self, ctx:CobolIsuzuParser.LinkageSectionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#linkageSection.
    def exitLinkageSection(self, ctx:CobolIsuzuParser.LinkageSectionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#communicationSection.
    def enterCommunicationSection(self, ctx:CobolIsuzuParser.CommunicationSectionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#communicationSection.
    def exitCommunicationSection(self, ctx:CobolIsuzuParser.CommunicationSectionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#communicationDescriptionEntry.
    def enterCommunicationDescriptionEntry(self, ctx:CobolIsuzuParser.CommunicationDescriptionEntryContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#communicationDescriptionEntry.
    def exitCommunicationDescriptionEntry(self, ctx:CobolIsuzuParser.CommunicationDescriptionEntryContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#communicationDescriptionEntryFormat1.
    def enterCommunicationDescriptionEntryFormat1(self, ctx:CobolIsuzuParser.CommunicationDescriptionEntryFormat1Context):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#communicationDescriptionEntryFormat1.
    def exitCommunicationDescriptionEntryFormat1(self, ctx:CobolIsuzuParser.CommunicationDescriptionEntryFormat1Context):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#communicationDescriptionEntryFormat2.
    def enterCommunicationDescriptionEntryFormat2(self, ctx:CobolIsuzuParser.CommunicationDescriptionEntryFormat2Context):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#communicationDescriptionEntryFormat2.
    def exitCommunicationDescriptionEntryFormat2(self, ctx:CobolIsuzuParser.CommunicationDescriptionEntryFormat2Context):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#communicationDescriptionEntryFormat3.
    def enterCommunicationDescriptionEntryFormat3(self, ctx:CobolIsuzuParser.CommunicationDescriptionEntryFormat3Context):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#communicationDescriptionEntryFormat3.
    def exitCommunicationDescriptionEntryFormat3(self, ctx:CobolIsuzuParser.CommunicationDescriptionEntryFormat3Context):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#destinationCountClause.
    def enterDestinationCountClause(self, ctx:CobolIsuzuParser.DestinationCountClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#destinationCountClause.
    def exitDestinationCountClause(self, ctx:CobolIsuzuParser.DestinationCountClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#destinationTableClause.
    def enterDestinationTableClause(self, ctx:CobolIsuzuParser.DestinationTableClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#destinationTableClause.
    def exitDestinationTableClause(self, ctx:CobolIsuzuParser.DestinationTableClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#endKeyClause.
    def enterEndKeyClause(self, ctx:CobolIsuzuParser.EndKeyClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#endKeyClause.
    def exitEndKeyClause(self, ctx:CobolIsuzuParser.EndKeyClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#errorKeyClause.
    def enterErrorKeyClause(self, ctx:CobolIsuzuParser.ErrorKeyClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#errorKeyClause.
    def exitErrorKeyClause(self, ctx:CobolIsuzuParser.ErrorKeyClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#messageCountClause.
    def enterMessageCountClause(self, ctx:CobolIsuzuParser.MessageCountClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#messageCountClause.
    def exitMessageCountClause(self, ctx:CobolIsuzuParser.MessageCountClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#messageDateClause.
    def enterMessageDateClause(self, ctx:CobolIsuzuParser.MessageDateClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#messageDateClause.
    def exitMessageDateClause(self, ctx:CobolIsuzuParser.MessageDateClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#messageTimeClause.
    def enterMessageTimeClause(self, ctx:CobolIsuzuParser.MessageTimeClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#messageTimeClause.
    def exitMessageTimeClause(self, ctx:CobolIsuzuParser.MessageTimeClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#statusKeyClause.
    def enterStatusKeyClause(self, ctx:CobolIsuzuParser.StatusKeyClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#statusKeyClause.
    def exitStatusKeyClause(self, ctx:CobolIsuzuParser.StatusKeyClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#symbolicDestinationClause.
    def enterSymbolicDestinationClause(self, ctx:CobolIsuzuParser.SymbolicDestinationClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#symbolicDestinationClause.
    def exitSymbolicDestinationClause(self, ctx:CobolIsuzuParser.SymbolicDestinationClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#symbolicQueueClause.
    def enterSymbolicQueueClause(self, ctx:CobolIsuzuParser.SymbolicQueueClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#symbolicQueueClause.
    def exitSymbolicQueueClause(self, ctx:CobolIsuzuParser.SymbolicQueueClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#symbolicSourceClause.
    def enterSymbolicSourceClause(self, ctx:CobolIsuzuParser.SymbolicSourceClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#symbolicSourceClause.
    def exitSymbolicSourceClause(self, ctx:CobolIsuzuParser.SymbolicSourceClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#symbolicTerminalClause.
    def enterSymbolicTerminalClause(self, ctx:CobolIsuzuParser.SymbolicTerminalClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#symbolicTerminalClause.
    def exitSymbolicTerminalClause(self, ctx:CobolIsuzuParser.SymbolicTerminalClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#symbolicSubQueueClause.
    def enterSymbolicSubQueueClause(self, ctx:CobolIsuzuParser.SymbolicSubQueueClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#symbolicSubQueueClause.
    def exitSymbolicSubQueueClause(self, ctx:CobolIsuzuParser.SymbolicSubQueueClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#textLengthClause.
    def enterTextLengthClause(self, ctx:CobolIsuzuParser.TextLengthClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#textLengthClause.
    def exitTextLengthClause(self, ctx:CobolIsuzuParser.TextLengthClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#localStorageSection.
    def enterLocalStorageSection(self, ctx:CobolIsuzuParser.LocalStorageSectionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#localStorageSection.
    def exitLocalStorageSection(self, ctx:CobolIsuzuParser.LocalStorageSectionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenSection.
    def enterScreenSection(self, ctx:CobolIsuzuParser.ScreenSectionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenSection.
    def exitScreenSection(self, ctx:CobolIsuzuParser.ScreenSectionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenDescriptionEntry.
    def enterScreenDescriptionEntry(self, ctx:CobolIsuzuParser.ScreenDescriptionEntryContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenDescriptionEntry.
    def exitScreenDescriptionEntry(self, ctx:CobolIsuzuParser.ScreenDescriptionEntryContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenDescriptionBlankClause.
    def enterScreenDescriptionBlankClause(self, ctx:CobolIsuzuParser.ScreenDescriptionBlankClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenDescriptionBlankClause.
    def exitScreenDescriptionBlankClause(self, ctx:CobolIsuzuParser.ScreenDescriptionBlankClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenDescriptionBellClause.
    def enterScreenDescriptionBellClause(self, ctx:CobolIsuzuParser.ScreenDescriptionBellClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenDescriptionBellClause.
    def exitScreenDescriptionBellClause(self, ctx:CobolIsuzuParser.ScreenDescriptionBellClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenDescriptionBlinkClause.
    def enterScreenDescriptionBlinkClause(self, ctx:CobolIsuzuParser.ScreenDescriptionBlinkClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenDescriptionBlinkClause.
    def exitScreenDescriptionBlinkClause(self, ctx:CobolIsuzuParser.ScreenDescriptionBlinkClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenDescriptionEraseClause.
    def enterScreenDescriptionEraseClause(self, ctx:CobolIsuzuParser.ScreenDescriptionEraseClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenDescriptionEraseClause.
    def exitScreenDescriptionEraseClause(self, ctx:CobolIsuzuParser.ScreenDescriptionEraseClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenDescriptionLightClause.
    def enterScreenDescriptionLightClause(self, ctx:CobolIsuzuParser.ScreenDescriptionLightClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenDescriptionLightClause.
    def exitScreenDescriptionLightClause(self, ctx:CobolIsuzuParser.ScreenDescriptionLightClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenDescriptionGridClause.
    def enterScreenDescriptionGridClause(self, ctx:CobolIsuzuParser.ScreenDescriptionGridClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenDescriptionGridClause.
    def exitScreenDescriptionGridClause(self, ctx:CobolIsuzuParser.ScreenDescriptionGridClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenDescriptionReverseVideoClause.
    def enterScreenDescriptionReverseVideoClause(self, ctx:CobolIsuzuParser.ScreenDescriptionReverseVideoClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenDescriptionReverseVideoClause.
    def exitScreenDescriptionReverseVideoClause(self, ctx:CobolIsuzuParser.ScreenDescriptionReverseVideoClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenDescriptionUnderlineClause.
    def enterScreenDescriptionUnderlineClause(self, ctx:CobolIsuzuParser.ScreenDescriptionUnderlineClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenDescriptionUnderlineClause.
    def exitScreenDescriptionUnderlineClause(self, ctx:CobolIsuzuParser.ScreenDescriptionUnderlineClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenDescriptionSizeClause.
    def enterScreenDescriptionSizeClause(self, ctx:CobolIsuzuParser.ScreenDescriptionSizeClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenDescriptionSizeClause.
    def exitScreenDescriptionSizeClause(self, ctx:CobolIsuzuParser.ScreenDescriptionSizeClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenDescriptionLineClause.
    def enterScreenDescriptionLineClause(self, ctx:CobolIsuzuParser.ScreenDescriptionLineClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenDescriptionLineClause.
    def exitScreenDescriptionLineClause(self, ctx:CobolIsuzuParser.ScreenDescriptionLineClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenDescriptionColumnClause.
    def enterScreenDescriptionColumnClause(self, ctx:CobolIsuzuParser.ScreenDescriptionColumnClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenDescriptionColumnClause.
    def exitScreenDescriptionColumnClause(self, ctx:CobolIsuzuParser.ScreenDescriptionColumnClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenDescriptionForegroundColorClause.
    def enterScreenDescriptionForegroundColorClause(self, ctx:CobolIsuzuParser.ScreenDescriptionForegroundColorClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenDescriptionForegroundColorClause.
    def exitScreenDescriptionForegroundColorClause(self, ctx:CobolIsuzuParser.ScreenDescriptionForegroundColorClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenDescriptionBackgroundColorClause.
    def enterScreenDescriptionBackgroundColorClause(self, ctx:CobolIsuzuParser.ScreenDescriptionBackgroundColorClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenDescriptionBackgroundColorClause.
    def exitScreenDescriptionBackgroundColorClause(self, ctx:CobolIsuzuParser.ScreenDescriptionBackgroundColorClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenDescriptionControlClause.
    def enterScreenDescriptionControlClause(self, ctx:CobolIsuzuParser.ScreenDescriptionControlClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenDescriptionControlClause.
    def exitScreenDescriptionControlClause(self, ctx:CobolIsuzuParser.ScreenDescriptionControlClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenDescriptionValueClause.
    def enterScreenDescriptionValueClause(self, ctx:CobolIsuzuParser.ScreenDescriptionValueClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenDescriptionValueClause.
    def exitScreenDescriptionValueClause(self, ctx:CobolIsuzuParser.ScreenDescriptionValueClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenDescriptionPictureClause.
    def enterScreenDescriptionPictureClause(self, ctx:CobolIsuzuParser.ScreenDescriptionPictureClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenDescriptionPictureClause.
    def exitScreenDescriptionPictureClause(self, ctx:CobolIsuzuParser.ScreenDescriptionPictureClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenDescriptionFromClause.
    def enterScreenDescriptionFromClause(self, ctx:CobolIsuzuParser.ScreenDescriptionFromClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenDescriptionFromClause.
    def exitScreenDescriptionFromClause(self, ctx:CobolIsuzuParser.ScreenDescriptionFromClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenDescriptionToClause.
    def enterScreenDescriptionToClause(self, ctx:CobolIsuzuParser.ScreenDescriptionToClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenDescriptionToClause.
    def exitScreenDescriptionToClause(self, ctx:CobolIsuzuParser.ScreenDescriptionToClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenDescriptionUsingClause.
    def enterScreenDescriptionUsingClause(self, ctx:CobolIsuzuParser.ScreenDescriptionUsingClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenDescriptionUsingClause.
    def exitScreenDescriptionUsingClause(self, ctx:CobolIsuzuParser.ScreenDescriptionUsingClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenDescriptionUsageClause.
    def enterScreenDescriptionUsageClause(self, ctx:CobolIsuzuParser.ScreenDescriptionUsageClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenDescriptionUsageClause.
    def exitScreenDescriptionUsageClause(self, ctx:CobolIsuzuParser.ScreenDescriptionUsageClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenDescriptionBlankWhenZeroClause.
    def enterScreenDescriptionBlankWhenZeroClause(self, ctx:CobolIsuzuParser.ScreenDescriptionBlankWhenZeroClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenDescriptionBlankWhenZeroClause.
    def exitScreenDescriptionBlankWhenZeroClause(self, ctx:CobolIsuzuParser.ScreenDescriptionBlankWhenZeroClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenDescriptionJustifiedClause.
    def enterScreenDescriptionJustifiedClause(self, ctx:CobolIsuzuParser.ScreenDescriptionJustifiedClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenDescriptionJustifiedClause.
    def exitScreenDescriptionJustifiedClause(self, ctx:CobolIsuzuParser.ScreenDescriptionJustifiedClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenDescriptionSignClause.
    def enterScreenDescriptionSignClause(self, ctx:CobolIsuzuParser.ScreenDescriptionSignClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenDescriptionSignClause.
    def exitScreenDescriptionSignClause(self, ctx:CobolIsuzuParser.ScreenDescriptionSignClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenDescriptionAutoClause.
    def enterScreenDescriptionAutoClause(self, ctx:CobolIsuzuParser.ScreenDescriptionAutoClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenDescriptionAutoClause.
    def exitScreenDescriptionAutoClause(self, ctx:CobolIsuzuParser.ScreenDescriptionAutoClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenDescriptionSecureClause.
    def enterScreenDescriptionSecureClause(self, ctx:CobolIsuzuParser.ScreenDescriptionSecureClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenDescriptionSecureClause.
    def exitScreenDescriptionSecureClause(self, ctx:CobolIsuzuParser.ScreenDescriptionSecureClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenDescriptionRequiredClause.
    def enterScreenDescriptionRequiredClause(self, ctx:CobolIsuzuParser.ScreenDescriptionRequiredClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenDescriptionRequiredClause.
    def exitScreenDescriptionRequiredClause(self, ctx:CobolIsuzuParser.ScreenDescriptionRequiredClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenDescriptionPromptClause.
    def enterScreenDescriptionPromptClause(self, ctx:CobolIsuzuParser.ScreenDescriptionPromptClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenDescriptionPromptClause.
    def exitScreenDescriptionPromptClause(self, ctx:CobolIsuzuParser.ScreenDescriptionPromptClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenDescriptionPromptOccursClause.
    def enterScreenDescriptionPromptOccursClause(self, ctx:CobolIsuzuParser.ScreenDescriptionPromptOccursClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenDescriptionPromptOccursClause.
    def exitScreenDescriptionPromptOccursClause(self, ctx:CobolIsuzuParser.ScreenDescriptionPromptOccursClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenDescriptionFullClause.
    def enterScreenDescriptionFullClause(self, ctx:CobolIsuzuParser.ScreenDescriptionFullClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenDescriptionFullClause.
    def exitScreenDescriptionFullClause(self, ctx:CobolIsuzuParser.ScreenDescriptionFullClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenDescriptionZeroFillClause.
    def enterScreenDescriptionZeroFillClause(self, ctx:CobolIsuzuParser.ScreenDescriptionZeroFillClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenDescriptionZeroFillClause.
    def exitScreenDescriptionZeroFillClause(self, ctx:CobolIsuzuParser.ScreenDescriptionZeroFillClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportSection.
    def enterReportSection(self, ctx:CobolIsuzuParser.ReportSectionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportSection.
    def exitReportSection(self, ctx:CobolIsuzuParser.ReportSectionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportDescription.
    def enterReportDescription(self, ctx:CobolIsuzuParser.ReportDescriptionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportDescription.
    def exitReportDescription(self, ctx:CobolIsuzuParser.ReportDescriptionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportDescriptionEntry.
    def enterReportDescriptionEntry(self, ctx:CobolIsuzuParser.ReportDescriptionEntryContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportDescriptionEntry.
    def exitReportDescriptionEntry(self, ctx:CobolIsuzuParser.ReportDescriptionEntryContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportDescriptionGlobalClause.
    def enterReportDescriptionGlobalClause(self, ctx:CobolIsuzuParser.ReportDescriptionGlobalClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportDescriptionGlobalClause.
    def exitReportDescriptionGlobalClause(self, ctx:CobolIsuzuParser.ReportDescriptionGlobalClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportDescriptionPageLimitClause.
    def enterReportDescriptionPageLimitClause(self, ctx:CobolIsuzuParser.ReportDescriptionPageLimitClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportDescriptionPageLimitClause.
    def exitReportDescriptionPageLimitClause(self, ctx:CobolIsuzuParser.ReportDescriptionPageLimitClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportDescriptionHeadingClause.
    def enterReportDescriptionHeadingClause(self, ctx:CobolIsuzuParser.ReportDescriptionHeadingClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportDescriptionHeadingClause.
    def exitReportDescriptionHeadingClause(self, ctx:CobolIsuzuParser.ReportDescriptionHeadingClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportDescriptionFirstDetailClause.
    def enterReportDescriptionFirstDetailClause(self, ctx:CobolIsuzuParser.ReportDescriptionFirstDetailClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportDescriptionFirstDetailClause.
    def exitReportDescriptionFirstDetailClause(self, ctx:CobolIsuzuParser.ReportDescriptionFirstDetailClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportDescriptionLastDetailClause.
    def enterReportDescriptionLastDetailClause(self, ctx:CobolIsuzuParser.ReportDescriptionLastDetailClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportDescriptionLastDetailClause.
    def exitReportDescriptionLastDetailClause(self, ctx:CobolIsuzuParser.ReportDescriptionLastDetailClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportDescriptionFootingClause.
    def enterReportDescriptionFootingClause(self, ctx:CobolIsuzuParser.ReportDescriptionFootingClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportDescriptionFootingClause.
    def exitReportDescriptionFootingClause(self, ctx:CobolIsuzuParser.ReportDescriptionFootingClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportGroupDescriptionEntry.
    def enterReportGroupDescriptionEntry(self, ctx:CobolIsuzuParser.ReportGroupDescriptionEntryContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportGroupDescriptionEntry.
    def exitReportGroupDescriptionEntry(self, ctx:CobolIsuzuParser.ReportGroupDescriptionEntryContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportGroupDescriptionEntryFormat1.
    def enterReportGroupDescriptionEntryFormat1(self, ctx:CobolIsuzuParser.ReportGroupDescriptionEntryFormat1Context):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportGroupDescriptionEntryFormat1.
    def exitReportGroupDescriptionEntryFormat1(self, ctx:CobolIsuzuParser.ReportGroupDescriptionEntryFormat1Context):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportGroupDescriptionEntryFormat2.
    def enterReportGroupDescriptionEntryFormat2(self, ctx:CobolIsuzuParser.ReportGroupDescriptionEntryFormat2Context):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportGroupDescriptionEntryFormat2.
    def exitReportGroupDescriptionEntryFormat2(self, ctx:CobolIsuzuParser.ReportGroupDescriptionEntryFormat2Context):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportGroupDescriptionEntryFormat3.
    def enterReportGroupDescriptionEntryFormat3(self, ctx:CobolIsuzuParser.ReportGroupDescriptionEntryFormat3Context):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportGroupDescriptionEntryFormat3.
    def exitReportGroupDescriptionEntryFormat3(self, ctx:CobolIsuzuParser.ReportGroupDescriptionEntryFormat3Context):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportGroupBlankWhenZeroClause.
    def enterReportGroupBlankWhenZeroClause(self, ctx:CobolIsuzuParser.ReportGroupBlankWhenZeroClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportGroupBlankWhenZeroClause.
    def exitReportGroupBlankWhenZeroClause(self, ctx:CobolIsuzuParser.ReportGroupBlankWhenZeroClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportGroupColumnNumberClause.
    def enterReportGroupColumnNumberClause(self, ctx:CobolIsuzuParser.ReportGroupColumnNumberClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportGroupColumnNumberClause.
    def exitReportGroupColumnNumberClause(self, ctx:CobolIsuzuParser.ReportGroupColumnNumberClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportGroupIndicateClause.
    def enterReportGroupIndicateClause(self, ctx:CobolIsuzuParser.ReportGroupIndicateClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportGroupIndicateClause.
    def exitReportGroupIndicateClause(self, ctx:CobolIsuzuParser.ReportGroupIndicateClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportGroupJustifiedClause.
    def enterReportGroupJustifiedClause(self, ctx:CobolIsuzuParser.ReportGroupJustifiedClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportGroupJustifiedClause.
    def exitReportGroupJustifiedClause(self, ctx:CobolIsuzuParser.ReportGroupJustifiedClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportGroupLineNumberClause.
    def enterReportGroupLineNumberClause(self, ctx:CobolIsuzuParser.ReportGroupLineNumberClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportGroupLineNumberClause.
    def exitReportGroupLineNumberClause(self, ctx:CobolIsuzuParser.ReportGroupLineNumberClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportGroupLineNumberNextPage.
    def enterReportGroupLineNumberNextPage(self, ctx:CobolIsuzuParser.ReportGroupLineNumberNextPageContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportGroupLineNumberNextPage.
    def exitReportGroupLineNumberNextPage(self, ctx:CobolIsuzuParser.ReportGroupLineNumberNextPageContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportGroupLineNumberPlus.
    def enterReportGroupLineNumberPlus(self, ctx:CobolIsuzuParser.ReportGroupLineNumberPlusContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportGroupLineNumberPlus.
    def exitReportGroupLineNumberPlus(self, ctx:CobolIsuzuParser.ReportGroupLineNumberPlusContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportGroupNextGroupClause.
    def enterReportGroupNextGroupClause(self, ctx:CobolIsuzuParser.ReportGroupNextGroupClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportGroupNextGroupClause.
    def exitReportGroupNextGroupClause(self, ctx:CobolIsuzuParser.ReportGroupNextGroupClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportGroupNextGroupPlus.
    def enterReportGroupNextGroupPlus(self, ctx:CobolIsuzuParser.ReportGroupNextGroupPlusContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportGroupNextGroupPlus.
    def exitReportGroupNextGroupPlus(self, ctx:CobolIsuzuParser.ReportGroupNextGroupPlusContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportGroupNextGroupNextPage.
    def enterReportGroupNextGroupNextPage(self, ctx:CobolIsuzuParser.ReportGroupNextGroupNextPageContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportGroupNextGroupNextPage.
    def exitReportGroupNextGroupNextPage(self, ctx:CobolIsuzuParser.ReportGroupNextGroupNextPageContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportGroupPictureClause.
    def enterReportGroupPictureClause(self, ctx:CobolIsuzuParser.ReportGroupPictureClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportGroupPictureClause.
    def exitReportGroupPictureClause(self, ctx:CobolIsuzuParser.ReportGroupPictureClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportGroupResetClause.
    def enterReportGroupResetClause(self, ctx:CobolIsuzuParser.ReportGroupResetClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportGroupResetClause.
    def exitReportGroupResetClause(self, ctx:CobolIsuzuParser.ReportGroupResetClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportGroupSignClause.
    def enterReportGroupSignClause(self, ctx:CobolIsuzuParser.ReportGroupSignClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportGroupSignClause.
    def exitReportGroupSignClause(self, ctx:CobolIsuzuParser.ReportGroupSignClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportGroupSourceClause.
    def enterReportGroupSourceClause(self, ctx:CobolIsuzuParser.ReportGroupSourceClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportGroupSourceClause.
    def exitReportGroupSourceClause(self, ctx:CobolIsuzuParser.ReportGroupSourceClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportGroupSumClause.
    def enterReportGroupSumClause(self, ctx:CobolIsuzuParser.ReportGroupSumClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportGroupSumClause.
    def exitReportGroupSumClause(self, ctx:CobolIsuzuParser.ReportGroupSumClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportGroupTypeClause.
    def enterReportGroupTypeClause(self, ctx:CobolIsuzuParser.ReportGroupTypeClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportGroupTypeClause.
    def exitReportGroupTypeClause(self, ctx:CobolIsuzuParser.ReportGroupTypeClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportGroupTypeReportHeading.
    def enterReportGroupTypeReportHeading(self, ctx:CobolIsuzuParser.ReportGroupTypeReportHeadingContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportGroupTypeReportHeading.
    def exitReportGroupTypeReportHeading(self, ctx:CobolIsuzuParser.ReportGroupTypeReportHeadingContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportGroupTypePageHeading.
    def enterReportGroupTypePageHeading(self, ctx:CobolIsuzuParser.ReportGroupTypePageHeadingContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportGroupTypePageHeading.
    def exitReportGroupTypePageHeading(self, ctx:CobolIsuzuParser.ReportGroupTypePageHeadingContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportGroupTypeControlHeading.
    def enterReportGroupTypeControlHeading(self, ctx:CobolIsuzuParser.ReportGroupTypeControlHeadingContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportGroupTypeControlHeading.
    def exitReportGroupTypeControlHeading(self, ctx:CobolIsuzuParser.ReportGroupTypeControlHeadingContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportGroupTypeDetail.
    def enterReportGroupTypeDetail(self, ctx:CobolIsuzuParser.ReportGroupTypeDetailContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportGroupTypeDetail.
    def exitReportGroupTypeDetail(self, ctx:CobolIsuzuParser.ReportGroupTypeDetailContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportGroupTypeControlFooting.
    def enterReportGroupTypeControlFooting(self, ctx:CobolIsuzuParser.ReportGroupTypeControlFootingContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportGroupTypeControlFooting.
    def exitReportGroupTypeControlFooting(self, ctx:CobolIsuzuParser.ReportGroupTypeControlFootingContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportGroupUsageClause.
    def enterReportGroupUsageClause(self, ctx:CobolIsuzuParser.ReportGroupUsageClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportGroupUsageClause.
    def exitReportGroupUsageClause(self, ctx:CobolIsuzuParser.ReportGroupUsageClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportGroupTypePageFooting.
    def enterReportGroupTypePageFooting(self, ctx:CobolIsuzuParser.ReportGroupTypePageFootingContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportGroupTypePageFooting.
    def exitReportGroupTypePageFooting(self, ctx:CobolIsuzuParser.ReportGroupTypePageFootingContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportGroupTypeReportFooting.
    def enterReportGroupTypeReportFooting(self, ctx:CobolIsuzuParser.ReportGroupTypeReportFootingContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportGroupTypeReportFooting.
    def exitReportGroupTypeReportFooting(self, ctx:CobolIsuzuParser.ReportGroupTypeReportFootingContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportGroupValueClause.
    def enterReportGroupValueClause(self, ctx:CobolIsuzuParser.ReportGroupValueClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportGroupValueClause.
    def exitReportGroupValueClause(self, ctx:CobolIsuzuParser.ReportGroupValueClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#programLibrarySection.
    def enterProgramLibrarySection(self, ctx:CobolIsuzuParser.ProgramLibrarySectionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#programLibrarySection.
    def exitProgramLibrarySection(self, ctx:CobolIsuzuParser.ProgramLibrarySectionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#libraryDescriptionEntry.
    def enterLibraryDescriptionEntry(self, ctx:CobolIsuzuParser.LibraryDescriptionEntryContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#libraryDescriptionEntry.
    def exitLibraryDescriptionEntry(self, ctx:CobolIsuzuParser.LibraryDescriptionEntryContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#libraryDescriptionEntryFormat1.
    def enterLibraryDescriptionEntryFormat1(self, ctx:CobolIsuzuParser.LibraryDescriptionEntryFormat1Context):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#libraryDescriptionEntryFormat1.
    def exitLibraryDescriptionEntryFormat1(self, ctx:CobolIsuzuParser.LibraryDescriptionEntryFormat1Context):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#libraryDescriptionEntryFormat2.
    def enterLibraryDescriptionEntryFormat2(self, ctx:CobolIsuzuParser.LibraryDescriptionEntryFormat2Context):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#libraryDescriptionEntryFormat2.
    def exitLibraryDescriptionEntryFormat2(self, ctx:CobolIsuzuParser.LibraryDescriptionEntryFormat2Context):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#libraryAttributeClauseFormat1.
    def enterLibraryAttributeClauseFormat1(self, ctx:CobolIsuzuParser.LibraryAttributeClauseFormat1Context):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#libraryAttributeClauseFormat1.
    def exitLibraryAttributeClauseFormat1(self, ctx:CobolIsuzuParser.LibraryAttributeClauseFormat1Context):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#libraryAttributeClauseFormat2.
    def enterLibraryAttributeClauseFormat2(self, ctx:CobolIsuzuParser.LibraryAttributeClauseFormat2Context):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#libraryAttributeClauseFormat2.
    def exitLibraryAttributeClauseFormat2(self, ctx:CobolIsuzuParser.LibraryAttributeClauseFormat2Context):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#libraryAttributeFunction.
    def enterLibraryAttributeFunction(self, ctx:CobolIsuzuParser.LibraryAttributeFunctionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#libraryAttributeFunction.
    def exitLibraryAttributeFunction(self, ctx:CobolIsuzuParser.LibraryAttributeFunctionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#libraryAttributeParameter.
    def enterLibraryAttributeParameter(self, ctx:CobolIsuzuParser.LibraryAttributeParameterContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#libraryAttributeParameter.
    def exitLibraryAttributeParameter(self, ctx:CobolIsuzuParser.LibraryAttributeParameterContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#libraryAttributeTitle.
    def enterLibraryAttributeTitle(self, ctx:CobolIsuzuParser.LibraryAttributeTitleContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#libraryAttributeTitle.
    def exitLibraryAttributeTitle(self, ctx:CobolIsuzuParser.LibraryAttributeTitleContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#libraryEntryProcedureClauseFormat1.
    def enterLibraryEntryProcedureClauseFormat1(self, ctx:CobolIsuzuParser.LibraryEntryProcedureClauseFormat1Context):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#libraryEntryProcedureClauseFormat1.
    def exitLibraryEntryProcedureClauseFormat1(self, ctx:CobolIsuzuParser.LibraryEntryProcedureClauseFormat1Context):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#libraryEntryProcedureClauseFormat2.
    def enterLibraryEntryProcedureClauseFormat2(self, ctx:CobolIsuzuParser.LibraryEntryProcedureClauseFormat2Context):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#libraryEntryProcedureClauseFormat2.
    def exitLibraryEntryProcedureClauseFormat2(self, ctx:CobolIsuzuParser.LibraryEntryProcedureClauseFormat2Context):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#libraryEntryProcedureForClause.
    def enterLibraryEntryProcedureForClause(self, ctx:CobolIsuzuParser.LibraryEntryProcedureForClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#libraryEntryProcedureForClause.
    def exitLibraryEntryProcedureForClause(self, ctx:CobolIsuzuParser.LibraryEntryProcedureForClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#libraryEntryProcedureGivingClause.
    def enterLibraryEntryProcedureGivingClause(self, ctx:CobolIsuzuParser.LibraryEntryProcedureGivingClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#libraryEntryProcedureGivingClause.
    def exitLibraryEntryProcedureGivingClause(self, ctx:CobolIsuzuParser.LibraryEntryProcedureGivingClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#libraryEntryProcedureUsingClause.
    def enterLibraryEntryProcedureUsingClause(self, ctx:CobolIsuzuParser.LibraryEntryProcedureUsingClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#libraryEntryProcedureUsingClause.
    def exitLibraryEntryProcedureUsingClause(self, ctx:CobolIsuzuParser.LibraryEntryProcedureUsingClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#libraryEntryProcedureUsingName.
    def enterLibraryEntryProcedureUsingName(self, ctx:CobolIsuzuParser.LibraryEntryProcedureUsingNameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#libraryEntryProcedureUsingName.
    def exitLibraryEntryProcedureUsingName(self, ctx:CobolIsuzuParser.LibraryEntryProcedureUsingNameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#libraryEntryProcedureWithClause.
    def enterLibraryEntryProcedureWithClause(self, ctx:CobolIsuzuParser.LibraryEntryProcedureWithClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#libraryEntryProcedureWithClause.
    def exitLibraryEntryProcedureWithClause(self, ctx:CobolIsuzuParser.LibraryEntryProcedureWithClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#libraryEntryProcedureWithName.
    def enterLibraryEntryProcedureWithName(self, ctx:CobolIsuzuParser.LibraryEntryProcedureWithNameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#libraryEntryProcedureWithName.
    def exitLibraryEntryProcedureWithName(self, ctx:CobolIsuzuParser.LibraryEntryProcedureWithNameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#libraryIsCommonClause.
    def enterLibraryIsCommonClause(self, ctx:CobolIsuzuParser.LibraryIsCommonClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#libraryIsCommonClause.
    def exitLibraryIsCommonClause(self, ctx:CobolIsuzuParser.LibraryIsCommonClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#libraryIsGlobalClause.
    def enterLibraryIsGlobalClause(self, ctx:CobolIsuzuParser.LibraryIsGlobalClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#libraryIsGlobalClause.
    def exitLibraryIsGlobalClause(self, ctx:CobolIsuzuParser.LibraryIsGlobalClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataDescriptionEntry.
    def enterDataDescriptionEntry(self, ctx:CobolIsuzuParser.DataDescriptionEntryContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataDescriptionEntry.
    def exitDataDescriptionEntry(self, ctx:CobolIsuzuParser.DataDescriptionEntryContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#copyStatement.
    def enterCopyStatement(self, ctx:CobolIsuzuParser.CopyStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#copyStatement.
    def exitCopyStatement(self, ctx:CobolIsuzuParser.CopyStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#disjoinPhrase.
    def enterDisjoinPhrase(self, ctx:CobolIsuzuParser.DisjoinPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#disjoinPhrase.
    def exitDisjoinPhrase(self, ctx:CobolIsuzuParser.DisjoinPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#joinPhrase.
    def enterJoinPhrase(self, ctx:CobolIsuzuParser.JoinPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#joinPhrase.
    def exitJoinPhrase(self, ctx:CobolIsuzuParser.JoinPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#copySource.
    def enterCopySource(self, ctx:CobolIsuzuParser.CopySourceContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#copySource.
    def exitCopySource(self, ctx:CobolIsuzuParser.CopySourceContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#copyLibrary.
    def enterCopyLibrary(self, ctx:CobolIsuzuParser.CopyLibraryContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#copyLibrary.
    def exitCopyLibrary(self, ctx:CobolIsuzuParser.CopyLibraryContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#replacingPhrase.
    def enterReplacingPhrase(self, ctx:CobolIsuzuParser.ReplacingPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#replacingPhrase.
    def exitReplacingPhrase(self, ctx:CobolIsuzuParser.ReplacingPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#replaceArea.
    def enterReplaceArea(self, ctx:CobolIsuzuParser.ReplaceAreaContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#replaceArea.
    def exitReplaceArea(self, ctx:CobolIsuzuParser.ReplaceAreaContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#replaceByStatement.
    def enterReplaceByStatement(self, ctx:CobolIsuzuParser.ReplaceByStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#replaceByStatement.
    def exitReplaceByStatement(self, ctx:CobolIsuzuParser.ReplaceByStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#replaceOffStatement.
    def enterReplaceOffStatement(self, ctx:CobolIsuzuParser.ReplaceOffStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#replaceOffStatement.
    def exitReplaceOffStatement(self, ctx:CobolIsuzuParser.ReplaceOffStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#replaceClause.
    def enterReplaceClause(self, ctx:CobolIsuzuParser.ReplaceClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#replaceClause.
    def exitReplaceClause(self, ctx:CobolIsuzuParser.ReplaceClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#directoryPhrase.
    def enterDirectoryPhrase(self, ctx:CobolIsuzuParser.DirectoryPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#directoryPhrase.
    def exitDirectoryPhrase(self, ctx:CobolIsuzuParser.DirectoryPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#familyPhrase.
    def enterFamilyPhrase(self, ctx:CobolIsuzuParser.FamilyPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#familyPhrase.
    def exitFamilyPhrase(self, ctx:CobolIsuzuParser.FamilyPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#replaceable.
    def enterReplaceable(self, ctx:CobolIsuzuParser.ReplaceableContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#replaceable.
    def exitReplaceable(self, ctx:CobolIsuzuParser.ReplaceableContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#replacement.
    def enterReplacement(self, ctx:CobolIsuzuParser.ReplacementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#replacement.
    def exitReplacement(self, ctx:CobolIsuzuParser.ReplacementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#ejectStatement.
    def enterEjectStatement(self, ctx:CobolIsuzuParser.EjectStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#ejectStatement.
    def exitEjectStatement(self, ctx:CobolIsuzuParser.EjectStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#skipStatement.
    def enterSkipStatement(self, ctx:CobolIsuzuParser.SkipStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#skipStatement.
    def exitSkipStatement(self, ctx:CobolIsuzuParser.SkipStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#titleStatement.
    def enterTitleStatement(self, ctx:CobolIsuzuParser.TitleStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#titleStatement.
    def exitTitleStatement(self, ctx:CobolIsuzuParser.TitleStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#pseudoText.
    def enterPseudoText(self, ctx:CobolIsuzuParser.PseudoTextContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#pseudoText.
    def exitPseudoText(self, ctx:CobolIsuzuParser.PseudoTextContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#charData.
    def enterCharData(self, ctx:CobolIsuzuParser.CharDataContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#charData.
    def exitCharData(self, ctx:CobolIsuzuParser.CharDataContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#charDataSql.
    def enterCharDataSql(self, ctx:CobolIsuzuParser.CharDataSqlContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#charDataSql.
    def exitCharDataSql(self, ctx:CobolIsuzuParser.CharDataSqlContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#charDataLine.
    def enterCharDataLine(self, ctx:CobolIsuzuParser.CharDataLineContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#charDataLine.
    def exitCharDataLine(self, ctx:CobolIsuzuParser.CharDataLineContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#cobolWord.
    def enterCobolWord(self, ctx:CobolIsuzuParser.CobolWordContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#cobolWord.
    def exitCobolWord(self, ctx:CobolIsuzuParser.CobolWordContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#literal.
    def enterLiteral(self, ctx:CobolIsuzuParser.LiteralContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#literal.
    def exitLiteral(self, ctx:CobolIsuzuParser.LiteralContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#jpEncodingText.
    def enterJpEncodingText(self, ctx:CobolIsuzuParser.JpEncodingTextContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#jpEncodingText.
    def exitJpEncodingText(self, ctx:CobolIsuzuParser.JpEncodingTextContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#filename.
    def enterFilename(self, ctx:CobolIsuzuParser.FilenameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#filename.
    def exitFilename(self, ctx:CobolIsuzuParser.FilenameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataDescriptionEntryFormat1.
    def enterDataDescriptionEntryFormat1(self, ctx:CobolIsuzuParser.DataDescriptionEntryFormat1Context):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataDescriptionEntryFormat1.
    def exitDataDescriptionEntryFormat1(self, ctx:CobolIsuzuParser.DataDescriptionEntryFormat1Context):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataPrintClause.
    def enterDataPrintClause(self, ctx:CobolIsuzuParser.DataPrintClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataPrintClause.
    def exitDataPrintClause(self, ctx:CobolIsuzuParser.DataPrintClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataCharacterClause.
    def enterDataCharacterClause(self, ctx:CobolIsuzuParser.DataCharacterClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataCharacterClause.
    def exitDataCharacterClause(self, ctx:CobolIsuzuParser.DataCharacterClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataDescriptionEntryFormat3.
    def enterDataDescriptionEntryFormat3(self, ctx:CobolIsuzuParser.DataDescriptionEntryFormat3Context):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataDescriptionEntryFormat3.
    def exitDataDescriptionEntryFormat3(self, ctx:CobolIsuzuParser.DataDescriptionEntryFormat3Context):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataDescriptionEntryFormat2.
    def enterDataDescriptionEntryFormat2(self, ctx:CobolIsuzuParser.DataDescriptionEntryFormat2Context):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataDescriptionEntryFormat2.
    def exitDataDescriptionEntryFormat2(self, ctx:CobolIsuzuParser.DataDescriptionEntryFormat2Context):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataDescriptionEntryExecSql.
    def enterDataDescriptionEntryExecSql(self, ctx:CobolIsuzuParser.DataDescriptionEntryExecSqlContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataDescriptionEntryExecSql.
    def exitDataDescriptionEntryExecSql(self, ctx:CobolIsuzuParser.DataDescriptionEntryExecSqlContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataAlignedClause.
    def enterDataAlignedClause(self, ctx:CobolIsuzuParser.DataAlignedClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataAlignedClause.
    def exitDataAlignedClause(self, ctx:CobolIsuzuParser.DataAlignedClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataBlankWhenZeroClause.
    def enterDataBlankWhenZeroClause(self, ctx:CobolIsuzuParser.DataBlankWhenZeroClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataBlankWhenZeroClause.
    def exitDataBlankWhenZeroClause(self, ctx:CobolIsuzuParser.DataBlankWhenZeroClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataCommonOwnLocalClause.
    def enterDataCommonOwnLocalClause(self, ctx:CobolIsuzuParser.DataCommonOwnLocalClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataCommonOwnLocalClause.
    def exitDataCommonOwnLocalClause(self, ctx:CobolIsuzuParser.DataCommonOwnLocalClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataExternalClause.
    def enterDataExternalClause(self, ctx:CobolIsuzuParser.DataExternalClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataExternalClause.
    def exitDataExternalClause(self, ctx:CobolIsuzuParser.DataExternalClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataGlobalClause.
    def enterDataGlobalClause(self, ctx:CobolIsuzuParser.DataGlobalClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataGlobalClause.
    def exitDataGlobalClause(self, ctx:CobolIsuzuParser.DataGlobalClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataIntegerStringClause.
    def enterDataIntegerStringClause(self, ctx:CobolIsuzuParser.DataIntegerStringClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataIntegerStringClause.
    def exitDataIntegerStringClause(self, ctx:CobolIsuzuParser.DataIntegerStringClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataJustifiedClause.
    def enterDataJustifiedClause(self, ctx:CobolIsuzuParser.DataJustifiedClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataJustifiedClause.
    def exitDataJustifiedClause(self, ctx:CobolIsuzuParser.DataJustifiedClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataOccursClause.
    def enterDataOccursClause(self, ctx:CobolIsuzuParser.DataOccursClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataOccursClause.
    def exitDataOccursClause(self, ctx:CobolIsuzuParser.DataOccursClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataOccursTo.
    def enterDataOccursTo(self, ctx:CobolIsuzuParser.DataOccursToContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataOccursTo.
    def exitDataOccursTo(self, ctx:CobolIsuzuParser.DataOccursToContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataOccursSort.
    def enterDataOccursSort(self, ctx:CobolIsuzuParser.DataOccursSortContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataOccursSort.
    def exitDataOccursSort(self, ctx:CobolIsuzuParser.DataOccursSortContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataPictureClause.
    def enterDataPictureClause(self, ctx:CobolIsuzuParser.DataPictureClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataPictureClause.
    def exitDataPictureClause(self, ctx:CobolIsuzuParser.DataPictureClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#pictureString.
    def enterPictureString(self, ctx:CobolIsuzuParser.PictureStringContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#pictureString.
    def exitPictureString(self, ctx:CobolIsuzuParser.PictureStringContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#pictureChars.
    def enterPictureChars(self, ctx:CobolIsuzuParser.PictureCharsContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#pictureChars.
    def exitPictureChars(self, ctx:CobolIsuzuParser.PictureCharsContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#pictureCardinality.
    def enterPictureCardinality(self, ctx:CobolIsuzuParser.PictureCardinalityContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#pictureCardinality.
    def exitPictureCardinality(self, ctx:CobolIsuzuParser.PictureCardinalityContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataReceivedByClause.
    def enterDataReceivedByClause(self, ctx:CobolIsuzuParser.DataReceivedByClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataReceivedByClause.
    def exitDataReceivedByClause(self, ctx:CobolIsuzuParser.DataReceivedByClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataRecordAreaClause.
    def enterDataRecordAreaClause(self, ctx:CobolIsuzuParser.DataRecordAreaClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataRecordAreaClause.
    def exitDataRecordAreaClause(self, ctx:CobolIsuzuParser.DataRecordAreaClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataRedefinesClause.
    def enterDataRedefinesClause(self, ctx:CobolIsuzuParser.DataRedefinesClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataRedefinesClause.
    def exitDataRedefinesClause(self, ctx:CobolIsuzuParser.DataRedefinesClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataRenamesClause.
    def enterDataRenamesClause(self, ctx:CobolIsuzuParser.DataRenamesClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataRenamesClause.
    def exitDataRenamesClause(self, ctx:CobolIsuzuParser.DataRenamesClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataSignClause.
    def enterDataSignClause(self, ctx:CobolIsuzuParser.DataSignClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataSignClause.
    def exitDataSignClause(self, ctx:CobolIsuzuParser.DataSignClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataSynchronizedClause.
    def enterDataSynchronizedClause(self, ctx:CobolIsuzuParser.DataSynchronizedClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataSynchronizedClause.
    def exitDataSynchronizedClause(self, ctx:CobolIsuzuParser.DataSynchronizedClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataThreadLocalClause.
    def enterDataThreadLocalClause(self, ctx:CobolIsuzuParser.DataThreadLocalClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataThreadLocalClause.
    def exitDataThreadLocalClause(self, ctx:CobolIsuzuParser.DataThreadLocalClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataTypeClause.
    def enterDataTypeClause(self, ctx:CobolIsuzuParser.DataTypeClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataTypeClause.
    def exitDataTypeClause(self, ctx:CobolIsuzuParser.DataTypeClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataTypeDefClause.
    def enterDataTypeDefClause(self, ctx:CobolIsuzuParser.DataTypeDefClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataTypeDefClause.
    def exitDataTypeDefClause(self, ctx:CobolIsuzuParser.DataTypeDefClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataUsageClause.
    def enterDataUsageClause(self, ctx:CobolIsuzuParser.DataUsageClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataUsageClause.
    def exitDataUsageClause(self, ctx:CobolIsuzuParser.DataUsageClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataUsingClause.
    def enterDataUsingClause(self, ctx:CobolIsuzuParser.DataUsingClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataUsingClause.
    def exitDataUsingClause(self, ctx:CobolIsuzuParser.DataUsingClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataValueClause.
    def enterDataValueClause(self, ctx:CobolIsuzuParser.DataValueClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataValueClause.
    def exitDataValueClause(self, ctx:CobolIsuzuParser.DataValueClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataValueInterval.
    def enterDataValueInterval(self, ctx:CobolIsuzuParser.DataValueIntervalContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataValueInterval.
    def exitDataValueInterval(self, ctx:CobolIsuzuParser.DataValueIntervalContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataValueIntervalFrom.
    def enterDataValueIntervalFrom(self, ctx:CobolIsuzuParser.DataValueIntervalFromContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataValueIntervalFrom.
    def exitDataValueIntervalFrom(self, ctx:CobolIsuzuParser.DataValueIntervalFromContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataValueIntervalTo.
    def enterDataValueIntervalTo(self, ctx:CobolIsuzuParser.DataValueIntervalToContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataValueIntervalTo.
    def exitDataValueIntervalTo(self, ctx:CobolIsuzuParser.DataValueIntervalToContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataWithLowerBoundsClause.
    def enterDataWithLowerBoundsClause(self, ctx:CobolIsuzuParser.DataWithLowerBoundsClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataWithLowerBoundsClause.
    def exitDataWithLowerBoundsClause(self, ctx:CobolIsuzuParser.DataWithLowerBoundsClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#procedureDivision.
    def enterProcedureDivision(self, ctx:CobolIsuzuParser.ProcedureDivisionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#procedureDivision.
    def exitProcedureDivision(self, ctx:CobolIsuzuParser.ProcedureDivisionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#procedureDivisionUsingClause.
    def enterProcedureDivisionUsingClause(self, ctx:CobolIsuzuParser.ProcedureDivisionUsingClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#procedureDivisionUsingClause.
    def exitProcedureDivisionUsingClause(self, ctx:CobolIsuzuParser.ProcedureDivisionUsingClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#procedureDivisionGivingClause.
    def enterProcedureDivisionGivingClause(self, ctx:CobolIsuzuParser.ProcedureDivisionGivingClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#procedureDivisionGivingClause.
    def exitProcedureDivisionGivingClause(self, ctx:CobolIsuzuParser.ProcedureDivisionGivingClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#procedureDivisionUsingParameter.
    def enterProcedureDivisionUsingParameter(self, ctx:CobolIsuzuParser.ProcedureDivisionUsingParameterContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#procedureDivisionUsingParameter.
    def exitProcedureDivisionUsingParameter(self, ctx:CobolIsuzuParser.ProcedureDivisionUsingParameterContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#procedureDivisionByReferencePhrase.
    def enterProcedureDivisionByReferencePhrase(self, ctx:CobolIsuzuParser.ProcedureDivisionByReferencePhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#procedureDivisionByReferencePhrase.
    def exitProcedureDivisionByReferencePhrase(self, ctx:CobolIsuzuParser.ProcedureDivisionByReferencePhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#procedureDivisionByReference.
    def enterProcedureDivisionByReference(self, ctx:CobolIsuzuParser.ProcedureDivisionByReferenceContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#procedureDivisionByReference.
    def exitProcedureDivisionByReference(self, ctx:CobolIsuzuParser.ProcedureDivisionByReferenceContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#procedureDivisionByValuePhrase.
    def enterProcedureDivisionByValuePhrase(self, ctx:CobolIsuzuParser.ProcedureDivisionByValuePhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#procedureDivisionByValuePhrase.
    def exitProcedureDivisionByValuePhrase(self, ctx:CobolIsuzuParser.ProcedureDivisionByValuePhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#procedureDivisionByValue.
    def enterProcedureDivisionByValue(self, ctx:CobolIsuzuParser.ProcedureDivisionByValueContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#procedureDivisionByValue.
    def exitProcedureDivisionByValue(self, ctx:CobolIsuzuParser.ProcedureDivisionByValueContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#procedureDeclaratives.
    def enterProcedureDeclaratives(self, ctx:CobolIsuzuParser.ProcedureDeclarativesContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#procedureDeclaratives.
    def exitProcedureDeclaratives(self, ctx:CobolIsuzuParser.ProcedureDeclarativesContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#procedureDeclarative.
    def enterProcedureDeclarative(self, ctx:CobolIsuzuParser.ProcedureDeclarativeContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#procedureDeclarative.
    def exitProcedureDeclarative(self, ctx:CobolIsuzuParser.ProcedureDeclarativeContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#procedureSectionHeader.
    def enterProcedureSectionHeader(self, ctx:CobolIsuzuParser.ProcedureSectionHeaderContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#procedureSectionHeader.
    def exitProcedureSectionHeader(self, ctx:CobolIsuzuParser.ProcedureSectionHeaderContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#procedureDivisionBody.
    def enterProcedureDivisionBody(self, ctx:CobolIsuzuParser.ProcedureDivisionBodyContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#procedureDivisionBody.
    def exitProcedureDivisionBody(self, ctx:CobolIsuzuParser.ProcedureDivisionBodyContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#procedureSection.
    def enterProcedureSection(self, ctx:CobolIsuzuParser.ProcedureSectionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#procedureSection.
    def exitProcedureSection(self, ctx:CobolIsuzuParser.ProcedureSectionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#paragraphs.
    def enterParagraphs(self, ctx:CobolIsuzuParser.ParagraphsContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#paragraphs.
    def exitParagraphs(self, ctx:CobolIsuzuParser.ParagraphsContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#paragraph.
    def enterParagraph(self, ctx:CobolIsuzuParser.ParagraphContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#paragraph.
    def exitParagraph(self, ctx:CobolIsuzuParser.ParagraphContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#sentence.
    def enterSentence(self, ctx:CobolIsuzuParser.SentenceContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#sentence.
    def exitSentence(self, ctx:CobolIsuzuParser.SentenceContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#statement.
    def enterStatement(self, ctx:CobolIsuzuParser.StatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#statement.
    def exitStatement(self, ctx:CobolIsuzuParser.StatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#findStatement.
    def enterFindStatement(self, ctx:CobolIsuzuParser.FindStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#findStatement.
    def exitFindStatement(self, ctx:CobolIsuzuParser.FindStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#viaClause.
    def enterViaClause(self, ctx:CobolIsuzuParser.ViaClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#viaClause.
    def exitViaClause(self, ctx:CobolIsuzuParser.ViaClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#findOption.
    def enterFindOption(self, ctx:CobolIsuzuParser.FindOptionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#findOption.
    def exitFindOption(self, ctx:CobolIsuzuParser.FindOptionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#getStatement.
    def enterGetStatement(self, ctx:CobolIsuzuParser.GetStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#getStatement.
    def exitGetStatement(self, ctx:CobolIsuzuParser.GetStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#finishStatement.
    def enterFinishStatement(self, ctx:CobolIsuzuParser.FinishStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#finishStatement.
    def exitFinishStatement(self, ctx:CobolIsuzuParser.FinishStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#eraseStatement.
    def enterEraseStatement(self, ctx:CobolIsuzuParser.EraseStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#eraseStatement.
    def exitEraseStatement(self, ctx:CobolIsuzuParser.EraseStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#storeStatement.
    def enterStoreStatement(self, ctx:CobolIsuzuParser.StoreStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#storeStatement.
    def exitStoreStatement(self, ctx:CobolIsuzuParser.StoreStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#storeSendingArea.
    def enterStoreSendingArea(self, ctx:CobolIsuzuParser.StoreSendingAreaContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#storeSendingArea.
    def exitStoreSendingArea(self, ctx:CobolIsuzuParser.StoreSendingAreaContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#storeToArea.
    def enterStoreToArea(self, ctx:CobolIsuzuParser.StoreToAreaContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#storeToArea.
    def exitStoreToArea(self, ctx:CobolIsuzuParser.StoreToAreaContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#modifyStatement.
    def enterModifyStatement(self, ctx:CobolIsuzuParser.ModifyStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#modifyStatement.
    def exitModifyStatement(self, ctx:CobolIsuzuParser.ModifyStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#readyStatement.
    def enterReadyStatement(self, ctx:CobolIsuzuParser.ReadyStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#readyStatement.
    def exitReadyStatement(self, ctx:CobolIsuzuParser.ReadyStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#transactionEndStatement.
    def enterTransactionEndStatement(self, ctx:CobolIsuzuParser.TransactionEndStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#transactionEndStatement.
    def exitTransactionEndStatement(self, ctx:CobolIsuzuParser.TransactionEndStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#execCicsStatement2.
    def enterExecCicsStatement2(self, ctx:CobolIsuzuParser.ExecCicsStatement2Context):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#execCicsStatement2.
    def exitExecCicsStatement2(self, ctx:CobolIsuzuParser.ExecCicsStatement2Context):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#acceptStatement.
    def enterAcceptStatement(self, ctx:CobolIsuzuParser.AcceptStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#acceptStatement.
    def exitAcceptStatement(self, ctx:CobolIsuzuParser.AcceptStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#acceptFromDateStatement.
    def enterAcceptFromDateStatement(self, ctx:CobolIsuzuParser.AcceptFromDateStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#acceptFromDateStatement.
    def exitAcceptFromDateStatement(self, ctx:CobolIsuzuParser.AcceptFromDateStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#acceptFromMnemonicStatement.
    def enterAcceptFromMnemonicStatement(self, ctx:CobolIsuzuParser.AcceptFromMnemonicStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#acceptFromMnemonicStatement.
    def exitAcceptFromMnemonicStatement(self, ctx:CobolIsuzuParser.AcceptFromMnemonicStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#acceptFromEscapeKeyStatement.
    def enterAcceptFromEscapeKeyStatement(self, ctx:CobolIsuzuParser.AcceptFromEscapeKeyStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#acceptFromEscapeKeyStatement.
    def exitAcceptFromEscapeKeyStatement(self, ctx:CobolIsuzuParser.AcceptFromEscapeKeyStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#acceptMessageCountStatement.
    def enterAcceptMessageCountStatement(self, ctx:CobolIsuzuParser.AcceptMessageCountStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#acceptMessageCountStatement.
    def exitAcceptMessageCountStatement(self, ctx:CobolIsuzuParser.AcceptMessageCountStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#addStatement.
    def enterAddStatement(self, ctx:CobolIsuzuParser.AddStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#addStatement.
    def exitAddStatement(self, ctx:CobolIsuzuParser.AddStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#addToStatement.
    def enterAddToStatement(self, ctx:CobolIsuzuParser.AddToStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#addToStatement.
    def exitAddToStatement(self, ctx:CobolIsuzuParser.AddToStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#addToGivingStatement.
    def enterAddToGivingStatement(self, ctx:CobolIsuzuParser.AddToGivingStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#addToGivingStatement.
    def exitAddToGivingStatement(self, ctx:CobolIsuzuParser.AddToGivingStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#addCorrespondingStatement.
    def enterAddCorrespondingStatement(self, ctx:CobolIsuzuParser.AddCorrespondingStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#addCorrespondingStatement.
    def exitAddCorrespondingStatement(self, ctx:CobolIsuzuParser.AddCorrespondingStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#addFrom.
    def enterAddFrom(self, ctx:CobolIsuzuParser.AddFromContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#addFrom.
    def exitAddFrom(self, ctx:CobolIsuzuParser.AddFromContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#addTo.
    def enterAddTo(self, ctx:CobolIsuzuParser.AddToContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#addTo.
    def exitAddTo(self, ctx:CobolIsuzuParser.AddToContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#addToGiving.
    def enterAddToGiving(self, ctx:CobolIsuzuParser.AddToGivingContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#addToGiving.
    def exitAddToGiving(self, ctx:CobolIsuzuParser.AddToGivingContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#addGiving.
    def enterAddGiving(self, ctx:CobolIsuzuParser.AddGivingContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#addGiving.
    def exitAddGiving(self, ctx:CobolIsuzuParser.AddGivingContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#alteredGoTo.
    def enterAlteredGoTo(self, ctx:CobolIsuzuParser.AlteredGoToContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#alteredGoTo.
    def exitAlteredGoTo(self, ctx:CobolIsuzuParser.AlteredGoToContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#alterStatement.
    def enterAlterStatement(self, ctx:CobolIsuzuParser.AlterStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#alterStatement.
    def exitAlterStatement(self, ctx:CobolIsuzuParser.AlterStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#alterProceedTo.
    def enterAlterProceedTo(self, ctx:CobolIsuzuParser.AlterProceedToContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#alterProceedTo.
    def exitAlterProceedTo(self, ctx:CobolIsuzuParser.AlterProceedToContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#callStatement.
    def enterCallStatement(self, ctx:CobolIsuzuParser.CallStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#callStatement.
    def exitCallStatement(self, ctx:CobolIsuzuParser.CallStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#callUsingPhrase.
    def enterCallUsingPhrase(self, ctx:CobolIsuzuParser.CallUsingPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#callUsingPhrase.
    def exitCallUsingPhrase(self, ctx:CobolIsuzuParser.CallUsingPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#callUsingParameter.
    def enterCallUsingParameter(self, ctx:CobolIsuzuParser.CallUsingParameterContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#callUsingParameter.
    def exitCallUsingParameter(self, ctx:CobolIsuzuParser.CallUsingParameterContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#callByReferencePhrase.
    def enterCallByReferencePhrase(self, ctx:CobolIsuzuParser.CallByReferencePhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#callByReferencePhrase.
    def exitCallByReferencePhrase(self, ctx:CobolIsuzuParser.CallByReferencePhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#callByReference.
    def enterCallByReference(self, ctx:CobolIsuzuParser.CallByReferenceContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#callByReference.
    def exitCallByReference(self, ctx:CobolIsuzuParser.CallByReferenceContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#callByValuePhrase.
    def enterCallByValuePhrase(self, ctx:CobolIsuzuParser.CallByValuePhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#callByValuePhrase.
    def exitCallByValuePhrase(self, ctx:CobolIsuzuParser.CallByValuePhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#callByValue.
    def enterCallByValue(self, ctx:CobolIsuzuParser.CallByValueContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#callByValue.
    def exitCallByValue(self, ctx:CobolIsuzuParser.CallByValueContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#callByContentPhrase.
    def enterCallByContentPhrase(self, ctx:CobolIsuzuParser.CallByContentPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#callByContentPhrase.
    def exitCallByContentPhrase(self, ctx:CobolIsuzuParser.CallByContentPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#callByContent.
    def enterCallByContent(self, ctx:CobolIsuzuParser.CallByContentContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#callByContent.
    def exitCallByContent(self, ctx:CobolIsuzuParser.CallByContentContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#callGivingPhrase.
    def enterCallGivingPhrase(self, ctx:CobolIsuzuParser.CallGivingPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#callGivingPhrase.
    def exitCallGivingPhrase(self, ctx:CobolIsuzuParser.CallGivingPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#callSystem.
    def enterCallSystem(self, ctx:CobolIsuzuParser.CallSystemContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#callSystem.
    def exitCallSystem(self, ctx:CobolIsuzuParser.CallSystemContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#cancelStatement.
    def enterCancelStatement(self, ctx:CobolIsuzuParser.CancelStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#cancelStatement.
    def exitCancelStatement(self, ctx:CobolIsuzuParser.CancelStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#cancelCall.
    def enterCancelCall(self, ctx:CobolIsuzuParser.CancelCallContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#cancelCall.
    def exitCancelCall(self, ctx:CobolIsuzuParser.CancelCallContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#closeStatement.
    def enterCloseStatement(self, ctx:CobolIsuzuParser.CloseStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#closeStatement.
    def exitCloseStatement(self, ctx:CobolIsuzuParser.CloseStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#closePhrase.
    def enterClosePhrase(self, ctx:CobolIsuzuParser.ClosePhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#closePhrase.
    def exitClosePhrase(self, ctx:CobolIsuzuParser.ClosePhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#closeFile.
    def enterCloseFile(self, ctx:CobolIsuzuParser.CloseFileContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#closeFile.
    def exitCloseFile(self, ctx:CobolIsuzuParser.CloseFileContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#closeReelUnitStatement.
    def enterCloseReelUnitStatement(self, ctx:CobolIsuzuParser.CloseReelUnitStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#closeReelUnitStatement.
    def exitCloseReelUnitStatement(self, ctx:CobolIsuzuParser.CloseReelUnitStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#closeRelativeStatement.
    def enterCloseRelativeStatement(self, ctx:CobolIsuzuParser.CloseRelativeStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#closeRelativeStatement.
    def exitCloseRelativeStatement(self, ctx:CobolIsuzuParser.CloseRelativeStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#closePortFileIOStatement.
    def enterClosePortFileIOStatement(self, ctx:CobolIsuzuParser.ClosePortFileIOStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#closePortFileIOStatement.
    def exitClosePortFileIOStatement(self, ctx:CobolIsuzuParser.ClosePortFileIOStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#closePortFileIOUsing.
    def enterClosePortFileIOUsing(self, ctx:CobolIsuzuParser.ClosePortFileIOUsingContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#closePortFileIOUsing.
    def exitClosePortFileIOUsing(self, ctx:CobolIsuzuParser.ClosePortFileIOUsingContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#closePortFileIOUsingCloseDisposition.
    def enterClosePortFileIOUsingCloseDisposition(self, ctx:CobolIsuzuParser.ClosePortFileIOUsingCloseDispositionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#closePortFileIOUsingCloseDisposition.
    def exitClosePortFileIOUsingCloseDisposition(self, ctx:CobolIsuzuParser.ClosePortFileIOUsingCloseDispositionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#closePortFileIOUsingAssociatedData.
    def enterClosePortFileIOUsingAssociatedData(self, ctx:CobolIsuzuParser.ClosePortFileIOUsingAssociatedDataContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#closePortFileIOUsingAssociatedData.
    def exitClosePortFileIOUsingAssociatedData(self, ctx:CobolIsuzuParser.ClosePortFileIOUsingAssociatedDataContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#closePortFileIOUsingAssociatedDataLength.
    def enterClosePortFileIOUsingAssociatedDataLength(self, ctx:CobolIsuzuParser.ClosePortFileIOUsingAssociatedDataLengthContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#closePortFileIOUsingAssociatedDataLength.
    def exitClosePortFileIOUsingAssociatedDataLength(self, ctx:CobolIsuzuParser.ClosePortFileIOUsingAssociatedDataLengthContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#computeStatement.
    def enterComputeStatement(self, ctx:CobolIsuzuParser.ComputeStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#computeStatement.
    def exitComputeStatement(self, ctx:CobolIsuzuParser.ComputeStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#computeStore.
    def enterComputeStore(self, ctx:CobolIsuzuParser.ComputeStoreContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#computeStore.
    def exitComputeStore(self, ctx:CobolIsuzuParser.ComputeStoreContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#continueStatement.
    def enterContinueStatement(self, ctx:CobolIsuzuParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#continueStatement.
    def exitContinueStatement(self, ctx:CobolIsuzuParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#deleteStatement.
    def enterDeleteStatement(self, ctx:CobolIsuzuParser.DeleteStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#deleteStatement.
    def exitDeleteStatement(self, ctx:CobolIsuzuParser.DeleteStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#disableStatement.
    def enterDisableStatement(self, ctx:CobolIsuzuParser.DisableStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#disableStatement.
    def exitDisableStatement(self, ctx:CobolIsuzuParser.DisableStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#displayStatement.
    def enterDisplayStatement(self, ctx:CobolIsuzuParser.DisplayStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#displayStatement.
    def exitDisplayStatement(self, ctx:CobolIsuzuParser.DisplayStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#displayOperand.
    def enterDisplayOperand(self, ctx:CobolIsuzuParser.DisplayOperandContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#displayOperand.
    def exitDisplayOperand(self, ctx:CobolIsuzuParser.DisplayOperandContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#displayAt.
    def enterDisplayAt(self, ctx:CobolIsuzuParser.DisplayAtContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#displayAt.
    def exitDisplayAt(self, ctx:CobolIsuzuParser.DisplayAtContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#displayUpon.
    def enterDisplayUpon(self, ctx:CobolIsuzuParser.DisplayUponContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#displayUpon.
    def exitDisplayUpon(self, ctx:CobolIsuzuParser.DisplayUponContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#displayWith.
    def enterDisplayWith(self, ctx:CobolIsuzuParser.DisplayWithContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#displayWith.
    def exitDisplayWith(self, ctx:CobolIsuzuParser.DisplayWithContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#divideStatement.
    def enterDivideStatement(self, ctx:CobolIsuzuParser.DivideStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#divideStatement.
    def exitDivideStatement(self, ctx:CobolIsuzuParser.DivideStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#divideIntoStatement.
    def enterDivideIntoStatement(self, ctx:CobolIsuzuParser.DivideIntoStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#divideIntoStatement.
    def exitDivideIntoStatement(self, ctx:CobolIsuzuParser.DivideIntoStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#divideIntoGivingStatement.
    def enterDivideIntoGivingStatement(self, ctx:CobolIsuzuParser.DivideIntoGivingStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#divideIntoGivingStatement.
    def exitDivideIntoGivingStatement(self, ctx:CobolIsuzuParser.DivideIntoGivingStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#divideByGivingStatement.
    def enterDivideByGivingStatement(self, ctx:CobolIsuzuParser.DivideByGivingStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#divideByGivingStatement.
    def exitDivideByGivingStatement(self, ctx:CobolIsuzuParser.DivideByGivingStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#divideGivingPhrase.
    def enterDivideGivingPhrase(self, ctx:CobolIsuzuParser.DivideGivingPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#divideGivingPhrase.
    def exitDivideGivingPhrase(self, ctx:CobolIsuzuParser.DivideGivingPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#divideInto.
    def enterDivideInto(self, ctx:CobolIsuzuParser.DivideIntoContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#divideInto.
    def exitDivideInto(self, ctx:CobolIsuzuParser.DivideIntoContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#divideGiving.
    def enterDivideGiving(self, ctx:CobolIsuzuParser.DivideGivingContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#divideGiving.
    def exitDivideGiving(self, ctx:CobolIsuzuParser.DivideGivingContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#divideRemainder.
    def enterDivideRemainder(self, ctx:CobolIsuzuParser.DivideRemainderContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#divideRemainder.
    def exitDivideRemainder(self, ctx:CobolIsuzuParser.DivideRemainderContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#enableStatement.
    def enterEnableStatement(self, ctx:CobolIsuzuParser.EnableStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#enableStatement.
    def exitEnableStatement(self, ctx:CobolIsuzuParser.EnableStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#entryStatement.
    def enterEntryStatement(self, ctx:CobolIsuzuParser.EntryStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#entryStatement.
    def exitEntryStatement(self, ctx:CobolIsuzuParser.EntryStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#evaluateStatement.
    def enterEvaluateStatement(self, ctx:CobolIsuzuParser.EvaluateStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#evaluateStatement.
    def exitEvaluateStatement(self, ctx:CobolIsuzuParser.EvaluateStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#evaluateSelect.
    def enterEvaluateSelect(self, ctx:CobolIsuzuParser.EvaluateSelectContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#evaluateSelect.
    def exitEvaluateSelect(self, ctx:CobolIsuzuParser.EvaluateSelectContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#evaluateAlsoSelect.
    def enterEvaluateAlsoSelect(self, ctx:CobolIsuzuParser.EvaluateAlsoSelectContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#evaluateAlsoSelect.
    def exitEvaluateAlsoSelect(self, ctx:CobolIsuzuParser.EvaluateAlsoSelectContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#evaluateWhenPhrase.
    def enterEvaluateWhenPhrase(self, ctx:CobolIsuzuParser.EvaluateWhenPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#evaluateWhenPhrase.
    def exitEvaluateWhenPhrase(self, ctx:CobolIsuzuParser.EvaluateWhenPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#evaluateWhen.
    def enterEvaluateWhen(self, ctx:CobolIsuzuParser.EvaluateWhenContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#evaluateWhen.
    def exitEvaluateWhen(self, ctx:CobolIsuzuParser.EvaluateWhenContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#evaluateCondition.
    def enterEvaluateCondition(self, ctx:CobolIsuzuParser.EvaluateConditionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#evaluateCondition.
    def exitEvaluateCondition(self, ctx:CobolIsuzuParser.EvaluateConditionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#evaluateThrough.
    def enterEvaluateThrough(self, ctx:CobolIsuzuParser.EvaluateThroughContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#evaluateThrough.
    def exitEvaluateThrough(self, ctx:CobolIsuzuParser.EvaluateThroughContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#evaluateAlsoCondition.
    def enterEvaluateAlsoCondition(self, ctx:CobolIsuzuParser.EvaluateAlsoConditionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#evaluateAlsoCondition.
    def exitEvaluateAlsoCondition(self, ctx:CobolIsuzuParser.EvaluateAlsoConditionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#evaluateWhenOther.
    def enterEvaluateWhenOther(self, ctx:CobolIsuzuParser.EvaluateWhenOtherContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#evaluateWhenOther.
    def exitEvaluateWhenOther(self, ctx:CobolIsuzuParser.EvaluateWhenOtherContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#evaluateValue.
    def enterEvaluateValue(self, ctx:CobolIsuzuParser.EvaluateValueContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#evaluateValue.
    def exitEvaluateValue(self, ctx:CobolIsuzuParser.EvaluateValueContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#execCicsStatement.
    def enterExecCicsStatement(self, ctx:CobolIsuzuParser.ExecCicsStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#execCicsStatement.
    def exitExecCicsStatement(self, ctx:CobolIsuzuParser.ExecCicsStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#execSqlStatement.
    def enterExecSqlStatement(self, ctx:CobolIsuzuParser.ExecSqlStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#execSqlStatement.
    def exitExecSqlStatement(self, ctx:CobolIsuzuParser.ExecSqlStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#execSqlImsStatement.
    def enterExecSqlImsStatement(self, ctx:CobolIsuzuParser.ExecSqlImsStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#execSqlImsStatement.
    def exitExecSqlImsStatement(self, ctx:CobolIsuzuParser.ExecSqlImsStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#exhibitStatement.
    def enterExhibitStatement(self, ctx:CobolIsuzuParser.ExhibitStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#exhibitStatement.
    def exitExhibitStatement(self, ctx:CobolIsuzuParser.ExhibitStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#exhibitOperand.
    def enterExhibitOperand(self, ctx:CobolIsuzuParser.ExhibitOperandContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#exhibitOperand.
    def exitExhibitOperand(self, ctx:CobolIsuzuParser.ExhibitOperandContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#exitStatement.
    def enterExitStatement(self, ctx:CobolIsuzuParser.ExitStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#exitStatement.
    def exitExitStatement(self, ctx:CobolIsuzuParser.ExitStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#generateStatement.
    def enterGenerateStatement(self, ctx:CobolIsuzuParser.GenerateStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#generateStatement.
    def exitGenerateStatement(self, ctx:CobolIsuzuParser.GenerateStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#gobackStatement.
    def enterGobackStatement(self, ctx:CobolIsuzuParser.GobackStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#gobackStatement.
    def exitGobackStatement(self, ctx:CobolIsuzuParser.GobackStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#goToStatement.
    def enterGoToStatement(self, ctx:CobolIsuzuParser.GoToStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#goToStatement.
    def exitGoToStatement(self, ctx:CobolIsuzuParser.GoToStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#goToStatementSimple.
    def enterGoToStatementSimple(self, ctx:CobolIsuzuParser.GoToStatementSimpleContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#goToStatementSimple.
    def exitGoToStatementSimple(self, ctx:CobolIsuzuParser.GoToStatementSimpleContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#goToDependingOnStatement.
    def enterGoToDependingOnStatement(self, ctx:CobolIsuzuParser.GoToDependingOnStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#goToDependingOnStatement.
    def exitGoToDependingOnStatement(self, ctx:CobolIsuzuParser.GoToDependingOnStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#ifStatement.
    def enterIfStatement(self, ctx:CobolIsuzuParser.IfStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#ifStatement.
    def exitIfStatement(self, ctx:CobolIsuzuParser.IfStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#ifThen.
    def enterIfThen(self, ctx:CobolIsuzuParser.IfThenContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#ifThen.
    def exitIfThen(self, ctx:CobolIsuzuParser.IfThenContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#ifElse.
    def enterIfElse(self, ctx:CobolIsuzuParser.IfElseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#ifElse.
    def exitIfElse(self, ctx:CobolIsuzuParser.IfElseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#initializeStatement.
    def enterInitializeStatement(self, ctx:CobolIsuzuParser.InitializeStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#initializeStatement.
    def exitInitializeStatement(self, ctx:CobolIsuzuParser.InitializeStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#initializeReplacingPhrase.
    def enterInitializeReplacingPhrase(self, ctx:CobolIsuzuParser.InitializeReplacingPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#initializeReplacingPhrase.
    def exitInitializeReplacingPhrase(self, ctx:CobolIsuzuParser.InitializeReplacingPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#initializeReplacingBy.
    def enterInitializeReplacingBy(self, ctx:CobolIsuzuParser.InitializeReplacingByContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#initializeReplacingBy.
    def exitInitializeReplacingBy(self, ctx:CobolIsuzuParser.InitializeReplacingByContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#initiateStatement.
    def enterInitiateStatement(self, ctx:CobolIsuzuParser.InitiateStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#initiateStatement.
    def exitInitiateStatement(self, ctx:CobolIsuzuParser.InitiateStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#inspectStatement.
    def enterInspectStatement(self, ctx:CobolIsuzuParser.InspectStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#inspectStatement.
    def exitInspectStatement(self, ctx:CobolIsuzuParser.InspectStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#inspectTallyingPhrase.
    def enterInspectTallyingPhrase(self, ctx:CobolIsuzuParser.InspectTallyingPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#inspectTallyingPhrase.
    def exitInspectTallyingPhrase(self, ctx:CobolIsuzuParser.InspectTallyingPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#inspectReplacingPhrase.
    def enterInspectReplacingPhrase(self, ctx:CobolIsuzuParser.InspectReplacingPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#inspectReplacingPhrase.
    def exitInspectReplacingPhrase(self, ctx:CobolIsuzuParser.InspectReplacingPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#inspectTallyingReplacingPhrase.
    def enterInspectTallyingReplacingPhrase(self, ctx:CobolIsuzuParser.InspectTallyingReplacingPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#inspectTallyingReplacingPhrase.
    def exitInspectTallyingReplacingPhrase(self, ctx:CobolIsuzuParser.InspectTallyingReplacingPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#inspectConvertingPhrase.
    def enterInspectConvertingPhrase(self, ctx:CobolIsuzuParser.InspectConvertingPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#inspectConvertingPhrase.
    def exitInspectConvertingPhrase(self, ctx:CobolIsuzuParser.InspectConvertingPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#inspectFor.
    def enterInspectFor(self, ctx:CobolIsuzuParser.InspectForContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#inspectFor.
    def exitInspectFor(self, ctx:CobolIsuzuParser.InspectForContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#inspectCharacters.
    def enterInspectCharacters(self, ctx:CobolIsuzuParser.InspectCharactersContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#inspectCharacters.
    def exitInspectCharacters(self, ctx:CobolIsuzuParser.InspectCharactersContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#inspectReplacingCharacters.
    def enterInspectReplacingCharacters(self, ctx:CobolIsuzuParser.InspectReplacingCharactersContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#inspectReplacingCharacters.
    def exitInspectReplacingCharacters(self, ctx:CobolIsuzuParser.InspectReplacingCharactersContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#inspectAllLeadings.
    def enterInspectAllLeadings(self, ctx:CobolIsuzuParser.InspectAllLeadingsContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#inspectAllLeadings.
    def exitInspectAllLeadings(self, ctx:CobolIsuzuParser.InspectAllLeadingsContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#inspectReplacingAllLeadings.
    def enterInspectReplacingAllLeadings(self, ctx:CobolIsuzuParser.InspectReplacingAllLeadingsContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#inspectReplacingAllLeadings.
    def exitInspectReplacingAllLeadings(self, ctx:CobolIsuzuParser.InspectReplacingAllLeadingsContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#inspectAllLeading.
    def enterInspectAllLeading(self, ctx:CobolIsuzuParser.InspectAllLeadingContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#inspectAllLeading.
    def exitInspectAllLeading(self, ctx:CobolIsuzuParser.InspectAllLeadingContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#inspectReplacingAllLeading.
    def enterInspectReplacingAllLeading(self, ctx:CobolIsuzuParser.InspectReplacingAllLeadingContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#inspectReplacingAllLeading.
    def exitInspectReplacingAllLeading(self, ctx:CobolIsuzuParser.InspectReplacingAllLeadingContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#inspectBy.
    def enterInspectBy(self, ctx:CobolIsuzuParser.InspectByContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#inspectBy.
    def exitInspectBy(self, ctx:CobolIsuzuParser.InspectByContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#inspectTo.
    def enterInspectTo(self, ctx:CobolIsuzuParser.InspectToContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#inspectTo.
    def exitInspectTo(self, ctx:CobolIsuzuParser.InspectToContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#inspectBeforeAfter.
    def enterInspectBeforeAfter(self, ctx:CobolIsuzuParser.InspectBeforeAfterContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#inspectBeforeAfter.
    def exitInspectBeforeAfter(self, ctx:CobolIsuzuParser.InspectBeforeAfterContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#mergeStatement.
    def enterMergeStatement(self, ctx:CobolIsuzuParser.MergeStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#mergeStatement.
    def exitMergeStatement(self, ctx:CobolIsuzuParser.MergeStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#mergeOnKeyClause.
    def enterMergeOnKeyClause(self, ctx:CobolIsuzuParser.MergeOnKeyClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#mergeOnKeyClause.
    def exitMergeOnKeyClause(self, ctx:CobolIsuzuParser.MergeOnKeyClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#mergeCollatingSequencePhrase.
    def enterMergeCollatingSequencePhrase(self, ctx:CobolIsuzuParser.MergeCollatingSequencePhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#mergeCollatingSequencePhrase.
    def exitMergeCollatingSequencePhrase(self, ctx:CobolIsuzuParser.MergeCollatingSequencePhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#mergeCollatingAlphanumeric.
    def enterMergeCollatingAlphanumeric(self, ctx:CobolIsuzuParser.MergeCollatingAlphanumericContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#mergeCollatingAlphanumeric.
    def exitMergeCollatingAlphanumeric(self, ctx:CobolIsuzuParser.MergeCollatingAlphanumericContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#mergeCollatingNational.
    def enterMergeCollatingNational(self, ctx:CobolIsuzuParser.MergeCollatingNationalContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#mergeCollatingNational.
    def exitMergeCollatingNational(self, ctx:CobolIsuzuParser.MergeCollatingNationalContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#mergeUsing.
    def enterMergeUsing(self, ctx:CobolIsuzuParser.MergeUsingContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#mergeUsing.
    def exitMergeUsing(self, ctx:CobolIsuzuParser.MergeUsingContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#mergeOutputProcedurePhrase.
    def enterMergeOutputProcedurePhrase(self, ctx:CobolIsuzuParser.MergeOutputProcedurePhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#mergeOutputProcedurePhrase.
    def exitMergeOutputProcedurePhrase(self, ctx:CobolIsuzuParser.MergeOutputProcedurePhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#mergeOutputThrough.
    def enterMergeOutputThrough(self, ctx:CobolIsuzuParser.MergeOutputThroughContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#mergeOutputThrough.
    def exitMergeOutputThrough(self, ctx:CobolIsuzuParser.MergeOutputThroughContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#mergeGivingPhrase.
    def enterMergeGivingPhrase(self, ctx:CobolIsuzuParser.MergeGivingPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#mergeGivingPhrase.
    def exitMergeGivingPhrase(self, ctx:CobolIsuzuParser.MergeGivingPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#mergeGiving.
    def enterMergeGiving(self, ctx:CobolIsuzuParser.MergeGivingContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#mergeGiving.
    def exitMergeGiving(self, ctx:CobolIsuzuParser.MergeGivingContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#moveStatement.
    def enterMoveStatement(self, ctx:CobolIsuzuParser.MoveStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#moveStatement.
    def exitMoveStatement(self, ctx:CobolIsuzuParser.MoveStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#moveToStatement.
    def enterMoveToStatement(self, ctx:CobolIsuzuParser.MoveToStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#moveToStatement.
    def exitMoveToStatement(self, ctx:CobolIsuzuParser.MoveToStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#moveToSendingArea.
    def enterMoveToSendingArea(self, ctx:CobolIsuzuParser.MoveToSendingAreaContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#moveToSendingArea.
    def exitMoveToSendingArea(self, ctx:CobolIsuzuParser.MoveToSendingAreaContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#moveCorrespondingToStatement.
    def enterMoveCorrespondingToStatement(self, ctx:CobolIsuzuParser.MoveCorrespondingToStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#moveCorrespondingToStatement.
    def exitMoveCorrespondingToStatement(self, ctx:CobolIsuzuParser.MoveCorrespondingToStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#moveCorrespondingToSendingArea.
    def enterMoveCorrespondingToSendingArea(self, ctx:CobolIsuzuParser.MoveCorrespondingToSendingAreaContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#moveCorrespondingToSendingArea.
    def exitMoveCorrespondingToSendingArea(self, ctx:CobolIsuzuParser.MoveCorrespondingToSendingAreaContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#moveAttributeClause.
    def enterMoveAttributeClause(self, ctx:CobolIsuzuParser.MoveAttributeClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#moveAttributeClause.
    def exitMoveAttributeClause(self, ctx:CobolIsuzuParser.MoveAttributeClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#multiplyStatement.
    def enterMultiplyStatement(self, ctx:CobolIsuzuParser.MultiplyStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#multiplyStatement.
    def exitMultiplyStatement(self, ctx:CobolIsuzuParser.MultiplyStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#multiplyRegular.
    def enterMultiplyRegular(self, ctx:CobolIsuzuParser.MultiplyRegularContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#multiplyRegular.
    def exitMultiplyRegular(self, ctx:CobolIsuzuParser.MultiplyRegularContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#multiplyRegularOperand.
    def enterMultiplyRegularOperand(self, ctx:CobolIsuzuParser.MultiplyRegularOperandContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#multiplyRegularOperand.
    def exitMultiplyRegularOperand(self, ctx:CobolIsuzuParser.MultiplyRegularOperandContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#multiplyGiving.
    def enterMultiplyGiving(self, ctx:CobolIsuzuParser.MultiplyGivingContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#multiplyGiving.
    def exitMultiplyGiving(self, ctx:CobolIsuzuParser.MultiplyGivingContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#multiplyGivingOperand.
    def enterMultiplyGivingOperand(self, ctx:CobolIsuzuParser.MultiplyGivingOperandContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#multiplyGivingOperand.
    def exitMultiplyGivingOperand(self, ctx:CobolIsuzuParser.MultiplyGivingOperandContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#multiplyGivingResult.
    def enterMultiplyGivingResult(self, ctx:CobolIsuzuParser.MultiplyGivingResultContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#multiplyGivingResult.
    def exitMultiplyGivingResult(self, ctx:CobolIsuzuParser.MultiplyGivingResultContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#openStatement.
    def enterOpenStatement(self, ctx:CobolIsuzuParser.OpenStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#openStatement.
    def exitOpenStatement(self, ctx:CobolIsuzuParser.OpenStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#openInputStatement.
    def enterOpenInputStatement(self, ctx:CobolIsuzuParser.OpenInputStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#openInputStatement.
    def exitOpenInputStatement(self, ctx:CobolIsuzuParser.OpenInputStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#openInput.
    def enterOpenInput(self, ctx:CobolIsuzuParser.OpenInputContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#openInput.
    def exitOpenInput(self, ctx:CobolIsuzuParser.OpenInputContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#openOutputStatement.
    def enterOpenOutputStatement(self, ctx:CobolIsuzuParser.OpenOutputStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#openOutputStatement.
    def exitOpenOutputStatement(self, ctx:CobolIsuzuParser.OpenOutputStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#openOutput.
    def enterOpenOutput(self, ctx:CobolIsuzuParser.OpenOutputContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#openOutput.
    def exitOpenOutput(self, ctx:CobolIsuzuParser.OpenOutputContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#openIOStatement.
    def enterOpenIOStatement(self, ctx:CobolIsuzuParser.OpenIOStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#openIOStatement.
    def exitOpenIOStatement(self, ctx:CobolIsuzuParser.OpenIOStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#openExtendStatement.
    def enterOpenExtendStatement(self, ctx:CobolIsuzuParser.OpenExtendStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#openExtendStatement.
    def exitOpenExtendStatement(self, ctx:CobolIsuzuParser.OpenExtendStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#performStatement.
    def enterPerformStatement(self, ctx:CobolIsuzuParser.PerformStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#performStatement.
    def exitPerformStatement(self, ctx:CobolIsuzuParser.PerformStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#performInlineStatement.
    def enterPerformInlineStatement(self, ctx:CobolIsuzuParser.PerformInlineStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#performInlineStatement.
    def exitPerformInlineStatement(self, ctx:CobolIsuzuParser.PerformInlineStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#performProcedureStatement.
    def enterPerformProcedureStatement(self, ctx:CobolIsuzuParser.PerformProcedureStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#performProcedureStatement.
    def exitPerformProcedureStatement(self, ctx:CobolIsuzuParser.PerformProcedureStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#performType.
    def enterPerformType(self, ctx:CobolIsuzuParser.PerformTypeContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#performType.
    def exitPerformType(self, ctx:CobolIsuzuParser.PerformTypeContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#performTimes.
    def enterPerformTimes(self, ctx:CobolIsuzuParser.PerformTimesContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#performTimes.
    def exitPerformTimes(self, ctx:CobolIsuzuParser.PerformTimesContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#performUntil.
    def enterPerformUntil(self, ctx:CobolIsuzuParser.PerformUntilContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#performUntil.
    def exitPerformUntil(self, ctx:CobolIsuzuParser.PerformUntilContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#performVarying.
    def enterPerformVarying(self, ctx:CobolIsuzuParser.PerformVaryingContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#performVarying.
    def exitPerformVarying(self, ctx:CobolIsuzuParser.PerformVaryingContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#performVaryingClause.
    def enterPerformVaryingClause(self, ctx:CobolIsuzuParser.PerformVaryingClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#performVaryingClause.
    def exitPerformVaryingClause(self, ctx:CobolIsuzuParser.PerformVaryingClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#performVaryingPhrase.
    def enterPerformVaryingPhrase(self, ctx:CobolIsuzuParser.PerformVaryingPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#performVaryingPhrase.
    def exitPerformVaryingPhrase(self, ctx:CobolIsuzuParser.PerformVaryingPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#performAfter.
    def enterPerformAfter(self, ctx:CobolIsuzuParser.PerformAfterContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#performAfter.
    def exitPerformAfter(self, ctx:CobolIsuzuParser.PerformAfterContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#performFrom.
    def enterPerformFrom(self, ctx:CobolIsuzuParser.PerformFromContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#performFrom.
    def exitPerformFrom(self, ctx:CobolIsuzuParser.PerformFromContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#performBy.
    def enterPerformBy(self, ctx:CobolIsuzuParser.PerformByContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#performBy.
    def exitPerformBy(self, ctx:CobolIsuzuParser.PerformByContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#performTestClause.
    def enterPerformTestClause(self, ctx:CobolIsuzuParser.PerformTestClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#performTestClause.
    def exitPerformTestClause(self, ctx:CobolIsuzuParser.PerformTestClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#purgeStatement.
    def enterPurgeStatement(self, ctx:CobolIsuzuParser.PurgeStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#purgeStatement.
    def exitPurgeStatement(self, ctx:CobolIsuzuParser.PurgeStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#readStatement.
    def enterReadStatement(self, ctx:CobolIsuzuParser.ReadStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#readStatement.
    def exitReadStatement(self, ctx:CobolIsuzuParser.ReadStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#readInto.
    def enterReadInto(self, ctx:CobolIsuzuParser.ReadIntoContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#readInto.
    def exitReadInto(self, ctx:CobolIsuzuParser.ReadIntoContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#readWith.
    def enterReadWith(self, ctx:CobolIsuzuParser.ReadWithContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#readWith.
    def exitReadWith(self, ctx:CobolIsuzuParser.ReadWithContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#readKey.
    def enterReadKey(self, ctx:CobolIsuzuParser.ReadKeyContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#readKey.
    def exitReadKey(self, ctx:CobolIsuzuParser.ReadKeyContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#receiveStatement.
    def enterReceiveStatement(self, ctx:CobolIsuzuParser.ReceiveStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#receiveStatement.
    def exitReceiveStatement(self, ctx:CobolIsuzuParser.ReceiveStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#receiveFromStatement.
    def enterReceiveFromStatement(self, ctx:CobolIsuzuParser.ReceiveFromStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#receiveFromStatement.
    def exitReceiveFromStatement(self, ctx:CobolIsuzuParser.ReceiveFromStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#receiveFrom.
    def enterReceiveFrom(self, ctx:CobolIsuzuParser.ReceiveFromContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#receiveFrom.
    def exitReceiveFrom(self, ctx:CobolIsuzuParser.ReceiveFromContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#receiveIntoStatement.
    def enterReceiveIntoStatement(self, ctx:CobolIsuzuParser.ReceiveIntoStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#receiveIntoStatement.
    def exitReceiveIntoStatement(self, ctx:CobolIsuzuParser.ReceiveIntoStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#receiveNoData.
    def enterReceiveNoData(self, ctx:CobolIsuzuParser.ReceiveNoDataContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#receiveNoData.
    def exitReceiveNoData(self, ctx:CobolIsuzuParser.ReceiveNoDataContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#receiveWithData.
    def enterReceiveWithData(self, ctx:CobolIsuzuParser.ReceiveWithDataContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#receiveWithData.
    def exitReceiveWithData(self, ctx:CobolIsuzuParser.ReceiveWithDataContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#receiveBefore.
    def enterReceiveBefore(self, ctx:CobolIsuzuParser.ReceiveBeforeContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#receiveBefore.
    def exitReceiveBefore(self, ctx:CobolIsuzuParser.ReceiveBeforeContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#receiveWith.
    def enterReceiveWith(self, ctx:CobolIsuzuParser.ReceiveWithContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#receiveWith.
    def exitReceiveWith(self, ctx:CobolIsuzuParser.ReceiveWithContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#receiveThread.
    def enterReceiveThread(self, ctx:CobolIsuzuParser.ReceiveThreadContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#receiveThread.
    def exitReceiveThread(self, ctx:CobolIsuzuParser.ReceiveThreadContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#receiveSize.
    def enterReceiveSize(self, ctx:CobolIsuzuParser.ReceiveSizeContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#receiveSize.
    def exitReceiveSize(self, ctx:CobolIsuzuParser.ReceiveSizeContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#receiveStatus.
    def enterReceiveStatus(self, ctx:CobolIsuzuParser.ReceiveStatusContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#receiveStatus.
    def exitReceiveStatus(self, ctx:CobolIsuzuParser.ReceiveStatusContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#releaseStatement.
    def enterReleaseStatement(self, ctx:CobolIsuzuParser.ReleaseStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#releaseStatement.
    def exitReleaseStatement(self, ctx:CobolIsuzuParser.ReleaseStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#returnStatement.
    def enterReturnStatement(self, ctx:CobolIsuzuParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#returnStatement.
    def exitReturnStatement(self, ctx:CobolIsuzuParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#returnInto.
    def enterReturnInto(self, ctx:CobolIsuzuParser.ReturnIntoContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#returnInto.
    def exitReturnInto(self, ctx:CobolIsuzuParser.ReturnIntoContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#rewriteStatement.
    def enterRewriteStatement(self, ctx:CobolIsuzuParser.RewriteStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#rewriteStatement.
    def exitRewriteStatement(self, ctx:CobolIsuzuParser.RewriteStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#rewriteFrom.
    def enterRewriteFrom(self, ctx:CobolIsuzuParser.RewriteFromContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#rewriteFrom.
    def exitRewriteFrom(self, ctx:CobolIsuzuParser.RewriteFromContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#searchStatement.
    def enterSearchStatement(self, ctx:CobolIsuzuParser.SearchStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#searchStatement.
    def exitSearchStatement(self, ctx:CobolIsuzuParser.SearchStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#searchVarying.
    def enterSearchVarying(self, ctx:CobolIsuzuParser.SearchVaryingContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#searchVarying.
    def exitSearchVarying(self, ctx:CobolIsuzuParser.SearchVaryingContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#searchWhen.
    def enterSearchWhen(self, ctx:CobolIsuzuParser.SearchWhenContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#searchWhen.
    def exitSearchWhen(self, ctx:CobolIsuzuParser.SearchWhenContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#sendStatement.
    def enterSendStatement(self, ctx:CobolIsuzuParser.SendStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#sendStatement.
    def exitSendStatement(self, ctx:CobolIsuzuParser.SendStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#sendStatementSync.
    def enterSendStatementSync(self, ctx:CobolIsuzuParser.SendStatementSyncContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#sendStatementSync.
    def exitSendStatementSync(self, ctx:CobolIsuzuParser.SendStatementSyncContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#sendStatementAsync.
    def enterSendStatementAsync(self, ctx:CobolIsuzuParser.SendStatementAsyncContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#sendStatementAsync.
    def exitSendStatementAsync(self, ctx:CobolIsuzuParser.SendStatementAsyncContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#sendFromPhrase.
    def enterSendFromPhrase(self, ctx:CobolIsuzuParser.SendFromPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#sendFromPhrase.
    def exitSendFromPhrase(self, ctx:CobolIsuzuParser.SendFromPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#sendWithPhrase.
    def enterSendWithPhrase(self, ctx:CobolIsuzuParser.SendWithPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#sendWithPhrase.
    def exitSendWithPhrase(self, ctx:CobolIsuzuParser.SendWithPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#sendReplacingPhrase.
    def enterSendReplacingPhrase(self, ctx:CobolIsuzuParser.SendReplacingPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#sendReplacingPhrase.
    def exitSendReplacingPhrase(self, ctx:CobolIsuzuParser.SendReplacingPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#sendAdvancingPhrase.
    def enterSendAdvancingPhrase(self, ctx:CobolIsuzuParser.SendAdvancingPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#sendAdvancingPhrase.
    def exitSendAdvancingPhrase(self, ctx:CobolIsuzuParser.SendAdvancingPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#sendAdvancingPage.
    def enterSendAdvancingPage(self, ctx:CobolIsuzuParser.SendAdvancingPageContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#sendAdvancingPage.
    def exitSendAdvancingPage(self, ctx:CobolIsuzuParser.SendAdvancingPageContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#sendAdvancingLines.
    def enterSendAdvancingLines(self, ctx:CobolIsuzuParser.SendAdvancingLinesContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#sendAdvancingLines.
    def exitSendAdvancingLines(self, ctx:CobolIsuzuParser.SendAdvancingLinesContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#sendAdvancingMnemonic.
    def enterSendAdvancingMnemonic(self, ctx:CobolIsuzuParser.SendAdvancingMnemonicContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#sendAdvancingMnemonic.
    def exitSendAdvancingMnemonic(self, ctx:CobolIsuzuParser.SendAdvancingMnemonicContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#setStatement.
    def enterSetStatement(self, ctx:CobolIsuzuParser.SetStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#setStatement.
    def exitSetStatement(self, ctx:CobolIsuzuParser.SetStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#setToStatement.
    def enterSetToStatement(self, ctx:CobolIsuzuParser.SetToStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#setToStatement.
    def exitSetToStatement(self, ctx:CobolIsuzuParser.SetToStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#setUpDownByStatement.
    def enterSetUpDownByStatement(self, ctx:CobolIsuzuParser.SetUpDownByStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#setUpDownByStatement.
    def exitSetUpDownByStatement(self, ctx:CobolIsuzuParser.SetUpDownByStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#setTo.
    def enterSetTo(self, ctx:CobolIsuzuParser.SetToContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#setTo.
    def exitSetTo(self, ctx:CobolIsuzuParser.SetToContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#setToValue.
    def enterSetToValue(self, ctx:CobolIsuzuParser.SetToValueContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#setToValue.
    def exitSetToValue(self, ctx:CobolIsuzuParser.SetToValueContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#setByValue.
    def enterSetByValue(self, ctx:CobolIsuzuParser.SetByValueContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#setByValue.
    def exitSetByValue(self, ctx:CobolIsuzuParser.SetByValueContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#sortStatement.
    def enterSortStatement(self, ctx:CobolIsuzuParser.SortStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#sortStatement.
    def exitSortStatement(self, ctx:CobolIsuzuParser.SortStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#sortOnKeyClause.
    def enterSortOnKeyClause(self, ctx:CobolIsuzuParser.SortOnKeyClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#sortOnKeyClause.
    def exitSortOnKeyClause(self, ctx:CobolIsuzuParser.SortOnKeyClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#sortDuplicatesPhrase.
    def enterSortDuplicatesPhrase(self, ctx:CobolIsuzuParser.SortDuplicatesPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#sortDuplicatesPhrase.
    def exitSortDuplicatesPhrase(self, ctx:CobolIsuzuParser.SortDuplicatesPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#sortCollatingSequencePhrase.
    def enterSortCollatingSequencePhrase(self, ctx:CobolIsuzuParser.SortCollatingSequencePhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#sortCollatingSequencePhrase.
    def exitSortCollatingSequencePhrase(self, ctx:CobolIsuzuParser.SortCollatingSequencePhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#sortCollatingAlphanumeric.
    def enterSortCollatingAlphanumeric(self, ctx:CobolIsuzuParser.SortCollatingAlphanumericContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#sortCollatingAlphanumeric.
    def exitSortCollatingAlphanumeric(self, ctx:CobolIsuzuParser.SortCollatingAlphanumericContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#sortCollatingNational.
    def enterSortCollatingNational(self, ctx:CobolIsuzuParser.SortCollatingNationalContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#sortCollatingNational.
    def exitSortCollatingNational(self, ctx:CobolIsuzuParser.SortCollatingNationalContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#sortInputProcedurePhrase.
    def enterSortInputProcedurePhrase(self, ctx:CobolIsuzuParser.SortInputProcedurePhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#sortInputProcedurePhrase.
    def exitSortInputProcedurePhrase(self, ctx:CobolIsuzuParser.SortInputProcedurePhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#sortInputThrough.
    def enterSortInputThrough(self, ctx:CobolIsuzuParser.SortInputThroughContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#sortInputThrough.
    def exitSortInputThrough(self, ctx:CobolIsuzuParser.SortInputThroughContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#sortUsing.
    def enterSortUsing(self, ctx:CobolIsuzuParser.SortUsingContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#sortUsing.
    def exitSortUsing(self, ctx:CobolIsuzuParser.SortUsingContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#sortOutputProcedurePhrase.
    def enterSortOutputProcedurePhrase(self, ctx:CobolIsuzuParser.SortOutputProcedurePhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#sortOutputProcedurePhrase.
    def exitSortOutputProcedurePhrase(self, ctx:CobolIsuzuParser.SortOutputProcedurePhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#sortOutputThrough.
    def enterSortOutputThrough(self, ctx:CobolIsuzuParser.SortOutputThroughContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#sortOutputThrough.
    def exitSortOutputThrough(self, ctx:CobolIsuzuParser.SortOutputThroughContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#sortGivingPhrase.
    def enterSortGivingPhrase(self, ctx:CobolIsuzuParser.SortGivingPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#sortGivingPhrase.
    def exitSortGivingPhrase(self, ctx:CobolIsuzuParser.SortGivingPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#sortGiving.
    def enterSortGiving(self, ctx:CobolIsuzuParser.SortGivingContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#sortGiving.
    def exitSortGiving(self, ctx:CobolIsuzuParser.SortGivingContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#startStatement.
    def enterStartStatement(self, ctx:CobolIsuzuParser.StartStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#startStatement.
    def exitStartStatement(self, ctx:CobolIsuzuParser.StartStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#startKey.
    def enterStartKey(self, ctx:CobolIsuzuParser.StartKeyContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#startKey.
    def exitStartKey(self, ctx:CobolIsuzuParser.StartKeyContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#stopStatement.
    def enterStopStatement(self, ctx:CobolIsuzuParser.StopStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#stopStatement.
    def exitStopStatement(self, ctx:CobolIsuzuParser.StopStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#stringStatement.
    def enterStringStatement(self, ctx:CobolIsuzuParser.StringStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#stringStatement.
    def exitStringStatement(self, ctx:CobolIsuzuParser.StringStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#stringSendingPhrase.
    def enterStringSendingPhrase(self, ctx:CobolIsuzuParser.StringSendingPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#stringSendingPhrase.
    def exitStringSendingPhrase(self, ctx:CobolIsuzuParser.StringSendingPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#stringSending.
    def enterStringSending(self, ctx:CobolIsuzuParser.StringSendingContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#stringSending.
    def exitStringSending(self, ctx:CobolIsuzuParser.StringSendingContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#stringDelimitedByPhrase.
    def enterStringDelimitedByPhrase(self, ctx:CobolIsuzuParser.StringDelimitedByPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#stringDelimitedByPhrase.
    def exitStringDelimitedByPhrase(self, ctx:CobolIsuzuParser.StringDelimitedByPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#stringForPhrase.
    def enterStringForPhrase(self, ctx:CobolIsuzuParser.StringForPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#stringForPhrase.
    def exitStringForPhrase(self, ctx:CobolIsuzuParser.StringForPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#stringIntoPhrase.
    def enterStringIntoPhrase(self, ctx:CobolIsuzuParser.StringIntoPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#stringIntoPhrase.
    def exitStringIntoPhrase(self, ctx:CobolIsuzuParser.StringIntoPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#stringWithPointerPhrase.
    def enterStringWithPointerPhrase(self, ctx:CobolIsuzuParser.StringWithPointerPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#stringWithPointerPhrase.
    def exitStringWithPointerPhrase(self, ctx:CobolIsuzuParser.StringWithPointerPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#subtractStatement.
    def enterSubtractStatement(self, ctx:CobolIsuzuParser.SubtractStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#subtractStatement.
    def exitSubtractStatement(self, ctx:CobolIsuzuParser.SubtractStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#subtractFromStatement.
    def enterSubtractFromStatement(self, ctx:CobolIsuzuParser.SubtractFromStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#subtractFromStatement.
    def exitSubtractFromStatement(self, ctx:CobolIsuzuParser.SubtractFromStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#subtractFromGivingStatement.
    def enterSubtractFromGivingStatement(self, ctx:CobolIsuzuParser.SubtractFromGivingStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#subtractFromGivingStatement.
    def exitSubtractFromGivingStatement(self, ctx:CobolIsuzuParser.SubtractFromGivingStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#subtractCorrespondingStatement.
    def enterSubtractCorrespondingStatement(self, ctx:CobolIsuzuParser.SubtractCorrespondingStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#subtractCorrespondingStatement.
    def exitSubtractCorrespondingStatement(self, ctx:CobolIsuzuParser.SubtractCorrespondingStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#subtractSubtrahend.
    def enterSubtractSubtrahend(self, ctx:CobolIsuzuParser.SubtractSubtrahendContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#subtractSubtrahend.
    def exitSubtractSubtrahend(self, ctx:CobolIsuzuParser.SubtractSubtrahendContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#subtractMinuend.
    def enterSubtractMinuend(self, ctx:CobolIsuzuParser.SubtractMinuendContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#subtractMinuend.
    def exitSubtractMinuend(self, ctx:CobolIsuzuParser.SubtractMinuendContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#subtractMinuendGiving.
    def enterSubtractMinuendGiving(self, ctx:CobolIsuzuParser.SubtractMinuendGivingContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#subtractMinuendGiving.
    def exitSubtractMinuendGiving(self, ctx:CobolIsuzuParser.SubtractMinuendGivingContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#subtractGiving.
    def enterSubtractGiving(self, ctx:CobolIsuzuParser.SubtractGivingContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#subtractGiving.
    def exitSubtractGiving(self, ctx:CobolIsuzuParser.SubtractGivingContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#subtractMinuendCorresponding.
    def enterSubtractMinuendCorresponding(self, ctx:CobolIsuzuParser.SubtractMinuendCorrespondingContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#subtractMinuendCorresponding.
    def exitSubtractMinuendCorresponding(self, ctx:CobolIsuzuParser.SubtractMinuendCorrespondingContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#transactionStatement.
    def enterTransactionStatement(self, ctx:CobolIsuzuParser.TransactionStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#transactionStatement.
    def exitTransactionStatement(self, ctx:CobolIsuzuParser.TransactionStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#transactionStart.
    def enterTransactionStart(self, ctx:CobolIsuzuParser.TransactionStartContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#transactionStart.
    def exitTransactionStart(self, ctx:CobolIsuzuParser.TransactionStartContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#transactionBody.
    def enterTransactionBody(self, ctx:CobolIsuzuParser.TransactionBodyContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#transactionBody.
    def exitTransactionBody(self, ctx:CobolIsuzuParser.TransactionBodyContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#transactionEnd.
    def enterTransactionEnd(self, ctx:CobolIsuzuParser.TransactionEndContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#transactionEnd.
    def exitTransactionEnd(self, ctx:CobolIsuzuParser.TransactionEndContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#transactionCancelStatement.
    def enterTransactionCancelStatement(self, ctx:CobolIsuzuParser.TransactionCancelStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#transactionCancelStatement.
    def exitTransactionCancelStatement(self, ctx:CobolIsuzuParser.TransactionCancelStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#terminateStatement.
    def enterTerminateStatement(self, ctx:CobolIsuzuParser.TerminateStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#terminateStatement.
    def exitTerminateStatement(self, ctx:CobolIsuzuParser.TerminateStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#unstringStatement.
    def enterUnstringStatement(self, ctx:CobolIsuzuParser.UnstringStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#unstringStatement.
    def exitUnstringStatement(self, ctx:CobolIsuzuParser.UnstringStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#unstringSendingPhrase.
    def enterUnstringSendingPhrase(self, ctx:CobolIsuzuParser.UnstringSendingPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#unstringSendingPhrase.
    def exitUnstringSendingPhrase(self, ctx:CobolIsuzuParser.UnstringSendingPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#unstringDelimitedByPhrase.
    def enterUnstringDelimitedByPhrase(self, ctx:CobolIsuzuParser.UnstringDelimitedByPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#unstringDelimitedByPhrase.
    def exitUnstringDelimitedByPhrase(self, ctx:CobolIsuzuParser.UnstringDelimitedByPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#unstringOrAllPhrase.
    def enterUnstringOrAllPhrase(self, ctx:CobolIsuzuParser.UnstringOrAllPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#unstringOrAllPhrase.
    def exitUnstringOrAllPhrase(self, ctx:CobolIsuzuParser.UnstringOrAllPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#unstringIntoPhrase.
    def enterUnstringIntoPhrase(self, ctx:CobolIsuzuParser.UnstringIntoPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#unstringIntoPhrase.
    def exitUnstringIntoPhrase(self, ctx:CobolIsuzuParser.UnstringIntoPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#unstringInto.
    def enterUnstringInto(self, ctx:CobolIsuzuParser.UnstringIntoContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#unstringInto.
    def exitUnstringInto(self, ctx:CobolIsuzuParser.UnstringIntoContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#unstringDelimiterIn.
    def enterUnstringDelimiterIn(self, ctx:CobolIsuzuParser.UnstringDelimiterInContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#unstringDelimiterIn.
    def exitUnstringDelimiterIn(self, ctx:CobolIsuzuParser.UnstringDelimiterInContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#unstringCountIn.
    def enterUnstringCountIn(self, ctx:CobolIsuzuParser.UnstringCountInContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#unstringCountIn.
    def exitUnstringCountIn(self, ctx:CobolIsuzuParser.UnstringCountInContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#unstringWithPointerPhrase.
    def enterUnstringWithPointerPhrase(self, ctx:CobolIsuzuParser.UnstringWithPointerPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#unstringWithPointerPhrase.
    def exitUnstringWithPointerPhrase(self, ctx:CobolIsuzuParser.UnstringWithPointerPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#unstringTallyingPhrase.
    def enterUnstringTallyingPhrase(self, ctx:CobolIsuzuParser.UnstringTallyingPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#unstringTallyingPhrase.
    def exitUnstringTallyingPhrase(self, ctx:CobolIsuzuParser.UnstringTallyingPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#useStatement.
    def enterUseStatement(self, ctx:CobolIsuzuParser.UseStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#useStatement.
    def exitUseStatement(self, ctx:CobolIsuzuParser.UseStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#useFor.
    def enterUseFor(self, ctx:CobolIsuzuParser.UseForContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#useFor.
    def exitUseFor(self, ctx:CobolIsuzuParser.UseForContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#useAfterClause.
    def enterUseAfterClause(self, ctx:CobolIsuzuParser.UseAfterClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#useAfterClause.
    def exitUseAfterClause(self, ctx:CobolIsuzuParser.UseAfterClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#useAfterOn.
    def enterUseAfterOn(self, ctx:CobolIsuzuParser.UseAfterOnContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#useAfterOn.
    def exitUseAfterOn(self, ctx:CobolIsuzuParser.UseAfterOnContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#useDebugClause.
    def enterUseDebugClause(self, ctx:CobolIsuzuParser.UseDebugClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#useDebugClause.
    def exitUseDebugClause(self, ctx:CobolIsuzuParser.UseDebugClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#useDebugOn.
    def enterUseDebugOn(self, ctx:CobolIsuzuParser.UseDebugOnContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#useDebugOn.
    def exitUseDebugOn(self, ctx:CobolIsuzuParser.UseDebugOnContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#useDeadLock.
    def enterUseDeadLock(self, ctx:CobolIsuzuParser.UseDeadLockContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#useDeadLock.
    def exitUseDeadLock(self, ctx:CobolIsuzuParser.UseDeadLockContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#writeStatement.
    def enterWriteStatement(self, ctx:CobolIsuzuParser.WriteStatementContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#writeStatement.
    def exitWriteStatement(self, ctx:CobolIsuzuParser.WriteStatementContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#writeFromPhrase.
    def enterWriteFromPhrase(self, ctx:CobolIsuzuParser.WriteFromPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#writeFromPhrase.
    def exitWriteFromPhrase(self, ctx:CobolIsuzuParser.WriteFromPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#writeAdvancingPhrase.
    def enterWriteAdvancingPhrase(self, ctx:CobolIsuzuParser.WriteAdvancingPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#writeAdvancingPhrase.
    def exitWriteAdvancingPhrase(self, ctx:CobolIsuzuParser.WriteAdvancingPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#writeAdvancingPage.
    def enterWriteAdvancingPage(self, ctx:CobolIsuzuParser.WriteAdvancingPageContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#writeAdvancingPage.
    def exitWriteAdvancingPage(self, ctx:CobolIsuzuParser.WriteAdvancingPageContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#writeAdvancingLines.
    def enterWriteAdvancingLines(self, ctx:CobolIsuzuParser.WriteAdvancingLinesContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#writeAdvancingLines.
    def exitWriteAdvancingLines(self, ctx:CobolIsuzuParser.WriteAdvancingLinesContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#writeAdvancingMnemonic.
    def enterWriteAdvancingMnemonic(self, ctx:CobolIsuzuParser.WriteAdvancingMnemonicContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#writeAdvancingMnemonic.
    def exitWriteAdvancingMnemonic(self, ctx:CobolIsuzuParser.WriteAdvancingMnemonicContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#writeAtEndOfPagePhrase.
    def enterWriteAtEndOfPagePhrase(self, ctx:CobolIsuzuParser.WriteAtEndOfPagePhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#writeAtEndOfPagePhrase.
    def exitWriteAtEndOfPagePhrase(self, ctx:CobolIsuzuParser.WriteAtEndOfPagePhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#writeNotAtEndOfPagePhrase.
    def enterWriteNotAtEndOfPagePhrase(self, ctx:CobolIsuzuParser.WriteNotAtEndOfPagePhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#writeNotAtEndOfPagePhrase.
    def exitWriteNotAtEndOfPagePhrase(self, ctx:CobolIsuzuParser.WriteNotAtEndOfPagePhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#atEndPhrase.
    def enterAtEndPhrase(self, ctx:CobolIsuzuParser.AtEndPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#atEndPhrase.
    def exitAtEndPhrase(self, ctx:CobolIsuzuParser.AtEndPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#notAtEndPhrase.
    def enterNotAtEndPhrase(self, ctx:CobolIsuzuParser.NotAtEndPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#notAtEndPhrase.
    def exitNotAtEndPhrase(self, ctx:CobolIsuzuParser.NotAtEndPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#invalidKeyPhrase.
    def enterInvalidKeyPhrase(self, ctx:CobolIsuzuParser.InvalidKeyPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#invalidKeyPhrase.
    def exitInvalidKeyPhrase(self, ctx:CobolIsuzuParser.InvalidKeyPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#notInvalidKeyPhrase.
    def enterNotInvalidKeyPhrase(self, ctx:CobolIsuzuParser.NotInvalidKeyPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#notInvalidKeyPhrase.
    def exitNotInvalidKeyPhrase(self, ctx:CobolIsuzuParser.NotInvalidKeyPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#onOverflowPhrase.
    def enterOnOverflowPhrase(self, ctx:CobolIsuzuParser.OnOverflowPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#onOverflowPhrase.
    def exitOnOverflowPhrase(self, ctx:CobolIsuzuParser.OnOverflowPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#notOnOverflowPhrase.
    def enterNotOnOverflowPhrase(self, ctx:CobolIsuzuParser.NotOnOverflowPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#notOnOverflowPhrase.
    def exitNotOnOverflowPhrase(self, ctx:CobolIsuzuParser.NotOnOverflowPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#onSizeErrorPhrase.
    def enterOnSizeErrorPhrase(self, ctx:CobolIsuzuParser.OnSizeErrorPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#onSizeErrorPhrase.
    def exitOnSizeErrorPhrase(self, ctx:CobolIsuzuParser.OnSizeErrorPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#notOnSizeErrorPhrase.
    def enterNotOnSizeErrorPhrase(self, ctx:CobolIsuzuParser.NotOnSizeErrorPhraseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#notOnSizeErrorPhrase.
    def exitNotOnSizeErrorPhrase(self, ctx:CobolIsuzuParser.NotOnSizeErrorPhraseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#onExceptionClause.
    def enterOnExceptionClause(self, ctx:CobolIsuzuParser.OnExceptionClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#onExceptionClause.
    def exitOnExceptionClause(self, ctx:CobolIsuzuParser.OnExceptionClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#notOnExceptionClause.
    def enterNotOnExceptionClause(self, ctx:CobolIsuzuParser.NotOnExceptionClauseContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#notOnExceptionClause.
    def exitNotOnExceptionClause(self, ctx:CobolIsuzuParser.NotOnExceptionClauseContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#arithmeticExpression.
    def enterArithmeticExpression(self, ctx:CobolIsuzuParser.ArithmeticExpressionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#arithmeticExpression.
    def exitArithmeticExpression(self, ctx:CobolIsuzuParser.ArithmeticExpressionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#plusMinus.
    def enterPlusMinus(self, ctx:CobolIsuzuParser.PlusMinusContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#plusMinus.
    def exitPlusMinus(self, ctx:CobolIsuzuParser.PlusMinusContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#multDivs.
    def enterMultDivs(self, ctx:CobolIsuzuParser.MultDivsContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#multDivs.
    def exitMultDivs(self, ctx:CobolIsuzuParser.MultDivsContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#multDiv.
    def enterMultDiv(self, ctx:CobolIsuzuParser.MultDivContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#multDiv.
    def exitMultDiv(self, ctx:CobolIsuzuParser.MultDivContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#powers.
    def enterPowers(self, ctx:CobolIsuzuParser.PowersContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#powers.
    def exitPowers(self, ctx:CobolIsuzuParser.PowersContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#power.
    def enterPower(self, ctx:CobolIsuzuParser.PowerContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#power.
    def exitPower(self, ctx:CobolIsuzuParser.PowerContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#basis.
    def enterBasis(self, ctx:CobolIsuzuParser.BasisContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#basis.
    def exitBasis(self, ctx:CobolIsuzuParser.BasisContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#condition.
    def enterCondition(self, ctx:CobolIsuzuParser.ConditionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#condition.
    def exitCondition(self, ctx:CobolIsuzuParser.ConditionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#andOrCondition.
    def enterAndOrCondition(self, ctx:CobolIsuzuParser.AndOrConditionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#andOrCondition.
    def exitAndOrCondition(self, ctx:CobolIsuzuParser.AndOrConditionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#combinableCondition.
    def enterCombinableCondition(self, ctx:CobolIsuzuParser.CombinableConditionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#combinableCondition.
    def exitCombinableCondition(self, ctx:CobolIsuzuParser.CombinableConditionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#simpleCondition.
    def enterSimpleCondition(self, ctx:CobolIsuzuParser.SimpleConditionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#simpleCondition.
    def exitSimpleCondition(self, ctx:CobolIsuzuParser.SimpleConditionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#classCondition.
    def enterClassCondition(self, ctx:CobolIsuzuParser.ClassConditionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#classCondition.
    def exitClassCondition(self, ctx:CobolIsuzuParser.ClassConditionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#conditionNameReference.
    def enterConditionNameReference(self, ctx:CobolIsuzuParser.ConditionNameReferenceContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#conditionNameReference.
    def exitConditionNameReference(self, ctx:CobolIsuzuParser.ConditionNameReferenceContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#conditionNameSubscriptReference.
    def enterConditionNameSubscriptReference(self, ctx:CobolIsuzuParser.ConditionNameSubscriptReferenceContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#conditionNameSubscriptReference.
    def exitConditionNameSubscriptReference(self, ctx:CobolIsuzuParser.ConditionNameSubscriptReferenceContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#relationCondition.
    def enterRelationCondition(self, ctx:CobolIsuzuParser.RelationConditionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#relationCondition.
    def exitRelationCondition(self, ctx:CobolIsuzuParser.RelationConditionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#relationSignCondition.
    def enterRelationSignCondition(self, ctx:CobolIsuzuParser.RelationSignConditionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#relationSignCondition.
    def exitRelationSignCondition(self, ctx:CobolIsuzuParser.RelationSignConditionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#relationArithmeticComparison.
    def enterRelationArithmeticComparison(self, ctx:CobolIsuzuParser.RelationArithmeticComparisonContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#relationArithmeticComparison.
    def exitRelationArithmeticComparison(self, ctx:CobolIsuzuParser.RelationArithmeticComparisonContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#relationCombinedComparison.
    def enterRelationCombinedComparison(self, ctx:CobolIsuzuParser.RelationCombinedComparisonContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#relationCombinedComparison.
    def exitRelationCombinedComparison(self, ctx:CobolIsuzuParser.RelationCombinedComparisonContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#relationCombinedCondition.
    def enterRelationCombinedCondition(self, ctx:CobolIsuzuParser.RelationCombinedConditionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#relationCombinedCondition.
    def exitRelationCombinedCondition(self, ctx:CobolIsuzuParser.RelationCombinedConditionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#relationalOperator.
    def enterRelationalOperator(self, ctx:CobolIsuzuParser.RelationalOperatorContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#relationalOperator.
    def exitRelationalOperator(self, ctx:CobolIsuzuParser.RelationalOperatorContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#abbreviation.
    def enterAbbreviation(self, ctx:CobolIsuzuParser.AbbreviationContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#abbreviation.
    def exitAbbreviation(self, ctx:CobolIsuzuParser.AbbreviationContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#identifier.
    def enterIdentifier(self, ctx:CobolIsuzuParser.IdentifierContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#identifier.
    def exitIdentifier(self, ctx:CobolIsuzuParser.IdentifierContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#tableCall.
    def enterTableCall(self, ctx:CobolIsuzuParser.TableCallContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#tableCall.
    def exitTableCall(self, ctx:CobolIsuzuParser.TableCallContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#functionCall.
    def enterFunctionCall(self, ctx:CobolIsuzuParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#functionCall.
    def exitFunctionCall(self, ctx:CobolIsuzuParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#referenceModifier.
    def enterReferenceModifier(self, ctx:CobolIsuzuParser.ReferenceModifierContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#referenceModifier.
    def exitReferenceModifier(self, ctx:CobolIsuzuParser.ReferenceModifierContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#characterPosition.
    def enterCharacterPosition(self, ctx:CobolIsuzuParser.CharacterPositionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#characterPosition.
    def exitCharacterPosition(self, ctx:CobolIsuzuParser.CharacterPositionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#length.
    def enterLength(self, ctx:CobolIsuzuParser.LengthContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#length.
    def exitLength(self, ctx:CobolIsuzuParser.LengthContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#subscript_.
    def enterSubscript_(self, ctx:CobolIsuzuParser.Subscript_Context):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#subscript_.
    def exitSubscript_(self, ctx:CobolIsuzuParser.Subscript_Context):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#argument.
    def enterArgument(self, ctx:CobolIsuzuParser.ArgumentContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#argument.
    def exitArgument(self, ctx:CobolIsuzuParser.ArgumentContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#qualifiedDataName.
    def enterQualifiedDataName(self, ctx:CobolIsuzuParser.QualifiedDataNameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#qualifiedDataName.
    def exitQualifiedDataName(self, ctx:CobolIsuzuParser.QualifiedDataNameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#qualifiedDataNameFormat1.
    def enterQualifiedDataNameFormat1(self, ctx:CobolIsuzuParser.QualifiedDataNameFormat1Context):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#qualifiedDataNameFormat1.
    def exitQualifiedDataNameFormat1(self, ctx:CobolIsuzuParser.QualifiedDataNameFormat1Context):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#qualifiedDataNameFormat2.
    def enterQualifiedDataNameFormat2(self, ctx:CobolIsuzuParser.QualifiedDataNameFormat2Context):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#qualifiedDataNameFormat2.
    def exitQualifiedDataNameFormat2(self, ctx:CobolIsuzuParser.QualifiedDataNameFormat2Context):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#qualifiedDataNameFormat3.
    def enterQualifiedDataNameFormat3(self, ctx:CobolIsuzuParser.QualifiedDataNameFormat3Context):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#qualifiedDataNameFormat3.
    def exitQualifiedDataNameFormat3(self, ctx:CobolIsuzuParser.QualifiedDataNameFormat3Context):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#qualifiedDataNameFormat4.
    def enterQualifiedDataNameFormat4(self, ctx:CobolIsuzuParser.QualifiedDataNameFormat4Context):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#qualifiedDataNameFormat4.
    def exitQualifiedDataNameFormat4(self, ctx:CobolIsuzuParser.QualifiedDataNameFormat4Context):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#qualifiedInData.
    def enterQualifiedInData(self, ctx:CobolIsuzuParser.QualifiedInDataContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#qualifiedInData.
    def exitQualifiedInData(self, ctx:CobolIsuzuParser.QualifiedInDataContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#inData.
    def enterInData(self, ctx:CobolIsuzuParser.InDataContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#inData.
    def exitInData(self, ctx:CobolIsuzuParser.InDataContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#inFile.
    def enterInFile(self, ctx:CobolIsuzuParser.InFileContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#inFile.
    def exitInFile(self, ctx:CobolIsuzuParser.InFileContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#inMnemonic.
    def enterInMnemonic(self, ctx:CobolIsuzuParser.InMnemonicContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#inMnemonic.
    def exitInMnemonic(self, ctx:CobolIsuzuParser.InMnemonicContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#inSection.
    def enterInSection(self, ctx:CobolIsuzuParser.InSectionContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#inSection.
    def exitInSection(self, ctx:CobolIsuzuParser.InSectionContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#inLibrary.
    def enterInLibrary(self, ctx:CobolIsuzuParser.InLibraryContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#inLibrary.
    def exitInLibrary(self, ctx:CobolIsuzuParser.InLibraryContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#inTable.
    def enterInTable(self, ctx:CobolIsuzuParser.InTableContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#inTable.
    def exitInTable(self, ctx:CobolIsuzuParser.InTableContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#alphabetName.
    def enterAlphabetName(self, ctx:CobolIsuzuParser.AlphabetNameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#alphabetName.
    def exitAlphabetName(self, ctx:CobolIsuzuParser.AlphabetNameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#assignmentName.
    def enterAssignmentName(self, ctx:CobolIsuzuParser.AssignmentNameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#assignmentName.
    def exitAssignmentName(self, ctx:CobolIsuzuParser.AssignmentNameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#basisName.
    def enterBasisName(self, ctx:CobolIsuzuParser.BasisNameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#basisName.
    def exitBasisName(self, ctx:CobolIsuzuParser.BasisNameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#cdName.
    def enterCdName(self, ctx:CobolIsuzuParser.CdNameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#cdName.
    def exitCdName(self, ctx:CobolIsuzuParser.CdNameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#className.
    def enterClassName(self, ctx:CobolIsuzuParser.ClassNameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#className.
    def exitClassName(self, ctx:CobolIsuzuParser.ClassNameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#computerName.
    def enterComputerName(self, ctx:CobolIsuzuParser.ComputerNameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#computerName.
    def exitComputerName(self, ctx:CobolIsuzuParser.ComputerNameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#conditionName.
    def enterConditionName(self, ctx:CobolIsuzuParser.ConditionNameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#conditionName.
    def exitConditionName(self, ctx:CobolIsuzuParser.ConditionNameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataName.
    def enterDataName(self, ctx:CobolIsuzuParser.DataNameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataName.
    def exitDataName(self, ctx:CobolIsuzuParser.DataNameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#dataDescName.
    def enterDataDescName(self, ctx:CobolIsuzuParser.DataDescNameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#dataDescName.
    def exitDataDescName(self, ctx:CobolIsuzuParser.DataDescNameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#environmentName.
    def enterEnvironmentName(self, ctx:CobolIsuzuParser.EnvironmentNameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#environmentName.
    def exitEnvironmentName(self, ctx:CobolIsuzuParser.EnvironmentNameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#fileName.
    def enterFileName(self, ctx:CobolIsuzuParser.FileNameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#fileName.
    def exitFileName(self, ctx:CobolIsuzuParser.FileNameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#functionName.
    def enterFunctionName(self, ctx:CobolIsuzuParser.FunctionNameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#functionName.
    def exitFunctionName(self, ctx:CobolIsuzuParser.FunctionNameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#indexName.
    def enterIndexName(self, ctx:CobolIsuzuParser.IndexNameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#indexName.
    def exitIndexName(self, ctx:CobolIsuzuParser.IndexNameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#languageName.
    def enterLanguageName(self, ctx:CobolIsuzuParser.LanguageNameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#languageName.
    def exitLanguageName(self, ctx:CobolIsuzuParser.LanguageNameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#libraryName.
    def enterLibraryName(self, ctx:CobolIsuzuParser.LibraryNameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#libraryName.
    def exitLibraryName(self, ctx:CobolIsuzuParser.LibraryNameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#localName.
    def enterLocalName(self, ctx:CobolIsuzuParser.LocalNameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#localName.
    def exitLocalName(self, ctx:CobolIsuzuParser.LocalNameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#mnemonicName.
    def enterMnemonicName(self, ctx:CobolIsuzuParser.MnemonicNameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#mnemonicName.
    def exitMnemonicName(self, ctx:CobolIsuzuParser.MnemonicNameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#paragraphName.
    def enterParagraphName(self, ctx:CobolIsuzuParser.ParagraphNameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#paragraphName.
    def exitParagraphName(self, ctx:CobolIsuzuParser.ParagraphNameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#procedureName.
    def enterProcedureName(self, ctx:CobolIsuzuParser.ProcedureNameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#procedureName.
    def exitProcedureName(self, ctx:CobolIsuzuParser.ProcedureNameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#programName.
    def enterProgramName(self, ctx:CobolIsuzuParser.ProgramNameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#programName.
    def exitProgramName(self, ctx:CobolIsuzuParser.ProgramNameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#recordName.
    def enterRecordName(self, ctx:CobolIsuzuParser.RecordNameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#recordName.
    def exitRecordName(self, ctx:CobolIsuzuParser.RecordNameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#reportName.
    def enterReportName(self, ctx:CobolIsuzuParser.ReportNameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#reportName.
    def exitReportName(self, ctx:CobolIsuzuParser.ReportNameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#routineName.
    def enterRoutineName(self, ctx:CobolIsuzuParser.RoutineNameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#routineName.
    def exitRoutineName(self, ctx:CobolIsuzuParser.RoutineNameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#screenName.
    def enterScreenName(self, ctx:CobolIsuzuParser.ScreenNameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#screenName.
    def exitScreenName(self, ctx:CobolIsuzuParser.ScreenNameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#schemaName.
    def enterSchemaName(self, ctx:CobolIsuzuParser.SchemaNameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#schemaName.
    def exitSchemaName(self, ctx:CobolIsuzuParser.SchemaNameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#sectionName.
    def enterSectionName(self, ctx:CobolIsuzuParser.SectionNameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#sectionName.
    def exitSectionName(self, ctx:CobolIsuzuParser.SectionNameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#systemName.
    def enterSystemName(self, ctx:CobolIsuzuParser.SystemNameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#systemName.
    def exitSystemName(self, ctx:CobolIsuzuParser.SystemNameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#symbolicCharacter.
    def enterSymbolicCharacter(self, ctx:CobolIsuzuParser.SymbolicCharacterContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#symbolicCharacter.
    def exitSymbolicCharacter(self, ctx:CobolIsuzuParser.SymbolicCharacterContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#textName.
    def enterTextName(self, ctx:CobolIsuzuParser.TextNameContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#textName.
    def exitTextName(self, ctx:CobolIsuzuParser.TextNameContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:CobolIsuzuParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:CobolIsuzuParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#numericLiteral.
    def enterNumericLiteral(self, ctx:CobolIsuzuParser.NumericLiteralContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#numericLiteral.
    def exitNumericLiteral(self, ctx:CobolIsuzuParser.NumericLiteralContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#integerLiteral.
    def enterIntegerLiteral(self, ctx:CobolIsuzuParser.IntegerLiteralContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#integerLiteral.
    def exitIntegerLiteral(self, ctx:CobolIsuzuParser.IntegerLiteralContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#cicsDfhRespLiteral.
    def enterCicsDfhRespLiteral(self, ctx:CobolIsuzuParser.CicsDfhRespLiteralContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#cicsDfhRespLiteral.
    def exitCicsDfhRespLiteral(self, ctx:CobolIsuzuParser.CicsDfhRespLiteralContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#cicsDfhValueLiteral.
    def enterCicsDfhValueLiteral(self, ctx:CobolIsuzuParser.CicsDfhValueLiteralContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#cicsDfhValueLiteral.
    def exitCicsDfhValueLiteral(self, ctx:CobolIsuzuParser.CicsDfhValueLiteralContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#figurativeConstant.
    def enterFigurativeConstant(self, ctx:CobolIsuzuParser.FigurativeConstantContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#figurativeConstant.
    def exitFigurativeConstant(self, ctx:CobolIsuzuParser.FigurativeConstantContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#specialRegister.
    def enterSpecialRegister(self, ctx:CobolIsuzuParser.SpecialRegisterContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#specialRegister.
    def exitSpecialRegister(self, ctx:CobolIsuzuParser.SpecialRegisterContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#commentEntry.
    def enterCommentEntry(self, ctx:CobolIsuzuParser.CommentEntryContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#commentEntry.
    def exitCommentEntry(self, ctx:CobolIsuzuParser.CommentEntryContext):
        pass


    # Enter a parse tree produced by CobolIsuzuParser#charDataKeyword.
    def enterCharDataKeyword(self, ctx:CobolIsuzuParser.CharDataKeywordContext):
        pass

    # Exit a parse tree produced by CobolIsuzuParser#charDataKeyword.
    def exitCharDataKeyword(self, ctx:CobolIsuzuParser.CharDataKeywordContext):
        pass



del CobolIsuzuParser