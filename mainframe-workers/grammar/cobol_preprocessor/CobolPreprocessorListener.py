# Generated from ./grammar/cobol_preprocessor/CobolPreprocessor.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CobolPreprocessorParser import CobolPreprocessorParser
else:
    from CobolPreprocessorParser import CobolPreprocessorParser

# This class defines a complete listener for a parse tree produced by CobolPreprocessorParser.
class CobolPreprocessorListener(ParseTreeListener):

    # Enter a parse tree produced by CobolPreprocessorParser#startRule.
    def enterStartRule(self, ctx:CobolPreprocessorParser.StartRuleContext):
        pass

    # Exit a parse tree produced by CobolPreprocessorParser#startRule.
    def exitStartRule(self, ctx:CobolPreprocessorParser.StartRuleContext):
        pass


    # Enter a parse tree produced by CobolPreprocessorParser#compilerOptions.
    def enterCompilerOptions(self, ctx:CobolPreprocessorParser.CompilerOptionsContext):
        pass

    # Exit a parse tree produced by CobolPreprocessorParser#compilerOptions.
    def exitCompilerOptions(self, ctx:CobolPreprocessorParser.CompilerOptionsContext):
        pass


    # Enter a parse tree produced by CobolPreprocessorParser#compilerXOpts.
    def enterCompilerXOpts(self, ctx:CobolPreprocessorParser.CompilerXOptsContext):
        pass

    # Exit a parse tree produced by CobolPreprocessorParser#compilerXOpts.
    def exitCompilerXOpts(self, ctx:CobolPreprocessorParser.CompilerXOptsContext):
        pass


    # Enter a parse tree produced by CobolPreprocessorParser#compilerOption.
    def enterCompilerOption(self, ctx:CobolPreprocessorParser.CompilerOptionContext):
        pass

    # Exit a parse tree produced by CobolPreprocessorParser#compilerOption.
    def exitCompilerOption(self, ctx:CobolPreprocessorParser.CompilerOptionContext):
        pass


    # Enter a parse tree produced by CobolPreprocessorParser#execCicsStatement.
    def enterExecCicsStatement(self, ctx:CobolPreprocessorParser.ExecCicsStatementContext):
        pass

    # Exit a parse tree produced by CobolPreprocessorParser#execCicsStatement.
    def exitExecCicsStatement(self, ctx:CobolPreprocessorParser.ExecCicsStatementContext):
        pass


    # Enter a parse tree produced by CobolPreprocessorParser#execSqlStatement.
    def enterExecSqlStatement(self, ctx:CobolPreprocessorParser.ExecSqlStatementContext):
        pass

    # Exit a parse tree produced by CobolPreprocessorParser#execSqlStatement.
    def exitExecSqlStatement(self, ctx:CobolPreprocessorParser.ExecSqlStatementContext):
        pass


    # Enter a parse tree produced by CobolPreprocessorParser#execSqlImsStatement.
    def enterExecSqlImsStatement(self, ctx:CobolPreprocessorParser.ExecSqlImsStatementContext):
        pass

    # Exit a parse tree produced by CobolPreprocessorParser#execSqlImsStatement.
    def exitExecSqlImsStatement(self, ctx:CobolPreprocessorParser.ExecSqlImsStatementContext):
        pass


    # Enter a parse tree produced by CobolPreprocessorParser#copyStatement.
    def enterCopyStatement(self, ctx:CobolPreprocessorParser.CopyStatementContext):
        pass

    # Exit a parse tree produced by CobolPreprocessorParser#copyStatement.
    def exitCopyStatement(self, ctx:CobolPreprocessorParser.CopyStatementContext):
        pass


    # Enter a parse tree produced by CobolPreprocessorParser#copySource.
    def enterCopySource(self, ctx:CobolPreprocessorParser.CopySourceContext):
        pass

    # Exit a parse tree produced by CobolPreprocessorParser#copySource.
    def exitCopySource(self, ctx:CobolPreprocessorParser.CopySourceContext):
        pass


    # Enter a parse tree produced by CobolPreprocessorParser#copyLibrary.
    def enterCopyLibrary(self, ctx:CobolPreprocessorParser.CopyLibraryContext):
        pass

    # Exit a parse tree produced by CobolPreprocessorParser#copyLibrary.
    def exitCopyLibrary(self, ctx:CobolPreprocessorParser.CopyLibraryContext):
        pass


    # Enter a parse tree produced by CobolPreprocessorParser#replacingPhrase.
    def enterReplacingPhrase(self, ctx:CobolPreprocessorParser.ReplacingPhraseContext):
        pass

    # Exit a parse tree produced by CobolPreprocessorParser#replacingPhrase.
    def exitReplacingPhrase(self, ctx:CobolPreprocessorParser.ReplacingPhraseContext):
        pass


    # Enter a parse tree produced by CobolPreprocessorParser#replaceArea.
    def enterReplaceArea(self, ctx:CobolPreprocessorParser.ReplaceAreaContext):
        pass

    # Exit a parse tree produced by CobolPreprocessorParser#replaceArea.
    def exitReplaceArea(self, ctx:CobolPreprocessorParser.ReplaceAreaContext):
        pass


    # Enter a parse tree produced by CobolPreprocessorParser#replaceByStatement.
    def enterReplaceByStatement(self, ctx:CobolPreprocessorParser.ReplaceByStatementContext):
        pass

    # Exit a parse tree produced by CobolPreprocessorParser#replaceByStatement.
    def exitReplaceByStatement(self, ctx:CobolPreprocessorParser.ReplaceByStatementContext):
        pass


    # Enter a parse tree produced by CobolPreprocessorParser#replaceOffStatement.
    def enterReplaceOffStatement(self, ctx:CobolPreprocessorParser.ReplaceOffStatementContext):
        pass

    # Exit a parse tree produced by CobolPreprocessorParser#replaceOffStatement.
    def exitReplaceOffStatement(self, ctx:CobolPreprocessorParser.ReplaceOffStatementContext):
        pass


    # Enter a parse tree produced by CobolPreprocessorParser#replaceClause.
    def enterReplaceClause(self, ctx:CobolPreprocessorParser.ReplaceClauseContext):
        pass

    # Exit a parse tree produced by CobolPreprocessorParser#replaceClause.
    def exitReplaceClause(self, ctx:CobolPreprocessorParser.ReplaceClauseContext):
        pass


    # Enter a parse tree produced by CobolPreprocessorParser#directoryPhrase.
    def enterDirectoryPhrase(self, ctx:CobolPreprocessorParser.DirectoryPhraseContext):
        pass

    # Exit a parse tree produced by CobolPreprocessorParser#directoryPhrase.
    def exitDirectoryPhrase(self, ctx:CobolPreprocessorParser.DirectoryPhraseContext):
        pass


    # Enter a parse tree produced by CobolPreprocessorParser#familyPhrase.
    def enterFamilyPhrase(self, ctx:CobolPreprocessorParser.FamilyPhraseContext):
        pass

    # Exit a parse tree produced by CobolPreprocessorParser#familyPhrase.
    def exitFamilyPhrase(self, ctx:CobolPreprocessorParser.FamilyPhraseContext):
        pass


    # Enter a parse tree produced by CobolPreprocessorParser#replaceable.
    def enterReplaceable(self, ctx:CobolPreprocessorParser.ReplaceableContext):
        pass

    # Exit a parse tree produced by CobolPreprocessorParser#replaceable.
    def exitReplaceable(self, ctx:CobolPreprocessorParser.ReplaceableContext):
        pass


    # Enter a parse tree produced by CobolPreprocessorParser#replacement.
    def enterReplacement(self, ctx:CobolPreprocessorParser.ReplacementContext):
        pass

    # Exit a parse tree produced by CobolPreprocessorParser#replacement.
    def exitReplacement(self, ctx:CobolPreprocessorParser.ReplacementContext):
        pass


    # Enter a parse tree produced by CobolPreprocessorParser#ejectStatement.
    def enterEjectStatement(self, ctx:CobolPreprocessorParser.EjectStatementContext):
        pass

    # Exit a parse tree produced by CobolPreprocessorParser#ejectStatement.
    def exitEjectStatement(self, ctx:CobolPreprocessorParser.EjectStatementContext):
        pass


    # Enter a parse tree produced by CobolPreprocessorParser#skipStatement.
    def enterSkipStatement(self, ctx:CobolPreprocessorParser.SkipStatementContext):
        pass

    # Exit a parse tree produced by CobolPreprocessorParser#skipStatement.
    def exitSkipStatement(self, ctx:CobolPreprocessorParser.SkipStatementContext):
        pass


    # Enter a parse tree produced by CobolPreprocessorParser#titleStatement.
    def enterTitleStatement(self, ctx:CobolPreprocessorParser.TitleStatementContext):
        pass

    # Exit a parse tree produced by CobolPreprocessorParser#titleStatement.
    def exitTitleStatement(self, ctx:CobolPreprocessorParser.TitleStatementContext):
        pass


    # Enter a parse tree produced by CobolPreprocessorParser#pseudoText.
    def enterPseudoText(self, ctx:CobolPreprocessorParser.PseudoTextContext):
        pass

    # Exit a parse tree produced by CobolPreprocessorParser#pseudoText.
    def exitPseudoText(self, ctx:CobolPreprocessorParser.PseudoTextContext):
        pass


    # Enter a parse tree produced by CobolPreprocessorParser#charData.
    def enterCharData(self, ctx:CobolPreprocessorParser.CharDataContext):
        pass

    # Exit a parse tree produced by CobolPreprocessorParser#charData.
    def exitCharData(self, ctx:CobolPreprocessorParser.CharDataContext):
        pass


    # Enter a parse tree produced by CobolPreprocessorParser#charDataSql.
    def enterCharDataSql(self, ctx:CobolPreprocessorParser.CharDataSqlContext):
        pass

    # Exit a parse tree produced by CobolPreprocessorParser#charDataSql.
    def exitCharDataSql(self, ctx:CobolPreprocessorParser.CharDataSqlContext):
        pass


    # Enter a parse tree produced by CobolPreprocessorParser#charDataLine.
    def enterCharDataLine(self, ctx:CobolPreprocessorParser.CharDataLineContext):
        pass

    # Exit a parse tree produced by CobolPreprocessorParser#charDataLine.
    def exitCharDataLine(self, ctx:CobolPreprocessorParser.CharDataLineContext):
        pass


    # Enter a parse tree produced by CobolPreprocessorParser#cobolWord.
    def enterCobolWord(self, ctx:CobolPreprocessorParser.CobolWordContext):
        pass

    # Exit a parse tree produced by CobolPreprocessorParser#cobolWord.
    def exitCobolWord(self, ctx:CobolPreprocessorParser.CobolWordContext):
        pass


    # Enter a parse tree produced by CobolPreprocessorParser#literal.
    def enterLiteral(self, ctx:CobolPreprocessorParser.LiteralContext):
        pass

    # Exit a parse tree produced by CobolPreprocessorParser#literal.
    def exitLiteral(self, ctx:CobolPreprocessorParser.LiteralContext):
        pass


    # Enter a parse tree produced by CobolPreprocessorParser#filename.
    def enterFilename(self, ctx:CobolPreprocessorParser.FilenameContext):
        pass

    # Exit a parse tree produced by CobolPreprocessorParser#filename.
    def exitFilename(self, ctx:CobolPreprocessorParser.FilenameContext):
        pass


    # Enter a parse tree produced by CobolPreprocessorParser#charDataKeyword.
    def enterCharDataKeyword(self, ctx:CobolPreprocessorParser.CharDataKeywordContext):
        pass

    # Exit a parse tree produced by CobolPreprocessorParser#charDataKeyword.
    def exitCharDataKeyword(self, ctx:CobolPreprocessorParser.CharDataKeywordContext):
        pass



del CobolPreprocessorParser