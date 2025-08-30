# Generated from ./src/parsers/grammar/pli/PLI.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PLIParser import PLIParser
else:
    from PLIParser import PLIParser

# This class defines a complete generic visitor for a parse tree produced by PLIParser.

class PLIVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PLIParser#startRule.
    def visitStartRule(self, ctx:PLIParser.StartRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#firstline.
    def visitFirstline(self, ctx:PLIParser.FirstlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#procedureBlock.
    def visitProcedureBlock(self, ctx:PLIParser.ProcedureBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#inlineBlock.
    def visitInlineBlock(self, ctx:PLIParser.InlineBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#procedureContent.
    def visitProcedureContent(self, ctx:PLIParser.ProcedureContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#pl1stmtlist.
    def visitPl1stmtlist(self, ctx:PLIParser.Pl1stmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#preconditioncommalist.
    def visitPreconditioncommalist(self, ctx:PLIParser.PreconditioncommalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#prestmtlist.
    def visitPrestmtlist(self, ctx:PLIParser.PrestmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#pl1stmt.
    def visitPl1stmt(self, ctx:PLIParser.Pl1stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#otherBlock.
    def visitOtherBlock(self, ctx:PLIParser.OtherBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#onBlock.
    def visitOnBlock(self, ctx:PLIParser.OnBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#doBlock.
    def visitDoBlock(self, ctx:PLIParser.DoBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#doContent.
    def visitDoContent(self, ctx:PLIParser.DoContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#selectBlock.
    def visitSelectBlock(self, ctx:PLIParser.SelectBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#ifBlock.
    def visitIfBlock(self, ctx:PLIParser.IfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#stmtscopeend.
    def visitStmtscopeend(self, ctx:PLIParser.StmtscopeendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#stmtscope.
    def visitStmtscope(self, ctx:PLIParser.StmtscopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#stmt.
    def visitStmt(self, ctx:PLIParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#includestmt.
    def visitIncludestmt(self, ctx:PLIParser.IncludestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#filename.
    def visitFilename(self, ctx:PLIParser.FilenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#allocatestmt.
    def visitAllocatestmt(self, ctx:PLIParser.AllocatestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#allocateoptionlist.
    def visitAllocateoptionlist(self, ctx:PLIParser.AllocateoptionlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#allocateoption.
    def visitAllocateoption(self, ctx:PLIParser.AllocateoptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#attachstmt.
    def visitAttachstmt(self, ctx:PLIParser.AttachstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#ctloptionlist.
    def visitCtloptionlist(self, ctx:PLIParser.CtloptionlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#ctlvarattribute.
    def visitCtlvarattribute(self, ctx:PLIParser.CtlvarattributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#beginstmt.
    def visitBeginstmt(self, ctx:PLIParser.BeginstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#beginstmtoptionlist.
    def visitBeginstmtoptionlist(self, ctx:PLIParser.BeginstmtoptionlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#beginstmtoption.
    def visitBeginstmtoption(self, ctx:PLIParser.BeginstmtoptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#delaystmt.
    def visitDelaystmt(self, ctx:PLIParser.DelaystmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#callstmt.
    def visitCallstmt(self, ctx:PLIParser.CallstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#inlinestmt.
    def visitInlinestmt(self, ctx:PLIParser.InlinestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#closestmt.
    def visitClosestmt(self, ctx:PLIParser.ClosestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#defaultstmt.
    def visitDefaultstmt(self, ctx:PLIParser.DefaultstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#definealiasstmt.
    def visitDefinealiasstmt(self, ctx:PLIParser.DefinealiasstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#defineordinalstmt.
    def visitDefineordinalstmt(self, ctx:PLIParser.DefineordinalstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#definestructurestmt.
    def visitDefinestructurestmt(self, ctx:PLIParser.DefinestructurestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#dclstructurecommalist.
    def visitDclstructurecommalist(self, ctx:PLIParser.DclstructurecommalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#dclstructure.
    def visitDclstructure(self, ctx:PLIParser.DclstructureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#ordinalmembercommalist.
    def visitOrdinalmembercommalist(self, ctx:PLIParser.OrdinalmembercommalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#ordinalmember.
    def visitOrdinalmember(self, ctx:PLIParser.OrdinalmemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#ordinaloptionlist.
    def visitOrdinaloptionlist(self, ctx:PLIParser.OrdinaloptionlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#ordinaloption.
    def visitOrdinaloption(self, ctx:PLIParser.OrdinaloptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#displaystmt.
    def visitDisplaystmt(self, ctx:PLIParser.DisplaystmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#deletestmt.
    def visitDeletestmt(self, ctx:PLIParser.DeletestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#detachstmt.
    def visitDetachstmt(self, ctx:PLIParser.DetachstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#endstmt.
    def visitEndstmt(self, ctx:PLIParser.EndstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#entrystmt.
    def visitEntrystmt(self, ctx:PLIParser.EntrystmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#execstmt.
    def visitExecstmt(self, ctx:PLIParser.ExecstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#sqlstmt.
    def visitSqlstmt(self, ctx:PLIParser.SqlstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#cicsstmt.
    def visitCicsstmt(self, ctx:PLIParser.CicsstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#command.
    def visitCommand(self, ctx:PLIParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#field.
    def visitField(self, ctx:PLIParser.FieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#declare.
    def visitDeclare(self, ctx:PLIParser.DeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#execInclude.
    def visitExecInclude(self, ctx:PLIParser.ExecIncludeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#sqlCommand.
    def visitSqlCommand(self, ctx:PLIParser.SqlCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#sqlDescribe.
    def visitSqlDescribe(self, ctx:PLIParser.SqlDescribeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#sqlPrepare.
    def visitSqlPrepare(self, ctx:PLIParser.SqlPrepareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#forCommand.
    def visitForCommand(self, ctx:PLIParser.ForCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#sqlOpen.
    def visitSqlOpen(self, ctx:PLIParser.SqlOpenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#sqlClose.
    def visitSqlClose(self, ctx:PLIParser.SqlCloseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#sqlFetch.
    def visitSqlFetch(self, ctx:PLIParser.SqlFetchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#sqlUpdate.
    def visitSqlUpdate(self, ctx:PLIParser.SqlUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#sqlCommit.
    def visitSqlCommit(self, ctx:PLIParser.SqlCommitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#sqlInsert.
    def visitSqlInsert(self, ctx:PLIParser.SqlInsertContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#sqlDelete.
    def visitSqlDelete(self, ctx:PLIParser.SqlDeleteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#sqlWheneverCommand.
    def visitSqlWheneverCommand(self, ctx:PLIParser.SqlWheneverCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#sqlSelectCommand.
    def visitSqlSelectCommand(self, ctx:PLIParser.SqlSelectCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#sqlRollback.
    def visitSqlRollback(self, ctx:PLIParser.SqlRollbackContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#from.
    def visitFrom(self, ctx:PLIParser.FromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#where.
    def visitWhere(self, ctx:PLIParser.WhereContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#order.
    def visitOrder(self, ctx:PLIParser.OrderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#into.
    def visitInto(self, ctx:PLIParser.IntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#group.
    def visitGroup(self, ctx:PLIParser.GroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#having.
    def visitHaving(self, ctx:PLIParser.HavingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#from_list.
    def visitFrom_list(self, ctx:PLIParser.From_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#list.
    def visitList(self, ctx:PLIParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#alist.
    def visitAlist(self, ctx:PLIParser.AlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#assignList.
    def visitAssignList(self, ctx:PLIParser.AssignListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#sqlExpList.
    def visitSqlExpList(self, ctx:PLIParser.SqlExpListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#sqlExp.
    def visitSqlExp(self, ctx:PLIParser.SqlExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#sqlCondExp.
    def visitSqlCondExp(self, ctx:PLIParser.SqlCondExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#sqlCond.
    def visitSqlCond(self, ctx:PLIParser.SqlCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#sign.
    def visitSign(self, ctx:PLIParser.SignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#set.
    def visitSet(self, ctx:PLIParser.SetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#avarname.
    def visitAvarname(self, ctx:PLIParser.AvarnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#string.
    def visitString(self, ctx:PLIParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#exitstmt.
    def visitExitstmt(self, ctx:PLIParser.ExitstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#fetchstmt.
    def visitFetchstmt(self, ctx:PLIParser.FetchstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#fetchoptioncommalist.
    def visitFetchoptioncommalist(self, ctx:PLIParser.FetchoptioncommalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#fetchoption.
    def visitFetchoption(self, ctx:PLIParser.FetchoptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#flushstmt.
    def visitFlushstmt(self, ctx:PLIParser.FlushstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#formatstmt.
    def visitFormatstmt(self, ctx:PLIParser.FormatstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#freestmt.
    def visitFreestmt(self, ctx:PLIParser.FreestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#freeoption.
    def visitFreeoption(self, ctx:PLIParser.FreeoptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#getstmt.
    def visitGetstmt(self, ctx:PLIParser.GetstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#gotostmt.
    def visitGotostmt(self, ctx:PLIParser.GotostmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#iteratestmt.
    def visitIteratestmt(self, ctx:PLIParser.IteratestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#leavestmt.
    def visitLeavestmt(self, ctx:PLIParser.LeavestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#locatestmt.
    def visitLocatestmt(self, ctx:PLIParser.LocatestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#onstmt.
    def visitOnstmt(self, ctx:PLIParser.OnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#openstmt.
    def visitOpenstmt(self, ctx:PLIParser.OpenstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#packagestmt.
    def visitPackagestmt(self, ctx:PLIParser.PackagestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#packagegrouplist.
    def visitPackagegrouplist(self, ctx:PLIParser.PackagegrouplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#packagegroup.
    def visitPackagegroup(self, ctx:PLIParser.PackagegroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#packagevarnamecommalist.
    def visitPackagevarnamecommalist(self, ctx:PLIParser.PackagevarnamecommalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#packagevarname.
    def visitPackagevarname(self, ctx:PLIParser.PackagevarnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#packageoptionlist.
    def visitPackageoptionlist(self, ctx:PLIParser.PackageoptionlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#packageoption.
    def visitPackageoption(self, ctx:PLIParser.PackageoptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#putstmt.
    def visitPutstmt(self, ctx:PLIParser.PutstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#procedurestmt.
    def visitProcedurestmt(self, ctx:PLIParser.ProcedurestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#readstmt.
    def visitReadstmt(self, ctx:PLIParser.ReadstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#releasestmt.
    def visitReleasestmt(self, ctx:PLIParser.ReleasestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#resignalstmt.
    def visitResignalstmt(self, ctx:PLIParser.ResignalstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#returnstmt.
    def visitReturnstmt(self, ctx:PLIParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#rewritestmt.
    def visitRewritestmt(self, ctx:PLIParser.RewritestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#revertstmt.
    def visitRevertstmt(self, ctx:PLIParser.RevertstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#signalstmt.
    def visitSignalstmt(self, ctx:PLIParser.SignalstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#stopstmt.
    def visitStopstmt(self, ctx:PLIParser.StopstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#unlockstmt.
    def visitUnlockstmt(self, ctx:PLIParser.UnlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#waitstmt.
    def visitWaitstmt(self, ctx:PLIParser.WaitstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#writestmt.
    def visitWritestmt(self, ctx:PLIParser.WritestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#readoptionlist.
    def visitReadoptionlist(self, ctx:PLIParser.ReadoptionlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#rewriteoptionlist.
    def visitRewriteoptionlist(self, ctx:PLIParser.RewriteoptionlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#selectstmt.
    def visitSelectstmt(self, ctx:PLIParser.SelectstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#whenstmt.
    def visitWhenstmt(self, ctx:PLIParser.WhenstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#otherwisestmt.
    def visitOtherwisestmt(self, ctx:PLIParser.OtherwisestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#writeoptionlist.
    def visitWriteoptionlist(self, ctx:PLIParser.WriteoptionlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#deleteoptionlist.
    def visitDeleteoptionlist(self, ctx:PLIParser.DeleteoptionlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#unlockoptionlist.
    def visitUnlockoptionlist(self, ctx:PLIParser.UnlockoptionlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#locateoptionlist.
    def visitLocateoptionlist(self, ctx:PLIParser.LocateoptionlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#calloptionlist.
    def visitCalloptionlist(self, ctx:PLIParser.CalloptionlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#callmultitaskoptionlist.
    def visitCallmultitaskoptionlist(self, ctx:PLIParser.CallmultitaskoptionlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#callmultitaskoption.
    def visitCallmultitaskoption(self, ctx:PLIParser.CallmultitaskoptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#closegrouplist.
    def visitClosegrouplist(self, ctx:PLIParser.ClosegrouplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#defaultitemcommalist.
    def visitDefaultitemcommalist(self, ctx:PLIParser.DefaultitemcommalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#defaultitem.
    def visitDefaultitem(self, ctx:PLIParser.DefaultitemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#defaultrangespec.
    def visitDefaultrangespec(self, ctx:PLIParser.DefaultrangespecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#defaultpredicateexpr.
    def visitDefaultpredicateexpr(self, ctx:PLIParser.DefaultpredicateexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#procgrouplist.
    def visitProcgrouplist(self, ctx:PLIParser.ProcgrouplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#entrygrouplist.
    def visitEntrygrouplist(self, ctx:PLIParser.EntrygrouplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#formatgrouplist.
    def visitFormatgrouplist(self, ctx:PLIParser.FormatgrouplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#iooption.
    def visitIooption(self, ctx:PLIParser.IooptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#readoption.
    def visitReadoption(self, ctx:PLIParser.ReadoptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#writeoption.
    def visitWriteoption(self, ctx:PLIParser.WriteoptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#rewriteoption.
    def visitRewriteoption(self, ctx:PLIParser.RewriteoptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#deleteoption.
    def visitDeleteoption(self, ctx:PLIParser.DeleteoptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#unlockoption.
    def visitUnlockoption(self, ctx:PLIParser.UnlockoptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#locateoption.
    def visitLocateoption(self, ctx:PLIParser.LocateoptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#opengrouplist.
    def visitOpengrouplist(self, ctx:PLIParser.OpengrouplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#opengroup.
    def visitOpengroup(self, ctx:PLIParser.OpengroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#openoptionlist.
    def visitOpenoptionlist(self, ctx:PLIParser.OpenoptionlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#openoption.
    def visitOpenoption(self, ctx:PLIParser.OpenoptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#closegroup.
    def visitClosegroup(self, ctx:PLIParser.ClosegroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#putoptionlist.
    def visitPutoptionlist(self, ctx:PLIParser.PutoptionlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#putoption.
    def visitPutoption(self, ctx:PLIParser.PutoptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#entrygroup.
    def visitEntrygroup(self, ctx:PLIParser.EntrygroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#procgroup.
    def visitProcgroup(self, ctx:PLIParser.ProcgroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#procoptionlist.
    def visitProcoptionlist(self, ctx:PLIParser.ProcoptionlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#procoption.
    def visitProcoption(self, ctx:PLIParser.ProcoptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#renamepaircommalist.
    def visitRenamepaircommalist(self, ctx:PLIParser.RenamepaircommalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#renamepair.
    def visitRenamepair(self, ctx:PLIParser.RenamepairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#getoptionlist.
    def visitGetoptionlist(self, ctx:PLIParser.GetoptionlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#getoption.
    def visitGetoption(self, ctx:PLIParser.GetoptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#dataspecification.
    def visitDataspecification(self, ctx:PLIParser.DataspecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#listdataspec.
    def visitListdataspec(self, ctx:PLIParser.ListdataspecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#datadataspec.
    def visitDatadataspec(self, ctx:PLIParser.DatadataspecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#editdataspec.
    def visitEditdataspec(self, ctx:PLIParser.EditdataspecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#editformatexpr.
    def visitEditformatexpr(self, ctx:PLIParser.EditformatexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#realformatexpr.
    def visitRealformatexpr(self, ctx:PLIParser.RealformatexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#editformatitem.
    def visitEditformatitem(self, ctx:PLIParser.EditformatitemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#editformatlist.
    def visitEditformatlist(self, ctx:PLIParser.EditformatlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#datalist.
    def visitDatalist(self, ctx:PLIParser.DatalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#dostmt.
    def visitDostmt(self, ctx:PLIParser.DostmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#do_type_1.
    def visitDo_type_1(self, ctx:PLIParser.Do_type_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#do_type_2.
    def visitDo_type_2(self, ctx:PLIParser.Do_type_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#do_spec_2.
    def visitDo_spec_2(self, ctx:PLIParser.Do_spec_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#do_type_3.
    def visitDo_type_3(self, ctx:PLIParser.Do_type_3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#do_spec_3list.
    def visitDo_spec_3list(self, ctx:PLIParser.Do_spec_3listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#do_spec_3.
    def visitDo_spec_3(self, ctx:PLIParser.Do_spec_3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#do_spec_3_exprlist.
    def visitDo_spec_3_exprlist(self, ctx:PLIParser.Do_spec_3_exprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#do_spec_3_expr.
    def visitDo_spec_3_expr(self, ctx:PLIParser.Do_spec_3_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#ifstmt.
    def visitIfstmt(self, ctx:PLIParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#ifprestmt.
    def visitIfprestmt(self, ctx:PLIParser.IfprestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#assignstmt.
    def visitAssignstmt(self, ctx:PLIParser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#expr.
    def visitExpr(self, ctx:PLIParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#exprbase.
    def visitExprbase(self, ctx:PLIParser.ExprbaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#exprnested.
    def visitExprnested(self, ctx:PLIParser.ExprnestedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#exprconst.
    def visitExprconst(self, ctx:PLIParser.ExprconstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#exprstrconst.
    def visitExprstrconst(self, ctx:PLIParser.ExprstrconstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#exprnumconst.
    def visitExprnumconst(self, ctx:PLIParser.ExprnumconstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#varnamerefcommalist.
    def visitVarnamerefcommalist(self, ctx:PLIParser.VarnamerefcommalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#varnameref.
    def visitVarnameref(self, ctx:PLIParser.VarnamerefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#varnamequal.
    def visitVarnamequal(self, ctx:PLIParser.VarnamequalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#varnamedimensioncommalist.
    def visitVarnamedimensioncommalist(self, ctx:PLIParser.VarnamedimensioncommalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#varnamedimension.
    def visitVarnamedimension(self, ctx:PLIParser.VarnamedimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#varnamecommalist.
    def visitVarnamecommalist(self, ctx:PLIParser.VarnamecommalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#varname.
    def visitVarname(self, ctx:PLIParser.VarnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#varname_kw.
    def visitVarname_kw(self, ctx:PLIParser.Varname_kwContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#varname_kwpp.
    def visitVarname_kwpp(self, ctx:PLIParser.Varname_kwppContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#varname_conditions.
    def visitVarname_conditions(self, ctx:PLIParser.Varname_conditionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#onconditioncommalist.
    def visitOnconditioncommalist(self, ctx:PLIParser.OnconditioncommalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#oncondition.
    def visitOncondition(self, ctx:PLIParser.OnconditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#precondition.
    def visitPrecondition(self, ctx:PLIParser.PreconditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#dclstmt.
    def visitDclstmt(self, ctx:PLIParser.DclstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#dcltermcommalist.
    def visitDcltermcommalist(self, ctx:PLIParser.DcltermcommalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#dclterm.
    def visitDclterm(self, ctx:PLIParser.DcltermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#dclnamebase.
    def visitDclnamebase(self, ctx:PLIParser.DclnamebaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#dclfactor.
    def visitDclfactor(self, ctx:PLIParser.DclfactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#dclarrayboundcommalist.
    def visitDclarrayboundcommalist(self, ctx:PLIParser.DclarrayboundcommalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#dclarraybound.
    def visitDclarraybound(self, ctx:PLIParser.DclarrayboundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#dcloptionlist.
    def visitDcloptionlist(self, ctx:PLIParser.DcloptionlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#dcloption.
    def visitDcloption(self, ctx:PLIParser.DcloptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#dclnumeric.
    def visitDclnumeric(self, ctx:PLIParser.DclnumericContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#dclnumericNUM.
    def visitDclnumericNUM(self, ctx:PLIParser.DclnumericNUMContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#dclio.
    def visitDclio(self, ctx:PLIParser.DclioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#dclchar.
    def visitDclchar(self, ctx:PLIParser.DclcharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#dclstg.
    def visitDclstg(self, ctx:PLIParser.DclstgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#dclpgm.
    def visitDclpgm(self, ctx:PLIParser.DclpgmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#dclmisc.
    def visitDclmisc(self, ctx:PLIParser.DclmiscContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#environmentspeclist.
    def visitEnvironmentspeclist(self, ctx:PLIParser.EnvironmentspeclistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#environmentspec.
    def visitEnvironmentspec(self, ctx:PLIParser.EnvironmentspecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#environmentspecparm.
    def visitEnvironmentspecparm(self, ctx:PLIParser.EnvironmentspecparmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#entryparmcommalist.
    def visitEntryparmcommalist(self, ctx:PLIParser.EntryparmcommalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#entryparm.
    def visitEntryparm(self, ctx:PLIParser.EntryparmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#entryarrayspec.
    def visitEntryarrayspec(self, ctx:PLIParser.EntryarrayspecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#entryarrayspeccommalist.
    def visitEntryarrayspeccommalist(self, ctx:PLIParser.EntryarrayspeccommalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#entryoptionlist.
    def visitEntryoptionlist(self, ctx:PLIParser.EntryoptionlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#entryoption.
    def visitEntryoption(self, ctx:PLIParser.EntryoptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#genericspeccommalist.
    def visitGenericspeccommalist(self, ctx:PLIParser.GenericspeccommalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#genericspec.
    def visitGenericspec(self, ctx:PLIParser.GenericspecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#genericwhenoptionlist.
    def visitGenericwhenoptionlist(self, ctx:PLIParser.GenericwhenoptionlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#genericwhenoption.
    def visitGenericwhenoption(self, ctx:PLIParser.GenericwhenoptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#charspec.
    def visitCharspec(self, ctx:PLIParser.CharspecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#dclinit.
    def visitDclinit(self, ctx:PLIParser.DclinitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#initialtospec.
    def visitInitialtospec(self, ctx:PLIParser.InitialtospecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#inititemcommalist.
    def visitInititemcommalist(self, ctx:PLIParser.InititemcommalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#inititem.
    def visitInititem(self, ctx:PLIParser.InititemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLIParser#inititerationfactorlist.
    def visitInititerationfactorlist(self, ctx:PLIParser.InititerationfactorlistContext):
        return self.visitChildren(ctx)



del PLIParser