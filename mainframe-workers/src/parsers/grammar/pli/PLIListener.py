# Generated from ./src/parsers/grammar/pli/PLI.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PLIParser import PLIParser
else:
    from PLIParser import PLIParser

# This class defines a complete listener for a parse tree produced by PLIParser.
class PLIListener(ParseTreeListener):

    # Enter a parse tree produced by PLIParser#startRule.
    def enterStartRule(self, ctx:PLIParser.StartRuleContext):
        pass

    # Exit a parse tree produced by PLIParser#startRule.
    def exitStartRule(self, ctx:PLIParser.StartRuleContext):
        pass


    # Enter a parse tree produced by PLIParser#firstline.
    def enterFirstline(self, ctx:PLIParser.FirstlineContext):
        pass

    # Exit a parse tree produced by PLIParser#firstline.
    def exitFirstline(self, ctx:PLIParser.FirstlineContext):
        pass


    # Enter a parse tree produced by PLIParser#procedureBlock.
    def enterProcedureBlock(self, ctx:PLIParser.ProcedureBlockContext):
        pass

    # Exit a parse tree produced by PLIParser#procedureBlock.
    def exitProcedureBlock(self, ctx:PLIParser.ProcedureBlockContext):
        pass


    # Enter a parse tree produced by PLIParser#inlineBlock.
    def enterInlineBlock(self, ctx:PLIParser.InlineBlockContext):
        pass

    # Exit a parse tree produced by PLIParser#inlineBlock.
    def exitInlineBlock(self, ctx:PLIParser.InlineBlockContext):
        pass


    # Enter a parse tree produced by PLIParser#procedureContent.
    def enterProcedureContent(self, ctx:PLIParser.ProcedureContentContext):
        pass

    # Exit a parse tree produced by PLIParser#procedureContent.
    def exitProcedureContent(self, ctx:PLIParser.ProcedureContentContext):
        pass


    # Enter a parse tree produced by PLIParser#pl1stmtlist.
    def enterPl1stmtlist(self, ctx:PLIParser.Pl1stmtlistContext):
        pass

    # Exit a parse tree produced by PLIParser#pl1stmtlist.
    def exitPl1stmtlist(self, ctx:PLIParser.Pl1stmtlistContext):
        pass


    # Enter a parse tree produced by PLIParser#preconditioncommalist.
    def enterPreconditioncommalist(self, ctx:PLIParser.PreconditioncommalistContext):
        pass

    # Exit a parse tree produced by PLIParser#preconditioncommalist.
    def exitPreconditioncommalist(self, ctx:PLIParser.PreconditioncommalistContext):
        pass


    # Enter a parse tree produced by PLIParser#prestmtlist.
    def enterPrestmtlist(self, ctx:PLIParser.PrestmtlistContext):
        pass

    # Exit a parse tree produced by PLIParser#prestmtlist.
    def exitPrestmtlist(self, ctx:PLIParser.PrestmtlistContext):
        pass


    # Enter a parse tree produced by PLIParser#pl1stmt.
    def enterPl1stmt(self, ctx:PLIParser.Pl1stmtContext):
        pass

    # Exit a parse tree produced by PLIParser#pl1stmt.
    def exitPl1stmt(self, ctx:PLIParser.Pl1stmtContext):
        pass


    # Enter a parse tree produced by PLIParser#otherBlock.
    def enterOtherBlock(self, ctx:PLIParser.OtherBlockContext):
        pass

    # Exit a parse tree produced by PLIParser#otherBlock.
    def exitOtherBlock(self, ctx:PLIParser.OtherBlockContext):
        pass


    # Enter a parse tree produced by PLIParser#onBlock.
    def enterOnBlock(self, ctx:PLIParser.OnBlockContext):
        pass

    # Exit a parse tree produced by PLIParser#onBlock.
    def exitOnBlock(self, ctx:PLIParser.OnBlockContext):
        pass


    # Enter a parse tree produced by PLIParser#doBlock.
    def enterDoBlock(self, ctx:PLIParser.DoBlockContext):
        pass

    # Exit a parse tree produced by PLIParser#doBlock.
    def exitDoBlock(self, ctx:PLIParser.DoBlockContext):
        pass


    # Enter a parse tree produced by PLIParser#doContent.
    def enterDoContent(self, ctx:PLIParser.DoContentContext):
        pass

    # Exit a parse tree produced by PLIParser#doContent.
    def exitDoContent(self, ctx:PLIParser.DoContentContext):
        pass


    # Enter a parse tree produced by PLIParser#selectBlock.
    def enterSelectBlock(self, ctx:PLIParser.SelectBlockContext):
        pass

    # Exit a parse tree produced by PLIParser#selectBlock.
    def exitSelectBlock(self, ctx:PLIParser.SelectBlockContext):
        pass


    # Enter a parse tree produced by PLIParser#ifBlock.
    def enterIfBlock(self, ctx:PLIParser.IfBlockContext):
        pass

    # Exit a parse tree produced by PLIParser#ifBlock.
    def exitIfBlock(self, ctx:PLIParser.IfBlockContext):
        pass


    # Enter a parse tree produced by PLIParser#stmtscopeend.
    def enterStmtscopeend(self, ctx:PLIParser.StmtscopeendContext):
        pass

    # Exit a parse tree produced by PLIParser#stmtscopeend.
    def exitStmtscopeend(self, ctx:PLIParser.StmtscopeendContext):
        pass


    # Enter a parse tree produced by PLIParser#stmtscope.
    def enterStmtscope(self, ctx:PLIParser.StmtscopeContext):
        pass

    # Exit a parse tree produced by PLIParser#stmtscope.
    def exitStmtscope(self, ctx:PLIParser.StmtscopeContext):
        pass


    # Enter a parse tree produced by PLIParser#stmt.
    def enterStmt(self, ctx:PLIParser.StmtContext):
        pass

    # Exit a parse tree produced by PLIParser#stmt.
    def exitStmt(self, ctx:PLIParser.StmtContext):
        pass


    # Enter a parse tree produced by PLIParser#includestmt.
    def enterIncludestmt(self, ctx:PLIParser.IncludestmtContext):
        pass

    # Exit a parse tree produced by PLIParser#includestmt.
    def exitIncludestmt(self, ctx:PLIParser.IncludestmtContext):
        pass


    # Enter a parse tree produced by PLIParser#filename.
    def enterFilename(self, ctx:PLIParser.FilenameContext):
        pass

    # Exit a parse tree produced by PLIParser#filename.
    def exitFilename(self, ctx:PLIParser.FilenameContext):
        pass


    # Enter a parse tree produced by PLIParser#allocatestmt.
    def enterAllocatestmt(self, ctx:PLIParser.AllocatestmtContext):
        pass

    # Exit a parse tree produced by PLIParser#allocatestmt.
    def exitAllocatestmt(self, ctx:PLIParser.AllocatestmtContext):
        pass


    # Enter a parse tree produced by PLIParser#allocateoptionlist.
    def enterAllocateoptionlist(self, ctx:PLIParser.AllocateoptionlistContext):
        pass

    # Exit a parse tree produced by PLIParser#allocateoptionlist.
    def exitAllocateoptionlist(self, ctx:PLIParser.AllocateoptionlistContext):
        pass


    # Enter a parse tree produced by PLIParser#allocateoption.
    def enterAllocateoption(self, ctx:PLIParser.AllocateoptionContext):
        pass

    # Exit a parse tree produced by PLIParser#allocateoption.
    def exitAllocateoption(self, ctx:PLIParser.AllocateoptionContext):
        pass


    # Enter a parse tree produced by PLIParser#attachstmt.
    def enterAttachstmt(self, ctx:PLIParser.AttachstmtContext):
        pass

    # Exit a parse tree produced by PLIParser#attachstmt.
    def exitAttachstmt(self, ctx:PLIParser.AttachstmtContext):
        pass


    # Enter a parse tree produced by PLIParser#ctloptionlist.
    def enterCtloptionlist(self, ctx:PLIParser.CtloptionlistContext):
        pass

    # Exit a parse tree produced by PLIParser#ctloptionlist.
    def exitCtloptionlist(self, ctx:PLIParser.CtloptionlistContext):
        pass


    # Enter a parse tree produced by PLIParser#ctlvarattribute.
    def enterCtlvarattribute(self, ctx:PLIParser.CtlvarattributeContext):
        pass

    # Exit a parse tree produced by PLIParser#ctlvarattribute.
    def exitCtlvarattribute(self, ctx:PLIParser.CtlvarattributeContext):
        pass


    # Enter a parse tree produced by PLIParser#beginstmt.
    def enterBeginstmt(self, ctx:PLIParser.BeginstmtContext):
        pass

    # Exit a parse tree produced by PLIParser#beginstmt.
    def exitBeginstmt(self, ctx:PLIParser.BeginstmtContext):
        pass


    # Enter a parse tree produced by PLIParser#beginstmtoptionlist.
    def enterBeginstmtoptionlist(self, ctx:PLIParser.BeginstmtoptionlistContext):
        pass

    # Exit a parse tree produced by PLIParser#beginstmtoptionlist.
    def exitBeginstmtoptionlist(self, ctx:PLIParser.BeginstmtoptionlistContext):
        pass


    # Enter a parse tree produced by PLIParser#beginstmtoption.
    def enterBeginstmtoption(self, ctx:PLIParser.BeginstmtoptionContext):
        pass

    # Exit a parse tree produced by PLIParser#beginstmtoption.
    def exitBeginstmtoption(self, ctx:PLIParser.BeginstmtoptionContext):
        pass


    # Enter a parse tree produced by PLIParser#delaystmt.
    def enterDelaystmt(self, ctx:PLIParser.DelaystmtContext):
        pass

    # Exit a parse tree produced by PLIParser#delaystmt.
    def exitDelaystmt(self, ctx:PLIParser.DelaystmtContext):
        pass


    # Enter a parse tree produced by PLIParser#callstmt.
    def enterCallstmt(self, ctx:PLIParser.CallstmtContext):
        pass

    # Exit a parse tree produced by PLIParser#callstmt.
    def exitCallstmt(self, ctx:PLIParser.CallstmtContext):
        pass


    # Enter a parse tree produced by PLIParser#inlinestmt.
    def enterInlinestmt(self, ctx:PLIParser.InlinestmtContext):
        pass

    # Exit a parse tree produced by PLIParser#inlinestmt.
    def exitInlinestmt(self, ctx:PLIParser.InlinestmtContext):
        pass


    # Enter a parse tree produced by PLIParser#closestmt.
    def enterClosestmt(self, ctx:PLIParser.ClosestmtContext):
        pass

    # Exit a parse tree produced by PLIParser#closestmt.
    def exitClosestmt(self, ctx:PLIParser.ClosestmtContext):
        pass


    # Enter a parse tree produced by PLIParser#defaultstmt.
    def enterDefaultstmt(self, ctx:PLIParser.DefaultstmtContext):
        pass

    # Exit a parse tree produced by PLIParser#defaultstmt.
    def exitDefaultstmt(self, ctx:PLIParser.DefaultstmtContext):
        pass


    # Enter a parse tree produced by PLIParser#definealiasstmt.
    def enterDefinealiasstmt(self, ctx:PLIParser.DefinealiasstmtContext):
        pass

    # Exit a parse tree produced by PLIParser#definealiasstmt.
    def exitDefinealiasstmt(self, ctx:PLIParser.DefinealiasstmtContext):
        pass


    # Enter a parse tree produced by PLIParser#defineordinalstmt.
    def enterDefineordinalstmt(self, ctx:PLIParser.DefineordinalstmtContext):
        pass

    # Exit a parse tree produced by PLIParser#defineordinalstmt.
    def exitDefineordinalstmt(self, ctx:PLIParser.DefineordinalstmtContext):
        pass


    # Enter a parse tree produced by PLIParser#definestructurestmt.
    def enterDefinestructurestmt(self, ctx:PLIParser.DefinestructurestmtContext):
        pass

    # Exit a parse tree produced by PLIParser#definestructurestmt.
    def exitDefinestructurestmt(self, ctx:PLIParser.DefinestructurestmtContext):
        pass


    # Enter a parse tree produced by PLIParser#dclstructurecommalist.
    def enterDclstructurecommalist(self, ctx:PLIParser.DclstructurecommalistContext):
        pass

    # Exit a parse tree produced by PLIParser#dclstructurecommalist.
    def exitDclstructurecommalist(self, ctx:PLIParser.DclstructurecommalistContext):
        pass


    # Enter a parse tree produced by PLIParser#dclstructure.
    def enterDclstructure(self, ctx:PLIParser.DclstructureContext):
        pass

    # Exit a parse tree produced by PLIParser#dclstructure.
    def exitDclstructure(self, ctx:PLIParser.DclstructureContext):
        pass


    # Enter a parse tree produced by PLIParser#ordinalmembercommalist.
    def enterOrdinalmembercommalist(self, ctx:PLIParser.OrdinalmembercommalistContext):
        pass

    # Exit a parse tree produced by PLIParser#ordinalmembercommalist.
    def exitOrdinalmembercommalist(self, ctx:PLIParser.OrdinalmembercommalistContext):
        pass


    # Enter a parse tree produced by PLIParser#ordinalmember.
    def enterOrdinalmember(self, ctx:PLIParser.OrdinalmemberContext):
        pass

    # Exit a parse tree produced by PLIParser#ordinalmember.
    def exitOrdinalmember(self, ctx:PLIParser.OrdinalmemberContext):
        pass


    # Enter a parse tree produced by PLIParser#ordinaloptionlist.
    def enterOrdinaloptionlist(self, ctx:PLIParser.OrdinaloptionlistContext):
        pass

    # Exit a parse tree produced by PLIParser#ordinaloptionlist.
    def exitOrdinaloptionlist(self, ctx:PLIParser.OrdinaloptionlistContext):
        pass


    # Enter a parse tree produced by PLIParser#ordinaloption.
    def enterOrdinaloption(self, ctx:PLIParser.OrdinaloptionContext):
        pass

    # Exit a parse tree produced by PLIParser#ordinaloption.
    def exitOrdinaloption(self, ctx:PLIParser.OrdinaloptionContext):
        pass


    # Enter a parse tree produced by PLIParser#displaystmt.
    def enterDisplaystmt(self, ctx:PLIParser.DisplaystmtContext):
        pass

    # Exit a parse tree produced by PLIParser#displaystmt.
    def exitDisplaystmt(self, ctx:PLIParser.DisplaystmtContext):
        pass


    # Enter a parse tree produced by PLIParser#deletestmt.
    def enterDeletestmt(self, ctx:PLIParser.DeletestmtContext):
        pass

    # Exit a parse tree produced by PLIParser#deletestmt.
    def exitDeletestmt(self, ctx:PLIParser.DeletestmtContext):
        pass


    # Enter a parse tree produced by PLIParser#detachstmt.
    def enterDetachstmt(self, ctx:PLIParser.DetachstmtContext):
        pass

    # Exit a parse tree produced by PLIParser#detachstmt.
    def exitDetachstmt(self, ctx:PLIParser.DetachstmtContext):
        pass


    # Enter a parse tree produced by PLIParser#endstmt.
    def enterEndstmt(self, ctx:PLIParser.EndstmtContext):
        pass

    # Exit a parse tree produced by PLIParser#endstmt.
    def exitEndstmt(self, ctx:PLIParser.EndstmtContext):
        pass


    # Enter a parse tree produced by PLIParser#entrystmt.
    def enterEntrystmt(self, ctx:PLIParser.EntrystmtContext):
        pass

    # Exit a parse tree produced by PLIParser#entrystmt.
    def exitEntrystmt(self, ctx:PLIParser.EntrystmtContext):
        pass


    # Enter a parse tree produced by PLIParser#execstmt.
    def enterExecstmt(self, ctx:PLIParser.ExecstmtContext):
        pass

    # Exit a parse tree produced by PLIParser#execstmt.
    def exitExecstmt(self, ctx:PLIParser.ExecstmtContext):
        pass


    # Enter a parse tree produced by PLIParser#sqlstmt.
    def enterSqlstmt(self, ctx:PLIParser.SqlstmtContext):
        pass

    # Exit a parse tree produced by PLIParser#sqlstmt.
    def exitSqlstmt(self, ctx:PLIParser.SqlstmtContext):
        pass


    # Enter a parse tree produced by PLIParser#cicsstmt.
    def enterCicsstmt(self, ctx:PLIParser.CicsstmtContext):
        pass

    # Exit a parse tree produced by PLIParser#cicsstmt.
    def exitCicsstmt(self, ctx:PLIParser.CicsstmtContext):
        pass


    # Enter a parse tree produced by PLIParser#command.
    def enterCommand(self, ctx:PLIParser.CommandContext):
        pass

    # Exit a parse tree produced by PLIParser#command.
    def exitCommand(self, ctx:PLIParser.CommandContext):
        pass


    # Enter a parse tree produced by PLIParser#field.
    def enterField(self, ctx:PLIParser.FieldContext):
        pass

    # Exit a parse tree produced by PLIParser#field.
    def exitField(self, ctx:PLIParser.FieldContext):
        pass


    # Enter a parse tree produced by PLIParser#declare.
    def enterDeclare(self, ctx:PLIParser.DeclareContext):
        pass

    # Exit a parse tree produced by PLIParser#declare.
    def exitDeclare(self, ctx:PLIParser.DeclareContext):
        pass


    # Enter a parse tree produced by PLIParser#execInclude.
    def enterExecInclude(self, ctx:PLIParser.ExecIncludeContext):
        pass

    # Exit a parse tree produced by PLIParser#execInclude.
    def exitExecInclude(self, ctx:PLIParser.ExecIncludeContext):
        pass


    # Enter a parse tree produced by PLIParser#sqlCommand.
    def enterSqlCommand(self, ctx:PLIParser.SqlCommandContext):
        pass

    # Exit a parse tree produced by PLIParser#sqlCommand.
    def exitSqlCommand(self, ctx:PLIParser.SqlCommandContext):
        pass


    # Enter a parse tree produced by PLIParser#sqlDescribe.
    def enterSqlDescribe(self, ctx:PLIParser.SqlDescribeContext):
        pass

    # Exit a parse tree produced by PLIParser#sqlDescribe.
    def exitSqlDescribe(self, ctx:PLIParser.SqlDescribeContext):
        pass


    # Enter a parse tree produced by PLIParser#sqlPrepare.
    def enterSqlPrepare(self, ctx:PLIParser.SqlPrepareContext):
        pass

    # Exit a parse tree produced by PLIParser#sqlPrepare.
    def exitSqlPrepare(self, ctx:PLIParser.SqlPrepareContext):
        pass


    # Enter a parse tree produced by PLIParser#forCommand.
    def enterForCommand(self, ctx:PLIParser.ForCommandContext):
        pass

    # Exit a parse tree produced by PLIParser#forCommand.
    def exitForCommand(self, ctx:PLIParser.ForCommandContext):
        pass


    # Enter a parse tree produced by PLIParser#sqlOpen.
    def enterSqlOpen(self, ctx:PLIParser.SqlOpenContext):
        pass

    # Exit a parse tree produced by PLIParser#sqlOpen.
    def exitSqlOpen(self, ctx:PLIParser.SqlOpenContext):
        pass


    # Enter a parse tree produced by PLIParser#sqlClose.
    def enterSqlClose(self, ctx:PLIParser.SqlCloseContext):
        pass

    # Exit a parse tree produced by PLIParser#sqlClose.
    def exitSqlClose(self, ctx:PLIParser.SqlCloseContext):
        pass


    # Enter a parse tree produced by PLIParser#sqlFetch.
    def enterSqlFetch(self, ctx:PLIParser.SqlFetchContext):
        pass

    # Exit a parse tree produced by PLIParser#sqlFetch.
    def exitSqlFetch(self, ctx:PLIParser.SqlFetchContext):
        pass


    # Enter a parse tree produced by PLIParser#sqlUpdate.
    def enterSqlUpdate(self, ctx:PLIParser.SqlUpdateContext):
        pass

    # Exit a parse tree produced by PLIParser#sqlUpdate.
    def exitSqlUpdate(self, ctx:PLIParser.SqlUpdateContext):
        pass


    # Enter a parse tree produced by PLIParser#sqlCommit.
    def enterSqlCommit(self, ctx:PLIParser.SqlCommitContext):
        pass

    # Exit a parse tree produced by PLIParser#sqlCommit.
    def exitSqlCommit(self, ctx:PLIParser.SqlCommitContext):
        pass


    # Enter a parse tree produced by PLIParser#sqlInsert.
    def enterSqlInsert(self, ctx:PLIParser.SqlInsertContext):
        pass

    # Exit a parse tree produced by PLIParser#sqlInsert.
    def exitSqlInsert(self, ctx:PLIParser.SqlInsertContext):
        pass


    # Enter a parse tree produced by PLIParser#sqlDelete.
    def enterSqlDelete(self, ctx:PLIParser.SqlDeleteContext):
        pass

    # Exit a parse tree produced by PLIParser#sqlDelete.
    def exitSqlDelete(self, ctx:PLIParser.SqlDeleteContext):
        pass


    # Enter a parse tree produced by PLIParser#sqlWheneverCommand.
    def enterSqlWheneverCommand(self, ctx:PLIParser.SqlWheneverCommandContext):
        pass

    # Exit a parse tree produced by PLIParser#sqlWheneverCommand.
    def exitSqlWheneverCommand(self, ctx:PLIParser.SqlWheneverCommandContext):
        pass


    # Enter a parse tree produced by PLIParser#sqlSelectCommand.
    def enterSqlSelectCommand(self, ctx:PLIParser.SqlSelectCommandContext):
        pass

    # Exit a parse tree produced by PLIParser#sqlSelectCommand.
    def exitSqlSelectCommand(self, ctx:PLIParser.SqlSelectCommandContext):
        pass


    # Enter a parse tree produced by PLIParser#sqlRollback.
    def enterSqlRollback(self, ctx:PLIParser.SqlRollbackContext):
        pass

    # Exit a parse tree produced by PLIParser#sqlRollback.
    def exitSqlRollback(self, ctx:PLIParser.SqlRollbackContext):
        pass


    # Enter a parse tree produced by PLIParser#from.
    def enterFrom(self, ctx:PLIParser.FromContext):
        pass

    # Exit a parse tree produced by PLIParser#from.
    def exitFrom(self, ctx:PLIParser.FromContext):
        pass


    # Enter a parse tree produced by PLIParser#where.
    def enterWhere(self, ctx:PLIParser.WhereContext):
        pass

    # Exit a parse tree produced by PLIParser#where.
    def exitWhere(self, ctx:PLIParser.WhereContext):
        pass


    # Enter a parse tree produced by PLIParser#order.
    def enterOrder(self, ctx:PLIParser.OrderContext):
        pass

    # Exit a parse tree produced by PLIParser#order.
    def exitOrder(self, ctx:PLIParser.OrderContext):
        pass


    # Enter a parse tree produced by PLIParser#into.
    def enterInto(self, ctx:PLIParser.IntoContext):
        pass

    # Exit a parse tree produced by PLIParser#into.
    def exitInto(self, ctx:PLIParser.IntoContext):
        pass


    # Enter a parse tree produced by PLIParser#group.
    def enterGroup(self, ctx:PLIParser.GroupContext):
        pass

    # Exit a parse tree produced by PLIParser#group.
    def exitGroup(self, ctx:PLIParser.GroupContext):
        pass


    # Enter a parse tree produced by PLIParser#having.
    def enterHaving(self, ctx:PLIParser.HavingContext):
        pass

    # Exit a parse tree produced by PLIParser#having.
    def exitHaving(self, ctx:PLIParser.HavingContext):
        pass


    # Enter a parse tree produced by PLIParser#from_list.
    def enterFrom_list(self, ctx:PLIParser.From_listContext):
        pass

    # Exit a parse tree produced by PLIParser#from_list.
    def exitFrom_list(self, ctx:PLIParser.From_listContext):
        pass


    # Enter a parse tree produced by PLIParser#list.
    def enterList(self, ctx:PLIParser.ListContext):
        pass

    # Exit a parse tree produced by PLIParser#list.
    def exitList(self, ctx:PLIParser.ListContext):
        pass


    # Enter a parse tree produced by PLIParser#alist.
    def enterAlist(self, ctx:PLIParser.AlistContext):
        pass

    # Exit a parse tree produced by PLIParser#alist.
    def exitAlist(self, ctx:PLIParser.AlistContext):
        pass


    # Enter a parse tree produced by PLIParser#assignList.
    def enterAssignList(self, ctx:PLIParser.AssignListContext):
        pass

    # Exit a parse tree produced by PLIParser#assignList.
    def exitAssignList(self, ctx:PLIParser.AssignListContext):
        pass


    # Enter a parse tree produced by PLIParser#sqlExpList.
    def enterSqlExpList(self, ctx:PLIParser.SqlExpListContext):
        pass

    # Exit a parse tree produced by PLIParser#sqlExpList.
    def exitSqlExpList(self, ctx:PLIParser.SqlExpListContext):
        pass


    # Enter a parse tree produced by PLIParser#sqlExp.
    def enterSqlExp(self, ctx:PLIParser.SqlExpContext):
        pass

    # Exit a parse tree produced by PLIParser#sqlExp.
    def exitSqlExp(self, ctx:PLIParser.SqlExpContext):
        pass


    # Enter a parse tree produced by PLIParser#sqlCondExp.
    def enterSqlCondExp(self, ctx:PLIParser.SqlCondExpContext):
        pass

    # Exit a parse tree produced by PLIParser#sqlCondExp.
    def exitSqlCondExp(self, ctx:PLIParser.SqlCondExpContext):
        pass


    # Enter a parse tree produced by PLIParser#sqlCond.
    def enterSqlCond(self, ctx:PLIParser.SqlCondContext):
        pass

    # Exit a parse tree produced by PLIParser#sqlCond.
    def exitSqlCond(self, ctx:PLIParser.SqlCondContext):
        pass


    # Enter a parse tree produced by PLIParser#sign.
    def enterSign(self, ctx:PLIParser.SignContext):
        pass

    # Exit a parse tree produced by PLIParser#sign.
    def exitSign(self, ctx:PLIParser.SignContext):
        pass


    # Enter a parse tree produced by PLIParser#set.
    def enterSet(self, ctx:PLIParser.SetContext):
        pass

    # Exit a parse tree produced by PLIParser#set.
    def exitSet(self, ctx:PLIParser.SetContext):
        pass


    # Enter a parse tree produced by PLIParser#avarname.
    def enterAvarname(self, ctx:PLIParser.AvarnameContext):
        pass

    # Exit a parse tree produced by PLIParser#avarname.
    def exitAvarname(self, ctx:PLIParser.AvarnameContext):
        pass


    # Enter a parse tree produced by PLIParser#string.
    def enterString(self, ctx:PLIParser.StringContext):
        pass

    # Exit a parse tree produced by PLIParser#string.
    def exitString(self, ctx:PLIParser.StringContext):
        pass


    # Enter a parse tree produced by PLIParser#exitstmt.
    def enterExitstmt(self, ctx:PLIParser.ExitstmtContext):
        pass

    # Exit a parse tree produced by PLIParser#exitstmt.
    def exitExitstmt(self, ctx:PLIParser.ExitstmtContext):
        pass


    # Enter a parse tree produced by PLIParser#fetchstmt.
    def enterFetchstmt(self, ctx:PLIParser.FetchstmtContext):
        pass

    # Exit a parse tree produced by PLIParser#fetchstmt.
    def exitFetchstmt(self, ctx:PLIParser.FetchstmtContext):
        pass


    # Enter a parse tree produced by PLIParser#fetchoptioncommalist.
    def enterFetchoptioncommalist(self, ctx:PLIParser.FetchoptioncommalistContext):
        pass

    # Exit a parse tree produced by PLIParser#fetchoptioncommalist.
    def exitFetchoptioncommalist(self, ctx:PLIParser.FetchoptioncommalistContext):
        pass


    # Enter a parse tree produced by PLIParser#fetchoption.
    def enterFetchoption(self, ctx:PLIParser.FetchoptionContext):
        pass

    # Exit a parse tree produced by PLIParser#fetchoption.
    def exitFetchoption(self, ctx:PLIParser.FetchoptionContext):
        pass


    # Enter a parse tree produced by PLIParser#flushstmt.
    def enterFlushstmt(self, ctx:PLIParser.FlushstmtContext):
        pass

    # Exit a parse tree produced by PLIParser#flushstmt.
    def exitFlushstmt(self, ctx:PLIParser.FlushstmtContext):
        pass


    # Enter a parse tree produced by PLIParser#formatstmt.
    def enterFormatstmt(self, ctx:PLIParser.FormatstmtContext):
        pass

    # Exit a parse tree produced by PLIParser#formatstmt.
    def exitFormatstmt(self, ctx:PLIParser.FormatstmtContext):
        pass


    # Enter a parse tree produced by PLIParser#freestmt.
    def enterFreestmt(self, ctx:PLIParser.FreestmtContext):
        pass

    # Exit a parse tree produced by PLIParser#freestmt.
    def exitFreestmt(self, ctx:PLIParser.FreestmtContext):
        pass


    # Enter a parse tree produced by PLIParser#freeoption.
    def enterFreeoption(self, ctx:PLIParser.FreeoptionContext):
        pass

    # Exit a parse tree produced by PLIParser#freeoption.
    def exitFreeoption(self, ctx:PLIParser.FreeoptionContext):
        pass


    # Enter a parse tree produced by PLIParser#getstmt.
    def enterGetstmt(self, ctx:PLIParser.GetstmtContext):
        pass

    # Exit a parse tree produced by PLIParser#getstmt.
    def exitGetstmt(self, ctx:PLIParser.GetstmtContext):
        pass


    # Enter a parse tree produced by PLIParser#gotostmt.
    def enterGotostmt(self, ctx:PLIParser.GotostmtContext):
        pass

    # Exit a parse tree produced by PLIParser#gotostmt.
    def exitGotostmt(self, ctx:PLIParser.GotostmtContext):
        pass


    # Enter a parse tree produced by PLIParser#iteratestmt.
    def enterIteratestmt(self, ctx:PLIParser.IteratestmtContext):
        pass

    # Exit a parse tree produced by PLIParser#iteratestmt.
    def exitIteratestmt(self, ctx:PLIParser.IteratestmtContext):
        pass


    # Enter a parse tree produced by PLIParser#leavestmt.
    def enterLeavestmt(self, ctx:PLIParser.LeavestmtContext):
        pass

    # Exit a parse tree produced by PLIParser#leavestmt.
    def exitLeavestmt(self, ctx:PLIParser.LeavestmtContext):
        pass


    # Enter a parse tree produced by PLIParser#locatestmt.
    def enterLocatestmt(self, ctx:PLIParser.LocatestmtContext):
        pass

    # Exit a parse tree produced by PLIParser#locatestmt.
    def exitLocatestmt(self, ctx:PLIParser.LocatestmtContext):
        pass


    # Enter a parse tree produced by PLIParser#onstmt.
    def enterOnstmt(self, ctx:PLIParser.OnstmtContext):
        pass

    # Exit a parse tree produced by PLIParser#onstmt.
    def exitOnstmt(self, ctx:PLIParser.OnstmtContext):
        pass


    # Enter a parse tree produced by PLIParser#openstmt.
    def enterOpenstmt(self, ctx:PLIParser.OpenstmtContext):
        pass

    # Exit a parse tree produced by PLIParser#openstmt.
    def exitOpenstmt(self, ctx:PLIParser.OpenstmtContext):
        pass


    # Enter a parse tree produced by PLIParser#packagestmt.
    def enterPackagestmt(self, ctx:PLIParser.PackagestmtContext):
        pass

    # Exit a parse tree produced by PLIParser#packagestmt.
    def exitPackagestmt(self, ctx:PLIParser.PackagestmtContext):
        pass


    # Enter a parse tree produced by PLIParser#packagegrouplist.
    def enterPackagegrouplist(self, ctx:PLIParser.PackagegrouplistContext):
        pass

    # Exit a parse tree produced by PLIParser#packagegrouplist.
    def exitPackagegrouplist(self, ctx:PLIParser.PackagegrouplistContext):
        pass


    # Enter a parse tree produced by PLIParser#packagegroup.
    def enterPackagegroup(self, ctx:PLIParser.PackagegroupContext):
        pass

    # Exit a parse tree produced by PLIParser#packagegroup.
    def exitPackagegroup(self, ctx:PLIParser.PackagegroupContext):
        pass


    # Enter a parse tree produced by PLIParser#packagevarnamecommalist.
    def enterPackagevarnamecommalist(self, ctx:PLIParser.PackagevarnamecommalistContext):
        pass

    # Exit a parse tree produced by PLIParser#packagevarnamecommalist.
    def exitPackagevarnamecommalist(self, ctx:PLIParser.PackagevarnamecommalistContext):
        pass


    # Enter a parse tree produced by PLIParser#packagevarname.
    def enterPackagevarname(self, ctx:PLIParser.PackagevarnameContext):
        pass

    # Exit a parse tree produced by PLIParser#packagevarname.
    def exitPackagevarname(self, ctx:PLIParser.PackagevarnameContext):
        pass


    # Enter a parse tree produced by PLIParser#packageoptionlist.
    def enterPackageoptionlist(self, ctx:PLIParser.PackageoptionlistContext):
        pass

    # Exit a parse tree produced by PLIParser#packageoptionlist.
    def exitPackageoptionlist(self, ctx:PLIParser.PackageoptionlistContext):
        pass


    # Enter a parse tree produced by PLIParser#packageoption.
    def enterPackageoption(self, ctx:PLIParser.PackageoptionContext):
        pass

    # Exit a parse tree produced by PLIParser#packageoption.
    def exitPackageoption(self, ctx:PLIParser.PackageoptionContext):
        pass


    # Enter a parse tree produced by PLIParser#putstmt.
    def enterPutstmt(self, ctx:PLIParser.PutstmtContext):
        pass

    # Exit a parse tree produced by PLIParser#putstmt.
    def exitPutstmt(self, ctx:PLIParser.PutstmtContext):
        pass


    # Enter a parse tree produced by PLIParser#procedurestmt.
    def enterProcedurestmt(self, ctx:PLIParser.ProcedurestmtContext):
        pass

    # Exit a parse tree produced by PLIParser#procedurestmt.
    def exitProcedurestmt(self, ctx:PLIParser.ProcedurestmtContext):
        pass


    # Enter a parse tree produced by PLIParser#readstmt.
    def enterReadstmt(self, ctx:PLIParser.ReadstmtContext):
        pass

    # Exit a parse tree produced by PLIParser#readstmt.
    def exitReadstmt(self, ctx:PLIParser.ReadstmtContext):
        pass


    # Enter a parse tree produced by PLIParser#releasestmt.
    def enterReleasestmt(self, ctx:PLIParser.ReleasestmtContext):
        pass

    # Exit a parse tree produced by PLIParser#releasestmt.
    def exitReleasestmt(self, ctx:PLIParser.ReleasestmtContext):
        pass


    # Enter a parse tree produced by PLIParser#resignalstmt.
    def enterResignalstmt(self, ctx:PLIParser.ResignalstmtContext):
        pass

    # Exit a parse tree produced by PLIParser#resignalstmt.
    def exitResignalstmt(self, ctx:PLIParser.ResignalstmtContext):
        pass


    # Enter a parse tree produced by PLIParser#returnstmt.
    def enterReturnstmt(self, ctx:PLIParser.ReturnstmtContext):
        pass

    # Exit a parse tree produced by PLIParser#returnstmt.
    def exitReturnstmt(self, ctx:PLIParser.ReturnstmtContext):
        pass


    # Enter a parse tree produced by PLIParser#rewritestmt.
    def enterRewritestmt(self, ctx:PLIParser.RewritestmtContext):
        pass

    # Exit a parse tree produced by PLIParser#rewritestmt.
    def exitRewritestmt(self, ctx:PLIParser.RewritestmtContext):
        pass


    # Enter a parse tree produced by PLIParser#revertstmt.
    def enterRevertstmt(self, ctx:PLIParser.RevertstmtContext):
        pass

    # Exit a parse tree produced by PLIParser#revertstmt.
    def exitRevertstmt(self, ctx:PLIParser.RevertstmtContext):
        pass


    # Enter a parse tree produced by PLIParser#signalstmt.
    def enterSignalstmt(self, ctx:PLIParser.SignalstmtContext):
        pass

    # Exit a parse tree produced by PLIParser#signalstmt.
    def exitSignalstmt(self, ctx:PLIParser.SignalstmtContext):
        pass


    # Enter a parse tree produced by PLIParser#stopstmt.
    def enterStopstmt(self, ctx:PLIParser.StopstmtContext):
        pass

    # Exit a parse tree produced by PLIParser#stopstmt.
    def exitStopstmt(self, ctx:PLIParser.StopstmtContext):
        pass


    # Enter a parse tree produced by PLIParser#unlockstmt.
    def enterUnlockstmt(self, ctx:PLIParser.UnlockstmtContext):
        pass

    # Exit a parse tree produced by PLIParser#unlockstmt.
    def exitUnlockstmt(self, ctx:PLIParser.UnlockstmtContext):
        pass


    # Enter a parse tree produced by PLIParser#waitstmt.
    def enterWaitstmt(self, ctx:PLIParser.WaitstmtContext):
        pass

    # Exit a parse tree produced by PLIParser#waitstmt.
    def exitWaitstmt(self, ctx:PLIParser.WaitstmtContext):
        pass


    # Enter a parse tree produced by PLIParser#writestmt.
    def enterWritestmt(self, ctx:PLIParser.WritestmtContext):
        pass

    # Exit a parse tree produced by PLIParser#writestmt.
    def exitWritestmt(self, ctx:PLIParser.WritestmtContext):
        pass


    # Enter a parse tree produced by PLIParser#readoptionlist.
    def enterReadoptionlist(self, ctx:PLIParser.ReadoptionlistContext):
        pass

    # Exit a parse tree produced by PLIParser#readoptionlist.
    def exitReadoptionlist(self, ctx:PLIParser.ReadoptionlistContext):
        pass


    # Enter a parse tree produced by PLIParser#rewriteoptionlist.
    def enterRewriteoptionlist(self, ctx:PLIParser.RewriteoptionlistContext):
        pass

    # Exit a parse tree produced by PLIParser#rewriteoptionlist.
    def exitRewriteoptionlist(self, ctx:PLIParser.RewriteoptionlistContext):
        pass


    # Enter a parse tree produced by PLIParser#selectstmt.
    def enterSelectstmt(self, ctx:PLIParser.SelectstmtContext):
        pass

    # Exit a parse tree produced by PLIParser#selectstmt.
    def exitSelectstmt(self, ctx:PLIParser.SelectstmtContext):
        pass


    # Enter a parse tree produced by PLIParser#whenstmt.
    def enterWhenstmt(self, ctx:PLIParser.WhenstmtContext):
        pass

    # Exit a parse tree produced by PLIParser#whenstmt.
    def exitWhenstmt(self, ctx:PLIParser.WhenstmtContext):
        pass


    # Enter a parse tree produced by PLIParser#otherwisestmt.
    def enterOtherwisestmt(self, ctx:PLIParser.OtherwisestmtContext):
        pass

    # Exit a parse tree produced by PLIParser#otherwisestmt.
    def exitOtherwisestmt(self, ctx:PLIParser.OtherwisestmtContext):
        pass


    # Enter a parse tree produced by PLIParser#writeoptionlist.
    def enterWriteoptionlist(self, ctx:PLIParser.WriteoptionlistContext):
        pass

    # Exit a parse tree produced by PLIParser#writeoptionlist.
    def exitWriteoptionlist(self, ctx:PLIParser.WriteoptionlistContext):
        pass


    # Enter a parse tree produced by PLIParser#deleteoptionlist.
    def enterDeleteoptionlist(self, ctx:PLIParser.DeleteoptionlistContext):
        pass

    # Exit a parse tree produced by PLIParser#deleteoptionlist.
    def exitDeleteoptionlist(self, ctx:PLIParser.DeleteoptionlistContext):
        pass


    # Enter a parse tree produced by PLIParser#unlockoptionlist.
    def enterUnlockoptionlist(self, ctx:PLIParser.UnlockoptionlistContext):
        pass

    # Exit a parse tree produced by PLIParser#unlockoptionlist.
    def exitUnlockoptionlist(self, ctx:PLIParser.UnlockoptionlistContext):
        pass


    # Enter a parse tree produced by PLIParser#locateoptionlist.
    def enterLocateoptionlist(self, ctx:PLIParser.LocateoptionlistContext):
        pass

    # Exit a parse tree produced by PLIParser#locateoptionlist.
    def exitLocateoptionlist(self, ctx:PLIParser.LocateoptionlistContext):
        pass


    # Enter a parse tree produced by PLIParser#calloptionlist.
    def enterCalloptionlist(self, ctx:PLIParser.CalloptionlistContext):
        pass

    # Exit a parse tree produced by PLIParser#calloptionlist.
    def exitCalloptionlist(self, ctx:PLIParser.CalloptionlistContext):
        pass


    # Enter a parse tree produced by PLIParser#callmultitaskoptionlist.
    def enterCallmultitaskoptionlist(self, ctx:PLIParser.CallmultitaskoptionlistContext):
        pass

    # Exit a parse tree produced by PLIParser#callmultitaskoptionlist.
    def exitCallmultitaskoptionlist(self, ctx:PLIParser.CallmultitaskoptionlistContext):
        pass


    # Enter a parse tree produced by PLIParser#callmultitaskoption.
    def enterCallmultitaskoption(self, ctx:PLIParser.CallmultitaskoptionContext):
        pass

    # Exit a parse tree produced by PLIParser#callmultitaskoption.
    def exitCallmultitaskoption(self, ctx:PLIParser.CallmultitaskoptionContext):
        pass


    # Enter a parse tree produced by PLIParser#closegrouplist.
    def enterClosegrouplist(self, ctx:PLIParser.ClosegrouplistContext):
        pass

    # Exit a parse tree produced by PLIParser#closegrouplist.
    def exitClosegrouplist(self, ctx:PLIParser.ClosegrouplistContext):
        pass


    # Enter a parse tree produced by PLIParser#defaultitemcommalist.
    def enterDefaultitemcommalist(self, ctx:PLIParser.DefaultitemcommalistContext):
        pass

    # Exit a parse tree produced by PLIParser#defaultitemcommalist.
    def exitDefaultitemcommalist(self, ctx:PLIParser.DefaultitemcommalistContext):
        pass


    # Enter a parse tree produced by PLIParser#defaultitem.
    def enterDefaultitem(self, ctx:PLIParser.DefaultitemContext):
        pass

    # Exit a parse tree produced by PLIParser#defaultitem.
    def exitDefaultitem(self, ctx:PLIParser.DefaultitemContext):
        pass


    # Enter a parse tree produced by PLIParser#defaultrangespec.
    def enterDefaultrangespec(self, ctx:PLIParser.DefaultrangespecContext):
        pass

    # Exit a parse tree produced by PLIParser#defaultrangespec.
    def exitDefaultrangespec(self, ctx:PLIParser.DefaultrangespecContext):
        pass


    # Enter a parse tree produced by PLIParser#defaultpredicateexpr.
    def enterDefaultpredicateexpr(self, ctx:PLIParser.DefaultpredicateexprContext):
        pass

    # Exit a parse tree produced by PLIParser#defaultpredicateexpr.
    def exitDefaultpredicateexpr(self, ctx:PLIParser.DefaultpredicateexprContext):
        pass


    # Enter a parse tree produced by PLIParser#procgrouplist.
    def enterProcgrouplist(self, ctx:PLIParser.ProcgrouplistContext):
        pass

    # Exit a parse tree produced by PLIParser#procgrouplist.
    def exitProcgrouplist(self, ctx:PLIParser.ProcgrouplistContext):
        pass


    # Enter a parse tree produced by PLIParser#entrygrouplist.
    def enterEntrygrouplist(self, ctx:PLIParser.EntrygrouplistContext):
        pass

    # Exit a parse tree produced by PLIParser#entrygrouplist.
    def exitEntrygrouplist(self, ctx:PLIParser.EntrygrouplistContext):
        pass


    # Enter a parse tree produced by PLIParser#formatgrouplist.
    def enterFormatgrouplist(self, ctx:PLIParser.FormatgrouplistContext):
        pass

    # Exit a parse tree produced by PLIParser#formatgrouplist.
    def exitFormatgrouplist(self, ctx:PLIParser.FormatgrouplistContext):
        pass


    # Enter a parse tree produced by PLIParser#iooption.
    def enterIooption(self, ctx:PLIParser.IooptionContext):
        pass

    # Exit a parse tree produced by PLIParser#iooption.
    def exitIooption(self, ctx:PLIParser.IooptionContext):
        pass


    # Enter a parse tree produced by PLIParser#readoption.
    def enterReadoption(self, ctx:PLIParser.ReadoptionContext):
        pass

    # Exit a parse tree produced by PLIParser#readoption.
    def exitReadoption(self, ctx:PLIParser.ReadoptionContext):
        pass


    # Enter a parse tree produced by PLIParser#writeoption.
    def enterWriteoption(self, ctx:PLIParser.WriteoptionContext):
        pass

    # Exit a parse tree produced by PLIParser#writeoption.
    def exitWriteoption(self, ctx:PLIParser.WriteoptionContext):
        pass


    # Enter a parse tree produced by PLIParser#rewriteoption.
    def enterRewriteoption(self, ctx:PLIParser.RewriteoptionContext):
        pass

    # Exit a parse tree produced by PLIParser#rewriteoption.
    def exitRewriteoption(self, ctx:PLIParser.RewriteoptionContext):
        pass


    # Enter a parse tree produced by PLIParser#deleteoption.
    def enterDeleteoption(self, ctx:PLIParser.DeleteoptionContext):
        pass

    # Exit a parse tree produced by PLIParser#deleteoption.
    def exitDeleteoption(self, ctx:PLIParser.DeleteoptionContext):
        pass


    # Enter a parse tree produced by PLIParser#unlockoption.
    def enterUnlockoption(self, ctx:PLIParser.UnlockoptionContext):
        pass

    # Exit a parse tree produced by PLIParser#unlockoption.
    def exitUnlockoption(self, ctx:PLIParser.UnlockoptionContext):
        pass


    # Enter a parse tree produced by PLIParser#locateoption.
    def enterLocateoption(self, ctx:PLIParser.LocateoptionContext):
        pass

    # Exit a parse tree produced by PLIParser#locateoption.
    def exitLocateoption(self, ctx:PLIParser.LocateoptionContext):
        pass


    # Enter a parse tree produced by PLIParser#opengrouplist.
    def enterOpengrouplist(self, ctx:PLIParser.OpengrouplistContext):
        pass

    # Exit a parse tree produced by PLIParser#opengrouplist.
    def exitOpengrouplist(self, ctx:PLIParser.OpengrouplistContext):
        pass


    # Enter a parse tree produced by PLIParser#opengroup.
    def enterOpengroup(self, ctx:PLIParser.OpengroupContext):
        pass

    # Exit a parse tree produced by PLIParser#opengroup.
    def exitOpengroup(self, ctx:PLIParser.OpengroupContext):
        pass


    # Enter a parse tree produced by PLIParser#openoptionlist.
    def enterOpenoptionlist(self, ctx:PLIParser.OpenoptionlistContext):
        pass

    # Exit a parse tree produced by PLIParser#openoptionlist.
    def exitOpenoptionlist(self, ctx:PLIParser.OpenoptionlistContext):
        pass


    # Enter a parse tree produced by PLIParser#openoption.
    def enterOpenoption(self, ctx:PLIParser.OpenoptionContext):
        pass

    # Exit a parse tree produced by PLIParser#openoption.
    def exitOpenoption(self, ctx:PLIParser.OpenoptionContext):
        pass


    # Enter a parse tree produced by PLIParser#closegroup.
    def enterClosegroup(self, ctx:PLIParser.ClosegroupContext):
        pass

    # Exit a parse tree produced by PLIParser#closegroup.
    def exitClosegroup(self, ctx:PLIParser.ClosegroupContext):
        pass


    # Enter a parse tree produced by PLIParser#putoptionlist.
    def enterPutoptionlist(self, ctx:PLIParser.PutoptionlistContext):
        pass

    # Exit a parse tree produced by PLIParser#putoptionlist.
    def exitPutoptionlist(self, ctx:PLIParser.PutoptionlistContext):
        pass


    # Enter a parse tree produced by PLIParser#putoption.
    def enterPutoption(self, ctx:PLIParser.PutoptionContext):
        pass

    # Exit a parse tree produced by PLIParser#putoption.
    def exitPutoption(self, ctx:PLIParser.PutoptionContext):
        pass


    # Enter a parse tree produced by PLIParser#entrygroup.
    def enterEntrygroup(self, ctx:PLIParser.EntrygroupContext):
        pass

    # Exit a parse tree produced by PLIParser#entrygroup.
    def exitEntrygroup(self, ctx:PLIParser.EntrygroupContext):
        pass


    # Enter a parse tree produced by PLIParser#procgroup.
    def enterProcgroup(self, ctx:PLIParser.ProcgroupContext):
        pass

    # Exit a parse tree produced by PLIParser#procgroup.
    def exitProcgroup(self, ctx:PLIParser.ProcgroupContext):
        pass


    # Enter a parse tree produced by PLIParser#procoptionlist.
    def enterProcoptionlist(self, ctx:PLIParser.ProcoptionlistContext):
        pass

    # Exit a parse tree produced by PLIParser#procoptionlist.
    def exitProcoptionlist(self, ctx:PLIParser.ProcoptionlistContext):
        pass


    # Enter a parse tree produced by PLIParser#procoption.
    def enterProcoption(self, ctx:PLIParser.ProcoptionContext):
        pass

    # Exit a parse tree produced by PLIParser#procoption.
    def exitProcoption(self, ctx:PLIParser.ProcoptionContext):
        pass


    # Enter a parse tree produced by PLIParser#renamepaircommalist.
    def enterRenamepaircommalist(self, ctx:PLIParser.RenamepaircommalistContext):
        pass

    # Exit a parse tree produced by PLIParser#renamepaircommalist.
    def exitRenamepaircommalist(self, ctx:PLIParser.RenamepaircommalistContext):
        pass


    # Enter a parse tree produced by PLIParser#renamepair.
    def enterRenamepair(self, ctx:PLIParser.RenamepairContext):
        pass

    # Exit a parse tree produced by PLIParser#renamepair.
    def exitRenamepair(self, ctx:PLIParser.RenamepairContext):
        pass


    # Enter a parse tree produced by PLIParser#getoptionlist.
    def enterGetoptionlist(self, ctx:PLIParser.GetoptionlistContext):
        pass

    # Exit a parse tree produced by PLIParser#getoptionlist.
    def exitGetoptionlist(self, ctx:PLIParser.GetoptionlistContext):
        pass


    # Enter a parse tree produced by PLIParser#getoption.
    def enterGetoption(self, ctx:PLIParser.GetoptionContext):
        pass

    # Exit a parse tree produced by PLIParser#getoption.
    def exitGetoption(self, ctx:PLIParser.GetoptionContext):
        pass


    # Enter a parse tree produced by PLIParser#dataspecification.
    def enterDataspecification(self, ctx:PLIParser.DataspecificationContext):
        pass

    # Exit a parse tree produced by PLIParser#dataspecification.
    def exitDataspecification(self, ctx:PLIParser.DataspecificationContext):
        pass


    # Enter a parse tree produced by PLIParser#listdataspec.
    def enterListdataspec(self, ctx:PLIParser.ListdataspecContext):
        pass

    # Exit a parse tree produced by PLIParser#listdataspec.
    def exitListdataspec(self, ctx:PLIParser.ListdataspecContext):
        pass


    # Enter a parse tree produced by PLIParser#datadataspec.
    def enterDatadataspec(self, ctx:PLIParser.DatadataspecContext):
        pass

    # Exit a parse tree produced by PLIParser#datadataspec.
    def exitDatadataspec(self, ctx:PLIParser.DatadataspecContext):
        pass


    # Enter a parse tree produced by PLIParser#editdataspec.
    def enterEditdataspec(self, ctx:PLIParser.EditdataspecContext):
        pass

    # Exit a parse tree produced by PLIParser#editdataspec.
    def exitEditdataspec(self, ctx:PLIParser.EditdataspecContext):
        pass


    # Enter a parse tree produced by PLIParser#editformatexpr.
    def enterEditformatexpr(self, ctx:PLIParser.EditformatexprContext):
        pass

    # Exit a parse tree produced by PLIParser#editformatexpr.
    def exitEditformatexpr(self, ctx:PLIParser.EditformatexprContext):
        pass


    # Enter a parse tree produced by PLIParser#realformatexpr.
    def enterRealformatexpr(self, ctx:PLIParser.RealformatexprContext):
        pass

    # Exit a parse tree produced by PLIParser#realformatexpr.
    def exitRealformatexpr(self, ctx:PLIParser.RealformatexprContext):
        pass


    # Enter a parse tree produced by PLIParser#editformatitem.
    def enterEditformatitem(self, ctx:PLIParser.EditformatitemContext):
        pass

    # Exit a parse tree produced by PLIParser#editformatitem.
    def exitEditformatitem(self, ctx:PLIParser.EditformatitemContext):
        pass


    # Enter a parse tree produced by PLIParser#editformatlist.
    def enterEditformatlist(self, ctx:PLIParser.EditformatlistContext):
        pass

    # Exit a parse tree produced by PLIParser#editformatlist.
    def exitEditformatlist(self, ctx:PLIParser.EditformatlistContext):
        pass


    # Enter a parse tree produced by PLIParser#datalist.
    def enterDatalist(self, ctx:PLIParser.DatalistContext):
        pass

    # Exit a parse tree produced by PLIParser#datalist.
    def exitDatalist(self, ctx:PLIParser.DatalistContext):
        pass


    # Enter a parse tree produced by PLIParser#dostmt.
    def enterDostmt(self, ctx:PLIParser.DostmtContext):
        pass

    # Exit a parse tree produced by PLIParser#dostmt.
    def exitDostmt(self, ctx:PLIParser.DostmtContext):
        pass


    # Enter a parse tree produced by PLIParser#do_type_1.
    def enterDo_type_1(self, ctx:PLIParser.Do_type_1Context):
        pass

    # Exit a parse tree produced by PLIParser#do_type_1.
    def exitDo_type_1(self, ctx:PLIParser.Do_type_1Context):
        pass


    # Enter a parse tree produced by PLIParser#do_type_2.
    def enterDo_type_2(self, ctx:PLIParser.Do_type_2Context):
        pass

    # Exit a parse tree produced by PLIParser#do_type_2.
    def exitDo_type_2(self, ctx:PLIParser.Do_type_2Context):
        pass


    # Enter a parse tree produced by PLIParser#do_spec_2.
    def enterDo_spec_2(self, ctx:PLIParser.Do_spec_2Context):
        pass

    # Exit a parse tree produced by PLIParser#do_spec_2.
    def exitDo_spec_2(self, ctx:PLIParser.Do_spec_2Context):
        pass


    # Enter a parse tree produced by PLIParser#do_type_3.
    def enterDo_type_3(self, ctx:PLIParser.Do_type_3Context):
        pass

    # Exit a parse tree produced by PLIParser#do_type_3.
    def exitDo_type_3(self, ctx:PLIParser.Do_type_3Context):
        pass


    # Enter a parse tree produced by PLIParser#do_spec_3list.
    def enterDo_spec_3list(self, ctx:PLIParser.Do_spec_3listContext):
        pass

    # Exit a parse tree produced by PLIParser#do_spec_3list.
    def exitDo_spec_3list(self, ctx:PLIParser.Do_spec_3listContext):
        pass


    # Enter a parse tree produced by PLIParser#do_spec_3.
    def enterDo_spec_3(self, ctx:PLIParser.Do_spec_3Context):
        pass

    # Exit a parse tree produced by PLIParser#do_spec_3.
    def exitDo_spec_3(self, ctx:PLIParser.Do_spec_3Context):
        pass


    # Enter a parse tree produced by PLIParser#do_spec_3_exprlist.
    def enterDo_spec_3_exprlist(self, ctx:PLIParser.Do_spec_3_exprlistContext):
        pass

    # Exit a parse tree produced by PLIParser#do_spec_3_exprlist.
    def exitDo_spec_3_exprlist(self, ctx:PLIParser.Do_spec_3_exprlistContext):
        pass


    # Enter a parse tree produced by PLIParser#do_spec_3_expr.
    def enterDo_spec_3_expr(self, ctx:PLIParser.Do_spec_3_exprContext):
        pass

    # Exit a parse tree produced by PLIParser#do_spec_3_expr.
    def exitDo_spec_3_expr(self, ctx:PLIParser.Do_spec_3_exprContext):
        pass


    # Enter a parse tree produced by PLIParser#ifstmt.
    def enterIfstmt(self, ctx:PLIParser.IfstmtContext):
        pass

    # Exit a parse tree produced by PLIParser#ifstmt.
    def exitIfstmt(self, ctx:PLIParser.IfstmtContext):
        pass


    # Enter a parse tree produced by PLIParser#ifprestmt.
    def enterIfprestmt(self, ctx:PLIParser.IfprestmtContext):
        pass

    # Exit a parse tree produced by PLIParser#ifprestmt.
    def exitIfprestmt(self, ctx:PLIParser.IfprestmtContext):
        pass


    # Enter a parse tree produced by PLIParser#assignstmt.
    def enterAssignstmt(self, ctx:PLIParser.AssignstmtContext):
        pass

    # Exit a parse tree produced by PLIParser#assignstmt.
    def exitAssignstmt(self, ctx:PLIParser.AssignstmtContext):
        pass


    # Enter a parse tree produced by PLIParser#expr.
    def enterExpr(self, ctx:PLIParser.ExprContext):
        pass

    # Exit a parse tree produced by PLIParser#expr.
    def exitExpr(self, ctx:PLIParser.ExprContext):
        pass


    # Enter a parse tree produced by PLIParser#exprbase.
    def enterExprbase(self, ctx:PLIParser.ExprbaseContext):
        pass

    # Exit a parse tree produced by PLIParser#exprbase.
    def exitExprbase(self, ctx:PLIParser.ExprbaseContext):
        pass


    # Enter a parse tree produced by PLIParser#exprnested.
    def enterExprnested(self, ctx:PLIParser.ExprnestedContext):
        pass

    # Exit a parse tree produced by PLIParser#exprnested.
    def exitExprnested(self, ctx:PLIParser.ExprnestedContext):
        pass


    # Enter a parse tree produced by PLIParser#exprconst.
    def enterExprconst(self, ctx:PLIParser.ExprconstContext):
        pass

    # Exit a parse tree produced by PLIParser#exprconst.
    def exitExprconst(self, ctx:PLIParser.ExprconstContext):
        pass


    # Enter a parse tree produced by PLIParser#exprstrconst.
    def enterExprstrconst(self, ctx:PLIParser.ExprstrconstContext):
        pass

    # Exit a parse tree produced by PLIParser#exprstrconst.
    def exitExprstrconst(self, ctx:PLIParser.ExprstrconstContext):
        pass


    # Enter a parse tree produced by PLIParser#exprnumconst.
    def enterExprnumconst(self, ctx:PLIParser.ExprnumconstContext):
        pass

    # Exit a parse tree produced by PLIParser#exprnumconst.
    def exitExprnumconst(self, ctx:PLIParser.ExprnumconstContext):
        pass


    # Enter a parse tree produced by PLIParser#varnamerefcommalist.
    def enterVarnamerefcommalist(self, ctx:PLIParser.VarnamerefcommalistContext):
        pass

    # Exit a parse tree produced by PLIParser#varnamerefcommalist.
    def exitVarnamerefcommalist(self, ctx:PLIParser.VarnamerefcommalistContext):
        pass


    # Enter a parse tree produced by PLIParser#varnameref.
    def enterVarnameref(self, ctx:PLIParser.VarnamerefContext):
        pass

    # Exit a parse tree produced by PLIParser#varnameref.
    def exitVarnameref(self, ctx:PLIParser.VarnamerefContext):
        pass


    # Enter a parse tree produced by PLIParser#varnamequal.
    def enterVarnamequal(self, ctx:PLIParser.VarnamequalContext):
        pass

    # Exit a parse tree produced by PLIParser#varnamequal.
    def exitVarnamequal(self, ctx:PLIParser.VarnamequalContext):
        pass


    # Enter a parse tree produced by PLIParser#varnamedimensioncommalist.
    def enterVarnamedimensioncommalist(self, ctx:PLIParser.VarnamedimensioncommalistContext):
        pass

    # Exit a parse tree produced by PLIParser#varnamedimensioncommalist.
    def exitVarnamedimensioncommalist(self, ctx:PLIParser.VarnamedimensioncommalistContext):
        pass


    # Enter a parse tree produced by PLIParser#varnamedimension.
    def enterVarnamedimension(self, ctx:PLIParser.VarnamedimensionContext):
        pass

    # Exit a parse tree produced by PLIParser#varnamedimension.
    def exitVarnamedimension(self, ctx:PLIParser.VarnamedimensionContext):
        pass


    # Enter a parse tree produced by PLIParser#varnamecommalist.
    def enterVarnamecommalist(self, ctx:PLIParser.VarnamecommalistContext):
        pass

    # Exit a parse tree produced by PLIParser#varnamecommalist.
    def exitVarnamecommalist(self, ctx:PLIParser.VarnamecommalistContext):
        pass


    # Enter a parse tree produced by PLIParser#varname.
    def enterVarname(self, ctx:PLIParser.VarnameContext):
        pass

    # Exit a parse tree produced by PLIParser#varname.
    def exitVarname(self, ctx:PLIParser.VarnameContext):
        pass


    # Enter a parse tree produced by PLIParser#varname_kw.
    def enterVarname_kw(self, ctx:PLIParser.Varname_kwContext):
        pass

    # Exit a parse tree produced by PLIParser#varname_kw.
    def exitVarname_kw(self, ctx:PLIParser.Varname_kwContext):
        pass


    # Enter a parse tree produced by PLIParser#varname_kwpp.
    def enterVarname_kwpp(self, ctx:PLIParser.Varname_kwppContext):
        pass

    # Exit a parse tree produced by PLIParser#varname_kwpp.
    def exitVarname_kwpp(self, ctx:PLIParser.Varname_kwppContext):
        pass


    # Enter a parse tree produced by PLIParser#varname_conditions.
    def enterVarname_conditions(self, ctx:PLIParser.Varname_conditionsContext):
        pass

    # Exit a parse tree produced by PLIParser#varname_conditions.
    def exitVarname_conditions(self, ctx:PLIParser.Varname_conditionsContext):
        pass


    # Enter a parse tree produced by PLIParser#onconditioncommalist.
    def enterOnconditioncommalist(self, ctx:PLIParser.OnconditioncommalistContext):
        pass

    # Exit a parse tree produced by PLIParser#onconditioncommalist.
    def exitOnconditioncommalist(self, ctx:PLIParser.OnconditioncommalistContext):
        pass


    # Enter a parse tree produced by PLIParser#oncondition.
    def enterOncondition(self, ctx:PLIParser.OnconditionContext):
        pass

    # Exit a parse tree produced by PLIParser#oncondition.
    def exitOncondition(self, ctx:PLIParser.OnconditionContext):
        pass


    # Enter a parse tree produced by PLIParser#precondition.
    def enterPrecondition(self, ctx:PLIParser.PreconditionContext):
        pass

    # Exit a parse tree produced by PLIParser#precondition.
    def exitPrecondition(self, ctx:PLIParser.PreconditionContext):
        pass


    # Enter a parse tree produced by PLIParser#dclstmt.
    def enterDclstmt(self, ctx:PLIParser.DclstmtContext):
        pass

    # Exit a parse tree produced by PLIParser#dclstmt.
    def exitDclstmt(self, ctx:PLIParser.DclstmtContext):
        pass


    # Enter a parse tree produced by PLIParser#dcltermcommalist.
    def enterDcltermcommalist(self, ctx:PLIParser.DcltermcommalistContext):
        pass

    # Exit a parse tree produced by PLIParser#dcltermcommalist.
    def exitDcltermcommalist(self, ctx:PLIParser.DcltermcommalistContext):
        pass


    # Enter a parse tree produced by PLIParser#dclterm.
    def enterDclterm(self, ctx:PLIParser.DcltermContext):
        pass

    # Exit a parse tree produced by PLIParser#dclterm.
    def exitDclterm(self, ctx:PLIParser.DcltermContext):
        pass


    # Enter a parse tree produced by PLIParser#dclnamebase.
    def enterDclnamebase(self, ctx:PLIParser.DclnamebaseContext):
        pass

    # Exit a parse tree produced by PLIParser#dclnamebase.
    def exitDclnamebase(self, ctx:PLIParser.DclnamebaseContext):
        pass


    # Enter a parse tree produced by PLIParser#dclfactor.
    def enterDclfactor(self, ctx:PLIParser.DclfactorContext):
        pass

    # Exit a parse tree produced by PLIParser#dclfactor.
    def exitDclfactor(self, ctx:PLIParser.DclfactorContext):
        pass


    # Enter a parse tree produced by PLIParser#dclarrayboundcommalist.
    def enterDclarrayboundcommalist(self, ctx:PLIParser.DclarrayboundcommalistContext):
        pass

    # Exit a parse tree produced by PLIParser#dclarrayboundcommalist.
    def exitDclarrayboundcommalist(self, ctx:PLIParser.DclarrayboundcommalistContext):
        pass


    # Enter a parse tree produced by PLIParser#dclarraybound.
    def enterDclarraybound(self, ctx:PLIParser.DclarrayboundContext):
        pass

    # Exit a parse tree produced by PLIParser#dclarraybound.
    def exitDclarraybound(self, ctx:PLIParser.DclarrayboundContext):
        pass


    # Enter a parse tree produced by PLIParser#dcloptionlist.
    def enterDcloptionlist(self, ctx:PLIParser.DcloptionlistContext):
        pass

    # Exit a parse tree produced by PLIParser#dcloptionlist.
    def exitDcloptionlist(self, ctx:PLIParser.DcloptionlistContext):
        pass


    # Enter a parse tree produced by PLIParser#dcloption.
    def enterDcloption(self, ctx:PLIParser.DcloptionContext):
        pass

    # Exit a parse tree produced by PLIParser#dcloption.
    def exitDcloption(self, ctx:PLIParser.DcloptionContext):
        pass


    # Enter a parse tree produced by PLIParser#dclnumeric.
    def enterDclnumeric(self, ctx:PLIParser.DclnumericContext):
        pass

    # Exit a parse tree produced by PLIParser#dclnumeric.
    def exitDclnumeric(self, ctx:PLIParser.DclnumericContext):
        pass


    # Enter a parse tree produced by PLIParser#dclnumericNUM.
    def enterDclnumericNUM(self, ctx:PLIParser.DclnumericNUMContext):
        pass

    # Exit a parse tree produced by PLIParser#dclnumericNUM.
    def exitDclnumericNUM(self, ctx:PLIParser.DclnumericNUMContext):
        pass


    # Enter a parse tree produced by PLIParser#dclio.
    def enterDclio(self, ctx:PLIParser.DclioContext):
        pass

    # Exit a parse tree produced by PLIParser#dclio.
    def exitDclio(self, ctx:PLIParser.DclioContext):
        pass


    # Enter a parse tree produced by PLIParser#dclchar.
    def enterDclchar(self, ctx:PLIParser.DclcharContext):
        pass

    # Exit a parse tree produced by PLIParser#dclchar.
    def exitDclchar(self, ctx:PLIParser.DclcharContext):
        pass


    # Enter a parse tree produced by PLIParser#dclstg.
    def enterDclstg(self, ctx:PLIParser.DclstgContext):
        pass

    # Exit a parse tree produced by PLIParser#dclstg.
    def exitDclstg(self, ctx:PLIParser.DclstgContext):
        pass


    # Enter a parse tree produced by PLIParser#dclpgm.
    def enterDclpgm(self, ctx:PLIParser.DclpgmContext):
        pass

    # Exit a parse tree produced by PLIParser#dclpgm.
    def exitDclpgm(self, ctx:PLIParser.DclpgmContext):
        pass


    # Enter a parse tree produced by PLIParser#dclmisc.
    def enterDclmisc(self, ctx:PLIParser.DclmiscContext):
        pass

    # Exit a parse tree produced by PLIParser#dclmisc.
    def exitDclmisc(self, ctx:PLIParser.DclmiscContext):
        pass


    # Enter a parse tree produced by PLIParser#environmentspeclist.
    def enterEnvironmentspeclist(self, ctx:PLIParser.EnvironmentspeclistContext):
        pass

    # Exit a parse tree produced by PLIParser#environmentspeclist.
    def exitEnvironmentspeclist(self, ctx:PLIParser.EnvironmentspeclistContext):
        pass


    # Enter a parse tree produced by PLIParser#environmentspec.
    def enterEnvironmentspec(self, ctx:PLIParser.EnvironmentspecContext):
        pass

    # Exit a parse tree produced by PLIParser#environmentspec.
    def exitEnvironmentspec(self, ctx:PLIParser.EnvironmentspecContext):
        pass


    # Enter a parse tree produced by PLIParser#environmentspecparm.
    def enterEnvironmentspecparm(self, ctx:PLIParser.EnvironmentspecparmContext):
        pass

    # Exit a parse tree produced by PLIParser#environmentspecparm.
    def exitEnvironmentspecparm(self, ctx:PLIParser.EnvironmentspecparmContext):
        pass


    # Enter a parse tree produced by PLIParser#entryparmcommalist.
    def enterEntryparmcommalist(self, ctx:PLIParser.EntryparmcommalistContext):
        pass

    # Exit a parse tree produced by PLIParser#entryparmcommalist.
    def exitEntryparmcommalist(self, ctx:PLIParser.EntryparmcommalistContext):
        pass


    # Enter a parse tree produced by PLIParser#entryparm.
    def enterEntryparm(self, ctx:PLIParser.EntryparmContext):
        pass

    # Exit a parse tree produced by PLIParser#entryparm.
    def exitEntryparm(self, ctx:PLIParser.EntryparmContext):
        pass


    # Enter a parse tree produced by PLIParser#entryarrayspec.
    def enterEntryarrayspec(self, ctx:PLIParser.EntryarrayspecContext):
        pass

    # Exit a parse tree produced by PLIParser#entryarrayspec.
    def exitEntryarrayspec(self, ctx:PLIParser.EntryarrayspecContext):
        pass


    # Enter a parse tree produced by PLIParser#entryarrayspeccommalist.
    def enterEntryarrayspeccommalist(self, ctx:PLIParser.EntryarrayspeccommalistContext):
        pass

    # Exit a parse tree produced by PLIParser#entryarrayspeccommalist.
    def exitEntryarrayspeccommalist(self, ctx:PLIParser.EntryarrayspeccommalistContext):
        pass


    # Enter a parse tree produced by PLIParser#entryoptionlist.
    def enterEntryoptionlist(self, ctx:PLIParser.EntryoptionlistContext):
        pass

    # Exit a parse tree produced by PLIParser#entryoptionlist.
    def exitEntryoptionlist(self, ctx:PLIParser.EntryoptionlistContext):
        pass


    # Enter a parse tree produced by PLIParser#entryoption.
    def enterEntryoption(self, ctx:PLIParser.EntryoptionContext):
        pass

    # Exit a parse tree produced by PLIParser#entryoption.
    def exitEntryoption(self, ctx:PLIParser.EntryoptionContext):
        pass


    # Enter a parse tree produced by PLIParser#genericspeccommalist.
    def enterGenericspeccommalist(self, ctx:PLIParser.GenericspeccommalistContext):
        pass

    # Exit a parse tree produced by PLIParser#genericspeccommalist.
    def exitGenericspeccommalist(self, ctx:PLIParser.GenericspeccommalistContext):
        pass


    # Enter a parse tree produced by PLIParser#genericspec.
    def enterGenericspec(self, ctx:PLIParser.GenericspecContext):
        pass

    # Exit a parse tree produced by PLIParser#genericspec.
    def exitGenericspec(self, ctx:PLIParser.GenericspecContext):
        pass


    # Enter a parse tree produced by PLIParser#genericwhenoptionlist.
    def enterGenericwhenoptionlist(self, ctx:PLIParser.GenericwhenoptionlistContext):
        pass

    # Exit a parse tree produced by PLIParser#genericwhenoptionlist.
    def exitGenericwhenoptionlist(self, ctx:PLIParser.GenericwhenoptionlistContext):
        pass


    # Enter a parse tree produced by PLIParser#genericwhenoption.
    def enterGenericwhenoption(self, ctx:PLIParser.GenericwhenoptionContext):
        pass

    # Exit a parse tree produced by PLIParser#genericwhenoption.
    def exitGenericwhenoption(self, ctx:PLIParser.GenericwhenoptionContext):
        pass


    # Enter a parse tree produced by PLIParser#charspec.
    def enterCharspec(self, ctx:PLIParser.CharspecContext):
        pass

    # Exit a parse tree produced by PLIParser#charspec.
    def exitCharspec(self, ctx:PLIParser.CharspecContext):
        pass


    # Enter a parse tree produced by PLIParser#dclinit.
    def enterDclinit(self, ctx:PLIParser.DclinitContext):
        pass

    # Exit a parse tree produced by PLIParser#dclinit.
    def exitDclinit(self, ctx:PLIParser.DclinitContext):
        pass


    # Enter a parse tree produced by PLIParser#initialtospec.
    def enterInitialtospec(self, ctx:PLIParser.InitialtospecContext):
        pass

    # Exit a parse tree produced by PLIParser#initialtospec.
    def exitInitialtospec(self, ctx:PLIParser.InitialtospecContext):
        pass


    # Enter a parse tree produced by PLIParser#inititemcommalist.
    def enterInititemcommalist(self, ctx:PLIParser.InititemcommalistContext):
        pass

    # Exit a parse tree produced by PLIParser#inititemcommalist.
    def exitInititemcommalist(self, ctx:PLIParser.InititemcommalistContext):
        pass


    # Enter a parse tree produced by PLIParser#inititem.
    def enterInititem(self, ctx:PLIParser.InititemContext):
        pass

    # Exit a parse tree produced by PLIParser#inititem.
    def exitInititem(self, ctx:PLIParser.InititemContext):
        pass


    # Enter a parse tree produced by PLIParser#inititerationfactorlist.
    def enterInititerationfactorlist(self, ctx:PLIParser.InititerationfactorlistContext):
        pass

    # Exit a parse tree produced by PLIParser#inititerationfactorlist.
    def exitInititerationfactorlist(self, ctx:PLIParser.InititerationfactorlistContext):
        pass



del PLIParser