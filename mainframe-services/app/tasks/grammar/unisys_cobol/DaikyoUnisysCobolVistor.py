# Generated from ./src/mainframe_migration/parser/grammar/unisys_cobol/CobolUnisys.g4 by ANTLR 4.13.2
from typing import List, Optional

from antlr4 import ParserRuleContext, TerminalNode
from loguru import logger

from ..common.base_cobol_schemas import (
    CobolVariable,
    CopybookReplace,
    FileControlEntry,
    FileDescriptionEntry,
    ImportedCopybook,
    Paragraph,
)
from ..utils import (
    find_all_children_by_type,
    find_parent_by_type,
    get_original_code_content,
    get_paragraph_section_of_cobol_statement,
    recursive_find_first_child_by_type,
)
from .CobolUnisysHelper import extract_cobol_variable
from .CobolUnisysParser import CobolUnisysParser
from .CobolUnisysVisitor import CobolUnisysVisitor


class DaikyoUnisysCobolVistor(CobolUnisysVisitor):

    def __init__(self, parser: CobolUnisysParser):
        self.parser = parser
        self.program_id = ""
        self.copybook_list: list[ImportedCopybook] = []
        self.file_control_list: list[FileControlEntry] = []
        self.file_description_list: list[FileDescriptionEntry] = []
        self.variable_list: list[CobolVariable] = []
        self.paragraph_list: list[Paragraph] = []
        self.statements = []
        self.func = {
            "AcceptStatement": self.assessAcceptStatement,
            "AcceptFromDateStatement": self.assessAcceptFromDateStatement,
            "AcceptFromEscapeKeyStatement": self.assessAcceptFromEscapeKeyStatement,
            "AcceptFromMnemonicStatement": self.assessAcceptFromMnemonicStatement,
            "AcceptFromMessageCountStatement": self.assessAcceptFromMessageCountStatement,
            "EvaluateStatementContext": self.assessEvaluateStatement,
            "AddStatementContext": self.assessAddStatement,
            "AlterStatementContext": self.assessAlterStatement,
            "CallStatementContext": self.assessCallStatement,
            "ChangeStatementContext": self.assessChangeStatement,
            "CloseStatementContext": self.assessCloseStatement,
            "ComputeStatementContext": self.assessComputeStatement,
            "ContinueStatementContext": self.assessContinueStatement,
            "CopyStatementContext": self.assessCopyStatement,
            "CreateStatementContext": self.assessCreateStatement,
            "DisplayStatementContext": self.assessDisplayStatement,
            # "ExecCicsStatement2Context": self.assessExecCicsStatement2,
            "ExitStatementContext": self.assessExitStatement,
            "FreeStatementContext": self.assessFreeStatement,
            "FindStatementContext": self.assessFindStatement,
            "LockStatementContext": self.assessLockStatement,
            "GobackStatementContext": self.assessGobackStatement,
            "GoToStatementContext": self.assessGoToStatement,
            "InitializeStatementContext": self.assessInitializeStatement,
            "InspectStatementContext": self.assessInspectStatement,
            "MoveStatementContext": self.assessMoveStatement,
            "ModifyStatementContext": self.assessModifyStatement,
            "StringStatementContext": self.assessStringStatement,
            "SubtractStatementContext": self.assessSubtractStatement,
            "SetStatementContext": self.assessSetStatement,
            "StopStatementContext": self.assessStopStatement,
            "TransactionStatementContext": self.assessTransactionStatement,
            "WaitStatementContext": self.assessWaitStatement,
            "WriteStatementContext": self.assessWriteStatement,
            "OpenStatementContext": self.assessOpenStatement,
            "IfStatementContext": self.assessIfStatement,
            "PerformStatementContext": self.assessPerformStatement,
            "ReadStatementContext": self.assessReadStatement,
            "RewriteStatementContext": self.assessRewriteStatement,
        }

    def find_parent(self, current_ctx, target_ctx):
        """
        Utility function to recursively find specific type of parent context.
        """
        p = current_ctx.parentCtx
        if p is None:
            return None
        if isinstance(p, target_ctx):
            return p
        else:
            return self.find_parent(p, target_ctx)

    def find_child(
        self, ctx: ParserRuleContext, target_context_type: type
    ) -> ParserRuleContext:
        """
        Utility function to recursively find the first child node of a given context type.

        :param ctx: The current parse tree node (context).
        :param target_context_type: The type of the target context to find.
        :return: The first child node of the target context type, or None if not found.
        """
        # Base case: if the current context is of the target type, return it
        if isinstance(ctx, target_context_type):
            return ctx

        # Recursively search in the children
        for child in ctx.children:
            if isinstance(child, ParserRuleContext):
                result = self.find_child(child, target_context_type)
                if result is not None:
                    return result

        # If no matching child is found, return None
        return None

    def visitStartRule(self, ctx: CobolUnisysParser.StartRuleContext):
        # tree_str = ctx.toStringTree(recog=self.parser)
        # lisp_tree_str = beautify_lisp_string(tree_str)
        # print(lisp_tree_str)
        return self.visitChildren(ctx)

    def assessAddStatement(self, ctx: CobolUnisysParser.AddStatementContext):
        # Intialize
        tag = "AddStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        # Get all children of context
        children = ctx.getChildren()
        children = [type(c) for c in children]
        # AddTo
        if CobolUnisysParser.AddToStatementContext in children:
            addToStatement = ctx.addToStatement()
            # addFrom
            addFrom = addToStatement.addFrom()
            if addFrom:
                res["identifier_1"] = []
                res["literal_1"] = []
                for af in addFrom:
                    for a in af.getChildren():
                        if isinstance(a, CobolUnisysParser.IdentifierContext):
                            # res["identifier_1"].append(a.getText())
                            res["identifier_1"].append(
                                get_original_code_content(
                                    self.parser,
                                    a.start.tokenIndex,
                                    a.stop.tokenIndex,
                                )
                            )
                        elif isinstance(a, CobolUnisysParser.LiteralContext):
                            res["literal_1"].append(a.getText())
            # addTo
            addTo = addToStatement.addTo()
            if addTo:
                res["identifier_2"] = []
                res["literal_2"] = []
                for at in addTo:
                    for a in at.getChildren():
                        if isinstance(a, CobolUnisysParser.IdentifierContext):
                            # res["identifier_2"].append(a.getText())
                            res["identifier_2"].append(
                                get_original_code_content(
                                    self.parser,
                                    a.start.tokenIndex,
                                    a.stop.tokenIndex,
                                )
                            )
                        elif isinstance(a, CobolUnisysParser.LiteralContext):
                            res["literal_2"].append(a.getText())
                        elif isinstance(a, CobolUnisysParser.FigurativeConstantContext):
                            res["literal_2"].append(a.getText())

        # AddToGiving
        elif CobolUnisysParser.AddToGivingStatementContext in children:
            addToGivingStatement = ctx.addToGivingStatement()
            # addFrom
            addFrom = addToGivingStatement.addFrom()
            if addFrom:
                res["identifier_1"] = []
                res["literal_1"] = []
                for af in addFrom:
                    for a in af.getChildren():
                        if isinstance(a, CobolUnisysParser.IdentifierContext):
                            # res["identifier_1"].append(a.getText())
                            res["identifier_1"].append(
                                get_original_code_content(
                                    self.parser,
                                    a.start.tokenIndex,
                                    a.stop.tokenIndex,
                                )
                            )
                        elif isinstance(a, CobolUnisysParser.LiteralContext):
                            res["literal_1"].append(a.getText())
            # addToGiving
            addToGiving = addToGivingStatement.addToGiving()
            if addToGiving:
                res["identifier_2"] = []
                res["literal_2"] = []
                for at in addToGiving:
                    for a in at.getChildren():
                        if isinstance(a, CobolUnisysParser.IdentifierContext):
                            # res["identifier_2"].append(a.getText())
                            res["identifier_2"].append(
                                get_original_code_content(
                                    self.parser,
                                    a.start.tokenIndex,
                                    a.stop.tokenIndex,
                                )
                            )
                        elif isinstance(a, CobolUnisysParser.LiteralContext):
                            res["literal_2"].append(a.getText())
                        elif isinstance(a, CobolUnisysParser.FigurativeConstantContext):
                            res["literal_2"].append(a.getText())
            # addGiving
            addGiving = addToGivingStatement.addGiving()
            if addGiving:
                res["identifier_3"] = []
                res["literal_3"] = []
                for ag in addGiving:
                    for a in ag.getChildren():
                        if isinstance(a, CobolUnisysParser.IdentifierContext):
                            # res["identifier_3"].append(a.getText())
                            res["identifier_3"].append(
                                get_original_code_content(
                                    self.parser,
                                    a.start.tokenIndex,
                                    a.stop.tokenIndex,
                                )
                            )
                        elif isinstance(a, CobolUnisysParser.LiteralContext):
                            res["literal_3"].append(a.getText())

        return res

    def visitAddStatement(self, ctx: CobolUnisysParser.AddStatementContext):
        res = self.assessAddStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessAlterStatement(self, ctx: CobolUnisysParser.AlterStatementContext):
        # Intialize
        tag = "AlterStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        # alterProceedTo
        alterProceedTo = ctx.alterProceedTo()
        if alterProceedTo:
            res["alterProceedTo"] = []
            for t in alterProceedTo:
                procedureName = t.procedureName()
                procedureName = [p.getText() for p in procedureName]  # Convert to list
                res["alterProceedTo"].append(
                    {
                        "procedure_name_1": procedureName[0],
                        "procedure_name_2": procedureName[1],
                    }
                )
        # print(res)
        return res

    def visitAlterStatement(self, ctx: CobolUnisysParser.AlterStatementContext):
        res = self.assessAlterStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessCallStatement(self, ctx: CobolUnisysParser.CallStatementContext):
        # Intialize
        tag = "CallStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        # Get all children of context
        children = ctx.getChildren()
        children = [type(c) for c in children]
        # literal_1
        if CobolUnisysParser.LiteralContext in children:
            literal = ctx.literal()
            res["call_literal"] = literal.getText()
        # identifier_1
        elif CobolUnisysParser.IdentifierContext in children:
            identifier = ctx.identifier()
            # res["identifier_1"] = identifier.getText()
            res["call_identifiers"].append(
                get_original_code_content(
                    self.parser,
                    identifier.start.tokenIndex,
                    identifier.stop.tokenIndex,
                )
            )
        # callUsingPhrase
        res["using_identifiers"] = []
        res["using_literals"] = []
        callUsingPhrase = ctx.callUsingPhrase()
        if callUsingPhrase:
            res["call_type"] = "USING"
            call_using_parameter_list: List[
                CobolUnisysParser.CallUsingParameterContext
            ] = callUsingPhrase.callUsingParameter()

            for call_using_parameter in call_using_parameter_list:
                call_using_parameter = call_using_parameter.getChild(0)
                if isinstance(
                    call_using_parameter, CobolUnisysParser.CallByReferencePhraseContext
                ):
                    call_by_reference_list: List[
                        CobolUnisysParser.CallByReferenceContext
                    ] = call_using_parameter.callByReference()

                    for call_by_reference in call_by_reference_list:
                        identifier = call_by_reference.identifier()
                        if identifier:
                            res["using_identifiers"].append(identifier.getText())
                        literal = (
                            call_by_reference.literal()
                            or call_by_reference.fileName()
                            or call_by_reference.OMITTED()
                        )
                        if literal:
                            if isinstance(literal, TerminalNode):
                                res["using_literals"].append(
                                    get_original_code_content(
                                        self.parser,
                                        literal.symbol.tokenIndex,
                                        literal.symbol.tokenIndex,
                                    )
                                )
                            else:
                                res["using_literals"].append(
                                    get_original_code_content(
                                        self.parser,
                                        literal.start.tokenIndex,
                                        literal.stop.tokenIndex,
                                    )
                                )

                elif isinstance(
                    call_using_parameter, CobolUnisysParser.CallByValuePhraseContext
                ):
                    call_by_value_list = call_using_parameter.callByValue()
                    for call_by_value in call_by_value_list:
                        identifier = call_by_value.identifier()
                        if identifier:
                            res["using_identifiers"].append(identifier.getText())

                        literal = call_by_value.literal()
                        if literal:
                            res["using_literals"].append(literal.getText())

                elif isinstance(
                    call_using_parameter, CobolUnisysParser.CallByContentPhraseContext
                ):
                    call_by_content_list = call_using_parameter.callByContent()
                    for call_by_content in call_by_content_list:
                        identifier = call_by_content.identifier()
                        if identifier:
                            res["using_identifiers"].append(identifier.getText())

                        literal = call_by_content.literal() or call_by_content.OMITTED()
                        if literal:
                            if isinstance(literal, TerminalNode):
                                res["using_literals"].append(
                                    get_original_code_content(
                                        self.parser,
                                        literal.symbol.tokenIndex,
                                        literal.symbol.tokenIndex,
                                    )
                                )
                            else:
                                res["using_literals"].append(
                                    get_original_code_content(
                                        self.parser,
                                        literal.start.tokenIndex,
                                        literal.stop.tokenIndex,
                                    )
                                )

        call_giving_phrase = ctx.callGivingPhrase()
        if call_giving_phrase:
            res["giving_identifier"] = call_giving_phrase.identifier().getText()

        # call system
        if ctx.callSystem():
            res["call_type"] = "SYSTEM"

        return res

    def visitCallStatement(self, ctx: CobolUnisysParser.CallStatementContext):
        res = self.assessCallStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessCloseStatement(self, ctx: CobolUnisysParser.CloseStatementContext):
        # Intialize
        tag = "CloseStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        # closeFile
        res["close_files"] = []
        close_phrases = ctx.closePhrase()

        for close_phrase in close_phrases:
            close_file_details = {}

            close_file = close_phrase.closeFile()

            file_name = close_file.fileName()
            close_file_details["file_name"] = file_name.getText()

            close_option = (
                close_phrase.SAVE()
                or close_phrase.PURGE()
                or close_phrase.RELEASE()
                or close_phrase.CRUNCH()
            )
            close_file_details["close_option"] = (
                close_option.getText() if close_option else None
            )

            close_file_details["on_exception_clause"] = []
            on_exception_clause = close_file.onExceptionClause()
            if on_exception_clause:
                statements = on_exception_clause.statement()
                for statement in statements:
                    child = statement.getChild(0)
                    type_ = type(child).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        close_file_details["on_exception_clause"].append(f(child))

            res["close_files"].append(close_file_details)

        return res

    def visitCloseStatement(self, ctx: CobolUnisysParser.CloseStatementContext):
        res = self.assessCloseStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessComputeStatement(self, ctx: CobolUnisysParser.ComputeStatementContext):
        # Intialize
        tag = "ComputeStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        computeStore = ctx.computeStore()
        if computeStore:
            computeStore = [c.getText() for c in computeStore]
            res["identifier_1"] = computeStore
        arithmeticExpression = ctx.arithmeticExpression()
        if arithmeticExpression:
            arithmetic_expression = " ".join(
                c.getText() for c in arithmeticExpression.getChildren()
            )
            res["arithmetic_expression"] = arithmetic_expression.strip()
        # print(res)
        return res

    def visitComputeStatement(self, ctx: CobolUnisysParser.ComputeStatementContext):
        res = self.assessComputeStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessContinueStatement(self, ctx: CobolUnisysParser.ContinueStatementContext):
        # Intialize
        tag = "ContinueStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        # print(res)
        return res

    def visitContinueStatement(self, ctx: CobolUnisysParser.ContinueStatementContext):
        res = self.assessContinueStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessCopyStatement(self, ctx: CobolUnisysParser.CopyStatementContext):
        # Intialize
        tag = "CopyStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        copySource = ctx.copySource()
        if copySource:
            # Get all children of context
            children = copySource.getChildren()
            children = [type(c) for c in children]
            # CobolUnisysParser.LiteralContext
            if CobolUnisysParser.LiteralContext in children:
                literal = copySource.literal()
                res["literal_1"] = literal.getText()
            # CobolUnisysParser.CobolWordContext
            elif CobolUnisysParser.CobolWordContext in children:
                cobolWord = copySource.cobolWord()
                res["text_name"] = cobolWord.getText()
            # CobolUnisysParser.FileNameContext
            elif CobolUnisysParser.FileNameContext in children:
                filename = copySource.filename()
                res["filename"] = filename.getText()
        # replacingPhrase
        replacingPhrase = ctx.replacingPhrase()
        if replacingPhrase:
            res["replacingPhrase"] = []
            for rp in replacingPhrase:
                replaceClause = rp.replaceClause()
                if replaceClause:
                    for rc in replaceClause:
                        replaceable = rc.replaceable()
                        replacement = rc.replacement()
                        res["replacingPhrase"].append(
                            {
                                "partial_word_1": replaceable.getText(),
                                "partial_word_2": replacement.getText(),
                            }
                        )
        # print(res)
        return res

    def assessDisplayStatement(self, ctx: CobolUnisysParser.DisplayStatementContext):
        # Intialize
        tag = "DisplayStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        displayOperand = ctx.displayOperand()
        if displayOperand:
            res["identifier_1"] = []
            res["literal_1"] = []
            for do in displayOperand:
                for d in do.getChildren():
                    if isinstance(d, CobolUnisysParser.IdentifierContext):
                        # res["identifier_1"].append(d.getText())
                        res["identifier_1"].append(
                            get_original_code_content(
                                self.parser, d.start.tokenIndex, d.stop.tokenIndex
                            )
                        )
                    elif isinstance(d, CobolUnisysParser.LiteralContext):
                        res["literal_1"].append(d.getText())
        # print(res)
        return res

    def visitDisplayStatement(self, ctx: CobolUnisysParser.DisplayStatementContext):
        res = self.assessDisplayStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessEvaluateStatement(self, ctx: CobolUnisysParser.EvaluateStatementContext):
        # Intialize
        tag = "EvaluateStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        raw = res["raw"]
        # evaluateSelect
        evaluateSelect = ctx.evaluateSelect()
        if evaluateSelect:
            res["evaluateSelect"] = evaluateSelect.getText()
        # evaluateAlsoSelect
        evaluateAlsoSelect = ctx.evaluateAlsoSelect()
        if evaluateAlsoSelect:
            res["evaluateAlsoSelect"] = []
            for eas in evaluateAlsoSelect:
                evaluateSelect = eas.evaluateSelect()
                res["evaluateAlsoSelect"].append(evaluateSelect.getText())
        # evaluateWhenPhrase
        evaluateWhenPhrase = ctx.evaluateWhenPhrase()
        if evaluateWhenPhrase:
            res["evaluateWhenPhrase"] = []
            for ewp in evaluateWhenPhrase:
                r = {}
                # evaluateWhen
                evaluateWhen = ewp.evaluateWhen()
                if evaluateWhen:
                    r["evaluateWhen"] = []
                    for ew in evaluateWhen:
                        start_idx = ew.start.tokenIndex
                        stop_idx = ew.stop.tokenIndex
                        evaluateCondition = ew.evaluateCondition()
                        # r["evaluateWhen"].append(self.code[start_idx:stop_idx+1])
                        r["evaluateWhen"].append(evaluateCondition.getText())

                # statement
                statement = ewp.statement()
                if statement:
                    r["statement"] = []
                    for st in statement:
                        start_idx = st.start.tokenIndex
                        stop_idx = st.stop.tokenIndex
                        c = st.getChild(0)
                        type_ = type(c).__name__
                        if type_ in self.func:
                            f = self.func[type_]
                            r["statement"].append(f(c))
                        else:
                            r["statement"].append(
                                get_original_code_content(
                                    self.parser, start_idx, stop_idx
                                )
                            )
                # Update
                res["evaluateWhenPhrase"].append(r)

        # evaluateWhenOther
        evaluateWhenOther = ctx.evaluateWhenOther()
        if evaluateWhenOther:
            res["evaluateWhenOther"] = []

        return res

    def visitEvaluateStatement(self, ctx: CobolUnisysParser.EvaluateStatementContext):
        res = self.assessEvaluateStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    # def assessExecCicsStatement2(
    #     self, ctx: CobolUnisysParser.ExecCicsStatement2Context
    # ):
    #     # Intialize
    #     tag = "ExecCicsStatement2"
    #     res = {}
    #     res["tag"] = tag
    #     # Get position and raw string
    #     start_token = ctx.start
    #     stop_token = ctx.stop
    #     res["start_line"] = start_token.line
    #     res["stop_line"] = stop_token.line
    #     res["start_idx"] = start_token.start
    #     res["stop_idx"] = stop_token.stop
    #     res["raw"] = get_original_code_content(
    #         self.parser, start_token.tokenIndex, stop_token.tokenIndex
    #     )
    #     # commandName
    #     commandName = ctx.commandName()
    #     res["commandName"] = commandName.getText()
    #     # commandBody
    #     commandBody = ctx.commandBody()
    #     if commandBody:
    #         res["commandBody"] = []
    #         commandParameter = commandBody.commandParameter()
    #         for cp in commandParameter:
    #             parameterName = cp.parameterName()
    #             parameterValue = cp.parameterValue()
    #             parameterValueWithIndex = cp.parameterValueWithIndex()
    #             if parameterValue:
    #                 res["commandBody"].append(
    #                     {
    #                         "parameterName": parameterName.getText(),
    #                         "parameterValue": parameterValue.getText(),
    #                     }
    #                 )
    #             elif parameterValueWithIndex:
    #                 res["commandBody"].append(
    #                     {
    #                         "parameterName": parameterName.getText(),
    #                         "parameterValue": parameterValueWithIndex.getText(),
    #                     }
    #                 )
    #             else:
    #                 res["commandBody"].append(
    #                     {"parameterName": parameterName.getText(), "parameterValue": ""}
    #                 )
    #     return res

    def visitExecCicsStatement2(self, ctx: CobolUnisysParser.ExecCicsStatement2Context):
        # res = self.assessExecCicsStatement2(ctx)
        # parent = ctx.parentCtx
        # grand_parent = parent.parentCtx
        # paragraph = find_parent_by_type(ctx, CobolUnisysParser.ParagraphContext)
        # if paragraph:
        #     paragraphName = paragraph.paragraphName()
        #     res["paragraph"] = paragraphName.getText()
        # else:
        #     res["paragraph"] = None
        # procedure_section = self.find_parent(
        #     ctx, CobolUnisysParser.ProcedureSectionContext
        # )
        # if procedure_section:
        #     procedure_section_header = procedure_section.procedureSectionHeader()
        #     sectionName = procedure_section_header.sectionName()
        #     res["section"] = sectionName.getText()
        # else:
        #     res["section"] = None
        # if type(grand_parent).__name__ == "SentenceContext":
        #     self.statements.append(res)
        return self.visitChildren(ctx)

    def assessExitStatement(self, ctx: CobolUnisysParser.ExitStatementContext):
        # Intialize
        tag = "ExitStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        return res

    def visitExitStatement(self, ctx: CobolUnisysParser.ExitStatementContext):
        res = self.assessExitStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessGobackStatement(self, ctx: CobolUnisysParser.GobackStatementContext):
        # Intialize
        tag = "GobackStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        return res

    def visitGobackStatement(self, ctx: CobolUnisysParser.GobackStatementContext):
        res = self.assessGobackStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessFindStatement(self, ctx: CobolUnisysParser.FindStatementContext):
        tag = "FindStatement"
        res = {}

        start_token = ctx.start
        stop_token = ctx.stop

        res["tag"] = tag
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )

        find_options = ctx.findOption()
        res["find_option"] = []

        if find_options:
            for find_option in find_options:
                res["find_option"].append(find_option.getText().upper())

        record_name = ctx.identifier()
        res["record_name"] = record_name.getText()

        via_clause = ctx.viaClause()

        if via_clause:
            via_find_option = via_clause.findOption()
            via_identifier = via_clause.identifier()

            res["via_find_option"] = (
                via_find_option.getText().upper() if via_find_option else None
            )
            res["via_identifier"] = via_identifier.getText()

        condition = ctx.condition()
        if condition:
            res["condition"] = get_original_code_content(
                self.parser, condition.start.tokenIndex, condition.stop.tokenIndex
            )

        res["on_exception_clause"] = []
        on_exception_clause = ctx.onExceptionClause()
        if on_exception_clause:
            statements = on_exception_clause.statement()
            for statement in statements:
                child = statement.getChild(0)
                type_ = type(child).__name__
                if type_ in self.func:
                    f = self.func[type_]
                    res["on_exception_clause"].append(f(child))

        return res

    # Visit a parse tree produced by CobolUnisysParser#findStatement.
    def visitFindStatement(self, ctx: CobolUnisysParser.FindStatementContext):
        res = self.assessFindStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)

        return self.visitChildren(ctx)

        return self.visitChildren(ctx)

    def assessLockStatement(self, ctx: CobolUnisysParser.LockStatementContext):
        tag = "LockStatement"
        res = {}

        start_token = ctx.start
        stop_token = ctx.stop

        res["tag"] = tag
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )

        database_name = ctx.qualifiedDataName()
        res["database_name"] = get_original_code_content(
            self.parser,
            database_name.start.tokenIndex,
            database_name.stop.tokenIndex,
        )

        lock_type = ctx.FIRST() or ctx.NEXT()
        res["lock_type"] = lock_type.getText().upper() if lock_type else None

        via_clause = ctx.viaClause()

        if via_clause:
            lock_option = via_clause.findOption()
            via_identifier = via_clause.identifier()

            res["lock_option"] = lock_option.getText().upper() if lock_option else None
            res["via_identifier"] = via_identifier.getText()

        condition = ctx.condition()
        if condition:
            res["condition"] = get_original_code_content(
                self.parser, condition.start.tokenIndex, condition.stop.tokenIndex
            )

        res["on_exception_clause"] = []
        on_exception_clause = ctx.onExceptionClause()
        if on_exception_clause:
            statements = on_exception_clause.statement()
            for statement in statements:
                child = statement.getChild(0)
                type_ = type(child).__name__
                if type_ in self.func:
                    f = self.func[type_]
                    res["on_exception_clause"].append(f(child))

        return res

    def visitLockStatement(self, ctx: CobolUnisysParser.LockStatementContext):
        res = self.assessLockStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)

        return super().visitLockStatement(ctx)

    def visitAttachStatement(self, ctx: CobolUnisysParser.AttachStatementContext):
        tag = "AttachStatement"
        res = {}

        start_token = ctx.start
        stop_token = ctx.stop

        res["tag"] = tag
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )

        self.statements.append(res)
        return super().visitAttachStatement(ctx)

    def assessTransactionStatement(
        self, ctx: CobolUnisysParser.TransactionStatementContext
    ):
        tag = "TransactionStatement"
        res = {}

        start_token = ctx.start
        stop_token = ctx.stop

        res["tag"] = tag
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )

        transaction = ctx.getChild(0)
        if isinstance(transaction, CobolUnisysParser.TransactionBeginContext):
            res["transaction_type"] = "BEGIN"
            audit = transaction.AUDIT()
            no_audit = transaction.NO_AUDIT()
            audit_option = (
                audit.getText().upper()
                if audit
                else no_audit.getText() if no_audit else None
            )

            database_name = transaction.qualifiedDataName()
            sync = True if transaction.SYNC() else False

            transaction_details = {
                "audit_option": audit_option,
                "database_name": database_name.getText(),
                "sync": sync,
            }

            transaction_details["on_exception_clause"] = []
            on_exception_clause = transaction.onExceptionClause()
            if on_exception_clause:
                statements = on_exception_clause.statement()
                for statement in statements:
                    child = statement.getChild(0)
                    type_ = type(child).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        transaction_details["on_exception_clause"].append(f(child))

            res["transaction_details"] = transaction_details

        elif isinstance(transaction, CobolUnisysParser.TransactionEndContext):
            res["transaction_type"] = "END"
            audit = transaction.AUDIT()
            no_audit = transaction.NO_AUDIT()
            audit_option = (
                audit.getText().upper()
                if audit
                else no_audit.getText() if no_audit else None
            )

            database_name = transaction.qualifiedDataName()
            sync = True if transaction.SYNC() else False

            transaction_details = {
                "audit_option": audit_option,
                "database_name": database_name.getText(),
                "sync": sync,
            }

            transaction_details["on_exception_clause"] = []
            on_exception_clause = transaction.onExceptionClause()
            if on_exception_clause:
                statements = on_exception_clause.statement()
                for statement in statements:
                    child = statement.getChild(0)
                    type_ = type(child).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        transaction_details["on_exception_clause"].append(f(child))

            res["transaction_details"] = transaction_details

        elif isinstance(transaction, CobolUnisysParser.TransactionCancelContext):
            res["transaction_type"] = "CANCEL"
            res["transaction_details"] = None

        return res

    def visitTransactionStatement(
        self, ctx: CobolUnisysParser.TransactionStatementContext
    ):
        res = self.assessTransactionStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)

        return super().visitTransactionStatement(ctx)

    def assessWaitStatement(self, ctx: CobolUnisysParser.WaitStatementContext):
        tag = "WaitStatement"
        res = {}

        start_token = ctx.start
        stop_token = ctx.stop

        res["tag"] = tag
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )

        reset = ctx.RESET()
        until = ctx.UNTIL()

        res["is_reset"] = True if reset else False
        res["is_wait_until"] = True if until else False

        wait_arithmetic_expression = ctx.waitArithmeticExpression()

        res["option"] = get_original_code_content(
            self.parser,
            wait_arithmetic_expression.start.tokenIndex,
            wait_arithmetic_expression.stop.tokenIndex,
        )

        identifier = recursive_find_first_child_by_type(
            ctx, CobolUnisysParser.IdentifierContext
        )
        if identifier:
            res["identifier"] = identifier.getText()

        literal = recursive_find_first_child_by_type(
            ctx, CobolUnisysParser.LiteralContext
        )

        if literal:
            res["literal"] = literal.getText()

        library_entry_procedure_using_clause = recursive_find_first_child_by_type(
            ctx, CobolUnisysParser.LibraryEntryProcedureUsingClauseContext
        )

        if library_entry_procedure_using_clause:
            using_names = (
                library_entry_procedure_using_clause.libraryEntryProcedureUsingName()
            )

            res["using_data_names"] = [name.getText() for name in using_names]

        library_entry_procedure_giving_clause = recursive_find_first_child_by_type(
            ctx, CobolUnisysParser.LibraryEntryProcedureGivingClauseContext
        )

        if library_entry_procedure_giving_clause:
            res["giving_data_name"] = (
                library_entry_procedure_giving_clause.dataName().getText()
            )

        self.statements.append(res)

        return res

    def visitWaitStatement(self, ctx: CobolUnisysParser.WaitStatementContext):
        res = self.assessWaitStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)

        return super().visitWaitStatement(ctx)

    def assessCreateStatement(self, ctx: CobolUnisysParser.CreateStatementContext):
        tag = "CreateStatement"
        res = {}

        start_token = ctx.start
        stop_token = ctx.stop

        res["tag"] = tag
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )

        create_type = ctx.getChild(0)
        identifier = ctx.identifier()

        res["create_type"] = create_type.getText().upper()
        res["identifier"] = identifier.getText()

        res["on_exception_clause"] = []
        on_exception_clause = ctx.onExceptionClause()
        if on_exception_clause:
            statements = on_exception_clause.statement()
            for statement in statements:
                child = statement.getChild(0)
                type_ = type(child).__name__
                if type_ in self.func:
                    f = self.func[type_]
                    res["on_exception_clause"].append(f(child))

        return res

    def visitCreateStatement(self, ctx: CobolUnisysParser.CreateStatementContext):
        res = self.assessCreateStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)

        return super().visitCreateStatement(ctx)

    def assessFreeStatement(self, ctx: CobolUnisysParser.FreeStatementContext):
        raw = get_original_code_content(
            self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex
        )
        tag = "FreeStatement"
        res = {}

        start_token = ctx.start
        stop_token = ctx.stop

        res["tag"] = tag
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )

        identifier = ctx.identifier()

        if not identifier:
            logger.warning(f"No identifier found in FreeStatement '{raw}'")

        res["identifier"] = identifier.getText() if identifier else ""
        res["on_exception_clause"] = []

        on_exception_clause = ctx.onExceptionClause()
        if on_exception_clause:
            statements = on_exception_clause.statement()
            for statement in statements:
                child = statement.getChild(0)
                type_ = type(child).__name__
                if type_ in self.func:
                    f = self.func[type_]
                    res["on_exception_clause"].append(f(child))

        return res

    def visitFreeStatement(self, ctx: CobolUnisysParser.FreeStatementContext):
        res = self.assessFreeStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)

        return super().visitFreeStatement(ctx)

    def assessModifyStatement(self, ctx: CobolUnisysParser.ModifyStatementContext):
        tag = "ModifyStatement"
        res = {}

        start_token = ctx.start
        stop_token = ctx.stop

        res["tag"] = tag
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )

        file_name = ctx.fileName()
        modify_to = ctx.modifyTo()
        condition = ctx.condition()

        res["file_name"] = file_name.getText()

        modify_to_child = modify_to.getChild(0)

        if isinstance(modify_to_child, CobolUnisysParser.IdentifierContext):
            res["modify_to"] = modify_to_child.getText()
        elif isinstance(modify_to_child, CobolUnisysParser.LiteralContext):
            res["modify_to"] = get_original_code_content(
                self.parser,
                modify_to_child.start.tokenIndex,
                modify_to_child.stop.tokenIndex,
            )
        elif isinstance(modify_to_child, CobolUnisysParser.ArithmeticExpressionContext):
            res["modify_to"] = get_original_code_content(
                self.parser,
                modify_to_child.start.tokenIndex,
                modify_to_child.stop.tokenIndex,
            )
        else:
            cobol_word = recursive_find_first_child_by_type(
                modify_to, CobolUnisysParser.CobolWordContext
            )

            if not cobol_word:
                logger.warning(
                    f"No identifier or literal found in ModifyStatement '{res['raw']}'"
                )
                res["modify_to"] = ""

            else:
                res["modify_to"] = cobol_word.getText()

        if condition:
            res["condition"] = get_original_code_content(
                self.parser, condition.start.tokenIndex, condition.stop.tokenIndex
            )

        res["on_exception_clause"] = []

        on_exception_clause = ctx.onExceptionClause()
        if on_exception_clause:
            statements = on_exception_clause.statement()
            for statement in statements:
                child = statement.getChild(0)
                type_ = type(child).__name__
                if type_ in self.func:
                    f = self.func[type_]
                    res["on_exception_clause"].append(f(child))

        return res

    def visitModifyStatement(self, ctx: CobolUnisysParser.ModifyStatementContext):
        res = self.assessModifyStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)

        return super().visitModifyStatement(ctx)

    def assessStoreStatement(self, ctx: CobolUnisysParser.StoreStatementContext):
        tag = "StoreStatement"
        res = {}

        start_token = ctx.start
        stop_token = ctx.stop

        res["tag"] = tag
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )

        database_name = ctx.qualifiedDataName()
        res["database_name"] = database_name.getText()

        res["on_exception_clause"] = []

        on_exception_clause = ctx.onExceptionClause()
        if on_exception_clause:
            statements = on_exception_clause.statement()
            for statement in statements:
                child = statement.getChild(0)
                type_ = type(child).__name__
                if type_ in self.func:
                    f = self.func[type_]
                    res["on_exception_clause"].append(f(child))

        return res

    def visitStoreStatement(self, ctx: CobolUnisysParser.StoreStatementContext):
        res = self.assessStoreStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)

        return super().visitStoreStatement(ctx)

    def assessChangeStatement(self, ctx: CobolUnisysParser.ChangeStatementContext):
        tag = "ChangeStatement"
        res = {}

        start_token = ctx.start
        stop_token = ctx.stop

        res["tag"] = tag
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )

        attribute_token = ctx.ATTRIBUTE()
        change_attribute = ctx.getChild(2)

        if isinstance(change_attribute, CobolUnisysParser.ChangeFileAttributeContext):
            res["attribute_type"] = "FILE"
            source_identifier = get_original_code_content(
                self.parser,
                change_attribute.getChild(1).start.tokenIndex,
                change_attribute.getChild(1).stop.tokenIndex,
            )
            res["source_identifier"] = source_identifier
            res["source_option"] = get_original_code_content(
                self.parser,
                attribute_token.symbol.tokenIndex,
                change_attribute.getChild(1).stop.tokenIndex,
            )

            target_identifier = change_attribute.identifier()

            target_literal = change_attribute.literal()
            res["target_identifier"] = (
                target_identifier.getText() if target_identifier else None
            )
            res["target_literal"] = target_literal.getText() if target_literal else None
            res["target_option"] = None

        elif isinstance(
            change_attribute, CobolUnisysParser.ChangeLibraryAttributeContext
        ):
            res["attribute_type"] = "LIBRARY"
            library_attribute_name: CobolUnisysParser.LibraryAttributeNameContext = (
                change_attribute.libraryAttributeName()
            )

            # check library attribute name is literal or identifier
            cobol_word: CobolUnisysParser.CobolWordContext = (
                library_attribute_name.cobolWord()
            )

            if isinstance(cobol_word, CobolUnisysParser.CharDataKeywordContext):
                res["source_identifier"] = None
                res["source_literal"] = library_attribute_name.getText()

            else:
                res["source_identifier"] = library_attribute_name.getText()
                res["source_literal"] = None

            of_library_name = change_attribute.getChild(2)
            if isinstance(of_library_name, TerminalNode):
                library_name = get_original_code_content(
                    self.parser,
                    of_library_name.symbol.tokenIndex,
                    of_library_name.symbol.tokenIndex,
                )
            else:
                library_name = get_original_code_content(
                    self.parser,
                    of_library_name.start.tokenIndex,
                    of_library_name.stop.tokenIndex,
                )
            res["library_name"] = library_name

            source_option = get_original_code_content(
                self.parser,
                attribute_token.symbol.tokenIndex,
                change_attribute.getChild(2).stop.tokenIndex,
            )

            res["source_option"] = source_option

            library_value_option: CobolUnisysParser.LibraryValueOptionContext = (
                change_attribute.libraryValueOption()
            )

            target_identifier = library_value_option.identifier()
            target_literal = library_value_option.literal()

            res["target_identifier"] = (
                target_identifier.getText() if target_identifier else None
            )
            res["target_literal"] = target_literal.getText() if target_literal else None
            res["target_option"] = library_value_option.getText()

        return res

    def visitChangeStatement(self, ctx: CobolUnisysParser.ChangeStatementContext):
        res = self.assessChangeStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)

        return super().visitChangeStatement(ctx)

    def assessGoToStatement(self, ctx: CobolUnisysParser.GoToStatementContext):
        # Intialize
        tag = "GoToStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        goToStatementSimple = ctx.goToStatementSimple()
        if goToStatementSimple:
            res["procedure_name_1"] = goToStatementSimple.getText()
        # print(res)
        return res

    def visitGoToStatement(self, ctx: CobolUnisysParser.GoToStatementContext):
        res = self.assessGoToStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessIfStatement(self, ctx: CobolUnisysParser.IfStatementContext):
        # Intialize
        tag = "IfStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        # condition
        condition = ctx.condition()
        if condition:
            start_idx = condition.start.tokenIndex
            stop_idx = condition.stop.tokenIndex
            res["condition"] = get_original_code_content(
                self.parser, start_idx, stop_idx
            )
        # ifThen
        ifThen = ctx.ifThen()
        if ifThen:
            res["ifThen"] = []
            statement = ifThen.statement()
            if statement:
                for st in statement:
                    start_idx = st.start.tokenIndex
                    stop_idx = st.stop.tokenIndex
                    c = st.getChild(0)
                    type_ = type(c).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        res["ifThen"].append(f(c))

        # ifElse
        ifElse = ctx.ifElse()
        if ifElse:
            res["ifElse"] = []
            statement = ifElse.statement()
            if statement:
                for st in statement:
                    start_idx = st.start.tokenIndex
                    stop_idx = st.stop.tokenIndex
                    c = st.getChild(0)
                    type_ = type(c).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        res["ifElse"].append(f(c))

        return res

    def visitIfStatement(self, ctx: CobolUnisysParser.IfStatementContext):
        res = self.assessIfStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessInitializeStatement(
        self, ctx: CobolUnisysParser.InitializeStatementContext
    ):
        # Intialize
        tag = "InitializeStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        # identifier
        identifier = ctx.identifier()
        if identifier:
            res["identifier_1"] = []
            for i in identifier:
                # res["identifier_1"].append(i.getText())
                res["identifier_1"].append(
                    get_original_code_content(
                        self.parser, i.start.tokenIndex, i.stop.tokenIndex
                    )
                )
        # print(res)
        return res

    def visitInitializeStatement(
        self, ctx: CobolUnisysParser.InitializeStatementContext
    ):
        res = self.assessInitializeStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessInspectStatement(self, ctx: CobolUnisysParser.InspectStatementContext):
        # Intialize
        tag = "InspectStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )

        identifier = ctx.identifier()
        res["identifier"] = identifier.getText()

        inspect_phrase = ctx.getChild(2)

        if isinstance(inspect_phrase, CobolUnisysParser.InspectReplacingPhraseContext):
            inspect_replacing_phrase_dict = self.extract_inspect_replacing_phrase(
                inspect_phrase
            )
            res["phrase"] = inspect_replacing_phrase_dict

        elif isinstance(inspect_phrase, CobolUnisysParser.InspectTallyingPhraseContext):
            inspect_tallying_phrase_dict = self.extract_inspect_tallying(inspect_phrase)
            res["phrase"] = inspect_tallying_phrase_dict

        elif isinstance(
            inspect_phrase, CobolUnisysParser.InspectTallyingReplacingPhraseContext
        ):
            inspect_tallying_replacing_dict = self.extract_inspect_tallying_replacing(
                inspect_phrase
            )
            res["phrase"] = inspect_tallying_replacing_dict

        elif isinstance(
            inspect_phrase, CobolUnisysParser.InspectConvertingPhraseContext
        ):
            inspect_converting_phrase_dict = self.extract_inspect_converting_phrase(
                inspect_phrase
            )
            res["phrase"] = inspect_converting_phrase_dict

        return res

    def visitInspectStatement(self, ctx: CobolUnisysParser.InspectStatementContext):
        res = self.assessInspectStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def extract_inspect_converting_phrase(
        self,
        inspect_converting_phrase: CobolUnisysParser.InspectConvertingPhraseContext,
    ):
        inspect_converting_phrase_dict = {
            "converting_from_identifier": None,
            "converting_from_literal": None,
            "to": None,
            "before_after": [],
        }

        identifier = inspect_converting_phrase.identifier()
        inspect_converting_phrase_dict["converting_from_identifier"] = (
            identifier.getText() if identifier else None
        )

        literal = inspect_converting_phrase.literal()
        inspect_converting_phrase_dict["converting_from_literal"] = (
            literal.getText() if literal else None
        )

        inspect_to = inspect_converting_phrase.inspectTo()
        inspect_to_identifier = inspect_to.identifier()
        inspect_to_literal = inspect_to.literal()
        inspect_to_dict = {
            "to_identifier": (
                inspect_to_identifier.getText() if inspect_to_identifier else None
            ),
            "to_literal": inspect_to_literal.getText() if inspect_to_literal else None,
        }
        inspect_converting_phrase_dict["to"] = inspect_to_dict

        inspect_before_after_list = inspect_converting_phrase.inspectBeforeAfter()

        for inspect_before_after in inspect_before_after_list:
            inspect_before_after_dict = self.extract_inspect_before_after(
                inspect_before_after
            )
            inspect_converting_phrase_dict["before_after"].append(
                inspect_before_after_dict
            )

        return inspect_converting_phrase_dict

    def extract_inspect_tallying_replacing(
        self, inspect_phrase: CobolUnisysParser.InspectTallyingReplacingPhraseContext
    ):
        inspect_tallying_replacing_phrase_dict = {"tallying": [], "replacing": []}
        inspect_for_list = inspect_phrase.inspectFor()

        for inspect_for in inspect_for_list:
            inspect_for_dict = self.extract_inspect_for(inspect_for)
            inspect_tallying_replacing_phrase_dict["tallying"].append(inspect_for_dict)

        inspect_replacing_phrase_list = inspect_phrase.inspectReplacingPhrase()
        for inspect_replacing_phrase in inspect_replacing_phrase_list:
            inspect_replacing_phrase_dict = self.extract_inspect_replacing_phrase(
                inspect_replacing_phrase
            )
            inspect_tallying_replacing_phrase_dict["replacing"].append(
                inspect_replacing_phrase_dict
            )

        return inspect_tallying_replacing_phrase_dict

    def extract_inspect_replacing_phrase(
        self, inspect_phrase: CobolUnisysParser.InspectReplacingPhraseContext
    ):
        inspect_replacing_phrase_dict = {"replacements": []}

        for child in inspect_phrase.getChildren():
            if isinstance(child, CobolUnisysParser.InspectReplacingCharactersContext):
                inspect_by = child.inspectBy()
                identifier = inspect_by.identifier()
                literal = inspect_by.literal()
                inspect_replacing_characters_dict = {"by": None, "before_after": []}
                inspect_replacing_phrase_dict["replacements"].append(
                    inspect_replacing_characters_dict
                )

                inspect_by_dict = {
                    "by_identifier": identifier.getText() if identifier else None,
                    "by_literal": literal.getText() if literal else None,
                }

                inspect_replacing_characters_dict["by"] = inspect_by_dict

                inspect_before_after_list = child.inspectBeforeAfter()

                for inspect_before_after in inspect_before_after_list:
                    inspect_before_after_dict = self.extract_inspect_before_after(
                        inspect_before_after
                    )

                    inspect_replacing_characters_dict["before_after"].append(
                        inspect_before_after_dict
                    )
            elif isinstance(
                child, CobolUnisysParser.InspectReplacingAllLeadingsContext
            ):
                leading_type = child.getChild(0).getText().upper()
                inspect_replacing_all_leadings_dict = {
                    "leading_type": leading_type,
                    "replacements": [],
                }
                inspect_replacing_phrase_dict["replacements"].append(
                    inspect_replacing_all_leadings_dict
                )

                inspect_replacing_all_leading_list: List[
                    CobolUnisysParser.InspectReplacingAllLeadingContext
                ] = child.inspectReplacingAllLeading()
                for inspect_replacing_all_leading in inspect_replacing_all_leading_list:
                    replacing_identifier = inspect_replacing_all_leading.identifier()
                    replacing_literal = (
                        inspect_replacing_all_leading.literal()
                        or inspect_replacing_all_leading.figurativeConstant()
                    )

                    inspect_replacing_all_leading_dict = {
                        "replacing_identifier": (
                            replacing_identifier.getText()
                            if replacing_identifier
                            else None
                        ),
                        "replacing_literal": (
                            replacing_literal.getText() if replacing_literal else None
                        ),
                        "inspect_by": [],
                        "before_after": [],
                    }
                    inspect_replacing_all_leadings_dict["replacements"].append(
                        inspect_replacing_all_leading_dict
                    )

                    inspect_by_list = inspect_replacing_all_leading.inspectBy()
                    for inspect_by in inspect_by_list:
                        by_identifier = inspect_by.identifier()
                        by_literal = inspect_by.literal()

                        inspect_by_dict = {
                            "by_identifier": (
                                by_identifier.getText() if by_identifier else None
                            ),
                            "by_literal": (
                                by_literal.getText() if by_literal else None
                            ),
                        }

                        inspect_replacing_all_leading_dict["inspect_by"].append(
                            inspect_by_dict
                        )

                    inspect_before_after_list = (
                        inspect_replacing_all_leading.inspectBeforeAfter()
                    )
                    for inspect_before_after in inspect_before_after_list:
                        inspect_before_after_dict = self.extract_inspect_before_after(
                            inspect_before_after
                        )

                        inspect_replacing_all_leading_dict["before_after"].append(
                            inspect_before_after_dict
                        )
        return inspect_replacing_phrase_dict

    def extract_inspect_tallying(
        self, inspect_tallying: CobolUnisysParser.InspectTallyingPhraseContext
    ):
        inspect_tallying_phrase_dict = {"tallying": []}
        inspect_for_list: List[CobolUnisysParser.InspectForContext] = (
            inspect_tallying.inspectFor()
        )

        for inspect_for in inspect_for_list:
            inspect_for_dict = self.extract_inspect_for(inspect_for)
            inspect_tallying_phrase_dict["tallying"].append(inspect_for_dict)

        return inspect_tallying_phrase_dict

    def extract_inspect_for(self, inspect_for: CobolUnisysParser.InspectForContext):
        identifier = inspect_for.identifier()
        inspect_for_dict = {
            "identifier": identifier.getText(),
            "for_targets": [],
        }

        for child in inspect_for.getChildren():
            if isinstance(child, CobolUnisysParser.InspectCharactersContext):
                inspect_characters_dict = {"before_after": []}
                inspect_for_dict["for_targets"].append(inspect_characters_dict)

                inspect_before_after_list = child.inspectBeforeAfter()
                for inspect_before_after in inspect_before_after_list:
                    inspect_before_after_dict = self.extract_inspect_before_after(
                        inspect_before_after
                    )

                    inspect_characters_dict["before_after"].append(
                        inspect_before_after_dict
                    )
            elif isinstance(child, CobolUnisysParser.InspectAllLeadingsContext):
                leading_type = child.getChild(0).getText().upper()
                inspect_all_leadings_dict = {
                    "leading_type": leading_type,
                    "inspect_all_leading": [],
                }
                inspect_for_dict["for_targets"].append(inspect_all_leadings_dict)

                inspect_all_leading_list: List[
                    CobolUnisysParser.InspectAllLeadingContext
                ] = child.inspectAllLeading()

                for inspect_all_leading in inspect_all_leading_list:
                    inspect_all_leading_dict = {
                        "identifier": None,
                        "literal": None,
                        "before_after": [],
                    }
                    inspect_all_leadings_dict["inspect_all_leading"].append(
                        inspect_all_leading_dict
                    )

                    identifier = inspect_all_leading.identifier()
                    literal = inspect_all_leading.literal()

                    inspect_all_leading_dict["identifier"] = (
                        identifier.getText() if identifier else None
                    )
                    inspect_all_leading_dict["literal"] = (
                        literal.getText() if literal else None
                    )

                    inspect_before_after_list = inspect_all_leading.inspectBeforeAfter()
                    for inspect_before_after in inspect_before_after_list:
                        inspect_before_after_dict = self.extract_inspect_before_after(
                            inspect_before_after
                        )

                        inspect_all_leading_dict["before_after"].append(
                            inspect_before_after_dict
                        )

        return inspect_for_dict

    def extract_inspect_before_after(
        self, inspect_before_after: CobolUnisysParser.InspectBeforeAfterContext
    ):
        position = inspect_before_after.getChild(0).getText().upper()
        replacing_identifier = inspect_before_after.identifier()
        replacing_literal = inspect_before_after.literal()

        inspect_before_after_dict = {
            "position": position,
            "replacing_identifier": (
                replacing_identifier.getText() if replacing_identifier else None
            ),
            "replacing_literal": (
                replacing_literal.getText() if replacing_literal else None
            ),
        }

        return inspect_before_after_dict

    def assessMoveStatement(self, ctx: CobolUnisysParser.MoveStatementContext):
        # Intialize
        tag = "MoveStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )

        if ctx.ALL():
            res["move_option"] = "ALL"

        if ctx.ATTRIBUTE():
            res["move_option"] = "ATTRIBUTE"

        move_to_statement: Optional[CobolUnisysParser.MoveToStatementContext] = (
            ctx.moveToStatement()
        )

        if move_to_statement:
            res["move_type"] = "TO"

            move_to_sending_area: CobolUnisysParser.MoveToSendingAreaContext = (
                move_to_statement.moveToSendingArea()
            )
            res["move_from"] = get_original_code_content(
                self.parser,
                move_to_sending_area.start.tokenIndex,
                move_to_sending_area.stop.tokenIndex,
            )

            move_to_sending_area_child = move_to_sending_area.getChild(0)
            if isinstance(
                move_to_sending_area_child, CobolUnisysParser.IdentifierContext
            ):
                res["from_identifier"] = move_to_sending_area_child.getText()
            elif isinstance(
                move_to_sending_area_child, CobolUnisysParser.MoveAttributeClauseContext
            ):
                cobol_word = move_to_sending_area_child.cobolWord(1)
                if isinstance(
                    cobol_word.getChild(0), CobolUnisysParser.CharDataKeywordContext
                ):
                    res["from_literal"] = cobol_word.getText()
                else:
                    res["from_identifier"] = cobol_word.getText()
            else:
                res["from_literal"] = get_original_code_content(
                    self.parser,
                    move_to_sending_area_child.start.tokenIndex,
                    move_to_sending_area_child.stop.tokenIndex,
                )

            move_to_identifier_list = move_to_statement.identifier()
            res["move_to"] = ""
            res["to_identifiers"] = []
            for move_to_identifier in move_to_identifier_list:
                res["move_to"] += (
                    get_original_code_content(
                        self.parser,
                        move_to_identifier.start.tokenIndex,
                        move_to_identifier.stop.tokenIndex,
                    )
                    + " "
                )

                res["to_identifiers"].append(move_to_identifier.getText())
            res["move_to"] = res["move_to"].strip()

        elif isinstance(
            move_to_statement, CobolUnisysParser.MoveCorrespondingToStatementContext
        ):
            res["move_type"] = "CORRESPONDING"
            res["from_identifier"] = (
                move_to_statement.moveCorrespondingToSendingArea.getText()
            )
            res["move_from"] = (
                move_to_statement.moveCorrespondingToSendingArea.getText()
            )

            move_to_identifier_list = move_to_statement.identifier()
            res["move_to"] = ""
            res["to_identifiers"] = []
            for move_to_identifier in move_to_identifier_list:
                res["move_to"] += (
                    get_original_code_content(
                        self.parser,
                        move_to_identifier.start.tokenIndex,
                        move_to_identifier.stop.tokenIndex,
                    )
                    + " "
                )

                res["to_identifiers"].append(move_to_identifier.getText())

            res["move_to"] = res["move_to"].strip()

        return res

    def visitMoveStatement(self, ctx: CobolUnisysParser.MoveStatementContext):
        res = self.assessMoveStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessPerformStatement(self, ctx: CobolUnisysParser.PerformStatementContext):
        # Intialize
        res = {}
        res["tag"] = "PerformStatement"
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        sub_tags = []
        # performProcedureStatement
        performProcedureStatement = ctx.performProcedureStatement()
        if performProcedureStatement:
            procedureName = performProcedureStatement.procedureName()
            if len(procedureName) == 1:
                res["procedure_name_1"] = procedureName[0].getText()
            if len(procedureName) == 2:
                res["procedure_name_1"] = procedureName[0].getText()
                res["procedure_name_2"] = procedureName[1].getText()
                sub_tags.append("THRU")

            performType = performProcedureStatement.performType()

            perform_times = recursive_find_first_child_by_type(
                ctx, CobolUnisysParser.PerformTimesContext
            )

            perform_until = recursive_find_first_child_by_type(
                ctx, CobolUnisysParser.PerformUntilContext
            )

            perform_varying = recursive_find_first_child_by_type(
                ctx, CobolUnisysParser.PerformVaryingContext
            )

            if perform_times:
                res["loop_times"] = get_original_code_content(
                    self.parser,
                    perform_times.start.tokenIndex,
                    perform_times.stop.tokenIndex,
                )
                sub_tags.append("TIMES")

            if perform_until:
                condition = recursive_find_first_child_by_type(
                    perform_until,
                    CobolUnisysParser.ConditionContext,
                )
                res["condition"] = get_original_code_content(
                    self.parser,
                    condition.start.tokenIndex,
                    condition.stop.tokenIndex,
                )
                sub_tags.append("UNTIL")

            if perform_varying:
                perform_varying_clause = recursive_find_first_child_by_type(
                    perform_varying, CobolUnisysParser.PerformVaryingClauseContext
                )
                perform_varying_phrase = perform_varying_clause.getChild(1)
                varying_variable = perform_varying_phrase.getChild(0)
                res["varying_variable"] = get_original_code_content(
                    self.parser,
                    varying_variable.start.tokenIndex,
                    varying_variable.stop.tokenIndex,
                )

                from_phrase = perform_varying_phrase.getChild(1)
                res["varying_from"] = get_original_code_content(
                    self.parser,
                    from_phrase.getChild(1).start.tokenIndex,
                    from_phrase.getChild(1).stop.tokenIndex,
                )

                by_phrase = perform_varying_phrase.getChild(2)
                res["varying_by"] = get_original_code_content(
                    self.parser,
                    by_phrase.getChild(1).start.tokenIndex,
                    by_phrase.getChild(1).stop.tokenIndex,
                )

                sub_tags.append("VARYING")

        res["sub_tags"] = sub_tags

        # performInlineStatement
        performInlineStatement = ctx.performInlineStatement()
        if performInlineStatement:
            res["performInlineStatement"] = {}
            performType = performInlineStatement.performType()
            if performType:
                res["performInlineStatement"]["performType"] = (
                    get_original_code_content(
                        self.parser,
                        performType.start.tokenIndex,
                        performType.stop.tokenIndex,
                    )
                )
            statement = performInlineStatement.statement()
            if statement:
                res["performInlineStatement"]["statement"] = []
                for st in statement:
                    start_idx = st.start.tokenIndex
                    stop_idx = st.stop.tokenIndex
                    c = st.getChild(0)
                    type_ = type(c).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        res["performInlineStatement"]["statement"].append(f(c))

        return res

    def visitPerformStatement(self, ctx: CobolUnisysParser.PerformStatementContext):
        res = self.assessPerformStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessReadStatement(self, ctx: CobolUnisysParser.ReadStatementContext):
        # Intialize
        tag = "ReadStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        # fileName
        fileName = ctx.fileName()
        if fileName:
            res["fileName"] = fileName.getText()

        next_record = ctx.NEXT()

        res["next_record"] = True if next_record else False

        # readInto
        readInto = ctx.readInto()
        if readInto:
            # res["identifier_1"] = readInto.identifier().getText()
            res["read_into_identifier"] = get_original_code_content(
                self.parser,
                readInto.identifier().start.tokenIndex,
                readInto.identifier().stop.tokenIndex,
            )

        read_with = ctx.readWith()
        if read_with:
            res["read_with"] = get_original_code_content(
                self.parser,
                read_with.start.tokenIndex,
                read_with.stop.tokenIndex,
            ).upper()

        read_key = ctx.readKey()
        if read_key:
            res["read_key"] = get_original_code_content(
                self.parser,
                read_key.start.tokenIndex,
                read_key.stop.tokenIndex,
            )

        # invalidKeyPhrase
        invalidKeyPhrase = ctx.invalidKeyPhrase()
        if invalidKeyPhrase:
            res["invalid_key_phrase"] = []
            statement = invalidKeyPhrase.statement()
            if statement:
                for st in statement:
                    start_idx = st.start.tokenIndex
                    stop_idx = st.stop.tokenIndex
                    c = st.getChild(0)
                    type_ = type(c).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        res["invalid_key_phrase"].append(f(c))

        # notInvalidKeyPhrase
        notInvalidKeyPhrase = ctx.notInvalidKeyPhrase()
        if notInvalidKeyPhrase:
            res["not_invalid_key_phrase"] = []
            statement = notInvalidKeyPhrase.statement()
            if statement:
                for st in statement:
                    start_idx = st.start.tokenIndex
                    stop_idx = st.stop.tokenIndex
                    c = st.getChild(0)
                    type_ = type(c).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        res["not_invalid_key_phrase"].append(f(c))

        at_end_phrase = ctx.atEndPhrase()
        if at_end_phrase:
            res["at_end_phrase"] = []
            statement = at_end_phrase.statement()
            if statement:
                for st in statement:
                    start_idx = st.start.tokenIndex
                    stop_idx = st.stop.tokenIndex
                    c = st.getChild(0)
                    type_ = type(c).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        res["at_end_phrase"].append(f(c))

        not_at_end_phrase = ctx.notAtEndPhrase()
        if not_at_end_phrase:
            res["not_at_end_phrase"] = []
            statement = not_at_end_phrase.statement()
            if statement:
                for st in statement:
                    start_idx = st.start.tokenIndex
                    stop_idx = st.stop.tokenIndex
                    c = st.getChild(0)
                    type_ = type(c).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        res["not_at_end_phrase"].append(f(c))

        return res

    def visitReadStatement(self, ctx: CobolUnisysParser.ReadStatementContext):
        res = self.assessReadStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessRewriteStatement(self, ctx: CobolUnisysParser.RewriteStatementContext):
        # Intialize
        tag = "RewriteStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        # recordName
        recordName = ctx.recordName()
        if recordName:
            res["record_name"] = recordName.getText()
        # rewriteFrom
        rewriteFrom = ctx.rewriteFrom()
        if rewriteFrom:
            # res["record_name_1"] = rewriteFrom.identifier().getText()
            res["rewrite_from_identifier"] = get_original_code_content(
                self.parser,
                rewriteFrom.identifier().start.tokenIndex,
                rewriteFrom.identifier().stop.tokenIndex,
            )

        # invalidKeyPhrase
        invalidKeyPhrase = ctx.invalidKeyPhrase()
        if invalidKeyPhrase:
            res["invalid_key_phrase"] = []
            statement = invalidKeyPhrase.statement()
            if statement:
                for st in statement:
                    start_idx = st.start.tokenIndex
                    stop_idx = st.stop.tokenIndex
                    c = st.getChild(0)
                    type_ = type(c).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        res["invalid_key_phrase"].append(f(c))

        # notInvalidKeyPhrase
        notInvalidKeyPhrase = ctx.notInvalidKeyPhrase()
        if notInvalidKeyPhrase:
            res["not_invalid_key_phrase"] = []
            statement = notInvalidKeyPhrase.statement()
            if statement:
                for st in statement:
                    start_idx = st.start.tokenIndex
                    stop_idx = st.stop.tokenIndex
                    c = st.getChild(0)
                    type_ = type(c).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        res["not_invalid_key_phrase"].append(f(c))
        return res

    def visitRewriteStatement(self, ctx: CobolUnisysParser.RewriteStatementContext):
        res = self.assessRewriteStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessStringStatement(self, ctx: CobolUnisysParser.StringStatementContext):
        # Intialize
        tag = "StringStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        res["stringSendingPhrase"] = []
        res["destination_identifier"] = None
        res["pointer_name"] = None

        string_sending_phrase_list: List[
            CobolUnisysParser.StringSendingPhraseContext
        ] = ctx.stringSendingPhrase()

        for string_sending_phrase in string_sending_phrase_list:
            string_sending_phrase_dict = {
                "source_identifiers": [],
                "source_literals": [],
                "delimiter_identifier": None,
                "delimiter_literal": None,
                "for_identifier": None,
                "for_literal": None,
            }
            res["stringSendingPhrase"].append(string_sending_phrase_dict)

            string_sending_list: List[CobolUnisysParser.StringSendingContext] = (
                string_sending_phrase.stringSending()
            )
            for string_sending in string_sending_list:
                sending_identifier = string_sending.identifier()
                sending_literal = string_sending.literal()

                if sending_identifier:
                    string_sending_phrase_dict["source_identifiers"].append(
                        sending_identifier.getText()
                    )

                if sending_literal:
                    string_sending_phrase_dict["source_literals"].append(
                        sending_literal.getText()
                    )

            string_delimited_by_phrase: Optional[
                CobolUnisysParser.StringDelimitedByPhraseContext
            ] = string_sending_phrase.stringDelimitedByPhrase()

            if string_delimited_by_phrase:
                delimiter_identifier = string_delimited_by_phrase.identifier()
                delimiter_literal = (
                    string_delimited_by_phrase.literal()
                    or string_delimited_by_phrase.SIZE()
                )

                string_sending_phrase_dict["delimiter_identifier"] = (
                    delimiter_identifier.getText() if delimiter_identifier else None
                )

                string_sending_phrase_dict["delimiter_literal"] = (
                    delimiter_literal.getText() if delimiter_literal else None
                )

            string_for_phrase: Optional[CobolUnisysParser.StringForPhraseContext] = (
                string_sending_phrase.stringForPhrase()
            )

            if string_for_phrase:
                identifier = string_for_phrase.identifier()
                literal = string_for_phrase.literal()

                string_sending_phrase_dict["for_identifier"] = (
                    identifier.getText() if identifier else None
                )
                string_sending_phrase_dict["for_literal"] = (
                    literal.getText() if literal else None
                )

        string_into_phrase: CobolUnisysParser.StringIntoPhraseContext = (
            ctx.stringIntoPhrase()
        )

        into_identifier = string_into_phrase.identifier()
        res["destination_identifier"] = into_identifier.getText()

        string_pointer_phrase: Optional[
            CobolUnisysParser.StringWithPointerPhraseContext
        ] = ctx.stringWithPointerPhrase()

        if string_pointer_phrase:
            pointer_qualified_data_name = string_pointer_phrase.qualifiedDataName()

            res["pointer_name"] = pointer_qualified_data_name.getText()

        res["on_overflow_phrase"] = []
        on_overflow_phrase = ctx.onOverflowPhrase()
        if on_overflow_phrase:
            statements = on_overflow_phrase.statement()
            for statement in statements:
                child = statement.getChild(0)
                type_ = type(child).__name__
                if type_ in self.func:
                    f = self.func[type_]
                    res["on_overflow_phrase"].append(f(child))

        res["not_on_overflow_phrase"] = []
        not_on_overflow_phrase = ctx.notOnOverflowPhrase()
        if not_on_overflow_phrase:
            statements = not_on_overflow_phrase.statement()
            for statement in statements:
                child = statement.getChild(0)
                type_ = type(child).__name__
                if type_ in self.func:
                    f = self.func[type_]
                    res["not_on_overflow_phrase"].append(f(child))

        return res

    def visitStringStatement(self, ctx: CobolUnisysParser.StringStatementContext):
        res = self.assessStringStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessSubtractStatement(self, ctx: CobolUnisysParser.SubtractStatementContext):
        # Intialize
        tag = "SubtractStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        res["subtrahends"] = []
        res["minuends"] = []
        res["results"] = []

        subtract_phrase = ctx.getChild(1)

        if isinstance(subtract_phrase, CobolUnisysParser.SubtractFromStatementContext):

            subtract_from_statement = subtract_phrase
            subtrahend_list = subtract_from_statement.subtractSubtrahend()

            for subtrahend in subtrahend_list:
                subtrahend = subtrahend.getChild(0)
                if isinstance(subtrahend, CobolUnisysParser.IdentifierContext):
                    res["subtrahends"].append(
                        {"identifier": subtrahend.getText(), "literal": None}
                    )
                else:
                    res["subtrahends"].append(
                        {"identifier": None, "literal": subtrahend.getText()}
                    )

            minuend_list = subtract_from_statement.subtractMinuend()

            for minuend in minuend_list:
                res["minuends"].append(
                    {"identifier": minuend.identifier().getText(), "literal": None}
                )
                res["results"].append(
                    {
                        "identifier": minuend.identifier().getText(),
                        "is_rounded": minuend.ROUNDED() is not None,
                    }
                )

        elif isinstance(
            subtract_phrase, CobolUnisysParser.SubtractFromGivingStatementContext
        ):
            subtract_from_statement = subtract_phrase
            subtrahend_list = subtract_from_statement.subtractSubtrahend()

            for subtrahend in subtrahend_list:
                subtrahend = subtrahend.getChild(0)
                if isinstance(subtrahend, CobolUnisysParser.IdentifierContext):
                    res["subtrahends"].append(
                        {"identifier": subtrahend.getText(), "literal": None}
                    )
                else:
                    res["subtrahends"].append(
                        {"identifier": None, "literal": subtrahend.getText()}
                    )

            minuend_giving = subtract_from_statement.subtractMinuendGiving()

            res["minuends"].append(
                {
                    "identifier": (
                        minuend_giving.identifier().getText()
                        if minuend_giving.identifier()
                        else None
                    ),
                    "literal": (
                        minuend_giving.getText()
                        if minuend_giving.literal()
                        or minuend_giving.figurativeConstant()
                        else None
                    ),
                }
            )

            subtract_giving_list = subtract_from_statement.subtractGiving()

            for subtract_giving in subtract_giving_list:
                res["results"].append(
                    {
                        "identifier": subtract_giving.identifier().getText(),
                        "is_rounded": subtract_giving.ROUNDED() is not None,
                    }
                )

        elif isinstance(
            subtract_phrase, CobolUnisysParser.SubtractCorrespondingStatementContext
        ):
            subtract_corresponding_statement = subtract_phrase
            qualified_data_name = subtract_corresponding_statement.qualifiedDataName()
            res["subtrahends"].append(
                {
                    "identifier": get_original_code_content(
                        self.parser,
                        qualified_data_name.start.tokenIndex,
                        qualified_data_name.stop.tokenIndex,
                    ),
                    "literal": None,
                }
            )

            subtract_minuend_corresponding = (
                subtract_corresponding_statement.subtractMinuendCorresponding()
            )
            res["minuends"].append(
                {
                    "identifier": get_original_code_content(
                        self.parser,
                        subtract_minuend_corresponding.start.tokenIndex,
                        subtract_minuend_corresponding.stop.tokenIndex,
                    ),
                    "literal": None,
                }
            )
            res["results"].append(
                {
                    "identifier": get_original_code_content(
                        self.parser,
                        subtract_minuend_corresponding.start.tokenIndex,
                        subtract_minuend_corresponding.stop.tokenIndex,
                    ),
                    "is_rounded": subtract_minuend_corresponding.ROUNDED() is not None,
                }
            )

        res["on_size_error_phrase"] = []
        on_size_error_phrase = ctx.onSizeErrorPhrase()
        if on_size_error_phrase:
            statements = on_size_error_phrase.statement()
            for statement in statements:
                child = statement.getChild(0)
                type_ = type(child).__name__
                if type_ in self.func:
                    f = self.func[type_]
                    res["on_size_error_phrase"].append(f(child))

        res["not_on_size_error_phrase"] = []
        not_on_size_error_phrase = ctx.notOnSizeErrorPhrase()
        if not_on_size_error_phrase:
            statements = not_on_size_error_phrase.statement()
            for statement in statements:
                child = statement.getChild(0)
                type_ = type(child).__name__
                if type_ in self.func:
                    f = self.func[type_]
                    res["not_on_size_error_phrase"].append(f(child))

        return res

    def visitSubtractStatement(self, ctx: CobolUnisysParser.SubtractStatementContext):
        res = self.assessSubtractStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)
        # print(res)
        return self.visitChildren(ctx)

    def assessSetStatement(self, ctx: CobolUnisysParser.SetStatementContext):
        # Intialize
        tag = "SetStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        # Get all children of context
        children = ctx.getChildren()
        children = [type(c) for c in children]
        # SetTo
        if CobolUnisysParser.SetToStatementContext in children:
            res["setToStatement"] = []
            setToStatement = ctx.setToStatement()
            for s in setToStatement:
                # init
                r = {}
                # setTo
                setTo = s.setTo()
                if setTo:
                    r["identifier_1"] = []
                    for c in setTo:
                        # r["identifier_1"].append(c.getText())
                        r["identifier_1"].append(
                            get_original_code_content(
                                self.parser, c.start.tokenIndex, c.stop.tokenIndex
                            )
                        )
                # setToValue
                setToValue = s.setToValue()
                if setToValue:
                    setToValue: CobolUnisysParser.SetToValueContext = setToValue[0]
                    setToIdentifier = setToValue.identifier()
                    if setToIdentifier:
                        r["identifier_2"] = get_original_code_content(
                            self.parser,
                            setToValue.start.tokenIndex,
                            setToValue.stop.tokenIndex,
                        )
                    else:
                        setToLiteral = setToValue.getChild(0)

                        if isinstance(setToLiteral, TerminalNode):
                            r["literal_2"] = get_original_code_content(
                                self.parser,
                                setToLiteral.symbol.tokenIndex,
                                setToLiteral.symbol.tokenIndex,
                            )
                        else:
                            r["literal_2"] = get_original_code_content(
                                self.parser,
                                setToLiteral.start.tokenIndex,
                                setToLiteral.stop.tokenIndex,
                            )
                    # r["identifier_2"] = []
                    # for c in setToValue:
                    #     # r["identifier_2"].append(c.getText())
                    #     r["identifier_2"].append(
                    #         get_original_code_content(
                    #             self.parser, c.start.tokenIndex, c.stop.tokenIndex
                    #         )
                    #     )
                # collect
                res["setToStatement"].append(r)

        return res

    def visitSetStatement(self, ctx: CobolUnisysParser.SetStatementContext):
        res = self.assessSetStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    def assessOpenStatement(self, ctx: CobolUnisysParser.OpenStatementContext):
        # Intialize
        tag = "OpenStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        # Get all children of context
        children = ctx.getChildren()

        res["open_files"] = []

        for child in children:
            if isinstance(child, CobolUnisysParser.OpenInputStatementContext):
                open_inputs = child.openInput()
                for open_input in open_inputs:
                    file_name = open_input.fileName()
                    res["open_files"].append(
                        {
                            "file_name": file_name.getText(),
                            "open_type": "INPUT",
                            "on_exception_clause": [],
                        }
                    )

            elif isinstance(child, CobolUnisysParser.OpenOutputStatementContext):
                open_outputs = child.openOutput()
                for open_output in open_outputs:
                    file_name = open_output.fileName()
                    res["open_files"].append(
                        {
                            "file_name": file_name.getText(),
                            "open_type": "OUTPUT",
                            "on_exception_clause": [],
                        }
                    )

            elif isinstance(child, CobolUnisysParser.OpenIOStatementContext):
                file_names = child.fileName()
                for file_name in file_names:
                    res["open_files"].append(
                        {
                            "file_name": file_name.getText(),
                            "open_type": "IO",
                            "on_exception_clause": [],
                        }
                    )
            elif isinstance(child, CobolUnisysParser.OpenInquiryContext):
                file_name = child.qualifiedDataName()
                on_exception_statements = []
                on_exception_clause = child.onExceptionClause()
                if on_exception_clause:
                    statements = on_exception_clause.statement()
                    for statement in statements:
                        child = statement.getChild(0)
                        type_ = type(child).__name__
                        if type_ in self.func:
                            f = self.func[type_]
                            on_exception_statements.append(f(child))

                res["open_files"].append(
                    {
                        "file_name": file_name.getText(),
                        "open_type": "INQUIRY",
                        "on_exception_clause": on_exception_statements,
                    }
                )

            elif isinstance(child, CobolUnisysParser.OpenExtendStatementContext):
                file_names = child.fileName()
                for file_name in file_names:
                    res["open_files"].append(
                        {
                            "file_name": file_name.getText(),
                            "open_type": "EXTEND",
                            "on_exception_clause": [],
                        }
                    )

            elif isinstance(child, CobolUnisysParser.OpenUpdateStatementContext):
                file_name = child.qualifiedDataName()

                on_exception_clause = child.onExceptionClause()
                on_exception_statements = []
                if on_exception_clause:
                    statements = on_exception_clause.statement()
                    for statement in statements:
                        child = statement.getChild(0)
                        type_ = type(child).__name__
                        if type_ in self.func:
                            f = self.func[type_]
                            on_exception_statements.append(f(child))

                res["open_files"].append(
                    {
                        "file_name": file_name.getText(),
                        "open_type": "UPDATE",
                        "on_exception_clause": on_exception_statements,
                    }
                )

        return res

    def visitOpenStatement(self, ctx: CobolUnisysParser.OpenStatementContext):
        res = self.assessOpenStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#programUnit.
    def visitProgramUnit(self, ctx: CobolUnisysParser.ProgramUnitContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#endProgramStatement.
    def visitEndProgramStatement(
        self, ctx: CobolUnisysParser.EndProgramStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#identificationDivision.
    def visitIdentificationDivision(
        self, ctx: CobolUnisysParser.IdentificationDivisionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#identificationDivisionBody.
    def visitIdentificationDivisionBody(
        self, ctx: CobolUnisysParser.IdentificationDivisionBodyContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#programIdParagraph.
    def visitProgramIdParagraph(self, ctx: CobolUnisysParser.ProgramIdParagraphContext):
        program_name = recursive_find_first_child_by_type(
            ctx, CobolUnisysParser.ProgramNameContext
        )

        if program_name:
            self.program_id = program_name.getText()

        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#author_name.
    def visitAuthor_name(self, ctx: CobolUnisysParser.Author_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#authorParagraph.
    def visitAuthorParagraph(self, ctx: CobolUnisysParser.AuthorParagraphContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#installationParagraph.
    def visitInstallationParagraph(
        self, ctx: CobolUnisysParser.InstallationParagraphContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dateWrittenParagraph.
    def visitDateWrittenParagraph(
        self, ctx: CobolUnisysParser.DateWrittenParagraphContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dateCompiledParagraph.
    def visitDateCompiledParagraph(
        self, ctx: CobolUnisysParser.DateCompiledParagraphContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#securityParagraph.
    def visitSecurityParagraph(self, ctx: CobolUnisysParser.SecurityParagraphContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#remarksParagraph.
    def visitRemarksParagraph(self, ctx: CobolUnisysParser.RemarksParagraphContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#environmentDivision.
    def visitEnvironmentDivision(
        self, ctx: CobolUnisysParser.EnvironmentDivisionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#environmentDivisionBody.
    def visitEnvironmentDivisionBody(
        self, ctx: CobolUnisysParser.EnvironmentDivisionBodyContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#configurationSection.
    def visitConfigurationSection(
        self, ctx: CobolUnisysParser.ConfigurationSectionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#configurationSectionParagraph.
    def visitConfigurationSectionParagraph(
        self, ctx: CobolUnisysParser.ConfigurationSectionParagraphContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#sourceComputerParagraph.
    def visitSourceComputerParagraph(
        self, ctx: CobolUnisysParser.SourceComputerParagraphContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#objectComputerParagraph.
    def visitObjectComputerParagraph(
        self, ctx: CobolUnisysParser.ObjectComputerParagraphContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#objectComputerClause.
    def visitObjectComputerClause(
        self, ctx: CobolUnisysParser.ObjectComputerClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#memorySizeClause.
    def visitMemorySizeClause(self, ctx: CobolUnisysParser.MemorySizeClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#diskSizeClause.
    def visitDiskSizeClause(self, ctx: CobolUnisysParser.DiskSizeClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#collatingSequenceClause.
    def visitCollatingSequenceClause(
        self, ctx: CobolUnisysParser.CollatingSequenceClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#collatingSequenceClauseAlphanumeric.
    def visitCollatingSequenceClauseAlphanumeric(
        self, ctx: CobolUnisysParser.CollatingSequenceClauseAlphanumericContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#collatingSequenceClauseNational.
    def visitCollatingSequenceClauseNational(
        self, ctx: CobolUnisysParser.CollatingSequenceClauseNationalContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#segmentLimitClause.
    def visitSegmentLimitClause(self, ctx: CobolUnisysParser.SegmentLimitClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#characterSetClause.
    def visitCharacterSetClause(self, ctx: CobolUnisysParser.CharacterSetClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#specialNamesParagraph.
    def visitSpecialNamesParagraph(
        self, ctx: CobolUnisysParser.SpecialNamesParagraphContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#specialNameClause.
    def visitSpecialNameClause(self, ctx: CobolUnisysParser.SpecialNameClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#alphabetClause.
    def visitAlphabetClause(self, ctx: CobolUnisysParser.AlphabetClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#alphabetClauseFormat1.
    def visitAlphabetClauseFormat1(
        self, ctx: CobolUnisysParser.AlphabetClauseFormat1Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#alphabetLiterals.
    def visitAlphabetLiterals(self, ctx: CobolUnisysParser.AlphabetLiteralsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#alphabetThrough.
    def visitAlphabetThrough(self, ctx: CobolUnisysParser.AlphabetThroughContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#alphabetAlso.
    def visitAlphabetAlso(self, ctx: CobolUnisysParser.AlphabetAlsoContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#alphabetClauseFormat2.
    def visitAlphabetClauseFormat2(
        self, ctx: CobolUnisysParser.AlphabetClauseFormat2Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#channelClause.
    def visitChannelClause(self, ctx: CobolUnisysParser.ChannelClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#classClause.
    def visitClassClause(self, ctx: CobolUnisysParser.ClassClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#classClauseThrough.
    def visitClassClauseThrough(self, ctx: CobolUnisysParser.ClassClauseThroughContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#classClauseFrom.
    def visitClassClauseFrom(self, ctx: CobolUnisysParser.ClassClauseFromContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#classClauseTo.
    def visitClassClauseTo(self, ctx: CobolUnisysParser.ClassClauseToContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#currencySignClause.
    def visitCurrencySignClause(self, ctx: CobolUnisysParser.CurrencySignClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#decimalPointClause.
    def visitDecimalPointClause(self, ctx: CobolUnisysParser.DecimalPointClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#defaultComputationalSignClause.
    def visitDefaultComputationalSignClause(
        self, ctx: CobolUnisysParser.DefaultComputationalSignClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#defaultDisplaySignClause.
    def visitDefaultDisplaySignClause(
        self, ctx: CobolUnisysParser.DefaultDisplaySignClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#environmentSwitchNameClause.
    def visitEnvironmentSwitchNameClause(
        self, ctx: CobolUnisysParser.EnvironmentSwitchNameClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#environmentSwitchNameSpecialNamesStatusPhrase.
    def visitEnvironmentSwitchNameSpecialNamesStatusPhrase(
        self,
        ctx: CobolUnisysParser.EnvironmentSwitchNameSpecialNamesStatusPhraseContext,
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#odtClause.
    def visitOdtClause(self, ctx: CobolUnisysParser.OdtClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reserveNetworkClause.
    def visitReserveNetworkClause(
        self, ctx: CobolUnisysParser.ReserveNetworkClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#symbolicCharactersClause.
    def visitSymbolicCharactersClause(
        self, ctx: CobolUnisysParser.SymbolicCharactersClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#symbolicCharacters.
    def visitSymbolicCharacters(self, ctx: CobolUnisysParser.SymbolicCharactersContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#inputOutputSection.
    def visitInputOutputSection(self, ctx: CobolUnisysParser.InputOutputSectionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#inputOutputSectionParagraph.
    def visitInputOutputSectionParagraph(
        self, ctx: CobolUnisysParser.InputOutputSectionParagraphContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#fileControlParagraph.
    def visitFileControlParagraph(
        self, ctx: CobolUnisysParser.FileControlParagraphContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#fileControlEntry.
    def visitFileControlEntry(self, ctx: CobolUnisysParser.FileControlEntryContext):
        select_clause = recursive_find_first_child_by_type(
            ctx, CobolUnisysParser.SelectClauseContext
        )

        if select_clause is None:
            raise ValueError(
                f"Select clause of statement '{ctx.getText()}' is missing."
            )

        file_name = recursive_find_first_child_by_type(
            select_clause, CobolUnisysParser.FileNameContext
        )

        if file_name is None:
            raise ValueError(
                f"File name in select clause of statement'{ctx.getText()}' is missing."
            )

        assignment_name = recursive_find_first_child_by_type(
            ctx, CobolUnisysParser.AssignmentNameContext
        )

        if assignment_name is None:
            # raise ValueError(
            #     f"Assignment name in select clause of statement'{ctx.getText()}' is missing."
            # )
            assignment_name = ""
        else:
            assignment_name = assignment_name.getText()

        file_control = FileControlEntry(
            file_name=file_name.getText(),
            assignment_name=assignment_name,
            code_content=get_original_code_content(
                self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex
            ),
            access_mode="",
        )

        self.file_control_list.append(file_control)

        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#selectClause.
    def visitSelectClause(self, ctx: CobolUnisysParser.SelectClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#fileControlClause.
    def visitFileControlClause(self, ctx: CobolUnisysParser.FileControlClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#assignClause.
    def visitAssignClause(self, ctx: CobolUnisysParser.AssignClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reserveClause.
    def visitReserveClause(self, ctx: CobolUnisysParser.ReserveClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#organizationClause.
    def visitOrganizationClause(self, ctx: CobolUnisysParser.OrganizationClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#paddingCharacterClause.
    def visitPaddingCharacterClause(
        self, ctx: CobolUnisysParser.PaddingCharacterClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#recordDelimiterClause.
    def visitRecordDelimiterClause(
        self, ctx: CobolUnisysParser.RecordDelimiterClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#accessModeClause.
    def visitAccessModeClause(self, ctx: CobolUnisysParser.AccessModeClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#recordKeyClause.
    def visitRecordKeyClause(self, ctx: CobolUnisysParser.RecordKeyClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#alternateRecordKeyClause.
    def visitAlternateRecordKeyClause(
        self, ctx: CobolUnisysParser.AlternateRecordKeyClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#passwordClause.
    def visitPasswordClause(self, ctx: CobolUnisysParser.PasswordClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#fileStatusClause.
    def visitFileStatusClause(self, ctx: CobolUnisysParser.FileStatusClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#relativeKeyClause.
    def visitRelativeKeyClause(self, ctx: CobolUnisysParser.RelativeKeyClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#ioControlParagraph.
    def visitIoControlParagraph(self, ctx: CobolUnisysParser.IoControlParagraphContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#ioControlClause.
    def visitIoControlClause(self, ctx: CobolUnisysParser.IoControlClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#rerunClause.
    def visitRerunClause(self, ctx: CobolUnisysParser.RerunClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#rerunEveryRecords.
    def visitRerunEveryRecords(self, ctx: CobolUnisysParser.RerunEveryRecordsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#rerunEveryOf.
    def visitRerunEveryOf(self, ctx: CobolUnisysParser.RerunEveryOfContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#rerunEveryClock.
    def visitRerunEveryClock(self, ctx: CobolUnisysParser.RerunEveryClockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#sameClause.
    def visitSameClause(self, ctx: CobolUnisysParser.SameClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#multipleFileClause.
    def visitMultipleFileClause(self, ctx: CobolUnisysParser.MultipleFileClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#multipleFilePosition.
    def visitMultipleFilePosition(
        self, ctx: CobolUnisysParser.MultipleFilePositionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#commitmentControlClause.
    def visitCommitmentControlClause(
        self, ctx: CobolUnisysParser.CommitmentControlClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataDivision.
    def visitDataDivision(self, ctx: CobolUnisysParser.DataDivisionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataDivisionSection.
    def visitDataDivisionSection(
        self, ctx: CobolUnisysParser.DataDivisionSectionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#fileSection.
    def visitFileSection(self, ctx: CobolUnisysParser.FileSectionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#fileDescriptionEntry.
    def visitFileDescriptionEntry(
        self, ctx: CobolUnisysParser.FileDescriptionEntryContext
    ):
        code_content = get_original_code_content(
            self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex
        )

        file_name = recursive_find_first_child_by_type(
            ctx, CobolUnisysParser.FileNameContext
        )

        if file_name is None:
            raise ValueError(
                f"File name is missing for FD statement {get_original_code_content(self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)}"
            )

        data_description_entries = find_all_children_by_type(
            ctx, CobolUnisysParser.DataDescriptionEntryContext
        )

        variables = []
        copybooks = []

        for entry in data_description_entries:
            entry = entry.getChild(0)

            # copy statement
            if isinstance(entry, CobolUnisysParser.CopyStatementContext):
                copy_source = recursive_find_first_child_by_type(
                    ctx, CobolUnisysParser.CopySourceContext
                )

                if copy_source is None:
                    raise ValueError(
                        f"File name of COPY statement {get_original_code_content(self.parser, entry.start.tokenIndex, entry.stop.tokenIndex)}"
                    )

                copy_name = copy_source.getChild(0)

                replace_clauses = find_all_children_by_type(
                    entry, CobolUnisysParser.ReplaceClauseContext
                )

                replace_list = []

                for replace_clause in replace_clauses:
                    replaceable = replace_clause.getChild(0)
                    replacement = replace_clause.getChild(2)

                    replace = CopybookReplace(
                        replaceable=replaceable.getText(),
                        replacement=replacement.getText(),
                    )
                    replace_list.append(replace)

                copybook = ImportedCopybook(
                    copybook_name=copy_name.getText(),
                    line_number=copy_source.start.line,
                    replacing=replace_list,
                )

                copybooks.append(copybook)
                continue

            # variable definition
            variable = extract_cobol_variable(entry)

            variables.append(variable)

        fd = FileDescriptionEntry(
            file_name=file_name.getText(),
            code_content=code_content,
            variables=variables,
            copybooks=copybooks,
        )

        self.file_description_list.append(fd)

        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#fileDescriptionEntryClause.
    def visitFileDescriptionEntryClause(
        self, ctx: CobolUnisysParser.FileDescriptionEntryClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#externalClause.
    def visitExternalClause(self, ctx: CobolUnisysParser.ExternalClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#globalClause.
    def visitGlobalClause(self, ctx: CobolUnisysParser.GlobalClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#blockContainsClause.
    def visitBlockContainsClause(
        self, ctx: CobolUnisysParser.BlockContainsClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#blockContainsTo.
    def visitBlockContainsTo(self, ctx: CobolUnisysParser.BlockContainsToContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#recordContainsClause.
    def visitRecordContainsClause(
        self, ctx: CobolUnisysParser.RecordContainsClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#recordContainsClauseFormat1.
    def visitRecordContainsClauseFormat1(
        self, ctx: CobolUnisysParser.RecordContainsClauseFormat1Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#recordContainsClauseFormat2.
    def visitRecordContainsClauseFormat2(
        self, ctx: CobolUnisysParser.RecordContainsClauseFormat2Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#recordContainsClauseFormat3.
    def visitRecordContainsClauseFormat3(
        self, ctx: CobolUnisysParser.RecordContainsClauseFormat3Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#recordContainsTo.
    def visitRecordContainsTo(self, ctx: CobolUnisysParser.RecordContainsToContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#labelRecordsClause.
    def visitLabelRecordsClause(self, ctx: CobolUnisysParser.LabelRecordsClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#valueOfClause.
    def visitValueOfClause(self, ctx: CobolUnisysParser.ValueOfClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#valuePair.
    def visitValuePair(self, ctx: CobolUnisysParser.ValuePairContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataRecordsClause.
    def visitDataRecordsClause(self, ctx: CobolUnisysParser.DataRecordsClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#linageClause.
    def visitLinageClause(self, ctx: CobolUnisysParser.LinageClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#linageAt.
    def visitLinageAt(self, ctx: CobolUnisysParser.LinageAtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#linageFootingAt.
    def visitLinageFootingAt(self, ctx: CobolUnisysParser.LinageFootingAtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#linageLinesAtTop.
    def visitLinageLinesAtTop(self, ctx: CobolUnisysParser.LinageLinesAtTopContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#linageLinesAtBottom.
    def visitLinageLinesAtBottom(
        self, ctx: CobolUnisysParser.LinageLinesAtBottomContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#recordingModeClause.
    def visitRecordingModeClause(
        self, ctx: CobolUnisysParser.RecordingModeClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#codeSetClause.
    def visitCodeSetClause(self, ctx: CobolUnisysParser.CodeSetClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportClause.
    def visitReportClause(self, ctx: CobolUnisysParser.ReportClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataBaseSection.
    def visitDataBaseSection(self, ctx: CobolUnisysParser.DataBaseSectionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataBaseSectionEntry.
    def visitDataBaseSectionEntry(
        self, ctx: CobolUnisysParser.DataBaseSectionEntryContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#workingStorageSection.
    def visitWorkingStorageSection(
        self, ctx: CobolUnisysParser.WorkingStorageSectionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#linkageSection.
    def visitLinkageSection(self, ctx: CobolUnisysParser.LinkageSectionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#communicationSection.
    def visitCommunicationSection(
        self, ctx: CobolUnisysParser.CommunicationSectionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#communicationDescriptionEntry.
    def visitCommunicationDescriptionEntry(
        self, ctx: CobolUnisysParser.CommunicationDescriptionEntryContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#communicationDescriptionEntryFormat1.
    def visitCommunicationDescriptionEntryFormat1(
        self, ctx: CobolUnisysParser.CommunicationDescriptionEntryFormat1Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#communicationDescriptionEntryFormat2.
    def visitCommunicationDescriptionEntryFormat2(
        self, ctx: CobolUnisysParser.CommunicationDescriptionEntryFormat2Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#communicationDescriptionEntryFormat3.
    def visitCommunicationDescriptionEntryFormat3(
        self, ctx: CobolUnisysParser.CommunicationDescriptionEntryFormat3Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#destinationCountClause.
    def visitDestinationCountClause(
        self, ctx: CobolUnisysParser.DestinationCountClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#destinationTableClause.
    def visitDestinationTableClause(
        self, ctx: CobolUnisysParser.DestinationTableClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#endKeyClause.
    def visitEndKeyClause(self, ctx: CobolUnisysParser.EndKeyClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#errorKeyClause.
    def visitErrorKeyClause(self, ctx: CobolUnisysParser.ErrorKeyClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#messageCountClause.
    def visitMessageCountClause(self, ctx: CobolUnisysParser.MessageCountClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#messageDateClause.
    def visitMessageDateClause(self, ctx: CobolUnisysParser.MessageDateClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#messageTimeClause.
    def visitMessageTimeClause(self, ctx: CobolUnisysParser.MessageTimeClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#statusKeyClause.
    def visitStatusKeyClause(self, ctx: CobolUnisysParser.StatusKeyClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#symbolicDestinationClause.
    def visitSymbolicDestinationClause(
        self, ctx: CobolUnisysParser.SymbolicDestinationClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#symbolicQueueClause.
    def visitSymbolicQueueClause(
        self, ctx: CobolUnisysParser.SymbolicQueueClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#symbolicSourceClause.
    def visitSymbolicSourceClause(
        self, ctx: CobolUnisysParser.SymbolicSourceClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#symbolicTerminalClause.
    def visitSymbolicTerminalClause(
        self, ctx: CobolUnisysParser.SymbolicTerminalClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#symbolicSubQueueClause.
    def visitSymbolicSubQueueClause(
        self, ctx: CobolUnisysParser.SymbolicSubQueueClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#textLengthClause.
    def visitTextLengthClause(self, ctx: CobolUnisysParser.TextLengthClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#localStorageSection.
    def visitLocalStorageSection(
        self, ctx: CobolUnisysParser.LocalStorageSectionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenSection.
    def visitScreenSection(self, ctx: CobolUnisysParser.ScreenSectionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionEntry.
    def visitScreenDescriptionEntry(
        self, ctx: CobolUnisysParser.ScreenDescriptionEntryContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionBlankClause.
    def visitScreenDescriptionBlankClause(
        self, ctx: CobolUnisysParser.ScreenDescriptionBlankClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionBellClause.
    def visitScreenDescriptionBellClause(
        self, ctx: CobolUnisysParser.ScreenDescriptionBellClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionBlinkClause.
    def visitScreenDescriptionBlinkClause(
        self, ctx: CobolUnisysParser.ScreenDescriptionBlinkClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionEraseClause.
    def visitScreenDescriptionEraseClause(
        self, ctx: CobolUnisysParser.ScreenDescriptionEraseClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionLightClause.
    def visitScreenDescriptionLightClause(
        self, ctx: CobolUnisysParser.ScreenDescriptionLightClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionGridClause.
    def visitScreenDescriptionGridClause(
        self, ctx: CobolUnisysParser.ScreenDescriptionGridClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionReverseVideoClause.
    def visitScreenDescriptionReverseVideoClause(
        self, ctx: CobolUnisysParser.ScreenDescriptionReverseVideoClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionUnderlineClause.
    def visitScreenDescriptionUnderlineClause(
        self, ctx: CobolUnisysParser.ScreenDescriptionUnderlineClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionSizeClause.
    def visitScreenDescriptionSizeClause(
        self, ctx: CobolUnisysParser.ScreenDescriptionSizeClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionLineClause.
    def visitScreenDescriptionLineClause(
        self, ctx: CobolUnisysParser.ScreenDescriptionLineClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionColumnClause.
    def visitScreenDescriptionColumnClause(
        self, ctx: CobolUnisysParser.ScreenDescriptionColumnClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionForegroundColorClause.
    def visitScreenDescriptionForegroundColorClause(
        self, ctx: CobolUnisysParser.ScreenDescriptionForegroundColorClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionBackgroundColorClause.
    def visitScreenDescriptionBackgroundColorClause(
        self, ctx: CobolUnisysParser.ScreenDescriptionBackgroundColorClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionControlClause.
    def visitScreenDescriptionControlClause(
        self, ctx: CobolUnisysParser.ScreenDescriptionControlClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionValueClause.
    def visitScreenDescriptionValueClause(
        self, ctx: CobolUnisysParser.ScreenDescriptionValueClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionPictureClause.
    def visitScreenDescriptionPictureClause(
        self, ctx: CobolUnisysParser.ScreenDescriptionPictureClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionFromClause.
    def visitScreenDescriptionFromClause(
        self, ctx: CobolUnisysParser.ScreenDescriptionFromClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionToClause.
    def visitScreenDescriptionToClause(
        self, ctx: CobolUnisysParser.ScreenDescriptionToClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionUsingClause.
    def visitScreenDescriptionUsingClause(
        self, ctx: CobolUnisysParser.ScreenDescriptionUsingClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionUsageClause.
    def visitScreenDescriptionUsageClause(
        self, ctx: CobolUnisysParser.ScreenDescriptionUsageClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionBlankWhenZeroClause.
    def visitScreenDescriptionBlankWhenZeroClause(
        self, ctx: CobolUnisysParser.ScreenDescriptionBlankWhenZeroClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionJustifiedClause.
    def visitScreenDescriptionJustifiedClause(
        self, ctx: CobolUnisysParser.ScreenDescriptionJustifiedClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionSignClause.
    def visitScreenDescriptionSignClause(
        self, ctx: CobolUnisysParser.ScreenDescriptionSignClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionAutoClause.
    def visitScreenDescriptionAutoClause(
        self, ctx: CobolUnisysParser.ScreenDescriptionAutoClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionSecureClause.
    def visitScreenDescriptionSecureClause(
        self, ctx: CobolUnisysParser.ScreenDescriptionSecureClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionRequiredClause.
    def visitScreenDescriptionRequiredClause(
        self, ctx: CobolUnisysParser.ScreenDescriptionRequiredClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionPromptClause.
    def visitScreenDescriptionPromptClause(
        self, ctx: CobolUnisysParser.ScreenDescriptionPromptClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionPromptOccursClause.
    def visitScreenDescriptionPromptOccursClause(
        self, ctx: CobolUnisysParser.ScreenDescriptionPromptOccursClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionFullClause.
    def visitScreenDescriptionFullClause(
        self, ctx: CobolUnisysParser.ScreenDescriptionFullClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenDescriptionZeroFillClause.
    def visitScreenDescriptionZeroFillClause(
        self, ctx: CobolUnisysParser.ScreenDescriptionZeroFillClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportSection.
    def visitReportSection(self, ctx: CobolUnisysParser.ReportSectionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportDescription.
    def visitReportDescription(self, ctx: CobolUnisysParser.ReportDescriptionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportDescriptionEntry.
    def visitReportDescriptionEntry(
        self, ctx: CobolUnisysParser.ReportDescriptionEntryContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportDescriptionGlobalClause.
    def visitReportDescriptionGlobalClause(
        self, ctx: CobolUnisysParser.ReportDescriptionGlobalClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportDescriptionPageLimitClause.
    def visitReportDescriptionPageLimitClause(
        self, ctx: CobolUnisysParser.ReportDescriptionPageLimitClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportDescriptionHeadingClause.
    def visitReportDescriptionHeadingClause(
        self, ctx: CobolUnisysParser.ReportDescriptionHeadingClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportDescriptionFirstDetailClause.
    def visitReportDescriptionFirstDetailClause(
        self, ctx: CobolUnisysParser.ReportDescriptionFirstDetailClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportDescriptionLastDetailClause.
    def visitReportDescriptionLastDetailClause(
        self, ctx: CobolUnisysParser.ReportDescriptionLastDetailClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportDescriptionFootingClause.
    def visitReportDescriptionFootingClause(
        self, ctx: CobolUnisysParser.ReportDescriptionFootingClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportGroupDescriptionEntry.
    def visitReportGroupDescriptionEntry(
        self, ctx: CobolUnisysParser.ReportGroupDescriptionEntryContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportGroupDescriptionEntryFormat1.
    def visitReportGroupDescriptionEntryFormat1(
        self, ctx: CobolUnisysParser.ReportGroupDescriptionEntryFormat1Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportGroupDescriptionEntryFormat2.
    def visitReportGroupDescriptionEntryFormat2(
        self, ctx: CobolUnisysParser.ReportGroupDescriptionEntryFormat2Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportGroupDescriptionEntryFormat3.
    def visitReportGroupDescriptionEntryFormat3(
        self, ctx: CobolUnisysParser.ReportGroupDescriptionEntryFormat3Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportGroupBlankWhenZeroClause.
    def visitReportGroupBlankWhenZeroClause(
        self, ctx: CobolUnisysParser.ReportGroupBlankWhenZeroClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportGroupColumnNumberClause.
    def visitReportGroupColumnNumberClause(
        self, ctx: CobolUnisysParser.ReportGroupColumnNumberClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportGroupIndicateClause.
    def visitReportGroupIndicateClause(
        self, ctx: CobolUnisysParser.ReportGroupIndicateClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportGroupJustifiedClause.
    def visitReportGroupJustifiedClause(
        self, ctx: CobolUnisysParser.ReportGroupJustifiedClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportGroupLineNumberClause.
    def visitReportGroupLineNumberClause(
        self, ctx: CobolUnisysParser.ReportGroupLineNumberClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportGroupLineNumberNextPage.
    def visitReportGroupLineNumberNextPage(
        self, ctx: CobolUnisysParser.ReportGroupLineNumberNextPageContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportGroupLineNumberPlus.
    def visitReportGroupLineNumberPlus(
        self, ctx: CobolUnisysParser.ReportGroupLineNumberPlusContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportGroupNextGroupClause.
    def visitReportGroupNextGroupClause(
        self, ctx: CobolUnisysParser.ReportGroupNextGroupClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportGroupNextGroupPlus.
    def visitReportGroupNextGroupPlus(
        self, ctx: CobolUnisysParser.ReportGroupNextGroupPlusContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportGroupNextGroupNextPage.
    def visitReportGroupNextGroupNextPage(
        self, ctx: CobolUnisysParser.ReportGroupNextGroupNextPageContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportGroupPictureClause.
    def visitReportGroupPictureClause(
        self, ctx: CobolUnisysParser.ReportGroupPictureClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportGroupResetClause.
    def visitReportGroupResetClause(
        self, ctx: CobolUnisysParser.ReportGroupResetClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportGroupSignClause.
    def visitReportGroupSignClause(
        self, ctx: CobolUnisysParser.ReportGroupSignClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportGroupSourceClause.
    def visitReportGroupSourceClause(
        self, ctx: CobolUnisysParser.ReportGroupSourceClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportGroupSumClause.
    def visitReportGroupSumClause(
        self, ctx: CobolUnisysParser.ReportGroupSumClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportGroupTypeClause.
    def visitReportGroupTypeClause(
        self, ctx: CobolUnisysParser.ReportGroupTypeClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportGroupTypeReportHeading.
    def visitReportGroupTypeReportHeading(
        self, ctx: CobolUnisysParser.ReportGroupTypeReportHeadingContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportGroupTypePageHeading.
    def visitReportGroupTypePageHeading(
        self, ctx: CobolUnisysParser.ReportGroupTypePageHeadingContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportGroupTypeControlHeading.
    def visitReportGroupTypeControlHeading(
        self, ctx: CobolUnisysParser.ReportGroupTypeControlHeadingContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportGroupTypeDetail.
    def visitReportGroupTypeDetail(
        self, ctx: CobolUnisysParser.ReportGroupTypeDetailContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportGroupTypeControlFooting.
    def visitReportGroupTypeControlFooting(
        self, ctx: CobolUnisysParser.ReportGroupTypeControlFootingContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportGroupUsageClause.
    def visitReportGroupUsageClause(
        self, ctx: CobolUnisysParser.ReportGroupUsageClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportGroupTypePageFooting.
    def visitReportGroupTypePageFooting(
        self, ctx: CobolUnisysParser.ReportGroupTypePageFootingContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportGroupTypeReportFooting.
    def visitReportGroupTypeReportFooting(
        self, ctx: CobolUnisysParser.ReportGroupTypeReportFootingContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportGroupValueClause.
    def visitReportGroupValueClause(
        self, ctx: CobolUnisysParser.ReportGroupValueClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#programLibrarySection.
    def visitProgramLibrarySection(
        self, ctx: CobolUnisysParser.ProgramLibrarySectionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#libraryDescriptionEntry.
    def visitLibraryDescriptionEntry(
        self, ctx: CobolUnisysParser.LibraryDescriptionEntryContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#libraryDescriptionEntryFormat1.
    def visitLibraryDescriptionEntryFormat1(
        self, ctx: CobolUnisysParser.LibraryDescriptionEntryFormat1Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#libraryDescriptionEntryFormat2.
    def visitLibraryDescriptionEntryFormat2(
        self, ctx: CobolUnisysParser.LibraryDescriptionEntryFormat2Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#libraryAttributeClauseFormat1.
    def visitLibraryAttributeClauseFormat1(
        self, ctx: CobolUnisysParser.LibraryAttributeClauseFormat1Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#libraryAttributeClauseFormat2.
    def visitLibraryAttributeClauseFormat2(
        self, ctx: CobolUnisysParser.LibraryAttributeClauseFormat2Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#libraryAttributeFunction.
    def visitLibraryAttributeFunction(
        self, ctx: CobolUnisysParser.LibraryAttributeFunctionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#libraryAttributeParameter.
    def visitLibraryAttributeParameter(
        self, ctx: CobolUnisysParser.LibraryAttributeParameterContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#libraryAttributeTitle.
    def visitLibraryAttributeTitle(
        self, ctx: CobolUnisysParser.LibraryAttributeTitleContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#libraryEntryProcedureClauseFormat1.
    def visitLibraryEntryProcedureClauseFormat1(
        self, ctx: CobolUnisysParser.LibraryEntryProcedureClauseFormat1Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#libraryEntryProcedureClauseFormat2.
    def visitLibraryEntryProcedureClauseFormat2(
        self, ctx: CobolUnisysParser.LibraryEntryProcedureClauseFormat2Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#libraryEntryProcedureForClause.
    def visitLibraryEntryProcedureForClause(
        self, ctx: CobolUnisysParser.LibraryEntryProcedureForClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#libraryEntryProcedureGivingClause.
    def visitLibraryEntryProcedureGivingClause(
        self, ctx: CobolUnisysParser.LibraryEntryProcedureGivingClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#libraryEntryProcedureUsingClause.
    def visitLibraryEntryProcedureUsingClause(
        self, ctx: CobolUnisysParser.LibraryEntryProcedureUsingClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#libraryEntryProcedureUsingName.
    def visitLibraryEntryProcedureUsingName(
        self, ctx: CobolUnisysParser.LibraryEntryProcedureUsingNameContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#libraryEntryProcedureWithClause.
    def visitLibraryEntryProcedureWithClause(
        self, ctx: CobolUnisysParser.LibraryEntryProcedureWithClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#libraryEntryProcedureWithName.
    def visitLibraryEntryProcedureWithName(
        self, ctx: CobolUnisysParser.LibraryEntryProcedureWithNameContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#libraryIsCommonClause.
    def visitLibraryIsCommonClause(
        self, ctx: CobolUnisysParser.LibraryIsCommonClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#libraryIsGlobalClause.
    def visitLibraryIsGlobalClause(
        self, ctx: CobolUnisysParser.LibraryIsGlobalClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataDescriptionEntry.
    def visitDataDescriptionEntry(
        self, ctx: CobolUnisysParser.DataDescriptionEntryContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#copyStatement.
    def visitCopyStatement(self, ctx: CobolUnisysParser.CopyStatementContext):
        # extract statements
        res = self.assessCopyStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)

        # extract dependency
        copy_source = recursive_find_first_child_by_type(
            ctx, CobolUnisysParser.CopySourceContext
        )

        if copy_source is None:
            raise ValueError(
                f"File name of COPY statement {get_original_code_content(self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)}"
            )

        copy_name = copy_source.getChild(0)

        replace_clauses = find_all_children_by_type(
            ctx, CobolUnisysParser.ReplaceClauseContext
        )

        replace_list = []

        for replace_clause in replace_clauses:
            replaceable = replace_clause.getChild(0)
            replacement = replace_clause.getChild(2)

            replace = CopybookReplace(
                replaceable=replaceable.getText(),
                replacement=replacement.getText(),
            )
            replace_list.append(replace)

        copybook = ImportedCopybook(
            copybook_name=copy_name.getText(),
            line_number=copy_source.start.line,
            replacing=replace_list,
        )

        self.copybook_list.append(copybook)

        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#copySource.
    def visitCopySource(self, ctx: CobolUnisysParser.CopySourceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#copyLibrary.
    def visitCopyLibrary(self, ctx: CobolUnisysParser.CopyLibraryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#replacingPhrase.
    def visitReplacingPhrase(self, ctx: CobolUnisysParser.ReplacingPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#replaceOffStatement.
    def visitReplaceOffStatement(
        self, ctx: CobolUnisysParser.ReplaceOffStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#replaceClause.
    def visitReplaceClause(self, ctx: CobolUnisysParser.ReplaceClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#directoryPhrase.
    def visitDirectoryPhrase(self, ctx: CobolUnisysParser.DirectoryPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#familyPhrase.
    def visitFamilyPhrase(self, ctx: CobolUnisysParser.FamilyPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#replaceable.
    def visitReplaceable(self, ctx: CobolUnisysParser.ReplaceableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#replacement.
    def visitReplacement(self, ctx: CobolUnisysParser.ReplacementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#ejectStatement.
    def visitEjectStatement(self, ctx: CobolUnisysParser.EjectStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#skipStatement.
    def visitSkipStatement(self, ctx: CobolUnisysParser.SkipStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#titleStatement.
    def visitTitleStatement(self, ctx: CobolUnisysParser.TitleStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#pseudoText.
    def visitPseudoText(self, ctx: CobolUnisysParser.PseudoTextContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#charData.
    def visitCharData(self, ctx: CobolUnisysParser.CharDataContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#charDataSql.
    def visitCharDataSql(self, ctx: CobolUnisysParser.CharDataSqlContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#charDataLine.
    def visitCharDataLine(self, ctx: CobolUnisysParser.CharDataLineContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#cobolWord.
    def visitCobolWord(self, ctx: CobolUnisysParser.CobolWordContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#literal.
    def visitLiteral(self, ctx: CobolUnisysParser.LiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#filename.
    def visitFilename(self, ctx: CobolUnisysParser.FilenameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataDescriptionEntryFormat1.
    def visitDataDescriptionEntryFormat1(
        self, ctx: CobolUnisysParser.DataDescriptionEntryFormat1Context
    ):
        variable = extract_cobol_variable(ctx)
        self.variable_list.append(variable)

        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataDescriptionEntryFormat2.
    def visitDataDescriptionEntryFormat2(
        self, ctx: CobolUnisysParser.DataDescriptionEntryFormat2Context
    ):
        variable = extract_cobol_variable(ctx)
        self.variable_list.append(variable)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataDescriptionEntryFormat3.
    def visitDataDescriptionEntryFormat3(
        self, ctx: CobolUnisysParser.DataDescriptionEntryFormat3Context
    ):
        variable = extract_cobol_variable(ctx)
        self.variable_list.append(variable)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataDescriptionEntryExecSql.
    def visitDataDescriptionEntryExecSql(
        self, ctx: CobolUnisysParser.DataDescriptionEntryExecSqlContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataAlignedClause.
    def visitDataAlignedClause(self, ctx: CobolUnisysParser.DataAlignedClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataBlankWhenZeroClause.
    def visitDataBlankWhenZeroClause(
        self, ctx: CobolUnisysParser.DataBlankWhenZeroClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataCommonOwnLocalClause.
    def visitDataCommonOwnLocalClause(
        self, ctx: CobolUnisysParser.DataCommonOwnLocalClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataExternalClause.
    def visitDataExternalClause(self, ctx: CobolUnisysParser.DataExternalClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataGlobalClause.
    def visitDataGlobalClause(self, ctx: CobolUnisysParser.DataGlobalClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataIntegerStringClause.
    def visitDataIntegerStringClause(
        self, ctx: CobolUnisysParser.DataIntegerStringClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataJustifiedClause.
    def visitDataJustifiedClause(
        self, ctx: CobolUnisysParser.DataJustifiedClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataOccursClause.
    def visitDataOccursClause(self, ctx: CobolUnisysParser.DataOccursClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataOccursTo.
    def visitDataOccursTo(self, ctx: CobolUnisysParser.DataOccursToContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataOccursSort.
    def visitDataOccursSort(self, ctx: CobolUnisysParser.DataOccursSortContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataPictureClause.
    def visitDataPictureClause(self, ctx: CobolUnisysParser.DataPictureClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#pictureString.
    def visitPictureString(self, ctx: CobolUnisysParser.PictureStringContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#pictureChars.
    def visitPictureChars(self, ctx: CobolUnisysParser.PictureCharsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#pictureCardinality.
    def visitPictureCardinality(self, ctx: CobolUnisysParser.PictureCardinalityContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataReceivedByClause.
    def visitDataReceivedByClause(
        self, ctx: CobolUnisysParser.DataReceivedByClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataRecordAreaClause.
    def visitDataRecordAreaClause(
        self, ctx: CobolUnisysParser.DataRecordAreaClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataRedefinesClause.
    def visitDataRedefinesClause(
        self, ctx: CobolUnisysParser.DataRedefinesClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataRenamesClause.
    def visitDataRenamesClause(self, ctx: CobolUnisysParser.DataRenamesClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataSignClause.
    def visitDataSignClause(self, ctx: CobolUnisysParser.DataSignClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataSynchronizedClause.
    def visitDataSynchronizedClause(
        self, ctx: CobolUnisysParser.DataSynchronizedClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataThreadLocalClause.
    def visitDataThreadLocalClause(
        self, ctx: CobolUnisysParser.DataThreadLocalClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataTypeClause.
    def visitDataTypeClause(self, ctx: CobolUnisysParser.DataTypeClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataTypeDefClause.
    def visitDataTypeDefClause(self, ctx: CobolUnisysParser.DataTypeDefClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataUsageClause.
    def visitDataUsageClause(self, ctx: CobolUnisysParser.DataUsageClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataUsingClause.
    def visitDataUsingClause(self, ctx: CobolUnisysParser.DataUsingClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataValueClause.
    def visitDataValueClause(self, ctx: CobolUnisysParser.DataValueClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataValueInterval.
    def visitDataValueInterval(self, ctx: CobolUnisysParser.DataValueIntervalContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataValueIntervalFrom.
    def visitDataValueIntervalFrom(
        self, ctx: CobolUnisysParser.DataValueIntervalFromContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataValueIntervalTo.
    def visitDataValueIntervalTo(
        self, ctx: CobolUnisysParser.DataValueIntervalToContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataWithLowerBoundsClause.
    def visitDataWithLowerBoundsClause(
        self, ctx: CobolUnisysParser.DataWithLowerBoundsClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#procedureDivision.
    def visitProcedureDivision(self, ctx: CobolUnisysParser.ProcedureDivisionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#procedureDivisionUsingClause.
    def visitProcedureDivisionUsingClause(
        self, ctx: CobolUnisysParser.ProcedureDivisionUsingClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#procedureDivisionGivingClause.
    def visitProcedureDivisionGivingClause(
        self, ctx: CobolUnisysParser.ProcedureDivisionGivingClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#procedureDivisionUsingParameter.
    def visitProcedureDivisionUsingParameter(
        self, ctx: CobolUnisysParser.ProcedureDivisionUsingParameterContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#procedureDivisionByReferencePhrase.
    def visitProcedureDivisionByReferencePhrase(
        self, ctx: CobolUnisysParser.ProcedureDivisionByReferencePhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#procedureDivisionByReference.
    def visitProcedureDivisionByReference(
        self, ctx: CobolUnisysParser.ProcedureDivisionByReferenceContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#procedureDivisionByValuePhrase.
    def visitProcedureDivisionByValuePhrase(
        self, ctx: CobolUnisysParser.ProcedureDivisionByValuePhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#procedureDivisionByValue.
    def visitProcedureDivisionByValue(
        self, ctx: CobolUnisysParser.ProcedureDivisionByValueContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#procedureDeclaratives.
    def visitProcedureDeclaratives(
        self, ctx: CobolUnisysParser.ProcedureDeclarativesContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#procedureDeclarative.
    def visitProcedureDeclarative(
        self, ctx: CobolUnisysParser.ProcedureDeclarativeContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#procedureSectionHeader.
    def visitProcedureSectionHeader(
        self, ctx: CobolUnisysParser.ProcedureSectionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#procedureDivisionBody.
    def visitProcedureDivisionBody(
        self, ctx: CobolUnisysParser.ProcedureDivisionBodyContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#procedureSection.
    def visitProcedureSection(self, ctx: CobolUnisysParser.ProcedureSectionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#paragraphs.
    def visitParagraphs(self, ctx: CobolUnisysParser.ParagraphsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#paragraph.
    def visitParagraph(self, ctx: CobolUnisysParser.ParagraphContext):
        paragraph_name = ctx.getChild(0)
        start_line = ctx.start.line
        end_line = ctx.stop.line

        perform_procedure_statements = find_all_children_by_type(
            ctx, CobolUnisysParser.PerformProcedureStatementContext
        )

        procedure_name_list = []

        for perform_statement in perform_procedure_statements:
            # perform statement can have multiple paragraph names
            procedure_names = find_all_children_by_type(
                perform_statement, CobolUnisysParser.ProcedureNameContext
            )

            procedure_names = list(
                map(lambda element: element.getText(), procedure_names)
            )

            procedure_name_list.extend(procedure_names)

        code_content = get_original_code_content(
            self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex
        )

        procedure_section = find_parent_by_type(
            ctx, self.parser.ProcedureSectionContext
        )
        section = None
        if procedure_section:
            procedure_section_header = procedure_section.procedureSectionHeader()
            section_name = procedure_section_header.sectionName()
            section = section_name.getText()

        paragraph = Paragraph(
            paragraph_name=paragraph_name.getText(),
            section=section,
            paragraph_code=code_content,
            paragraph_lines=[start_line, end_line],
            ref_paragraphs=procedure_name_list,
        )

        self.paragraph_list.append(paragraph)

        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#sentence.
    def visitSentence(self, ctx: CobolUnisysParser.SentenceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#statement.
    def visitStatement(self, ctx: CobolUnisysParser.StatementContext):
        return self.visitChildren(ctx)

    def assessAcceptStatement(self, ctx: CobolUnisysParser.AcceptStatementContext):
        tag = "AcceptStatement"

        identifier = recursive_find_first_child_by_type(
            ctx, CobolUnisysParser.IdentifierContext
        )

        raw = get_original_code_content(
            self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex
        )
        start_token = ctx.start
        stop_token = ctx.stop

        if not identifier:
            logger.warning(f"Identifier is missing in accept statement'{raw}'")

        return {
            "tag": tag,
            "raw": raw,
            "start_line": start_token.line,
            "stop_line": stop_token.line,
            "start_idx": start_token.start,
            "stop_idx": stop_token.stop,
            "identifier": identifier.getText() if identifier else "",
        }

    # Visit a parse tree produced by CobolUnisysParser#acceptStatement.
    def visitAcceptStatement(self, ctx: CobolUnisysParser.AcceptStatementContext):

        # ignore other accept statements
        if (
            ctx.acceptFromDateStatement()
            or ctx.acceptFromMnemonicStatement()
            or ctx.acceptFromEscapeKeyStatement()
            or ctx.acceptMessageCountStatement()
        ):
            return self.visitChildren(ctx)

        res = self.assessAcceptStatement(ctx)

        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)

        self.statements.append(res)

        return self.visitChildren(ctx)

    def assessAcceptFromDateStatement(
        self, ctx: CobolUnisysParser.AcceptFromDateStatementContext
    ):
        tag = "AcceptFromDateStatement"

        accept_from_date_phrase = ctx.acceptFromDatePhrase()

        date = get_original_code_content(
            self.parser,
            accept_from_date_phrase.start.tokenIndex,
            accept_from_date_phrase.stop.tokenIndex,
        )

        # fix missing code by getting the parent code
        accept_statement_context: CobolUnisysParser.AcceptStatementContext = (
            ctx.parentCtx
        )

        identifier = accept_statement_context.identifier()

        raw = get_original_code_content(
            self.parser,
            accept_statement_context.start.tokenIndex,
            accept_statement_context.stop.tokenIndex,
        )
        start_token = ctx.start
        stop_token = ctx.stop

        if not date:
            logger.warning(f"Date is missing in accept from date statement'{raw}'")

        return {
            "tag": tag,
            "raw": raw,
            "start_line": start_token.line,
            "stop_line": stop_token.line,
            "start_idx": start_token.start,
            "stop_idx": stop_token.stop,
            "identifier": identifier.getText() if identifier else "",
            "datetime": date,
        }

    # Visit a parse tree produced by CobolUnisysParser#acceptFromDateStatement.
    def visitAcceptFromDateStatement(
        self, ctx: CobolUnisysParser.AcceptFromDateStatementContext
    ):
        res = self.assessAcceptFromDateStatement(ctx)

        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)

        self.statements.append(res)
        return self.visitChildren(ctx)

    def assessAcceptFromMnemonicStatement(
        self, ctx: CobolUnisysParser.AcceptFromMnemonicStatementContext
    ):
        tag = "AcceptFromMnemonicStatement"
        mnemonic = ctx.getChild(1)

        accept_statement_context: CobolUnisysParser.AcceptStatementContext = (
            ctx.parentCtx
        )

        identifier = accept_statement_context.identifier()

        raw = get_original_code_content(
            self.parser,
            accept_statement_context.start.tokenIndex,
            accept_statement_context.stop.tokenIndex,
        )
        start_token = ctx.start
        stop_token = ctx.stop

        if not mnemonic:
            logger.warning(
                f"Mnemonic is missing in accept from mnemonic statement'{raw}'"
            )

        return {
            "tag": tag,
            "raw": raw,
            "start_line": start_token.line,
            "stop_line": stop_token.line,
            "start_idx": start_token.start,
            "stop_idx": stop_token.stop,
            "identifier": identifier.getText() if identifier else "",
            "mnemonic_name": mnemonic.getText() if mnemonic else "",
        }

    # Visit a parse tree produced by CobolUnisysParser#acceptFromMnemonicStatement.
    def visitAcceptFromMnemonicStatement(
        self, ctx: CobolUnisysParser.AcceptFromMnemonicStatementContext
    ):
        res = self.assessAcceptFromMnemonicStatement(ctx)

        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)

        return self.visitChildren(ctx)

    def assessAcceptFromEscapeKeyStatement(
        self, ctx: CobolUnisysParser.AcceptFromEscapeKeyStatementContext
    ):
        tag = "AcceptFromEscapeKeyStatement"

        accept_statement_context: CobolUnisysParser.AcceptStatementContext = (
            ctx.parentCtx
        )
        identifier = accept_statement_context.identifier()

        raw = get_original_code_content(
            self.parser,
            accept_statement_context.start.tokenIndex,
            accept_statement_context.stop.tokenIndex,
        )
        start_token = ctx.start
        stop_token = ctx.stop

        if not identifier:
            logger.warning(f"Identifier is missing in accept statement'{raw}'")

        return {
            "tag": tag,
            "raw": raw,
            "start_line": start_token.line,
            "stop_line": stop_token.line,
            "start_idx": start_token.start,
            "stop_idx": stop_token.stop,
            "identifier": identifier.getText() if identifier else "",
        }

    # Visit a parse tree produced by CobolUnisysParser#acceptFromEscapeKeyStatement.
    def visitAcceptFromEscapeKeyStatement(
        self, ctx: CobolUnisysParser.AcceptFromEscapeKeyStatementContext
    ):
        res = self.assessAcceptFromEscapeKeyStatement(ctx)

        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)

        return self.visitChildren(ctx)

    def assessAcceptFromMessageCountStatement(self, ctx):
        tag = "AcceptFromMessageCountStatement"

        accept_statement_context: CobolUnisysParser.AcceptStatementContext = (
            ctx.parentCtx
        )
        identifier = accept_statement_context.identifier()

        raw = get_original_code_content(
            self.parser,
            accept_statement_context.start.tokenIndex,
            accept_statement_context.stop.tokenIndex,
        )
        start_token = ctx.start
        stop_token = ctx.stop

        if not identifier:
            logger.warning(f"Identifier is missing in accept statement'{raw}'")

        return {
            "tag": tag,
            "raw": raw,
            "start_line": start_token.line,
            "stop_line": stop_token.line,
            "start_idx": start_token.start,
            "stop_idx": stop_token.stop,
            "identifier": identifier.getText() if identifier else "",
        }

    # Visit a parse tree produced by CobolUnisysParser#acceptMessageCountStatement.
    def visitAcceptMessageCountStatement(
        self, ctx: CobolUnisysParser.AcceptMessageCountStatementContext
    ):
        res = self.assessAcceptFromMessageCountStatement(ctx)

        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#addToStatement.
    def visitAddToStatement(self, ctx: CobolUnisysParser.AddToStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#addToGivingStatement.
    def visitAddToGivingStatement(
        self, ctx: CobolUnisysParser.AddToGivingStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#addCorrespondingStatement.
    def visitAddCorrespondingStatement(
        self, ctx: CobolUnisysParser.AddCorrespondingStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#addFrom.
    def visitAddFrom(self, ctx: CobolUnisysParser.AddFromContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#addTo.
    def visitAddTo(self, ctx: CobolUnisysParser.AddToContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#addToGiving.
    def visitAddToGiving(self, ctx: CobolUnisysParser.AddToGivingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#addGiving.
    def visitAddGiving(self, ctx: CobolUnisysParser.AddGivingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#alteredGoTo.
    def visitAlteredGoTo(self, ctx: CobolUnisysParser.AlteredGoToContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#alterProceedTo.
    def visitAlterProceedTo(self, ctx: CobolUnisysParser.AlterProceedToContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#callUsingPhrase.
    def visitCallUsingPhrase(self, ctx: CobolUnisysParser.CallUsingPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#callUsingParameter.
    def visitCallUsingParameter(self, ctx: CobolUnisysParser.CallUsingParameterContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#callByReferencePhrase.
    def visitCallByReferencePhrase(
        self, ctx: CobolUnisysParser.CallByReferencePhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#callByReference.
    def visitCallByReference(self, ctx: CobolUnisysParser.CallByReferenceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#callByValuePhrase.
    def visitCallByValuePhrase(self, ctx: CobolUnisysParser.CallByValuePhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#callByValue.
    def visitCallByValue(self, ctx: CobolUnisysParser.CallByValueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#callByContentPhrase.
    def visitCallByContentPhrase(
        self, ctx: CobolUnisysParser.CallByContentPhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#callByContent.
    def visitCallByContent(self, ctx: CobolUnisysParser.CallByContentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#callGivingPhrase.
    def visitCallGivingPhrase(self, ctx: CobolUnisysParser.CallGivingPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#cancelStatement.
    def visitCancelStatement(self, ctx: CobolUnisysParser.CancelStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#cancelCall.
    def visitCancelCall(self, ctx: CobolUnisysParser.CancelCallContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#closeFile.
    def visitCloseFile(self, ctx: CobolUnisysParser.CloseFileContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#closeReelUnitStatement.
    def visitCloseReelUnitStatement(
        self, ctx: CobolUnisysParser.CloseReelUnitStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#closeRelativeStatement.
    def visitCloseRelativeStatement(
        self, ctx: CobolUnisysParser.CloseRelativeStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#closePortFileIOStatement.
    def visitClosePortFileIOStatement(
        self, ctx: CobolUnisysParser.ClosePortFileIOStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#closePortFileIOUsing.
    def visitClosePortFileIOUsing(
        self, ctx: CobolUnisysParser.ClosePortFileIOUsingContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#closePortFileIOUsingCloseDisposition.
    def visitClosePortFileIOUsingCloseDisposition(
        self, ctx: CobolUnisysParser.ClosePortFileIOUsingCloseDispositionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#closePortFileIOUsingAssociatedData.
    def visitClosePortFileIOUsingAssociatedData(
        self, ctx: CobolUnisysParser.ClosePortFileIOUsingAssociatedDataContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#closePortFileIOUsingAssociatedDataLength.
    def visitClosePortFileIOUsingAssociatedDataLength(
        self, ctx: CobolUnisysParser.ClosePortFileIOUsingAssociatedDataLengthContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#computeStore.
    def visitComputeStore(self, ctx: CobolUnisysParser.ComputeStoreContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#deleteStatement.
    def visitDeleteStatement(self, ctx: CobolUnisysParser.DeleteStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#disableStatement.
    def visitDisableStatement(self, ctx: CobolUnisysParser.DisableStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#displayOperand.
    def visitDisplayOperand(self, ctx: CobolUnisysParser.DisplayOperandContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#displayAt.
    def visitDisplayAt(self, ctx: CobolUnisysParser.DisplayAtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#displayUpon.
    def visitDisplayUpon(self, ctx: CobolUnisysParser.DisplayUponContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#displayWith.
    def visitDisplayWith(self, ctx: CobolUnisysParser.DisplayWithContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#divideStatement.
    def visitDivideStatement(self, ctx: CobolUnisysParser.DivideStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#divideIntoStatement.
    def visitDivideIntoStatement(
        self, ctx: CobolUnisysParser.DivideIntoStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#divideIntoGivingStatement.
    def visitDivideIntoGivingStatement(
        self, ctx: CobolUnisysParser.DivideIntoGivingStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#divideByGivingStatement.
    def visitDivideByGivingStatement(
        self, ctx: CobolUnisysParser.DivideByGivingStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#divideGivingPhrase.
    def visitDivideGivingPhrase(self, ctx: CobolUnisysParser.DivideGivingPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#divideInto.
    def visitDivideInto(self, ctx: CobolUnisysParser.DivideIntoContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#divideGiving.
    def visitDivideGiving(self, ctx: CobolUnisysParser.DivideGivingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#divideRemainder.
    def visitDivideRemainder(self, ctx: CobolUnisysParser.DivideRemainderContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#enableStatement.
    def visitEnableStatement(self, ctx: CobolUnisysParser.EnableStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#entryStatement.
    def visitEntryStatement(self, ctx: CobolUnisysParser.EntryStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#evaluateSelect.
    def visitEvaluateSelect(self, ctx: CobolUnisysParser.EvaluateSelectContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#evaluateAlsoSelect.
    def visitEvaluateAlsoSelect(self, ctx: CobolUnisysParser.EvaluateAlsoSelectContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#evaluateWhenPhrase.
    def visitEvaluateWhenPhrase(self, ctx: CobolUnisysParser.EvaluateWhenPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#evaluateWhen.
    def visitEvaluateWhen(self, ctx: CobolUnisysParser.EvaluateWhenContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#evaluateCondition.
    def visitEvaluateCondition(self, ctx: CobolUnisysParser.EvaluateConditionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#evaluateThrough.
    def visitEvaluateThrough(self, ctx: CobolUnisysParser.EvaluateThroughContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#evaluateAlsoCondition.
    def visitEvaluateAlsoCondition(
        self, ctx: CobolUnisysParser.EvaluateAlsoConditionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#evaluateWhenOther.
    def visitEvaluateWhenOther(self, ctx: CobolUnisysParser.EvaluateWhenOtherContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#evaluateValue.
    def visitEvaluateValue(self, ctx: CobolUnisysParser.EvaluateValueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#execCicsStatement.
    def visitExecCicsStatement(self, ctx: CobolUnisysParser.ExecCicsStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#execSqlStatement.
    def visitExecSqlStatement(self, ctx: CobolUnisysParser.ExecSqlStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#execSqlImsStatement.
    def visitExecSqlImsStatement(
        self, ctx: CobolUnisysParser.ExecSqlImsStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#exhibitStatement.
    def visitExhibitStatement(self, ctx: CobolUnisysParser.ExhibitStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#exhibitOperand.
    def visitExhibitOperand(self, ctx: CobolUnisysParser.ExhibitOperandContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#generateStatement.
    def visitGenerateStatement(self, ctx: CobolUnisysParser.GenerateStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#goToStatementSimple.
    def visitGoToStatementSimple(
        self, ctx: CobolUnisysParser.GoToStatementSimpleContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#goToDependingOnStatement.
    def visitGoToDependingOnStatement(
        self, ctx: CobolUnisysParser.GoToDependingOnStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#ifThen.
    def visitIfThen(self, ctx: CobolUnisysParser.IfThenContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#ifElse.
    def visitIfElse(self, ctx: CobolUnisysParser.IfElseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#initializeReplacingPhrase.
    def visitInitializeReplacingPhrase(
        self, ctx: CobolUnisysParser.InitializeReplacingPhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#initializeReplacingBy.
    def visitInitializeReplacingBy(
        self, ctx: CobolUnisysParser.InitializeReplacingByContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#initiateStatement.
    def visitInitiateStatement(self, ctx: CobolUnisysParser.InitiateStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#inspectTallyingPhrase.
    def visitInspectTallyingPhrase(
        self, ctx: CobolUnisysParser.InspectTallyingPhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#inspectReplacingPhrase.
    def visitInspectReplacingPhrase(
        self, ctx: CobolUnisysParser.InspectReplacingPhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#inspectTallyingReplacingPhrase.
    def visitInspectTallyingReplacingPhrase(
        self, ctx: CobolUnisysParser.InspectTallyingReplacingPhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#inspectConvertingPhrase.
    def visitInspectConvertingPhrase(
        self, ctx: CobolUnisysParser.InspectConvertingPhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#inspectFor.
    def visitInspectFor(self, ctx: CobolUnisysParser.InspectForContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#inspectCharacters.
    def visitInspectCharacters(self, ctx: CobolUnisysParser.InspectCharactersContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#inspectReplacingCharacters.
    def visitInspectReplacingCharacters(
        self, ctx: CobolUnisysParser.InspectReplacingCharactersContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#inspectAllLeadings.
    def visitInspectAllLeadings(self, ctx: CobolUnisysParser.InspectAllLeadingsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#inspectReplacingAllLeadings.
    def visitInspectReplacingAllLeadings(
        self, ctx: CobolUnisysParser.InspectReplacingAllLeadingsContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#inspectAllLeading.
    def visitInspectAllLeading(self, ctx: CobolUnisysParser.InspectAllLeadingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#inspectReplacingAllLeading.
    def visitInspectReplacingAllLeading(
        self, ctx: CobolUnisysParser.InspectReplacingAllLeadingContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#inspectBy.
    def visitInspectBy(self, ctx: CobolUnisysParser.InspectByContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#inspectTo.
    def visitInspectTo(self, ctx: CobolUnisysParser.InspectToContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#inspectBeforeAfter.
    def visitInspectBeforeAfter(self, ctx: CobolUnisysParser.InspectBeforeAfterContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#mergeStatement.
    def visitMergeStatement(self, ctx: CobolUnisysParser.MergeStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#mergeOnKeyClause.
    def visitMergeOnKeyClause(self, ctx: CobolUnisysParser.MergeOnKeyClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#mergeCollatingSequencePhrase.
    def visitMergeCollatingSequencePhrase(
        self, ctx: CobolUnisysParser.MergeCollatingSequencePhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#mergeCollatingAlphanumeric.
    def visitMergeCollatingAlphanumeric(
        self, ctx: CobolUnisysParser.MergeCollatingAlphanumericContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#mergeCollatingNational.
    def visitMergeCollatingNational(
        self, ctx: CobolUnisysParser.MergeCollatingNationalContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#mergeUsing.
    def visitMergeUsing(self, ctx: CobolUnisysParser.MergeUsingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#mergeOutputProcedurePhrase.
    def visitMergeOutputProcedurePhrase(
        self, ctx: CobolUnisysParser.MergeOutputProcedurePhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#mergeOutputThrough.
    def visitMergeOutputThrough(self, ctx: CobolUnisysParser.MergeOutputThroughContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#mergeGivingPhrase.
    def visitMergeGivingPhrase(self, ctx: CobolUnisysParser.MergeGivingPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#mergeGiving.
    def visitMergeGiving(self, ctx: CobolUnisysParser.MergeGivingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#moveToStatement.
    def visitMoveToStatement(self, ctx: CobolUnisysParser.MoveToStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#moveToSendingArea.
    def visitMoveToSendingArea(self, ctx: CobolUnisysParser.MoveToSendingAreaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#moveCorrespondingToStatement.
    def visitMoveCorrespondingToStatement(
        self, ctx: CobolUnisysParser.MoveCorrespondingToStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#moveCorrespondingToSendingArea.
    def visitMoveCorrespondingToSendingArea(
        self, ctx: CobolUnisysParser.MoveCorrespondingToSendingAreaContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#multiplyStatement.
    def visitMultiplyStatement(self, ctx: CobolUnisysParser.MultiplyStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#multiplyRegular.
    def visitMultiplyRegular(self, ctx: CobolUnisysParser.MultiplyRegularContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#multiplyRegularOperand.
    def visitMultiplyRegularOperand(
        self, ctx: CobolUnisysParser.MultiplyRegularOperandContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#multiplyGiving.
    def visitMultiplyGiving(self, ctx: CobolUnisysParser.MultiplyGivingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#multiplyGivingOperand.
    def visitMultiplyGivingOperand(
        self, ctx: CobolUnisysParser.MultiplyGivingOperandContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#multiplyGivingResult.
    def visitMultiplyGivingResult(
        self, ctx: CobolUnisysParser.MultiplyGivingResultContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#openInputStatement.
    def visitOpenInputStatement(self, ctx: CobolUnisysParser.OpenInputStatementContext):
        file_control_name = recursive_find_first_child_by_type(
            ctx, CobolUnisysParser.FileNameContext
        )

        if file_control_name is None:
            raise ValueError(
                f"Missing file name in OPEN statement {get_original_code_content(self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)}"
            )

        for file_control in self.file_control_list:
            if file_control.file_name == file_control_name.getText():
                file_control.access_mode = "INPUT"

        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#openInput.
    def visitOpenInput(self, ctx: CobolUnisysParser.OpenInputContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#openOutputStatement.
    def visitOpenOutputStatement(
        self, ctx: CobolUnisysParser.OpenOutputStatementContext
    ):
        file_control_name = recursive_find_first_child_by_type(
            ctx, CobolUnisysParser.FileNameContext
        )

        if file_control_name is None:
            raise ValueError(
                f"Missing file name in OPEN statement {get_original_code_content(self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)}"
            )

        for file_control in self.file_control_list:
            if file_control.file_name == file_control_name.getText():
                file_control.access_mode = "OUTPUT"

        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#openOutput.
    def visitOpenOutput(self, ctx: CobolUnisysParser.OpenOutputContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#openIOStatement.
    def visitOpenIOStatement(self, ctx: CobolUnisysParser.OpenIOStatementContext):
        file_control_name = recursive_find_first_child_by_type(
            ctx, CobolUnisysParser.FileNameContext
        )

        if file_control_name is None:
            raise ValueError(
                f"Missing file name in OPEN statement {get_original_code_content(self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)}"
            )

        for file_control in self.file_control_list:
            if file_control.file_name == file_control_name.getText():
                file_control.access_mode = "I-O"

        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#openExtendStatement.
    def visitOpenExtendStatement(
        self, ctx: CobolUnisysParser.OpenExtendStatementContext
    ):
        file_control_name = recursive_find_first_child_by_type(
            ctx, CobolUnisysParser.FileNameContext
        )

        if file_control_name is None:
            raise ValueError(
                f"Missing file name in OPEN statement {get_original_code_content(self.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex)}"
            )

        for file_control in self.file_control_list:
            if file_control.file_name == file_control_name.getText():
                file_control.access_mode = "EXTEND"

        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#performInlineStatement.
    def visitPerformInlineStatement(
        self, ctx: CobolUnisysParser.PerformInlineStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#performProcedureStatement.
    def visitPerformProcedureStatement(
        self, ctx: CobolUnisysParser.PerformProcedureStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#performType.
    def visitPerformType(self, ctx: CobolUnisysParser.PerformTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#performTimes.
    def visitPerformTimes(self, ctx: CobolUnisysParser.PerformTimesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#performUntil.
    def visitPerformUntil(self, ctx: CobolUnisysParser.PerformUntilContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#performVarying.
    def visitPerformVarying(self, ctx: CobolUnisysParser.PerformVaryingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#performVaryingClause.
    def visitPerformVaryingClause(
        self, ctx: CobolUnisysParser.PerformVaryingClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#performVaryingPhrase.
    def visitPerformVaryingPhrase(
        self, ctx: CobolUnisysParser.PerformVaryingPhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#performAfter.
    def visitPerformAfter(self, ctx: CobolUnisysParser.PerformAfterContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#performFrom.
    def visitPerformFrom(self, ctx: CobolUnisysParser.PerformFromContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#performBy.
    def visitPerformBy(self, ctx: CobolUnisysParser.PerformByContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#performTestClause.
    def visitPerformTestClause(self, ctx: CobolUnisysParser.PerformTestClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#purgeStatement.
    def visitPurgeStatement(self, ctx: CobolUnisysParser.PurgeStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#readWith.
    def visitReadWith(self, ctx: CobolUnisysParser.ReadWithContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#readKey.
    def visitReadKey(self, ctx: CobolUnisysParser.ReadKeyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#receiveStatement.
    def visitReceiveStatement(self, ctx: CobolUnisysParser.ReceiveStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#receiveFromStatement.
    def visitReceiveFromStatement(
        self, ctx: CobolUnisysParser.ReceiveFromStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#receiveFrom.
    def visitReceiveFrom(self, ctx: CobolUnisysParser.ReceiveFromContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#receiveIntoStatement.
    def visitReceiveIntoStatement(
        self, ctx: CobolUnisysParser.ReceiveIntoStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#receiveNoData.
    def visitReceiveNoData(self, ctx: CobolUnisysParser.ReceiveNoDataContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#receiveWithData.
    def visitReceiveWithData(self, ctx: CobolUnisysParser.ReceiveWithDataContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#receiveBefore.
    def visitReceiveBefore(self, ctx: CobolUnisysParser.ReceiveBeforeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#receiveWith.
    def visitReceiveWith(self, ctx: CobolUnisysParser.ReceiveWithContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#receiveThread.
    def visitReceiveThread(self, ctx: CobolUnisysParser.ReceiveThreadContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#receiveSize.
    def visitReceiveSize(self, ctx: CobolUnisysParser.ReceiveSizeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#receiveStatus.
    def visitReceiveStatus(self, ctx: CobolUnisysParser.ReceiveStatusContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#releaseStatement.
    def visitReleaseStatement(self, ctx: CobolUnisysParser.ReleaseStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#returnStatement.
    def visitReturnStatement(self, ctx: CobolUnisysParser.ReturnStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#returnInto.
    def visitReturnInto(self, ctx: CobolUnisysParser.ReturnIntoContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#rewriteFrom.
    def visitRewriteFrom(self, ctx: CobolUnisysParser.RewriteFromContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#searchStatement.
    def visitSearchStatement(self, ctx: CobolUnisysParser.SearchStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#searchVarying.
    def visitSearchVarying(self, ctx: CobolUnisysParser.SearchVaryingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#searchWhen.
    def visitSearchWhen(self, ctx: CobolUnisysParser.SearchWhenContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#sendStatement.
    def visitSendStatement(self, ctx: CobolUnisysParser.SendStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#sendStatementSync.
    def visitSendStatementSync(self, ctx: CobolUnisysParser.SendStatementSyncContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#sendStatementAsync.
    def visitSendStatementAsync(self, ctx: CobolUnisysParser.SendStatementAsyncContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#sendFromPhrase.
    def visitSendFromPhrase(self, ctx: CobolUnisysParser.SendFromPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#sendWithPhrase.
    def visitSendWithPhrase(self, ctx: CobolUnisysParser.SendWithPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#sendReplacingPhrase.
    def visitSendReplacingPhrase(
        self, ctx: CobolUnisysParser.SendReplacingPhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#sendAdvancingPhrase.
    def visitSendAdvancingPhrase(
        self, ctx: CobolUnisysParser.SendAdvancingPhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#sendAdvancingPage.
    def visitSendAdvancingPage(self, ctx: CobolUnisysParser.SendAdvancingPageContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#sendAdvancingLines.
    def visitSendAdvancingLines(self, ctx: CobolUnisysParser.SendAdvancingLinesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#sendAdvancingMnemonic.
    def visitSendAdvancingMnemonic(
        self, ctx: CobolUnisysParser.SendAdvancingMnemonicContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#setToStatement.
    def visitSetToStatement(self, ctx: CobolUnisysParser.SetToStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#setUpDownByStatement.
    def visitSetUpDownByStatement(
        self, ctx: CobolUnisysParser.SetUpDownByStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#setTo.
    def visitSetTo(self, ctx: CobolUnisysParser.SetToContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#setToValue.
    def visitSetToValue(self, ctx: CobolUnisysParser.SetToValueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#setByValue.
    def visitSetByValue(self, ctx: CobolUnisysParser.SetByValueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#sortStatement.
    def visitSortStatement(self, ctx: CobolUnisysParser.SortStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#sortOnKeyClause.
    def visitSortOnKeyClause(self, ctx: CobolUnisysParser.SortOnKeyClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#sortDuplicatesPhrase.
    def visitSortDuplicatesPhrase(
        self, ctx: CobolUnisysParser.SortDuplicatesPhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#sortCollatingSequencePhrase.
    def visitSortCollatingSequencePhrase(
        self, ctx: CobolUnisysParser.SortCollatingSequencePhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#sortCollatingAlphanumeric.
    def visitSortCollatingAlphanumeric(
        self, ctx: CobolUnisysParser.SortCollatingAlphanumericContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#sortCollatingNational.
    def visitSortCollatingNational(
        self, ctx: CobolUnisysParser.SortCollatingNationalContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#sortInputProcedurePhrase.
    def visitSortInputProcedurePhrase(
        self, ctx: CobolUnisysParser.SortInputProcedurePhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#sortInputThrough.
    def visitSortInputThrough(self, ctx: CobolUnisysParser.SortInputThroughContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#sortUsing.
    def visitSortUsing(self, ctx: CobolUnisysParser.SortUsingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#sortOutputProcedurePhrase.
    def visitSortOutputProcedurePhrase(
        self, ctx: CobolUnisysParser.SortOutputProcedurePhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#sortOutputThrough.
    def visitSortOutputThrough(self, ctx: CobolUnisysParser.SortOutputThroughContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#sortGivingPhrase.
    def visitSortGivingPhrase(self, ctx: CobolUnisysParser.SortGivingPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#sortGiving.
    def visitSortGiving(self, ctx: CobolUnisysParser.SortGivingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#startStatement.
    def visitStartStatement(self, ctx: CobolUnisysParser.StartStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#startKey.
    def visitStartKey(self, ctx: CobolUnisysParser.StartKeyContext):
        return self.visitChildren(ctx)

    def assessStopStatement(self, ctx):
        # Intialize
        tag = "StopStatement"
        res = {}
        res["tag"] = tag
        # Get position and raw string
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        return res

    # Visit a parse tree produced by CobolUnisysParser#stopStatement.
    def visitStopStatement(self, ctx: CobolUnisysParser.StopStatementContext):
        res = self.assessStopStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)

        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#stringSendingPhrase.
    def visitStringSendingPhrase(
        self, ctx: CobolUnisysParser.StringSendingPhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#stringSending.
    def visitStringSending(self, ctx: CobolUnisysParser.StringSendingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#stringDelimitedByPhrase.
    def visitStringDelimitedByPhrase(
        self, ctx: CobolUnisysParser.StringDelimitedByPhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#stringForPhrase.
    def visitStringForPhrase(self, ctx: CobolUnisysParser.StringForPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#stringIntoPhrase.
    def visitStringIntoPhrase(self, ctx: CobolUnisysParser.StringIntoPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#stringWithPointerPhrase.
    def visitStringWithPointerPhrase(
        self, ctx: CobolUnisysParser.StringWithPointerPhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#subtractFromStatement.
    def visitSubtractFromStatement(
        self, ctx: CobolUnisysParser.SubtractFromStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#subtractFromGivingStatement.
    def visitSubtractFromGivingStatement(
        self, ctx: CobolUnisysParser.SubtractFromGivingStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#subtractCorrespondingStatement.
    def visitSubtractCorrespondingStatement(
        self, ctx: CobolUnisysParser.SubtractCorrespondingStatementContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#subtractSubtrahend.
    def visitSubtractSubtrahend(self, ctx: CobolUnisysParser.SubtractSubtrahendContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#subtractMinuend.
    def visitSubtractMinuend(self, ctx: CobolUnisysParser.SubtractMinuendContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#subtractMinuendGiving.
    def visitSubtractMinuendGiving(
        self, ctx: CobolUnisysParser.SubtractMinuendGivingContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#subtractGiving.
    def visitSubtractGiving(self, ctx: CobolUnisysParser.SubtractGivingContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#subtractMinuendCorresponding.
    def visitSubtractMinuendCorresponding(
        self, ctx: CobolUnisysParser.SubtractMinuendCorrespondingContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#terminateStatement.
    def visitTerminateStatement(self, ctx: CobolUnisysParser.TerminateStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#unstringStatement.
    def visitUnstringStatement(self, ctx: CobolUnisysParser.UnstringStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#unstringSendingPhrase.
    def visitUnstringSendingPhrase(
        self, ctx: CobolUnisysParser.UnstringSendingPhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#unstringDelimitedByPhrase.
    def visitUnstringDelimitedByPhrase(
        self, ctx: CobolUnisysParser.UnstringDelimitedByPhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#unstringOrAllPhrase.
    def visitUnstringOrAllPhrase(
        self, ctx: CobolUnisysParser.UnstringOrAllPhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#unstringIntoPhrase.
    def visitUnstringIntoPhrase(self, ctx: CobolUnisysParser.UnstringIntoPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#unstringInto.
    def visitUnstringInto(self, ctx: CobolUnisysParser.UnstringIntoContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#unstringDelimiterIn.
    def visitUnstringDelimiterIn(
        self, ctx: CobolUnisysParser.UnstringDelimiterInContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#unstringCountIn.
    def visitUnstringCountIn(self, ctx: CobolUnisysParser.UnstringCountInContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#unstringWithPointerPhrase.
    def visitUnstringWithPointerPhrase(
        self, ctx: CobolUnisysParser.UnstringWithPointerPhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#unstringTallyingPhrase.
    def visitUnstringTallyingPhrase(
        self, ctx: CobolUnisysParser.UnstringTallyingPhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#useStatement.
    def visitUseStatement(self, ctx: CobolUnisysParser.UseStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#useAfterClause.
    def visitUseAfterClause(self, ctx: CobolUnisysParser.UseAfterClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#useAfterOn.
    def visitUseAfterOn(self, ctx: CobolUnisysParser.UseAfterOnContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#useDebugClause.
    def visitUseDebugClause(self, ctx: CobolUnisysParser.UseDebugClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#useDebugOn.
    def visitUseDebugOn(self, ctx: CobolUnisysParser.UseDebugOnContext):
        return self.visitChildren(ctx)

    def assessWriteStatement(self, ctx: CobolUnisysParser.WriteStatementContext):
        tag = "WriteStatement"
        res = {}

        start_token = ctx.start
        stop_token = ctx.stop

        res["tag"] = tag
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            self.parser, start_token.tokenIndex, stop_token.tokenIndex
        )

        record_name = ctx.recordName()
        res["record_name"] = record_name.getText()

        write_from = ctx.writeFromPhrase()
        if write_from:
            res["write_from_phrase"] = {}

            res["write_from_phrase"]["identifier"] = (
                write_from.identifier().getText() if write_from.identifier() else None
            )
            res["write_from_phrase"]["literal"] = (
                write_from.literal().getText() if write_from.literal() else None
            )

        write_advancing_phrase = ctx.writeAdvancingPhrase()
        if write_advancing_phrase:
            res["write_advancing_phrase"] = {}
            res["write_advancing_phrase"]["position"] = (
                write_advancing_phrase.getChild(0).getText().upper()
            )
            advancing_type = (
                write_advancing_phrase.ADVANCING().getText().upper()
                if write_advancing_phrase.ADVANCING()
                else None
            )
            advancing_type = (
                advancing_type or write_advancing_phrase.CHANNEL().getText().upper()
                if write_advancing_phrase.CHANNEL()
                else None
            )
            res["write_advancing_phrase"]["advancing_type"] = advancing_type

            write_advancing_page = write_advancing_phrase.writeAdvancingPage()
            if write_advancing_page:
                res["write_advancing_phrase"]["advancing"] = "PAGE"

            write_advancing_lines = write_advancing_phrase.writeAdvancingLines()
            if write_advancing_lines:
                res["write_advancing_phrase"]["advancing"] = {
                    "identifier": (
                        write_advancing_lines.identifier().getText()
                        if write_advancing_lines.identifier()
                        else None
                    ),
                    "literal": (
                        write_advancing_lines.literal().getText()
                        if write_advancing_lines.literal()
                        else None
                    ),
                }

            write_advancing_mnemonic = write_advancing_phrase.writeAdvancingMnemonic()
            if write_advancing_mnemonic:
                res["write_advancing_phrase"]["advancing"] = {}
                res["write_advancing_phrase"]["advancing"][
                    "mnemonic_name"
                ] = write_advancing_mnemonic.getText().upper()

        write_at_end_of_page_phrase = ctx.writeAtEndOfPagePhrase()
        if write_at_end_of_page_phrase:
            res["write_at_end_of_page_phrase"] = []
            statement = write_at_end_of_page_phrase.statement()
            if statement:
                for st in statement:
                    start_idx = st.start.tokenIndex
                    stop_idx = st.stop.tokenIndex
                    c = st.getChild(0)
                    type_ = type(c).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        res["write_at_end_of_page_phrase"].append(f(c))

        write_not_at_end_of_page_phrase = ctx.writeNotAtEndOfPagePhrase()
        if write_not_at_end_of_page_phrase:
            res["not_invalid_key_phrase"] = []
            statement = write_not_at_end_of_page_phrase.statement()
            if statement:
                for st in statement:
                    start_idx = st.start.tokenIndex
                    stop_idx = st.stop.tokenIndex
                    c = st.getChild(0)
                    type_ = type(c).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        res["write_not_at_end_of_page_phrase"].append(f(c))

        # invalidKeyPhrase
        invalidKeyPhrase = ctx.invalidKeyPhrase()
        if invalidKeyPhrase:
            res["invalid_key_phrase"] = []
            statement = invalidKeyPhrase.statement()
            if statement:
                for st in statement:
                    start_idx = st.start.tokenIndex
                    stop_idx = st.stop.tokenIndex
                    c = st.getChild(0)
                    type_ = type(c).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        res["invalid_key_phrase"].append(f(c))

        # notInvalidKeyPhrase
        notInvalidKeyPhrase = ctx.notInvalidKeyPhrase()
        if notInvalidKeyPhrase:
            res["not_invalid_key_phrase"] = []
            statement = notInvalidKeyPhrase.statement()
            if statement:
                for st in statement:
                    start_idx = st.start.tokenIndex
                    stop_idx = st.stop.tokenIndex
                    c = st.getChild(0)
                    type_ = type(c).__name__
                    if type_ in self.func:
                        f = self.func[type_]
                        res["not_invalid_key_phrase"].append(f(c))

        return res

    # Visit a parse tree produced by CobolUnisysParser#writeStatement.
    def visitWriteStatement(self, ctx: CobolUnisysParser.WriteStatementContext):
        res = self.assessWriteStatement(ctx)
        section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
            self.parser, ctx
        )
        res.update(section_paragraph_info_dict)
        grandparent = ctx.parentCtx.parentCtx
        if isinstance(grandparent, CobolUnisysParser.SentenceContext):
            self.statements.append(res)

        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#writeFromPhrase.
    def visitWriteFromPhrase(self, ctx: CobolUnisysParser.WriteFromPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#writeAdvancingPhrase.
    def visitWriteAdvancingPhrase(
        self, ctx: CobolUnisysParser.WriteAdvancingPhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#writeAdvancingPage.
    def visitWriteAdvancingPage(self, ctx: CobolUnisysParser.WriteAdvancingPageContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#writeAdvancingLines.
    def visitWriteAdvancingLines(
        self, ctx: CobolUnisysParser.WriteAdvancingLinesContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#writeAdvancingMnemonic.
    def visitWriteAdvancingMnemonic(
        self, ctx: CobolUnisysParser.WriteAdvancingMnemonicContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#writeAtEndOfPagePhrase.
    def visitWriteAtEndOfPagePhrase(
        self, ctx: CobolUnisysParser.WriteAtEndOfPagePhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#writeNotAtEndOfPagePhrase.
    def visitWriteNotAtEndOfPagePhrase(
        self, ctx: CobolUnisysParser.WriteNotAtEndOfPagePhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#atEndPhrase.
    def visitAtEndPhrase(self, ctx: CobolUnisysParser.AtEndPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#notAtEndPhrase.
    def visitNotAtEndPhrase(self, ctx: CobolUnisysParser.NotAtEndPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#invalidKeyPhrase.
    def visitInvalidKeyPhrase(self, ctx: CobolUnisysParser.InvalidKeyPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#notInvalidKeyPhrase.
    def visitNotInvalidKeyPhrase(
        self, ctx: CobolUnisysParser.NotInvalidKeyPhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#onOverflowPhrase.
    def visitOnOverflowPhrase(self, ctx: CobolUnisysParser.OnOverflowPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#notOnOverflowPhrase.
    def visitNotOnOverflowPhrase(
        self, ctx: CobolUnisysParser.NotOnOverflowPhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#onSizeErrorPhrase.
    def visitOnSizeErrorPhrase(self, ctx: CobolUnisysParser.OnSizeErrorPhraseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#notOnSizeErrorPhrase.
    def visitNotOnSizeErrorPhrase(
        self, ctx: CobolUnisysParser.NotOnSizeErrorPhraseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#onExceptionClause.
    def visitOnExceptionClause(self, ctx: CobolUnisysParser.OnExceptionClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#notOnExceptionClause.
    def visitNotOnExceptionClause(
        self, ctx: CobolUnisysParser.NotOnExceptionClauseContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#arithmeticExpression.
    def visitArithmeticExpression(
        self, ctx: CobolUnisysParser.ArithmeticExpressionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#plusMinus.
    def visitPlusMinus(self, ctx: CobolUnisysParser.PlusMinusContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#multDivs.
    def visitMultDivs(self, ctx: CobolUnisysParser.MultDivsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#multDiv.
    def visitMultDiv(self, ctx: CobolUnisysParser.MultDivContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#powers.
    def visitPowers(self, ctx: CobolUnisysParser.PowersContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#power.
    def visitPower(self, ctx: CobolUnisysParser.PowerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#basis.
    def visitBasis(self, ctx: CobolUnisysParser.BasisContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#condition.
    def visitCondition(self, ctx: CobolUnisysParser.ConditionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#andOrCondition.
    def visitAndOrCondition(self, ctx: CobolUnisysParser.AndOrConditionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#combinableCondition.
    def visitCombinableCondition(
        self, ctx: CobolUnisysParser.CombinableConditionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#simpleCondition.
    def visitSimpleCondition(self, ctx: CobolUnisysParser.SimpleConditionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#classCondition.
    def visitClassCondition(self, ctx: CobolUnisysParser.ClassConditionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#conditionNameReference.
    def visitConditionNameReference(
        self, ctx: CobolUnisysParser.ConditionNameReferenceContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#conditionNameSubscriptReference.
    def visitConditionNameSubscriptReference(
        self, ctx: CobolUnisysParser.ConditionNameSubscriptReferenceContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#relationCondition.
    def visitRelationCondition(self, ctx: CobolUnisysParser.RelationConditionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#relationSignCondition.
    def visitRelationSignCondition(
        self, ctx: CobolUnisysParser.RelationSignConditionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#relationArithmeticComparison.
    def visitRelationArithmeticComparison(
        self, ctx: CobolUnisysParser.RelationArithmeticComparisonContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#relationCombinedComparison.
    def visitRelationCombinedComparison(
        self, ctx: CobolUnisysParser.RelationCombinedComparisonContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#relationCombinedCondition.
    def visitRelationCombinedCondition(
        self, ctx: CobolUnisysParser.RelationCombinedConditionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#relationalOperator.
    def visitRelationalOperator(self, ctx: CobolUnisysParser.RelationalOperatorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#abbreviation.
    def visitAbbreviation(self, ctx: CobolUnisysParser.AbbreviationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#identifier.
    def visitIdentifier(self, ctx: CobolUnisysParser.IdentifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#tableCall.
    def visitTableCall(self, ctx: CobolUnisysParser.TableCallContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#functionCall.
    def visitFunctionCall(self, ctx: CobolUnisysParser.FunctionCallContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#referenceModifier.
    def visitReferenceModifier(self, ctx: CobolUnisysParser.ReferenceModifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#characterPosition.
    def visitCharacterPosition(self, ctx: CobolUnisysParser.CharacterPositionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#length.
    def visitLength(self, ctx: CobolUnisysParser.LengthContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#subscript_.
    def visitSubscript_(self, ctx: CobolUnisysParser.Subscript_Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#argument.
    def visitArgument(self, ctx: CobolUnisysParser.ArgumentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#qualifiedDataName.
    def visitQualifiedDataName(self, ctx: CobolUnisysParser.QualifiedDataNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#qualifiedDataNameFormat1.
    def visitQualifiedDataNameFormat1(
        self, ctx: CobolUnisysParser.QualifiedDataNameFormat1Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#qualifiedDataNameFormat2.
    def visitQualifiedDataNameFormat2(
        self, ctx: CobolUnisysParser.QualifiedDataNameFormat2Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#qualifiedDataNameFormat3.
    def visitQualifiedDataNameFormat3(
        self, ctx: CobolUnisysParser.QualifiedDataNameFormat3Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#qualifiedDataNameFormat4.
    def visitQualifiedDataNameFormat4(
        self, ctx: CobolUnisysParser.QualifiedDataNameFormat4Context
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#qualifiedInData.
    def visitQualifiedInData(self, ctx: CobolUnisysParser.QualifiedInDataContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#inData.
    def visitInData(self, ctx: CobolUnisysParser.InDataContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#inFile.
    def visitInFile(self, ctx: CobolUnisysParser.InFileContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#inMnemonic.
    def visitInMnemonic(self, ctx: CobolUnisysParser.InMnemonicContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#inSection.
    def visitInSection(self, ctx: CobolUnisysParser.InSectionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#inLibrary.
    def visitInLibrary(self, ctx: CobolUnisysParser.InLibraryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#inTable.
    def visitInTable(self, ctx: CobolUnisysParser.InTableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#alphabetName.
    def visitAlphabetName(self, ctx: CobolUnisysParser.AlphabetNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#assignmentName.
    def visitAssignmentName(self, ctx: CobolUnisysParser.AssignmentNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#basisName.
    def visitBasisName(self, ctx: CobolUnisysParser.BasisNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#cdName.
    def visitCdName(self, ctx: CobolUnisysParser.CdNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#className.
    def visitClassName(self, ctx: CobolUnisysParser.ClassNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#computerName.
    def visitComputerName(self, ctx: CobolUnisysParser.ComputerNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#conditionName.
    def visitConditionName(self, ctx: CobolUnisysParser.ConditionNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataName.
    def visitDataName(self, ctx: CobolUnisysParser.DataNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#dataDescName.
    def visitDataDescName(self, ctx: CobolUnisysParser.DataDescNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#environmentName.
    def visitEnvironmentName(self, ctx: CobolUnisysParser.EnvironmentNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#fileName.
    def visitFileName(self, ctx: CobolUnisysParser.FileNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#functionName.
    def visitFunctionName(self, ctx: CobolUnisysParser.FunctionNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#indexName.
    def visitIndexName(self, ctx: CobolUnisysParser.IndexNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#languageName.
    def visitLanguageName(self, ctx: CobolUnisysParser.LanguageNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#libraryName.
    def visitLibraryName(self, ctx: CobolUnisysParser.LibraryNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#localName.
    def visitLocalName(self, ctx: CobolUnisysParser.LocalNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#mnemonicName.
    def visitMnemonicName(self, ctx: CobolUnisysParser.MnemonicNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#paragraphName.
    def visitParagraphName(self, ctx: CobolUnisysParser.ParagraphNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#procedureName.
    def visitProcedureName(self, ctx: CobolUnisysParser.ProcedureNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#programName.
    def visitProgramName(self, ctx: CobolUnisysParser.ProgramNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#recordName.
    def visitRecordName(self, ctx: CobolUnisysParser.RecordNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#reportName.
    def visitReportName(self, ctx: CobolUnisysParser.ReportNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#routineName.
    def visitRoutineName(self, ctx: CobolUnisysParser.RoutineNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#screenName.
    def visitScreenName(self, ctx: CobolUnisysParser.ScreenNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#sectionName.
    def visitSectionName(self, ctx: CobolUnisysParser.SectionNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#systemName.
    def visitSystemName(self, ctx: CobolUnisysParser.SystemNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#symbolicCharacter.
    def visitSymbolicCharacter(self, ctx: CobolUnisysParser.SymbolicCharacterContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#textName.
    def visitTextName(self, ctx: CobolUnisysParser.TextNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#booleanLiteral.
    def visitBooleanLiteral(self, ctx: CobolUnisysParser.BooleanLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#numericLiteral.
    def visitNumericLiteral(self, ctx: CobolUnisysParser.NumericLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#integerLiteral.
    def visitIntegerLiteral(self, ctx: CobolUnisysParser.IntegerLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#cicsDfhRespLiteral.
    def visitCicsDfhRespLiteral(self, ctx: CobolUnisysParser.CicsDfhRespLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#cicsDfhValueLiteral.
    def visitCicsDfhValueLiteral(
        self, ctx: CobolUnisysParser.CicsDfhValueLiteralContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#figurativeConstant.
    def visitFigurativeConstant(self, ctx: CobolUnisysParser.FigurativeConstantContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#specialRegister.
    def visitSpecialRegister(self, ctx: CobolUnisysParser.SpecialRegisterContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CobolUnisysParser#commentEntry.
    def visitCommentEntry(self, ctx: CobolUnisysParser.CommentEntryContext):
        return self.visitChildren(ctx)
