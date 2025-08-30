// Generated from /Users/nguyen/Work/mainframe-services/app/tasks/grammar/dnp/DNP.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link DNPParser}.
 */
public interface DNPListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link DNPParser#startRule}.
	 * @param ctx the parse tree
	 */
	void enterStartRule(DNPParser.StartRuleContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#startRule}.
	 * @param ctx the parse tree
	 */
	void exitStartRule(DNPParser.StartRuleContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#compilationUnit}.
	 * @param ctx the parse tree
	 */
	void enterCompilationUnit(DNPParser.CompilationUnitContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#compilationUnit}.
	 * @param ctx the parse tree
	 */
	void exitCompilationUnit(DNPParser.CompilationUnitContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#programUnit}.
	 * @param ctx the parse tree
	 */
	void enterProgramUnit(DNPParser.ProgramUnitContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#programUnit}.
	 * @param ctx the parse tree
	 */
	void exitProgramUnit(DNPParser.ProgramUnitContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#endProgramStatement}.
	 * @param ctx the parse tree
	 */
	void enterEndProgramStatement(DNPParser.EndProgramStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#endProgramStatement}.
	 * @param ctx the parse tree
	 */
	void exitEndProgramStatement(DNPParser.EndProgramStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#identificationDivision}.
	 * @param ctx the parse tree
	 */
	void enterIdentificationDivision(DNPParser.IdentificationDivisionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#identificationDivision}.
	 * @param ctx the parse tree
	 */
	void exitIdentificationDivision(DNPParser.IdentificationDivisionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#identificationDivisionBody}.
	 * @param ctx the parse tree
	 */
	void enterIdentificationDivisionBody(DNPParser.IdentificationDivisionBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#identificationDivisionBody}.
	 * @param ctx the parse tree
	 */
	void exitIdentificationDivisionBody(DNPParser.IdentificationDivisionBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#programIdParagraph}.
	 * @param ctx the parse tree
	 */
	void enterProgramIdParagraph(DNPParser.ProgramIdParagraphContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#programIdParagraph}.
	 * @param ctx the parse tree
	 */
	void exitProgramIdParagraph(DNPParser.ProgramIdParagraphContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#author_name}.
	 * @param ctx the parse tree
	 */
	void enterAuthor_name(DNPParser.Author_nameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#author_name}.
	 * @param ctx the parse tree
	 */
	void exitAuthor_name(DNPParser.Author_nameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#authorParagraph}.
	 * @param ctx the parse tree
	 */
	void enterAuthorParagraph(DNPParser.AuthorParagraphContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#authorParagraph}.
	 * @param ctx the parse tree
	 */
	void exitAuthorParagraph(DNPParser.AuthorParagraphContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#installationParagraph}.
	 * @param ctx the parse tree
	 */
	void enterInstallationParagraph(DNPParser.InstallationParagraphContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#installationParagraph}.
	 * @param ctx the parse tree
	 */
	void exitInstallationParagraph(DNPParser.InstallationParagraphContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dateWrittenParagraph}.
	 * @param ctx the parse tree
	 */
	void enterDateWrittenParagraph(DNPParser.DateWrittenParagraphContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dateWrittenParagraph}.
	 * @param ctx the parse tree
	 */
	void exitDateWrittenParagraph(DNPParser.DateWrittenParagraphContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dateCompiledParagraph}.
	 * @param ctx the parse tree
	 */
	void enterDateCompiledParagraph(DNPParser.DateCompiledParagraphContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dateCompiledParagraph}.
	 * @param ctx the parse tree
	 */
	void exitDateCompiledParagraph(DNPParser.DateCompiledParagraphContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#securityParagraph}.
	 * @param ctx the parse tree
	 */
	void enterSecurityParagraph(DNPParser.SecurityParagraphContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#securityParagraph}.
	 * @param ctx the parse tree
	 */
	void exitSecurityParagraph(DNPParser.SecurityParagraphContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#remarksParagraph}.
	 * @param ctx the parse tree
	 */
	void enterRemarksParagraph(DNPParser.RemarksParagraphContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#remarksParagraph}.
	 * @param ctx the parse tree
	 */
	void exitRemarksParagraph(DNPParser.RemarksParagraphContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#environmentDivision}.
	 * @param ctx the parse tree
	 */
	void enterEnvironmentDivision(DNPParser.EnvironmentDivisionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#environmentDivision}.
	 * @param ctx the parse tree
	 */
	void exitEnvironmentDivision(DNPParser.EnvironmentDivisionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#environmentDivisionBody}.
	 * @param ctx the parse tree
	 */
	void enterEnvironmentDivisionBody(DNPParser.EnvironmentDivisionBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#environmentDivisionBody}.
	 * @param ctx the parse tree
	 */
	void exitEnvironmentDivisionBody(DNPParser.EnvironmentDivisionBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#configurationSection}.
	 * @param ctx the parse tree
	 */
	void enterConfigurationSection(DNPParser.ConfigurationSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#configurationSection}.
	 * @param ctx the parse tree
	 */
	void exitConfigurationSection(DNPParser.ConfigurationSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#configurationSectionParagraph}.
	 * @param ctx the parse tree
	 */
	void enterConfigurationSectionParagraph(DNPParser.ConfigurationSectionParagraphContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#configurationSectionParagraph}.
	 * @param ctx the parse tree
	 */
	void exitConfigurationSectionParagraph(DNPParser.ConfigurationSectionParagraphContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#sourceComputerParagraph}.
	 * @param ctx the parse tree
	 */
	void enterSourceComputerParagraph(DNPParser.SourceComputerParagraphContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#sourceComputerParagraph}.
	 * @param ctx the parse tree
	 */
	void exitSourceComputerParagraph(DNPParser.SourceComputerParagraphContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#objectComputerParagraph}.
	 * @param ctx the parse tree
	 */
	void enterObjectComputerParagraph(DNPParser.ObjectComputerParagraphContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#objectComputerParagraph}.
	 * @param ctx the parse tree
	 */
	void exitObjectComputerParagraph(DNPParser.ObjectComputerParagraphContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#objectComputerClause}.
	 * @param ctx the parse tree
	 */
	void enterObjectComputerClause(DNPParser.ObjectComputerClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#objectComputerClause}.
	 * @param ctx the parse tree
	 */
	void exitObjectComputerClause(DNPParser.ObjectComputerClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#memorySizeClause}.
	 * @param ctx the parse tree
	 */
	void enterMemorySizeClause(DNPParser.MemorySizeClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#memorySizeClause}.
	 * @param ctx the parse tree
	 */
	void exitMemorySizeClause(DNPParser.MemorySizeClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#diskSizeClause}.
	 * @param ctx the parse tree
	 */
	void enterDiskSizeClause(DNPParser.DiskSizeClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#diskSizeClause}.
	 * @param ctx the parse tree
	 */
	void exitDiskSizeClause(DNPParser.DiskSizeClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#collatingSequenceClause}.
	 * @param ctx the parse tree
	 */
	void enterCollatingSequenceClause(DNPParser.CollatingSequenceClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#collatingSequenceClause}.
	 * @param ctx the parse tree
	 */
	void exitCollatingSequenceClause(DNPParser.CollatingSequenceClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#collatingSequenceClauseAlphanumeric}.
	 * @param ctx the parse tree
	 */
	void enterCollatingSequenceClauseAlphanumeric(DNPParser.CollatingSequenceClauseAlphanumericContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#collatingSequenceClauseAlphanumeric}.
	 * @param ctx the parse tree
	 */
	void exitCollatingSequenceClauseAlphanumeric(DNPParser.CollatingSequenceClauseAlphanumericContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#collatingSequenceClauseNational}.
	 * @param ctx the parse tree
	 */
	void enterCollatingSequenceClauseNational(DNPParser.CollatingSequenceClauseNationalContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#collatingSequenceClauseNational}.
	 * @param ctx the parse tree
	 */
	void exitCollatingSequenceClauseNational(DNPParser.CollatingSequenceClauseNationalContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#segmentLimitClause}.
	 * @param ctx the parse tree
	 */
	void enterSegmentLimitClause(DNPParser.SegmentLimitClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#segmentLimitClause}.
	 * @param ctx the parse tree
	 */
	void exitSegmentLimitClause(DNPParser.SegmentLimitClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#characterSetClause}.
	 * @param ctx the parse tree
	 */
	void enterCharacterSetClause(DNPParser.CharacterSetClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#characterSetClause}.
	 * @param ctx the parse tree
	 */
	void exitCharacterSetClause(DNPParser.CharacterSetClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#specialNamesParagraph}.
	 * @param ctx the parse tree
	 */
	void enterSpecialNamesParagraph(DNPParser.SpecialNamesParagraphContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#specialNamesParagraph}.
	 * @param ctx the parse tree
	 */
	void exitSpecialNamesParagraph(DNPParser.SpecialNamesParagraphContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#specialNameClause}.
	 * @param ctx the parse tree
	 */
	void enterSpecialNameClause(DNPParser.SpecialNameClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#specialNameClause}.
	 * @param ctx the parse tree
	 */
	void exitSpecialNameClause(DNPParser.SpecialNameClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#alphabetClause}.
	 * @param ctx the parse tree
	 */
	void enterAlphabetClause(DNPParser.AlphabetClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#alphabetClause}.
	 * @param ctx the parse tree
	 */
	void exitAlphabetClause(DNPParser.AlphabetClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#alphabetClauseFormat1}.
	 * @param ctx the parse tree
	 */
	void enterAlphabetClauseFormat1(DNPParser.AlphabetClauseFormat1Context ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#alphabetClauseFormat1}.
	 * @param ctx the parse tree
	 */
	void exitAlphabetClauseFormat1(DNPParser.AlphabetClauseFormat1Context ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#alphabetLiterals}.
	 * @param ctx the parse tree
	 */
	void enterAlphabetLiterals(DNPParser.AlphabetLiteralsContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#alphabetLiterals}.
	 * @param ctx the parse tree
	 */
	void exitAlphabetLiterals(DNPParser.AlphabetLiteralsContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#alphabetThrough}.
	 * @param ctx the parse tree
	 */
	void enterAlphabetThrough(DNPParser.AlphabetThroughContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#alphabetThrough}.
	 * @param ctx the parse tree
	 */
	void exitAlphabetThrough(DNPParser.AlphabetThroughContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#alphabetAlso}.
	 * @param ctx the parse tree
	 */
	void enterAlphabetAlso(DNPParser.AlphabetAlsoContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#alphabetAlso}.
	 * @param ctx the parse tree
	 */
	void exitAlphabetAlso(DNPParser.AlphabetAlsoContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#alphabetClauseFormat2}.
	 * @param ctx the parse tree
	 */
	void enterAlphabetClauseFormat2(DNPParser.AlphabetClauseFormat2Context ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#alphabetClauseFormat2}.
	 * @param ctx the parse tree
	 */
	void exitAlphabetClauseFormat2(DNPParser.AlphabetClauseFormat2Context ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#channelClause}.
	 * @param ctx the parse tree
	 */
	void enterChannelClause(DNPParser.ChannelClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#channelClause}.
	 * @param ctx the parse tree
	 */
	void exitChannelClause(DNPParser.ChannelClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#classClause}.
	 * @param ctx the parse tree
	 */
	void enterClassClause(DNPParser.ClassClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#classClause}.
	 * @param ctx the parse tree
	 */
	void exitClassClause(DNPParser.ClassClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#classClauseThrough}.
	 * @param ctx the parse tree
	 */
	void enterClassClauseThrough(DNPParser.ClassClauseThroughContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#classClauseThrough}.
	 * @param ctx the parse tree
	 */
	void exitClassClauseThrough(DNPParser.ClassClauseThroughContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#classClauseFrom}.
	 * @param ctx the parse tree
	 */
	void enterClassClauseFrom(DNPParser.ClassClauseFromContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#classClauseFrom}.
	 * @param ctx the parse tree
	 */
	void exitClassClauseFrom(DNPParser.ClassClauseFromContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#classClauseTo}.
	 * @param ctx the parse tree
	 */
	void enterClassClauseTo(DNPParser.ClassClauseToContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#classClauseTo}.
	 * @param ctx the parse tree
	 */
	void exitClassClauseTo(DNPParser.ClassClauseToContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#currencySignClause}.
	 * @param ctx the parse tree
	 */
	void enterCurrencySignClause(DNPParser.CurrencySignClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#currencySignClause}.
	 * @param ctx the parse tree
	 */
	void exitCurrencySignClause(DNPParser.CurrencySignClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#decimalPointClause}.
	 * @param ctx the parse tree
	 */
	void enterDecimalPointClause(DNPParser.DecimalPointClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#decimalPointClause}.
	 * @param ctx the parse tree
	 */
	void exitDecimalPointClause(DNPParser.DecimalPointClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#defaultComputationalSignClause}.
	 * @param ctx the parse tree
	 */
	void enterDefaultComputationalSignClause(DNPParser.DefaultComputationalSignClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#defaultComputationalSignClause}.
	 * @param ctx the parse tree
	 */
	void exitDefaultComputationalSignClause(DNPParser.DefaultComputationalSignClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#defaultDisplaySignClause}.
	 * @param ctx the parse tree
	 */
	void enterDefaultDisplaySignClause(DNPParser.DefaultDisplaySignClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#defaultDisplaySignClause}.
	 * @param ctx the parse tree
	 */
	void exitDefaultDisplaySignClause(DNPParser.DefaultDisplaySignClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#environmentSwitchNameClause}.
	 * @param ctx the parse tree
	 */
	void enterEnvironmentSwitchNameClause(DNPParser.EnvironmentSwitchNameClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#environmentSwitchNameClause}.
	 * @param ctx the parse tree
	 */
	void exitEnvironmentSwitchNameClause(DNPParser.EnvironmentSwitchNameClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#environmentSwitchNameSpecialNamesStatusPhrase}.
	 * @param ctx the parse tree
	 */
	void enterEnvironmentSwitchNameSpecialNamesStatusPhrase(DNPParser.EnvironmentSwitchNameSpecialNamesStatusPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#environmentSwitchNameSpecialNamesStatusPhrase}.
	 * @param ctx the parse tree
	 */
	void exitEnvironmentSwitchNameSpecialNamesStatusPhrase(DNPParser.EnvironmentSwitchNameSpecialNamesStatusPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#odtClause}.
	 * @param ctx the parse tree
	 */
	void enterOdtClause(DNPParser.OdtClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#odtClause}.
	 * @param ctx the parse tree
	 */
	void exitOdtClause(DNPParser.OdtClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reserveNetworkClause}.
	 * @param ctx the parse tree
	 */
	void enterReserveNetworkClause(DNPParser.ReserveNetworkClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reserveNetworkClause}.
	 * @param ctx the parse tree
	 */
	void exitReserveNetworkClause(DNPParser.ReserveNetworkClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#symbolicCharactersClause}.
	 * @param ctx the parse tree
	 */
	void enterSymbolicCharactersClause(DNPParser.SymbolicCharactersClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#symbolicCharactersClause}.
	 * @param ctx the parse tree
	 */
	void exitSymbolicCharactersClause(DNPParser.SymbolicCharactersClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#symbolicCharacters}.
	 * @param ctx the parse tree
	 */
	void enterSymbolicCharacters(DNPParser.SymbolicCharactersContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#symbolicCharacters}.
	 * @param ctx the parse tree
	 */
	void exitSymbolicCharacters(DNPParser.SymbolicCharactersContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#inputOutputSection}.
	 * @param ctx the parse tree
	 */
	void enterInputOutputSection(DNPParser.InputOutputSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#inputOutputSection}.
	 * @param ctx the parse tree
	 */
	void exitInputOutputSection(DNPParser.InputOutputSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#inputOutputSectionParagraph}.
	 * @param ctx the parse tree
	 */
	void enterInputOutputSectionParagraph(DNPParser.InputOutputSectionParagraphContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#inputOutputSectionParagraph}.
	 * @param ctx the parse tree
	 */
	void exitInputOutputSectionParagraph(DNPParser.InputOutputSectionParagraphContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#fileControlParagraph}.
	 * @param ctx the parse tree
	 */
	void enterFileControlParagraph(DNPParser.FileControlParagraphContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#fileControlParagraph}.
	 * @param ctx the parse tree
	 */
	void exitFileControlParagraph(DNPParser.FileControlParagraphContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#fileControlEntry}.
	 * @param ctx the parse tree
	 */
	void enterFileControlEntry(DNPParser.FileControlEntryContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#fileControlEntry}.
	 * @param ctx the parse tree
	 */
	void exitFileControlEntry(DNPParser.FileControlEntryContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#selectClause}.
	 * @param ctx the parse tree
	 */
	void enterSelectClause(DNPParser.SelectClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#selectClause}.
	 * @param ctx the parse tree
	 */
	void exitSelectClause(DNPParser.SelectClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#fileControlClause}.
	 * @param ctx the parse tree
	 */
	void enterFileControlClause(DNPParser.FileControlClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#fileControlClause}.
	 * @param ctx the parse tree
	 */
	void exitFileControlClause(DNPParser.FileControlClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#assignClause}.
	 * @param ctx the parse tree
	 */
	void enterAssignClause(DNPParser.AssignClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#assignClause}.
	 * @param ctx the parse tree
	 */
	void exitAssignClause(DNPParser.AssignClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reserveClause}.
	 * @param ctx the parse tree
	 */
	void enterReserveClause(DNPParser.ReserveClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reserveClause}.
	 * @param ctx the parse tree
	 */
	void exitReserveClause(DNPParser.ReserveClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#organizationClause}.
	 * @param ctx the parse tree
	 */
	void enterOrganizationClause(DNPParser.OrganizationClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#organizationClause}.
	 * @param ctx the parse tree
	 */
	void exitOrganizationClause(DNPParser.OrganizationClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#paddingCharacterClause}.
	 * @param ctx the parse tree
	 */
	void enterPaddingCharacterClause(DNPParser.PaddingCharacterClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#paddingCharacterClause}.
	 * @param ctx the parse tree
	 */
	void exitPaddingCharacterClause(DNPParser.PaddingCharacterClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#recordDelimiterClause}.
	 * @param ctx the parse tree
	 */
	void enterRecordDelimiterClause(DNPParser.RecordDelimiterClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#recordDelimiterClause}.
	 * @param ctx the parse tree
	 */
	void exitRecordDelimiterClause(DNPParser.RecordDelimiterClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#accessModeClause}.
	 * @param ctx the parse tree
	 */
	void enterAccessModeClause(DNPParser.AccessModeClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#accessModeClause}.
	 * @param ctx the parse tree
	 */
	void exitAccessModeClause(DNPParser.AccessModeClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#recordKeyClause}.
	 * @param ctx the parse tree
	 */
	void enterRecordKeyClause(DNPParser.RecordKeyClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#recordKeyClause}.
	 * @param ctx the parse tree
	 */
	void exitRecordKeyClause(DNPParser.RecordKeyClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#alternateRecordKeyClause}.
	 * @param ctx the parse tree
	 */
	void enterAlternateRecordKeyClause(DNPParser.AlternateRecordKeyClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#alternateRecordKeyClause}.
	 * @param ctx the parse tree
	 */
	void exitAlternateRecordKeyClause(DNPParser.AlternateRecordKeyClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#passwordClause}.
	 * @param ctx the parse tree
	 */
	void enterPasswordClause(DNPParser.PasswordClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#passwordClause}.
	 * @param ctx the parse tree
	 */
	void exitPasswordClause(DNPParser.PasswordClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#fileStatusClause}.
	 * @param ctx the parse tree
	 */
	void enterFileStatusClause(DNPParser.FileStatusClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#fileStatusClause}.
	 * @param ctx the parse tree
	 */
	void exitFileStatusClause(DNPParser.FileStatusClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#relativeKeyClause}.
	 * @param ctx the parse tree
	 */
	void enterRelativeKeyClause(DNPParser.RelativeKeyClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#relativeKeyClause}.
	 * @param ctx the parse tree
	 */
	void exitRelativeKeyClause(DNPParser.RelativeKeyClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#ioControlParagraph}.
	 * @param ctx the parse tree
	 */
	void enterIoControlParagraph(DNPParser.IoControlParagraphContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#ioControlParagraph}.
	 * @param ctx the parse tree
	 */
	void exitIoControlParagraph(DNPParser.IoControlParagraphContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#ioControlClause}.
	 * @param ctx the parse tree
	 */
	void enterIoControlClause(DNPParser.IoControlClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#ioControlClause}.
	 * @param ctx the parse tree
	 */
	void exitIoControlClause(DNPParser.IoControlClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#rerunClause}.
	 * @param ctx the parse tree
	 */
	void enterRerunClause(DNPParser.RerunClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#rerunClause}.
	 * @param ctx the parse tree
	 */
	void exitRerunClause(DNPParser.RerunClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#rerunEveryRecords}.
	 * @param ctx the parse tree
	 */
	void enterRerunEveryRecords(DNPParser.RerunEveryRecordsContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#rerunEveryRecords}.
	 * @param ctx the parse tree
	 */
	void exitRerunEveryRecords(DNPParser.RerunEveryRecordsContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#rerunEveryOf}.
	 * @param ctx the parse tree
	 */
	void enterRerunEveryOf(DNPParser.RerunEveryOfContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#rerunEveryOf}.
	 * @param ctx the parse tree
	 */
	void exitRerunEveryOf(DNPParser.RerunEveryOfContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#rerunEveryClock}.
	 * @param ctx the parse tree
	 */
	void enterRerunEveryClock(DNPParser.RerunEveryClockContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#rerunEveryClock}.
	 * @param ctx the parse tree
	 */
	void exitRerunEveryClock(DNPParser.RerunEveryClockContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#sameClause}.
	 * @param ctx the parse tree
	 */
	void enterSameClause(DNPParser.SameClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#sameClause}.
	 * @param ctx the parse tree
	 */
	void exitSameClause(DNPParser.SameClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#multipleFileClause}.
	 * @param ctx the parse tree
	 */
	void enterMultipleFileClause(DNPParser.MultipleFileClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#multipleFileClause}.
	 * @param ctx the parse tree
	 */
	void exitMultipleFileClause(DNPParser.MultipleFileClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#multipleFilePosition}.
	 * @param ctx the parse tree
	 */
	void enterMultipleFilePosition(DNPParser.MultipleFilePositionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#multipleFilePosition}.
	 * @param ctx the parse tree
	 */
	void exitMultipleFilePosition(DNPParser.MultipleFilePositionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#commitmentControlClause}.
	 * @param ctx the parse tree
	 */
	void enterCommitmentControlClause(DNPParser.CommitmentControlClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#commitmentControlClause}.
	 * @param ctx the parse tree
	 */
	void exitCommitmentControlClause(DNPParser.CommitmentControlClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataDivision}.
	 * @param ctx the parse tree
	 */
	void enterDataDivision(DNPParser.DataDivisionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataDivision}.
	 * @param ctx the parse tree
	 */
	void exitDataDivision(DNPParser.DataDivisionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataDivisionSection}.
	 * @param ctx the parse tree
	 */
	void enterDataDivisionSection(DNPParser.DataDivisionSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataDivisionSection}.
	 * @param ctx the parse tree
	 */
	void exitDataDivisionSection(DNPParser.DataDivisionSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#fileSection}.
	 * @param ctx the parse tree
	 */
	void enterFileSection(DNPParser.FileSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#fileSection}.
	 * @param ctx the parse tree
	 */
	void exitFileSection(DNPParser.FileSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#fileDescriptionEntry}.
	 * @param ctx the parse tree
	 */
	void enterFileDescriptionEntry(DNPParser.FileDescriptionEntryContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#fileDescriptionEntry}.
	 * @param ctx the parse tree
	 */
	void exitFileDescriptionEntry(DNPParser.FileDescriptionEntryContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#fileDescriptionEntryClause}.
	 * @param ctx the parse tree
	 */
	void enterFileDescriptionEntryClause(DNPParser.FileDescriptionEntryClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#fileDescriptionEntryClause}.
	 * @param ctx the parse tree
	 */
	void exitFileDescriptionEntryClause(DNPParser.FileDescriptionEntryClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#externalClause}.
	 * @param ctx the parse tree
	 */
	void enterExternalClause(DNPParser.ExternalClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#externalClause}.
	 * @param ctx the parse tree
	 */
	void exitExternalClause(DNPParser.ExternalClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#globalClause}.
	 * @param ctx the parse tree
	 */
	void enterGlobalClause(DNPParser.GlobalClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#globalClause}.
	 * @param ctx the parse tree
	 */
	void exitGlobalClause(DNPParser.GlobalClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#blockContainsClause}.
	 * @param ctx the parse tree
	 */
	void enterBlockContainsClause(DNPParser.BlockContainsClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#blockContainsClause}.
	 * @param ctx the parse tree
	 */
	void exitBlockContainsClause(DNPParser.BlockContainsClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#blockContainsTo}.
	 * @param ctx the parse tree
	 */
	void enterBlockContainsTo(DNPParser.BlockContainsToContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#blockContainsTo}.
	 * @param ctx the parse tree
	 */
	void exitBlockContainsTo(DNPParser.BlockContainsToContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#recordContainsClause}.
	 * @param ctx the parse tree
	 */
	void enterRecordContainsClause(DNPParser.RecordContainsClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#recordContainsClause}.
	 * @param ctx the parse tree
	 */
	void exitRecordContainsClause(DNPParser.RecordContainsClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#recordContainsClauseFormat1}.
	 * @param ctx the parse tree
	 */
	void enterRecordContainsClauseFormat1(DNPParser.RecordContainsClauseFormat1Context ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#recordContainsClauseFormat1}.
	 * @param ctx the parse tree
	 */
	void exitRecordContainsClauseFormat1(DNPParser.RecordContainsClauseFormat1Context ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#recordContainsClauseFormat2}.
	 * @param ctx the parse tree
	 */
	void enterRecordContainsClauseFormat2(DNPParser.RecordContainsClauseFormat2Context ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#recordContainsClauseFormat2}.
	 * @param ctx the parse tree
	 */
	void exitRecordContainsClauseFormat2(DNPParser.RecordContainsClauseFormat2Context ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#recordContainsClauseFormat3}.
	 * @param ctx the parse tree
	 */
	void enterRecordContainsClauseFormat3(DNPParser.RecordContainsClauseFormat3Context ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#recordContainsClauseFormat3}.
	 * @param ctx the parse tree
	 */
	void exitRecordContainsClauseFormat3(DNPParser.RecordContainsClauseFormat3Context ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#recordContainsTo}.
	 * @param ctx the parse tree
	 */
	void enterRecordContainsTo(DNPParser.RecordContainsToContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#recordContainsTo}.
	 * @param ctx the parse tree
	 */
	void exitRecordContainsTo(DNPParser.RecordContainsToContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#labelRecordsClause}.
	 * @param ctx the parse tree
	 */
	void enterLabelRecordsClause(DNPParser.LabelRecordsClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#labelRecordsClause}.
	 * @param ctx the parse tree
	 */
	void exitLabelRecordsClause(DNPParser.LabelRecordsClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#valueOfClause}.
	 * @param ctx the parse tree
	 */
	void enterValueOfClause(DNPParser.ValueOfClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#valueOfClause}.
	 * @param ctx the parse tree
	 */
	void exitValueOfClause(DNPParser.ValueOfClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#valuePair}.
	 * @param ctx the parse tree
	 */
	void enterValuePair(DNPParser.ValuePairContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#valuePair}.
	 * @param ctx the parse tree
	 */
	void exitValuePair(DNPParser.ValuePairContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataRecordsClause}.
	 * @param ctx the parse tree
	 */
	void enterDataRecordsClause(DNPParser.DataRecordsClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataRecordsClause}.
	 * @param ctx the parse tree
	 */
	void exitDataRecordsClause(DNPParser.DataRecordsClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#linageClause}.
	 * @param ctx the parse tree
	 */
	void enterLinageClause(DNPParser.LinageClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#linageClause}.
	 * @param ctx the parse tree
	 */
	void exitLinageClause(DNPParser.LinageClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#linageAt}.
	 * @param ctx the parse tree
	 */
	void enterLinageAt(DNPParser.LinageAtContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#linageAt}.
	 * @param ctx the parse tree
	 */
	void exitLinageAt(DNPParser.LinageAtContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#linageFootingAt}.
	 * @param ctx the parse tree
	 */
	void enterLinageFootingAt(DNPParser.LinageFootingAtContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#linageFootingAt}.
	 * @param ctx the parse tree
	 */
	void exitLinageFootingAt(DNPParser.LinageFootingAtContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#linageLinesAtTop}.
	 * @param ctx the parse tree
	 */
	void enterLinageLinesAtTop(DNPParser.LinageLinesAtTopContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#linageLinesAtTop}.
	 * @param ctx the parse tree
	 */
	void exitLinageLinesAtTop(DNPParser.LinageLinesAtTopContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#linageLinesAtBottom}.
	 * @param ctx the parse tree
	 */
	void enterLinageLinesAtBottom(DNPParser.LinageLinesAtBottomContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#linageLinesAtBottom}.
	 * @param ctx the parse tree
	 */
	void exitLinageLinesAtBottom(DNPParser.LinageLinesAtBottomContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#recordingModeClause}.
	 * @param ctx the parse tree
	 */
	void enterRecordingModeClause(DNPParser.RecordingModeClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#recordingModeClause}.
	 * @param ctx the parse tree
	 */
	void exitRecordingModeClause(DNPParser.RecordingModeClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#modeStatement}.
	 * @param ctx the parse tree
	 */
	void enterModeStatement(DNPParser.ModeStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#modeStatement}.
	 * @param ctx the parse tree
	 */
	void exitModeStatement(DNPParser.ModeStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#codeSetClause}.
	 * @param ctx the parse tree
	 */
	void enterCodeSetClause(DNPParser.CodeSetClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#codeSetClause}.
	 * @param ctx the parse tree
	 */
	void exitCodeSetClause(DNPParser.CodeSetClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportClause}.
	 * @param ctx the parse tree
	 */
	void enterReportClause(DNPParser.ReportClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportClause}.
	 * @param ctx the parse tree
	 */
	void exitReportClause(DNPParser.ReportClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataBaseSection}.
	 * @param ctx the parse tree
	 */
	void enterDataBaseSection(DNPParser.DataBaseSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataBaseSection}.
	 * @param ctx the parse tree
	 */
	void exitDataBaseSection(DNPParser.DataBaseSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataBaseSectionEntry}.
	 * @param ctx the parse tree
	 */
	void enterDataBaseSectionEntry(DNPParser.DataBaseSectionEntryContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataBaseSectionEntry}.
	 * @param ctx the parse tree
	 */
	void exitDataBaseSectionEntry(DNPParser.DataBaseSectionEntryContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataBaseDeclare}.
	 * @param ctx the parse tree
	 */
	void enterDataBaseDeclare(DNPParser.DataBaseDeclareContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataBaseDeclare}.
	 * @param ctx the parse tree
	 */
	void exitDataBaseDeclare(DNPParser.DataBaseDeclareContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataBaseDatasetDeclare}.
	 * @param ctx the parse tree
	 */
	void enterDataBaseDatasetDeclare(DNPParser.DataBaseDatasetDeclareContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataBaseDatasetDeclare}.
	 * @param ctx the parse tree
	 */
	void exitDataBaseDatasetDeclare(DNPParser.DataBaseDatasetDeclareContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#invokeClause}.
	 * @param ctx the parse tree
	 */
	void enterInvokeClause(DNPParser.InvokeClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#invokeClause}.
	 * @param ctx the parse tree
	 */
	void exitInvokeClause(DNPParser.InvokeClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#usingClause}.
	 * @param ctx the parse tree
	 */
	void enterUsingClause(DNPParser.UsingClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#usingClause}.
	 * @param ctx the parse tree
	 */
	void exitUsingClause(DNPParser.UsingClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#workingStorageSection}.
	 * @param ctx the parse tree
	 */
	void enterWorkingStorageSection(DNPParser.WorkingStorageSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#workingStorageSection}.
	 * @param ctx the parse tree
	 */
	void exitWorkingStorageSection(DNPParser.WorkingStorageSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#linkageSection}.
	 * @param ctx the parse tree
	 */
	void enterLinkageSection(DNPParser.LinkageSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#linkageSection}.
	 * @param ctx the parse tree
	 */
	void exitLinkageSection(DNPParser.LinkageSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#communicationSection}.
	 * @param ctx the parse tree
	 */
	void enterCommunicationSection(DNPParser.CommunicationSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#communicationSection}.
	 * @param ctx the parse tree
	 */
	void exitCommunicationSection(DNPParser.CommunicationSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#communicationDescriptionEntry}.
	 * @param ctx the parse tree
	 */
	void enterCommunicationDescriptionEntry(DNPParser.CommunicationDescriptionEntryContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#communicationDescriptionEntry}.
	 * @param ctx the parse tree
	 */
	void exitCommunicationDescriptionEntry(DNPParser.CommunicationDescriptionEntryContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#communicationDescriptionEntryFormat1}.
	 * @param ctx the parse tree
	 */
	void enterCommunicationDescriptionEntryFormat1(DNPParser.CommunicationDescriptionEntryFormat1Context ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#communicationDescriptionEntryFormat1}.
	 * @param ctx the parse tree
	 */
	void exitCommunicationDescriptionEntryFormat1(DNPParser.CommunicationDescriptionEntryFormat1Context ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#communicationDescriptionEntryFormat2}.
	 * @param ctx the parse tree
	 */
	void enterCommunicationDescriptionEntryFormat2(DNPParser.CommunicationDescriptionEntryFormat2Context ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#communicationDescriptionEntryFormat2}.
	 * @param ctx the parse tree
	 */
	void exitCommunicationDescriptionEntryFormat2(DNPParser.CommunicationDescriptionEntryFormat2Context ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#communicationDescriptionEntryFormat3}.
	 * @param ctx the parse tree
	 */
	void enterCommunicationDescriptionEntryFormat3(DNPParser.CommunicationDescriptionEntryFormat3Context ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#communicationDescriptionEntryFormat3}.
	 * @param ctx the parse tree
	 */
	void exitCommunicationDescriptionEntryFormat3(DNPParser.CommunicationDescriptionEntryFormat3Context ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#communicationDescriptionEntryFormat4}.
	 * @param ctx the parse tree
	 */
	void enterCommunicationDescriptionEntryFormat4(DNPParser.CommunicationDescriptionEntryFormat4Context ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#communicationDescriptionEntryFormat4}.
	 * @param ctx the parse tree
	 */
	void exitCommunicationDescriptionEntryFormat4(DNPParser.CommunicationDescriptionEntryFormat4Context ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#communicationAttribute}.
	 * @param ctx the parse tree
	 */
	void enterCommunicationAttribute(DNPParser.CommunicationAttributeContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#communicationAttribute}.
	 * @param ctx the parse tree
	 */
	void exitCommunicationAttribute(DNPParser.CommunicationAttributeContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#communicationIoHeader}.
	 * @param ctx the parse tree
	 */
	void enterCommunicationIoHeader(DNPParser.CommunicationIoHeaderContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#communicationIoHeader}.
	 * @param ctx the parse tree
	 */
	void exitCommunicationIoHeader(DNPParser.CommunicationIoHeaderContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#conversationClause}.
	 * @param ctx the parse tree
	 */
	void enterConversationClause(DNPParser.ConversationClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#conversationClause}.
	 * @param ctx the parse tree
	 */
	void exitConversationClause(DNPParser.ConversationClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#destinationCountClause}.
	 * @param ctx the parse tree
	 */
	void enterDestinationCountClause(DNPParser.DestinationCountClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#destinationCountClause}.
	 * @param ctx the parse tree
	 */
	void exitDestinationCountClause(DNPParser.DestinationCountClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#destinationTableClause}.
	 * @param ctx the parse tree
	 */
	void enterDestinationTableClause(DNPParser.DestinationTableClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#destinationTableClause}.
	 * @param ctx the parse tree
	 */
	void exitDestinationTableClause(DNPParser.DestinationTableClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#endKeyClause}.
	 * @param ctx the parse tree
	 */
	void enterEndKeyClause(DNPParser.EndKeyClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#endKeyClause}.
	 * @param ctx the parse tree
	 */
	void exitEndKeyClause(DNPParser.EndKeyClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#errorKeyClause}.
	 * @param ctx the parse tree
	 */
	void enterErrorKeyClause(DNPParser.ErrorKeyClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#errorKeyClause}.
	 * @param ctx the parse tree
	 */
	void exitErrorKeyClause(DNPParser.ErrorKeyClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#messageCountClause}.
	 * @param ctx the parse tree
	 */
	void enterMessageCountClause(DNPParser.MessageCountClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#messageCountClause}.
	 * @param ctx the parse tree
	 */
	void exitMessageCountClause(DNPParser.MessageCountClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#messageDateClause}.
	 * @param ctx the parse tree
	 */
	void enterMessageDateClause(DNPParser.MessageDateClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#messageDateClause}.
	 * @param ctx the parse tree
	 */
	void exitMessageDateClause(DNPParser.MessageDateClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#messageTimeClause}.
	 * @param ctx the parse tree
	 */
	void enterMessageTimeClause(DNPParser.MessageTimeClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#messageTimeClause}.
	 * @param ctx the parse tree
	 */
	void exitMessageTimeClause(DNPParser.MessageTimeClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#statusKeyClause}.
	 * @param ctx the parse tree
	 */
	void enterStatusKeyClause(DNPParser.StatusKeyClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#statusKeyClause}.
	 * @param ctx the parse tree
	 */
	void exitStatusKeyClause(DNPParser.StatusKeyClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#symbolicDestinationClause}.
	 * @param ctx the parse tree
	 */
	void enterSymbolicDestinationClause(DNPParser.SymbolicDestinationClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#symbolicDestinationClause}.
	 * @param ctx the parse tree
	 */
	void exitSymbolicDestinationClause(DNPParser.SymbolicDestinationClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#symbolicQueueClause}.
	 * @param ctx the parse tree
	 */
	void enterSymbolicQueueClause(DNPParser.SymbolicQueueClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#symbolicQueueClause}.
	 * @param ctx the parse tree
	 */
	void exitSymbolicQueueClause(DNPParser.SymbolicQueueClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#symbolicSourceClause}.
	 * @param ctx the parse tree
	 */
	void enterSymbolicSourceClause(DNPParser.SymbolicSourceClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#symbolicSourceClause}.
	 * @param ctx the parse tree
	 */
	void exitSymbolicSourceClause(DNPParser.SymbolicSourceClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#symbolicTerminalClause}.
	 * @param ctx the parse tree
	 */
	void enterSymbolicTerminalClause(DNPParser.SymbolicTerminalClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#symbolicTerminalClause}.
	 * @param ctx the parse tree
	 */
	void exitSymbolicTerminalClause(DNPParser.SymbolicTerminalClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#symbolicSubQueueClause}.
	 * @param ctx the parse tree
	 */
	void enterSymbolicSubQueueClause(DNPParser.SymbolicSubQueueClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#symbolicSubQueueClause}.
	 * @param ctx the parse tree
	 */
	void exitSymbolicSubQueueClause(DNPParser.SymbolicSubQueueClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#textLengthClause}.
	 * @param ctx the parse tree
	 */
	void enterTextLengthClause(DNPParser.TextLengthClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#textLengthClause}.
	 * @param ctx the parse tree
	 */
	void exitTextLengthClause(DNPParser.TextLengthClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#localStorageSection}.
	 * @param ctx the parse tree
	 */
	void enterLocalStorageSection(DNPParser.LocalStorageSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#localStorageSection}.
	 * @param ctx the parse tree
	 */
	void exitLocalStorageSection(DNPParser.LocalStorageSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenSection}.
	 * @param ctx the parse tree
	 */
	void enterScreenSection(DNPParser.ScreenSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenSection}.
	 * @param ctx the parse tree
	 */
	void exitScreenSection(DNPParser.ScreenSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenDescriptionEntry}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionEntry(DNPParser.ScreenDescriptionEntryContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenDescriptionEntry}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionEntry(DNPParser.ScreenDescriptionEntryContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenDescriptionBlankClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionBlankClause(DNPParser.ScreenDescriptionBlankClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenDescriptionBlankClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionBlankClause(DNPParser.ScreenDescriptionBlankClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenDescriptionBellClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionBellClause(DNPParser.ScreenDescriptionBellClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenDescriptionBellClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionBellClause(DNPParser.ScreenDescriptionBellClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenDescriptionBlinkClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionBlinkClause(DNPParser.ScreenDescriptionBlinkClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenDescriptionBlinkClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionBlinkClause(DNPParser.ScreenDescriptionBlinkClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenDescriptionEraseClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionEraseClause(DNPParser.ScreenDescriptionEraseClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenDescriptionEraseClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionEraseClause(DNPParser.ScreenDescriptionEraseClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenDescriptionLightClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionLightClause(DNPParser.ScreenDescriptionLightClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenDescriptionLightClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionLightClause(DNPParser.ScreenDescriptionLightClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenDescriptionGridClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionGridClause(DNPParser.ScreenDescriptionGridClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenDescriptionGridClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionGridClause(DNPParser.ScreenDescriptionGridClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenDescriptionReverseVideoClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionReverseVideoClause(DNPParser.ScreenDescriptionReverseVideoClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenDescriptionReverseVideoClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionReverseVideoClause(DNPParser.ScreenDescriptionReverseVideoClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenDescriptionUnderlineClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionUnderlineClause(DNPParser.ScreenDescriptionUnderlineClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenDescriptionUnderlineClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionUnderlineClause(DNPParser.ScreenDescriptionUnderlineClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenDescriptionSizeClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionSizeClause(DNPParser.ScreenDescriptionSizeClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenDescriptionSizeClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionSizeClause(DNPParser.ScreenDescriptionSizeClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenDescriptionLineClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionLineClause(DNPParser.ScreenDescriptionLineClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenDescriptionLineClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionLineClause(DNPParser.ScreenDescriptionLineClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenDescriptionColumnClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionColumnClause(DNPParser.ScreenDescriptionColumnClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenDescriptionColumnClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionColumnClause(DNPParser.ScreenDescriptionColumnClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenDescriptionForegroundColorClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionForegroundColorClause(DNPParser.ScreenDescriptionForegroundColorClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenDescriptionForegroundColorClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionForegroundColorClause(DNPParser.ScreenDescriptionForegroundColorClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenDescriptionBackgroundColorClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionBackgroundColorClause(DNPParser.ScreenDescriptionBackgroundColorClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenDescriptionBackgroundColorClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionBackgroundColorClause(DNPParser.ScreenDescriptionBackgroundColorClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenDescriptionControlClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionControlClause(DNPParser.ScreenDescriptionControlClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenDescriptionControlClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionControlClause(DNPParser.ScreenDescriptionControlClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenDescriptionValueClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionValueClause(DNPParser.ScreenDescriptionValueClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenDescriptionValueClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionValueClause(DNPParser.ScreenDescriptionValueClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenDescriptionPictureClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionPictureClause(DNPParser.ScreenDescriptionPictureClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenDescriptionPictureClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionPictureClause(DNPParser.ScreenDescriptionPictureClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenDescriptionFromClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionFromClause(DNPParser.ScreenDescriptionFromClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenDescriptionFromClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionFromClause(DNPParser.ScreenDescriptionFromClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenDescriptionToClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionToClause(DNPParser.ScreenDescriptionToClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenDescriptionToClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionToClause(DNPParser.ScreenDescriptionToClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenDescriptionUsingClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionUsingClause(DNPParser.ScreenDescriptionUsingClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenDescriptionUsingClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionUsingClause(DNPParser.ScreenDescriptionUsingClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenDescriptionUsageClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionUsageClause(DNPParser.ScreenDescriptionUsageClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenDescriptionUsageClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionUsageClause(DNPParser.ScreenDescriptionUsageClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenDescriptionBlankWhenZeroClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionBlankWhenZeroClause(DNPParser.ScreenDescriptionBlankWhenZeroClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenDescriptionBlankWhenZeroClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionBlankWhenZeroClause(DNPParser.ScreenDescriptionBlankWhenZeroClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenDescriptionJustifiedClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionJustifiedClause(DNPParser.ScreenDescriptionJustifiedClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenDescriptionJustifiedClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionJustifiedClause(DNPParser.ScreenDescriptionJustifiedClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenDescriptionSignClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionSignClause(DNPParser.ScreenDescriptionSignClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenDescriptionSignClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionSignClause(DNPParser.ScreenDescriptionSignClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenDescriptionAutoClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionAutoClause(DNPParser.ScreenDescriptionAutoClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenDescriptionAutoClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionAutoClause(DNPParser.ScreenDescriptionAutoClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenDescriptionSecureClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionSecureClause(DNPParser.ScreenDescriptionSecureClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenDescriptionSecureClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionSecureClause(DNPParser.ScreenDescriptionSecureClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenDescriptionRequiredClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionRequiredClause(DNPParser.ScreenDescriptionRequiredClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenDescriptionRequiredClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionRequiredClause(DNPParser.ScreenDescriptionRequiredClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenDescriptionPromptClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionPromptClause(DNPParser.ScreenDescriptionPromptClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenDescriptionPromptClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionPromptClause(DNPParser.ScreenDescriptionPromptClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenDescriptionPromptOccursClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionPromptOccursClause(DNPParser.ScreenDescriptionPromptOccursClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenDescriptionPromptOccursClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionPromptOccursClause(DNPParser.ScreenDescriptionPromptOccursClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenDescriptionFullClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionFullClause(DNPParser.ScreenDescriptionFullClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenDescriptionFullClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionFullClause(DNPParser.ScreenDescriptionFullClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenDescriptionZeroFillClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionZeroFillClause(DNPParser.ScreenDescriptionZeroFillClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenDescriptionZeroFillClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionZeroFillClause(DNPParser.ScreenDescriptionZeroFillClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportSection}.
	 * @param ctx the parse tree
	 */
	void enterReportSection(DNPParser.ReportSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportSection}.
	 * @param ctx the parse tree
	 */
	void exitReportSection(DNPParser.ReportSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportDescription}.
	 * @param ctx the parse tree
	 */
	void enterReportDescription(DNPParser.ReportDescriptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportDescription}.
	 * @param ctx the parse tree
	 */
	void exitReportDescription(DNPParser.ReportDescriptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportDescriptionEntry}.
	 * @param ctx the parse tree
	 */
	void enterReportDescriptionEntry(DNPParser.ReportDescriptionEntryContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportDescriptionEntry}.
	 * @param ctx the parse tree
	 */
	void exitReportDescriptionEntry(DNPParser.ReportDescriptionEntryContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportDescriptionGlobalClause}.
	 * @param ctx the parse tree
	 */
	void enterReportDescriptionGlobalClause(DNPParser.ReportDescriptionGlobalClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportDescriptionGlobalClause}.
	 * @param ctx the parse tree
	 */
	void exitReportDescriptionGlobalClause(DNPParser.ReportDescriptionGlobalClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportDescriptionPageLimitClause}.
	 * @param ctx the parse tree
	 */
	void enterReportDescriptionPageLimitClause(DNPParser.ReportDescriptionPageLimitClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportDescriptionPageLimitClause}.
	 * @param ctx the parse tree
	 */
	void exitReportDescriptionPageLimitClause(DNPParser.ReportDescriptionPageLimitClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportDescriptionHeadingClause}.
	 * @param ctx the parse tree
	 */
	void enterReportDescriptionHeadingClause(DNPParser.ReportDescriptionHeadingClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportDescriptionHeadingClause}.
	 * @param ctx the parse tree
	 */
	void exitReportDescriptionHeadingClause(DNPParser.ReportDescriptionHeadingClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportDescriptionFirstDetailClause}.
	 * @param ctx the parse tree
	 */
	void enterReportDescriptionFirstDetailClause(DNPParser.ReportDescriptionFirstDetailClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportDescriptionFirstDetailClause}.
	 * @param ctx the parse tree
	 */
	void exitReportDescriptionFirstDetailClause(DNPParser.ReportDescriptionFirstDetailClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportDescriptionLastDetailClause}.
	 * @param ctx the parse tree
	 */
	void enterReportDescriptionLastDetailClause(DNPParser.ReportDescriptionLastDetailClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportDescriptionLastDetailClause}.
	 * @param ctx the parse tree
	 */
	void exitReportDescriptionLastDetailClause(DNPParser.ReportDescriptionLastDetailClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportDescriptionFootingClause}.
	 * @param ctx the parse tree
	 */
	void enterReportDescriptionFootingClause(DNPParser.ReportDescriptionFootingClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportDescriptionFootingClause}.
	 * @param ctx the parse tree
	 */
	void exitReportDescriptionFootingClause(DNPParser.ReportDescriptionFootingClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportGroupDescriptionEntry}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupDescriptionEntry(DNPParser.ReportGroupDescriptionEntryContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportGroupDescriptionEntry}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupDescriptionEntry(DNPParser.ReportGroupDescriptionEntryContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportGroupDescriptionEntryFormat1}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupDescriptionEntryFormat1(DNPParser.ReportGroupDescriptionEntryFormat1Context ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportGroupDescriptionEntryFormat1}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupDescriptionEntryFormat1(DNPParser.ReportGroupDescriptionEntryFormat1Context ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportGroupDescriptionEntryFormat2}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupDescriptionEntryFormat2(DNPParser.ReportGroupDescriptionEntryFormat2Context ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportGroupDescriptionEntryFormat2}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupDescriptionEntryFormat2(DNPParser.ReportGroupDescriptionEntryFormat2Context ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportGroupDescriptionEntryFormat3}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupDescriptionEntryFormat3(DNPParser.ReportGroupDescriptionEntryFormat3Context ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportGroupDescriptionEntryFormat3}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupDescriptionEntryFormat3(DNPParser.ReportGroupDescriptionEntryFormat3Context ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportGroupBlankWhenZeroClause}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupBlankWhenZeroClause(DNPParser.ReportGroupBlankWhenZeroClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportGroupBlankWhenZeroClause}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupBlankWhenZeroClause(DNPParser.ReportGroupBlankWhenZeroClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportGroupColumnNumberClause}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupColumnNumberClause(DNPParser.ReportGroupColumnNumberClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportGroupColumnNumberClause}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupColumnNumberClause(DNPParser.ReportGroupColumnNumberClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportGroupIndicateClause}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupIndicateClause(DNPParser.ReportGroupIndicateClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportGroupIndicateClause}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupIndicateClause(DNPParser.ReportGroupIndicateClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportGroupJustifiedClause}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupJustifiedClause(DNPParser.ReportGroupJustifiedClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportGroupJustifiedClause}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupJustifiedClause(DNPParser.ReportGroupJustifiedClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportGroupLineNumberClause}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupLineNumberClause(DNPParser.ReportGroupLineNumberClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportGroupLineNumberClause}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupLineNumberClause(DNPParser.ReportGroupLineNumberClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportGroupLineNumberNextPage}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupLineNumberNextPage(DNPParser.ReportGroupLineNumberNextPageContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportGroupLineNumberNextPage}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupLineNumberNextPage(DNPParser.ReportGroupLineNumberNextPageContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportGroupLineNumberPlus}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupLineNumberPlus(DNPParser.ReportGroupLineNumberPlusContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportGroupLineNumberPlus}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupLineNumberPlus(DNPParser.ReportGroupLineNumberPlusContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportGroupNextGroupClause}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupNextGroupClause(DNPParser.ReportGroupNextGroupClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportGroupNextGroupClause}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupNextGroupClause(DNPParser.ReportGroupNextGroupClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportGroupNextGroupPlus}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupNextGroupPlus(DNPParser.ReportGroupNextGroupPlusContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportGroupNextGroupPlus}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupNextGroupPlus(DNPParser.ReportGroupNextGroupPlusContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportGroupNextGroupNextPage}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupNextGroupNextPage(DNPParser.ReportGroupNextGroupNextPageContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportGroupNextGroupNextPage}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupNextGroupNextPage(DNPParser.ReportGroupNextGroupNextPageContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportGroupPictureClause}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupPictureClause(DNPParser.ReportGroupPictureClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportGroupPictureClause}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupPictureClause(DNPParser.ReportGroupPictureClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportGroupResetClause}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupResetClause(DNPParser.ReportGroupResetClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportGroupResetClause}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupResetClause(DNPParser.ReportGroupResetClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportGroupSignClause}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupSignClause(DNPParser.ReportGroupSignClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportGroupSignClause}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupSignClause(DNPParser.ReportGroupSignClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportGroupSourceClause}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupSourceClause(DNPParser.ReportGroupSourceClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportGroupSourceClause}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupSourceClause(DNPParser.ReportGroupSourceClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportGroupSumClause}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupSumClause(DNPParser.ReportGroupSumClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportGroupSumClause}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupSumClause(DNPParser.ReportGroupSumClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportGroupTypeClause}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupTypeClause(DNPParser.ReportGroupTypeClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportGroupTypeClause}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupTypeClause(DNPParser.ReportGroupTypeClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportGroupTypeReportHeading}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupTypeReportHeading(DNPParser.ReportGroupTypeReportHeadingContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportGroupTypeReportHeading}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupTypeReportHeading(DNPParser.ReportGroupTypeReportHeadingContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportGroupTypePageHeading}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupTypePageHeading(DNPParser.ReportGroupTypePageHeadingContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportGroupTypePageHeading}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupTypePageHeading(DNPParser.ReportGroupTypePageHeadingContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportGroupTypeControlHeading}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupTypeControlHeading(DNPParser.ReportGroupTypeControlHeadingContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportGroupTypeControlHeading}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupTypeControlHeading(DNPParser.ReportGroupTypeControlHeadingContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportGroupTypeDetail}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupTypeDetail(DNPParser.ReportGroupTypeDetailContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportGroupTypeDetail}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupTypeDetail(DNPParser.ReportGroupTypeDetailContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportGroupTypeControlFooting}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupTypeControlFooting(DNPParser.ReportGroupTypeControlFootingContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportGroupTypeControlFooting}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupTypeControlFooting(DNPParser.ReportGroupTypeControlFootingContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportGroupUsageClause}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupUsageClause(DNPParser.ReportGroupUsageClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportGroupUsageClause}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupUsageClause(DNPParser.ReportGroupUsageClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportGroupTypePageFooting}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupTypePageFooting(DNPParser.ReportGroupTypePageFootingContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportGroupTypePageFooting}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupTypePageFooting(DNPParser.ReportGroupTypePageFootingContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportGroupTypeReportFooting}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupTypeReportFooting(DNPParser.ReportGroupTypeReportFootingContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportGroupTypeReportFooting}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupTypeReportFooting(DNPParser.ReportGroupTypeReportFootingContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportGroupValueClause}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupValueClause(DNPParser.ReportGroupValueClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportGroupValueClause}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupValueClause(DNPParser.ReportGroupValueClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#programLibrarySection}.
	 * @param ctx the parse tree
	 */
	void enterProgramLibrarySection(DNPParser.ProgramLibrarySectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#programLibrarySection}.
	 * @param ctx the parse tree
	 */
	void exitProgramLibrarySection(DNPParser.ProgramLibrarySectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#libraryDescriptionEntry}.
	 * @param ctx the parse tree
	 */
	void enterLibraryDescriptionEntry(DNPParser.LibraryDescriptionEntryContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#libraryDescriptionEntry}.
	 * @param ctx the parse tree
	 */
	void exitLibraryDescriptionEntry(DNPParser.LibraryDescriptionEntryContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#libraryDescriptionEntryFormat1}.
	 * @param ctx the parse tree
	 */
	void enterLibraryDescriptionEntryFormat1(DNPParser.LibraryDescriptionEntryFormat1Context ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#libraryDescriptionEntryFormat1}.
	 * @param ctx the parse tree
	 */
	void exitLibraryDescriptionEntryFormat1(DNPParser.LibraryDescriptionEntryFormat1Context ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#libraryDescriptionEntryFormat2}.
	 * @param ctx the parse tree
	 */
	void enterLibraryDescriptionEntryFormat2(DNPParser.LibraryDescriptionEntryFormat2Context ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#libraryDescriptionEntryFormat2}.
	 * @param ctx the parse tree
	 */
	void exitLibraryDescriptionEntryFormat2(DNPParser.LibraryDescriptionEntryFormat2Context ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#libraryAttributeClauseFormat1}.
	 * @param ctx the parse tree
	 */
	void enterLibraryAttributeClauseFormat1(DNPParser.LibraryAttributeClauseFormat1Context ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#libraryAttributeClauseFormat1}.
	 * @param ctx the parse tree
	 */
	void exitLibraryAttributeClauseFormat1(DNPParser.LibraryAttributeClauseFormat1Context ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#libraryAttributeClauseFormat2}.
	 * @param ctx the parse tree
	 */
	void enterLibraryAttributeClauseFormat2(DNPParser.LibraryAttributeClauseFormat2Context ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#libraryAttributeClauseFormat2}.
	 * @param ctx the parse tree
	 */
	void exitLibraryAttributeClauseFormat2(DNPParser.LibraryAttributeClauseFormat2Context ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#libraryAttributeFunction}.
	 * @param ctx the parse tree
	 */
	void enterLibraryAttributeFunction(DNPParser.LibraryAttributeFunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#libraryAttributeFunction}.
	 * @param ctx the parse tree
	 */
	void exitLibraryAttributeFunction(DNPParser.LibraryAttributeFunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#libraryAttributeParameter}.
	 * @param ctx the parse tree
	 */
	void enterLibraryAttributeParameter(DNPParser.LibraryAttributeParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#libraryAttributeParameter}.
	 * @param ctx the parse tree
	 */
	void exitLibraryAttributeParameter(DNPParser.LibraryAttributeParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#libraryAttributeTitle}.
	 * @param ctx the parse tree
	 */
	void enterLibraryAttributeTitle(DNPParser.LibraryAttributeTitleContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#libraryAttributeTitle}.
	 * @param ctx the parse tree
	 */
	void exitLibraryAttributeTitle(DNPParser.LibraryAttributeTitleContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#libraryEntryProcedureClauseFormat1}.
	 * @param ctx the parse tree
	 */
	void enterLibraryEntryProcedureClauseFormat1(DNPParser.LibraryEntryProcedureClauseFormat1Context ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#libraryEntryProcedureClauseFormat1}.
	 * @param ctx the parse tree
	 */
	void exitLibraryEntryProcedureClauseFormat1(DNPParser.LibraryEntryProcedureClauseFormat1Context ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#libraryEntryProcedureClauseFormat2}.
	 * @param ctx the parse tree
	 */
	void enterLibraryEntryProcedureClauseFormat2(DNPParser.LibraryEntryProcedureClauseFormat2Context ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#libraryEntryProcedureClauseFormat2}.
	 * @param ctx the parse tree
	 */
	void exitLibraryEntryProcedureClauseFormat2(DNPParser.LibraryEntryProcedureClauseFormat2Context ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#libraryEntryProcedureForClause}.
	 * @param ctx the parse tree
	 */
	void enterLibraryEntryProcedureForClause(DNPParser.LibraryEntryProcedureForClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#libraryEntryProcedureForClause}.
	 * @param ctx the parse tree
	 */
	void exitLibraryEntryProcedureForClause(DNPParser.LibraryEntryProcedureForClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#libraryEntryProcedureGivingClause}.
	 * @param ctx the parse tree
	 */
	void enterLibraryEntryProcedureGivingClause(DNPParser.LibraryEntryProcedureGivingClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#libraryEntryProcedureGivingClause}.
	 * @param ctx the parse tree
	 */
	void exitLibraryEntryProcedureGivingClause(DNPParser.LibraryEntryProcedureGivingClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#libraryEntryProcedureUsingClause}.
	 * @param ctx the parse tree
	 */
	void enterLibraryEntryProcedureUsingClause(DNPParser.LibraryEntryProcedureUsingClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#libraryEntryProcedureUsingClause}.
	 * @param ctx the parse tree
	 */
	void exitLibraryEntryProcedureUsingClause(DNPParser.LibraryEntryProcedureUsingClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#libraryEntryProcedureUsingName}.
	 * @param ctx the parse tree
	 */
	void enterLibraryEntryProcedureUsingName(DNPParser.LibraryEntryProcedureUsingNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#libraryEntryProcedureUsingName}.
	 * @param ctx the parse tree
	 */
	void exitLibraryEntryProcedureUsingName(DNPParser.LibraryEntryProcedureUsingNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#libraryEntryProcedureWithClause}.
	 * @param ctx the parse tree
	 */
	void enterLibraryEntryProcedureWithClause(DNPParser.LibraryEntryProcedureWithClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#libraryEntryProcedureWithClause}.
	 * @param ctx the parse tree
	 */
	void exitLibraryEntryProcedureWithClause(DNPParser.LibraryEntryProcedureWithClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#libraryEntryProcedureWithName}.
	 * @param ctx the parse tree
	 */
	void enterLibraryEntryProcedureWithName(DNPParser.LibraryEntryProcedureWithNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#libraryEntryProcedureWithName}.
	 * @param ctx the parse tree
	 */
	void exitLibraryEntryProcedureWithName(DNPParser.LibraryEntryProcedureWithNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#libraryIsCommonClause}.
	 * @param ctx the parse tree
	 */
	void enterLibraryIsCommonClause(DNPParser.LibraryIsCommonClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#libraryIsCommonClause}.
	 * @param ctx the parse tree
	 */
	void exitLibraryIsCommonClause(DNPParser.LibraryIsCommonClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#libraryIsGlobalClause}.
	 * @param ctx the parse tree
	 */
	void enterLibraryIsGlobalClause(DNPParser.LibraryIsGlobalClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#libraryIsGlobalClause}.
	 * @param ctx the parse tree
	 */
	void exitLibraryIsGlobalClause(DNPParser.LibraryIsGlobalClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataDescriptionEntry}.
	 * @param ctx the parse tree
	 */
	void enterDataDescriptionEntry(DNPParser.DataDescriptionEntryContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataDescriptionEntry}.
	 * @param ctx the parse tree
	 */
	void exitDataDescriptionEntry(DNPParser.DataDescriptionEntryContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#copyStatement}.
	 * @param ctx the parse tree
	 */
	void enterCopyStatement(DNPParser.CopyStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#copyStatement}.
	 * @param ctx the parse tree
	 */
	void exitCopyStatement(DNPParser.CopyStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#copySource}.
	 * @param ctx the parse tree
	 */
	void enterCopySource(DNPParser.CopySourceContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#copySource}.
	 * @param ctx the parse tree
	 */
	void exitCopySource(DNPParser.CopySourceContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#copyLibrary}.
	 * @param ctx the parse tree
	 */
	void enterCopyLibrary(DNPParser.CopyLibraryContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#copyLibrary}.
	 * @param ctx the parse tree
	 */
	void exitCopyLibrary(DNPParser.CopyLibraryContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#replacingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterReplacingPhrase(DNPParser.ReplacingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#replacingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitReplacingPhrase(DNPParser.ReplacingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#changeStatement}.
	 * @param ctx the parse tree
	 */
	void enterChangeStatement(DNPParser.ChangeStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#changeStatement}.
	 * @param ctx the parse tree
	 */
	void exitChangeStatement(DNPParser.ChangeStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#changeFileAttribute}.
	 * @param ctx the parse tree
	 */
	void enterChangeFileAttribute(DNPParser.ChangeFileAttributeContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#changeFileAttribute}.
	 * @param ctx the parse tree
	 */
	void exitChangeFileAttribute(DNPParser.ChangeFileAttributeContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#changeLibraryAttribute}.
	 * @param ctx the parse tree
	 */
	void enterChangeLibraryAttribute(DNPParser.ChangeLibraryAttributeContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#changeLibraryAttribute}.
	 * @param ctx the parse tree
	 */
	void exitChangeLibraryAttribute(DNPParser.ChangeLibraryAttributeContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#libraryAttributeName}.
	 * @param ctx the parse tree
	 */
	void enterLibraryAttributeName(DNPParser.LibraryAttributeNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#libraryAttributeName}.
	 * @param ctx the parse tree
	 */
	void exitLibraryAttributeName(DNPParser.LibraryAttributeNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#libraryValueOption}.
	 * @param ctx the parse tree
	 */
	void enterLibraryValueOption(DNPParser.LibraryValueOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#libraryValueOption}.
	 * @param ctx the parse tree
	 */
	void exitLibraryValueOption(DNPParser.LibraryValueOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#toValueOption}.
	 * @param ctx the parse tree
	 */
	void enterToValueOption(DNPParser.ToValueOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#toValueOption}.
	 * @param ctx the parse tree
	 */
	void exitToValueOption(DNPParser.ToValueOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#createStatement}.
	 * @param ctx the parse tree
	 */
	void enterCreateStatement(DNPParser.CreateStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#createStatement}.
	 * @param ctx the parse tree
	 */
	void exitCreateStatement(DNPParser.CreateStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#replaceOffStatement}.
	 * @param ctx the parse tree
	 */
	void enterReplaceOffStatement(DNPParser.ReplaceOffStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#replaceOffStatement}.
	 * @param ctx the parse tree
	 */
	void exitReplaceOffStatement(DNPParser.ReplaceOffStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#replaceClause}.
	 * @param ctx the parse tree
	 */
	void enterReplaceClause(DNPParser.ReplaceClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#replaceClause}.
	 * @param ctx the parse tree
	 */
	void exitReplaceClause(DNPParser.ReplaceClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#directoryPhrase}.
	 * @param ctx the parse tree
	 */
	void enterDirectoryPhrase(DNPParser.DirectoryPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#directoryPhrase}.
	 * @param ctx the parse tree
	 */
	void exitDirectoryPhrase(DNPParser.DirectoryPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#familyPhrase}.
	 * @param ctx the parse tree
	 */
	void enterFamilyPhrase(DNPParser.FamilyPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#familyPhrase}.
	 * @param ctx the parse tree
	 */
	void exitFamilyPhrase(DNPParser.FamilyPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#replaceable}.
	 * @param ctx the parse tree
	 */
	void enterReplaceable(DNPParser.ReplaceableContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#replaceable}.
	 * @param ctx the parse tree
	 */
	void exitReplaceable(DNPParser.ReplaceableContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#replacement}.
	 * @param ctx the parse tree
	 */
	void enterReplacement(DNPParser.ReplacementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#replacement}.
	 * @param ctx the parse tree
	 */
	void exitReplacement(DNPParser.ReplacementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#ejectStatement}.
	 * @param ctx the parse tree
	 */
	void enterEjectStatement(DNPParser.EjectStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#ejectStatement}.
	 * @param ctx the parse tree
	 */
	void exitEjectStatement(DNPParser.EjectStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#skipStatement}.
	 * @param ctx the parse tree
	 */
	void enterSkipStatement(DNPParser.SkipStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#skipStatement}.
	 * @param ctx the parse tree
	 */
	void exitSkipStatement(DNPParser.SkipStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#titleStatement}.
	 * @param ctx the parse tree
	 */
	void enterTitleStatement(DNPParser.TitleStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#titleStatement}.
	 * @param ctx the parse tree
	 */
	void exitTitleStatement(DNPParser.TitleStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#pseudoText}.
	 * @param ctx the parse tree
	 */
	void enterPseudoText(DNPParser.PseudoTextContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#pseudoText}.
	 * @param ctx the parse tree
	 */
	void exitPseudoText(DNPParser.PseudoTextContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#charData}.
	 * @param ctx the parse tree
	 */
	void enterCharData(DNPParser.CharDataContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#charData}.
	 * @param ctx the parse tree
	 */
	void exitCharData(DNPParser.CharDataContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#charDataSql}.
	 * @param ctx the parse tree
	 */
	void enterCharDataSql(DNPParser.CharDataSqlContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#charDataSql}.
	 * @param ctx the parse tree
	 */
	void exitCharDataSql(DNPParser.CharDataSqlContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#charDataLine}.
	 * @param ctx the parse tree
	 */
	void enterCharDataLine(DNPParser.CharDataLineContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#charDataLine}.
	 * @param ctx the parse tree
	 */
	void exitCharDataLine(DNPParser.CharDataLineContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#cobolWord}.
	 * @param ctx the parse tree
	 */
	void enterCobolWord(DNPParser.CobolWordContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#cobolWord}.
	 * @param ctx the parse tree
	 */
	void exitCobolWord(DNPParser.CobolWordContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(DNPParser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(DNPParser.LiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#jpEncodingText}.
	 * @param ctx the parse tree
	 */
	void enterJpEncodingText(DNPParser.JpEncodingTextContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#jpEncodingText}.
	 * @param ctx the parse tree
	 */
	void exitJpEncodingText(DNPParser.JpEncodingTextContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#filename}.
	 * @param ctx the parse tree
	 */
	void enterFilename(DNPParser.FilenameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#filename}.
	 * @param ctx the parse tree
	 */
	void exitFilename(DNPParser.FilenameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataDescriptionEntryFormat1}.
	 * @param ctx the parse tree
	 */
	void enterDataDescriptionEntryFormat1(DNPParser.DataDescriptionEntryFormat1Context ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataDescriptionEntryFormat1}.
	 * @param ctx the parse tree
	 */
	void exitDataDescriptionEntryFormat1(DNPParser.DataDescriptionEntryFormat1Context ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataDescriptionEntryFormat2}.
	 * @param ctx the parse tree
	 */
	void enterDataDescriptionEntryFormat2(DNPParser.DataDescriptionEntryFormat2Context ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataDescriptionEntryFormat2}.
	 * @param ctx the parse tree
	 */
	void exitDataDescriptionEntryFormat2(DNPParser.DataDescriptionEntryFormat2Context ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataDescriptionEntryFormat3}.
	 * @param ctx the parse tree
	 */
	void enterDataDescriptionEntryFormat3(DNPParser.DataDescriptionEntryFormat3Context ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataDescriptionEntryFormat3}.
	 * @param ctx the parse tree
	 */
	void exitDataDescriptionEntryFormat3(DNPParser.DataDescriptionEntryFormat3Context ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataDescriptionEntryExecSql}.
	 * @param ctx the parse tree
	 */
	void enterDataDescriptionEntryExecSql(DNPParser.DataDescriptionEntryExecSqlContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataDescriptionEntryExecSql}.
	 * @param ctx the parse tree
	 */
	void exitDataDescriptionEntryExecSql(DNPParser.DataDescriptionEntryExecSqlContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataAlignedClause}.
	 * @param ctx the parse tree
	 */
	void enterDataAlignedClause(DNPParser.DataAlignedClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataAlignedClause}.
	 * @param ctx the parse tree
	 */
	void exitDataAlignedClause(DNPParser.DataAlignedClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataBlankWhenZeroClause}.
	 * @param ctx the parse tree
	 */
	void enterDataBlankWhenZeroClause(DNPParser.DataBlankWhenZeroClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataBlankWhenZeroClause}.
	 * @param ctx the parse tree
	 */
	void exitDataBlankWhenZeroClause(DNPParser.DataBlankWhenZeroClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataCommonOwnLocalClause}.
	 * @param ctx the parse tree
	 */
	void enterDataCommonOwnLocalClause(DNPParser.DataCommonOwnLocalClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataCommonOwnLocalClause}.
	 * @param ctx the parse tree
	 */
	void exitDataCommonOwnLocalClause(DNPParser.DataCommonOwnLocalClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataExternalClause}.
	 * @param ctx the parse tree
	 */
	void enterDataExternalClause(DNPParser.DataExternalClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataExternalClause}.
	 * @param ctx the parse tree
	 */
	void exitDataExternalClause(DNPParser.DataExternalClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataGlobalClause}.
	 * @param ctx the parse tree
	 */
	void enterDataGlobalClause(DNPParser.DataGlobalClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataGlobalClause}.
	 * @param ctx the parse tree
	 */
	void exitDataGlobalClause(DNPParser.DataGlobalClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataIntegerStringClause}.
	 * @param ctx the parse tree
	 */
	void enterDataIntegerStringClause(DNPParser.DataIntegerStringClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataIntegerStringClause}.
	 * @param ctx the parse tree
	 */
	void exitDataIntegerStringClause(DNPParser.DataIntegerStringClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataJustifiedClause}.
	 * @param ctx the parse tree
	 */
	void enterDataJustifiedClause(DNPParser.DataJustifiedClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataJustifiedClause}.
	 * @param ctx the parse tree
	 */
	void exitDataJustifiedClause(DNPParser.DataJustifiedClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataOccursClause}.
	 * @param ctx the parse tree
	 */
	void enterDataOccursClause(DNPParser.DataOccursClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataOccursClause}.
	 * @param ctx the parse tree
	 */
	void exitDataOccursClause(DNPParser.DataOccursClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataOccursTo}.
	 * @param ctx the parse tree
	 */
	void enterDataOccursTo(DNPParser.DataOccursToContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataOccursTo}.
	 * @param ctx the parse tree
	 */
	void exitDataOccursTo(DNPParser.DataOccursToContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataOccursSort}.
	 * @param ctx the parse tree
	 */
	void enterDataOccursSort(DNPParser.DataOccursSortContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataOccursSort}.
	 * @param ctx the parse tree
	 */
	void exitDataOccursSort(DNPParser.DataOccursSortContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataPictureClause}.
	 * @param ctx the parse tree
	 */
	void enterDataPictureClause(DNPParser.DataPictureClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataPictureClause}.
	 * @param ctx the parse tree
	 */
	void exitDataPictureClause(DNPParser.DataPictureClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#pictureString}.
	 * @param ctx the parse tree
	 */
	void enterPictureString(DNPParser.PictureStringContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#pictureString}.
	 * @param ctx the parse tree
	 */
	void exitPictureString(DNPParser.PictureStringContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#pictureChars}.
	 * @param ctx the parse tree
	 */
	void enterPictureChars(DNPParser.PictureCharsContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#pictureChars}.
	 * @param ctx the parse tree
	 */
	void exitPictureChars(DNPParser.PictureCharsContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#pictureCardinality}.
	 * @param ctx the parse tree
	 */
	void enterPictureCardinality(DNPParser.PictureCardinalityContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#pictureCardinality}.
	 * @param ctx the parse tree
	 */
	void exitPictureCardinality(DNPParser.PictureCardinalityContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataReceivedByClause}.
	 * @param ctx the parse tree
	 */
	void enterDataReceivedByClause(DNPParser.DataReceivedByClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataReceivedByClause}.
	 * @param ctx the parse tree
	 */
	void exitDataReceivedByClause(DNPParser.DataReceivedByClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataRecordAreaClause}.
	 * @param ctx the parse tree
	 */
	void enterDataRecordAreaClause(DNPParser.DataRecordAreaClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataRecordAreaClause}.
	 * @param ctx the parse tree
	 */
	void exitDataRecordAreaClause(DNPParser.DataRecordAreaClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataRedefinesClause}.
	 * @param ctx the parse tree
	 */
	void enterDataRedefinesClause(DNPParser.DataRedefinesClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataRedefinesClause}.
	 * @param ctx the parse tree
	 */
	void exitDataRedefinesClause(DNPParser.DataRedefinesClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataRenamesClause}.
	 * @param ctx the parse tree
	 */
	void enterDataRenamesClause(DNPParser.DataRenamesClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataRenamesClause}.
	 * @param ctx the parse tree
	 */
	void exitDataRenamesClause(DNPParser.DataRenamesClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataSignClause}.
	 * @param ctx the parse tree
	 */
	void enterDataSignClause(DNPParser.DataSignClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataSignClause}.
	 * @param ctx the parse tree
	 */
	void exitDataSignClause(DNPParser.DataSignClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataSynchronizedClause}.
	 * @param ctx the parse tree
	 */
	void enterDataSynchronizedClause(DNPParser.DataSynchronizedClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataSynchronizedClause}.
	 * @param ctx the parse tree
	 */
	void exitDataSynchronizedClause(DNPParser.DataSynchronizedClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataThreadLocalClause}.
	 * @param ctx the parse tree
	 */
	void enterDataThreadLocalClause(DNPParser.DataThreadLocalClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataThreadLocalClause}.
	 * @param ctx the parse tree
	 */
	void exitDataThreadLocalClause(DNPParser.DataThreadLocalClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataTypeClause}.
	 * @param ctx the parse tree
	 */
	void enterDataTypeClause(DNPParser.DataTypeClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataTypeClause}.
	 * @param ctx the parse tree
	 */
	void exitDataTypeClause(DNPParser.DataTypeClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataTypeDefClause}.
	 * @param ctx the parse tree
	 */
	void enterDataTypeDefClause(DNPParser.DataTypeDefClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataTypeDefClause}.
	 * @param ctx the parse tree
	 */
	void exitDataTypeDefClause(DNPParser.DataTypeDefClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataUsageClause}.
	 * @param ctx the parse tree
	 */
	void enterDataUsageClause(DNPParser.DataUsageClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataUsageClause}.
	 * @param ctx the parse tree
	 */
	void exitDataUsageClause(DNPParser.DataUsageClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataUsingClause}.
	 * @param ctx the parse tree
	 */
	void enterDataUsingClause(DNPParser.DataUsingClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataUsingClause}.
	 * @param ctx the parse tree
	 */
	void exitDataUsingClause(DNPParser.DataUsingClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataValueClause}.
	 * @param ctx the parse tree
	 */
	void enterDataValueClause(DNPParser.DataValueClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataValueClause}.
	 * @param ctx the parse tree
	 */
	void exitDataValueClause(DNPParser.DataValueClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataValueInterval}.
	 * @param ctx the parse tree
	 */
	void enterDataValueInterval(DNPParser.DataValueIntervalContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataValueInterval}.
	 * @param ctx the parse tree
	 */
	void exitDataValueInterval(DNPParser.DataValueIntervalContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataValueIntervalFrom}.
	 * @param ctx the parse tree
	 */
	void enterDataValueIntervalFrom(DNPParser.DataValueIntervalFromContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataValueIntervalFrom}.
	 * @param ctx the parse tree
	 */
	void exitDataValueIntervalFrom(DNPParser.DataValueIntervalFromContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataValueIntervalTo}.
	 * @param ctx the parse tree
	 */
	void enterDataValueIntervalTo(DNPParser.DataValueIntervalToContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataValueIntervalTo}.
	 * @param ctx the parse tree
	 */
	void exitDataValueIntervalTo(DNPParser.DataValueIntervalToContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataWithLowerBoundsClause}.
	 * @param ctx the parse tree
	 */
	void enterDataWithLowerBoundsClause(DNPParser.DataWithLowerBoundsClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataWithLowerBoundsClause}.
	 * @param ctx the parse tree
	 */
	void exitDataWithLowerBoundsClause(DNPParser.DataWithLowerBoundsClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#procedureDivision}.
	 * @param ctx the parse tree
	 */
	void enterProcedureDivision(DNPParser.ProcedureDivisionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#procedureDivision}.
	 * @param ctx the parse tree
	 */
	void exitProcedureDivision(DNPParser.ProcedureDivisionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#procedureDivisionUsingClause}.
	 * @param ctx the parse tree
	 */
	void enterProcedureDivisionUsingClause(DNPParser.ProcedureDivisionUsingClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#procedureDivisionUsingClause}.
	 * @param ctx the parse tree
	 */
	void exitProcedureDivisionUsingClause(DNPParser.ProcedureDivisionUsingClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#procedureDivisionGivingClause}.
	 * @param ctx the parse tree
	 */
	void enterProcedureDivisionGivingClause(DNPParser.ProcedureDivisionGivingClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#procedureDivisionGivingClause}.
	 * @param ctx the parse tree
	 */
	void exitProcedureDivisionGivingClause(DNPParser.ProcedureDivisionGivingClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#procedureDivisionUsingParameter}.
	 * @param ctx the parse tree
	 */
	void enterProcedureDivisionUsingParameter(DNPParser.ProcedureDivisionUsingParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#procedureDivisionUsingParameter}.
	 * @param ctx the parse tree
	 */
	void exitProcedureDivisionUsingParameter(DNPParser.ProcedureDivisionUsingParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#procedureDivisionByReferencePhrase}.
	 * @param ctx the parse tree
	 */
	void enterProcedureDivisionByReferencePhrase(DNPParser.ProcedureDivisionByReferencePhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#procedureDivisionByReferencePhrase}.
	 * @param ctx the parse tree
	 */
	void exitProcedureDivisionByReferencePhrase(DNPParser.ProcedureDivisionByReferencePhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#procedureDivisionByReference}.
	 * @param ctx the parse tree
	 */
	void enterProcedureDivisionByReference(DNPParser.ProcedureDivisionByReferenceContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#procedureDivisionByReference}.
	 * @param ctx the parse tree
	 */
	void exitProcedureDivisionByReference(DNPParser.ProcedureDivisionByReferenceContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#procedureDivisionByValuePhrase}.
	 * @param ctx the parse tree
	 */
	void enterProcedureDivisionByValuePhrase(DNPParser.ProcedureDivisionByValuePhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#procedureDivisionByValuePhrase}.
	 * @param ctx the parse tree
	 */
	void exitProcedureDivisionByValuePhrase(DNPParser.ProcedureDivisionByValuePhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#procedureDivisionByValue}.
	 * @param ctx the parse tree
	 */
	void enterProcedureDivisionByValue(DNPParser.ProcedureDivisionByValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#procedureDivisionByValue}.
	 * @param ctx the parse tree
	 */
	void exitProcedureDivisionByValue(DNPParser.ProcedureDivisionByValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#procedureDeclaratives}.
	 * @param ctx the parse tree
	 */
	void enterProcedureDeclaratives(DNPParser.ProcedureDeclarativesContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#procedureDeclaratives}.
	 * @param ctx the parse tree
	 */
	void exitProcedureDeclaratives(DNPParser.ProcedureDeclarativesContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#procedureDeclarative}.
	 * @param ctx the parse tree
	 */
	void enterProcedureDeclarative(DNPParser.ProcedureDeclarativeContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#procedureDeclarative}.
	 * @param ctx the parse tree
	 */
	void exitProcedureDeclarative(DNPParser.ProcedureDeclarativeContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#procedureSectionHeader}.
	 * @param ctx the parse tree
	 */
	void enterProcedureSectionHeader(DNPParser.ProcedureSectionHeaderContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#procedureSectionHeader}.
	 * @param ctx the parse tree
	 */
	void exitProcedureSectionHeader(DNPParser.ProcedureSectionHeaderContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#procedureDivisionBody}.
	 * @param ctx the parse tree
	 */
	void enterProcedureDivisionBody(DNPParser.ProcedureDivisionBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#procedureDivisionBody}.
	 * @param ctx the parse tree
	 */
	void exitProcedureDivisionBody(DNPParser.ProcedureDivisionBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#procedureSection}.
	 * @param ctx the parse tree
	 */
	void enterProcedureSection(DNPParser.ProcedureSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#procedureSection}.
	 * @param ctx the parse tree
	 */
	void exitProcedureSection(DNPParser.ProcedureSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#paragraphs}.
	 * @param ctx the parse tree
	 */
	void enterParagraphs(DNPParser.ParagraphsContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#paragraphs}.
	 * @param ctx the parse tree
	 */
	void exitParagraphs(DNPParser.ParagraphsContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#paragraph}.
	 * @param ctx the parse tree
	 */
	void enterParagraph(DNPParser.ParagraphContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#paragraph}.
	 * @param ctx the parse tree
	 */
	void exitParagraph(DNPParser.ParagraphContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#sentence}.
	 * @param ctx the parse tree
	 */
	void enterSentence(DNPParser.SentenceContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#sentence}.
	 * @param ctx the parse tree
	 */
	void exitSentence(DNPParser.SentenceContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(DNPParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(DNPParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#execCicsStatement2}.
	 * @param ctx the parse tree
	 */
	void enterExecCicsStatement2(DNPParser.ExecCicsStatement2Context ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#execCicsStatement2}.
	 * @param ctx the parse tree
	 */
	void exitExecCicsStatement2(DNPParser.ExecCicsStatement2Context ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#acceptStatement}.
	 * @param ctx the parse tree
	 */
	void enterAcceptStatement(DNPParser.AcceptStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#acceptStatement}.
	 * @param ctx the parse tree
	 */
	void exitAcceptStatement(DNPParser.AcceptStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#acceptFromDateStatement}.
	 * @param ctx the parse tree
	 */
	void enterAcceptFromDateStatement(DNPParser.AcceptFromDateStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#acceptFromDateStatement}.
	 * @param ctx the parse tree
	 */
	void exitAcceptFromDateStatement(DNPParser.AcceptFromDateStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#acceptFromDatePhrase}.
	 * @param ctx the parse tree
	 */
	void enterAcceptFromDatePhrase(DNPParser.AcceptFromDatePhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#acceptFromDatePhrase}.
	 * @param ctx the parse tree
	 */
	void exitAcceptFromDatePhrase(DNPParser.AcceptFromDatePhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#acceptFromMnemonicStatement}.
	 * @param ctx the parse tree
	 */
	void enterAcceptFromMnemonicStatement(DNPParser.AcceptFromMnemonicStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#acceptFromMnemonicStatement}.
	 * @param ctx the parse tree
	 */
	void exitAcceptFromMnemonicStatement(DNPParser.AcceptFromMnemonicStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#acceptFromEscapeKeyStatement}.
	 * @param ctx the parse tree
	 */
	void enterAcceptFromEscapeKeyStatement(DNPParser.AcceptFromEscapeKeyStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#acceptFromEscapeKeyStatement}.
	 * @param ctx the parse tree
	 */
	void exitAcceptFromEscapeKeyStatement(DNPParser.AcceptFromEscapeKeyStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#acceptMessageCountStatement}.
	 * @param ctx the parse tree
	 */
	void enterAcceptMessageCountStatement(DNPParser.AcceptMessageCountStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#acceptMessageCountStatement}.
	 * @param ctx the parse tree
	 */
	void exitAcceptMessageCountStatement(DNPParser.AcceptMessageCountStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#addStatement}.
	 * @param ctx the parse tree
	 */
	void enterAddStatement(DNPParser.AddStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#addStatement}.
	 * @param ctx the parse tree
	 */
	void exitAddStatement(DNPParser.AddStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#addToStatement}.
	 * @param ctx the parse tree
	 */
	void enterAddToStatement(DNPParser.AddToStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#addToStatement}.
	 * @param ctx the parse tree
	 */
	void exitAddToStatement(DNPParser.AddToStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#addToGivingStatement}.
	 * @param ctx the parse tree
	 */
	void enterAddToGivingStatement(DNPParser.AddToGivingStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#addToGivingStatement}.
	 * @param ctx the parse tree
	 */
	void exitAddToGivingStatement(DNPParser.AddToGivingStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#addCorrespondingStatement}.
	 * @param ctx the parse tree
	 */
	void enterAddCorrespondingStatement(DNPParser.AddCorrespondingStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#addCorrespondingStatement}.
	 * @param ctx the parse tree
	 */
	void exitAddCorrespondingStatement(DNPParser.AddCorrespondingStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#addFrom}.
	 * @param ctx the parse tree
	 */
	void enterAddFrom(DNPParser.AddFromContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#addFrom}.
	 * @param ctx the parse tree
	 */
	void exitAddFrom(DNPParser.AddFromContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#addTo}.
	 * @param ctx the parse tree
	 */
	void enterAddTo(DNPParser.AddToContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#addTo}.
	 * @param ctx the parse tree
	 */
	void exitAddTo(DNPParser.AddToContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#addToGiving}.
	 * @param ctx the parse tree
	 */
	void enterAddToGiving(DNPParser.AddToGivingContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#addToGiving}.
	 * @param ctx the parse tree
	 */
	void exitAddToGiving(DNPParser.AddToGivingContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#addGiving}.
	 * @param ctx the parse tree
	 */
	void enterAddGiving(DNPParser.AddGivingContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#addGiving}.
	 * @param ctx the parse tree
	 */
	void exitAddGiving(DNPParser.AddGivingContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#alteredGoTo}.
	 * @param ctx the parse tree
	 */
	void enterAlteredGoTo(DNPParser.AlteredGoToContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#alteredGoTo}.
	 * @param ctx the parse tree
	 */
	void exitAlteredGoTo(DNPParser.AlteredGoToContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#alterStatement}.
	 * @param ctx the parse tree
	 */
	void enterAlterStatement(DNPParser.AlterStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#alterStatement}.
	 * @param ctx the parse tree
	 */
	void exitAlterStatement(DNPParser.AlterStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#alterProceedTo}.
	 * @param ctx the parse tree
	 */
	void enterAlterProceedTo(DNPParser.AlterProceedToContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#alterProceedTo}.
	 * @param ctx the parse tree
	 */
	void exitAlterProceedTo(DNPParser.AlterProceedToContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#attachStatement}.
	 * @param ctx the parse tree
	 */
	void enterAttachStatement(DNPParser.AttachStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#attachStatement}.
	 * @param ctx the parse tree
	 */
	void exitAttachStatement(DNPParser.AttachStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#callStatement}.
	 * @param ctx the parse tree
	 */
	void enterCallStatement(DNPParser.CallStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#callStatement}.
	 * @param ctx the parse tree
	 */
	void exitCallStatement(DNPParser.CallStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#callUsingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterCallUsingPhrase(DNPParser.CallUsingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#callUsingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitCallUsingPhrase(DNPParser.CallUsingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#callUsingParameter}.
	 * @param ctx the parse tree
	 */
	void enterCallUsingParameter(DNPParser.CallUsingParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#callUsingParameter}.
	 * @param ctx the parse tree
	 */
	void exitCallUsingParameter(DNPParser.CallUsingParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#callByReferencePhrase}.
	 * @param ctx the parse tree
	 */
	void enterCallByReferencePhrase(DNPParser.CallByReferencePhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#callByReferencePhrase}.
	 * @param ctx the parse tree
	 */
	void exitCallByReferencePhrase(DNPParser.CallByReferencePhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#callByReference}.
	 * @param ctx the parse tree
	 */
	void enterCallByReference(DNPParser.CallByReferenceContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#callByReference}.
	 * @param ctx the parse tree
	 */
	void exitCallByReference(DNPParser.CallByReferenceContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#callByValuePhrase}.
	 * @param ctx the parse tree
	 */
	void enterCallByValuePhrase(DNPParser.CallByValuePhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#callByValuePhrase}.
	 * @param ctx the parse tree
	 */
	void exitCallByValuePhrase(DNPParser.CallByValuePhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#callByValue}.
	 * @param ctx the parse tree
	 */
	void enterCallByValue(DNPParser.CallByValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#callByValue}.
	 * @param ctx the parse tree
	 */
	void exitCallByValue(DNPParser.CallByValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#callByContentPhrase}.
	 * @param ctx the parse tree
	 */
	void enterCallByContentPhrase(DNPParser.CallByContentPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#callByContentPhrase}.
	 * @param ctx the parse tree
	 */
	void exitCallByContentPhrase(DNPParser.CallByContentPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#callByContent}.
	 * @param ctx the parse tree
	 */
	void enterCallByContent(DNPParser.CallByContentContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#callByContent}.
	 * @param ctx the parse tree
	 */
	void exitCallByContent(DNPParser.CallByContentContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#callGivingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterCallGivingPhrase(DNPParser.CallGivingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#callGivingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitCallGivingPhrase(DNPParser.CallGivingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#callSystem}.
	 * @param ctx the parse tree
	 */
	void enterCallSystem(DNPParser.CallSystemContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#callSystem}.
	 * @param ctx the parse tree
	 */
	void exitCallSystem(DNPParser.CallSystemContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#cancelStatement}.
	 * @param ctx the parse tree
	 */
	void enterCancelStatement(DNPParser.CancelStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#cancelStatement}.
	 * @param ctx the parse tree
	 */
	void exitCancelStatement(DNPParser.CancelStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#cancelCall}.
	 * @param ctx the parse tree
	 */
	void enterCancelCall(DNPParser.CancelCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#cancelCall}.
	 * @param ctx the parse tree
	 */
	void exitCancelCall(DNPParser.CancelCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#closeStatement}.
	 * @param ctx the parse tree
	 */
	void enterCloseStatement(DNPParser.CloseStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#closeStatement}.
	 * @param ctx the parse tree
	 */
	void exitCloseStatement(DNPParser.CloseStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#closePhrase}.
	 * @param ctx the parse tree
	 */
	void enterClosePhrase(DNPParser.ClosePhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#closePhrase}.
	 * @param ctx the parse tree
	 */
	void exitClosePhrase(DNPParser.ClosePhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#closeFile}.
	 * @param ctx the parse tree
	 */
	void enterCloseFile(DNPParser.CloseFileContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#closeFile}.
	 * @param ctx the parse tree
	 */
	void exitCloseFile(DNPParser.CloseFileContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#closeReelUnitStatement}.
	 * @param ctx the parse tree
	 */
	void enterCloseReelUnitStatement(DNPParser.CloseReelUnitStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#closeReelUnitStatement}.
	 * @param ctx the parse tree
	 */
	void exitCloseReelUnitStatement(DNPParser.CloseReelUnitStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#closeRelativeStatement}.
	 * @param ctx the parse tree
	 */
	void enterCloseRelativeStatement(DNPParser.CloseRelativeStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#closeRelativeStatement}.
	 * @param ctx the parse tree
	 */
	void exitCloseRelativeStatement(DNPParser.CloseRelativeStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#closePortFileIOStatement}.
	 * @param ctx the parse tree
	 */
	void enterClosePortFileIOStatement(DNPParser.ClosePortFileIOStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#closePortFileIOStatement}.
	 * @param ctx the parse tree
	 */
	void exitClosePortFileIOStatement(DNPParser.ClosePortFileIOStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#closePortFileIOUsing}.
	 * @param ctx the parse tree
	 */
	void enterClosePortFileIOUsing(DNPParser.ClosePortFileIOUsingContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#closePortFileIOUsing}.
	 * @param ctx the parse tree
	 */
	void exitClosePortFileIOUsing(DNPParser.ClosePortFileIOUsingContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#closePortFileIOUsingCloseDisposition}.
	 * @param ctx the parse tree
	 */
	void enterClosePortFileIOUsingCloseDisposition(DNPParser.ClosePortFileIOUsingCloseDispositionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#closePortFileIOUsingCloseDisposition}.
	 * @param ctx the parse tree
	 */
	void exitClosePortFileIOUsingCloseDisposition(DNPParser.ClosePortFileIOUsingCloseDispositionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#closePortFileIOUsingAssociatedData}.
	 * @param ctx the parse tree
	 */
	void enterClosePortFileIOUsingAssociatedData(DNPParser.ClosePortFileIOUsingAssociatedDataContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#closePortFileIOUsingAssociatedData}.
	 * @param ctx the parse tree
	 */
	void exitClosePortFileIOUsingAssociatedData(DNPParser.ClosePortFileIOUsingAssociatedDataContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#closePortFileIOUsingAssociatedDataLength}.
	 * @param ctx the parse tree
	 */
	void enterClosePortFileIOUsingAssociatedDataLength(DNPParser.ClosePortFileIOUsingAssociatedDataLengthContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#closePortFileIOUsingAssociatedDataLength}.
	 * @param ctx the parse tree
	 */
	void exitClosePortFileIOUsingAssociatedDataLength(DNPParser.ClosePortFileIOUsingAssociatedDataLengthContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#computeStatement}.
	 * @param ctx the parse tree
	 */
	void enterComputeStatement(DNPParser.ComputeStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#computeStatement}.
	 * @param ctx the parse tree
	 */
	void exitComputeStatement(DNPParser.ComputeStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#computeStore}.
	 * @param ctx the parse tree
	 */
	void enterComputeStore(DNPParser.ComputeStoreContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#computeStore}.
	 * @param ctx the parse tree
	 */
	void exitComputeStore(DNPParser.ComputeStoreContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#continueStatement}.
	 * @param ctx the parse tree
	 */
	void enterContinueStatement(DNPParser.ContinueStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#continueStatement}.
	 * @param ctx the parse tree
	 */
	void exitContinueStatement(DNPParser.ContinueStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#continueIndicator}.
	 * @param ctx the parse tree
	 */
	void enterContinueIndicator(DNPParser.ContinueIndicatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#continueIndicator}.
	 * @param ctx the parse tree
	 */
	void exitContinueIndicator(DNPParser.ContinueIndicatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#deleteStatement}.
	 * @param ctx the parse tree
	 */
	void enterDeleteStatement(DNPParser.DeleteStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#deleteStatement}.
	 * @param ctx the parse tree
	 */
	void exitDeleteStatement(DNPParser.DeleteStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#disableStatement}.
	 * @param ctx the parse tree
	 */
	void enterDisableStatement(DNPParser.DisableStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#disableStatement}.
	 * @param ctx the parse tree
	 */
	void exitDisableStatement(DNPParser.DisableStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#displayStatement}.
	 * @param ctx the parse tree
	 */
	void enterDisplayStatement(DNPParser.DisplayStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#displayStatement}.
	 * @param ctx the parse tree
	 */
	void exitDisplayStatement(DNPParser.DisplayStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#displayOperand}.
	 * @param ctx the parse tree
	 */
	void enterDisplayOperand(DNPParser.DisplayOperandContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#displayOperand}.
	 * @param ctx the parse tree
	 */
	void exitDisplayOperand(DNPParser.DisplayOperandContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#displayAt}.
	 * @param ctx the parse tree
	 */
	void enterDisplayAt(DNPParser.DisplayAtContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#displayAt}.
	 * @param ctx the parse tree
	 */
	void exitDisplayAt(DNPParser.DisplayAtContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#displayUpon}.
	 * @param ctx the parse tree
	 */
	void enterDisplayUpon(DNPParser.DisplayUponContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#displayUpon}.
	 * @param ctx the parse tree
	 */
	void exitDisplayUpon(DNPParser.DisplayUponContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#displayWith}.
	 * @param ctx the parse tree
	 */
	void enterDisplayWith(DNPParser.DisplayWithContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#displayWith}.
	 * @param ctx the parse tree
	 */
	void exitDisplayWith(DNPParser.DisplayWithContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#divideStatement}.
	 * @param ctx the parse tree
	 */
	void enterDivideStatement(DNPParser.DivideStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#divideStatement}.
	 * @param ctx the parse tree
	 */
	void exitDivideStatement(DNPParser.DivideStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#divideIntoStatement}.
	 * @param ctx the parse tree
	 */
	void enterDivideIntoStatement(DNPParser.DivideIntoStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#divideIntoStatement}.
	 * @param ctx the parse tree
	 */
	void exitDivideIntoStatement(DNPParser.DivideIntoStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#divideIntoGivingStatement}.
	 * @param ctx the parse tree
	 */
	void enterDivideIntoGivingStatement(DNPParser.DivideIntoGivingStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#divideIntoGivingStatement}.
	 * @param ctx the parse tree
	 */
	void exitDivideIntoGivingStatement(DNPParser.DivideIntoGivingStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#divideByGivingStatement}.
	 * @param ctx the parse tree
	 */
	void enterDivideByGivingStatement(DNPParser.DivideByGivingStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#divideByGivingStatement}.
	 * @param ctx the parse tree
	 */
	void exitDivideByGivingStatement(DNPParser.DivideByGivingStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#divideGivingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterDivideGivingPhrase(DNPParser.DivideGivingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#divideGivingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitDivideGivingPhrase(DNPParser.DivideGivingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#divideInto}.
	 * @param ctx the parse tree
	 */
	void enterDivideInto(DNPParser.DivideIntoContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#divideInto}.
	 * @param ctx the parse tree
	 */
	void exitDivideInto(DNPParser.DivideIntoContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#divideGiving}.
	 * @param ctx the parse tree
	 */
	void enterDivideGiving(DNPParser.DivideGivingContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#divideGiving}.
	 * @param ctx the parse tree
	 */
	void exitDivideGiving(DNPParser.DivideGivingContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#divideRemainder}.
	 * @param ctx the parse tree
	 */
	void enterDivideRemainder(DNPParser.DivideRemainderContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#divideRemainder}.
	 * @param ctx the parse tree
	 */
	void exitDivideRemainder(DNPParser.DivideRemainderContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#enableStatement}.
	 * @param ctx the parse tree
	 */
	void enterEnableStatement(DNPParser.EnableStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#enableStatement}.
	 * @param ctx the parse tree
	 */
	void exitEnableStatement(DNPParser.EnableStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#entryStatement}.
	 * @param ctx the parse tree
	 */
	void enterEntryStatement(DNPParser.EntryStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#entryStatement}.
	 * @param ctx the parse tree
	 */
	void exitEntryStatement(DNPParser.EntryStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#evaluateStatement}.
	 * @param ctx the parse tree
	 */
	void enterEvaluateStatement(DNPParser.EvaluateStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#evaluateStatement}.
	 * @param ctx the parse tree
	 */
	void exitEvaluateStatement(DNPParser.EvaluateStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#evaluateSelect}.
	 * @param ctx the parse tree
	 */
	void enterEvaluateSelect(DNPParser.EvaluateSelectContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#evaluateSelect}.
	 * @param ctx the parse tree
	 */
	void exitEvaluateSelect(DNPParser.EvaluateSelectContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#evaluateAlsoSelect}.
	 * @param ctx the parse tree
	 */
	void enterEvaluateAlsoSelect(DNPParser.EvaluateAlsoSelectContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#evaluateAlsoSelect}.
	 * @param ctx the parse tree
	 */
	void exitEvaluateAlsoSelect(DNPParser.EvaluateAlsoSelectContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#evaluateWhenPhrase}.
	 * @param ctx the parse tree
	 */
	void enterEvaluateWhenPhrase(DNPParser.EvaluateWhenPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#evaluateWhenPhrase}.
	 * @param ctx the parse tree
	 */
	void exitEvaluateWhenPhrase(DNPParser.EvaluateWhenPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#evaluateWhen}.
	 * @param ctx the parse tree
	 */
	void enterEvaluateWhen(DNPParser.EvaluateWhenContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#evaluateWhen}.
	 * @param ctx the parse tree
	 */
	void exitEvaluateWhen(DNPParser.EvaluateWhenContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#evaluateCondition}.
	 * @param ctx the parse tree
	 */
	void enterEvaluateCondition(DNPParser.EvaluateConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#evaluateCondition}.
	 * @param ctx the parse tree
	 */
	void exitEvaluateCondition(DNPParser.EvaluateConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#evaluateThrough}.
	 * @param ctx the parse tree
	 */
	void enterEvaluateThrough(DNPParser.EvaluateThroughContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#evaluateThrough}.
	 * @param ctx the parse tree
	 */
	void exitEvaluateThrough(DNPParser.EvaluateThroughContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#evaluateAlsoCondition}.
	 * @param ctx the parse tree
	 */
	void enterEvaluateAlsoCondition(DNPParser.EvaluateAlsoConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#evaluateAlsoCondition}.
	 * @param ctx the parse tree
	 */
	void exitEvaluateAlsoCondition(DNPParser.EvaluateAlsoConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#evaluateWhenOther}.
	 * @param ctx the parse tree
	 */
	void enterEvaluateWhenOther(DNPParser.EvaluateWhenOtherContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#evaluateWhenOther}.
	 * @param ctx the parse tree
	 */
	void exitEvaluateWhenOther(DNPParser.EvaluateWhenOtherContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#evaluateValue}.
	 * @param ctx the parse tree
	 */
	void enterEvaluateValue(DNPParser.EvaluateValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#evaluateValue}.
	 * @param ctx the parse tree
	 */
	void exitEvaluateValue(DNPParser.EvaluateValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#execCicsStatement}.
	 * @param ctx the parse tree
	 */
	void enterExecCicsStatement(DNPParser.ExecCicsStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#execCicsStatement}.
	 * @param ctx the parse tree
	 */
	void exitExecCicsStatement(DNPParser.ExecCicsStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#execSqlStatement}.
	 * @param ctx the parse tree
	 */
	void enterExecSqlStatement(DNPParser.ExecSqlStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#execSqlStatement}.
	 * @param ctx the parse tree
	 */
	void exitExecSqlStatement(DNPParser.ExecSqlStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#execSqlImsStatement}.
	 * @param ctx the parse tree
	 */
	void enterExecSqlImsStatement(DNPParser.ExecSqlImsStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#execSqlImsStatement}.
	 * @param ctx the parse tree
	 */
	void exitExecSqlImsStatement(DNPParser.ExecSqlImsStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#exhibitStatement}.
	 * @param ctx the parse tree
	 */
	void enterExhibitStatement(DNPParser.ExhibitStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#exhibitStatement}.
	 * @param ctx the parse tree
	 */
	void exitExhibitStatement(DNPParser.ExhibitStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#exhibitOperand}.
	 * @param ctx the parse tree
	 */
	void enterExhibitOperand(DNPParser.ExhibitOperandContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#exhibitOperand}.
	 * @param ctx the parse tree
	 */
	void exitExhibitOperand(DNPParser.ExhibitOperandContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#exitStatement}.
	 * @param ctx the parse tree
	 */
	void enterExitStatement(DNPParser.ExitStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#exitStatement}.
	 * @param ctx the parse tree
	 */
	void exitExitStatement(DNPParser.ExitStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#findStatement}.
	 * @param ctx the parse tree
	 */
	void enterFindStatement(DNPParser.FindStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#findStatement}.
	 * @param ctx the parse tree
	 */
	void exitFindStatement(DNPParser.FindStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#viaClause}.
	 * @param ctx the parse tree
	 */
	void enterViaClause(DNPParser.ViaClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#viaClause}.
	 * @param ctx the parse tree
	 */
	void exitViaClause(DNPParser.ViaClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#findOption}.
	 * @param ctx the parse tree
	 */
	void enterFindOption(DNPParser.FindOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#findOption}.
	 * @param ctx the parse tree
	 */
	void exitFindOption(DNPParser.FindOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#freeStatement}.
	 * @param ctx the parse tree
	 */
	void enterFreeStatement(DNPParser.FreeStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#freeStatement}.
	 * @param ctx the parse tree
	 */
	void exitFreeStatement(DNPParser.FreeStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#generateStatement}.
	 * @param ctx the parse tree
	 */
	void enterGenerateStatement(DNPParser.GenerateStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#generateStatement}.
	 * @param ctx the parse tree
	 */
	void exitGenerateStatement(DNPParser.GenerateStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#gobackStatement}.
	 * @param ctx the parse tree
	 */
	void enterGobackStatement(DNPParser.GobackStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#gobackStatement}.
	 * @param ctx the parse tree
	 */
	void exitGobackStatement(DNPParser.GobackStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#goToStatement}.
	 * @param ctx the parse tree
	 */
	void enterGoToStatement(DNPParser.GoToStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#goToStatement}.
	 * @param ctx the parse tree
	 */
	void exitGoToStatement(DNPParser.GoToStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#goToStatementSimple}.
	 * @param ctx the parse tree
	 */
	void enterGoToStatementSimple(DNPParser.GoToStatementSimpleContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#goToStatementSimple}.
	 * @param ctx the parse tree
	 */
	void exitGoToStatementSimple(DNPParser.GoToStatementSimpleContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#goToDependingOnStatement}.
	 * @param ctx the parse tree
	 */
	void enterGoToDependingOnStatement(DNPParser.GoToDependingOnStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#goToDependingOnStatement}.
	 * @param ctx the parse tree
	 */
	void exitGoToDependingOnStatement(DNPParser.GoToDependingOnStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(DNPParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(DNPParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#ifThen}.
	 * @param ctx the parse tree
	 */
	void enterIfThen(DNPParser.IfThenContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#ifThen}.
	 * @param ctx the parse tree
	 */
	void exitIfThen(DNPParser.IfThenContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#ifElse}.
	 * @param ctx the parse tree
	 */
	void enterIfElse(DNPParser.IfElseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#ifElse}.
	 * @param ctx the parse tree
	 */
	void exitIfElse(DNPParser.IfElseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#initializeStatement}.
	 * @param ctx the parse tree
	 */
	void enterInitializeStatement(DNPParser.InitializeStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#initializeStatement}.
	 * @param ctx the parse tree
	 */
	void exitInitializeStatement(DNPParser.InitializeStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#initializeReplacingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterInitializeReplacingPhrase(DNPParser.InitializeReplacingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#initializeReplacingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitInitializeReplacingPhrase(DNPParser.InitializeReplacingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#initializeReplacingBy}.
	 * @param ctx the parse tree
	 */
	void enterInitializeReplacingBy(DNPParser.InitializeReplacingByContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#initializeReplacingBy}.
	 * @param ctx the parse tree
	 */
	void exitInitializeReplacingBy(DNPParser.InitializeReplacingByContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#initiateStatement}.
	 * @param ctx the parse tree
	 */
	void enterInitiateStatement(DNPParser.InitiateStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#initiateStatement}.
	 * @param ctx the parse tree
	 */
	void exitInitiateStatement(DNPParser.InitiateStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#inspectStatement}.
	 * @param ctx the parse tree
	 */
	void enterInspectStatement(DNPParser.InspectStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#inspectStatement}.
	 * @param ctx the parse tree
	 */
	void exitInspectStatement(DNPParser.InspectStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#inspectTallyingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterInspectTallyingPhrase(DNPParser.InspectTallyingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#inspectTallyingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitInspectTallyingPhrase(DNPParser.InspectTallyingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#inspectReplacingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterInspectReplacingPhrase(DNPParser.InspectReplacingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#inspectReplacingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitInspectReplacingPhrase(DNPParser.InspectReplacingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#inspectTallyingReplacingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterInspectTallyingReplacingPhrase(DNPParser.InspectTallyingReplacingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#inspectTallyingReplacingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitInspectTallyingReplacingPhrase(DNPParser.InspectTallyingReplacingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#inspectConvertingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterInspectConvertingPhrase(DNPParser.InspectConvertingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#inspectConvertingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitInspectConvertingPhrase(DNPParser.InspectConvertingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#inspectFor}.
	 * @param ctx the parse tree
	 */
	void enterInspectFor(DNPParser.InspectForContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#inspectFor}.
	 * @param ctx the parse tree
	 */
	void exitInspectFor(DNPParser.InspectForContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#inspectCharacters}.
	 * @param ctx the parse tree
	 */
	void enterInspectCharacters(DNPParser.InspectCharactersContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#inspectCharacters}.
	 * @param ctx the parse tree
	 */
	void exitInspectCharacters(DNPParser.InspectCharactersContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#inspectReplacingCharacters}.
	 * @param ctx the parse tree
	 */
	void enterInspectReplacingCharacters(DNPParser.InspectReplacingCharactersContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#inspectReplacingCharacters}.
	 * @param ctx the parse tree
	 */
	void exitInspectReplacingCharacters(DNPParser.InspectReplacingCharactersContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#inspectAllLeadings}.
	 * @param ctx the parse tree
	 */
	void enterInspectAllLeadings(DNPParser.InspectAllLeadingsContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#inspectAllLeadings}.
	 * @param ctx the parse tree
	 */
	void exitInspectAllLeadings(DNPParser.InspectAllLeadingsContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#inspectReplacingAllLeadings}.
	 * @param ctx the parse tree
	 */
	void enterInspectReplacingAllLeadings(DNPParser.InspectReplacingAllLeadingsContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#inspectReplacingAllLeadings}.
	 * @param ctx the parse tree
	 */
	void exitInspectReplacingAllLeadings(DNPParser.InspectReplacingAllLeadingsContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#inspectAllLeading}.
	 * @param ctx the parse tree
	 */
	void enterInspectAllLeading(DNPParser.InspectAllLeadingContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#inspectAllLeading}.
	 * @param ctx the parse tree
	 */
	void exitInspectAllLeading(DNPParser.InspectAllLeadingContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#inspectReplacingAllLeading}.
	 * @param ctx the parse tree
	 */
	void enterInspectReplacingAllLeading(DNPParser.InspectReplacingAllLeadingContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#inspectReplacingAllLeading}.
	 * @param ctx the parse tree
	 */
	void exitInspectReplacingAllLeading(DNPParser.InspectReplacingAllLeadingContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#inspectBy}.
	 * @param ctx the parse tree
	 */
	void enterInspectBy(DNPParser.InspectByContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#inspectBy}.
	 * @param ctx the parse tree
	 */
	void exitInspectBy(DNPParser.InspectByContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#inspectTo}.
	 * @param ctx the parse tree
	 */
	void enterInspectTo(DNPParser.InspectToContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#inspectTo}.
	 * @param ctx the parse tree
	 */
	void exitInspectTo(DNPParser.InspectToContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#inspectBeforeAfter}.
	 * @param ctx the parse tree
	 */
	void enterInspectBeforeAfter(DNPParser.InspectBeforeAfterContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#inspectBeforeAfter}.
	 * @param ctx the parse tree
	 */
	void exitInspectBeforeAfter(DNPParser.InspectBeforeAfterContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#lockStatement}.
	 * @param ctx the parse tree
	 */
	void enterLockStatement(DNPParser.LockStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#lockStatement}.
	 * @param ctx the parse tree
	 */
	void exitLockStatement(DNPParser.LockStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#mergeStatement}.
	 * @param ctx the parse tree
	 */
	void enterMergeStatement(DNPParser.MergeStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#mergeStatement}.
	 * @param ctx the parse tree
	 */
	void exitMergeStatement(DNPParser.MergeStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#mergeOnKeyClause}.
	 * @param ctx the parse tree
	 */
	void enterMergeOnKeyClause(DNPParser.MergeOnKeyClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#mergeOnKeyClause}.
	 * @param ctx the parse tree
	 */
	void exitMergeOnKeyClause(DNPParser.MergeOnKeyClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#mergeCollatingSequencePhrase}.
	 * @param ctx the parse tree
	 */
	void enterMergeCollatingSequencePhrase(DNPParser.MergeCollatingSequencePhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#mergeCollatingSequencePhrase}.
	 * @param ctx the parse tree
	 */
	void exitMergeCollatingSequencePhrase(DNPParser.MergeCollatingSequencePhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#mergeCollatingAlphanumeric}.
	 * @param ctx the parse tree
	 */
	void enterMergeCollatingAlphanumeric(DNPParser.MergeCollatingAlphanumericContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#mergeCollatingAlphanumeric}.
	 * @param ctx the parse tree
	 */
	void exitMergeCollatingAlphanumeric(DNPParser.MergeCollatingAlphanumericContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#mergeCollatingNational}.
	 * @param ctx the parse tree
	 */
	void enterMergeCollatingNational(DNPParser.MergeCollatingNationalContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#mergeCollatingNational}.
	 * @param ctx the parse tree
	 */
	void exitMergeCollatingNational(DNPParser.MergeCollatingNationalContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#mergeUsing}.
	 * @param ctx the parse tree
	 */
	void enterMergeUsing(DNPParser.MergeUsingContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#mergeUsing}.
	 * @param ctx the parse tree
	 */
	void exitMergeUsing(DNPParser.MergeUsingContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#mergeOutputProcedurePhrase}.
	 * @param ctx the parse tree
	 */
	void enterMergeOutputProcedurePhrase(DNPParser.MergeOutputProcedurePhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#mergeOutputProcedurePhrase}.
	 * @param ctx the parse tree
	 */
	void exitMergeOutputProcedurePhrase(DNPParser.MergeOutputProcedurePhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#mergeOutputThrough}.
	 * @param ctx the parse tree
	 */
	void enterMergeOutputThrough(DNPParser.MergeOutputThroughContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#mergeOutputThrough}.
	 * @param ctx the parse tree
	 */
	void exitMergeOutputThrough(DNPParser.MergeOutputThroughContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#mergeGivingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterMergeGivingPhrase(DNPParser.MergeGivingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#mergeGivingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitMergeGivingPhrase(DNPParser.MergeGivingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#mergeGiving}.
	 * @param ctx the parse tree
	 */
	void enterMergeGiving(DNPParser.MergeGivingContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#mergeGiving}.
	 * @param ctx the parse tree
	 */
	void exitMergeGiving(DNPParser.MergeGivingContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#moveStatement}.
	 * @param ctx the parse tree
	 */
	void enterMoveStatement(DNPParser.MoveStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#moveStatement}.
	 * @param ctx the parse tree
	 */
	void exitMoveStatement(DNPParser.MoveStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#moveToStatement}.
	 * @param ctx the parse tree
	 */
	void enterMoveToStatement(DNPParser.MoveToStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#moveToStatement}.
	 * @param ctx the parse tree
	 */
	void exitMoveToStatement(DNPParser.MoveToStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#moveToSendingArea}.
	 * @param ctx the parse tree
	 */
	void enterMoveToSendingArea(DNPParser.MoveToSendingAreaContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#moveToSendingArea}.
	 * @param ctx the parse tree
	 */
	void exitMoveToSendingArea(DNPParser.MoveToSendingAreaContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#moveCorrespondingToStatement}.
	 * @param ctx the parse tree
	 */
	void enterMoveCorrespondingToStatement(DNPParser.MoveCorrespondingToStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#moveCorrespondingToStatement}.
	 * @param ctx the parse tree
	 */
	void exitMoveCorrespondingToStatement(DNPParser.MoveCorrespondingToStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#moveCorrespondingToSendingArea}.
	 * @param ctx the parse tree
	 */
	void enterMoveCorrespondingToSendingArea(DNPParser.MoveCorrespondingToSendingAreaContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#moveCorrespondingToSendingArea}.
	 * @param ctx the parse tree
	 */
	void exitMoveCorrespondingToSendingArea(DNPParser.MoveCorrespondingToSendingAreaContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#moveAttributeClause}.
	 * @param ctx the parse tree
	 */
	void enterMoveAttributeClause(DNPParser.MoveAttributeClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#moveAttributeClause}.
	 * @param ctx the parse tree
	 */
	void exitMoveAttributeClause(DNPParser.MoveAttributeClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#modifyStatement}.
	 * @param ctx the parse tree
	 */
	void enterModifyStatement(DNPParser.ModifyStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#modifyStatement}.
	 * @param ctx the parse tree
	 */
	void exitModifyStatement(DNPParser.ModifyStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#modifyTo}.
	 * @param ctx the parse tree
	 */
	void enterModifyTo(DNPParser.ModifyToContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#modifyTo}.
	 * @param ctx the parse tree
	 */
	void exitModifyTo(DNPParser.ModifyToContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#modifyOption}.
	 * @param ctx the parse tree
	 */
	void enterModifyOption(DNPParser.ModifyOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#modifyOption}.
	 * @param ctx the parse tree
	 */
	void exitModifyOption(DNPParser.ModifyOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#multiplyStatement}.
	 * @param ctx the parse tree
	 */
	void enterMultiplyStatement(DNPParser.MultiplyStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#multiplyStatement}.
	 * @param ctx the parse tree
	 */
	void exitMultiplyStatement(DNPParser.MultiplyStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#multiplyRegular}.
	 * @param ctx the parse tree
	 */
	void enterMultiplyRegular(DNPParser.MultiplyRegularContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#multiplyRegular}.
	 * @param ctx the parse tree
	 */
	void exitMultiplyRegular(DNPParser.MultiplyRegularContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#multiplyRegularOperand}.
	 * @param ctx the parse tree
	 */
	void enterMultiplyRegularOperand(DNPParser.MultiplyRegularOperandContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#multiplyRegularOperand}.
	 * @param ctx the parse tree
	 */
	void exitMultiplyRegularOperand(DNPParser.MultiplyRegularOperandContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#multiplyGiving}.
	 * @param ctx the parse tree
	 */
	void enterMultiplyGiving(DNPParser.MultiplyGivingContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#multiplyGiving}.
	 * @param ctx the parse tree
	 */
	void exitMultiplyGiving(DNPParser.MultiplyGivingContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#multiplyGivingOperand}.
	 * @param ctx the parse tree
	 */
	void enterMultiplyGivingOperand(DNPParser.MultiplyGivingOperandContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#multiplyGivingOperand}.
	 * @param ctx the parse tree
	 */
	void exitMultiplyGivingOperand(DNPParser.MultiplyGivingOperandContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#multiplyGivingResult}.
	 * @param ctx the parse tree
	 */
	void enterMultiplyGivingResult(DNPParser.MultiplyGivingResultContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#multiplyGivingResult}.
	 * @param ctx the parse tree
	 */
	void exitMultiplyGivingResult(DNPParser.MultiplyGivingResultContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#openStatement}.
	 * @param ctx the parse tree
	 */
	void enterOpenStatement(DNPParser.OpenStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#openStatement}.
	 * @param ctx the parse tree
	 */
	void exitOpenStatement(DNPParser.OpenStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#openInputStatement}.
	 * @param ctx the parse tree
	 */
	void enterOpenInputStatement(DNPParser.OpenInputStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#openInputStatement}.
	 * @param ctx the parse tree
	 */
	void exitOpenInputStatement(DNPParser.OpenInputStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#openInput}.
	 * @param ctx the parse tree
	 */
	void enterOpenInput(DNPParser.OpenInputContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#openInput}.
	 * @param ctx the parse tree
	 */
	void exitOpenInput(DNPParser.OpenInputContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#openUpdateStatement}.
	 * @param ctx the parse tree
	 */
	void enterOpenUpdateStatement(DNPParser.OpenUpdateStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#openUpdateStatement}.
	 * @param ctx the parse tree
	 */
	void exitOpenUpdateStatement(DNPParser.OpenUpdateStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#openOutputStatement}.
	 * @param ctx the parse tree
	 */
	void enterOpenOutputStatement(DNPParser.OpenOutputStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#openOutputStatement}.
	 * @param ctx the parse tree
	 */
	void exitOpenOutputStatement(DNPParser.OpenOutputStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#openOutput}.
	 * @param ctx the parse tree
	 */
	void enterOpenOutput(DNPParser.OpenOutputContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#openOutput}.
	 * @param ctx the parse tree
	 */
	void exitOpenOutput(DNPParser.OpenOutputContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#openIOStatement}.
	 * @param ctx the parse tree
	 */
	void enterOpenIOStatement(DNPParser.OpenIOStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#openIOStatement}.
	 * @param ctx the parse tree
	 */
	void exitOpenIOStatement(DNPParser.OpenIOStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#openInquiry}.
	 * @param ctx the parse tree
	 */
	void enterOpenInquiry(DNPParser.OpenInquiryContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#openInquiry}.
	 * @param ctx the parse tree
	 */
	void exitOpenInquiry(DNPParser.OpenInquiryContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#openExtendStatement}.
	 * @param ctx the parse tree
	 */
	void enterOpenExtendStatement(DNPParser.OpenExtendStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#openExtendStatement}.
	 * @param ctx the parse tree
	 */
	void exitOpenExtendStatement(DNPParser.OpenExtendStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#performStatement}.
	 * @param ctx the parse tree
	 */
	void enterPerformStatement(DNPParser.PerformStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#performStatement}.
	 * @param ctx the parse tree
	 */
	void exitPerformStatement(DNPParser.PerformStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#performInlineStatement}.
	 * @param ctx the parse tree
	 */
	void enterPerformInlineStatement(DNPParser.PerformInlineStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#performInlineStatement}.
	 * @param ctx the parse tree
	 */
	void exitPerformInlineStatement(DNPParser.PerformInlineStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#performProcedureStatement}.
	 * @param ctx the parse tree
	 */
	void enterPerformProcedureStatement(DNPParser.PerformProcedureStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#performProcedureStatement}.
	 * @param ctx the parse tree
	 */
	void exitPerformProcedureStatement(DNPParser.PerformProcedureStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#performType}.
	 * @param ctx the parse tree
	 */
	void enterPerformType(DNPParser.PerformTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#performType}.
	 * @param ctx the parse tree
	 */
	void exitPerformType(DNPParser.PerformTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#performTimes}.
	 * @param ctx the parse tree
	 */
	void enterPerformTimes(DNPParser.PerformTimesContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#performTimes}.
	 * @param ctx the parse tree
	 */
	void exitPerformTimes(DNPParser.PerformTimesContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#performUntil}.
	 * @param ctx the parse tree
	 */
	void enterPerformUntil(DNPParser.PerformUntilContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#performUntil}.
	 * @param ctx the parse tree
	 */
	void exitPerformUntil(DNPParser.PerformUntilContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#performVarying}.
	 * @param ctx the parse tree
	 */
	void enterPerformVarying(DNPParser.PerformVaryingContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#performVarying}.
	 * @param ctx the parse tree
	 */
	void exitPerformVarying(DNPParser.PerformVaryingContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#performVaryingClause}.
	 * @param ctx the parse tree
	 */
	void enterPerformVaryingClause(DNPParser.PerformVaryingClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#performVaryingClause}.
	 * @param ctx the parse tree
	 */
	void exitPerformVaryingClause(DNPParser.PerformVaryingClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#performVaryingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterPerformVaryingPhrase(DNPParser.PerformVaryingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#performVaryingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitPerformVaryingPhrase(DNPParser.PerformVaryingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#performAfter}.
	 * @param ctx the parse tree
	 */
	void enterPerformAfter(DNPParser.PerformAfterContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#performAfter}.
	 * @param ctx the parse tree
	 */
	void exitPerformAfter(DNPParser.PerformAfterContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#performFrom}.
	 * @param ctx the parse tree
	 */
	void enterPerformFrom(DNPParser.PerformFromContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#performFrom}.
	 * @param ctx the parse tree
	 */
	void exitPerformFrom(DNPParser.PerformFromContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#performBy}.
	 * @param ctx the parse tree
	 */
	void enterPerformBy(DNPParser.PerformByContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#performBy}.
	 * @param ctx the parse tree
	 */
	void exitPerformBy(DNPParser.PerformByContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#performTestClause}.
	 * @param ctx the parse tree
	 */
	void enterPerformTestClause(DNPParser.PerformTestClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#performTestClause}.
	 * @param ctx the parse tree
	 */
	void exitPerformTestClause(DNPParser.PerformTestClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#purgeStatement}.
	 * @param ctx the parse tree
	 */
	void enterPurgeStatement(DNPParser.PurgeStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#purgeStatement}.
	 * @param ctx the parse tree
	 */
	void exitPurgeStatement(DNPParser.PurgeStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#readStatement}.
	 * @param ctx the parse tree
	 */
	void enterReadStatement(DNPParser.ReadStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#readStatement}.
	 * @param ctx the parse tree
	 */
	void exitReadStatement(DNPParser.ReadStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#readInto}.
	 * @param ctx the parse tree
	 */
	void enterReadInto(DNPParser.ReadIntoContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#readInto}.
	 * @param ctx the parse tree
	 */
	void exitReadInto(DNPParser.ReadIntoContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#readWith}.
	 * @param ctx the parse tree
	 */
	void enterReadWith(DNPParser.ReadWithContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#readWith}.
	 * @param ctx the parse tree
	 */
	void exitReadWith(DNPParser.ReadWithContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#readKey}.
	 * @param ctx the parse tree
	 */
	void enterReadKey(DNPParser.ReadKeyContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#readKey}.
	 * @param ctx the parse tree
	 */
	void exitReadKey(DNPParser.ReadKeyContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#receiveStatement}.
	 * @param ctx the parse tree
	 */
	void enterReceiveStatement(DNPParser.ReceiveStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#receiveStatement}.
	 * @param ctx the parse tree
	 */
	void exitReceiveStatement(DNPParser.ReceiveStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#receiveFromStatement}.
	 * @param ctx the parse tree
	 */
	void enterReceiveFromStatement(DNPParser.ReceiveFromStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#receiveFromStatement}.
	 * @param ctx the parse tree
	 */
	void exitReceiveFromStatement(DNPParser.ReceiveFromStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#receiveFrom}.
	 * @param ctx the parse tree
	 */
	void enterReceiveFrom(DNPParser.ReceiveFromContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#receiveFrom}.
	 * @param ctx the parse tree
	 */
	void exitReceiveFrom(DNPParser.ReceiveFromContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#receiveIntoStatement}.
	 * @param ctx the parse tree
	 */
	void enterReceiveIntoStatement(DNPParser.ReceiveIntoStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#receiveIntoStatement}.
	 * @param ctx the parse tree
	 */
	void exitReceiveIntoStatement(DNPParser.ReceiveIntoStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#receiveNoData}.
	 * @param ctx the parse tree
	 */
	void enterReceiveNoData(DNPParser.ReceiveNoDataContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#receiveNoData}.
	 * @param ctx the parse tree
	 */
	void exitReceiveNoData(DNPParser.ReceiveNoDataContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#receiveWithData}.
	 * @param ctx the parse tree
	 */
	void enterReceiveWithData(DNPParser.ReceiveWithDataContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#receiveWithData}.
	 * @param ctx the parse tree
	 */
	void exitReceiveWithData(DNPParser.ReceiveWithDataContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#receiveBefore}.
	 * @param ctx the parse tree
	 */
	void enterReceiveBefore(DNPParser.ReceiveBeforeContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#receiveBefore}.
	 * @param ctx the parse tree
	 */
	void exitReceiveBefore(DNPParser.ReceiveBeforeContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#receiveWith}.
	 * @param ctx the parse tree
	 */
	void enterReceiveWith(DNPParser.ReceiveWithContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#receiveWith}.
	 * @param ctx the parse tree
	 */
	void exitReceiveWith(DNPParser.ReceiveWithContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#receiveThread}.
	 * @param ctx the parse tree
	 */
	void enterReceiveThread(DNPParser.ReceiveThreadContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#receiveThread}.
	 * @param ctx the parse tree
	 */
	void exitReceiveThread(DNPParser.ReceiveThreadContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#receiveSize}.
	 * @param ctx the parse tree
	 */
	void enterReceiveSize(DNPParser.ReceiveSizeContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#receiveSize}.
	 * @param ctx the parse tree
	 */
	void exitReceiveSize(DNPParser.ReceiveSizeContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#receiveStatus}.
	 * @param ctx the parse tree
	 */
	void enterReceiveStatus(DNPParser.ReceiveStatusContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#receiveStatus}.
	 * @param ctx the parse tree
	 */
	void exitReceiveStatus(DNPParser.ReceiveStatusContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#releaseStatement}.
	 * @param ctx the parse tree
	 */
	void enterReleaseStatement(DNPParser.ReleaseStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#releaseStatement}.
	 * @param ctx the parse tree
	 */
	void exitReleaseStatement(DNPParser.ReleaseStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void enterReturnStatement(DNPParser.ReturnStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void exitReturnStatement(DNPParser.ReturnStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#returnInto}.
	 * @param ctx the parse tree
	 */
	void enterReturnInto(DNPParser.ReturnIntoContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#returnInto}.
	 * @param ctx the parse tree
	 */
	void exitReturnInto(DNPParser.ReturnIntoContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#rewriteStatement}.
	 * @param ctx the parse tree
	 */
	void enterRewriteStatement(DNPParser.RewriteStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#rewriteStatement}.
	 * @param ctx the parse tree
	 */
	void exitRewriteStatement(DNPParser.RewriteStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#rewriteFrom}.
	 * @param ctx the parse tree
	 */
	void enterRewriteFrom(DNPParser.RewriteFromContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#rewriteFrom}.
	 * @param ctx the parse tree
	 */
	void exitRewriteFrom(DNPParser.RewriteFromContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#searchStatement}.
	 * @param ctx the parse tree
	 */
	void enterSearchStatement(DNPParser.SearchStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#searchStatement}.
	 * @param ctx the parse tree
	 */
	void exitSearchStatement(DNPParser.SearchStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#searchVarying}.
	 * @param ctx the parse tree
	 */
	void enterSearchVarying(DNPParser.SearchVaryingContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#searchVarying}.
	 * @param ctx the parse tree
	 */
	void exitSearchVarying(DNPParser.SearchVaryingContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#searchWhen}.
	 * @param ctx the parse tree
	 */
	void enterSearchWhen(DNPParser.SearchWhenContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#searchWhen}.
	 * @param ctx the parse tree
	 */
	void exitSearchWhen(DNPParser.SearchWhenContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#sendStatement}.
	 * @param ctx the parse tree
	 */
	void enterSendStatement(DNPParser.SendStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#sendStatement}.
	 * @param ctx the parse tree
	 */
	void exitSendStatement(DNPParser.SendStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#sendStatementSync}.
	 * @param ctx the parse tree
	 */
	void enterSendStatementSync(DNPParser.SendStatementSyncContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#sendStatementSync}.
	 * @param ctx the parse tree
	 */
	void exitSendStatementSync(DNPParser.SendStatementSyncContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#sendStatementAsync}.
	 * @param ctx the parse tree
	 */
	void enterSendStatementAsync(DNPParser.SendStatementAsyncContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#sendStatementAsync}.
	 * @param ctx the parse tree
	 */
	void exitSendStatementAsync(DNPParser.SendStatementAsyncContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#sendFromPhrase}.
	 * @param ctx the parse tree
	 */
	void enterSendFromPhrase(DNPParser.SendFromPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#sendFromPhrase}.
	 * @param ctx the parse tree
	 */
	void exitSendFromPhrase(DNPParser.SendFromPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#sendWithPhrase}.
	 * @param ctx the parse tree
	 */
	void enterSendWithPhrase(DNPParser.SendWithPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#sendWithPhrase}.
	 * @param ctx the parse tree
	 */
	void exitSendWithPhrase(DNPParser.SendWithPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#sendReplacingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterSendReplacingPhrase(DNPParser.SendReplacingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#sendReplacingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitSendReplacingPhrase(DNPParser.SendReplacingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#sendAdvancingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterSendAdvancingPhrase(DNPParser.SendAdvancingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#sendAdvancingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitSendAdvancingPhrase(DNPParser.SendAdvancingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#sendAdvancingPage}.
	 * @param ctx the parse tree
	 */
	void enterSendAdvancingPage(DNPParser.SendAdvancingPageContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#sendAdvancingPage}.
	 * @param ctx the parse tree
	 */
	void exitSendAdvancingPage(DNPParser.SendAdvancingPageContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#sendAdvancingLines}.
	 * @param ctx the parse tree
	 */
	void enterSendAdvancingLines(DNPParser.SendAdvancingLinesContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#sendAdvancingLines}.
	 * @param ctx the parse tree
	 */
	void exitSendAdvancingLines(DNPParser.SendAdvancingLinesContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#sendAdvancingMnemonic}.
	 * @param ctx the parse tree
	 */
	void enterSendAdvancingMnemonic(DNPParser.SendAdvancingMnemonicContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#sendAdvancingMnemonic}.
	 * @param ctx the parse tree
	 */
	void exitSendAdvancingMnemonic(DNPParser.SendAdvancingMnemonicContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#setStatement}.
	 * @param ctx the parse tree
	 */
	void enterSetStatement(DNPParser.SetStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#setStatement}.
	 * @param ctx the parse tree
	 */
	void exitSetStatement(DNPParser.SetStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#setToStatement}.
	 * @param ctx the parse tree
	 */
	void enterSetToStatement(DNPParser.SetToStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#setToStatement}.
	 * @param ctx the parse tree
	 */
	void exitSetToStatement(DNPParser.SetToStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#setUpDownByStatement}.
	 * @param ctx the parse tree
	 */
	void enterSetUpDownByStatement(DNPParser.SetUpDownByStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#setUpDownByStatement}.
	 * @param ctx the parse tree
	 */
	void exitSetUpDownByStatement(DNPParser.SetUpDownByStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#setTo}.
	 * @param ctx the parse tree
	 */
	void enterSetTo(DNPParser.SetToContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#setTo}.
	 * @param ctx the parse tree
	 */
	void exitSetTo(DNPParser.SetToContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#setToValue}.
	 * @param ctx the parse tree
	 */
	void enterSetToValue(DNPParser.SetToValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#setToValue}.
	 * @param ctx the parse tree
	 */
	void exitSetToValue(DNPParser.SetToValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#setByValue}.
	 * @param ctx the parse tree
	 */
	void enterSetByValue(DNPParser.SetByValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#setByValue}.
	 * @param ctx the parse tree
	 */
	void exitSetByValue(DNPParser.SetByValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#sortStatement}.
	 * @param ctx the parse tree
	 */
	void enterSortStatement(DNPParser.SortStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#sortStatement}.
	 * @param ctx the parse tree
	 */
	void exitSortStatement(DNPParser.SortStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#sortOptional}.
	 * @param ctx the parse tree
	 */
	void enterSortOptional(DNPParser.SortOptionalContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#sortOptional}.
	 * @param ctx the parse tree
	 */
	void exitSortOptional(DNPParser.SortOptionalContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#sortOnKeyClause}.
	 * @param ctx the parse tree
	 */
	void enterSortOnKeyClause(DNPParser.SortOnKeyClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#sortOnKeyClause}.
	 * @param ctx the parse tree
	 */
	void exitSortOnKeyClause(DNPParser.SortOnKeyClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#sortDuplicatesPhrase}.
	 * @param ctx the parse tree
	 */
	void enterSortDuplicatesPhrase(DNPParser.SortDuplicatesPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#sortDuplicatesPhrase}.
	 * @param ctx the parse tree
	 */
	void exitSortDuplicatesPhrase(DNPParser.SortDuplicatesPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#sortCollatingSequencePhrase}.
	 * @param ctx the parse tree
	 */
	void enterSortCollatingSequencePhrase(DNPParser.SortCollatingSequencePhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#sortCollatingSequencePhrase}.
	 * @param ctx the parse tree
	 */
	void exitSortCollatingSequencePhrase(DNPParser.SortCollatingSequencePhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#sortCollatingAlphanumeric}.
	 * @param ctx the parse tree
	 */
	void enterSortCollatingAlphanumeric(DNPParser.SortCollatingAlphanumericContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#sortCollatingAlphanumeric}.
	 * @param ctx the parse tree
	 */
	void exitSortCollatingAlphanumeric(DNPParser.SortCollatingAlphanumericContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#sortCollatingNational}.
	 * @param ctx the parse tree
	 */
	void enterSortCollatingNational(DNPParser.SortCollatingNationalContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#sortCollatingNational}.
	 * @param ctx the parse tree
	 */
	void exitSortCollatingNational(DNPParser.SortCollatingNationalContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#sortInputProcedurePhrase}.
	 * @param ctx the parse tree
	 */
	void enterSortInputProcedurePhrase(DNPParser.SortInputProcedurePhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#sortInputProcedurePhrase}.
	 * @param ctx the parse tree
	 */
	void exitSortInputProcedurePhrase(DNPParser.SortInputProcedurePhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#sortInputThrough}.
	 * @param ctx the parse tree
	 */
	void enterSortInputThrough(DNPParser.SortInputThroughContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#sortInputThrough}.
	 * @param ctx the parse tree
	 */
	void exitSortInputThrough(DNPParser.SortInputThroughContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#sortUsing}.
	 * @param ctx the parse tree
	 */
	void enterSortUsing(DNPParser.SortUsingContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#sortUsing}.
	 * @param ctx the parse tree
	 */
	void exitSortUsing(DNPParser.SortUsingContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#sortOutputProcedurePhrase}.
	 * @param ctx the parse tree
	 */
	void enterSortOutputProcedurePhrase(DNPParser.SortOutputProcedurePhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#sortOutputProcedurePhrase}.
	 * @param ctx the parse tree
	 */
	void exitSortOutputProcedurePhrase(DNPParser.SortOutputProcedurePhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#sortOutputThrough}.
	 * @param ctx the parse tree
	 */
	void enterSortOutputThrough(DNPParser.SortOutputThroughContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#sortOutputThrough}.
	 * @param ctx the parse tree
	 */
	void exitSortOutputThrough(DNPParser.SortOutputThroughContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#sortGivingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterSortGivingPhrase(DNPParser.SortGivingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#sortGivingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitSortGivingPhrase(DNPParser.SortGivingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#sortGiving}.
	 * @param ctx the parse tree
	 */
	void enterSortGiving(DNPParser.SortGivingContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#sortGiving}.
	 * @param ctx the parse tree
	 */
	void exitSortGiving(DNPParser.SortGivingContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#startStatement}.
	 * @param ctx the parse tree
	 */
	void enterStartStatement(DNPParser.StartStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#startStatement}.
	 * @param ctx the parse tree
	 */
	void exitStartStatement(DNPParser.StartStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#startKey}.
	 * @param ctx the parse tree
	 */
	void enterStartKey(DNPParser.StartKeyContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#startKey}.
	 * @param ctx the parse tree
	 */
	void exitStartKey(DNPParser.StartKeyContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#stopStatement}.
	 * @param ctx the parse tree
	 */
	void enterStopStatement(DNPParser.StopStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#stopStatement}.
	 * @param ctx the parse tree
	 */
	void exitStopStatement(DNPParser.StopStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#stopOption}.
	 * @param ctx the parse tree
	 */
	void enterStopOption(DNPParser.StopOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#stopOption}.
	 * @param ctx the parse tree
	 */
	void exitStopOption(DNPParser.StopOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#storeStatement}.
	 * @param ctx the parse tree
	 */
	void enterStoreStatement(DNPParser.StoreStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#storeStatement}.
	 * @param ctx the parse tree
	 */
	void exitStoreStatement(DNPParser.StoreStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#stringStatement}.
	 * @param ctx the parse tree
	 */
	void enterStringStatement(DNPParser.StringStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#stringStatement}.
	 * @param ctx the parse tree
	 */
	void exitStringStatement(DNPParser.StringStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#stringSendingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterStringSendingPhrase(DNPParser.StringSendingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#stringSendingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitStringSendingPhrase(DNPParser.StringSendingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#stringSending}.
	 * @param ctx the parse tree
	 */
	void enterStringSending(DNPParser.StringSendingContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#stringSending}.
	 * @param ctx the parse tree
	 */
	void exitStringSending(DNPParser.StringSendingContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#stringDelimitedByPhrase}.
	 * @param ctx the parse tree
	 */
	void enterStringDelimitedByPhrase(DNPParser.StringDelimitedByPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#stringDelimitedByPhrase}.
	 * @param ctx the parse tree
	 */
	void exitStringDelimitedByPhrase(DNPParser.StringDelimitedByPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#stringForPhrase}.
	 * @param ctx the parse tree
	 */
	void enterStringForPhrase(DNPParser.StringForPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#stringForPhrase}.
	 * @param ctx the parse tree
	 */
	void exitStringForPhrase(DNPParser.StringForPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#stringIntoPhrase}.
	 * @param ctx the parse tree
	 */
	void enterStringIntoPhrase(DNPParser.StringIntoPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#stringIntoPhrase}.
	 * @param ctx the parse tree
	 */
	void exitStringIntoPhrase(DNPParser.StringIntoPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#stringWithPointerPhrase}.
	 * @param ctx the parse tree
	 */
	void enterStringWithPointerPhrase(DNPParser.StringWithPointerPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#stringWithPointerPhrase}.
	 * @param ctx the parse tree
	 */
	void exitStringWithPointerPhrase(DNPParser.StringWithPointerPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#subtractStatement}.
	 * @param ctx the parse tree
	 */
	void enterSubtractStatement(DNPParser.SubtractStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#subtractStatement}.
	 * @param ctx the parse tree
	 */
	void exitSubtractStatement(DNPParser.SubtractStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#subtractFromStatement}.
	 * @param ctx the parse tree
	 */
	void enterSubtractFromStatement(DNPParser.SubtractFromStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#subtractFromStatement}.
	 * @param ctx the parse tree
	 */
	void exitSubtractFromStatement(DNPParser.SubtractFromStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#subtractFromGivingStatement}.
	 * @param ctx the parse tree
	 */
	void enterSubtractFromGivingStatement(DNPParser.SubtractFromGivingStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#subtractFromGivingStatement}.
	 * @param ctx the parse tree
	 */
	void exitSubtractFromGivingStatement(DNPParser.SubtractFromGivingStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#subtractCorrespondingStatement}.
	 * @param ctx the parse tree
	 */
	void enterSubtractCorrespondingStatement(DNPParser.SubtractCorrespondingStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#subtractCorrespondingStatement}.
	 * @param ctx the parse tree
	 */
	void exitSubtractCorrespondingStatement(DNPParser.SubtractCorrespondingStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#subtractSubtrahend}.
	 * @param ctx the parse tree
	 */
	void enterSubtractSubtrahend(DNPParser.SubtractSubtrahendContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#subtractSubtrahend}.
	 * @param ctx the parse tree
	 */
	void exitSubtractSubtrahend(DNPParser.SubtractSubtrahendContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#subtractMinuend}.
	 * @param ctx the parse tree
	 */
	void enterSubtractMinuend(DNPParser.SubtractMinuendContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#subtractMinuend}.
	 * @param ctx the parse tree
	 */
	void exitSubtractMinuend(DNPParser.SubtractMinuendContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#subtractMinuendGiving}.
	 * @param ctx the parse tree
	 */
	void enterSubtractMinuendGiving(DNPParser.SubtractMinuendGivingContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#subtractMinuendGiving}.
	 * @param ctx the parse tree
	 */
	void exitSubtractMinuendGiving(DNPParser.SubtractMinuendGivingContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#subtractGiving}.
	 * @param ctx the parse tree
	 */
	void enterSubtractGiving(DNPParser.SubtractGivingContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#subtractGiving}.
	 * @param ctx the parse tree
	 */
	void exitSubtractGiving(DNPParser.SubtractGivingContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#subtractMinuendCorresponding}.
	 * @param ctx the parse tree
	 */
	void enterSubtractMinuendCorresponding(DNPParser.SubtractMinuendCorrespondingContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#subtractMinuendCorresponding}.
	 * @param ctx the parse tree
	 */
	void exitSubtractMinuendCorresponding(DNPParser.SubtractMinuendCorrespondingContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#transactionStatement}.
	 * @param ctx the parse tree
	 */
	void enterTransactionStatement(DNPParser.TransactionStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#transactionStatement}.
	 * @param ctx the parse tree
	 */
	void exitTransactionStatement(DNPParser.TransactionStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#transactionBegin}.
	 * @param ctx the parse tree
	 */
	void enterTransactionBegin(DNPParser.TransactionBeginContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#transactionBegin}.
	 * @param ctx the parse tree
	 */
	void exitTransactionBegin(DNPParser.TransactionBeginContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#transactionCancel}.
	 * @param ctx the parse tree
	 */
	void enterTransactionCancel(DNPParser.TransactionCancelContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#transactionCancel}.
	 * @param ctx the parse tree
	 */
	void exitTransactionCancel(DNPParser.TransactionCancelContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#transactionEnd}.
	 * @param ctx the parse tree
	 */
	void enterTransactionEnd(DNPParser.TransactionEndContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#transactionEnd}.
	 * @param ctx the parse tree
	 */
	void exitTransactionEnd(DNPParser.TransactionEndContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#terminateStatement}.
	 * @param ctx the parse tree
	 */
	void enterTerminateStatement(DNPParser.TerminateStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#terminateStatement}.
	 * @param ctx the parse tree
	 */
	void exitTerminateStatement(DNPParser.TerminateStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#unstringStatement}.
	 * @param ctx the parse tree
	 */
	void enterUnstringStatement(DNPParser.UnstringStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#unstringStatement}.
	 * @param ctx the parse tree
	 */
	void exitUnstringStatement(DNPParser.UnstringStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#unstringSendingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterUnstringSendingPhrase(DNPParser.UnstringSendingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#unstringSendingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitUnstringSendingPhrase(DNPParser.UnstringSendingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#unstringDelimitedByPhrase}.
	 * @param ctx the parse tree
	 */
	void enterUnstringDelimitedByPhrase(DNPParser.UnstringDelimitedByPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#unstringDelimitedByPhrase}.
	 * @param ctx the parse tree
	 */
	void exitUnstringDelimitedByPhrase(DNPParser.UnstringDelimitedByPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#unstringOrAllPhrase}.
	 * @param ctx the parse tree
	 */
	void enterUnstringOrAllPhrase(DNPParser.UnstringOrAllPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#unstringOrAllPhrase}.
	 * @param ctx the parse tree
	 */
	void exitUnstringOrAllPhrase(DNPParser.UnstringOrAllPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#unstringIntoPhrase}.
	 * @param ctx the parse tree
	 */
	void enterUnstringIntoPhrase(DNPParser.UnstringIntoPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#unstringIntoPhrase}.
	 * @param ctx the parse tree
	 */
	void exitUnstringIntoPhrase(DNPParser.UnstringIntoPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#unstringInto}.
	 * @param ctx the parse tree
	 */
	void enterUnstringInto(DNPParser.UnstringIntoContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#unstringInto}.
	 * @param ctx the parse tree
	 */
	void exitUnstringInto(DNPParser.UnstringIntoContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#unstringDelimiterIn}.
	 * @param ctx the parse tree
	 */
	void enterUnstringDelimiterIn(DNPParser.UnstringDelimiterInContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#unstringDelimiterIn}.
	 * @param ctx the parse tree
	 */
	void exitUnstringDelimiterIn(DNPParser.UnstringDelimiterInContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#unstringCountIn}.
	 * @param ctx the parse tree
	 */
	void enterUnstringCountIn(DNPParser.UnstringCountInContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#unstringCountIn}.
	 * @param ctx the parse tree
	 */
	void exitUnstringCountIn(DNPParser.UnstringCountInContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#unstringWithPointerPhrase}.
	 * @param ctx the parse tree
	 */
	void enterUnstringWithPointerPhrase(DNPParser.UnstringWithPointerPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#unstringWithPointerPhrase}.
	 * @param ctx the parse tree
	 */
	void exitUnstringWithPointerPhrase(DNPParser.UnstringWithPointerPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#unstringTallyingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterUnstringTallyingPhrase(DNPParser.UnstringTallyingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#unstringTallyingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitUnstringTallyingPhrase(DNPParser.UnstringTallyingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#useStatement}.
	 * @param ctx the parse tree
	 */
	void enterUseStatement(DNPParser.UseStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#useStatement}.
	 * @param ctx the parse tree
	 */
	void exitUseStatement(DNPParser.UseStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#useAfterClause}.
	 * @param ctx the parse tree
	 */
	void enterUseAfterClause(DNPParser.UseAfterClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#useAfterClause}.
	 * @param ctx the parse tree
	 */
	void exitUseAfterClause(DNPParser.UseAfterClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#useAfterOn}.
	 * @param ctx the parse tree
	 */
	void enterUseAfterOn(DNPParser.UseAfterOnContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#useAfterOn}.
	 * @param ctx the parse tree
	 */
	void exitUseAfterOn(DNPParser.UseAfterOnContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#useDebugClause}.
	 * @param ctx the parse tree
	 */
	void enterUseDebugClause(DNPParser.UseDebugClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#useDebugClause}.
	 * @param ctx the parse tree
	 */
	void exitUseDebugClause(DNPParser.UseDebugClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#useDebugOn}.
	 * @param ctx the parse tree
	 */
	void enterUseDebugOn(DNPParser.UseDebugOnContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#useDebugOn}.
	 * @param ctx the parse tree
	 */
	void exitUseDebugOn(DNPParser.UseDebugOnContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#useDeadLock}.
	 * @param ctx the parse tree
	 */
	void enterUseDeadLock(DNPParser.UseDeadLockContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#useDeadLock}.
	 * @param ctx the parse tree
	 */
	void exitUseDeadLock(DNPParser.UseDeadLockContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#useProcedure}.
	 * @param ctx the parse tree
	 */
	void enterUseProcedure(DNPParser.UseProcedureContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#useProcedure}.
	 * @param ctx the parse tree
	 */
	void exitUseProcedure(DNPParser.UseProcedureContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#waitStatement}.
	 * @param ctx the parse tree
	 */
	void enterWaitStatement(DNPParser.WaitStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#waitStatement}.
	 * @param ctx the parse tree
	 */
	void exitWaitStatement(DNPParser.WaitStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#waitArithmeticExpression}.
	 * @param ctx the parse tree
	 */
	void enterWaitArithmeticExpression(DNPParser.WaitArithmeticExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#waitArithmeticExpression}.
	 * @param ctx the parse tree
	 */
	void exitWaitArithmeticExpression(DNPParser.WaitArithmeticExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#attributeChangeEvent}.
	 * @param ctx the parse tree
	 */
	void enterAttributeChangeEvent(DNPParser.AttributeChangeEventContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#attributeChangeEvent}.
	 * @param ctx the parse tree
	 */
	void exitAttributeChangeEvent(DNPParser.AttributeChangeEventContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#attributeInputEvent}.
	 * @param ctx the parse tree
	 */
	void enterAttributeInputEvent(DNPParser.AttributeInputEventContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#attributeInputEvent}.
	 * @param ctx the parse tree
	 */
	void exitAttributeInputEvent(DNPParser.AttributeInputEventContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#attributeOutputEvent}.
	 * @param ctx the parse tree
	 */
	void enterAttributeOutputEvent(DNPParser.AttributeOutputEventContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#attributeOutputEvent}.
	 * @param ctx the parse tree
	 */
	void exitAttributeOutputEvent(DNPParser.AttributeOutputEventContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#attributeAcceptEvent}.
	 * @param ctx the parse tree
	 */
	void enterAttributeAcceptEvent(DNPParser.AttributeAcceptEventContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#attributeAcceptEvent}.
	 * @param ctx the parse tree
	 */
	void exitAttributeAcceptEvent(DNPParser.AttributeAcceptEventContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#attributeExceptionEvent}.
	 * @param ctx the parse tree
	 */
	void enterAttributeExceptionEvent(DNPParser.AttributeExceptionEventContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#attributeExceptionEvent}.
	 * @param ctx the parse tree
	 */
	void exitAttributeExceptionEvent(DNPParser.AttributeExceptionEventContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#eventIdentifier}.
	 * @param ctx the parse tree
	 */
	void enterEventIdentifier(DNPParser.EventIdentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#eventIdentifier}.
	 * @param ctx the parse tree
	 */
	void exitEventIdentifier(DNPParser.EventIdentifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#crcrEvent}.
	 * @param ctx the parse tree
	 */
	void enterCrcrEvent(DNPParser.CrcrEventContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#crcrEvent}.
	 * @param ctx the parse tree
	 */
	void exitCrcrEvent(DNPParser.CrcrEventContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#odtInputPresent}.
	 * @param ctx the parse tree
	 */
	void enterOdtInputPresent(DNPParser.OdtInputPresentContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#odtInputPresent}.
	 * @param ctx the parse tree
	 */
	void exitOdtInputPresent(DNPParser.OdtInputPresentContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#readOk}.
	 * @param ctx the parse tree
	 */
	void enterReadOk(DNPParser.ReadOkContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#readOk}.
	 * @param ctx the parse tree
	 */
	void exitReadOk(DNPParser.ReadOkContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#writeOk}.
	 * @param ctx the parse tree
	 */
	void enterWriteOk(DNPParser.WriteOkContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#writeOk}.
	 * @param ctx the parse tree
	 */
	void exitWriteOk(DNPParser.WriteOkContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#stoqEvent}.
	 * @param ctx the parse tree
	 */
	void enterStoqEvent(DNPParser.StoqEventContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#stoqEvent}.
	 * @param ctx the parse tree
	 */
	void exitStoqEvent(DNPParser.StoqEventContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#writeStatement}.
	 * @param ctx the parse tree
	 */
	void enterWriteStatement(DNPParser.WriteStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#writeStatement}.
	 * @param ctx the parse tree
	 */
	void exitWriteStatement(DNPParser.WriteStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#writeFromPhrase}.
	 * @param ctx the parse tree
	 */
	void enterWriteFromPhrase(DNPParser.WriteFromPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#writeFromPhrase}.
	 * @param ctx the parse tree
	 */
	void exitWriteFromPhrase(DNPParser.WriteFromPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#writeAdvancingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterWriteAdvancingPhrase(DNPParser.WriteAdvancingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#writeAdvancingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitWriteAdvancingPhrase(DNPParser.WriteAdvancingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#writeAdvancingPage}.
	 * @param ctx the parse tree
	 */
	void enterWriteAdvancingPage(DNPParser.WriteAdvancingPageContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#writeAdvancingPage}.
	 * @param ctx the parse tree
	 */
	void exitWriteAdvancingPage(DNPParser.WriteAdvancingPageContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#writeAdvancingLines}.
	 * @param ctx the parse tree
	 */
	void enterWriteAdvancingLines(DNPParser.WriteAdvancingLinesContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#writeAdvancingLines}.
	 * @param ctx the parse tree
	 */
	void exitWriteAdvancingLines(DNPParser.WriteAdvancingLinesContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#writeAdvancingMnemonic}.
	 * @param ctx the parse tree
	 */
	void enterWriteAdvancingMnemonic(DNPParser.WriteAdvancingMnemonicContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#writeAdvancingMnemonic}.
	 * @param ctx the parse tree
	 */
	void exitWriteAdvancingMnemonic(DNPParser.WriteAdvancingMnemonicContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#writeAtEndOfPagePhrase}.
	 * @param ctx the parse tree
	 */
	void enterWriteAtEndOfPagePhrase(DNPParser.WriteAtEndOfPagePhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#writeAtEndOfPagePhrase}.
	 * @param ctx the parse tree
	 */
	void exitWriteAtEndOfPagePhrase(DNPParser.WriteAtEndOfPagePhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#writeNotAtEndOfPagePhrase}.
	 * @param ctx the parse tree
	 */
	void enterWriteNotAtEndOfPagePhrase(DNPParser.WriteNotAtEndOfPagePhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#writeNotAtEndOfPagePhrase}.
	 * @param ctx the parse tree
	 */
	void exitWriteNotAtEndOfPagePhrase(DNPParser.WriteNotAtEndOfPagePhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#atEndPhrase}.
	 * @param ctx the parse tree
	 */
	void enterAtEndPhrase(DNPParser.AtEndPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#atEndPhrase}.
	 * @param ctx the parse tree
	 */
	void exitAtEndPhrase(DNPParser.AtEndPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#notAtEndPhrase}.
	 * @param ctx the parse tree
	 */
	void enterNotAtEndPhrase(DNPParser.NotAtEndPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#notAtEndPhrase}.
	 * @param ctx the parse tree
	 */
	void exitNotAtEndPhrase(DNPParser.NotAtEndPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#invalidKeyPhrase}.
	 * @param ctx the parse tree
	 */
	void enterInvalidKeyPhrase(DNPParser.InvalidKeyPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#invalidKeyPhrase}.
	 * @param ctx the parse tree
	 */
	void exitInvalidKeyPhrase(DNPParser.InvalidKeyPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#notInvalidKeyPhrase}.
	 * @param ctx the parse tree
	 */
	void enterNotInvalidKeyPhrase(DNPParser.NotInvalidKeyPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#notInvalidKeyPhrase}.
	 * @param ctx the parse tree
	 */
	void exitNotInvalidKeyPhrase(DNPParser.NotInvalidKeyPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#onOverflowPhrase}.
	 * @param ctx the parse tree
	 */
	void enterOnOverflowPhrase(DNPParser.OnOverflowPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#onOverflowPhrase}.
	 * @param ctx the parse tree
	 */
	void exitOnOverflowPhrase(DNPParser.OnOverflowPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#notOnOverflowPhrase}.
	 * @param ctx the parse tree
	 */
	void enterNotOnOverflowPhrase(DNPParser.NotOnOverflowPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#notOnOverflowPhrase}.
	 * @param ctx the parse tree
	 */
	void exitNotOnOverflowPhrase(DNPParser.NotOnOverflowPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#onSizeErrorPhrase}.
	 * @param ctx the parse tree
	 */
	void enterOnSizeErrorPhrase(DNPParser.OnSizeErrorPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#onSizeErrorPhrase}.
	 * @param ctx the parse tree
	 */
	void exitOnSizeErrorPhrase(DNPParser.OnSizeErrorPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#notOnSizeErrorPhrase}.
	 * @param ctx the parse tree
	 */
	void enterNotOnSizeErrorPhrase(DNPParser.NotOnSizeErrorPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#notOnSizeErrorPhrase}.
	 * @param ctx the parse tree
	 */
	void exitNotOnSizeErrorPhrase(DNPParser.NotOnSizeErrorPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#onExceptionClause}.
	 * @param ctx the parse tree
	 */
	void enterOnExceptionClause(DNPParser.OnExceptionClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#onExceptionClause}.
	 * @param ctx the parse tree
	 */
	void exitOnExceptionClause(DNPParser.OnExceptionClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#notOnExceptionClause}.
	 * @param ctx the parse tree
	 */
	void enterNotOnExceptionClause(DNPParser.NotOnExceptionClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#notOnExceptionClause}.
	 * @param ctx the parse tree
	 */
	void exitNotOnExceptionClause(DNPParser.NotOnExceptionClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#arithmeticExpression}.
	 * @param ctx the parse tree
	 */
	void enterArithmeticExpression(DNPParser.ArithmeticExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#arithmeticExpression}.
	 * @param ctx the parse tree
	 */
	void exitArithmeticExpression(DNPParser.ArithmeticExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#plusMinus}.
	 * @param ctx the parse tree
	 */
	void enterPlusMinus(DNPParser.PlusMinusContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#plusMinus}.
	 * @param ctx the parse tree
	 */
	void exitPlusMinus(DNPParser.PlusMinusContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#multDivs}.
	 * @param ctx the parse tree
	 */
	void enterMultDivs(DNPParser.MultDivsContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#multDivs}.
	 * @param ctx the parse tree
	 */
	void exitMultDivs(DNPParser.MultDivsContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#multDiv}.
	 * @param ctx the parse tree
	 */
	void enterMultDiv(DNPParser.MultDivContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#multDiv}.
	 * @param ctx the parse tree
	 */
	void exitMultDiv(DNPParser.MultDivContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#powers}.
	 * @param ctx the parse tree
	 */
	void enterPowers(DNPParser.PowersContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#powers}.
	 * @param ctx the parse tree
	 */
	void exitPowers(DNPParser.PowersContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#power}.
	 * @param ctx the parse tree
	 */
	void enterPower(DNPParser.PowerContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#power}.
	 * @param ctx the parse tree
	 */
	void exitPower(DNPParser.PowerContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#basis}.
	 * @param ctx the parse tree
	 */
	void enterBasis(DNPParser.BasisContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#basis}.
	 * @param ctx the parse tree
	 */
	void exitBasis(DNPParser.BasisContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(DNPParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(DNPParser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#andOrCondition}.
	 * @param ctx the parse tree
	 */
	void enterAndOrCondition(DNPParser.AndOrConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#andOrCondition}.
	 * @param ctx the parse tree
	 */
	void exitAndOrCondition(DNPParser.AndOrConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#combinableCondition}.
	 * @param ctx the parse tree
	 */
	void enterCombinableCondition(DNPParser.CombinableConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#combinableCondition}.
	 * @param ctx the parse tree
	 */
	void exitCombinableCondition(DNPParser.CombinableConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#simpleCondition}.
	 * @param ctx the parse tree
	 */
	void enterSimpleCondition(DNPParser.SimpleConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#simpleCondition}.
	 * @param ctx the parse tree
	 */
	void exitSimpleCondition(DNPParser.SimpleConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#classCondition}.
	 * @param ctx the parse tree
	 */
	void enterClassCondition(DNPParser.ClassConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#classCondition}.
	 * @param ctx the parse tree
	 */
	void exitClassCondition(DNPParser.ClassConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#conditionNameReference}.
	 * @param ctx the parse tree
	 */
	void enterConditionNameReference(DNPParser.ConditionNameReferenceContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#conditionNameReference}.
	 * @param ctx the parse tree
	 */
	void exitConditionNameReference(DNPParser.ConditionNameReferenceContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#conditionNameSubscriptReference}.
	 * @param ctx the parse tree
	 */
	void enterConditionNameSubscriptReference(DNPParser.ConditionNameSubscriptReferenceContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#conditionNameSubscriptReference}.
	 * @param ctx the parse tree
	 */
	void exitConditionNameSubscriptReference(DNPParser.ConditionNameSubscriptReferenceContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#attributeCondition}.
	 * @param ctx the parse tree
	 */
	void enterAttributeCondition(DNPParser.AttributeConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#attributeCondition}.
	 * @param ctx the parse tree
	 */
	void exitAttributeCondition(DNPParser.AttributeConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#attributeConditionExpr}.
	 * @param ctx the parse tree
	 */
	void enterAttributeConditionExpr(DNPParser.AttributeConditionExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#attributeConditionExpr}.
	 * @param ctx the parse tree
	 */
	void exitAttributeConditionExpr(DNPParser.AttributeConditionExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#relationCondition}.
	 * @param ctx the parse tree
	 */
	void enterRelationCondition(DNPParser.RelationConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#relationCondition}.
	 * @param ctx the parse tree
	 */
	void exitRelationCondition(DNPParser.RelationConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#relationSignCondition}.
	 * @param ctx the parse tree
	 */
	void enterRelationSignCondition(DNPParser.RelationSignConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#relationSignCondition}.
	 * @param ctx the parse tree
	 */
	void exitRelationSignCondition(DNPParser.RelationSignConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#relationArithmeticComparison}.
	 * @param ctx the parse tree
	 */
	void enterRelationArithmeticComparison(DNPParser.RelationArithmeticComparisonContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#relationArithmeticComparison}.
	 * @param ctx the parse tree
	 */
	void exitRelationArithmeticComparison(DNPParser.RelationArithmeticComparisonContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#relationCombinedComparison}.
	 * @param ctx the parse tree
	 */
	void enterRelationCombinedComparison(DNPParser.RelationCombinedComparisonContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#relationCombinedComparison}.
	 * @param ctx the parse tree
	 */
	void exitRelationCombinedComparison(DNPParser.RelationCombinedComparisonContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#relationCombinedCondition}.
	 * @param ctx the parse tree
	 */
	void enterRelationCombinedCondition(DNPParser.RelationCombinedConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#relationCombinedCondition}.
	 * @param ctx the parse tree
	 */
	void exitRelationCombinedCondition(DNPParser.RelationCombinedConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#relationalOperator}.
	 * @param ctx the parse tree
	 */
	void enterRelationalOperator(DNPParser.RelationalOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#relationalOperator}.
	 * @param ctx the parse tree
	 */
	void exitRelationalOperator(DNPParser.RelationalOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#abbreviation}.
	 * @param ctx the parse tree
	 */
	void enterAbbreviation(DNPParser.AbbreviationContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#abbreviation}.
	 * @param ctx the parse tree
	 */
	void exitAbbreviation(DNPParser.AbbreviationContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#identifier}.
	 * @param ctx the parse tree
	 */
	void enterIdentifier(DNPParser.IdentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#identifier}.
	 * @param ctx the parse tree
	 */
	void exitIdentifier(DNPParser.IdentifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#tableCall}.
	 * @param ctx the parse tree
	 */
	void enterTableCall(DNPParser.TableCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#tableCall}.
	 * @param ctx the parse tree
	 */
	void exitTableCall(DNPParser.TableCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCall(DNPParser.FunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCall(DNPParser.FunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#referenceModifier}.
	 * @param ctx the parse tree
	 */
	void enterReferenceModifier(DNPParser.ReferenceModifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#referenceModifier}.
	 * @param ctx the parse tree
	 */
	void exitReferenceModifier(DNPParser.ReferenceModifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#characterPosition}.
	 * @param ctx the parse tree
	 */
	void enterCharacterPosition(DNPParser.CharacterPositionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#characterPosition}.
	 * @param ctx the parse tree
	 */
	void exitCharacterPosition(DNPParser.CharacterPositionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#length}.
	 * @param ctx the parse tree
	 */
	void enterLength(DNPParser.LengthContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#length}.
	 * @param ctx the parse tree
	 */
	void exitLength(DNPParser.LengthContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#subscript_}.
	 * @param ctx the parse tree
	 */
	void enterSubscript_(DNPParser.Subscript_Context ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#subscript_}.
	 * @param ctx the parse tree
	 */
	void exitSubscript_(DNPParser.Subscript_Context ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#argument}.
	 * @param ctx the parse tree
	 */
	void enterArgument(DNPParser.ArgumentContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#argument}.
	 * @param ctx the parse tree
	 */
	void exitArgument(DNPParser.ArgumentContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#qualifiedDataName}.
	 * @param ctx the parse tree
	 */
	void enterQualifiedDataName(DNPParser.QualifiedDataNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#qualifiedDataName}.
	 * @param ctx the parse tree
	 */
	void exitQualifiedDataName(DNPParser.QualifiedDataNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#qualifiedDataNameFormat1}.
	 * @param ctx the parse tree
	 */
	void enterQualifiedDataNameFormat1(DNPParser.QualifiedDataNameFormat1Context ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#qualifiedDataNameFormat1}.
	 * @param ctx the parse tree
	 */
	void exitQualifiedDataNameFormat1(DNPParser.QualifiedDataNameFormat1Context ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#qualifiedDataNameFormat2}.
	 * @param ctx the parse tree
	 */
	void enterQualifiedDataNameFormat2(DNPParser.QualifiedDataNameFormat2Context ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#qualifiedDataNameFormat2}.
	 * @param ctx the parse tree
	 */
	void exitQualifiedDataNameFormat2(DNPParser.QualifiedDataNameFormat2Context ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#qualifiedDataNameFormat3}.
	 * @param ctx the parse tree
	 */
	void enterQualifiedDataNameFormat3(DNPParser.QualifiedDataNameFormat3Context ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#qualifiedDataNameFormat3}.
	 * @param ctx the parse tree
	 */
	void exitQualifiedDataNameFormat3(DNPParser.QualifiedDataNameFormat3Context ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#qualifiedDataNameFormat4}.
	 * @param ctx the parse tree
	 */
	void enterQualifiedDataNameFormat4(DNPParser.QualifiedDataNameFormat4Context ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#qualifiedDataNameFormat4}.
	 * @param ctx the parse tree
	 */
	void exitQualifiedDataNameFormat4(DNPParser.QualifiedDataNameFormat4Context ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#qualifiedInData}.
	 * @param ctx the parse tree
	 */
	void enterQualifiedInData(DNPParser.QualifiedInDataContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#qualifiedInData}.
	 * @param ctx the parse tree
	 */
	void exitQualifiedInData(DNPParser.QualifiedInDataContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#inData}.
	 * @param ctx the parse tree
	 */
	void enterInData(DNPParser.InDataContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#inData}.
	 * @param ctx the parse tree
	 */
	void exitInData(DNPParser.InDataContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#inFile}.
	 * @param ctx the parse tree
	 */
	void enterInFile(DNPParser.InFileContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#inFile}.
	 * @param ctx the parse tree
	 */
	void exitInFile(DNPParser.InFileContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#inMnemonic}.
	 * @param ctx the parse tree
	 */
	void enterInMnemonic(DNPParser.InMnemonicContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#inMnemonic}.
	 * @param ctx the parse tree
	 */
	void exitInMnemonic(DNPParser.InMnemonicContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#inSection}.
	 * @param ctx the parse tree
	 */
	void enterInSection(DNPParser.InSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#inSection}.
	 * @param ctx the parse tree
	 */
	void exitInSection(DNPParser.InSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#inLibrary}.
	 * @param ctx the parse tree
	 */
	void enterInLibrary(DNPParser.InLibraryContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#inLibrary}.
	 * @param ctx the parse tree
	 */
	void exitInLibrary(DNPParser.InLibraryContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#inTable}.
	 * @param ctx the parse tree
	 */
	void enterInTable(DNPParser.InTableContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#inTable}.
	 * @param ctx the parse tree
	 */
	void exitInTable(DNPParser.InTableContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#alphabetName}.
	 * @param ctx the parse tree
	 */
	void enterAlphabetName(DNPParser.AlphabetNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#alphabetName}.
	 * @param ctx the parse tree
	 */
	void exitAlphabetName(DNPParser.AlphabetNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#assignmentName}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentName(DNPParser.AssignmentNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#assignmentName}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentName(DNPParser.AssignmentNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#basisName}.
	 * @param ctx the parse tree
	 */
	void enterBasisName(DNPParser.BasisNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#basisName}.
	 * @param ctx the parse tree
	 */
	void exitBasisName(DNPParser.BasisNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#cdName}.
	 * @param ctx the parse tree
	 */
	void enterCdName(DNPParser.CdNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#cdName}.
	 * @param ctx the parse tree
	 */
	void exitCdName(DNPParser.CdNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#className}.
	 * @param ctx the parse tree
	 */
	void enterClassName(DNPParser.ClassNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#className}.
	 * @param ctx the parse tree
	 */
	void exitClassName(DNPParser.ClassNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#computerName}.
	 * @param ctx the parse tree
	 */
	void enterComputerName(DNPParser.ComputerNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#computerName}.
	 * @param ctx the parse tree
	 */
	void exitComputerName(DNPParser.ComputerNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#conditionName}.
	 * @param ctx the parse tree
	 */
	void enterConditionName(DNPParser.ConditionNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#conditionName}.
	 * @param ctx the parse tree
	 */
	void exitConditionName(DNPParser.ConditionNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataName}.
	 * @param ctx the parse tree
	 */
	void enterDataName(DNPParser.DataNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataName}.
	 * @param ctx the parse tree
	 */
	void exitDataName(DNPParser.DataNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#dataDescName}.
	 * @param ctx the parse tree
	 */
	void enterDataDescName(DNPParser.DataDescNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#dataDescName}.
	 * @param ctx the parse tree
	 */
	void exitDataDescName(DNPParser.DataDescNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#environmentName}.
	 * @param ctx the parse tree
	 */
	void enterEnvironmentName(DNPParser.EnvironmentNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#environmentName}.
	 * @param ctx the parse tree
	 */
	void exitEnvironmentName(DNPParser.EnvironmentNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#fileAttribute}.
	 * @param ctx the parse tree
	 */
	void enterFileAttribute(DNPParser.FileAttributeContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#fileAttribute}.
	 * @param ctx the parse tree
	 */
	void exitFileAttribute(DNPParser.FileAttributeContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#fileName}.
	 * @param ctx the parse tree
	 */
	void enterFileName(DNPParser.FileNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#fileName}.
	 * @param ctx the parse tree
	 */
	void exitFileName(DNPParser.FileNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#functionName}.
	 * @param ctx the parse tree
	 */
	void enterFunctionName(DNPParser.FunctionNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#functionName}.
	 * @param ctx the parse tree
	 */
	void exitFunctionName(DNPParser.FunctionNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#indexName}.
	 * @param ctx the parse tree
	 */
	void enterIndexName(DNPParser.IndexNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#indexName}.
	 * @param ctx the parse tree
	 */
	void exitIndexName(DNPParser.IndexNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#languageName}.
	 * @param ctx the parse tree
	 */
	void enterLanguageName(DNPParser.LanguageNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#languageName}.
	 * @param ctx the parse tree
	 */
	void exitLanguageName(DNPParser.LanguageNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#libraryName}.
	 * @param ctx the parse tree
	 */
	void enterLibraryName(DNPParser.LibraryNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#libraryName}.
	 * @param ctx the parse tree
	 */
	void exitLibraryName(DNPParser.LibraryNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#localName}.
	 * @param ctx the parse tree
	 */
	void enterLocalName(DNPParser.LocalNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#localName}.
	 * @param ctx the parse tree
	 */
	void exitLocalName(DNPParser.LocalNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#mnemonicName}.
	 * @param ctx the parse tree
	 */
	void enterMnemonicName(DNPParser.MnemonicNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#mnemonicName}.
	 * @param ctx the parse tree
	 */
	void exitMnemonicName(DNPParser.MnemonicNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#paragraphName}.
	 * @param ctx the parse tree
	 */
	void enterParagraphName(DNPParser.ParagraphNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#paragraphName}.
	 * @param ctx the parse tree
	 */
	void exitParagraphName(DNPParser.ParagraphNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#procedureName}.
	 * @param ctx the parse tree
	 */
	void enterProcedureName(DNPParser.ProcedureNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#procedureName}.
	 * @param ctx the parse tree
	 */
	void exitProcedureName(DNPParser.ProcedureNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#programName}.
	 * @param ctx the parse tree
	 */
	void enterProgramName(DNPParser.ProgramNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#programName}.
	 * @param ctx the parse tree
	 */
	void exitProgramName(DNPParser.ProgramNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#recordName}.
	 * @param ctx the parse tree
	 */
	void enterRecordName(DNPParser.RecordNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#recordName}.
	 * @param ctx the parse tree
	 */
	void exitRecordName(DNPParser.RecordNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#reportName}.
	 * @param ctx the parse tree
	 */
	void enterReportName(DNPParser.ReportNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#reportName}.
	 * @param ctx the parse tree
	 */
	void exitReportName(DNPParser.ReportNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#routineName}.
	 * @param ctx the parse tree
	 */
	void enterRoutineName(DNPParser.RoutineNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#routineName}.
	 * @param ctx the parse tree
	 */
	void exitRoutineName(DNPParser.RoutineNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#screenName}.
	 * @param ctx the parse tree
	 */
	void enterScreenName(DNPParser.ScreenNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#screenName}.
	 * @param ctx the parse tree
	 */
	void exitScreenName(DNPParser.ScreenNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#sectionName}.
	 * @param ctx the parse tree
	 */
	void enterSectionName(DNPParser.SectionNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#sectionName}.
	 * @param ctx the parse tree
	 */
	void exitSectionName(DNPParser.SectionNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#systemName}.
	 * @param ctx the parse tree
	 */
	void enterSystemName(DNPParser.SystemNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#systemName}.
	 * @param ctx the parse tree
	 */
	void exitSystemName(DNPParser.SystemNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#symbolicCharacter}.
	 * @param ctx the parse tree
	 */
	void enterSymbolicCharacter(DNPParser.SymbolicCharacterContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#symbolicCharacter}.
	 * @param ctx the parse tree
	 */
	void exitSymbolicCharacter(DNPParser.SymbolicCharacterContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#textName}.
	 * @param ctx the parse tree
	 */
	void enterTextName(DNPParser.TextNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#textName}.
	 * @param ctx the parse tree
	 */
	void exitTextName(DNPParser.TextNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#booleanLiteral}.
	 * @param ctx the parse tree
	 */
	void enterBooleanLiteral(DNPParser.BooleanLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#booleanLiteral}.
	 * @param ctx the parse tree
	 */
	void exitBooleanLiteral(DNPParser.BooleanLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#numericLiteral}.
	 * @param ctx the parse tree
	 */
	void enterNumericLiteral(DNPParser.NumericLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#numericLiteral}.
	 * @param ctx the parse tree
	 */
	void exitNumericLiteral(DNPParser.NumericLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#integerLiteral}.
	 * @param ctx the parse tree
	 */
	void enterIntegerLiteral(DNPParser.IntegerLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#integerLiteral}.
	 * @param ctx the parse tree
	 */
	void exitIntegerLiteral(DNPParser.IntegerLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#cicsDfhRespLiteral}.
	 * @param ctx the parse tree
	 */
	void enterCicsDfhRespLiteral(DNPParser.CicsDfhRespLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#cicsDfhRespLiteral}.
	 * @param ctx the parse tree
	 */
	void exitCicsDfhRespLiteral(DNPParser.CicsDfhRespLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#cicsDfhValueLiteral}.
	 * @param ctx the parse tree
	 */
	void enterCicsDfhValueLiteral(DNPParser.CicsDfhValueLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#cicsDfhValueLiteral}.
	 * @param ctx the parse tree
	 */
	void exitCicsDfhValueLiteral(DNPParser.CicsDfhValueLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#figurativeConstant}.
	 * @param ctx the parse tree
	 */
	void enterFigurativeConstant(DNPParser.FigurativeConstantContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#figurativeConstant}.
	 * @param ctx the parse tree
	 */
	void exitFigurativeConstant(DNPParser.FigurativeConstantContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#specialRegister}.
	 * @param ctx the parse tree
	 */
	void enterSpecialRegister(DNPParser.SpecialRegisterContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#specialRegister}.
	 * @param ctx the parse tree
	 */
	void exitSpecialRegister(DNPParser.SpecialRegisterContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#commentEntry}.
	 * @param ctx the parse tree
	 */
	void enterCommentEntry(DNPParser.CommentEntryContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#commentEntry}.
	 * @param ctx the parse tree
	 */
	void exitCommentEntry(DNPParser.CommentEntryContext ctx);
	/**
	 * Enter a parse tree produced by {@link DNPParser#charDataKeyword}.
	 * @param ctx the parse tree
	 */
	void enterCharDataKeyword(DNPParser.CharDataKeywordContext ctx);
	/**
	 * Exit a parse tree produced by {@link DNPParser#charDataKeyword}.
	 * @param ctx the parse tree
	 */
	void exitCharDataKeyword(DNPParser.CharDataKeywordContext ctx);
}