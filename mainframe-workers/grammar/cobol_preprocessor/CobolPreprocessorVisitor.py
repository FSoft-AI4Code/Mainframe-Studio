# Generated from ./grammar/cobol_preprocessor/CobolPreprocessor.g4 by ANTLR 4.13.2
from antlr4 import *

if "." in __name__:
    from .CobolPreprocessorParser import CobolPreprocessorParser
else:
    from CobolPreprocessorParser import CobolPreprocessorParser

# This class defines a complete generic visitor for a parse tree produced by CobolPreprocessorParser.


class CobolPreprocessorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CobolPreprocessorParser#startRule.
    def visitStartRule(self, ctx: CobolPreprocessorParser.StartRuleContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolPreprocessorParser#compilerOptions.
    def visitCompilerOptions(self, ctx: CobolPreprocessorParser.CompilerOptionsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolPreprocessorParser#compilerXOpts.
    def visitCompilerXOpts(self, ctx: CobolPreprocessorParser.CompilerXOptsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolPreprocessorParser#compilerOption.
    def visitCompilerOption(self, ctx: CobolPreprocessorParser.CompilerOptionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolPreprocessorParser#execCicsStatement.
    def visitExecCicsStatement(
        self, ctx: CobolPreprocessorParser.ExecCicsStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolPreprocessorParser#execSqlStatement.
    def visitExecSqlStatement(
        self, ctx: CobolPreprocessorParser.ExecSqlStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolPreprocessorParser#execSqlImsStatement.
    def visitExecSqlImsStatement(
        self, ctx: CobolPreprocessorParser.ExecSqlImsStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolPreprocessorParser#copyStatement.
    def visitCopyStatement(self, ctx: CobolPreprocessorParser.CopyStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolPreprocessorParser#copySource.
    def visitCopySource(self, ctx: CobolPreprocessorParser.CopySourceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolPreprocessorParser#copyLibrary.
    def visitCopyLibrary(self, ctx: CobolPreprocessorParser.CopyLibraryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolPreprocessorParser#replacingPhrase.
    def visitReplacingPhrase(self, ctx: CobolPreprocessorParser.ReplacingPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolPreprocessorParser#replaceArea.
    def visitReplaceArea(self, ctx: CobolPreprocessorParser.ReplaceAreaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolPreprocessorParser#replaceByStatement.
    def visitReplaceByStatement(
        self, ctx: CobolPreprocessorParser.ReplaceByStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolPreprocessorParser#replaceOffStatement.
    def visitReplaceOffStatement(
        self, ctx: CobolPreprocessorParser.ReplaceOffStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolPreprocessorParser#replaceClause.
    def visitReplaceClause(self, ctx: CobolPreprocessorParser.ReplaceClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolPreprocessorParser#directoryPhrase.
    def visitDirectoryPhrase(self, ctx: CobolPreprocessorParser.DirectoryPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolPreprocessorParser#familyPhrase.
    def visitFamilyPhrase(self, ctx: CobolPreprocessorParser.FamilyPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolPreprocessorParser#replaceable.
    def visitReplaceable(self, ctx: CobolPreprocessorParser.ReplaceableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolPreprocessorParser#replacement.
    def visitReplacement(self, ctx: CobolPreprocessorParser.ReplacementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolPreprocessorParser#ejectStatement.
    def visitEjectStatement(self, ctx: CobolPreprocessorParser.EjectStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolPreprocessorParser#skipStatement.
    def visitSkipStatement(self, ctx: CobolPreprocessorParser.SkipStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolPreprocessorParser#titleStatement.
    def visitTitleStatement(self, ctx: CobolPreprocessorParser.TitleStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolPreprocessorParser#pseudoText.
    def visitPseudoText(self, ctx: CobolPreprocessorParser.PseudoTextContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolPreprocessorParser#charData.
    def visitCharData(self, ctx: CobolPreprocessorParser.CharDataContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolPreprocessorParser#charDataSql.
    def visitCharDataSql(self, ctx: CobolPreprocessorParser.CharDataSqlContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolPreprocessorParser#charDataLine.
    def visitCharDataLine(self, ctx: CobolPreprocessorParser.CharDataLineContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolPreprocessorParser#cobolWord.
    def visitCobolWord(self, ctx: CobolPreprocessorParser.CobolWordContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolPreprocessorParser#literal.
    def visitLiteral(self, ctx: CobolPreprocessorParser.LiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolPreprocessorParser#filename.
    def visitFilename(self, ctx: CobolPreprocessorParser.FilenameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolPreprocessorParser#charDataKeyword.
    def visitCharDataKeyword(self, ctx: CobolPreprocessorParser.CharDataKeywordContext):
        return self.visitChildren(ctx)


del CobolPreprocessorParser
