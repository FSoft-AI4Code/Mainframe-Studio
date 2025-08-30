// Generated from /home/neil/Documents/mainframe-workers/grammar/isuzu_cobol/CobolIsuzu.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CobolIsuzuParser}.
 */
public interface CobolIsuzuListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#startRule}.
	 * @param ctx the parse tree
	 */
	void enterStartRule(CobolIsuzuParser.StartRuleContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#startRule}.
	 * @param ctx the parse tree
	 */
	void exitStartRule(CobolIsuzuParser.StartRuleContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#compilationUnit}.
	 * @param ctx the parse tree
	 */
	void enterCompilationUnit(CobolIsuzuParser.CompilationUnitContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#compilationUnit}.
	 * @param ctx the parse tree
	 */
	void exitCompilationUnit(CobolIsuzuParser.CompilationUnitContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#programUnit}.
	 * @param ctx the parse tree
	 */
	void enterProgramUnit(CobolIsuzuParser.ProgramUnitContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#programUnit}.
	 * @param ctx the parse tree
	 */
	void exitProgramUnit(CobolIsuzuParser.ProgramUnitContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#endProgramStatement}.
	 * @param ctx the parse tree
	 */
	void enterEndProgramStatement(CobolIsuzuParser.EndProgramStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#endProgramStatement}.
	 * @param ctx the parse tree
	 */
	void exitEndProgramStatement(CobolIsuzuParser.EndProgramStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#identificationDivision}.
	 * @param ctx the parse tree
	 */
	void enterIdentificationDivision(CobolIsuzuParser.IdentificationDivisionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#identificationDivision}.
	 * @param ctx the parse tree
	 */
	void exitIdentificationDivision(CobolIsuzuParser.IdentificationDivisionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#identificationDivisionBody}.
	 * @param ctx the parse tree
	 */
	void enterIdentificationDivisionBody(CobolIsuzuParser.IdentificationDivisionBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#identificationDivisionBody}.
	 * @param ctx the parse tree
	 */
	void exitIdentificationDivisionBody(CobolIsuzuParser.IdentificationDivisionBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#programIdParagraph}.
	 * @param ctx the parse tree
	 */
	void enterProgramIdParagraph(CobolIsuzuParser.ProgramIdParagraphContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#programIdParagraph}.
	 * @param ctx the parse tree
	 */
	void exitProgramIdParagraph(CobolIsuzuParser.ProgramIdParagraphContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#author_name}.
	 * @param ctx the parse tree
	 */
	void enterAuthor_name(CobolIsuzuParser.Author_nameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#author_name}.
	 * @param ctx the parse tree
	 */
	void exitAuthor_name(CobolIsuzuParser.Author_nameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#authorParagraph}.
	 * @param ctx the parse tree
	 */
	void enterAuthorParagraph(CobolIsuzuParser.AuthorParagraphContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#authorParagraph}.
	 * @param ctx the parse tree
	 */
	void exitAuthorParagraph(CobolIsuzuParser.AuthorParagraphContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#installationParagraph}.
	 * @param ctx the parse tree
	 */
	void enterInstallationParagraph(CobolIsuzuParser.InstallationParagraphContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#installationParagraph}.
	 * @param ctx the parse tree
	 */
	void exitInstallationParagraph(CobolIsuzuParser.InstallationParagraphContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dateWrittenParagraph}.
	 * @param ctx the parse tree
	 */
	void enterDateWrittenParagraph(CobolIsuzuParser.DateWrittenParagraphContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dateWrittenParagraph}.
	 * @param ctx the parse tree
	 */
	void exitDateWrittenParagraph(CobolIsuzuParser.DateWrittenParagraphContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dateCompiledParagraph}.
	 * @param ctx the parse tree
	 */
	void enterDateCompiledParagraph(CobolIsuzuParser.DateCompiledParagraphContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dateCompiledParagraph}.
	 * @param ctx the parse tree
	 */
	void exitDateCompiledParagraph(CobolIsuzuParser.DateCompiledParagraphContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#securityParagraph}.
	 * @param ctx the parse tree
	 */
	void enterSecurityParagraph(CobolIsuzuParser.SecurityParagraphContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#securityParagraph}.
	 * @param ctx the parse tree
	 */
	void exitSecurityParagraph(CobolIsuzuParser.SecurityParagraphContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#remarksParagraph}.
	 * @param ctx the parse tree
	 */
	void enterRemarksParagraph(CobolIsuzuParser.RemarksParagraphContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#remarksParagraph}.
	 * @param ctx the parse tree
	 */
	void exitRemarksParagraph(CobolIsuzuParser.RemarksParagraphContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#environmentDivision}.
	 * @param ctx the parse tree
	 */
	void enterEnvironmentDivision(CobolIsuzuParser.EnvironmentDivisionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#environmentDivision}.
	 * @param ctx the parse tree
	 */
	void exitEnvironmentDivision(CobolIsuzuParser.EnvironmentDivisionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#environmentDivisionBody}.
	 * @param ctx the parse tree
	 */
	void enterEnvironmentDivisionBody(CobolIsuzuParser.EnvironmentDivisionBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#environmentDivisionBody}.
	 * @param ctx the parse tree
	 */
	void exitEnvironmentDivisionBody(CobolIsuzuParser.EnvironmentDivisionBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#configurationSection}.
	 * @param ctx the parse tree
	 */
	void enterConfigurationSection(CobolIsuzuParser.ConfigurationSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#configurationSection}.
	 * @param ctx the parse tree
	 */
	void exitConfigurationSection(CobolIsuzuParser.ConfigurationSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#configurationSectionParagraph}.
	 * @param ctx the parse tree
	 */
	void enterConfigurationSectionParagraph(CobolIsuzuParser.ConfigurationSectionParagraphContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#configurationSectionParagraph}.
	 * @param ctx the parse tree
	 */
	void exitConfigurationSectionParagraph(CobolIsuzuParser.ConfigurationSectionParagraphContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#subSchemaParagraph}.
	 * @param ctx the parse tree
	 */
	void enterSubSchemaParagraph(CobolIsuzuParser.SubSchemaParagraphContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#subSchemaParagraph}.
	 * @param ctx the parse tree
	 */
	void exitSubSchemaParagraph(CobolIsuzuParser.SubSchemaParagraphContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#sourceComputerParagraph}.
	 * @param ctx the parse tree
	 */
	void enterSourceComputerParagraph(CobolIsuzuParser.SourceComputerParagraphContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#sourceComputerParagraph}.
	 * @param ctx the parse tree
	 */
	void exitSourceComputerParagraph(CobolIsuzuParser.SourceComputerParagraphContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#objectComputerParagraph}.
	 * @param ctx the parse tree
	 */
	void enterObjectComputerParagraph(CobolIsuzuParser.ObjectComputerParagraphContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#objectComputerParagraph}.
	 * @param ctx the parse tree
	 */
	void exitObjectComputerParagraph(CobolIsuzuParser.ObjectComputerParagraphContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#objectComputerClause}.
	 * @param ctx the parse tree
	 */
	void enterObjectComputerClause(CobolIsuzuParser.ObjectComputerClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#objectComputerClause}.
	 * @param ctx the parse tree
	 */
	void exitObjectComputerClause(CobolIsuzuParser.ObjectComputerClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#memorySizeClause}.
	 * @param ctx the parse tree
	 */
	void enterMemorySizeClause(CobolIsuzuParser.MemorySizeClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#memorySizeClause}.
	 * @param ctx the parse tree
	 */
	void exitMemorySizeClause(CobolIsuzuParser.MemorySizeClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#diskSizeClause}.
	 * @param ctx the parse tree
	 */
	void enterDiskSizeClause(CobolIsuzuParser.DiskSizeClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#diskSizeClause}.
	 * @param ctx the parse tree
	 */
	void exitDiskSizeClause(CobolIsuzuParser.DiskSizeClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#collatingSequenceClause}.
	 * @param ctx the parse tree
	 */
	void enterCollatingSequenceClause(CobolIsuzuParser.CollatingSequenceClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#collatingSequenceClause}.
	 * @param ctx the parse tree
	 */
	void exitCollatingSequenceClause(CobolIsuzuParser.CollatingSequenceClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#collatingSequenceClauseAlphanumeric}.
	 * @param ctx the parse tree
	 */
	void enterCollatingSequenceClauseAlphanumeric(CobolIsuzuParser.CollatingSequenceClauseAlphanumericContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#collatingSequenceClauseAlphanumeric}.
	 * @param ctx the parse tree
	 */
	void exitCollatingSequenceClauseAlphanumeric(CobolIsuzuParser.CollatingSequenceClauseAlphanumericContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#collatingSequenceClauseNational}.
	 * @param ctx the parse tree
	 */
	void enterCollatingSequenceClauseNational(CobolIsuzuParser.CollatingSequenceClauseNationalContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#collatingSequenceClauseNational}.
	 * @param ctx the parse tree
	 */
	void exitCollatingSequenceClauseNational(CobolIsuzuParser.CollatingSequenceClauseNationalContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#segmentLimitClause}.
	 * @param ctx the parse tree
	 */
	void enterSegmentLimitClause(CobolIsuzuParser.SegmentLimitClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#segmentLimitClause}.
	 * @param ctx the parse tree
	 */
	void exitSegmentLimitClause(CobolIsuzuParser.SegmentLimitClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#characterSetClause}.
	 * @param ctx the parse tree
	 */
	void enterCharacterSetClause(CobolIsuzuParser.CharacterSetClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#characterSetClause}.
	 * @param ctx the parse tree
	 */
	void exitCharacterSetClause(CobolIsuzuParser.CharacterSetClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#specialNamesParagraph}.
	 * @param ctx the parse tree
	 */
	void enterSpecialNamesParagraph(CobolIsuzuParser.SpecialNamesParagraphContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#specialNamesParagraph}.
	 * @param ctx the parse tree
	 */
	void exitSpecialNamesParagraph(CobolIsuzuParser.SpecialNamesParagraphContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#specialNameClause}.
	 * @param ctx the parse tree
	 */
	void enterSpecialNameClause(CobolIsuzuParser.SpecialNameClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#specialNameClause}.
	 * @param ctx the parse tree
	 */
	void exitSpecialNameClause(CobolIsuzuParser.SpecialNameClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#alphabetClause}.
	 * @param ctx the parse tree
	 */
	void enterAlphabetClause(CobolIsuzuParser.AlphabetClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#alphabetClause}.
	 * @param ctx the parse tree
	 */
	void exitAlphabetClause(CobolIsuzuParser.AlphabetClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#alphabetClauseFormat1}.
	 * @param ctx the parse tree
	 */
	void enterAlphabetClauseFormat1(CobolIsuzuParser.AlphabetClauseFormat1Context ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#alphabetClauseFormat1}.
	 * @param ctx the parse tree
	 */
	void exitAlphabetClauseFormat1(CobolIsuzuParser.AlphabetClauseFormat1Context ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#alphabetLiterals}.
	 * @param ctx the parse tree
	 */
	void enterAlphabetLiterals(CobolIsuzuParser.AlphabetLiteralsContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#alphabetLiterals}.
	 * @param ctx the parse tree
	 */
	void exitAlphabetLiterals(CobolIsuzuParser.AlphabetLiteralsContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#alphabetThrough}.
	 * @param ctx the parse tree
	 */
	void enterAlphabetThrough(CobolIsuzuParser.AlphabetThroughContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#alphabetThrough}.
	 * @param ctx the parse tree
	 */
	void exitAlphabetThrough(CobolIsuzuParser.AlphabetThroughContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#alphabetAlso}.
	 * @param ctx the parse tree
	 */
	void enterAlphabetAlso(CobolIsuzuParser.AlphabetAlsoContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#alphabetAlso}.
	 * @param ctx the parse tree
	 */
	void exitAlphabetAlso(CobolIsuzuParser.AlphabetAlsoContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#alphabetClauseFormat2}.
	 * @param ctx the parse tree
	 */
	void enterAlphabetClauseFormat2(CobolIsuzuParser.AlphabetClauseFormat2Context ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#alphabetClauseFormat2}.
	 * @param ctx the parse tree
	 */
	void exitAlphabetClauseFormat2(CobolIsuzuParser.AlphabetClauseFormat2Context ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#channelClause}.
	 * @param ctx the parse tree
	 */
	void enterChannelClause(CobolIsuzuParser.ChannelClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#channelClause}.
	 * @param ctx the parse tree
	 */
	void exitChannelClause(CobolIsuzuParser.ChannelClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#classClause}.
	 * @param ctx the parse tree
	 */
	void enterClassClause(CobolIsuzuParser.ClassClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#classClause}.
	 * @param ctx the parse tree
	 */
	void exitClassClause(CobolIsuzuParser.ClassClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#classClauseThrough}.
	 * @param ctx the parse tree
	 */
	void enterClassClauseThrough(CobolIsuzuParser.ClassClauseThroughContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#classClauseThrough}.
	 * @param ctx the parse tree
	 */
	void exitClassClauseThrough(CobolIsuzuParser.ClassClauseThroughContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#classClauseFrom}.
	 * @param ctx the parse tree
	 */
	void enterClassClauseFrom(CobolIsuzuParser.ClassClauseFromContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#classClauseFrom}.
	 * @param ctx the parse tree
	 */
	void exitClassClauseFrom(CobolIsuzuParser.ClassClauseFromContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#classClauseTo}.
	 * @param ctx the parse tree
	 */
	void enterClassClauseTo(CobolIsuzuParser.ClassClauseToContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#classClauseTo}.
	 * @param ctx the parse tree
	 */
	void exitClassClauseTo(CobolIsuzuParser.ClassClauseToContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#currencySignClause}.
	 * @param ctx the parse tree
	 */
	void enterCurrencySignClause(CobolIsuzuParser.CurrencySignClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#currencySignClause}.
	 * @param ctx the parse tree
	 */
	void exitCurrencySignClause(CobolIsuzuParser.CurrencySignClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#decimalPointClause}.
	 * @param ctx the parse tree
	 */
	void enterDecimalPointClause(CobolIsuzuParser.DecimalPointClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#decimalPointClause}.
	 * @param ctx the parse tree
	 */
	void exitDecimalPointClause(CobolIsuzuParser.DecimalPointClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#defaultComputationalSignClause}.
	 * @param ctx the parse tree
	 */
	void enterDefaultComputationalSignClause(CobolIsuzuParser.DefaultComputationalSignClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#defaultComputationalSignClause}.
	 * @param ctx the parse tree
	 */
	void exitDefaultComputationalSignClause(CobolIsuzuParser.DefaultComputationalSignClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#defaultDisplaySignClause}.
	 * @param ctx the parse tree
	 */
	void enterDefaultDisplaySignClause(CobolIsuzuParser.DefaultDisplaySignClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#defaultDisplaySignClause}.
	 * @param ctx the parse tree
	 */
	void exitDefaultDisplaySignClause(CobolIsuzuParser.DefaultDisplaySignClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#environmentSwitchNameClause}.
	 * @param ctx the parse tree
	 */
	void enterEnvironmentSwitchNameClause(CobolIsuzuParser.EnvironmentSwitchNameClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#environmentSwitchNameClause}.
	 * @param ctx the parse tree
	 */
	void exitEnvironmentSwitchNameClause(CobolIsuzuParser.EnvironmentSwitchNameClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#environmentSwitchNameSpecialNamesStatusPhrase}.
	 * @param ctx the parse tree
	 */
	void enterEnvironmentSwitchNameSpecialNamesStatusPhrase(CobolIsuzuParser.EnvironmentSwitchNameSpecialNamesStatusPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#environmentSwitchNameSpecialNamesStatusPhrase}.
	 * @param ctx the parse tree
	 */
	void exitEnvironmentSwitchNameSpecialNamesStatusPhrase(CobolIsuzuParser.EnvironmentSwitchNameSpecialNamesStatusPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#odtClause}.
	 * @param ctx the parse tree
	 */
	void enterOdtClause(CobolIsuzuParser.OdtClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#odtClause}.
	 * @param ctx the parse tree
	 */
	void exitOdtClause(CobolIsuzuParser.OdtClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reserveNetworkClause}.
	 * @param ctx the parse tree
	 */
	void enterReserveNetworkClause(CobolIsuzuParser.ReserveNetworkClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reserveNetworkClause}.
	 * @param ctx the parse tree
	 */
	void exitReserveNetworkClause(CobolIsuzuParser.ReserveNetworkClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#symbolicCharactersClause}.
	 * @param ctx the parse tree
	 */
	void enterSymbolicCharactersClause(CobolIsuzuParser.SymbolicCharactersClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#symbolicCharactersClause}.
	 * @param ctx the parse tree
	 */
	void exitSymbolicCharactersClause(CobolIsuzuParser.SymbolicCharactersClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#symbolicCharacters}.
	 * @param ctx the parse tree
	 */
	void enterSymbolicCharacters(CobolIsuzuParser.SymbolicCharactersContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#symbolicCharacters}.
	 * @param ctx the parse tree
	 */
	void exitSymbolicCharacters(CobolIsuzuParser.SymbolicCharactersContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#inputOutputSection}.
	 * @param ctx the parse tree
	 */
	void enterInputOutputSection(CobolIsuzuParser.InputOutputSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#inputOutputSection}.
	 * @param ctx the parse tree
	 */
	void exitInputOutputSection(CobolIsuzuParser.InputOutputSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#inputOutputSectionParagraph}.
	 * @param ctx the parse tree
	 */
	void enterInputOutputSectionParagraph(CobolIsuzuParser.InputOutputSectionParagraphContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#inputOutputSectionParagraph}.
	 * @param ctx the parse tree
	 */
	void exitInputOutputSectionParagraph(CobolIsuzuParser.InputOutputSectionParagraphContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#fileControlParagraph}.
	 * @param ctx the parse tree
	 */
	void enterFileControlParagraph(CobolIsuzuParser.FileControlParagraphContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#fileControlParagraph}.
	 * @param ctx the parse tree
	 */
	void exitFileControlParagraph(CobolIsuzuParser.FileControlParagraphContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#fileControlEntry}.
	 * @param ctx the parse tree
	 */
	void enterFileControlEntry(CobolIsuzuParser.FileControlEntryContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#fileControlEntry}.
	 * @param ctx the parse tree
	 */
	void exitFileControlEntry(CobolIsuzuParser.FileControlEntryContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#selectClause}.
	 * @param ctx the parse tree
	 */
	void enterSelectClause(CobolIsuzuParser.SelectClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#selectClause}.
	 * @param ctx the parse tree
	 */
	void exitSelectClause(CobolIsuzuParser.SelectClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#fileControlClause}.
	 * @param ctx the parse tree
	 */
	void enterFileControlClause(CobolIsuzuParser.FileControlClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#fileControlClause}.
	 * @param ctx the parse tree
	 */
	void exitFileControlClause(CobolIsuzuParser.FileControlClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#selectedFunctionClause}.
	 * @param ctx the parse tree
	 */
	void enterSelectedFunctionClause(CobolIsuzuParser.SelectedFunctionClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#selectedFunctionClause}.
	 * @param ctx the parse tree
	 */
	void exitSelectedFunctionClause(CobolIsuzuParser.SelectedFunctionClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#assignClause}.
	 * @param ctx the parse tree
	 */
	void enterAssignClause(CobolIsuzuParser.AssignClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#assignClause}.
	 * @param ctx the parse tree
	 */
	void exitAssignClause(CobolIsuzuParser.AssignClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reserveClause}.
	 * @param ctx the parse tree
	 */
	void enterReserveClause(CobolIsuzuParser.ReserveClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reserveClause}.
	 * @param ctx the parse tree
	 */
	void exitReserveClause(CobolIsuzuParser.ReserveClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#organizationClause}.
	 * @param ctx the parse tree
	 */
	void enterOrganizationClause(CobolIsuzuParser.OrganizationClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#organizationClause}.
	 * @param ctx the parse tree
	 */
	void exitOrganizationClause(CobolIsuzuParser.OrganizationClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#destinationClause}.
	 * @param ctx the parse tree
	 */
	void enterDestinationClause(CobolIsuzuParser.DestinationClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#destinationClause}.
	 * @param ctx the parse tree
	 */
	void exitDestinationClause(CobolIsuzuParser.DestinationClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#formatClause}.
	 * @param ctx the parse tree
	 */
	void enterFormatClause(CobolIsuzuParser.FormatClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#formatClause}.
	 * @param ctx the parse tree
	 */
	void exitFormatClause(CobolIsuzuParser.FormatClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#messageModeClause}.
	 * @param ctx the parse tree
	 */
	void enterMessageModeClause(CobolIsuzuParser.MessageModeClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#messageModeClause}.
	 * @param ctx the parse tree
	 */
	void exitMessageModeClause(CobolIsuzuParser.MessageModeClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#paddingCharacterClause}.
	 * @param ctx the parse tree
	 */
	void enterPaddingCharacterClause(CobolIsuzuParser.PaddingCharacterClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#paddingCharacterClause}.
	 * @param ctx the parse tree
	 */
	void exitPaddingCharacterClause(CobolIsuzuParser.PaddingCharacterClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#recordDelimiterClause}.
	 * @param ctx the parse tree
	 */
	void enterRecordDelimiterClause(CobolIsuzuParser.RecordDelimiterClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#recordDelimiterClause}.
	 * @param ctx the parse tree
	 */
	void exitRecordDelimiterClause(CobolIsuzuParser.RecordDelimiterClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#accessModeClause}.
	 * @param ctx the parse tree
	 */
	void enterAccessModeClause(CobolIsuzuParser.AccessModeClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#accessModeClause}.
	 * @param ctx the parse tree
	 */
	void exitAccessModeClause(CobolIsuzuParser.AccessModeClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#recordKeyClause}.
	 * @param ctx the parse tree
	 */
	void enterRecordKeyClause(CobolIsuzuParser.RecordKeyClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#recordKeyClause}.
	 * @param ctx the parse tree
	 */
	void exitRecordKeyClause(CobolIsuzuParser.RecordKeyClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#alternateRecordKeyClause}.
	 * @param ctx the parse tree
	 */
	void enterAlternateRecordKeyClause(CobolIsuzuParser.AlternateRecordKeyClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#alternateRecordKeyClause}.
	 * @param ctx the parse tree
	 */
	void exitAlternateRecordKeyClause(CobolIsuzuParser.AlternateRecordKeyClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#passwordClause}.
	 * @param ctx the parse tree
	 */
	void enterPasswordClause(CobolIsuzuParser.PasswordClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#passwordClause}.
	 * @param ctx the parse tree
	 */
	void exitPasswordClause(CobolIsuzuParser.PasswordClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#fileStatusClause}.
	 * @param ctx the parse tree
	 */
	void enterFileStatusClause(CobolIsuzuParser.FileStatusClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#fileStatusClause}.
	 * @param ctx the parse tree
	 */
	void exitFileStatusClause(CobolIsuzuParser.FileStatusClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#relativeKeyClause}.
	 * @param ctx the parse tree
	 */
	void enterRelativeKeyClause(CobolIsuzuParser.RelativeKeyClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#relativeKeyClause}.
	 * @param ctx the parse tree
	 */
	void exitRelativeKeyClause(CobolIsuzuParser.RelativeKeyClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#sessionControlClause}.
	 * @param ctx the parse tree
	 */
	void enterSessionControlClause(CobolIsuzuParser.SessionControlClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#sessionControlClause}.
	 * @param ctx the parse tree
	 */
	void exitSessionControlClause(CobolIsuzuParser.SessionControlClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#ioControlParagraph}.
	 * @param ctx the parse tree
	 */
	void enterIoControlParagraph(CobolIsuzuParser.IoControlParagraphContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#ioControlParagraph}.
	 * @param ctx the parse tree
	 */
	void exitIoControlParagraph(CobolIsuzuParser.IoControlParagraphContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#ioControlClause}.
	 * @param ctx the parse tree
	 */
	void enterIoControlClause(CobolIsuzuParser.IoControlClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#ioControlClause}.
	 * @param ctx the parse tree
	 */
	void exitIoControlClause(CobolIsuzuParser.IoControlClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#applyClause}.
	 * @param ctx the parse tree
	 */
	void enterApplyClause(CobolIsuzuParser.ApplyClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#applyClause}.
	 * @param ctx the parse tree
	 */
	void exitApplyClause(CobolIsuzuParser.ApplyClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#rerunClause}.
	 * @param ctx the parse tree
	 */
	void enterRerunClause(CobolIsuzuParser.RerunClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#rerunClause}.
	 * @param ctx the parse tree
	 */
	void exitRerunClause(CobolIsuzuParser.RerunClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#rerunEveryRecords}.
	 * @param ctx the parse tree
	 */
	void enterRerunEveryRecords(CobolIsuzuParser.RerunEveryRecordsContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#rerunEveryRecords}.
	 * @param ctx the parse tree
	 */
	void exitRerunEveryRecords(CobolIsuzuParser.RerunEveryRecordsContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#rerunEveryOf}.
	 * @param ctx the parse tree
	 */
	void enterRerunEveryOf(CobolIsuzuParser.RerunEveryOfContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#rerunEveryOf}.
	 * @param ctx the parse tree
	 */
	void exitRerunEveryOf(CobolIsuzuParser.RerunEveryOfContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#rerunEveryClock}.
	 * @param ctx the parse tree
	 */
	void enterRerunEveryClock(CobolIsuzuParser.RerunEveryClockContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#rerunEveryClock}.
	 * @param ctx the parse tree
	 */
	void exitRerunEveryClock(CobolIsuzuParser.RerunEveryClockContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#sameClause}.
	 * @param ctx the parse tree
	 */
	void enterSameClause(CobolIsuzuParser.SameClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#sameClause}.
	 * @param ctx the parse tree
	 */
	void exitSameClause(CobolIsuzuParser.SameClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#multipleFileClause}.
	 * @param ctx the parse tree
	 */
	void enterMultipleFileClause(CobolIsuzuParser.MultipleFileClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#multipleFileClause}.
	 * @param ctx the parse tree
	 */
	void exitMultipleFileClause(CobolIsuzuParser.MultipleFileClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#multipleFilePosition}.
	 * @param ctx the parse tree
	 */
	void enterMultipleFilePosition(CobolIsuzuParser.MultipleFilePositionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#multipleFilePosition}.
	 * @param ctx the parse tree
	 */
	void exitMultipleFilePosition(CobolIsuzuParser.MultipleFilePositionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#commitmentControlClause}.
	 * @param ctx the parse tree
	 */
	void enterCommitmentControlClause(CobolIsuzuParser.CommitmentControlClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#commitmentControlClause}.
	 * @param ctx the parse tree
	 */
	void exitCommitmentControlClause(CobolIsuzuParser.CommitmentControlClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataDivision}.
	 * @param ctx the parse tree
	 */
	void enterDataDivision(CobolIsuzuParser.DataDivisionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataDivision}.
	 * @param ctx the parse tree
	 */
	void exitDataDivision(CobolIsuzuParser.DataDivisionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataDivisionSection}.
	 * @param ctx the parse tree
	 */
	void enterDataDivisionSection(CobolIsuzuParser.DataDivisionSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataDivisionSection}.
	 * @param ctx the parse tree
	 */
	void exitDataDivisionSection(CobolIsuzuParser.DataDivisionSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#fileSection}.
	 * @param ctx the parse tree
	 */
	void enterFileSection(CobolIsuzuParser.FileSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#fileSection}.
	 * @param ctx the parse tree
	 */
	void exitFileSection(CobolIsuzuParser.FileSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#fileDescriptionEntry}.
	 * @param ctx the parse tree
	 */
	void enterFileDescriptionEntry(CobolIsuzuParser.FileDescriptionEntryContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#fileDescriptionEntry}.
	 * @param ctx the parse tree
	 */
	void exitFileDescriptionEntry(CobolIsuzuParser.FileDescriptionEntryContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#fileDescriptionEntryClause}.
	 * @param ctx the parse tree
	 */
	void enterFileDescriptionEntryClause(CobolIsuzuParser.FileDescriptionEntryClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#fileDescriptionEntryClause}.
	 * @param ctx the parse tree
	 */
	void exitFileDescriptionEntryClause(CobolIsuzuParser.FileDescriptionEntryClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#externalClause}.
	 * @param ctx the parse tree
	 */
	void enterExternalClause(CobolIsuzuParser.ExternalClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#externalClause}.
	 * @param ctx the parse tree
	 */
	void exitExternalClause(CobolIsuzuParser.ExternalClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#globalClause}.
	 * @param ctx the parse tree
	 */
	void enterGlobalClause(CobolIsuzuParser.GlobalClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#globalClause}.
	 * @param ctx the parse tree
	 */
	void exitGlobalClause(CobolIsuzuParser.GlobalClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#blockContainsClause}.
	 * @param ctx the parse tree
	 */
	void enterBlockContainsClause(CobolIsuzuParser.BlockContainsClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#blockContainsClause}.
	 * @param ctx the parse tree
	 */
	void exitBlockContainsClause(CobolIsuzuParser.BlockContainsClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#blockContainsTo}.
	 * @param ctx the parse tree
	 */
	void enterBlockContainsTo(CobolIsuzuParser.BlockContainsToContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#blockContainsTo}.
	 * @param ctx the parse tree
	 */
	void exitBlockContainsTo(CobolIsuzuParser.BlockContainsToContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#recordContainsClause}.
	 * @param ctx the parse tree
	 */
	void enterRecordContainsClause(CobolIsuzuParser.RecordContainsClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#recordContainsClause}.
	 * @param ctx the parse tree
	 */
	void exitRecordContainsClause(CobolIsuzuParser.RecordContainsClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#recordContainsClauseFormat1}.
	 * @param ctx the parse tree
	 */
	void enterRecordContainsClauseFormat1(CobolIsuzuParser.RecordContainsClauseFormat1Context ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#recordContainsClauseFormat1}.
	 * @param ctx the parse tree
	 */
	void exitRecordContainsClauseFormat1(CobolIsuzuParser.RecordContainsClauseFormat1Context ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#recordContainsClauseFormat2}.
	 * @param ctx the parse tree
	 */
	void enterRecordContainsClauseFormat2(CobolIsuzuParser.RecordContainsClauseFormat2Context ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#recordContainsClauseFormat2}.
	 * @param ctx the parse tree
	 */
	void exitRecordContainsClauseFormat2(CobolIsuzuParser.RecordContainsClauseFormat2Context ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#recordContainsClauseFormat3}.
	 * @param ctx the parse tree
	 */
	void enterRecordContainsClauseFormat3(CobolIsuzuParser.RecordContainsClauseFormat3Context ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#recordContainsClauseFormat3}.
	 * @param ctx the parse tree
	 */
	void exitRecordContainsClauseFormat3(CobolIsuzuParser.RecordContainsClauseFormat3Context ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#recordContainsTo}.
	 * @param ctx the parse tree
	 */
	void enterRecordContainsTo(CobolIsuzuParser.RecordContainsToContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#recordContainsTo}.
	 * @param ctx the parse tree
	 */
	void exitRecordContainsTo(CobolIsuzuParser.RecordContainsToContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#labelRecordsClause}.
	 * @param ctx the parse tree
	 */
	void enterLabelRecordsClause(CobolIsuzuParser.LabelRecordsClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#labelRecordsClause}.
	 * @param ctx the parse tree
	 */
	void exitLabelRecordsClause(CobolIsuzuParser.LabelRecordsClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#valueOfClause}.
	 * @param ctx the parse tree
	 */
	void enterValueOfClause(CobolIsuzuParser.ValueOfClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#valueOfClause}.
	 * @param ctx the parse tree
	 */
	void exitValueOfClause(CobolIsuzuParser.ValueOfClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#valuePair}.
	 * @param ctx the parse tree
	 */
	void enterValuePair(CobolIsuzuParser.ValuePairContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#valuePair}.
	 * @param ctx the parse tree
	 */
	void exitValuePair(CobolIsuzuParser.ValuePairContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataRecordsClause}.
	 * @param ctx the parse tree
	 */
	void enterDataRecordsClause(CobolIsuzuParser.DataRecordsClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataRecordsClause}.
	 * @param ctx the parse tree
	 */
	void exitDataRecordsClause(CobolIsuzuParser.DataRecordsClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#linageClause}.
	 * @param ctx the parse tree
	 */
	void enterLinageClause(CobolIsuzuParser.LinageClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#linageClause}.
	 * @param ctx the parse tree
	 */
	void exitLinageClause(CobolIsuzuParser.LinageClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#linageAt}.
	 * @param ctx the parse tree
	 */
	void enterLinageAt(CobolIsuzuParser.LinageAtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#linageAt}.
	 * @param ctx the parse tree
	 */
	void exitLinageAt(CobolIsuzuParser.LinageAtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#linageFootingAt}.
	 * @param ctx the parse tree
	 */
	void enterLinageFootingAt(CobolIsuzuParser.LinageFootingAtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#linageFootingAt}.
	 * @param ctx the parse tree
	 */
	void exitLinageFootingAt(CobolIsuzuParser.LinageFootingAtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#linageLinesAtTop}.
	 * @param ctx the parse tree
	 */
	void enterLinageLinesAtTop(CobolIsuzuParser.LinageLinesAtTopContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#linageLinesAtTop}.
	 * @param ctx the parse tree
	 */
	void exitLinageLinesAtTop(CobolIsuzuParser.LinageLinesAtTopContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#linageLinesAtBottom}.
	 * @param ctx the parse tree
	 */
	void enterLinageLinesAtBottom(CobolIsuzuParser.LinageLinesAtBottomContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#linageLinesAtBottom}.
	 * @param ctx the parse tree
	 */
	void exitLinageLinesAtBottom(CobolIsuzuParser.LinageLinesAtBottomContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#recordingModeClause}.
	 * @param ctx the parse tree
	 */
	void enterRecordingModeClause(CobolIsuzuParser.RecordingModeClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#recordingModeClause}.
	 * @param ctx the parse tree
	 */
	void exitRecordingModeClause(CobolIsuzuParser.RecordingModeClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#modeStatement}.
	 * @param ctx the parse tree
	 */
	void enterModeStatement(CobolIsuzuParser.ModeStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#modeStatement}.
	 * @param ctx the parse tree
	 */
	void exitModeStatement(CobolIsuzuParser.ModeStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#codeSetClause}.
	 * @param ctx the parse tree
	 */
	void enterCodeSetClause(CobolIsuzuParser.CodeSetClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#codeSetClause}.
	 * @param ctx the parse tree
	 */
	void exitCodeSetClause(CobolIsuzuParser.CodeSetClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportClause}.
	 * @param ctx the parse tree
	 */
	void enterReportClause(CobolIsuzuParser.ReportClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportClause}.
	 * @param ctx the parse tree
	 */
	void exitReportClause(CobolIsuzuParser.ReportClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataBaseSection}.
	 * @param ctx the parse tree
	 */
	void enterDataBaseSection(CobolIsuzuParser.DataBaseSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataBaseSection}.
	 * @param ctx the parse tree
	 */
	void exitDataBaseSection(CobolIsuzuParser.DataBaseSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataBaseSectionEntry}.
	 * @param ctx the parse tree
	 */
	void enterDataBaseSectionEntry(CobolIsuzuParser.DataBaseSectionEntryContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataBaseSectionEntry}.
	 * @param ctx the parse tree
	 */
	void exitDataBaseSectionEntry(CobolIsuzuParser.DataBaseSectionEntryContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#workingStorageSection}.
	 * @param ctx the parse tree
	 */
	void enterWorkingStorageSection(CobolIsuzuParser.WorkingStorageSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#workingStorageSection}.
	 * @param ctx the parse tree
	 */
	void exitWorkingStorageSection(CobolIsuzuParser.WorkingStorageSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#constantSection}.
	 * @param ctx the parse tree
	 */
	void enterConstantSection(CobolIsuzuParser.ConstantSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#constantSection}.
	 * @param ctx the parse tree
	 */
	void exitConstantSection(CobolIsuzuParser.ConstantSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#linkageSection}.
	 * @param ctx the parse tree
	 */
	void enterLinkageSection(CobolIsuzuParser.LinkageSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#linkageSection}.
	 * @param ctx the parse tree
	 */
	void exitLinkageSection(CobolIsuzuParser.LinkageSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#communicationSection}.
	 * @param ctx the parse tree
	 */
	void enterCommunicationSection(CobolIsuzuParser.CommunicationSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#communicationSection}.
	 * @param ctx the parse tree
	 */
	void exitCommunicationSection(CobolIsuzuParser.CommunicationSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#communicationDescriptionEntry}.
	 * @param ctx the parse tree
	 */
	void enterCommunicationDescriptionEntry(CobolIsuzuParser.CommunicationDescriptionEntryContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#communicationDescriptionEntry}.
	 * @param ctx the parse tree
	 */
	void exitCommunicationDescriptionEntry(CobolIsuzuParser.CommunicationDescriptionEntryContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#communicationDescriptionEntryFormat1}.
	 * @param ctx the parse tree
	 */
	void enterCommunicationDescriptionEntryFormat1(CobolIsuzuParser.CommunicationDescriptionEntryFormat1Context ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#communicationDescriptionEntryFormat1}.
	 * @param ctx the parse tree
	 */
	void exitCommunicationDescriptionEntryFormat1(CobolIsuzuParser.CommunicationDescriptionEntryFormat1Context ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#communicationDescriptionEntryFormat2}.
	 * @param ctx the parse tree
	 */
	void enterCommunicationDescriptionEntryFormat2(CobolIsuzuParser.CommunicationDescriptionEntryFormat2Context ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#communicationDescriptionEntryFormat2}.
	 * @param ctx the parse tree
	 */
	void exitCommunicationDescriptionEntryFormat2(CobolIsuzuParser.CommunicationDescriptionEntryFormat2Context ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#communicationDescriptionEntryFormat3}.
	 * @param ctx the parse tree
	 */
	void enterCommunicationDescriptionEntryFormat3(CobolIsuzuParser.CommunicationDescriptionEntryFormat3Context ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#communicationDescriptionEntryFormat3}.
	 * @param ctx the parse tree
	 */
	void exitCommunicationDescriptionEntryFormat3(CobolIsuzuParser.CommunicationDescriptionEntryFormat3Context ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#destinationCountClause}.
	 * @param ctx the parse tree
	 */
	void enterDestinationCountClause(CobolIsuzuParser.DestinationCountClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#destinationCountClause}.
	 * @param ctx the parse tree
	 */
	void exitDestinationCountClause(CobolIsuzuParser.DestinationCountClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#destinationTableClause}.
	 * @param ctx the parse tree
	 */
	void enterDestinationTableClause(CobolIsuzuParser.DestinationTableClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#destinationTableClause}.
	 * @param ctx the parse tree
	 */
	void exitDestinationTableClause(CobolIsuzuParser.DestinationTableClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#endKeyClause}.
	 * @param ctx the parse tree
	 */
	void enterEndKeyClause(CobolIsuzuParser.EndKeyClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#endKeyClause}.
	 * @param ctx the parse tree
	 */
	void exitEndKeyClause(CobolIsuzuParser.EndKeyClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#errorKeyClause}.
	 * @param ctx the parse tree
	 */
	void enterErrorKeyClause(CobolIsuzuParser.ErrorKeyClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#errorKeyClause}.
	 * @param ctx the parse tree
	 */
	void exitErrorKeyClause(CobolIsuzuParser.ErrorKeyClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#messageCountClause}.
	 * @param ctx the parse tree
	 */
	void enterMessageCountClause(CobolIsuzuParser.MessageCountClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#messageCountClause}.
	 * @param ctx the parse tree
	 */
	void exitMessageCountClause(CobolIsuzuParser.MessageCountClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#messageDateClause}.
	 * @param ctx the parse tree
	 */
	void enterMessageDateClause(CobolIsuzuParser.MessageDateClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#messageDateClause}.
	 * @param ctx the parse tree
	 */
	void exitMessageDateClause(CobolIsuzuParser.MessageDateClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#messageTimeClause}.
	 * @param ctx the parse tree
	 */
	void enterMessageTimeClause(CobolIsuzuParser.MessageTimeClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#messageTimeClause}.
	 * @param ctx the parse tree
	 */
	void exitMessageTimeClause(CobolIsuzuParser.MessageTimeClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#statusKeyClause}.
	 * @param ctx the parse tree
	 */
	void enterStatusKeyClause(CobolIsuzuParser.StatusKeyClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#statusKeyClause}.
	 * @param ctx the parse tree
	 */
	void exitStatusKeyClause(CobolIsuzuParser.StatusKeyClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#symbolicDestinationClause}.
	 * @param ctx the parse tree
	 */
	void enterSymbolicDestinationClause(CobolIsuzuParser.SymbolicDestinationClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#symbolicDestinationClause}.
	 * @param ctx the parse tree
	 */
	void exitSymbolicDestinationClause(CobolIsuzuParser.SymbolicDestinationClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#symbolicQueueClause}.
	 * @param ctx the parse tree
	 */
	void enterSymbolicQueueClause(CobolIsuzuParser.SymbolicQueueClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#symbolicQueueClause}.
	 * @param ctx the parse tree
	 */
	void exitSymbolicQueueClause(CobolIsuzuParser.SymbolicQueueClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#symbolicSourceClause}.
	 * @param ctx the parse tree
	 */
	void enterSymbolicSourceClause(CobolIsuzuParser.SymbolicSourceClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#symbolicSourceClause}.
	 * @param ctx the parse tree
	 */
	void exitSymbolicSourceClause(CobolIsuzuParser.SymbolicSourceClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#symbolicTerminalClause}.
	 * @param ctx the parse tree
	 */
	void enterSymbolicTerminalClause(CobolIsuzuParser.SymbolicTerminalClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#symbolicTerminalClause}.
	 * @param ctx the parse tree
	 */
	void exitSymbolicTerminalClause(CobolIsuzuParser.SymbolicTerminalClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#symbolicSubQueueClause}.
	 * @param ctx the parse tree
	 */
	void enterSymbolicSubQueueClause(CobolIsuzuParser.SymbolicSubQueueClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#symbolicSubQueueClause}.
	 * @param ctx the parse tree
	 */
	void exitSymbolicSubQueueClause(CobolIsuzuParser.SymbolicSubQueueClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#textLengthClause}.
	 * @param ctx the parse tree
	 */
	void enterTextLengthClause(CobolIsuzuParser.TextLengthClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#textLengthClause}.
	 * @param ctx the parse tree
	 */
	void exitTextLengthClause(CobolIsuzuParser.TextLengthClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#localStorageSection}.
	 * @param ctx the parse tree
	 */
	void enterLocalStorageSection(CobolIsuzuParser.LocalStorageSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#localStorageSection}.
	 * @param ctx the parse tree
	 */
	void exitLocalStorageSection(CobolIsuzuParser.LocalStorageSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenSection}.
	 * @param ctx the parse tree
	 */
	void enterScreenSection(CobolIsuzuParser.ScreenSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenSection}.
	 * @param ctx the parse tree
	 */
	void exitScreenSection(CobolIsuzuParser.ScreenSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenDescriptionEntry}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionEntry(CobolIsuzuParser.ScreenDescriptionEntryContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenDescriptionEntry}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionEntry(CobolIsuzuParser.ScreenDescriptionEntryContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenDescriptionBlankClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionBlankClause(CobolIsuzuParser.ScreenDescriptionBlankClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenDescriptionBlankClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionBlankClause(CobolIsuzuParser.ScreenDescriptionBlankClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenDescriptionBellClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionBellClause(CobolIsuzuParser.ScreenDescriptionBellClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenDescriptionBellClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionBellClause(CobolIsuzuParser.ScreenDescriptionBellClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenDescriptionBlinkClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionBlinkClause(CobolIsuzuParser.ScreenDescriptionBlinkClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenDescriptionBlinkClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionBlinkClause(CobolIsuzuParser.ScreenDescriptionBlinkClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenDescriptionEraseClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionEraseClause(CobolIsuzuParser.ScreenDescriptionEraseClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenDescriptionEraseClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionEraseClause(CobolIsuzuParser.ScreenDescriptionEraseClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenDescriptionLightClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionLightClause(CobolIsuzuParser.ScreenDescriptionLightClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenDescriptionLightClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionLightClause(CobolIsuzuParser.ScreenDescriptionLightClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenDescriptionGridClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionGridClause(CobolIsuzuParser.ScreenDescriptionGridClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenDescriptionGridClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionGridClause(CobolIsuzuParser.ScreenDescriptionGridClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenDescriptionReverseVideoClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionReverseVideoClause(CobolIsuzuParser.ScreenDescriptionReverseVideoClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenDescriptionReverseVideoClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionReverseVideoClause(CobolIsuzuParser.ScreenDescriptionReverseVideoClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenDescriptionUnderlineClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionUnderlineClause(CobolIsuzuParser.ScreenDescriptionUnderlineClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenDescriptionUnderlineClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionUnderlineClause(CobolIsuzuParser.ScreenDescriptionUnderlineClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenDescriptionSizeClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionSizeClause(CobolIsuzuParser.ScreenDescriptionSizeClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenDescriptionSizeClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionSizeClause(CobolIsuzuParser.ScreenDescriptionSizeClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenDescriptionLineClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionLineClause(CobolIsuzuParser.ScreenDescriptionLineClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenDescriptionLineClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionLineClause(CobolIsuzuParser.ScreenDescriptionLineClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenDescriptionColumnClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionColumnClause(CobolIsuzuParser.ScreenDescriptionColumnClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenDescriptionColumnClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionColumnClause(CobolIsuzuParser.ScreenDescriptionColumnClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenDescriptionForegroundColorClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionForegroundColorClause(CobolIsuzuParser.ScreenDescriptionForegroundColorClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenDescriptionForegroundColorClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionForegroundColorClause(CobolIsuzuParser.ScreenDescriptionForegroundColorClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenDescriptionBackgroundColorClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionBackgroundColorClause(CobolIsuzuParser.ScreenDescriptionBackgroundColorClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenDescriptionBackgroundColorClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionBackgroundColorClause(CobolIsuzuParser.ScreenDescriptionBackgroundColorClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenDescriptionControlClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionControlClause(CobolIsuzuParser.ScreenDescriptionControlClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenDescriptionControlClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionControlClause(CobolIsuzuParser.ScreenDescriptionControlClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenDescriptionValueClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionValueClause(CobolIsuzuParser.ScreenDescriptionValueClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenDescriptionValueClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionValueClause(CobolIsuzuParser.ScreenDescriptionValueClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenDescriptionPictureClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionPictureClause(CobolIsuzuParser.ScreenDescriptionPictureClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenDescriptionPictureClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionPictureClause(CobolIsuzuParser.ScreenDescriptionPictureClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenDescriptionFromClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionFromClause(CobolIsuzuParser.ScreenDescriptionFromClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenDescriptionFromClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionFromClause(CobolIsuzuParser.ScreenDescriptionFromClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenDescriptionToClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionToClause(CobolIsuzuParser.ScreenDescriptionToClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenDescriptionToClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionToClause(CobolIsuzuParser.ScreenDescriptionToClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenDescriptionUsingClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionUsingClause(CobolIsuzuParser.ScreenDescriptionUsingClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenDescriptionUsingClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionUsingClause(CobolIsuzuParser.ScreenDescriptionUsingClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenDescriptionUsageClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionUsageClause(CobolIsuzuParser.ScreenDescriptionUsageClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenDescriptionUsageClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionUsageClause(CobolIsuzuParser.ScreenDescriptionUsageClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenDescriptionBlankWhenZeroClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionBlankWhenZeroClause(CobolIsuzuParser.ScreenDescriptionBlankWhenZeroClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenDescriptionBlankWhenZeroClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionBlankWhenZeroClause(CobolIsuzuParser.ScreenDescriptionBlankWhenZeroClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenDescriptionJustifiedClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionJustifiedClause(CobolIsuzuParser.ScreenDescriptionJustifiedClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenDescriptionJustifiedClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionJustifiedClause(CobolIsuzuParser.ScreenDescriptionJustifiedClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenDescriptionSignClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionSignClause(CobolIsuzuParser.ScreenDescriptionSignClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenDescriptionSignClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionSignClause(CobolIsuzuParser.ScreenDescriptionSignClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenDescriptionAutoClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionAutoClause(CobolIsuzuParser.ScreenDescriptionAutoClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenDescriptionAutoClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionAutoClause(CobolIsuzuParser.ScreenDescriptionAutoClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenDescriptionSecureClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionSecureClause(CobolIsuzuParser.ScreenDescriptionSecureClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenDescriptionSecureClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionSecureClause(CobolIsuzuParser.ScreenDescriptionSecureClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenDescriptionRequiredClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionRequiredClause(CobolIsuzuParser.ScreenDescriptionRequiredClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenDescriptionRequiredClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionRequiredClause(CobolIsuzuParser.ScreenDescriptionRequiredClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenDescriptionPromptClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionPromptClause(CobolIsuzuParser.ScreenDescriptionPromptClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenDescriptionPromptClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionPromptClause(CobolIsuzuParser.ScreenDescriptionPromptClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenDescriptionPromptOccursClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionPromptOccursClause(CobolIsuzuParser.ScreenDescriptionPromptOccursClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenDescriptionPromptOccursClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionPromptOccursClause(CobolIsuzuParser.ScreenDescriptionPromptOccursClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenDescriptionFullClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionFullClause(CobolIsuzuParser.ScreenDescriptionFullClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenDescriptionFullClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionFullClause(CobolIsuzuParser.ScreenDescriptionFullClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenDescriptionZeroFillClause}.
	 * @param ctx the parse tree
	 */
	void enterScreenDescriptionZeroFillClause(CobolIsuzuParser.ScreenDescriptionZeroFillClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenDescriptionZeroFillClause}.
	 * @param ctx the parse tree
	 */
	void exitScreenDescriptionZeroFillClause(CobolIsuzuParser.ScreenDescriptionZeroFillClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportSection}.
	 * @param ctx the parse tree
	 */
	void enterReportSection(CobolIsuzuParser.ReportSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportSection}.
	 * @param ctx the parse tree
	 */
	void exitReportSection(CobolIsuzuParser.ReportSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportDescription}.
	 * @param ctx the parse tree
	 */
	void enterReportDescription(CobolIsuzuParser.ReportDescriptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportDescription}.
	 * @param ctx the parse tree
	 */
	void exitReportDescription(CobolIsuzuParser.ReportDescriptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportDescriptionEntry}.
	 * @param ctx the parse tree
	 */
	void enterReportDescriptionEntry(CobolIsuzuParser.ReportDescriptionEntryContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportDescriptionEntry}.
	 * @param ctx the parse tree
	 */
	void exitReportDescriptionEntry(CobolIsuzuParser.ReportDescriptionEntryContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportDescriptionGlobalClause}.
	 * @param ctx the parse tree
	 */
	void enterReportDescriptionGlobalClause(CobolIsuzuParser.ReportDescriptionGlobalClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportDescriptionGlobalClause}.
	 * @param ctx the parse tree
	 */
	void exitReportDescriptionGlobalClause(CobolIsuzuParser.ReportDescriptionGlobalClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportDescriptionPageLimitClause}.
	 * @param ctx the parse tree
	 */
	void enterReportDescriptionPageLimitClause(CobolIsuzuParser.ReportDescriptionPageLimitClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportDescriptionPageLimitClause}.
	 * @param ctx the parse tree
	 */
	void exitReportDescriptionPageLimitClause(CobolIsuzuParser.ReportDescriptionPageLimitClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportDescriptionHeadingClause}.
	 * @param ctx the parse tree
	 */
	void enterReportDescriptionHeadingClause(CobolIsuzuParser.ReportDescriptionHeadingClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportDescriptionHeadingClause}.
	 * @param ctx the parse tree
	 */
	void exitReportDescriptionHeadingClause(CobolIsuzuParser.ReportDescriptionHeadingClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportDescriptionFirstDetailClause}.
	 * @param ctx the parse tree
	 */
	void enterReportDescriptionFirstDetailClause(CobolIsuzuParser.ReportDescriptionFirstDetailClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportDescriptionFirstDetailClause}.
	 * @param ctx the parse tree
	 */
	void exitReportDescriptionFirstDetailClause(CobolIsuzuParser.ReportDescriptionFirstDetailClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportDescriptionLastDetailClause}.
	 * @param ctx the parse tree
	 */
	void enterReportDescriptionLastDetailClause(CobolIsuzuParser.ReportDescriptionLastDetailClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportDescriptionLastDetailClause}.
	 * @param ctx the parse tree
	 */
	void exitReportDescriptionLastDetailClause(CobolIsuzuParser.ReportDescriptionLastDetailClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportDescriptionFootingClause}.
	 * @param ctx the parse tree
	 */
	void enterReportDescriptionFootingClause(CobolIsuzuParser.ReportDescriptionFootingClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportDescriptionFootingClause}.
	 * @param ctx the parse tree
	 */
	void exitReportDescriptionFootingClause(CobolIsuzuParser.ReportDescriptionFootingClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportGroupDescriptionEntry}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupDescriptionEntry(CobolIsuzuParser.ReportGroupDescriptionEntryContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportGroupDescriptionEntry}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupDescriptionEntry(CobolIsuzuParser.ReportGroupDescriptionEntryContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportGroupDescriptionEntryFormat1}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupDescriptionEntryFormat1(CobolIsuzuParser.ReportGroupDescriptionEntryFormat1Context ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportGroupDescriptionEntryFormat1}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupDescriptionEntryFormat1(CobolIsuzuParser.ReportGroupDescriptionEntryFormat1Context ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportGroupDescriptionEntryFormat2}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupDescriptionEntryFormat2(CobolIsuzuParser.ReportGroupDescriptionEntryFormat2Context ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportGroupDescriptionEntryFormat2}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupDescriptionEntryFormat2(CobolIsuzuParser.ReportGroupDescriptionEntryFormat2Context ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportGroupDescriptionEntryFormat3}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupDescriptionEntryFormat3(CobolIsuzuParser.ReportGroupDescriptionEntryFormat3Context ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportGroupDescriptionEntryFormat3}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupDescriptionEntryFormat3(CobolIsuzuParser.ReportGroupDescriptionEntryFormat3Context ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportGroupBlankWhenZeroClause}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupBlankWhenZeroClause(CobolIsuzuParser.ReportGroupBlankWhenZeroClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportGroupBlankWhenZeroClause}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupBlankWhenZeroClause(CobolIsuzuParser.ReportGroupBlankWhenZeroClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportGroupColumnNumberClause}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupColumnNumberClause(CobolIsuzuParser.ReportGroupColumnNumberClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportGroupColumnNumberClause}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupColumnNumberClause(CobolIsuzuParser.ReportGroupColumnNumberClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportGroupIndicateClause}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupIndicateClause(CobolIsuzuParser.ReportGroupIndicateClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportGroupIndicateClause}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupIndicateClause(CobolIsuzuParser.ReportGroupIndicateClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportGroupJustifiedClause}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupJustifiedClause(CobolIsuzuParser.ReportGroupJustifiedClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportGroupJustifiedClause}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupJustifiedClause(CobolIsuzuParser.ReportGroupJustifiedClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportGroupLineNumberClause}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupLineNumberClause(CobolIsuzuParser.ReportGroupLineNumberClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportGroupLineNumberClause}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupLineNumberClause(CobolIsuzuParser.ReportGroupLineNumberClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportGroupLineNumberNextPage}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupLineNumberNextPage(CobolIsuzuParser.ReportGroupLineNumberNextPageContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportGroupLineNumberNextPage}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupLineNumberNextPage(CobolIsuzuParser.ReportGroupLineNumberNextPageContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportGroupLineNumberPlus}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupLineNumberPlus(CobolIsuzuParser.ReportGroupLineNumberPlusContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportGroupLineNumberPlus}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupLineNumberPlus(CobolIsuzuParser.ReportGroupLineNumberPlusContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportGroupNextGroupClause}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupNextGroupClause(CobolIsuzuParser.ReportGroupNextGroupClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportGroupNextGroupClause}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupNextGroupClause(CobolIsuzuParser.ReportGroupNextGroupClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportGroupNextGroupPlus}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupNextGroupPlus(CobolIsuzuParser.ReportGroupNextGroupPlusContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportGroupNextGroupPlus}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupNextGroupPlus(CobolIsuzuParser.ReportGroupNextGroupPlusContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportGroupNextGroupNextPage}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupNextGroupNextPage(CobolIsuzuParser.ReportGroupNextGroupNextPageContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportGroupNextGroupNextPage}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupNextGroupNextPage(CobolIsuzuParser.ReportGroupNextGroupNextPageContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportGroupPictureClause}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupPictureClause(CobolIsuzuParser.ReportGroupPictureClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportGroupPictureClause}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupPictureClause(CobolIsuzuParser.ReportGroupPictureClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportGroupResetClause}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupResetClause(CobolIsuzuParser.ReportGroupResetClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportGroupResetClause}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupResetClause(CobolIsuzuParser.ReportGroupResetClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportGroupSignClause}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupSignClause(CobolIsuzuParser.ReportGroupSignClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportGroupSignClause}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupSignClause(CobolIsuzuParser.ReportGroupSignClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportGroupSourceClause}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupSourceClause(CobolIsuzuParser.ReportGroupSourceClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportGroupSourceClause}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupSourceClause(CobolIsuzuParser.ReportGroupSourceClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportGroupSumClause}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupSumClause(CobolIsuzuParser.ReportGroupSumClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportGroupSumClause}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupSumClause(CobolIsuzuParser.ReportGroupSumClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportGroupTypeClause}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupTypeClause(CobolIsuzuParser.ReportGroupTypeClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportGroupTypeClause}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupTypeClause(CobolIsuzuParser.ReportGroupTypeClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportGroupTypeReportHeading}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupTypeReportHeading(CobolIsuzuParser.ReportGroupTypeReportHeadingContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportGroupTypeReportHeading}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupTypeReportHeading(CobolIsuzuParser.ReportGroupTypeReportHeadingContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportGroupTypePageHeading}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupTypePageHeading(CobolIsuzuParser.ReportGroupTypePageHeadingContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportGroupTypePageHeading}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupTypePageHeading(CobolIsuzuParser.ReportGroupTypePageHeadingContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportGroupTypeControlHeading}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupTypeControlHeading(CobolIsuzuParser.ReportGroupTypeControlHeadingContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportGroupTypeControlHeading}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupTypeControlHeading(CobolIsuzuParser.ReportGroupTypeControlHeadingContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportGroupTypeDetail}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupTypeDetail(CobolIsuzuParser.ReportGroupTypeDetailContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportGroupTypeDetail}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupTypeDetail(CobolIsuzuParser.ReportGroupTypeDetailContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportGroupTypeControlFooting}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupTypeControlFooting(CobolIsuzuParser.ReportGroupTypeControlFootingContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportGroupTypeControlFooting}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupTypeControlFooting(CobolIsuzuParser.ReportGroupTypeControlFootingContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportGroupUsageClause}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupUsageClause(CobolIsuzuParser.ReportGroupUsageClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportGroupUsageClause}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupUsageClause(CobolIsuzuParser.ReportGroupUsageClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportGroupTypePageFooting}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupTypePageFooting(CobolIsuzuParser.ReportGroupTypePageFootingContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportGroupTypePageFooting}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupTypePageFooting(CobolIsuzuParser.ReportGroupTypePageFootingContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportGroupTypeReportFooting}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupTypeReportFooting(CobolIsuzuParser.ReportGroupTypeReportFootingContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportGroupTypeReportFooting}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupTypeReportFooting(CobolIsuzuParser.ReportGroupTypeReportFootingContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportGroupValueClause}.
	 * @param ctx the parse tree
	 */
	void enterReportGroupValueClause(CobolIsuzuParser.ReportGroupValueClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportGroupValueClause}.
	 * @param ctx the parse tree
	 */
	void exitReportGroupValueClause(CobolIsuzuParser.ReportGroupValueClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#programLibrarySection}.
	 * @param ctx the parse tree
	 */
	void enterProgramLibrarySection(CobolIsuzuParser.ProgramLibrarySectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#programLibrarySection}.
	 * @param ctx the parse tree
	 */
	void exitProgramLibrarySection(CobolIsuzuParser.ProgramLibrarySectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#libraryDescriptionEntry}.
	 * @param ctx the parse tree
	 */
	void enterLibraryDescriptionEntry(CobolIsuzuParser.LibraryDescriptionEntryContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#libraryDescriptionEntry}.
	 * @param ctx the parse tree
	 */
	void exitLibraryDescriptionEntry(CobolIsuzuParser.LibraryDescriptionEntryContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#libraryDescriptionEntryFormat1}.
	 * @param ctx the parse tree
	 */
	void enterLibraryDescriptionEntryFormat1(CobolIsuzuParser.LibraryDescriptionEntryFormat1Context ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#libraryDescriptionEntryFormat1}.
	 * @param ctx the parse tree
	 */
	void exitLibraryDescriptionEntryFormat1(CobolIsuzuParser.LibraryDescriptionEntryFormat1Context ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#libraryDescriptionEntryFormat2}.
	 * @param ctx the parse tree
	 */
	void enterLibraryDescriptionEntryFormat2(CobolIsuzuParser.LibraryDescriptionEntryFormat2Context ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#libraryDescriptionEntryFormat2}.
	 * @param ctx the parse tree
	 */
	void exitLibraryDescriptionEntryFormat2(CobolIsuzuParser.LibraryDescriptionEntryFormat2Context ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#libraryAttributeClauseFormat1}.
	 * @param ctx the parse tree
	 */
	void enterLibraryAttributeClauseFormat1(CobolIsuzuParser.LibraryAttributeClauseFormat1Context ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#libraryAttributeClauseFormat1}.
	 * @param ctx the parse tree
	 */
	void exitLibraryAttributeClauseFormat1(CobolIsuzuParser.LibraryAttributeClauseFormat1Context ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#libraryAttributeClauseFormat2}.
	 * @param ctx the parse tree
	 */
	void enterLibraryAttributeClauseFormat2(CobolIsuzuParser.LibraryAttributeClauseFormat2Context ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#libraryAttributeClauseFormat2}.
	 * @param ctx the parse tree
	 */
	void exitLibraryAttributeClauseFormat2(CobolIsuzuParser.LibraryAttributeClauseFormat2Context ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#libraryAttributeFunction}.
	 * @param ctx the parse tree
	 */
	void enterLibraryAttributeFunction(CobolIsuzuParser.LibraryAttributeFunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#libraryAttributeFunction}.
	 * @param ctx the parse tree
	 */
	void exitLibraryAttributeFunction(CobolIsuzuParser.LibraryAttributeFunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#libraryAttributeParameter}.
	 * @param ctx the parse tree
	 */
	void enterLibraryAttributeParameter(CobolIsuzuParser.LibraryAttributeParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#libraryAttributeParameter}.
	 * @param ctx the parse tree
	 */
	void exitLibraryAttributeParameter(CobolIsuzuParser.LibraryAttributeParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#libraryAttributeTitle}.
	 * @param ctx the parse tree
	 */
	void enterLibraryAttributeTitle(CobolIsuzuParser.LibraryAttributeTitleContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#libraryAttributeTitle}.
	 * @param ctx the parse tree
	 */
	void exitLibraryAttributeTitle(CobolIsuzuParser.LibraryAttributeTitleContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#libraryEntryProcedureClauseFormat1}.
	 * @param ctx the parse tree
	 */
	void enterLibraryEntryProcedureClauseFormat1(CobolIsuzuParser.LibraryEntryProcedureClauseFormat1Context ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#libraryEntryProcedureClauseFormat1}.
	 * @param ctx the parse tree
	 */
	void exitLibraryEntryProcedureClauseFormat1(CobolIsuzuParser.LibraryEntryProcedureClauseFormat1Context ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#libraryEntryProcedureClauseFormat2}.
	 * @param ctx the parse tree
	 */
	void enterLibraryEntryProcedureClauseFormat2(CobolIsuzuParser.LibraryEntryProcedureClauseFormat2Context ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#libraryEntryProcedureClauseFormat2}.
	 * @param ctx the parse tree
	 */
	void exitLibraryEntryProcedureClauseFormat2(CobolIsuzuParser.LibraryEntryProcedureClauseFormat2Context ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#libraryEntryProcedureForClause}.
	 * @param ctx the parse tree
	 */
	void enterLibraryEntryProcedureForClause(CobolIsuzuParser.LibraryEntryProcedureForClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#libraryEntryProcedureForClause}.
	 * @param ctx the parse tree
	 */
	void exitLibraryEntryProcedureForClause(CobolIsuzuParser.LibraryEntryProcedureForClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#libraryEntryProcedureGivingClause}.
	 * @param ctx the parse tree
	 */
	void enterLibraryEntryProcedureGivingClause(CobolIsuzuParser.LibraryEntryProcedureGivingClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#libraryEntryProcedureGivingClause}.
	 * @param ctx the parse tree
	 */
	void exitLibraryEntryProcedureGivingClause(CobolIsuzuParser.LibraryEntryProcedureGivingClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#libraryEntryProcedureUsingClause}.
	 * @param ctx the parse tree
	 */
	void enterLibraryEntryProcedureUsingClause(CobolIsuzuParser.LibraryEntryProcedureUsingClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#libraryEntryProcedureUsingClause}.
	 * @param ctx the parse tree
	 */
	void exitLibraryEntryProcedureUsingClause(CobolIsuzuParser.LibraryEntryProcedureUsingClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#libraryEntryProcedureUsingName}.
	 * @param ctx the parse tree
	 */
	void enterLibraryEntryProcedureUsingName(CobolIsuzuParser.LibraryEntryProcedureUsingNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#libraryEntryProcedureUsingName}.
	 * @param ctx the parse tree
	 */
	void exitLibraryEntryProcedureUsingName(CobolIsuzuParser.LibraryEntryProcedureUsingNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#libraryEntryProcedureWithClause}.
	 * @param ctx the parse tree
	 */
	void enterLibraryEntryProcedureWithClause(CobolIsuzuParser.LibraryEntryProcedureWithClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#libraryEntryProcedureWithClause}.
	 * @param ctx the parse tree
	 */
	void exitLibraryEntryProcedureWithClause(CobolIsuzuParser.LibraryEntryProcedureWithClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#libraryEntryProcedureWithName}.
	 * @param ctx the parse tree
	 */
	void enterLibraryEntryProcedureWithName(CobolIsuzuParser.LibraryEntryProcedureWithNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#libraryEntryProcedureWithName}.
	 * @param ctx the parse tree
	 */
	void exitLibraryEntryProcedureWithName(CobolIsuzuParser.LibraryEntryProcedureWithNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#libraryIsCommonClause}.
	 * @param ctx the parse tree
	 */
	void enterLibraryIsCommonClause(CobolIsuzuParser.LibraryIsCommonClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#libraryIsCommonClause}.
	 * @param ctx the parse tree
	 */
	void exitLibraryIsCommonClause(CobolIsuzuParser.LibraryIsCommonClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#libraryIsGlobalClause}.
	 * @param ctx the parse tree
	 */
	void enterLibraryIsGlobalClause(CobolIsuzuParser.LibraryIsGlobalClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#libraryIsGlobalClause}.
	 * @param ctx the parse tree
	 */
	void exitLibraryIsGlobalClause(CobolIsuzuParser.LibraryIsGlobalClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataDescriptionEntry}.
	 * @param ctx the parse tree
	 */
	void enterDataDescriptionEntry(CobolIsuzuParser.DataDescriptionEntryContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataDescriptionEntry}.
	 * @param ctx the parse tree
	 */
	void exitDataDescriptionEntry(CobolIsuzuParser.DataDescriptionEntryContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#copyStatement}.
	 * @param ctx the parse tree
	 */
	void enterCopyStatement(CobolIsuzuParser.CopyStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#copyStatement}.
	 * @param ctx the parse tree
	 */
	void exitCopyStatement(CobolIsuzuParser.CopyStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#disjoinPhrase}.
	 * @param ctx the parse tree
	 */
	void enterDisjoinPhrase(CobolIsuzuParser.DisjoinPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#disjoinPhrase}.
	 * @param ctx the parse tree
	 */
	void exitDisjoinPhrase(CobolIsuzuParser.DisjoinPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#joinPhrase}.
	 * @param ctx the parse tree
	 */
	void enterJoinPhrase(CobolIsuzuParser.JoinPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#joinPhrase}.
	 * @param ctx the parse tree
	 */
	void exitJoinPhrase(CobolIsuzuParser.JoinPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#copySource}.
	 * @param ctx the parse tree
	 */
	void enterCopySource(CobolIsuzuParser.CopySourceContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#copySource}.
	 * @param ctx the parse tree
	 */
	void exitCopySource(CobolIsuzuParser.CopySourceContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#copyLibrary}.
	 * @param ctx the parse tree
	 */
	void enterCopyLibrary(CobolIsuzuParser.CopyLibraryContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#copyLibrary}.
	 * @param ctx the parse tree
	 */
	void exitCopyLibrary(CobolIsuzuParser.CopyLibraryContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#replacingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterReplacingPhrase(CobolIsuzuParser.ReplacingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#replacingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitReplacingPhrase(CobolIsuzuParser.ReplacingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#replaceArea}.
	 * @param ctx the parse tree
	 */
	void enterReplaceArea(CobolIsuzuParser.ReplaceAreaContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#replaceArea}.
	 * @param ctx the parse tree
	 */
	void exitReplaceArea(CobolIsuzuParser.ReplaceAreaContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#replaceByStatement}.
	 * @param ctx the parse tree
	 */
	void enterReplaceByStatement(CobolIsuzuParser.ReplaceByStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#replaceByStatement}.
	 * @param ctx the parse tree
	 */
	void exitReplaceByStatement(CobolIsuzuParser.ReplaceByStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#replaceOffStatement}.
	 * @param ctx the parse tree
	 */
	void enterReplaceOffStatement(CobolIsuzuParser.ReplaceOffStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#replaceOffStatement}.
	 * @param ctx the parse tree
	 */
	void exitReplaceOffStatement(CobolIsuzuParser.ReplaceOffStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#replaceClause}.
	 * @param ctx the parse tree
	 */
	void enterReplaceClause(CobolIsuzuParser.ReplaceClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#replaceClause}.
	 * @param ctx the parse tree
	 */
	void exitReplaceClause(CobolIsuzuParser.ReplaceClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#directoryPhrase}.
	 * @param ctx the parse tree
	 */
	void enterDirectoryPhrase(CobolIsuzuParser.DirectoryPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#directoryPhrase}.
	 * @param ctx the parse tree
	 */
	void exitDirectoryPhrase(CobolIsuzuParser.DirectoryPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#familyPhrase}.
	 * @param ctx the parse tree
	 */
	void enterFamilyPhrase(CobolIsuzuParser.FamilyPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#familyPhrase}.
	 * @param ctx the parse tree
	 */
	void exitFamilyPhrase(CobolIsuzuParser.FamilyPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#replaceable}.
	 * @param ctx the parse tree
	 */
	void enterReplaceable(CobolIsuzuParser.ReplaceableContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#replaceable}.
	 * @param ctx the parse tree
	 */
	void exitReplaceable(CobolIsuzuParser.ReplaceableContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#replacement}.
	 * @param ctx the parse tree
	 */
	void enterReplacement(CobolIsuzuParser.ReplacementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#replacement}.
	 * @param ctx the parse tree
	 */
	void exitReplacement(CobolIsuzuParser.ReplacementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#ejectStatement}.
	 * @param ctx the parse tree
	 */
	void enterEjectStatement(CobolIsuzuParser.EjectStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#ejectStatement}.
	 * @param ctx the parse tree
	 */
	void exitEjectStatement(CobolIsuzuParser.EjectStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#skipStatement}.
	 * @param ctx the parse tree
	 */
	void enterSkipStatement(CobolIsuzuParser.SkipStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#skipStatement}.
	 * @param ctx the parse tree
	 */
	void exitSkipStatement(CobolIsuzuParser.SkipStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#titleStatement}.
	 * @param ctx the parse tree
	 */
	void enterTitleStatement(CobolIsuzuParser.TitleStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#titleStatement}.
	 * @param ctx the parse tree
	 */
	void exitTitleStatement(CobolIsuzuParser.TitleStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#pseudoText}.
	 * @param ctx the parse tree
	 */
	void enterPseudoText(CobolIsuzuParser.PseudoTextContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#pseudoText}.
	 * @param ctx the parse tree
	 */
	void exitPseudoText(CobolIsuzuParser.PseudoTextContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#charData}.
	 * @param ctx the parse tree
	 */
	void enterCharData(CobolIsuzuParser.CharDataContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#charData}.
	 * @param ctx the parse tree
	 */
	void exitCharData(CobolIsuzuParser.CharDataContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#charDataSql}.
	 * @param ctx the parse tree
	 */
	void enterCharDataSql(CobolIsuzuParser.CharDataSqlContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#charDataSql}.
	 * @param ctx the parse tree
	 */
	void exitCharDataSql(CobolIsuzuParser.CharDataSqlContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#charDataLine}.
	 * @param ctx the parse tree
	 */
	void enterCharDataLine(CobolIsuzuParser.CharDataLineContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#charDataLine}.
	 * @param ctx the parse tree
	 */
	void exitCharDataLine(CobolIsuzuParser.CharDataLineContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#cobolWord}.
	 * @param ctx the parse tree
	 */
	void enterCobolWord(CobolIsuzuParser.CobolWordContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#cobolWord}.
	 * @param ctx the parse tree
	 */
	void exitCobolWord(CobolIsuzuParser.CobolWordContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(CobolIsuzuParser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(CobolIsuzuParser.LiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#jpEncodingText}.
	 * @param ctx the parse tree
	 */
	void enterJpEncodingText(CobolIsuzuParser.JpEncodingTextContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#jpEncodingText}.
	 * @param ctx the parse tree
	 */
	void exitJpEncodingText(CobolIsuzuParser.JpEncodingTextContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#filename}.
	 * @param ctx the parse tree
	 */
	void enterFilename(CobolIsuzuParser.FilenameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#filename}.
	 * @param ctx the parse tree
	 */
	void exitFilename(CobolIsuzuParser.FilenameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataDescriptionEntryFormat1}.
	 * @param ctx the parse tree
	 */
	void enterDataDescriptionEntryFormat1(CobolIsuzuParser.DataDescriptionEntryFormat1Context ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataDescriptionEntryFormat1}.
	 * @param ctx the parse tree
	 */
	void exitDataDescriptionEntryFormat1(CobolIsuzuParser.DataDescriptionEntryFormat1Context ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataPrintClause}.
	 * @param ctx the parse tree
	 */
	void enterDataPrintClause(CobolIsuzuParser.DataPrintClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataPrintClause}.
	 * @param ctx the parse tree
	 */
	void exitDataPrintClause(CobolIsuzuParser.DataPrintClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataCharacterClause}.
	 * @param ctx the parse tree
	 */
	void enterDataCharacterClause(CobolIsuzuParser.DataCharacterClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataCharacterClause}.
	 * @param ctx the parse tree
	 */
	void exitDataCharacterClause(CobolIsuzuParser.DataCharacterClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataDescriptionEntryFormat3}.
	 * @param ctx the parse tree
	 */
	void enterDataDescriptionEntryFormat3(CobolIsuzuParser.DataDescriptionEntryFormat3Context ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataDescriptionEntryFormat3}.
	 * @param ctx the parse tree
	 */
	void exitDataDescriptionEntryFormat3(CobolIsuzuParser.DataDescriptionEntryFormat3Context ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataDescriptionEntryFormat2}.
	 * @param ctx the parse tree
	 */
	void enterDataDescriptionEntryFormat2(CobolIsuzuParser.DataDescriptionEntryFormat2Context ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataDescriptionEntryFormat2}.
	 * @param ctx the parse tree
	 */
	void exitDataDescriptionEntryFormat2(CobolIsuzuParser.DataDescriptionEntryFormat2Context ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataDescriptionEntryExecSql}.
	 * @param ctx the parse tree
	 */
	void enterDataDescriptionEntryExecSql(CobolIsuzuParser.DataDescriptionEntryExecSqlContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataDescriptionEntryExecSql}.
	 * @param ctx the parse tree
	 */
	void exitDataDescriptionEntryExecSql(CobolIsuzuParser.DataDescriptionEntryExecSqlContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataAlignedClause}.
	 * @param ctx the parse tree
	 */
	void enterDataAlignedClause(CobolIsuzuParser.DataAlignedClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataAlignedClause}.
	 * @param ctx the parse tree
	 */
	void exitDataAlignedClause(CobolIsuzuParser.DataAlignedClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataBlankWhenZeroClause}.
	 * @param ctx the parse tree
	 */
	void enterDataBlankWhenZeroClause(CobolIsuzuParser.DataBlankWhenZeroClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataBlankWhenZeroClause}.
	 * @param ctx the parse tree
	 */
	void exitDataBlankWhenZeroClause(CobolIsuzuParser.DataBlankWhenZeroClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataCommonOwnLocalClause}.
	 * @param ctx the parse tree
	 */
	void enterDataCommonOwnLocalClause(CobolIsuzuParser.DataCommonOwnLocalClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataCommonOwnLocalClause}.
	 * @param ctx the parse tree
	 */
	void exitDataCommonOwnLocalClause(CobolIsuzuParser.DataCommonOwnLocalClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataExternalClause}.
	 * @param ctx the parse tree
	 */
	void enterDataExternalClause(CobolIsuzuParser.DataExternalClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataExternalClause}.
	 * @param ctx the parse tree
	 */
	void exitDataExternalClause(CobolIsuzuParser.DataExternalClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataGlobalClause}.
	 * @param ctx the parse tree
	 */
	void enterDataGlobalClause(CobolIsuzuParser.DataGlobalClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataGlobalClause}.
	 * @param ctx the parse tree
	 */
	void exitDataGlobalClause(CobolIsuzuParser.DataGlobalClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataIntegerStringClause}.
	 * @param ctx the parse tree
	 */
	void enterDataIntegerStringClause(CobolIsuzuParser.DataIntegerStringClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataIntegerStringClause}.
	 * @param ctx the parse tree
	 */
	void exitDataIntegerStringClause(CobolIsuzuParser.DataIntegerStringClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataJustifiedClause}.
	 * @param ctx the parse tree
	 */
	void enterDataJustifiedClause(CobolIsuzuParser.DataJustifiedClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataJustifiedClause}.
	 * @param ctx the parse tree
	 */
	void exitDataJustifiedClause(CobolIsuzuParser.DataJustifiedClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataOccursClause}.
	 * @param ctx the parse tree
	 */
	void enterDataOccursClause(CobolIsuzuParser.DataOccursClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataOccursClause}.
	 * @param ctx the parse tree
	 */
	void exitDataOccursClause(CobolIsuzuParser.DataOccursClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataOccursTo}.
	 * @param ctx the parse tree
	 */
	void enterDataOccursTo(CobolIsuzuParser.DataOccursToContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataOccursTo}.
	 * @param ctx the parse tree
	 */
	void exitDataOccursTo(CobolIsuzuParser.DataOccursToContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataOccursSort}.
	 * @param ctx the parse tree
	 */
	void enterDataOccursSort(CobolIsuzuParser.DataOccursSortContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataOccursSort}.
	 * @param ctx the parse tree
	 */
	void exitDataOccursSort(CobolIsuzuParser.DataOccursSortContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataPictureClause}.
	 * @param ctx the parse tree
	 */
	void enterDataPictureClause(CobolIsuzuParser.DataPictureClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataPictureClause}.
	 * @param ctx the parse tree
	 */
	void exitDataPictureClause(CobolIsuzuParser.DataPictureClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#pictureString}.
	 * @param ctx the parse tree
	 */
	void enterPictureString(CobolIsuzuParser.PictureStringContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#pictureString}.
	 * @param ctx the parse tree
	 */
	void exitPictureString(CobolIsuzuParser.PictureStringContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#pictureChars}.
	 * @param ctx the parse tree
	 */
	void enterPictureChars(CobolIsuzuParser.PictureCharsContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#pictureChars}.
	 * @param ctx the parse tree
	 */
	void exitPictureChars(CobolIsuzuParser.PictureCharsContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#pictureCardinality}.
	 * @param ctx the parse tree
	 */
	void enterPictureCardinality(CobolIsuzuParser.PictureCardinalityContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#pictureCardinality}.
	 * @param ctx the parse tree
	 */
	void exitPictureCardinality(CobolIsuzuParser.PictureCardinalityContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataReceivedByClause}.
	 * @param ctx the parse tree
	 */
	void enterDataReceivedByClause(CobolIsuzuParser.DataReceivedByClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataReceivedByClause}.
	 * @param ctx the parse tree
	 */
	void exitDataReceivedByClause(CobolIsuzuParser.DataReceivedByClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataRecordAreaClause}.
	 * @param ctx the parse tree
	 */
	void enterDataRecordAreaClause(CobolIsuzuParser.DataRecordAreaClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataRecordAreaClause}.
	 * @param ctx the parse tree
	 */
	void exitDataRecordAreaClause(CobolIsuzuParser.DataRecordAreaClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataRedefinesClause}.
	 * @param ctx the parse tree
	 */
	void enterDataRedefinesClause(CobolIsuzuParser.DataRedefinesClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataRedefinesClause}.
	 * @param ctx the parse tree
	 */
	void exitDataRedefinesClause(CobolIsuzuParser.DataRedefinesClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataRenamesClause}.
	 * @param ctx the parse tree
	 */
	void enterDataRenamesClause(CobolIsuzuParser.DataRenamesClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataRenamesClause}.
	 * @param ctx the parse tree
	 */
	void exitDataRenamesClause(CobolIsuzuParser.DataRenamesClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataSignClause}.
	 * @param ctx the parse tree
	 */
	void enterDataSignClause(CobolIsuzuParser.DataSignClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataSignClause}.
	 * @param ctx the parse tree
	 */
	void exitDataSignClause(CobolIsuzuParser.DataSignClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataSynchronizedClause}.
	 * @param ctx the parse tree
	 */
	void enterDataSynchronizedClause(CobolIsuzuParser.DataSynchronizedClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataSynchronizedClause}.
	 * @param ctx the parse tree
	 */
	void exitDataSynchronizedClause(CobolIsuzuParser.DataSynchronizedClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataThreadLocalClause}.
	 * @param ctx the parse tree
	 */
	void enterDataThreadLocalClause(CobolIsuzuParser.DataThreadLocalClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataThreadLocalClause}.
	 * @param ctx the parse tree
	 */
	void exitDataThreadLocalClause(CobolIsuzuParser.DataThreadLocalClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataTypeClause}.
	 * @param ctx the parse tree
	 */
	void enterDataTypeClause(CobolIsuzuParser.DataTypeClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataTypeClause}.
	 * @param ctx the parse tree
	 */
	void exitDataTypeClause(CobolIsuzuParser.DataTypeClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataTypeDefClause}.
	 * @param ctx the parse tree
	 */
	void enterDataTypeDefClause(CobolIsuzuParser.DataTypeDefClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataTypeDefClause}.
	 * @param ctx the parse tree
	 */
	void exitDataTypeDefClause(CobolIsuzuParser.DataTypeDefClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataUsageClause}.
	 * @param ctx the parse tree
	 */
	void enterDataUsageClause(CobolIsuzuParser.DataUsageClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataUsageClause}.
	 * @param ctx the parse tree
	 */
	void exitDataUsageClause(CobolIsuzuParser.DataUsageClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataUsingClause}.
	 * @param ctx the parse tree
	 */
	void enterDataUsingClause(CobolIsuzuParser.DataUsingClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataUsingClause}.
	 * @param ctx the parse tree
	 */
	void exitDataUsingClause(CobolIsuzuParser.DataUsingClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataValueClause}.
	 * @param ctx the parse tree
	 */
	void enterDataValueClause(CobolIsuzuParser.DataValueClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataValueClause}.
	 * @param ctx the parse tree
	 */
	void exitDataValueClause(CobolIsuzuParser.DataValueClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataValueInterval}.
	 * @param ctx the parse tree
	 */
	void enterDataValueInterval(CobolIsuzuParser.DataValueIntervalContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataValueInterval}.
	 * @param ctx the parse tree
	 */
	void exitDataValueInterval(CobolIsuzuParser.DataValueIntervalContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataValueIntervalFrom}.
	 * @param ctx the parse tree
	 */
	void enterDataValueIntervalFrom(CobolIsuzuParser.DataValueIntervalFromContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataValueIntervalFrom}.
	 * @param ctx the parse tree
	 */
	void exitDataValueIntervalFrom(CobolIsuzuParser.DataValueIntervalFromContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataValueIntervalTo}.
	 * @param ctx the parse tree
	 */
	void enterDataValueIntervalTo(CobolIsuzuParser.DataValueIntervalToContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataValueIntervalTo}.
	 * @param ctx the parse tree
	 */
	void exitDataValueIntervalTo(CobolIsuzuParser.DataValueIntervalToContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataWithLowerBoundsClause}.
	 * @param ctx the parse tree
	 */
	void enterDataWithLowerBoundsClause(CobolIsuzuParser.DataWithLowerBoundsClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataWithLowerBoundsClause}.
	 * @param ctx the parse tree
	 */
	void exitDataWithLowerBoundsClause(CobolIsuzuParser.DataWithLowerBoundsClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#procedureDivision}.
	 * @param ctx the parse tree
	 */
	void enterProcedureDivision(CobolIsuzuParser.ProcedureDivisionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#procedureDivision}.
	 * @param ctx the parse tree
	 */
	void exitProcedureDivision(CobolIsuzuParser.ProcedureDivisionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#procedureDivisionUsingClause}.
	 * @param ctx the parse tree
	 */
	void enterProcedureDivisionUsingClause(CobolIsuzuParser.ProcedureDivisionUsingClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#procedureDivisionUsingClause}.
	 * @param ctx the parse tree
	 */
	void exitProcedureDivisionUsingClause(CobolIsuzuParser.ProcedureDivisionUsingClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#procedureDivisionGivingClause}.
	 * @param ctx the parse tree
	 */
	void enterProcedureDivisionGivingClause(CobolIsuzuParser.ProcedureDivisionGivingClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#procedureDivisionGivingClause}.
	 * @param ctx the parse tree
	 */
	void exitProcedureDivisionGivingClause(CobolIsuzuParser.ProcedureDivisionGivingClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#procedureDivisionUsingParameter}.
	 * @param ctx the parse tree
	 */
	void enterProcedureDivisionUsingParameter(CobolIsuzuParser.ProcedureDivisionUsingParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#procedureDivisionUsingParameter}.
	 * @param ctx the parse tree
	 */
	void exitProcedureDivisionUsingParameter(CobolIsuzuParser.ProcedureDivisionUsingParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#procedureDivisionByReferencePhrase}.
	 * @param ctx the parse tree
	 */
	void enterProcedureDivisionByReferencePhrase(CobolIsuzuParser.ProcedureDivisionByReferencePhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#procedureDivisionByReferencePhrase}.
	 * @param ctx the parse tree
	 */
	void exitProcedureDivisionByReferencePhrase(CobolIsuzuParser.ProcedureDivisionByReferencePhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#procedureDivisionByReference}.
	 * @param ctx the parse tree
	 */
	void enterProcedureDivisionByReference(CobolIsuzuParser.ProcedureDivisionByReferenceContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#procedureDivisionByReference}.
	 * @param ctx the parse tree
	 */
	void exitProcedureDivisionByReference(CobolIsuzuParser.ProcedureDivisionByReferenceContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#procedureDivisionByValuePhrase}.
	 * @param ctx the parse tree
	 */
	void enterProcedureDivisionByValuePhrase(CobolIsuzuParser.ProcedureDivisionByValuePhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#procedureDivisionByValuePhrase}.
	 * @param ctx the parse tree
	 */
	void exitProcedureDivisionByValuePhrase(CobolIsuzuParser.ProcedureDivisionByValuePhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#procedureDivisionByValue}.
	 * @param ctx the parse tree
	 */
	void enterProcedureDivisionByValue(CobolIsuzuParser.ProcedureDivisionByValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#procedureDivisionByValue}.
	 * @param ctx the parse tree
	 */
	void exitProcedureDivisionByValue(CobolIsuzuParser.ProcedureDivisionByValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#procedureDeclaratives}.
	 * @param ctx the parse tree
	 */
	void enterProcedureDeclaratives(CobolIsuzuParser.ProcedureDeclarativesContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#procedureDeclaratives}.
	 * @param ctx the parse tree
	 */
	void exitProcedureDeclaratives(CobolIsuzuParser.ProcedureDeclarativesContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#procedureDeclarative}.
	 * @param ctx the parse tree
	 */
	void enterProcedureDeclarative(CobolIsuzuParser.ProcedureDeclarativeContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#procedureDeclarative}.
	 * @param ctx the parse tree
	 */
	void exitProcedureDeclarative(CobolIsuzuParser.ProcedureDeclarativeContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#procedureSectionHeader}.
	 * @param ctx the parse tree
	 */
	void enterProcedureSectionHeader(CobolIsuzuParser.ProcedureSectionHeaderContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#procedureSectionHeader}.
	 * @param ctx the parse tree
	 */
	void exitProcedureSectionHeader(CobolIsuzuParser.ProcedureSectionHeaderContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#procedureDivisionBody}.
	 * @param ctx the parse tree
	 */
	void enterProcedureDivisionBody(CobolIsuzuParser.ProcedureDivisionBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#procedureDivisionBody}.
	 * @param ctx the parse tree
	 */
	void exitProcedureDivisionBody(CobolIsuzuParser.ProcedureDivisionBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#procedureSection}.
	 * @param ctx the parse tree
	 */
	void enterProcedureSection(CobolIsuzuParser.ProcedureSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#procedureSection}.
	 * @param ctx the parse tree
	 */
	void exitProcedureSection(CobolIsuzuParser.ProcedureSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#paragraphs}.
	 * @param ctx the parse tree
	 */
	void enterParagraphs(CobolIsuzuParser.ParagraphsContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#paragraphs}.
	 * @param ctx the parse tree
	 */
	void exitParagraphs(CobolIsuzuParser.ParagraphsContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#paragraph}.
	 * @param ctx the parse tree
	 */
	void enterParagraph(CobolIsuzuParser.ParagraphContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#paragraph}.
	 * @param ctx the parse tree
	 */
	void exitParagraph(CobolIsuzuParser.ParagraphContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#sentence}.
	 * @param ctx the parse tree
	 */
	void enterSentence(CobolIsuzuParser.SentenceContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#sentence}.
	 * @param ctx the parse tree
	 */
	void exitSentence(CobolIsuzuParser.SentenceContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(CobolIsuzuParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(CobolIsuzuParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#findStatement}.
	 * @param ctx the parse tree
	 */
	void enterFindStatement(CobolIsuzuParser.FindStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#findStatement}.
	 * @param ctx the parse tree
	 */
	void exitFindStatement(CobolIsuzuParser.FindStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#viaClause}.
	 * @param ctx the parse tree
	 */
	void enterViaClause(CobolIsuzuParser.ViaClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#viaClause}.
	 * @param ctx the parse tree
	 */
	void exitViaClause(CobolIsuzuParser.ViaClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#findOption}.
	 * @param ctx the parse tree
	 */
	void enterFindOption(CobolIsuzuParser.FindOptionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#findOption}.
	 * @param ctx the parse tree
	 */
	void exitFindOption(CobolIsuzuParser.FindOptionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#getStatement}.
	 * @param ctx the parse tree
	 */
	void enterGetStatement(CobolIsuzuParser.GetStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#getStatement}.
	 * @param ctx the parse tree
	 */
	void exitGetStatement(CobolIsuzuParser.GetStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#finishStatement}.
	 * @param ctx the parse tree
	 */
	void enterFinishStatement(CobolIsuzuParser.FinishStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#finishStatement}.
	 * @param ctx the parse tree
	 */
	void exitFinishStatement(CobolIsuzuParser.FinishStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#eraseStatement}.
	 * @param ctx the parse tree
	 */
	void enterEraseStatement(CobolIsuzuParser.EraseStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#eraseStatement}.
	 * @param ctx the parse tree
	 */
	void exitEraseStatement(CobolIsuzuParser.EraseStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#storeStatement}.
	 * @param ctx the parse tree
	 */
	void enterStoreStatement(CobolIsuzuParser.StoreStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#storeStatement}.
	 * @param ctx the parse tree
	 */
	void exitStoreStatement(CobolIsuzuParser.StoreStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#storeSendingArea}.
	 * @param ctx the parse tree
	 */
	void enterStoreSendingArea(CobolIsuzuParser.StoreSendingAreaContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#storeSendingArea}.
	 * @param ctx the parse tree
	 */
	void exitStoreSendingArea(CobolIsuzuParser.StoreSendingAreaContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#storeToArea}.
	 * @param ctx the parse tree
	 */
	void enterStoreToArea(CobolIsuzuParser.StoreToAreaContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#storeToArea}.
	 * @param ctx the parse tree
	 */
	void exitStoreToArea(CobolIsuzuParser.StoreToAreaContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#modifyStatement}.
	 * @param ctx the parse tree
	 */
	void enterModifyStatement(CobolIsuzuParser.ModifyStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#modifyStatement}.
	 * @param ctx the parse tree
	 */
	void exitModifyStatement(CobolIsuzuParser.ModifyStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#readyStatement}.
	 * @param ctx the parse tree
	 */
	void enterReadyStatement(CobolIsuzuParser.ReadyStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#readyStatement}.
	 * @param ctx the parse tree
	 */
	void exitReadyStatement(CobolIsuzuParser.ReadyStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#transactionEndStatement}.
	 * @param ctx the parse tree
	 */
	void enterTransactionEndStatement(CobolIsuzuParser.TransactionEndStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#transactionEndStatement}.
	 * @param ctx the parse tree
	 */
	void exitTransactionEndStatement(CobolIsuzuParser.TransactionEndStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#execCicsStatement2}.
	 * @param ctx the parse tree
	 */
	void enterExecCicsStatement2(CobolIsuzuParser.ExecCicsStatement2Context ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#execCicsStatement2}.
	 * @param ctx the parse tree
	 */
	void exitExecCicsStatement2(CobolIsuzuParser.ExecCicsStatement2Context ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#acceptStatement}.
	 * @param ctx the parse tree
	 */
	void enterAcceptStatement(CobolIsuzuParser.AcceptStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#acceptStatement}.
	 * @param ctx the parse tree
	 */
	void exitAcceptStatement(CobolIsuzuParser.AcceptStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#acceptFromDateStatement}.
	 * @param ctx the parse tree
	 */
	void enterAcceptFromDateStatement(CobolIsuzuParser.AcceptFromDateStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#acceptFromDateStatement}.
	 * @param ctx the parse tree
	 */
	void exitAcceptFromDateStatement(CobolIsuzuParser.AcceptFromDateStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#acceptFromMnemonicStatement}.
	 * @param ctx the parse tree
	 */
	void enterAcceptFromMnemonicStatement(CobolIsuzuParser.AcceptFromMnemonicStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#acceptFromMnemonicStatement}.
	 * @param ctx the parse tree
	 */
	void exitAcceptFromMnemonicStatement(CobolIsuzuParser.AcceptFromMnemonicStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#acceptFromEscapeKeyStatement}.
	 * @param ctx the parse tree
	 */
	void enterAcceptFromEscapeKeyStatement(CobolIsuzuParser.AcceptFromEscapeKeyStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#acceptFromEscapeKeyStatement}.
	 * @param ctx the parse tree
	 */
	void exitAcceptFromEscapeKeyStatement(CobolIsuzuParser.AcceptFromEscapeKeyStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#acceptMessageCountStatement}.
	 * @param ctx the parse tree
	 */
	void enterAcceptMessageCountStatement(CobolIsuzuParser.AcceptMessageCountStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#acceptMessageCountStatement}.
	 * @param ctx the parse tree
	 */
	void exitAcceptMessageCountStatement(CobolIsuzuParser.AcceptMessageCountStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#addStatement}.
	 * @param ctx the parse tree
	 */
	void enterAddStatement(CobolIsuzuParser.AddStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#addStatement}.
	 * @param ctx the parse tree
	 */
	void exitAddStatement(CobolIsuzuParser.AddStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#addToStatement}.
	 * @param ctx the parse tree
	 */
	void enterAddToStatement(CobolIsuzuParser.AddToStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#addToStatement}.
	 * @param ctx the parse tree
	 */
	void exitAddToStatement(CobolIsuzuParser.AddToStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#addToGivingStatement}.
	 * @param ctx the parse tree
	 */
	void enterAddToGivingStatement(CobolIsuzuParser.AddToGivingStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#addToGivingStatement}.
	 * @param ctx the parse tree
	 */
	void exitAddToGivingStatement(CobolIsuzuParser.AddToGivingStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#addCorrespondingStatement}.
	 * @param ctx the parse tree
	 */
	void enterAddCorrespondingStatement(CobolIsuzuParser.AddCorrespondingStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#addCorrespondingStatement}.
	 * @param ctx the parse tree
	 */
	void exitAddCorrespondingStatement(CobolIsuzuParser.AddCorrespondingStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#addFrom}.
	 * @param ctx the parse tree
	 */
	void enterAddFrom(CobolIsuzuParser.AddFromContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#addFrom}.
	 * @param ctx the parse tree
	 */
	void exitAddFrom(CobolIsuzuParser.AddFromContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#addTo}.
	 * @param ctx the parse tree
	 */
	void enterAddTo(CobolIsuzuParser.AddToContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#addTo}.
	 * @param ctx the parse tree
	 */
	void exitAddTo(CobolIsuzuParser.AddToContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#addToGiving}.
	 * @param ctx the parse tree
	 */
	void enterAddToGiving(CobolIsuzuParser.AddToGivingContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#addToGiving}.
	 * @param ctx the parse tree
	 */
	void exitAddToGiving(CobolIsuzuParser.AddToGivingContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#addGiving}.
	 * @param ctx the parse tree
	 */
	void enterAddGiving(CobolIsuzuParser.AddGivingContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#addGiving}.
	 * @param ctx the parse tree
	 */
	void exitAddGiving(CobolIsuzuParser.AddGivingContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#alteredGoTo}.
	 * @param ctx the parse tree
	 */
	void enterAlteredGoTo(CobolIsuzuParser.AlteredGoToContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#alteredGoTo}.
	 * @param ctx the parse tree
	 */
	void exitAlteredGoTo(CobolIsuzuParser.AlteredGoToContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#alterStatement}.
	 * @param ctx the parse tree
	 */
	void enterAlterStatement(CobolIsuzuParser.AlterStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#alterStatement}.
	 * @param ctx the parse tree
	 */
	void exitAlterStatement(CobolIsuzuParser.AlterStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#alterProceedTo}.
	 * @param ctx the parse tree
	 */
	void enterAlterProceedTo(CobolIsuzuParser.AlterProceedToContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#alterProceedTo}.
	 * @param ctx the parse tree
	 */
	void exitAlterProceedTo(CobolIsuzuParser.AlterProceedToContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#callStatement}.
	 * @param ctx the parse tree
	 */
	void enterCallStatement(CobolIsuzuParser.CallStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#callStatement}.
	 * @param ctx the parse tree
	 */
	void exitCallStatement(CobolIsuzuParser.CallStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#callUsingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterCallUsingPhrase(CobolIsuzuParser.CallUsingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#callUsingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitCallUsingPhrase(CobolIsuzuParser.CallUsingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#callUsingParameter}.
	 * @param ctx the parse tree
	 */
	void enterCallUsingParameter(CobolIsuzuParser.CallUsingParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#callUsingParameter}.
	 * @param ctx the parse tree
	 */
	void exitCallUsingParameter(CobolIsuzuParser.CallUsingParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#callByReferencePhrase}.
	 * @param ctx the parse tree
	 */
	void enterCallByReferencePhrase(CobolIsuzuParser.CallByReferencePhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#callByReferencePhrase}.
	 * @param ctx the parse tree
	 */
	void exitCallByReferencePhrase(CobolIsuzuParser.CallByReferencePhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#callByReference}.
	 * @param ctx the parse tree
	 */
	void enterCallByReference(CobolIsuzuParser.CallByReferenceContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#callByReference}.
	 * @param ctx the parse tree
	 */
	void exitCallByReference(CobolIsuzuParser.CallByReferenceContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#callByValuePhrase}.
	 * @param ctx the parse tree
	 */
	void enterCallByValuePhrase(CobolIsuzuParser.CallByValuePhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#callByValuePhrase}.
	 * @param ctx the parse tree
	 */
	void exitCallByValuePhrase(CobolIsuzuParser.CallByValuePhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#callByValue}.
	 * @param ctx the parse tree
	 */
	void enterCallByValue(CobolIsuzuParser.CallByValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#callByValue}.
	 * @param ctx the parse tree
	 */
	void exitCallByValue(CobolIsuzuParser.CallByValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#callByContentPhrase}.
	 * @param ctx the parse tree
	 */
	void enterCallByContentPhrase(CobolIsuzuParser.CallByContentPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#callByContentPhrase}.
	 * @param ctx the parse tree
	 */
	void exitCallByContentPhrase(CobolIsuzuParser.CallByContentPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#callByContent}.
	 * @param ctx the parse tree
	 */
	void enterCallByContent(CobolIsuzuParser.CallByContentContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#callByContent}.
	 * @param ctx the parse tree
	 */
	void exitCallByContent(CobolIsuzuParser.CallByContentContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#callGivingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterCallGivingPhrase(CobolIsuzuParser.CallGivingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#callGivingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitCallGivingPhrase(CobolIsuzuParser.CallGivingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#callSystem}.
	 * @param ctx the parse tree
	 */
	void enterCallSystem(CobolIsuzuParser.CallSystemContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#callSystem}.
	 * @param ctx the parse tree
	 */
	void exitCallSystem(CobolIsuzuParser.CallSystemContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#cancelStatement}.
	 * @param ctx the parse tree
	 */
	void enterCancelStatement(CobolIsuzuParser.CancelStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#cancelStatement}.
	 * @param ctx the parse tree
	 */
	void exitCancelStatement(CobolIsuzuParser.CancelStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#cancelCall}.
	 * @param ctx the parse tree
	 */
	void enterCancelCall(CobolIsuzuParser.CancelCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#cancelCall}.
	 * @param ctx the parse tree
	 */
	void exitCancelCall(CobolIsuzuParser.CancelCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#closeStatement}.
	 * @param ctx the parse tree
	 */
	void enterCloseStatement(CobolIsuzuParser.CloseStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#closeStatement}.
	 * @param ctx the parse tree
	 */
	void exitCloseStatement(CobolIsuzuParser.CloseStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#closePhrase}.
	 * @param ctx the parse tree
	 */
	void enterClosePhrase(CobolIsuzuParser.ClosePhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#closePhrase}.
	 * @param ctx the parse tree
	 */
	void exitClosePhrase(CobolIsuzuParser.ClosePhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#closeFile}.
	 * @param ctx the parse tree
	 */
	void enterCloseFile(CobolIsuzuParser.CloseFileContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#closeFile}.
	 * @param ctx the parse tree
	 */
	void exitCloseFile(CobolIsuzuParser.CloseFileContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#closeReelUnitStatement}.
	 * @param ctx the parse tree
	 */
	void enterCloseReelUnitStatement(CobolIsuzuParser.CloseReelUnitStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#closeReelUnitStatement}.
	 * @param ctx the parse tree
	 */
	void exitCloseReelUnitStatement(CobolIsuzuParser.CloseReelUnitStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#closeRelativeStatement}.
	 * @param ctx the parse tree
	 */
	void enterCloseRelativeStatement(CobolIsuzuParser.CloseRelativeStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#closeRelativeStatement}.
	 * @param ctx the parse tree
	 */
	void exitCloseRelativeStatement(CobolIsuzuParser.CloseRelativeStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#closePortFileIOStatement}.
	 * @param ctx the parse tree
	 */
	void enterClosePortFileIOStatement(CobolIsuzuParser.ClosePortFileIOStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#closePortFileIOStatement}.
	 * @param ctx the parse tree
	 */
	void exitClosePortFileIOStatement(CobolIsuzuParser.ClosePortFileIOStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#closePortFileIOUsing}.
	 * @param ctx the parse tree
	 */
	void enterClosePortFileIOUsing(CobolIsuzuParser.ClosePortFileIOUsingContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#closePortFileIOUsing}.
	 * @param ctx the parse tree
	 */
	void exitClosePortFileIOUsing(CobolIsuzuParser.ClosePortFileIOUsingContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#closePortFileIOUsingCloseDisposition}.
	 * @param ctx the parse tree
	 */
	void enterClosePortFileIOUsingCloseDisposition(CobolIsuzuParser.ClosePortFileIOUsingCloseDispositionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#closePortFileIOUsingCloseDisposition}.
	 * @param ctx the parse tree
	 */
	void exitClosePortFileIOUsingCloseDisposition(CobolIsuzuParser.ClosePortFileIOUsingCloseDispositionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#closePortFileIOUsingAssociatedData}.
	 * @param ctx the parse tree
	 */
	void enterClosePortFileIOUsingAssociatedData(CobolIsuzuParser.ClosePortFileIOUsingAssociatedDataContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#closePortFileIOUsingAssociatedData}.
	 * @param ctx the parse tree
	 */
	void exitClosePortFileIOUsingAssociatedData(CobolIsuzuParser.ClosePortFileIOUsingAssociatedDataContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#closePortFileIOUsingAssociatedDataLength}.
	 * @param ctx the parse tree
	 */
	void enterClosePortFileIOUsingAssociatedDataLength(CobolIsuzuParser.ClosePortFileIOUsingAssociatedDataLengthContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#closePortFileIOUsingAssociatedDataLength}.
	 * @param ctx the parse tree
	 */
	void exitClosePortFileIOUsingAssociatedDataLength(CobolIsuzuParser.ClosePortFileIOUsingAssociatedDataLengthContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#computeStatement}.
	 * @param ctx the parse tree
	 */
	void enterComputeStatement(CobolIsuzuParser.ComputeStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#computeStatement}.
	 * @param ctx the parse tree
	 */
	void exitComputeStatement(CobolIsuzuParser.ComputeStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#computeStore}.
	 * @param ctx the parse tree
	 */
	void enterComputeStore(CobolIsuzuParser.ComputeStoreContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#computeStore}.
	 * @param ctx the parse tree
	 */
	void exitComputeStore(CobolIsuzuParser.ComputeStoreContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#continueStatement}.
	 * @param ctx the parse tree
	 */
	void enterContinueStatement(CobolIsuzuParser.ContinueStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#continueStatement}.
	 * @param ctx the parse tree
	 */
	void exitContinueStatement(CobolIsuzuParser.ContinueStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#deleteStatement}.
	 * @param ctx the parse tree
	 */
	void enterDeleteStatement(CobolIsuzuParser.DeleteStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#deleteStatement}.
	 * @param ctx the parse tree
	 */
	void exitDeleteStatement(CobolIsuzuParser.DeleteStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#disableStatement}.
	 * @param ctx the parse tree
	 */
	void enterDisableStatement(CobolIsuzuParser.DisableStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#disableStatement}.
	 * @param ctx the parse tree
	 */
	void exitDisableStatement(CobolIsuzuParser.DisableStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#displayStatement}.
	 * @param ctx the parse tree
	 */
	void enterDisplayStatement(CobolIsuzuParser.DisplayStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#displayStatement}.
	 * @param ctx the parse tree
	 */
	void exitDisplayStatement(CobolIsuzuParser.DisplayStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#displayOperand}.
	 * @param ctx the parse tree
	 */
	void enterDisplayOperand(CobolIsuzuParser.DisplayOperandContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#displayOperand}.
	 * @param ctx the parse tree
	 */
	void exitDisplayOperand(CobolIsuzuParser.DisplayOperandContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#displayAt}.
	 * @param ctx the parse tree
	 */
	void enterDisplayAt(CobolIsuzuParser.DisplayAtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#displayAt}.
	 * @param ctx the parse tree
	 */
	void exitDisplayAt(CobolIsuzuParser.DisplayAtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#displayUpon}.
	 * @param ctx the parse tree
	 */
	void enterDisplayUpon(CobolIsuzuParser.DisplayUponContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#displayUpon}.
	 * @param ctx the parse tree
	 */
	void exitDisplayUpon(CobolIsuzuParser.DisplayUponContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#displayWith}.
	 * @param ctx the parse tree
	 */
	void enterDisplayWith(CobolIsuzuParser.DisplayWithContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#displayWith}.
	 * @param ctx the parse tree
	 */
	void exitDisplayWith(CobolIsuzuParser.DisplayWithContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#divideStatement}.
	 * @param ctx the parse tree
	 */
	void enterDivideStatement(CobolIsuzuParser.DivideStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#divideStatement}.
	 * @param ctx the parse tree
	 */
	void exitDivideStatement(CobolIsuzuParser.DivideStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#divideIntoStatement}.
	 * @param ctx the parse tree
	 */
	void enterDivideIntoStatement(CobolIsuzuParser.DivideIntoStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#divideIntoStatement}.
	 * @param ctx the parse tree
	 */
	void exitDivideIntoStatement(CobolIsuzuParser.DivideIntoStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#divideIntoGivingStatement}.
	 * @param ctx the parse tree
	 */
	void enterDivideIntoGivingStatement(CobolIsuzuParser.DivideIntoGivingStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#divideIntoGivingStatement}.
	 * @param ctx the parse tree
	 */
	void exitDivideIntoGivingStatement(CobolIsuzuParser.DivideIntoGivingStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#divideByGivingStatement}.
	 * @param ctx the parse tree
	 */
	void enterDivideByGivingStatement(CobolIsuzuParser.DivideByGivingStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#divideByGivingStatement}.
	 * @param ctx the parse tree
	 */
	void exitDivideByGivingStatement(CobolIsuzuParser.DivideByGivingStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#divideGivingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterDivideGivingPhrase(CobolIsuzuParser.DivideGivingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#divideGivingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitDivideGivingPhrase(CobolIsuzuParser.DivideGivingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#divideInto}.
	 * @param ctx the parse tree
	 */
	void enterDivideInto(CobolIsuzuParser.DivideIntoContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#divideInto}.
	 * @param ctx the parse tree
	 */
	void exitDivideInto(CobolIsuzuParser.DivideIntoContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#divideGiving}.
	 * @param ctx the parse tree
	 */
	void enterDivideGiving(CobolIsuzuParser.DivideGivingContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#divideGiving}.
	 * @param ctx the parse tree
	 */
	void exitDivideGiving(CobolIsuzuParser.DivideGivingContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#divideRemainder}.
	 * @param ctx the parse tree
	 */
	void enterDivideRemainder(CobolIsuzuParser.DivideRemainderContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#divideRemainder}.
	 * @param ctx the parse tree
	 */
	void exitDivideRemainder(CobolIsuzuParser.DivideRemainderContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#enableStatement}.
	 * @param ctx the parse tree
	 */
	void enterEnableStatement(CobolIsuzuParser.EnableStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#enableStatement}.
	 * @param ctx the parse tree
	 */
	void exitEnableStatement(CobolIsuzuParser.EnableStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#entryStatement}.
	 * @param ctx the parse tree
	 */
	void enterEntryStatement(CobolIsuzuParser.EntryStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#entryStatement}.
	 * @param ctx the parse tree
	 */
	void exitEntryStatement(CobolIsuzuParser.EntryStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#evaluateStatement}.
	 * @param ctx the parse tree
	 */
	void enterEvaluateStatement(CobolIsuzuParser.EvaluateStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#evaluateStatement}.
	 * @param ctx the parse tree
	 */
	void exitEvaluateStatement(CobolIsuzuParser.EvaluateStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#evaluateSelect}.
	 * @param ctx the parse tree
	 */
	void enterEvaluateSelect(CobolIsuzuParser.EvaluateSelectContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#evaluateSelect}.
	 * @param ctx the parse tree
	 */
	void exitEvaluateSelect(CobolIsuzuParser.EvaluateSelectContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#evaluateAlsoSelect}.
	 * @param ctx the parse tree
	 */
	void enterEvaluateAlsoSelect(CobolIsuzuParser.EvaluateAlsoSelectContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#evaluateAlsoSelect}.
	 * @param ctx the parse tree
	 */
	void exitEvaluateAlsoSelect(CobolIsuzuParser.EvaluateAlsoSelectContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#evaluateWhenPhrase}.
	 * @param ctx the parse tree
	 */
	void enterEvaluateWhenPhrase(CobolIsuzuParser.EvaluateWhenPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#evaluateWhenPhrase}.
	 * @param ctx the parse tree
	 */
	void exitEvaluateWhenPhrase(CobolIsuzuParser.EvaluateWhenPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#evaluateWhen}.
	 * @param ctx the parse tree
	 */
	void enterEvaluateWhen(CobolIsuzuParser.EvaluateWhenContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#evaluateWhen}.
	 * @param ctx the parse tree
	 */
	void exitEvaluateWhen(CobolIsuzuParser.EvaluateWhenContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#evaluateCondition}.
	 * @param ctx the parse tree
	 */
	void enterEvaluateCondition(CobolIsuzuParser.EvaluateConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#evaluateCondition}.
	 * @param ctx the parse tree
	 */
	void exitEvaluateCondition(CobolIsuzuParser.EvaluateConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#evaluateThrough}.
	 * @param ctx the parse tree
	 */
	void enterEvaluateThrough(CobolIsuzuParser.EvaluateThroughContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#evaluateThrough}.
	 * @param ctx the parse tree
	 */
	void exitEvaluateThrough(CobolIsuzuParser.EvaluateThroughContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#evaluateAlsoCondition}.
	 * @param ctx the parse tree
	 */
	void enterEvaluateAlsoCondition(CobolIsuzuParser.EvaluateAlsoConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#evaluateAlsoCondition}.
	 * @param ctx the parse tree
	 */
	void exitEvaluateAlsoCondition(CobolIsuzuParser.EvaluateAlsoConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#evaluateWhenOther}.
	 * @param ctx the parse tree
	 */
	void enterEvaluateWhenOther(CobolIsuzuParser.EvaluateWhenOtherContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#evaluateWhenOther}.
	 * @param ctx the parse tree
	 */
	void exitEvaluateWhenOther(CobolIsuzuParser.EvaluateWhenOtherContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#evaluateValue}.
	 * @param ctx the parse tree
	 */
	void enterEvaluateValue(CobolIsuzuParser.EvaluateValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#evaluateValue}.
	 * @param ctx the parse tree
	 */
	void exitEvaluateValue(CobolIsuzuParser.EvaluateValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#execCicsStatement}.
	 * @param ctx the parse tree
	 */
	void enterExecCicsStatement(CobolIsuzuParser.ExecCicsStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#execCicsStatement}.
	 * @param ctx the parse tree
	 */
	void exitExecCicsStatement(CobolIsuzuParser.ExecCicsStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#execSqlStatement}.
	 * @param ctx the parse tree
	 */
	void enterExecSqlStatement(CobolIsuzuParser.ExecSqlStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#execSqlStatement}.
	 * @param ctx the parse tree
	 */
	void exitExecSqlStatement(CobolIsuzuParser.ExecSqlStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#execSqlImsStatement}.
	 * @param ctx the parse tree
	 */
	void enterExecSqlImsStatement(CobolIsuzuParser.ExecSqlImsStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#execSqlImsStatement}.
	 * @param ctx the parse tree
	 */
	void exitExecSqlImsStatement(CobolIsuzuParser.ExecSqlImsStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#exhibitStatement}.
	 * @param ctx the parse tree
	 */
	void enterExhibitStatement(CobolIsuzuParser.ExhibitStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#exhibitStatement}.
	 * @param ctx the parse tree
	 */
	void exitExhibitStatement(CobolIsuzuParser.ExhibitStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#exhibitOperand}.
	 * @param ctx the parse tree
	 */
	void enterExhibitOperand(CobolIsuzuParser.ExhibitOperandContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#exhibitOperand}.
	 * @param ctx the parse tree
	 */
	void exitExhibitOperand(CobolIsuzuParser.ExhibitOperandContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#exitStatement}.
	 * @param ctx the parse tree
	 */
	void enterExitStatement(CobolIsuzuParser.ExitStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#exitStatement}.
	 * @param ctx the parse tree
	 */
	void exitExitStatement(CobolIsuzuParser.ExitStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#generateStatement}.
	 * @param ctx the parse tree
	 */
	void enterGenerateStatement(CobolIsuzuParser.GenerateStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#generateStatement}.
	 * @param ctx the parse tree
	 */
	void exitGenerateStatement(CobolIsuzuParser.GenerateStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#gobackStatement}.
	 * @param ctx the parse tree
	 */
	void enterGobackStatement(CobolIsuzuParser.GobackStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#gobackStatement}.
	 * @param ctx the parse tree
	 */
	void exitGobackStatement(CobolIsuzuParser.GobackStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#goToStatement}.
	 * @param ctx the parse tree
	 */
	void enterGoToStatement(CobolIsuzuParser.GoToStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#goToStatement}.
	 * @param ctx the parse tree
	 */
	void exitGoToStatement(CobolIsuzuParser.GoToStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#goToStatementSimple}.
	 * @param ctx the parse tree
	 */
	void enterGoToStatementSimple(CobolIsuzuParser.GoToStatementSimpleContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#goToStatementSimple}.
	 * @param ctx the parse tree
	 */
	void exitGoToStatementSimple(CobolIsuzuParser.GoToStatementSimpleContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#goToDependingOnStatement}.
	 * @param ctx the parse tree
	 */
	void enterGoToDependingOnStatement(CobolIsuzuParser.GoToDependingOnStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#goToDependingOnStatement}.
	 * @param ctx the parse tree
	 */
	void exitGoToDependingOnStatement(CobolIsuzuParser.GoToDependingOnStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(CobolIsuzuParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(CobolIsuzuParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#ifThen}.
	 * @param ctx the parse tree
	 */
	void enterIfThen(CobolIsuzuParser.IfThenContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#ifThen}.
	 * @param ctx the parse tree
	 */
	void exitIfThen(CobolIsuzuParser.IfThenContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#ifElse}.
	 * @param ctx the parse tree
	 */
	void enterIfElse(CobolIsuzuParser.IfElseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#ifElse}.
	 * @param ctx the parse tree
	 */
	void exitIfElse(CobolIsuzuParser.IfElseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#initializeStatement}.
	 * @param ctx the parse tree
	 */
	void enterInitializeStatement(CobolIsuzuParser.InitializeStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#initializeStatement}.
	 * @param ctx the parse tree
	 */
	void exitInitializeStatement(CobolIsuzuParser.InitializeStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#initializeReplacingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterInitializeReplacingPhrase(CobolIsuzuParser.InitializeReplacingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#initializeReplacingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitInitializeReplacingPhrase(CobolIsuzuParser.InitializeReplacingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#initializeReplacingBy}.
	 * @param ctx the parse tree
	 */
	void enterInitializeReplacingBy(CobolIsuzuParser.InitializeReplacingByContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#initializeReplacingBy}.
	 * @param ctx the parse tree
	 */
	void exitInitializeReplacingBy(CobolIsuzuParser.InitializeReplacingByContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#initiateStatement}.
	 * @param ctx the parse tree
	 */
	void enterInitiateStatement(CobolIsuzuParser.InitiateStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#initiateStatement}.
	 * @param ctx the parse tree
	 */
	void exitInitiateStatement(CobolIsuzuParser.InitiateStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#inspectStatement}.
	 * @param ctx the parse tree
	 */
	void enterInspectStatement(CobolIsuzuParser.InspectStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#inspectStatement}.
	 * @param ctx the parse tree
	 */
	void exitInspectStatement(CobolIsuzuParser.InspectStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#inspectTallyingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterInspectTallyingPhrase(CobolIsuzuParser.InspectTallyingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#inspectTallyingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitInspectTallyingPhrase(CobolIsuzuParser.InspectTallyingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#inspectReplacingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterInspectReplacingPhrase(CobolIsuzuParser.InspectReplacingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#inspectReplacingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitInspectReplacingPhrase(CobolIsuzuParser.InspectReplacingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#inspectTallyingReplacingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterInspectTallyingReplacingPhrase(CobolIsuzuParser.InspectTallyingReplacingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#inspectTallyingReplacingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitInspectTallyingReplacingPhrase(CobolIsuzuParser.InspectTallyingReplacingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#inspectConvertingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterInspectConvertingPhrase(CobolIsuzuParser.InspectConvertingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#inspectConvertingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitInspectConvertingPhrase(CobolIsuzuParser.InspectConvertingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#inspectFor}.
	 * @param ctx the parse tree
	 */
	void enterInspectFor(CobolIsuzuParser.InspectForContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#inspectFor}.
	 * @param ctx the parse tree
	 */
	void exitInspectFor(CobolIsuzuParser.InspectForContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#inspectCharacters}.
	 * @param ctx the parse tree
	 */
	void enterInspectCharacters(CobolIsuzuParser.InspectCharactersContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#inspectCharacters}.
	 * @param ctx the parse tree
	 */
	void exitInspectCharacters(CobolIsuzuParser.InspectCharactersContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#inspectReplacingCharacters}.
	 * @param ctx the parse tree
	 */
	void enterInspectReplacingCharacters(CobolIsuzuParser.InspectReplacingCharactersContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#inspectReplacingCharacters}.
	 * @param ctx the parse tree
	 */
	void exitInspectReplacingCharacters(CobolIsuzuParser.InspectReplacingCharactersContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#inspectAllLeadings}.
	 * @param ctx the parse tree
	 */
	void enterInspectAllLeadings(CobolIsuzuParser.InspectAllLeadingsContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#inspectAllLeadings}.
	 * @param ctx the parse tree
	 */
	void exitInspectAllLeadings(CobolIsuzuParser.InspectAllLeadingsContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#inspectReplacingAllLeadings}.
	 * @param ctx the parse tree
	 */
	void enterInspectReplacingAllLeadings(CobolIsuzuParser.InspectReplacingAllLeadingsContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#inspectReplacingAllLeadings}.
	 * @param ctx the parse tree
	 */
	void exitInspectReplacingAllLeadings(CobolIsuzuParser.InspectReplacingAllLeadingsContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#inspectAllLeading}.
	 * @param ctx the parse tree
	 */
	void enterInspectAllLeading(CobolIsuzuParser.InspectAllLeadingContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#inspectAllLeading}.
	 * @param ctx the parse tree
	 */
	void exitInspectAllLeading(CobolIsuzuParser.InspectAllLeadingContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#inspectReplacingAllLeading}.
	 * @param ctx the parse tree
	 */
	void enterInspectReplacingAllLeading(CobolIsuzuParser.InspectReplacingAllLeadingContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#inspectReplacingAllLeading}.
	 * @param ctx the parse tree
	 */
	void exitInspectReplacingAllLeading(CobolIsuzuParser.InspectReplacingAllLeadingContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#inspectBy}.
	 * @param ctx the parse tree
	 */
	void enterInspectBy(CobolIsuzuParser.InspectByContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#inspectBy}.
	 * @param ctx the parse tree
	 */
	void exitInspectBy(CobolIsuzuParser.InspectByContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#inspectTo}.
	 * @param ctx the parse tree
	 */
	void enterInspectTo(CobolIsuzuParser.InspectToContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#inspectTo}.
	 * @param ctx the parse tree
	 */
	void exitInspectTo(CobolIsuzuParser.InspectToContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#inspectBeforeAfter}.
	 * @param ctx the parse tree
	 */
	void enterInspectBeforeAfter(CobolIsuzuParser.InspectBeforeAfterContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#inspectBeforeAfter}.
	 * @param ctx the parse tree
	 */
	void exitInspectBeforeAfter(CobolIsuzuParser.InspectBeforeAfterContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#mergeStatement}.
	 * @param ctx the parse tree
	 */
	void enterMergeStatement(CobolIsuzuParser.MergeStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#mergeStatement}.
	 * @param ctx the parse tree
	 */
	void exitMergeStatement(CobolIsuzuParser.MergeStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#mergeOnKeyClause}.
	 * @param ctx the parse tree
	 */
	void enterMergeOnKeyClause(CobolIsuzuParser.MergeOnKeyClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#mergeOnKeyClause}.
	 * @param ctx the parse tree
	 */
	void exitMergeOnKeyClause(CobolIsuzuParser.MergeOnKeyClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#mergeCollatingSequencePhrase}.
	 * @param ctx the parse tree
	 */
	void enterMergeCollatingSequencePhrase(CobolIsuzuParser.MergeCollatingSequencePhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#mergeCollatingSequencePhrase}.
	 * @param ctx the parse tree
	 */
	void exitMergeCollatingSequencePhrase(CobolIsuzuParser.MergeCollatingSequencePhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#mergeCollatingAlphanumeric}.
	 * @param ctx the parse tree
	 */
	void enterMergeCollatingAlphanumeric(CobolIsuzuParser.MergeCollatingAlphanumericContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#mergeCollatingAlphanumeric}.
	 * @param ctx the parse tree
	 */
	void exitMergeCollatingAlphanumeric(CobolIsuzuParser.MergeCollatingAlphanumericContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#mergeCollatingNational}.
	 * @param ctx the parse tree
	 */
	void enterMergeCollatingNational(CobolIsuzuParser.MergeCollatingNationalContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#mergeCollatingNational}.
	 * @param ctx the parse tree
	 */
	void exitMergeCollatingNational(CobolIsuzuParser.MergeCollatingNationalContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#mergeUsing}.
	 * @param ctx the parse tree
	 */
	void enterMergeUsing(CobolIsuzuParser.MergeUsingContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#mergeUsing}.
	 * @param ctx the parse tree
	 */
	void exitMergeUsing(CobolIsuzuParser.MergeUsingContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#mergeOutputProcedurePhrase}.
	 * @param ctx the parse tree
	 */
	void enterMergeOutputProcedurePhrase(CobolIsuzuParser.MergeOutputProcedurePhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#mergeOutputProcedurePhrase}.
	 * @param ctx the parse tree
	 */
	void exitMergeOutputProcedurePhrase(CobolIsuzuParser.MergeOutputProcedurePhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#mergeOutputThrough}.
	 * @param ctx the parse tree
	 */
	void enterMergeOutputThrough(CobolIsuzuParser.MergeOutputThroughContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#mergeOutputThrough}.
	 * @param ctx the parse tree
	 */
	void exitMergeOutputThrough(CobolIsuzuParser.MergeOutputThroughContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#mergeGivingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterMergeGivingPhrase(CobolIsuzuParser.MergeGivingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#mergeGivingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitMergeGivingPhrase(CobolIsuzuParser.MergeGivingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#mergeGiving}.
	 * @param ctx the parse tree
	 */
	void enterMergeGiving(CobolIsuzuParser.MergeGivingContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#mergeGiving}.
	 * @param ctx the parse tree
	 */
	void exitMergeGiving(CobolIsuzuParser.MergeGivingContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#moveStatement}.
	 * @param ctx the parse tree
	 */
	void enterMoveStatement(CobolIsuzuParser.MoveStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#moveStatement}.
	 * @param ctx the parse tree
	 */
	void exitMoveStatement(CobolIsuzuParser.MoveStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#moveToStatement}.
	 * @param ctx the parse tree
	 */
	void enterMoveToStatement(CobolIsuzuParser.MoveToStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#moveToStatement}.
	 * @param ctx the parse tree
	 */
	void exitMoveToStatement(CobolIsuzuParser.MoveToStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#moveToSendingArea}.
	 * @param ctx the parse tree
	 */
	void enterMoveToSendingArea(CobolIsuzuParser.MoveToSendingAreaContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#moveToSendingArea}.
	 * @param ctx the parse tree
	 */
	void exitMoveToSendingArea(CobolIsuzuParser.MoveToSendingAreaContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#moveCorrespondingToStatement}.
	 * @param ctx the parse tree
	 */
	void enterMoveCorrespondingToStatement(CobolIsuzuParser.MoveCorrespondingToStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#moveCorrespondingToStatement}.
	 * @param ctx the parse tree
	 */
	void exitMoveCorrespondingToStatement(CobolIsuzuParser.MoveCorrespondingToStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#moveCorrespondingToSendingArea}.
	 * @param ctx the parse tree
	 */
	void enterMoveCorrespondingToSendingArea(CobolIsuzuParser.MoveCorrespondingToSendingAreaContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#moveCorrespondingToSendingArea}.
	 * @param ctx the parse tree
	 */
	void exitMoveCorrespondingToSendingArea(CobolIsuzuParser.MoveCorrespondingToSendingAreaContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#moveAttributeClause}.
	 * @param ctx the parse tree
	 */
	void enterMoveAttributeClause(CobolIsuzuParser.MoveAttributeClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#moveAttributeClause}.
	 * @param ctx the parse tree
	 */
	void exitMoveAttributeClause(CobolIsuzuParser.MoveAttributeClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#multiplyStatement}.
	 * @param ctx the parse tree
	 */
	void enterMultiplyStatement(CobolIsuzuParser.MultiplyStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#multiplyStatement}.
	 * @param ctx the parse tree
	 */
	void exitMultiplyStatement(CobolIsuzuParser.MultiplyStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#multiplyRegular}.
	 * @param ctx the parse tree
	 */
	void enterMultiplyRegular(CobolIsuzuParser.MultiplyRegularContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#multiplyRegular}.
	 * @param ctx the parse tree
	 */
	void exitMultiplyRegular(CobolIsuzuParser.MultiplyRegularContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#multiplyRegularOperand}.
	 * @param ctx the parse tree
	 */
	void enterMultiplyRegularOperand(CobolIsuzuParser.MultiplyRegularOperandContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#multiplyRegularOperand}.
	 * @param ctx the parse tree
	 */
	void exitMultiplyRegularOperand(CobolIsuzuParser.MultiplyRegularOperandContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#multiplyGiving}.
	 * @param ctx the parse tree
	 */
	void enterMultiplyGiving(CobolIsuzuParser.MultiplyGivingContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#multiplyGiving}.
	 * @param ctx the parse tree
	 */
	void exitMultiplyGiving(CobolIsuzuParser.MultiplyGivingContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#multiplyGivingOperand}.
	 * @param ctx the parse tree
	 */
	void enterMultiplyGivingOperand(CobolIsuzuParser.MultiplyGivingOperandContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#multiplyGivingOperand}.
	 * @param ctx the parse tree
	 */
	void exitMultiplyGivingOperand(CobolIsuzuParser.MultiplyGivingOperandContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#multiplyGivingResult}.
	 * @param ctx the parse tree
	 */
	void enterMultiplyGivingResult(CobolIsuzuParser.MultiplyGivingResultContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#multiplyGivingResult}.
	 * @param ctx the parse tree
	 */
	void exitMultiplyGivingResult(CobolIsuzuParser.MultiplyGivingResultContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#openStatement}.
	 * @param ctx the parse tree
	 */
	void enterOpenStatement(CobolIsuzuParser.OpenStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#openStatement}.
	 * @param ctx the parse tree
	 */
	void exitOpenStatement(CobolIsuzuParser.OpenStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#openInputStatement}.
	 * @param ctx the parse tree
	 */
	void enterOpenInputStatement(CobolIsuzuParser.OpenInputStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#openInputStatement}.
	 * @param ctx the parse tree
	 */
	void exitOpenInputStatement(CobolIsuzuParser.OpenInputStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#openInput}.
	 * @param ctx the parse tree
	 */
	void enterOpenInput(CobolIsuzuParser.OpenInputContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#openInput}.
	 * @param ctx the parse tree
	 */
	void exitOpenInput(CobolIsuzuParser.OpenInputContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#openOutputStatement}.
	 * @param ctx the parse tree
	 */
	void enterOpenOutputStatement(CobolIsuzuParser.OpenOutputStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#openOutputStatement}.
	 * @param ctx the parse tree
	 */
	void exitOpenOutputStatement(CobolIsuzuParser.OpenOutputStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#openOutput}.
	 * @param ctx the parse tree
	 */
	void enterOpenOutput(CobolIsuzuParser.OpenOutputContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#openOutput}.
	 * @param ctx the parse tree
	 */
	void exitOpenOutput(CobolIsuzuParser.OpenOutputContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#openIOStatement}.
	 * @param ctx the parse tree
	 */
	void enterOpenIOStatement(CobolIsuzuParser.OpenIOStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#openIOStatement}.
	 * @param ctx the parse tree
	 */
	void exitOpenIOStatement(CobolIsuzuParser.OpenIOStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#openExtendStatement}.
	 * @param ctx the parse tree
	 */
	void enterOpenExtendStatement(CobolIsuzuParser.OpenExtendStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#openExtendStatement}.
	 * @param ctx the parse tree
	 */
	void exitOpenExtendStatement(CobolIsuzuParser.OpenExtendStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#performStatement}.
	 * @param ctx the parse tree
	 */
	void enterPerformStatement(CobolIsuzuParser.PerformStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#performStatement}.
	 * @param ctx the parse tree
	 */
	void exitPerformStatement(CobolIsuzuParser.PerformStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#performInlineStatement}.
	 * @param ctx the parse tree
	 */
	void enterPerformInlineStatement(CobolIsuzuParser.PerformInlineStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#performInlineStatement}.
	 * @param ctx the parse tree
	 */
	void exitPerformInlineStatement(CobolIsuzuParser.PerformInlineStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#performProcedureStatement}.
	 * @param ctx the parse tree
	 */
	void enterPerformProcedureStatement(CobolIsuzuParser.PerformProcedureStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#performProcedureStatement}.
	 * @param ctx the parse tree
	 */
	void exitPerformProcedureStatement(CobolIsuzuParser.PerformProcedureStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#performType}.
	 * @param ctx the parse tree
	 */
	void enterPerformType(CobolIsuzuParser.PerformTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#performType}.
	 * @param ctx the parse tree
	 */
	void exitPerformType(CobolIsuzuParser.PerformTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#performTimes}.
	 * @param ctx the parse tree
	 */
	void enterPerformTimes(CobolIsuzuParser.PerformTimesContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#performTimes}.
	 * @param ctx the parse tree
	 */
	void exitPerformTimes(CobolIsuzuParser.PerformTimesContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#performUntil}.
	 * @param ctx the parse tree
	 */
	void enterPerformUntil(CobolIsuzuParser.PerformUntilContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#performUntil}.
	 * @param ctx the parse tree
	 */
	void exitPerformUntil(CobolIsuzuParser.PerformUntilContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#performVarying}.
	 * @param ctx the parse tree
	 */
	void enterPerformVarying(CobolIsuzuParser.PerformVaryingContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#performVarying}.
	 * @param ctx the parse tree
	 */
	void exitPerformVarying(CobolIsuzuParser.PerformVaryingContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#performVaryingClause}.
	 * @param ctx the parse tree
	 */
	void enterPerformVaryingClause(CobolIsuzuParser.PerformVaryingClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#performVaryingClause}.
	 * @param ctx the parse tree
	 */
	void exitPerformVaryingClause(CobolIsuzuParser.PerformVaryingClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#performVaryingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterPerformVaryingPhrase(CobolIsuzuParser.PerformVaryingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#performVaryingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitPerformVaryingPhrase(CobolIsuzuParser.PerformVaryingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#performAfter}.
	 * @param ctx the parse tree
	 */
	void enterPerformAfter(CobolIsuzuParser.PerformAfterContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#performAfter}.
	 * @param ctx the parse tree
	 */
	void exitPerformAfter(CobolIsuzuParser.PerformAfterContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#performFrom}.
	 * @param ctx the parse tree
	 */
	void enterPerformFrom(CobolIsuzuParser.PerformFromContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#performFrom}.
	 * @param ctx the parse tree
	 */
	void exitPerformFrom(CobolIsuzuParser.PerformFromContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#performBy}.
	 * @param ctx the parse tree
	 */
	void enterPerformBy(CobolIsuzuParser.PerformByContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#performBy}.
	 * @param ctx the parse tree
	 */
	void exitPerformBy(CobolIsuzuParser.PerformByContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#performTestClause}.
	 * @param ctx the parse tree
	 */
	void enterPerformTestClause(CobolIsuzuParser.PerformTestClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#performTestClause}.
	 * @param ctx the parse tree
	 */
	void exitPerformTestClause(CobolIsuzuParser.PerformTestClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#purgeStatement}.
	 * @param ctx the parse tree
	 */
	void enterPurgeStatement(CobolIsuzuParser.PurgeStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#purgeStatement}.
	 * @param ctx the parse tree
	 */
	void exitPurgeStatement(CobolIsuzuParser.PurgeStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#readStatement}.
	 * @param ctx the parse tree
	 */
	void enterReadStatement(CobolIsuzuParser.ReadStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#readStatement}.
	 * @param ctx the parse tree
	 */
	void exitReadStatement(CobolIsuzuParser.ReadStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#readInto}.
	 * @param ctx the parse tree
	 */
	void enterReadInto(CobolIsuzuParser.ReadIntoContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#readInto}.
	 * @param ctx the parse tree
	 */
	void exitReadInto(CobolIsuzuParser.ReadIntoContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#readWith}.
	 * @param ctx the parse tree
	 */
	void enterReadWith(CobolIsuzuParser.ReadWithContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#readWith}.
	 * @param ctx the parse tree
	 */
	void exitReadWith(CobolIsuzuParser.ReadWithContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#readKey}.
	 * @param ctx the parse tree
	 */
	void enterReadKey(CobolIsuzuParser.ReadKeyContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#readKey}.
	 * @param ctx the parse tree
	 */
	void exitReadKey(CobolIsuzuParser.ReadKeyContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#receiveStatement}.
	 * @param ctx the parse tree
	 */
	void enterReceiveStatement(CobolIsuzuParser.ReceiveStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#receiveStatement}.
	 * @param ctx the parse tree
	 */
	void exitReceiveStatement(CobolIsuzuParser.ReceiveStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#receiveFromStatement}.
	 * @param ctx the parse tree
	 */
	void enterReceiveFromStatement(CobolIsuzuParser.ReceiveFromStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#receiveFromStatement}.
	 * @param ctx the parse tree
	 */
	void exitReceiveFromStatement(CobolIsuzuParser.ReceiveFromStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#receiveFrom}.
	 * @param ctx the parse tree
	 */
	void enterReceiveFrom(CobolIsuzuParser.ReceiveFromContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#receiveFrom}.
	 * @param ctx the parse tree
	 */
	void exitReceiveFrom(CobolIsuzuParser.ReceiveFromContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#receiveIntoStatement}.
	 * @param ctx the parse tree
	 */
	void enterReceiveIntoStatement(CobolIsuzuParser.ReceiveIntoStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#receiveIntoStatement}.
	 * @param ctx the parse tree
	 */
	void exitReceiveIntoStatement(CobolIsuzuParser.ReceiveIntoStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#receiveNoData}.
	 * @param ctx the parse tree
	 */
	void enterReceiveNoData(CobolIsuzuParser.ReceiveNoDataContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#receiveNoData}.
	 * @param ctx the parse tree
	 */
	void exitReceiveNoData(CobolIsuzuParser.ReceiveNoDataContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#receiveWithData}.
	 * @param ctx the parse tree
	 */
	void enterReceiveWithData(CobolIsuzuParser.ReceiveWithDataContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#receiveWithData}.
	 * @param ctx the parse tree
	 */
	void exitReceiveWithData(CobolIsuzuParser.ReceiveWithDataContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#receiveBefore}.
	 * @param ctx the parse tree
	 */
	void enterReceiveBefore(CobolIsuzuParser.ReceiveBeforeContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#receiveBefore}.
	 * @param ctx the parse tree
	 */
	void exitReceiveBefore(CobolIsuzuParser.ReceiveBeforeContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#receiveWith}.
	 * @param ctx the parse tree
	 */
	void enterReceiveWith(CobolIsuzuParser.ReceiveWithContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#receiveWith}.
	 * @param ctx the parse tree
	 */
	void exitReceiveWith(CobolIsuzuParser.ReceiveWithContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#receiveThread}.
	 * @param ctx the parse tree
	 */
	void enterReceiveThread(CobolIsuzuParser.ReceiveThreadContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#receiveThread}.
	 * @param ctx the parse tree
	 */
	void exitReceiveThread(CobolIsuzuParser.ReceiveThreadContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#receiveSize}.
	 * @param ctx the parse tree
	 */
	void enterReceiveSize(CobolIsuzuParser.ReceiveSizeContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#receiveSize}.
	 * @param ctx the parse tree
	 */
	void exitReceiveSize(CobolIsuzuParser.ReceiveSizeContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#receiveStatus}.
	 * @param ctx the parse tree
	 */
	void enterReceiveStatus(CobolIsuzuParser.ReceiveStatusContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#receiveStatus}.
	 * @param ctx the parse tree
	 */
	void exitReceiveStatus(CobolIsuzuParser.ReceiveStatusContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#releaseStatement}.
	 * @param ctx the parse tree
	 */
	void enterReleaseStatement(CobolIsuzuParser.ReleaseStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#releaseStatement}.
	 * @param ctx the parse tree
	 */
	void exitReleaseStatement(CobolIsuzuParser.ReleaseStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void enterReturnStatement(CobolIsuzuParser.ReturnStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void exitReturnStatement(CobolIsuzuParser.ReturnStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#returnInto}.
	 * @param ctx the parse tree
	 */
	void enterReturnInto(CobolIsuzuParser.ReturnIntoContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#returnInto}.
	 * @param ctx the parse tree
	 */
	void exitReturnInto(CobolIsuzuParser.ReturnIntoContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#rewriteStatement}.
	 * @param ctx the parse tree
	 */
	void enterRewriteStatement(CobolIsuzuParser.RewriteStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#rewriteStatement}.
	 * @param ctx the parse tree
	 */
	void exitRewriteStatement(CobolIsuzuParser.RewriteStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#rewriteFrom}.
	 * @param ctx the parse tree
	 */
	void enterRewriteFrom(CobolIsuzuParser.RewriteFromContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#rewriteFrom}.
	 * @param ctx the parse tree
	 */
	void exitRewriteFrom(CobolIsuzuParser.RewriteFromContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#searchStatement}.
	 * @param ctx the parse tree
	 */
	void enterSearchStatement(CobolIsuzuParser.SearchStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#searchStatement}.
	 * @param ctx the parse tree
	 */
	void exitSearchStatement(CobolIsuzuParser.SearchStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#searchVarying}.
	 * @param ctx the parse tree
	 */
	void enterSearchVarying(CobolIsuzuParser.SearchVaryingContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#searchVarying}.
	 * @param ctx the parse tree
	 */
	void exitSearchVarying(CobolIsuzuParser.SearchVaryingContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#searchWhen}.
	 * @param ctx the parse tree
	 */
	void enterSearchWhen(CobolIsuzuParser.SearchWhenContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#searchWhen}.
	 * @param ctx the parse tree
	 */
	void exitSearchWhen(CobolIsuzuParser.SearchWhenContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#sendStatement}.
	 * @param ctx the parse tree
	 */
	void enterSendStatement(CobolIsuzuParser.SendStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#sendStatement}.
	 * @param ctx the parse tree
	 */
	void exitSendStatement(CobolIsuzuParser.SendStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#sendStatementSync}.
	 * @param ctx the parse tree
	 */
	void enterSendStatementSync(CobolIsuzuParser.SendStatementSyncContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#sendStatementSync}.
	 * @param ctx the parse tree
	 */
	void exitSendStatementSync(CobolIsuzuParser.SendStatementSyncContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#sendStatementAsync}.
	 * @param ctx the parse tree
	 */
	void enterSendStatementAsync(CobolIsuzuParser.SendStatementAsyncContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#sendStatementAsync}.
	 * @param ctx the parse tree
	 */
	void exitSendStatementAsync(CobolIsuzuParser.SendStatementAsyncContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#sendFromPhrase}.
	 * @param ctx the parse tree
	 */
	void enterSendFromPhrase(CobolIsuzuParser.SendFromPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#sendFromPhrase}.
	 * @param ctx the parse tree
	 */
	void exitSendFromPhrase(CobolIsuzuParser.SendFromPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#sendWithPhrase}.
	 * @param ctx the parse tree
	 */
	void enterSendWithPhrase(CobolIsuzuParser.SendWithPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#sendWithPhrase}.
	 * @param ctx the parse tree
	 */
	void exitSendWithPhrase(CobolIsuzuParser.SendWithPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#sendReplacingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterSendReplacingPhrase(CobolIsuzuParser.SendReplacingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#sendReplacingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitSendReplacingPhrase(CobolIsuzuParser.SendReplacingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#sendAdvancingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterSendAdvancingPhrase(CobolIsuzuParser.SendAdvancingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#sendAdvancingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitSendAdvancingPhrase(CobolIsuzuParser.SendAdvancingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#sendAdvancingPage}.
	 * @param ctx the parse tree
	 */
	void enterSendAdvancingPage(CobolIsuzuParser.SendAdvancingPageContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#sendAdvancingPage}.
	 * @param ctx the parse tree
	 */
	void exitSendAdvancingPage(CobolIsuzuParser.SendAdvancingPageContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#sendAdvancingLines}.
	 * @param ctx the parse tree
	 */
	void enterSendAdvancingLines(CobolIsuzuParser.SendAdvancingLinesContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#sendAdvancingLines}.
	 * @param ctx the parse tree
	 */
	void exitSendAdvancingLines(CobolIsuzuParser.SendAdvancingLinesContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#sendAdvancingMnemonic}.
	 * @param ctx the parse tree
	 */
	void enterSendAdvancingMnemonic(CobolIsuzuParser.SendAdvancingMnemonicContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#sendAdvancingMnemonic}.
	 * @param ctx the parse tree
	 */
	void exitSendAdvancingMnemonic(CobolIsuzuParser.SendAdvancingMnemonicContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#setStatement}.
	 * @param ctx the parse tree
	 */
	void enterSetStatement(CobolIsuzuParser.SetStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#setStatement}.
	 * @param ctx the parse tree
	 */
	void exitSetStatement(CobolIsuzuParser.SetStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#setToStatement}.
	 * @param ctx the parse tree
	 */
	void enterSetToStatement(CobolIsuzuParser.SetToStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#setToStatement}.
	 * @param ctx the parse tree
	 */
	void exitSetToStatement(CobolIsuzuParser.SetToStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#setUpDownByStatement}.
	 * @param ctx the parse tree
	 */
	void enterSetUpDownByStatement(CobolIsuzuParser.SetUpDownByStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#setUpDownByStatement}.
	 * @param ctx the parse tree
	 */
	void exitSetUpDownByStatement(CobolIsuzuParser.SetUpDownByStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#setTo}.
	 * @param ctx the parse tree
	 */
	void enterSetTo(CobolIsuzuParser.SetToContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#setTo}.
	 * @param ctx the parse tree
	 */
	void exitSetTo(CobolIsuzuParser.SetToContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#setToValue}.
	 * @param ctx the parse tree
	 */
	void enterSetToValue(CobolIsuzuParser.SetToValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#setToValue}.
	 * @param ctx the parse tree
	 */
	void exitSetToValue(CobolIsuzuParser.SetToValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#setByValue}.
	 * @param ctx the parse tree
	 */
	void enterSetByValue(CobolIsuzuParser.SetByValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#setByValue}.
	 * @param ctx the parse tree
	 */
	void exitSetByValue(CobolIsuzuParser.SetByValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#sortStatement}.
	 * @param ctx the parse tree
	 */
	void enterSortStatement(CobolIsuzuParser.SortStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#sortStatement}.
	 * @param ctx the parse tree
	 */
	void exitSortStatement(CobolIsuzuParser.SortStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#sortOnKeyClause}.
	 * @param ctx the parse tree
	 */
	void enterSortOnKeyClause(CobolIsuzuParser.SortOnKeyClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#sortOnKeyClause}.
	 * @param ctx the parse tree
	 */
	void exitSortOnKeyClause(CobolIsuzuParser.SortOnKeyClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#sortDuplicatesPhrase}.
	 * @param ctx the parse tree
	 */
	void enterSortDuplicatesPhrase(CobolIsuzuParser.SortDuplicatesPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#sortDuplicatesPhrase}.
	 * @param ctx the parse tree
	 */
	void exitSortDuplicatesPhrase(CobolIsuzuParser.SortDuplicatesPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#sortCollatingSequencePhrase}.
	 * @param ctx the parse tree
	 */
	void enterSortCollatingSequencePhrase(CobolIsuzuParser.SortCollatingSequencePhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#sortCollatingSequencePhrase}.
	 * @param ctx the parse tree
	 */
	void exitSortCollatingSequencePhrase(CobolIsuzuParser.SortCollatingSequencePhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#sortCollatingAlphanumeric}.
	 * @param ctx the parse tree
	 */
	void enterSortCollatingAlphanumeric(CobolIsuzuParser.SortCollatingAlphanumericContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#sortCollatingAlphanumeric}.
	 * @param ctx the parse tree
	 */
	void exitSortCollatingAlphanumeric(CobolIsuzuParser.SortCollatingAlphanumericContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#sortCollatingNational}.
	 * @param ctx the parse tree
	 */
	void enterSortCollatingNational(CobolIsuzuParser.SortCollatingNationalContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#sortCollatingNational}.
	 * @param ctx the parse tree
	 */
	void exitSortCollatingNational(CobolIsuzuParser.SortCollatingNationalContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#sortInputProcedurePhrase}.
	 * @param ctx the parse tree
	 */
	void enterSortInputProcedurePhrase(CobolIsuzuParser.SortInputProcedurePhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#sortInputProcedurePhrase}.
	 * @param ctx the parse tree
	 */
	void exitSortInputProcedurePhrase(CobolIsuzuParser.SortInputProcedurePhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#sortInputThrough}.
	 * @param ctx the parse tree
	 */
	void enterSortInputThrough(CobolIsuzuParser.SortInputThroughContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#sortInputThrough}.
	 * @param ctx the parse tree
	 */
	void exitSortInputThrough(CobolIsuzuParser.SortInputThroughContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#sortUsing}.
	 * @param ctx the parse tree
	 */
	void enterSortUsing(CobolIsuzuParser.SortUsingContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#sortUsing}.
	 * @param ctx the parse tree
	 */
	void exitSortUsing(CobolIsuzuParser.SortUsingContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#sortOutputProcedurePhrase}.
	 * @param ctx the parse tree
	 */
	void enterSortOutputProcedurePhrase(CobolIsuzuParser.SortOutputProcedurePhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#sortOutputProcedurePhrase}.
	 * @param ctx the parse tree
	 */
	void exitSortOutputProcedurePhrase(CobolIsuzuParser.SortOutputProcedurePhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#sortOutputThrough}.
	 * @param ctx the parse tree
	 */
	void enterSortOutputThrough(CobolIsuzuParser.SortOutputThroughContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#sortOutputThrough}.
	 * @param ctx the parse tree
	 */
	void exitSortOutputThrough(CobolIsuzuParser.SortOutputThroughContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#sortGivingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterSortGivingPhrase(CobolIsuzuParser.SortGivingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#sortGivingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitSortGivingPhrase(CobolIsuzuParser.SortGivingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#sortGiving}.
	 * @param ctx the parse tree
	 */
	void enterSortGiving(CobolIsuzuParser.SortGivingContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#sortGiving}.
	 * @param ctx the parse tree
	 */
	void exitSortGiving(CobolIsuzuParser.SortGivingContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#startStatement}.
	 * @param ctx the parse tree
	 */
	void enterStartStatement(CobolIsuzuParser.StartStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#startStatement}.
	 * @param ctx the parse tree
	 */
	void exitStartStatement(CobolIsuzuParser.StartStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#startKey}.
	 * @param ctx the parse tree
	 */
	void enterStartKey(CobolIsuzuParser.StartKeyContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#startKey}.
	 * @param ctx the parse tree
	 */
	void exitStartKey(CobolIsuzuParser.StartKeyContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#stopStatement}.
	 * @param ctx the parse tree
	 */
	void enterStopStatement(CobolIsuzuParser.StopStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#stopStatement}.
	 * @param ctx the parse tree
	 */
	void exitStopStatement(CobolIsuzuParser.StopStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#stringStatement}.
	 * @param ctx the parse tree
	 */
	void enterStringStatement(CobolIsuzuParser.StringStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#stringStatement}.
	 * @param ctx the parse tree
	 */
	void exitStringStatement(CobolIsuzuParser.StringStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#stringSendingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterStringSendingPhrase(CobolIsuzuParser.StringSendingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#stringSendingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitStringSendingPhrase(CobolIsuzuParser.StringSendingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#stringSending}.
	 * @param ctx the parse tree
	 */
	void enterStringSending(CobolIsuzuParser.StringSendingContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#stringSending}.
	 * @param ctx the parse tree
	 */
	void exitStringSending(CobolIsuzuParser.StringSendingContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#stringDelimitedByPhrase}.
	 * @param ctx the parse tree
	 */
	void enterStringDelimitedByPhrase(CobolIsuzuParser.StringDelimitedByPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#stringDelimitedByPhrase}.
	 * @param ctx the parse tree
	 */
	void exitStringDelimitedByPhrase(CobolIsuzuParser.StringDelimitedByPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#stringForPhrase}.
	 * @param ctx the parse tree
	 */
	void enterStringForPhrase(CobolIsuzuParser.StringForPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#stringForPhrase}.
	 * @param ctx the parse tree
	 */
	void exitStringForPhrase(CobolIsuzuParser.StringForPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#stringIntoPhrase}.
	 * @param ctx the parse tree
	 */
	void enterStringIntoPhrase(CobolIsuzuParser.StringIntoPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#stringIntoPhrase}.
	 * @param ctx the parse tree
	 */
	void exitStringIntoPhrase(CobolIsuzuParser.StringIntoPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#stringWithPointerPhrase}.
	 * @param ctx the parse tree
	 */
	void enterStringWithPointerPhrase(CobolIsuzuParser.StringWithPointerPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#stringWithPointerPhrase}.
	 * @param ctx the parse tree
	 */
	void exitStringWithPointerPhrase(CobolIsuzuParser.StringWithPointerPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#subtractStatement}.
	 * @param ctx the parse tree
	 */
	void enterSubtractStatement(CobolIsuzuParser.SubtractStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#subtractStatement}.
	 * @param ctx the parse tree
	 */
	void exitSubtractStatement(CobolIsuzuParser.SubtractStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#subtractFromStatement}.
	 * @param ctx the parse tree
	 */
	void enterSubtractFromStatement(CobolIsuzuParser.SubtractFromStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#subtractFromStatement}.
	 * @param ctx the parse tree
	 */
	void exitSubtractFromStatement(CobolIsuzuParser.SubtractFromStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#subtractFromGivingStatement}.
	 * @param ctx the parse tree
	 */
	void enterSubtractFromGivingStatement(CobolIsuzuParser.SubtractFromGivingStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#subtractFromGivingStatement}.
	 * @param ctx the parse tree
	 */
	void exitSubtractFromGivingStatement(CobolIsuzuParser.SubtractFromGivingStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#subtractCorrespondingStatement}.
	 * @param ctx the parse tree
	 */
	void enterSubtractCorrespondingStatement(CobolIsuzuParser.SubtractCorrespondingStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#subtractCorrespondingStatement}.
	 * @param ctx the parse tree
	 */
	void exitSubtractCorrespondingStatement(CobolIsuzuParser.SubtractCorrespondingStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#subtractSubtrahend}.
	 * @param ctx the parse tree
	 */
	void enterSubtractSubtrahend(CobolIsuzuParser.SubtractSubtrahendContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#subtractSubtrahend}.
	 * @param ctx the parse tree
	 */
	void exitSubtractSubtrahend(CobolIsuzuParser.SubtractSubtrahendContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#subtractMinuend}.
	 * @param ctx the parse tree
	 */
	void enterSubtractMinuend(CobolIsuzuParser.SubtractMinuendContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#subtractMinuend}.
	 * @param ctx the parse tree
	 */
	void exitSubtractMinuend(CobolIsuzuParser.SubtractMinuendContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#subtractMinuendGiving}.
	 * @param ctx the parse tree
	 */
	void enterSubtractMinuendGiving(CobolIsuzuParser.SubtractMinuendGivingContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#subtractMinuendGiving}.
	 * @param ctx the parse tree
	 */
	void exitSubtractMinuendGiving(CobolIsuzuParser.SubtractMinuendGivingContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#subtractGiving}.
	 * @param ctx the parse tree
	 */
	void enterSubtractGiving(CobolIsuzuParser.SubtractGivingContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#subtractGiving}.
	 * @param ctx the parse tree
	 */
	void exitSubtractGiving(CobolIsuzuParser.SubtractGivingContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#subtractMinuendCorresponding}.
	 * @param ctx the parse tree
	 */
	void enterSubtractMinuendCorresponding(CobolIsuzuParser.SubtractMinuendCorrespondingContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#subtractMinuendCorresponding}.
	 * @param ctx the parse tree
	 */
	void exitSubtractMinuendCorresponding(CobolIsuzuParser.SubtractMinuendCorrespondingContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#transactionStatement}.
	 * @param ctx the parse tree
	 */
	void enterTransactionStatement(CobolIsuzuParser.TransactionStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#transactionStatement}.
	 * @param ctx the parse tree
	 */
	void exitTransactionStatement(CobolIsuzuParser.TransactionStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#transactionStart}.
	 * @param ctx the parse tree
	 */
	void enterTransactionStart(CobolIsuzuParser.TransactionStartContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#transactionStart}.
	 * @param ctx the parse tree
	 */
	void exitTransactionStart(CobolIsuzuParser.TransactionStartContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#transactionBody}.
	 * @param ctx the parse tree
	 */
	void enterTransactionBody(CobolIsuzuParser.TransactionBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#transactionBody}.
	 * @param ctx the parse tree
	 */
	void exitTransactionBody(CobolIsuzuParser.TransactionBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#transactionEnd}.
	 * @param ctx the parse tree
	 */
	void enterTransactionEnd(CobolIsuzuParser.TransactionEndContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#transactionEnd}.
	 * @param ctx the parse tree
	 */
	void exitTransactionEnd(CobolIsuzuParser.TransactionEndContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#transactionCancelStatement}.
	 * @param ctx the parse tree
	 */
	void enterTransactionCancelStatement(CobolIsuzuParser.TransactionCancelStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#transactionCancelStatement}.
	 * @param ctx the parse tree
	 */
	void exitTransactionCancelStatement(CobolIsuzuParser.TransactionCancelStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#terminateStatement}.
	 * @param ctx the parse tree
	 */
	void enterTerminateStatement(CobolIsuzuParser.TerminateStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#terminateStatement}.
	 * @param ctx the parse tree
	 */
	void exitTerminateStatement(CobolIsuzuParser.TerminateStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#unstringStatement}.
	 * @param ctx the parse tree
	 */
	void enterUnstringStatement(CobolIsuzuParser.UnstringStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#unstringStatement}.
	 * @param ctx the parse tree
	 */
	void exitUnstringStatement(CobolIsuzuParser.UnstringStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#unstringSendingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterUnstringSendingPhrase(CobolIsuzuParser.UnstringSendingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#unstringSendingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitUnstringSendingPhrase(CobolIsuzuParser.UnstringSendingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#unstringDelimitedByPhrase}.
	 * @param ctx the parse tree
	 */
	void enterUnstringDelimitedByPhrase(CobolIsuzuParser.UnstringDelimitedByPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#unstringDelimitedByPhrase}.
	 * @param ctx the parse tree
	 */
	void exitUnstringDelimitedByPhrase(CobolIsuzuParser.UnstringDelimitedByPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#unstringOrAllPhrase}.
	 * @param ctx the parse tree
	 */
	void enterUnstringOrAllPhrase(CobolIsuzuParser.UnstringOrAllPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#unstringOrAllPhrase}.
	 * @param ctx the parse tree
	 */
	void exitUnstringOrAllPhrase(CobolIsuzuParser.UnstringOrAllPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#unstringIntoPhrase}.
	 * @param ctx the parse tree
	 */
	void enterUnstringIntoPhrase(CobolIsuzuParser.UnstringIntoPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#unstringIntoPhrase}.
	 * @param ctx the parse tree
	 */
	void exitUnstringIntoPhrase(CobolIsuzuParser.UnstringIntoPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#unstringInto}.
	 * @param ctx the parse tree
	 */
	void enterUnstringInto(CobolIsuzuParser.UnstringIntoContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#unstringInto}.
	 * @param ctx the parse tree
	 */
	void exitUnstringInto(CobolIsuzuParser.UnstringIntoContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#unstringDelimiterIn}.
	 * @param ctx the parse tree
	 */
	void enterUnstringDelimiterIn(CobolIsuzuParser.UnstringDelimiterInContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#unstringDelimiterIn}.
	 * @param ctx the parse tree
	 */
	void exitUnstringDelimiterIn(CobolIsuzuParser.UnstringDelimiterInContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#unstringCountIn}.
	 * @param ctx the parse tree
	 */
	void enterUnstringCountIn(CobolIsuzuParser.UnstringCountInContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#unstringCountIn}.
	 * @param ctx the parse tree
	 */
	void exitUnstringCountIn(CobolIsuzuParser.UnstringCountInContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#unstringWithPointerPhrase}.
	 * @param ctx the parse tree
	 */
	void enterUnstringWithPointerPhrase(CobolIsuzuParser.UnstringWithPointerPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#unstringWithPointerPhrase}.
	 * @param ctx the parse tree
	 */
	void exitUnstringWithPointerPhrase(CobolIsuzuParser.UnstringWithPointerPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#unstringTallyingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterUnstringTallyingPhrase(CobolIsuzuParser.UnstringTallyingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#unstringTallyingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitUnstringTallyingPhrase(CobolIsuzuParser.UnstringTallyingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#useStatement}.
	 * @param ctx the parse tree
	 */
	void enterUseStatement(CobolIsuzuParser.UseStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#useStatement}.
	 * @param ctx the parse tree
	 */
	void exitUseStatement(CobolIsuzuParser.UseStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#useFor}.
	 * @param ctx the parse tree
	 */
	void enterUseFor(CobolIsuzuParser.UseForContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#useFor}.
	 * @param ctx the parse tree
	 */
	void exitUseFor(CobolIsuzuParser.UseForContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#useAfterClause}.
	 * @param ctx the parse tree
	 */
	void enterUseAfterClause(CobolIsuzuParser.UseAfterClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#useAfterClause}.
	 * @param ctx the parse tree
	 */
	void exitUseAfterClause(CobolIsuzuParser.UseAfterClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#useAfterOn}.
	 * @param ctx the parse tree
	 */
	void enterUseAfterOn(CobolIsuzuParser.UseAfterOnContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#useAfterOn}.
	 * @param ctx the parse tree
	 */
	void exitUseAfterOn(CobolIsuzuParser.UseAfterOnContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#useDebugClause}.
	 * @param ctx the parse tree
	 */
	void enterUseDebugClause(CobolIsuzuParser.UseDebugClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#useDebugClause}.
	 * @param ctx the parse tree
	 */
	void exitUseDebugClause(CobolIsuzuParser.UseDebugClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#useDebugOn}.
	 * @param ctx the parse tree
	 */
	void enterUseDebugOn(CobolIsuzuParser.UseDebugOnContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#useDebugOn}.
	 * @param ctx the parse tree
	 */
	void exitUseDebugOn(CobolIsuzuParser.UseDebugOnContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#useDeadLock}.
	 * @param ctx the parse tree
	 */
	void enterUseDeadLock(CobolIsuzuParser.UseDeadLockContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#useDeadLock}.
	 * @param ctx the parse tree
	 */
	void exitUseDeadLock(CobolIsuzuParser.UseDeadLockContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#writeStatement}.
	 * @param ctx the parse tree
	 */
	void enterWriteStatement(CobolIsuzuParser.WriteStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#writeStatement}.
	 * @param ctx the parse tree
	 */
	void exitWriteStatement(CobolIsuzuParser.WriteStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#writeFromPhrase}.
	 * @param ctx the parse tree
	 */
	void enterWriteFromPhrase(CobolIsuzuParser.WriteFromPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#writeFromPhrase}.
	 * @param ctx the parse tree
	 */
	void exitWriteFromPhrase(CobolIsuzuParser.WriteFromPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#writeAdvancingPhrase}.
	 * @param ctx the parse tree
	 */
	void enterWriteAdvancingPhrase(CobolIsuzuParser.WriteAdvancingPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#writeAdvancingPhrase}.
	 * @param ctx the parse tree
	 */
	void exitWriteAdvancingPhrase(CobolIsuzuParser.WriteAdvancingPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#writeAdvancingPage}.
	 * @param ctx the parse tree
	 */
	void enterWriteAdvancingPage(CobolIsuzuParser.WriteAdvancingPageContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#writeAdvancingPage}.
	 * @param ctx the parse tree
	 */
	void exitWriteAdvancingPage(CobolIsuzuParser.WriteAdvancingPageContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#writeAdvancingLines}.
	 * @param ctx the parse tree
	 */
	void enterWriteAdvancingLines(CobolIsuzuParser.WriteAdvancingLinesContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#writeAdvancingLines}.
	 * @param ctx the parse tree
	 */
	void exitWriteAdvancingLines(CobolIsuzuParser.WriteAdvancingLinesContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#writeAdvancingMnemonic}.
	 * @param ctx the parse tree
	 */
	void enterWriteAdvancingMnemonic(CobolIsuzuParser.WriteAdvancingMnemonicContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#writeAdvancingMnemonic}.
	 * @param ctx the parse tree
	 */
	void exitWriteAdvancingMnemonic(CobolIsuzuParser.WriteAdvancingMnemonicContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#writeAtEndOfPagePhrase}.
	 * @param ctx the parse tree
	 */
	void enterWriteAtEndOfPagePhrase(CobolIsuzuParser.WriteAtEndOfPagePhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#writeAtEndOfPagePhrase}.
	 * @param ctx the parse tree
	 */
	void exitWriteAtEndOfPagePhrase(CobolIsuzuParser.WriteAtEndOfPagePhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#writeNotAtEndOfPagePhrase}.
	 * @param ctx the parse tree
	 */
	void enterWriteNotAtEndOfPagePhrase(CobolIsuzuParser.WriteNotAtEndOfPagePhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#writeNotAtEndOfPagePhrase}.
	 * @param ctx the parse tree
	 */
	void exitWriteNotAtEndOfPagePhrase(CobolIsuzuParser.WriteNotAtEndOfPagePhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#atEndPhrase}.
	 * @param ctx the parse tree
	 */
	void enterAtEndPhrase(CobolIsuzuParser.AtEndPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#atEndPhrase}.
	 * @param ctx the parse tree
	 */
	void exitAtEndPhrase(CobolIsuzuParser.AtEndPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#notAtEndPhrase}.
	 * @param ctx the parse tree
	 */
	void enterNotAtEndPhrase(CobolIsuzuParser.NotAtEndPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#notAtEndPhrase}.
	 * @param ctx the parse tree
	 */
	void exitNotAtEndPhrase(CobolIsuzuParser.NotAtEndPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#invalidKeyPhrase}.
	 * @param ctx the parse tree
	 */
	void enterInvalidKeyPhrase(CobolIsuzuParser.InvalidKeyPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#invalidKeyPhrase}.
	 * @param ctx the parse tree
	 */
	void exitInvalidKeyPhrase(CobolIsuzuParser.InvalidKeyPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#notInvalidKeyPhrase}.
	 * @param ctx the parse tree
	 */
	void enterNotInvalidKeyPhrase(CobolIsuzuParser.NotInvalidKeyPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#notInvalidKeyPhrase}.
	 * @param ctx the parse tree
	 */
	void exitNotInvalidKeyPhrase(CobolIsuzuParser.NotInvalidKeyPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#onOverflowPhrase}.
	 * @param ctx the parse tree
	 */
	void enterOnOverflowPhrase(CobolIsuzuParser.OnOverflowPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#onOverflowPhrase}.
	 * @param ctx the parse tree
	 */
	void exitOnOverflowPhrase(CobolIsuzuParser.OnOverflowPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#notOnOverflowPhrase}.
	 * @param ctx the parse tree
	 */
	void enterNotOnOverflowPhrase(CobolIsuzuParser.NotOnOverflowPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#notOnOverflowPhrase}.
	 * @param ctx the parse tree
	 */
	void exitNotOnOverflowPhrase(CobolIsuzuParser.NotOnOverflowPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#onSizeErrorPhrase}.
	 * @param ctx the parse tree
	 */
	void enterOnSizeErrorPhrase(CobolIsuzuParser.OnSizeErrorPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#onSizeErrorPhrase}.
	 * @param ctx the parse tree
	 */
	void exitOnSizeErrorPhrase(CobolIsuzuParser.OnSizeErrorPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#notOnSizeErrorPhrase}.
	 * @param ctx the parse tree
	 */
	void enterNotOnSizeErrorPhrase(CobolIsuzuParser.NotOnSizeErrorPhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#notOnSizeErrorPhrase}.
	 * @param ctx the parse tree
	 */
	void exitNotOnSizeErrorPhrase(CobolIsuzuParser.NotOnSizeErrorPhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#onExceptionClause}.
	 * @param ctx the parse tree
	 */
	void enterOnExceptionClause(CobolIsuzuParser.OnExceptionClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#onExceptionClause}.
	 * @param ctx the parse tree
	 */
	void exitOnExceptionClause(CobolIsuzuParser.OnExceptionClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#notOnExceptionClause}.
	 * @param ctx the parse tree
	 */
	void enterNotOnExceptionClause(CobolIsuzuParser.NotOnExceptionClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#notOnExceptionClause}.
	 * @param ctx the parse tree
	 */
	void exitNotOnExceptionClause(CobolIsuzuParser.NotOnExceptionClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#arithmeticExpression}.
	 * @param ctx the parse tree
	 */
	void enterArithmeticExpression(CobolIsuzuParser.ArithmeticExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#arithmeticExpression}.
	 * @param ctx the parse tree
	 */
	void exitArithmeticExpression(CobolIsuzuParser.ArithmeticExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#plusMinus}.
	 * @param ctx the parse tree
	 */
	void enterPlusMinus(CobolIsuzuParser.PlusMinusContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#plusMinus}.
	 * @param ctx the parse tree
	 */
	void exitPlusMinus(CobolIsuzuParser.PlusMinusContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#multDivs}.
	 * @param ctx the parse tree
	 */
	void enterMultDivs(CobolIsuzuParser.MultDivsContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#multDivs}.
	 * @param ctx the parse tree
	 */
	void exitMultDivs(CobolIsuzuParser.MultDivsContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#multDiv}.
	 * @param ctx the parse tree
	 */
	void enterMultDiv(CobolIsuzuParser.MultDivContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#multDiv}.
	 * @param ctx the parse tree
	 */
	void exitMultDiv(CobolIsuzuParser.MultDivContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#powers}.
	 * @param ctx the parse tree
	 */
	void enterPowers(CobolIsuzuParser.PowersContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#powers}.
	 * @param ctx the parse tree
	 */
	void exitPowers(CobolIsuzuParser.PowersContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#power}.
	 * @param ctx the parse tree
	 */
	void enterPower(CobolIsuzuParser.PowerContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#power}.
	 * @param ctx the parse tree
	 */
	void exitPower(CobolIsuzuParser.PowerContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#basis}.
	 * @param ctx the parse tree
	 */
	void enterBasis(CobolIsuzuParser.BasisContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#basis}.
	 * @param ctx the parse tree
	 */
	void exitBasis(CobolIsuzuParser.BasisContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(CobolIsuzuParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(CobolIsuzuParser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#andOrCondition}.
	 * @param ctx the parse tree
	 */
	void enterAndOrCondition(CobolIsuzuParser.AndOrConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#andOrCondition}.
	 * @param ctx the parse tree
	 */
	void exitAndOrCondition(CobolIsuzuParser.AndOrConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#combinableCondition}.
	 * @param ctx the parse tree
	 */
	void enterCombinableCondition(CobolIsuzuParser.CombinableConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#combinableCondition}.
	 * @param ctx the parse tree
	 */
	void exitCombinableCondition(CobolIsuzuParser.CombinableConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#simpleCondition}.
	 * @param ctx the parse tree
	 */
	void enterSimpleCondition(CobolIsuzuParser.SimpleConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#simpleCondition}.
	 * @param ctx the parse tree
	 */
	void exitSimpleCondition(CobolIsuzuParser.SimpleConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#classCondition}.
	 * @param ctx the parse tree
	 */
	void enterClassCondition(CobolIsuzuParser.ClassConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#classCondition}.
	 * @param ctx the parse tree
	 */
	void exitClassCondition(CobolIsuzuParser.ClassConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#conditionNameReference}.
	 * @param ctx the parse tree
	 */
	void enterConditionNameReference(CobolIsuzuParser.ConditionNameReferenceContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#conditionNameReference}.
	 * @param ctx the parse tree
	 */
	void exitConditionNameReference(CobolIsuzuParser.ConditionNameReferenceContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#conditionNameSubscriptReference}.
	 * @param ctx the parse tree
	 */
	void enterConditionNameSubscriptReference(CobolIsuzuParser.ConditionNameSubscriptReferenceContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#conditionNameSubscriptReference}.
	 * @param ctx the parse tree
	 */
	void exitConditionNameSubscriptReference(CobolIsuzuParser.ConditionNameSubscriptReferenceContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#relationCondition}.
	 * @param ctx the parse tree
	 */
	void enterRelationCondition(CobolIsuzuParser.RelationConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#relationCondition}.
	 * @param ctx the parse tree
	 */
	void exitRelationCondition(CobolIsuzuParser.RelationConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#relationSignCondition}.
	 * @param ctx the parse tree
	 */
	void enterRelationSignCondition(CobolIsuzuParser.RelationSignConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#relationSignCondition}.
	 * @param ctx the parse tree
	 */
	void exitRelationSignCondition(CobolIsuzuParser.RelationSignConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#relationArithmeticComparison}.
	 * @param ctx the parse tree
	 */
	void enterRelationArithmeticComparison(CobolIsuzuParser.RelationArithmeticComparisonContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#relationArithmeticComparison}.
	 * @param ctx the parse tree
	 */
	void exitRelationArithmeticComparison(CobolIsuzuParser.RelationArithmeticComparisonContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#relationCombinedComparison}.
	 * @param ctx the parse tree
	 */
	void enterRelationCombinedComparison(CobolIsuzuParser.RelationCombinedComparisonContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#relationCombinedComparison}.
	 * @param ctx the parse tree
	 */
	void exitRelationCombinedComparison(CobolIsuzuParser.RelationCombinedComparisonContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#relationCombinedCondition}.
	 * @param ctx the parse tree
	 */
	void enterRelationCombinedCondition(CobolIsuzuParser.RelationCombinedConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#relationCombinedCondition}.
	 * @param ctx the parse tree
	 */
	void exitRelationCombinedCondition(CobolIsuzuParser.RelationCombinedConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#relationalOperator}.
	 * @param ctx the parse tree
	 */
	void enterRelationalOperator(CobolIsuzuParser.RelationalOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#relationalOperator}.
	 * @param ctx the parse tree
	 */
	void exitRelationalOperator(CobolIsuzuParser.RelationalOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#abbreviation}.
	 * @param ctx the parse tree
	 */
	void enterAbbreviation(CobolIsuzuParser.AbbreviationContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#abbreviation}.
	 * @param ctx the parse tree
	 */
	void exitAbbreviation(CobolIsuzuParser.AbbreviationContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#identifier}.
	 * @param ctx the parse tree
	 */
	void enterIdentifier(CobolIsuzuParser.IdentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#identifier}.
	 * @param ctx the parse tree
	 */
	void exitIdentifier(CobolIsuzuParser.IdentifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#tableCall}.
	 * @param ctx the parse tree
	 */
	void enterTableCall(CobolIsuzuParser.TableCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#tableCall}.
	 * @param ctx the parse tree
	 */
	void exitTableCall(CobolIsuzuParser.TableCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCall(CobolIsuzuParser.FunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCall(CobolIsuzuParser.FunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#referenceModifier}.
	 * @param ctx the parse tree
	 */
	void enterReferenceModifier(CobolIsuzuParser.ReferenceModifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#referenceModifier}.
	 * @param ctx the parse tree
	 */
	void exitReferenceModifier(CobolIsuzuParser.ReferenceModifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#characterPosition}.
	 * @param ctx the parse tree
	 */
	void enterCharacterPosition(CobolIsuzuParser.CharacterPositionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#characterPosition}.
	 * @param ctx the parse tree
	 */
	void exitCharacterPosition(CobolIsuzuParser.CharacterPositionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#length}.
	 * @param ctx the parse tree
	 */
	void enterLength(CobolIsuzuParser.LengthContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#length}.
	 * @param ctx the parse tree
	 */
	void exitLength(CobolIsuzuParser.LengthContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#subscript_}.
	 * @param ctx the parse tree
	 */
	void enterSubscript_(CobolIsuzuParser.Subscript_Context ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#subscript_}.
	 * @param ctx the parse tree
	 */
	void exitSubscript_(CobolIsuzuParser.Subscript_Context ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#argument}.
	 * @param ctx the parse tree
	 */
	void enterArgument(CobolIsuzuParser.ArgumentContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#argument}.
	 * @param ctx the parse tree
	 */
	void exitArgument(CobolIsuzuParser.ArgumentContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#qualifiedDataName}.
	 * @param ctx the parse tree
	 */
	void enterQualifiedDataName(CobolIsuzuParser.QualifiedDataNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#qualifiedDataName}.
	 * @param ctx the parse tree
	 */
	void exitQualifiedDataName(CobolIsuzuParser.QualifiedDataNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#qualifiedDataNameFormat1}.
	 * @param ctx the parse tree
	 */
	void enterQualifiedDataNameFormat1(CobolIsuzuParser.QualifiedDataNameFormat1Context ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#qualifiedDataNameFormat1}.
	 * @param ctx the parse tree
	 */
	void exitQualifiedDataNameFormat1(CobolIsuzuParser.QualifiedDataNameFormat1Context ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#qualifiedDataNameFormat2}.
	 * @param ctx the parse tree
	 */
	void enterQualifiedDataNameFormat2(CobolIsuzuParser.QualifiedDataNameFormat2Context ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#qualifiedDataNameFormat2}.
	 * @param ctx the parse tree
	 */
	void exitQualifiedDataNameFormat2(CobolIsuzuParser.QualifiedDataNameFormat2Context ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#qualifiedDataNameFormat3}.
	 * @param ctx the parse tree
	 */
	void enterQualifiedDataNameFormat3(CobolIsuzuParser.QualifiedDataNameFormat3Context ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#qualifiedDataNameFormat3}.
	 * @param ctx the parse tree
	 */
	void exitQualifiedDataNameFormat3(CobolIsuzuParser.QualifiedDataNameFormat3Context ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#qualifiedDataNameFormat4}.
	 * @param ctx the parse tree
	 */
	void enterQualifiedDataNameFormat4(CobolIsuzuParser.QualifiedDataNameFormat4Context ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#qualifiedDataNameFormat4}.
	 * @param ctx the parse tree
	 */
	void exitQualifiedDataNameFormat4(CobolIsuzuParser.QualifiedDataNameFormat4Context ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#qualifiedInData}.
	 * @param ctx the parse tree
	 */
	void enterQualifiedInData(CobolIsuzuParser.QualifiedInDataContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#qualifiedInData}.
	 * @param ctx the parse tree
	 */
	void exitQualifiedInData(CobolIsuzuParser.QualifiedInDataContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#inData}.
	 * @param ctx the parse tree
	 */
	void enterInData(CobolIsuzuParser.InDataContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#inData}.
	 * @param ctx the parse tree
	 */
	void exitInData(CobolIsuzuParser.InDataContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#inFile}.
	 * @param ctx the parse tree
	 */
	void enterInFile(CobolIsuzuParser.InFileContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#inFile}.
	 * @param ctx the parse tree
	 */
	void exitInFile(CobolIsuzuParser.InFileContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#inMnemonic}.
	 * @param ctx the parse tree
	 */
	void enterInMnemonic(CobolIsuzuParser.InMnemonicContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#inMnemonic}.
	 * @param ctx the parse tree
	 */
	void exitInMnemonic(CobolIsuzuParser.InMnemonicContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#inSection}.
	 * @param ctx the parse tree
	 */
	void enterInSection(CobolIsuzuParser.InSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#inSection}.
	 * @param ctx the parse tree
	 */
	void exitInSection(CobolIsuzuParser.InSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#inLibrary}.
	 * @param ctx the parse tree
	 */
	void enterInLibrary(CobolIsuzuParser.InLibraryContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#inLibrary}.
	 * @param ctx the parse tree
	 */
	void exitInLibrary(CobolIsuzuParser.InLibraryContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#inTable}.
	 * @param ctx the parse tree
	 */
	void enterInTable(CobolIsuzuParser.InTableContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#inTable}.
	 * @param ctx the parse tree
	 */
	void exitInTable(CobolIsuzuParser.InTableContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#alphabetName}.
	 * @param ctx the parse tree
	 */
	void enterAlphabetName(CobolIsuzuParser.AlphabetNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#alphabetName}.
	 * @param ctx the parse tree
	 */
	void exitAlphabetName(CobolIsuzuParser.AlphabetNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#assignmentName}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentName(CobolIsuzuParser.AssignmentNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#assignmentName}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentName(CobolIsuzuParser.AssignmentNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#basisName}.
	 * @param ctx the parse tree
	 */
	void enterBasisName(CobolIsuzuParser.BasisNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#basisName}.
	 * @param ctx the parse tree
	 */
	void exitBasisName(CobolIsuzuParser.BasisNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#cdName}.
	 * @param ctx the parse tree
	 */
	void enterCdName(CobolIsuzuParser.CdNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#cdName}.
	 * @param ctx the parse tree
	 */
	void exitCdName(CobolIsuzuParser.CdNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#className}.
	 * @param ctx the parse tree
	 */
	void enterClassName(CobolIsuzuParser.ClassNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#className}.
	 * @param ctx the parse tree
	 */
	void exitClassName(CobolIsuzuParser.ClassNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#computerName}.
	 * @param ctx the parse tree
	 */
	void enterComputerName(CobolIsuzuParser.ComputerNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#computerName}.
	 * @param ctx the parse tree
	 */
	void exitComputerName(CobolIsuzuParser.ComputerNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#conditionName}.
	 * @param ctx the parse tree
	 */
	void enterConditionName(CobolIsuzuParser.ConditionNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#conditionName}.
	 * @param ctx the parse tree
	 */
	void exitConditionName(CobolIsuzuParser.ConditionNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataName}.
	 * @param ctx the parse tree
	 */
	void enterDataName(CobolIsuzuParser.DataNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataName}.
	 * @param ctx the parse tree
	 */
	void exitDataName(CobolIsuzuParser.DataNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#dataDescName}.
	 * @param ctx the parse tree
	 */
	void enterDataDescName(CobolIsuzuParser.DataDescNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#dataDescName}.
	 * @param ctx the parse tree
	 */
	void exitDataDescName(CobolIsuzuParser.DataDescNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#environmentName}.
	 * @param ctx the parse tree
	 */
	void enterEnvironmentName(CobolIsuzuParser.EnvironmentNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#environmentName}.
	 * @param ctx the parse tree
	 */
	void exitEnvironmentName(CobolIsuzuParser.EnvironmentNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#fileName}.
	 * @param ctx the parse tree
	 */
	void enterFileName(CobolIsuzuParser.FileNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#fileName}.
	 * @param ctx the parse tree
	 */
	void exitFileName(CobolIsuzuParser.FileNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#functionName}.
	 * @param ctx the parse tree
	 */
	void enterFunctionName(CobolIsuzuParser.FunctionNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#functionName}.
	 * @param ctx the parse tree
	 */
	void exitFunctionName(CobolIsuzuParser.FunctionNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#indexName}.
	 * @param ctx the parse tree
	 */
	void enterIndexName(CobolIsuzuParser.IndexNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#indexName}.
	 * @param ctx the parse tree
	 */
	void exitIndexName(CobolIsuzuParser.IndexNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#languageName}.
	 * @param ctx the parse tree
	 */
	void enterLanguageName(CobolIsuzuParser.LanguageNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#languageName}.
	 * @param ctx the parse tree
	 */
	void exitLanguageName(CobolIsuzuParser.LanguageNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#libraryName}.
	 * @param ctx the parse tree
	 */
	void enterLibraryName(CobolIsuzuParser.LibraryNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#libraryName}.
	 * @param ctx the parse tree
	 */
	void exitLibraryName(CobolIsuzuParser.LibraryNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#localName}.
	 * @param ctx the parse tree
	 */
	void enterLocalName(CobolIsuzuParser.LocalNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#localName}.
	 * @param ctx the parse tree
	 */
	void exitLocalName(CobolIsuzuParser.LocalNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#mnemonicName}.
	 * @param ctx the parse tree
	 */
	void enterMnemonicName(CobolIsuzuParser.MnemonicNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#mnemonicName}.
	 * @param ctx the parse tree
	 */
	void exitMnemonicName(CobolIsuzuParser.MnemonicNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#paragraphName}.
	 * @param ctx the parse tree
	 */
	void enterParagraphName(CobolIsuzuParser.ParagraphNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#paragraphName}.
	 * @param ctx the parse tree
	 */
	void exitParagraphName(CobolIsuzuParser.ParagraphNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#procedureName}.
	 * @param ctx the parse tree
	 */
	void enterProcedureName(CobolIsuzuParser.ProcedureNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#procedureName}.
	 * @param ctx the parse tree
	 */
	void exitProcedureName(CobolIsuzuParser.ProcedureNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#programName}.
	 * @param ctx the parse tree
	 */
	void enterProgramName(CobolIsuzuParser.ProgramNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#programName}.
	 * @param ctx the parse tree
	 */
	void exitProgramName(CobolIsuzuParser.ProgramNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#recordName}.
	 * @param ctx the parse tree
	 */
	void enterRecordName(CobolIsuzuParser.RecordNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#recordName}.
	 * @param ctx the parse tree
	 */
	void exitRecordName(CobolIsuzuParser.RecordNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#reportName}.
	 * @param ctx the parse tree
	 */
	void enterReportName(CobolIsuzuParser.ReportNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#reportName}.
	 * @param ctx the parse tree
	 */
	void exitReportName(CobolIsuzuParser.ReportNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#routineName}.
	 * @param ctx the parse tree
	 */
	void enterRoutineName(CobolIsuzuParser.RoutineNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#routineName}.
	 * @param ctx the parse tree
	 */
	void exitRoutineName(CobolIsuzuParser.RoutineNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#screenName}.
	 * @param ctx the parse tree
	 */
	void enterScreenName(CobolIsuzuParser.ScreenNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#screenName}.
	 * @param ctx the parse tree
	 */
	void exitScreenName(CobolIsuzuParser.ScreenNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#schemaName}.
	 * @param ctx the parse tree
	 */
	void enterSchemaName(CobolIsuzuParser.SchemaNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#schemaName}.
	 * @param ctx the parse tree
	 */
	void exitSchemaName(CobolIsuzuParser.SchemaNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#sectionName}.
	 * @param ctx the parse tree
	 */
	void enterSectionName(CobolIsuzuParser.SectionNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#sectionName}.
	 * @param ctx the parse tree
	 */
	void exitSectionName(CobolIsuzuParser.SectionNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#systemName}.
	 * @param ctx the parse tree
	 */
	void enterSystemName(CobolIsuzuParser.SystemNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#systemName}.
	 * @param ctx the parse tree
	 */
	void exitSystemName(CobolIsuzuParser.SystemNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#symbolicCharacter}.
	 * @param ctx the parse tree
	 */
	void enterSymbolicCharacter(CobolIsuzuParser.SymbolicCharacterContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#symbolicCharacter}.
	 * @param ctx the parse tree
	 */
	void exitSymbolicCharacter(CobolIsuzuParser.SymbolicCharacterContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#textName}.
	 * @param ctx the parse tree
	 */
	void enterTextName(CobolIsuzuParser.TextNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#textName}.
	 * @param ctx the parse tree
	 */
	void exitTextName(CobolIsuzuParser.TextNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#booleanLiteral}.
	 * @param ctx the parse tree
	 */
	void enterBooleanLiteral(CobolIsuzuParser.BooleanLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#booleanLiteral}.
	 * @param ctx the parse tree
	 */
	void exitBooleanLiteral(CobolIsuzuParser.BooleanLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#numericLiteral}.
	 * @param ctx the parse tree
	 */
	void enterNumericLiteral(CobolIsuzuParser.NumericLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#numericLiteral}.
	 * @param ctx the parse tree
	 */
	void exitNumericLiteral(CobolIsuzuParser.NumericLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#integerLiteral}.
	 * @param ctx the parse tree
	 */
	void enterIntegerLiteral(CobolIsuzuParser.IntegerLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#integerLiteral}.
	 * @param ctx the parse tree
	 */
	void exitIntegerLiteral(CobolIsuzuParser.IntegerLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#cicsDfhRespLiteral}.
	 * @param ctx the parse tree
	 */
	void enterCicsDfhRespLiteral(CobolIsuzuParser.CicsDfhRespLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#cicsDfhRespLiteral}.
	 * @param ctx the parse tree
	 */
	void exitCicsDfhRespLiteral(CobolIsuzuParser.CicsDfhRespLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#cicsDfhValueLiteral}.
	 * @param ctx the parse tree
	 */
	void enterCicsDfhValueLiteral(CobolIsuzuParser.CicsDfhValueLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#cicsDfhValueLiteral}.
	 * @param ctx the parse tree
	 */
	void exitCicsDfhValueLiteral(CobolIsuzuParser.CicsDfhValueLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#figurativeConstant}.
	 * @param ctx the parse tree
	 */
	void enterFigurativeConstant(CobolIsuzuParser.FigurativeConstantContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#figurativeConstant}.
	 * @param ctx the parse tree
	 */
	void exitFigurativeConstant(CobolIsuzuParser.FigurativeConstantContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#specialRegister}.
	 * @param ctx the parse tree
	 */
	void enterSpecialRegister(CobolIsuzuParser.SpecialRegisterContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#specialRegister}.
	 * @param ctx the parse tree
	 */
	void exitSpecialRegister(CobolIsuzuParser.SpecialRegisterContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#commentEntry}.
	 * @param ctx the parse tree
	 */
	void enterCommentEntry(CobolIsuzuParser.CommentEntryContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#commentEntry}.
	 * @param ctx the parse tree
	 */
	void exitCommentEntry(CobolIsuzuParser.CommentEntryContext ctx);
	/**
	 * Enter a parse tree produced by {@link CobolIsuzuParser#charDataKeyword}.
	 * @param ctx the parse tree
	 */
	void enterCharDataKeyword(CobolIsuzuParser.CharDataKeywordContext ctx);
	/**
	 * Exit a parse tree produced by {@link CobolIsuzuParser#charDataKeyword}.
	 * @param ctx the parse tree
	 */
	void exitCharDataKeyword(CobolIsuzuParser.CharDataKeywordContext ctx);
}