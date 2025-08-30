from typing import List, Union

from antlr4 import ParserRuleContext
from antlr4.tree.Tree import TerminalNodeImpl
from loguru import logger

from grammar.copybook.CopyBookParser import CopyBookParser
from grammar.ibm_cobol.Cobol85Parser import Cobol85Parser
from grammar.utils import (
    get_original_code_content,
    get_paragraph_section_of_cobol_statement,
)

logger.add("out.log", backtrace=True, diagnose=True)


class CobolStatementAssessor:
    def __init__(self) -> None:
        self.func = {
            "AcceptStatementContext": self.assess_accept_statement,
            "AcceptFromDateStatementContext": self.assess_accept_from_date_statement,
            "AcceptMessageCountStatementContext": self.assess_accept_from_message_count_statement,
            "AcceptFromMnemonicStatementContext": self.assess_accept_from_mnemonic_statement,
            "AcceptFromEscapeKeyStatementContext": self.assess_accept_from_escape_key_statement,
            "AddStatementContext": self.assess_add_statement,
            "AlterStatementContext": self.assess_alter_statement,
            "CallStatementContext": self.assess_call_statement,
            "CancelStatementContext": self.assess_cancel_statement,
            "CloseStatementContext": self.assess_close_statement,
            "ComputeStatementContext": self.assess_compute_statement,
            "ContinueStatementContext": self.assess_continue_statement,
            "CopyStatementContext": self.assess_copy_statement,
            "DisplayStatementContext": self.assess_display_statement,
            "DivideStatementContext": self.assess_divide_statement,
            "DeleteStatementContext": self.assess_delete_statement,
            "EvaluateStatementContext": self.assess_evaluate_statement,
            "ExecCicsStatement2Context": self.assess_exec_cics_statement2,
            "ExecSqlStatement2Context": self.assess_exec_sql_statement2,
            "ExitStatementContext": self.assess_exit_statement,
            "GoToStatementContext": self.assess_go_to_statement,
            "GobackStatementContext": self.assess_goback_statement,
            "InitializeStatementContext": self.assess_initialize_statement,
            "InspectStatementContext": self.assess_inspect_statement,
            "MoveStatementContext": self.assess_move_statement,
            "MultiplyStatementContext": self.assess_multiply_statement,
            "SearchStatementContext": self.assess_search_statement,
            "StringStatementContext": self.assess_string_statement,
            "SubtractStatementContext": self.assess_subtract_statement,
            "SetStatementContext": self.assess_set_statement,
            "StartStatementContext": self.assess_start_statement,
            "StopStatementContext": self.assess_stop_statement,
            "SortStatementContext": self.assess_sort_statement,
            "WriteStatementContext": self.assess_write_statement,
            "OpenStatementContext": self.assess_open_statement,
            "IfStatementContext": self.assess_if_statement,
            "PerformStatementContext": self.assess_perform_statement,
            "ReadStatementContext": self.assess_read_statement,
            "ReleaseStatementContext": self.assess_release_statement,
            "ReturnStatementContext": self.assess_return_statement,
            "RewriteStatementContext": self.assess_rewrite_statement,
            "UnstringStatementContext": self.assess_unstring_statement,
        }

    def assess_statement(self, ctx: ParserRuleContext):
        """Extract information of a statement context in COBOL or Copybook. Do not pass statement context of other languages.

        Args:
            ctx (ParserRuleContext): The statement context of COBOL or Copybook to be assessed.

        Returns:
            dict: The assessment result of the statement context.
        """
        # get the type of the statement
        if isinstance(
            ctx, (Cobol85Parser.StatementContext, CopyBookParser.StatementContext)
        ):
            ctx = ctx.getChild(0)

        statement_type = type(ctx).__name__
        if statement_type in self.func:
            f = self.func[statement_type]
            statement_dict = f(ctx)

            section_paragraph_info_dict = get_paragraph_section_of_cobol_statement(
                ctx.parser, ctx  # type: ignore
            )
            statement_dict.update(section_paragraph_info_dict)
            return statement_dict

        logger.warning(f"Statement assessment not implemented: '{statement_type}'")
        return {}

    def _extract_statement_metadata(self, ctx: ParserRuleContext) -> dict:
        res = {}
        tag = type(ctx).__name__.replace("Context", "")
        res["tag"] = tag
        start_token = ctx.start
        stop_token = ctx.stop
        res["start_line"] = start_token.line
        res["stop_line"] = stop_token.line
        res["start_idx"] = start_token.start
        res["stop_idx"] = stop_token.stop
        res["raw"] = get_original_code_content(
            ctx.parser, start_token.tokenIndex, stop_token.tokenIndex  # type: ignore
        )
        return res

    def _assess_nested_statements(self, ctx) -> List[dict]:
        if not hasattr(ctx, "statement"):
            logger.exception(
                f"Context does not have statement attribute: {type(ctx).__name__}"
            )
            return []

        if not isinstance(ctx.statement(), list):
            logger.warning(
                f"Context statement attribute is not a list: {type(ctx).__name__}"
            )
            return []

        statements = []

        for statement_ctx in ctx.statement():
            statement = self.assess_statement(statement_ctx)
            if statement:
                statements.append(statement)

        return statements

    def assess_accept_statement(
        self,
        ctx: Union[
            Cobol85Parser.AcceptStatementContext, CopyBookParser.AcceptStatementContext
        ],
    ):
        identifier = ctx.identifier()

        metadata = self._extract_statement_metadata(ctx)

        res = {
            "identifier": identifier.getText() if identifier else "",
        }

        res.update(metadata)

        accept_type_ctx = ctx.getChild(2)
        child_res = self.assess_statement(accept_type_ctx)
        if child_res:
            res.update(child_res)

        on_size_error_phrase = ctx.onExceptionClause()
        if on_size_error_phrase:
            res["on_exception_clause"] = self._assess_nested_statements(
                on_size_error_phrase
            )

        not_on_size_error_phrase = ctx.notOnExceptionClause()
        if not_on_size_error_phrase:
            res["not_on_exception_clause"] = self._assess_nested_statements(
                not_on_size_error_phrase
            )

        return res

    def assess_accept_from_date_statement(
        self,
        ctx: Union[
            Cobol85Parser.AcceptFromDateStatementContext,
            CopyBookParser.AcceptFromDateStatementContext,
        ],
    ):
        tag = "AcceptFromDateStatement"

        # fix missing code by getting the parent code
        accept_statement_context = ctx.parentCtx

        identifier = accept_statement_context.identifier()

        date = ""

        for i, child in enumerate(ctx.getChildren()):
            # skip FROM token
            if i == 0:
                continue

            date += " " + child.getText()

        date = date.strip()

        if not date:
            raw = get_original_code_content(
                ctx.parser, ctx.start.tokenIndex, ctx.stop.tokenIndex
            )
            logger.warning(f"Date is missing in accept from date statement'{raw}'")

        return {
            "tag": tag,
            "identifier": identifier.getText() if identifier else "",
            "datetime": date,
        }

    def assess_accept_from_message_count_statement(
        self,
        ctx: Union[
            Cobol85Parser.AcceptMessageCountStatementContext,
            CopyBookParser.AcceptMessageCountStatementContext,
        ],
    ):
        tag = "AcceptFromMessageCountStatement"

        accept_statement_context = ctx.parentCtx
        identifier = accept_statement_context.identifier()

        return {
            "tag": tag,
            "identifier": identifier.getText() if identifier else "",
        }

    def assess_accept_from_mnemonic_statement(
        self,
        ctx: Union[
            Cobol85Parser.AcceptFromMnemonicStatementContext,
            CopyBookParser.AcceptFromMnemonicStatementContext,
        ],
    ):
        tag = "AcceptFromMnemonicStatement"
        mnemonic = ctx.getChild(1)

        accept_statement_context = ctx.parentCtx

        identifier = accept_statement_context.identifier()

        return {
            "tag": tag,
            "identifier": identifier.getText() if identifier else "",
            "mnemonic_name": mnemonic.getText() if mnemonic else "",
        }

    def assess_accept_from_escape_key_statement(
        self,
        ctx: Union[
            Cobol85Parser.AcceptFromEscapeKeyStatementContext,
            CopyBookParser.AcceptFromEscapeKeyStatementContext,
        ],
    ):
        tag = "AcceptFromEscapeKeyStatement"

        accept_statement_context: Cobol85Parser.AcceptStatementContext = ctx.parentCtx
        identifier = accept_statement_context.identifier()

        return {
            "tag": tag,
            "identifier": identifier.getText() if identifier else "",
        }

    def assess_evaluate_statement(
        self,
        ctx: Union[
            Cobol85Parser.EvaluateStatementContext,
            CopyBookParser.EvaluateStatementContext,
        ],
    ):
        # Intialize
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

        evaluate_select = ctx.evaluateSelect()

        if evaluate_select.identifier():
            res["evaluate_identifier"] = evaluate_select.identifier()[0].getText()
        elif evaluate_select.literal():
            res["evaluate_literal"] = get_original_code_content(
                ctx.parser,
                evaluate_select.start.tokenIndex,
                evaluate_select.stop.tokenIndex,
            )

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
                        evaluateCondition = ew.evaluateCondition()
                        # r["evaluateWhen"].append(self.code[start_idx:stop_idx+1])
                        r["evaluateWhen"].append(evaluateCondition.getText())

                r["statement"] = self._assess_nested_statements(ewp)

                # Update
                res["evaluateWhenPhrase"].append(r)

        # evaluateWhenOther
        evaluateWhenOther = ctx.evaluateWhenOther()
        if evaluateWhenOther:
            res["evaluateWhenOther"] = []

        return res

    def assess_add_statement(
        self,
        ctx: Union[
            Cobol85Parser.AddStatementContext, CopyBookParser.AddStatementContext
        ],
    ):
        # Intialize
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

        # Get all children of context
        children = ctx.getChildren()
        children = [type(c) for c in children]

        # AddTo
        if (
            Cobol85Parser.AddToStatementContext in children
            or CopyBookParser.AddToStatementContext in children
        ):
            addToStatement = ctx.addToStatement()
            # addFrom
            addFrom = addToStatement.addFrom()
            if addFrom:
                res["identifier_1"] = []
                res["literal_1"] = []
                for af in addFrom:
                    for a in af.getChildren():
                        if isinstance(
                            a,
                            (
                                Cobol85Parser.IdentifierContext,
                                CopyBookParser.IdentifierContext,
                            ),
                        ):
                            # res["identifier_1"].append(a.getText())
                            res["identifier_1"].append(
                                get_original_code_content(
                                    ctx.parser,
                                    a.start.tokenIndex,
                                    a.stop.tokenIndex,
                                )
                            )
                        elif isinstance(a, Cobol85Parser.LiteralContext):
                            res["literal_1"].append(a.getText())
            # addTo
            addTo = addToStatement.addTo()
            if addTo:
                res["identifier_2"] = []
                res["literal_2"] = []
                for at in addTo:
                    for a in at.getChildren():
                        if isinstance(
                            a,
                            (
                                Cobol85Parser.IdentifierContext,
                                CopyBookParser.IdentifierContext,
                            ),
                        ):
                            # res["identifier_2"].append(a.getText())
                            res["identifier_2"].append(
                                get_original_code_content(
                                    ctx.parser,
                                    a.start.tokenIndex,
                                    a.stop.tokenIndex,
                                )
                            )
                        elif isinstance(
                            a,
                            (
                                Cobol85Parser.LiteralContext,
                                CopyBookParser.LiteralContext,
                            ),
                        ):
                            res["literal_2"].append(a.getText())
                        elif isinstance(
                            a,
                            (
                                Cobol85Parser.FigurativeConstantContext,
                                CopyBookParser.FigurativeConstantContext,
                            ),
                        ):
                            res["literal_2"].append(a.getText())

        # AddToGiving
        elif (
            Cobol85Parser.AddToGivingStatementContext in children
            or CopyBookParser.AddToGivingStatementContext in children
        ):
            addToGivingStatement = ctx.addToGivingStatement()
            # addFrom
            addFrom = addToGivingStatement.addFrom()
            if addFrom:
                res["identifier_1"] = []
                res["literal_1"] = []
                for af in addFrom:
                    for a in af.getChildren():
                        if isinstance(
                            a,
                            (
                                Cobol85Parser.IdentifierContext,
                                CopyBookParser.IdentifierContext,
                            ),
                        ):
                            # res["identifier_1"].append(a.getText())
                            res["identifier_1"].append(
                                get_original_code_content(
                                    ctx.parser,
                                    a.start.tokenIndex,
                                    a.stop.tokenIndex,
                                )
                            )
                        elif isinstance(
                            a,
                            (
                                Cobol85Parser.LiteralContext,
                                CopyBookParser.LiteralContext,
                            ),
                        ):
                            res["literal_1"].append(a.getText())
            # addToGiving
            addToGiving = addToGivingStatement.addToGiving()
            if addToGiving:
                res["identifier_2"] = []
                res["literal_2"] = []
                for at in addToGiving:
                    for a in at.getChildren():
                        if isinstance(
                            a,
                            (
                                Cobol85Parser.IdentifierContext,
                                CopyBookParser.IdentifierContext,
                            ),
                        ):
                            # res["identifier_2"].append(a.getText())
                            res["identifier_2"].append(
                                get_original_code_content(
                                    ctx.parser,
                                    a.start.tokenIndex,
                                    a.stop.tokenIndex,
                                )
                            )
                        elif isinstance(
                            a,
                            (
                                Cobol85Parser.LiteralContext,
                                CopyBookParser.LiteralContext,
                            ),
                        ):
                            res["literal_2"].append(a.getText())
                        elif isinstance(
                            a,
                            (
                                Cobol85Parser.FigurativeConstantContext,
                                CopyBookParser.FigurativeConstantContext,
                            ),
                        ):
                            res["literal_2"].append(a.getText())
            # addGiving
            addGiving = addToGivingStatement.addGiving()
            if addGiving:
                res["identifier_3"] = []
                res["literal_3"] = []
                for ag in addGiving:
                    for a in ag.getChildren():
                        if isinstance(a, Cobol85Parser.IdentifierContext):
                            # res["identifier_3"].append(a.getText())
                            res["identifier_3"].append(
                                get_original_code_content(
                                    ctx.parser,
                                    a.start.tokenIndex,
                                    a.stop.tokenIndex,
                                )
                            )
                        elif isinstance(a, Cobol85Parser.LiteralContext):
                            res["literal_3"].append(a.getText())

        return res

    def assess_alter_statement(
        self,
        ctx: Union[
            Cobol85Parser.AlterStatementContext, CopyBookParser.AlterStatementContext
        ],
    ):
        # Intialize
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

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
        return res

    def assess_call_statement(
        self,
        ctx: Union[
            Cobol85Parser.CallStatementContext, CopyBookParser.CallStatementContext
        ],
    ):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

        res["call_identifiers"] = []  # Set default value as empty

        # Get all children of context
        children = ctx.getChildren()
        children = [type(c) for c in children]

        # literal_1
        if (
            Cobol85Parser.LiteralContext in children
            or CopyBookParser.LiteralContext in children
        ):
            literal = ctx.literal()
            res["call_literal"] = literal.getText()

        # identifier_1
        elif (
            Cobol85Parser.IdentifierContext in children
            or CopyBookParser.IdentifierContext in children
        ):
            identifier = ctx.identifier()
            # res["identifier_1"] = identifier.getText()
            res["call_identifiers"].append(
                get_original_code_content(
                    ctx.parser,
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
            call_using_parameter_list = callUsingPhrase.callUsingParameter()

            for call_using_parameter in call_using_parameter_list:
                call_using_parameter = call_using_parameter.getChild(0)

                if isinstance(
                    call_using_parameter, Cobol85Parser.CallByReferencePhraseContext
                ):
                    call_by_reference_list = call_using_parameter.callByReference()

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
                            if isinstance(literal, TerminalNodeImpl):
                                res["using_literals"].append(
                                    get_original_code_content(
                                        ctx.parser,
                                        literal.symbol.tokenIndex,
                                        literal.symbol.tokenIndex,
                                    )
                                )
                            else:
                                res["using_literals"].append(
                                    get_original_code_content(
                                        ctx.parser,
                                        literal.start.tokenIndex,
                                        literal.stop.tokenIndex,
                                    )
                                )

                elif isinstance(
                    call_using_parameter, Cobol85Parser.CallByValuePhraseContext
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
                    call_using_parameter, Cobol85Parser.CallByContentPhraseContext
                ):
                    call_by_content_list = call_using_parameter.callByContent()
                    for call_by_content in call_by_content_list:
                        identifier = call_by_content.identifier()
                        if identifier:
                            res["using_identifiers"].append(identifier.getText())

                        literal = call_by_content.literal() or call_by_content.OMITTED()
                        if literal:
                            if isinstance(literal, TerminalNodeImpl):
                                res["using_literals"].append(
                                    get_original_code_content(
                                        ctx.parser,
                                        literal.symbol.tokenIndex,
                                        literal.symbol.tokenIndex,
                                    )
                                )
                            else:
                                res["using_literals"].append(
                                    get_original_code_content(
                                        ctx.parser,
                                        literal.start.tokenIndex,
                                        literal.stop.tokenIndex,
                                    )
                                )

        call_giving_phrase = ctx.callGivingPhrase()

        if call_giving_phrase:
            res["giving_identifier"] = call_giving_phrase.identifier().getText()

        # ibm has no call system
        res["call_type"] = None

        return res

    def assess_cancel_statement(
        self,
        ctx: Union[
            Cobol85Parser.CancelStatementContext, CopyBookParser.CancelStatementContext
        ],
    ):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

        cancel_call_list = ctx.cancelCall()

        res["program_names"] = []

        for cancel_call in cancel_call_list:
            res["program_names"].append(
                get_original_code_content(
                    ctx.parser,
                    cancel_call.start.tokenIndex,
                    cancel_call.stop.tokenIndex,
                )
            )

        return res

    def assess_close_statement(
        self,
        ctx: Union[
            Cobol85Parser.CloseStatementContext, CopyBookParser.CloseStatementContext
        ],
    ):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

        # closeFile
        res["close_files"] = []
        close_files_ctx = ctx.closeFile()

        for close_file_ctx in close_files_ctx:
            close_file_details = {}

            file_name = close_file_ctx.fileName()
            close_file_details["file_name"] = file_name.getText()

            close_file_details["close_option"] = None

            close_file_details["on_exception_clause"] = []

            res["close_files"].append(close_file_details)

        return res

    def assess_compute_statement(
        self,
        ctx: Union[
            Cobol85Parser.ComputeStatementContext,
            CopyBookParser.ComputeStatementContext,
        ],
    ):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

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
        return res

    def assess_continue_statement(
        self,
        ctx: Union[
            Cobol85Parser.ContinueStatementContext,
            CopyBookParser.ContinueStatementContext,
        ],
    ):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)
        return res

    def assess_copy_statement(
        self,
        ctx: Union[
            Cobol85Parser.CopyStatementContext, CopyBookParser.CopyStatementContext
        ],
    ):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

        copySource = ctx.copySource()
        if copySource:
            # Get all children of context
            children = copySource.getChildren()
            children = [type(c) for c in children]
            # Cobol85Parser.LiteralContext
            if Cobol85Parser.LiteralContext in children:
                literal = copySource.literal()
                res["literal_1"] = literal.getText()
            # Cobol85Parser.CobolWordContext
            elif Cobol85Parser.CobolWordContext in children:
                cobolWord = copySource.cobolWord()
                res["text_name"] = cobolWord.getText()
            # Cobol85Parser.FileNameContext
            elif Cobol85Parser.FileNameContext in children:
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
        return res

    def assess_display_statement(
        self,
        ctx: Union[
            Cobol85Parser.DisplayStatementContext,
            CopyBookParser.DisplayStatementContext,
        ],
    ):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

        displayOperand = ctx.displayOperand()
        if displayOperand:
            res["identifier_1"] = []
            res["literal_1"] = []
            for do in displayOperand:
                for d in do.getChildren():
                    if isinstance(d, Cobol85Parser.IdentifierContext):
                        res["identifier_1"].append(
                            get_original_code_content(
                                ctx.parser, d.start.tokenIndex, d.stop.tokenIndex
                            )
                        )
                    elif isinstance(d, Cobol85Parser.LiteralContext):
                        res["literal_1"].append(d.getText())
        return res

    def assess_divide_statement(
        self,
        ctx: Union[
            Cobol85Parser.DivideStatementContext, CopyBookParser.DivideStatementContext
        ],
    ):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

        divide_statement = ctx.getChild(2)

        if isinstance(
            divide_statement,
            (
                Cobol85Parser.DivideIntoStatementContext,
                Cobol85Parser.DivideIntoStatementContext,
            ),
        ):
            res["divide_type"] = "INTO"

            divisor_identifier = ctx.identifier()
            res["divisor_identifier"] = (
                divisor_identifier.getText() if divisor_identifier else None
            )

            divisor_literal = ctx.literal()
            res["divisor_literal"] = (
                divisor_literal.getText() if divisor_literal else None
            )

            divide_into_list = divide_statement.divideInto()
            res["dividend_identifiers"] = [
                divide_into.identifier().getText() for divide_into in divide_into_list
            ]
            # the result of the division is stored in the corresponding dividend
            res["results"] = res["dividend_identifiers"]

        elif isinstance(
            divide_statement,
            (
                Cobol85Parser.DivideIntoGivingStatementContext,
                Cobol85Parser.DivideIntoGivingStatementContext,
            ),
        ):
            res["divide_type"] = "INTO"

            divisor_identifier = ctx.identifier()
            res["divisor_identifier"] = (
                divisor_identifier.getText() if divisor_identifier else None
            )

            divisor_literal = ctx.literal()
            res["divisor_literal"] = (
                divisor_literal.getText() if divisor_literal else None
            )

            res["dividend_identifiers"] = (
                [divide_statement.identifier().getText()]
                if divide_statement.identifier()
                else []
            )
            res["dividend_literal"] = (
                divide_statement.literal().getText()
                if divide_statement.literal()
                else None
            )

            # the results of the division are stored in the giving identifiers
            divide_giving_phrase = divide_statement.divideGivingPhrase()
            if divide_giving_phrase:
                divide_giving_list: List[Cobol85Parser.DivideGivingContext] = (
                    divide_giving_phrase.divideGiving()
                )
                res["results"] = [
                    divide_giving.identifier().getText()
                    for divide_giving in divide_giving_list
                ]

        elif isinstance(
            divide_statement,
            (
                Cobol85Parser.DivideByGivingStatementContext,
                Cobol85Parser.DivideByGivingStatementContext,
            ),
        ):
            res["divide_type"] = "BY"

            dividend_identifier = ctx.identifier()
            dividend_literal = ctx.literal()
            if dividend_identifier:
                res["dividend_identifiers"] = [dividend_identifier.getText()]
            if dividend_literal:
                res["dividend_literal"] = get_original_code_content(
                    ctx.parser,
                    dividend_literal.start.tokenIndex,
                    dividend_literal.stop.tokenIndex,
                )

            divisor_identifier = divide_statement.identifier()
            divisor_literal = divide_statement.literal()
            if divisor_identifier:
                res["divisor_identifier"] = divisor_identifier.getText()

            if divisor_literal:
                res["divisor_literal"] = get_original_code_content(
                    ctx.parser,
                    divisor_literal.start.tokenIndex,
                    divisor_literal.stop.tokenIndex,
                )

            divide_giving_phrase = divide_statement.divideGivingPhrase()

            if divide_giving_phrase:
                divide_giving_list: List[Cobol85Parser.DivideGivingContext] = (
                    divide_giving_phrase.divideGiving()
                )
                res["results"] = [
                    divide_giving.identifier().getText()
                    for divide_giving in divide_giving_list
                ]

        divide_remainder = ctx.divideRemainder()
        res["remainder_identifier"] = (
            divide_remainder.identifier().getText() if divide_remainder else None
        )

        res["on_size_error_phrase"] = []
        on_size_error_phrase = ctx.onSizeErrorPhrase()
        if on_size_error_phrase:
            res["on_size_error_phrase"] = self._assess_nested_statements(
                on_size_error_phrase
            )

        res["not_on_size_error_phrase"] = []
        not_on_size_error_phrase = ctx.notOnSizeErrorPhrase()
        if not_on_size_error_phrase:
            res["not_on_size_error_phrase"] = self._assess_nested_statements(
                not_on_size_error_phrase
            )

        return res

    def assess_delete_statement(self, ctx: Cobol85Parser.DeleteStatementContext):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

        file_name = ctx.fileName()
        res["file_name"] = file_name.getText()

        invalid_key_phrase = ctx.invalidKeyPhrase()
        if invalid_key_phrase:
            res["invalid_key_phrase"] = self._assess_nested_statements(
                invalid_key_phrase
            )

        not_invalid_key_phrase = ctx.notInvalidKeyPhrase()
        if not_invalid_key_phrase:
            res["not_invalid_key_phrase"] = self._assess_nested_statements(
                not_invalid_key_phrase
            )

        return res

    def assess_exec_cics_statement2(
        self,
        ctx: Union[
            Cobol85Parser.ExecCicsStatement2Context,
            CopyBookParser.ExecCicsStatement2Context,
        ],
    ):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

        # commandName
        commandName = ctx.commandName()
        res["commandName"] = commandName.getText()
        # commandBody
        commandBody = ctx.commandBody()
        if commandBody:
            res["commandBody"] = []
            commandParameter = commandBody.commandParameter()
            for cp in commandParameter:
                parameterName = cp.parameterName()
                parameterValue = cp.parameterValue()
                parameterValueWithIndex = cp.parameterValueWithIndex()
                if parameterValue:
                    res["commandBody"].append(
                        {
                            "parameterName": parameterName.getText(),
                            "parameterValue": parameterValue.getText(),
                        }
                    )
                elif parameterValueWithIndex:
                    res["commandBody"].append(
                        {
                            "parameterName": parameterName.getText(),
                            "parameterValue": parameterValueWithIndex.getText(),
                        }
                    )
                else:
                    res["commandBody"].append(
                        {"parameterName": parameterName.getText(), "parameterValue": ""}
                    )
        return res

    def assess_exec_sql_statement2(
        self,
        ctx: Union[
            Cobol85Parser.ExecSqlStatement2Context,
            CopyBookParser.ExecSqlStatement2Context,
        ],
    ):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

        sql_code = ctx.charDataSql()
        res["sql_code"] = get_original_code_content(
            ctx.parser, sql_code.start.tokenIndex, sql_code.stop.tokenIndex
        )
        return res

    def assess_exit_statement(
        self,
        ctx: Union[
            Cobol85Parser.ExitStatementContext, CopyBookParser.ExitStatementContext
        ],
    ):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

        return res

    def assess_goback_statement(
        self,
        ctx: Union[
            Cobol85Parser.GobackStatementContext, CopyBookParser.GobackStatementContext
        ],
    ):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

        return res

    def assess_go_to_statement(
        self,
        ctx: Union[
            Cobol85Parser.GoToStatementContext, CopyBookParser.GoToStatementContext
        ],
    ):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

        goToStatementSimple = ctx.goToStatementSimple()
        if goToStatementSimple:
            res["procedure_name_1"] = goToStatementSimple.getText()
        return res

    def assess_initialize_statement(
        self,
        ctx: Union[
            Cobol85Parser.InitializeStatementContext,
            CopyBookParser.InitializeStatementContext,
        ],
    ):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

        # identifier
        identifier = ctx.identifier()
        if identifier:
            res["identifier_1"] = []
            for i in identifier:
                # res["identifier_1"].append(i.getText())
                res["identifier_1"].append(
                    get_original_code_content(
                        ctx.parser, i.start.tokenIndex, i.stop.tokenIndex
                    )
                )
        return res

    def assess_inspect_statement(
        self,
        ctx: Union[
            Cobol85Parser.InspectStatementContext,
            CopyBookParser.InspectStatementContext,
        ],
    ):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

        identifier = ctx.identifier()
        res["identifier"] = identifier.getText()

        inspect_phrase = ctx.getChild(2)

        if isinstance(
            inspect_phrase,
            Union[
                Cobol85Parser.InspectReplacingPhraseContext,
                CopyBookParser.InspectReplacingPhraseContext,
            ],
        ):
            inspect_replacing_phrase_dict = self.extract_inspect_replacing_phrase(
                inspect_phrase
            )
            res["phrase"] = inspect_replacing_phrase_dict

        elif isinstance(
            inspect_phrase,
            Union[
                Cobol85Parser.InspectTallyingPhraseContext,
                CopyBookParser.InspectTallyingPhraseContext,
            ],
        ):
            inspect_tallying_phrase_dict = self.extract_inspect_tallying(inspect_phrase)
            res["phrase"] = inspect_tallying_phrase_dict

        elif isinstance(
            inspect_phrase,
            Union[
                Cobol85Parser.InspectTallyingReplacingPhraseContext,
                CopyBookParser.InspectTallyingReplacingPhraseContext,
            ],
        ):
            inspect_tallying_replacing_dict = self.extract_inspect_tallying_replacing(
                inspect_phrase
            )
            res["phrase"] = inspect_tallying_replacing_dict

        elif isinstance(
            inspect_phrase,
            Union[
                Cobol85Parser.InspectConvertingPhraseContext,
                CopyBookParser.InspectConvertingPhraseContext,
            ],
        ):
            inspect_converting_phrase_dict = self.extract_inspect_converting_phrase(
                inspect_phrase
            )
            res["phrase"] = inspect_converting_phrase_dict

        return res

    def extract_inspect_tallying_replacing(
        self,
        inspect_phrase: Union[
            Cobol85Parser.InspectTallyingReplacingPhraseContext,
            CopyBookParser.InspectTallyingReplacingPhraseContext,
        ],
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
        self,
        inspect_phrase: Union[
            Cobol85Parser.InspectReplacingPhraseContext,
            CopyBookParser.InspectReplacingPhraseContext,
        ],
    ):
        inspect_replacing_phrase_dict = {"replacements": []}

        for child in inspect_phrase.getChildren():
            if isinstance(
                child,
                (
                    Cobol85Parser.InspectReplacingCharactersContext,
                    CopyBookParser.InspectReplacingCharactersContext,
                ),
            ):
                inspect_by = child.inspectBy()
                identifier = inspect_by.identifier()
                literal = inspect_by.literal() or (
                    inspect_by.figurativeConstant()
                    if isinstance(inspect_by, Cobol85Parser.InspectByContext)
                    else None
                )
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
                child,
                (
                    Cobol85Parser.InspectReplacingAllLeadingsContext,
                    CopyBookParser.InspectReplacingAllLeadingsContext,
                ),
            ):
                leading_type = child.getChild(0).getText().upper()
                inspect_replacing_all_leadings_dict = {
                    "leading_type": leading_type,
                    "replacements": [],
                }
                inspect_replacing_phrase_dict["replacements"].append(
                    inspect_replacing_all_leadings_dict
                )

                inspect_replacing_all_leading_list = child.inspectReplacingAllLeading()
                for inspect_replacing_all_leading in inspect_replacing_all_leading_list:
                    replacing_identifier = inspect_replacing_all_leading.identifier()
                    replacing_literal = inspect_replacing_all_leading.literal() or (
                        inspect_replacing_all_leading.figurativeConstant()
                        if isinstance(
                            inspect_replacing_all_leading,
                            Cobol85Parser.InspectReplacingAllLeadingContext,
                        )
                        else None
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

                    inspect_by_list = [inspect_replacing_all_leading.inspectBy()]
                    for inspect_by in inspect_by_list:
                        by_identifier = inspect_by.identifier()
                        by_literal = inspect_by.literal() or (
                            inspect_by.figurativeConstant()
                            if isinstance(inspect_by, Cobol85Parser.InspectByContext)
                            else None
                        )

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
        self,
        inspect_tallying: Union[
            Cobol85Parser.InspectTallyingPhraseContext,
            CopyBookParser.InspectTallyingPhraseContext,
        ],
    ):
        inspect_tallying_phrase_dict = {"tallying": []}
        inspect_for_list = inspect_tallying.inspectFor()

        for inspect_for in inspect_for_list:
            inspect_for_dict = self.extract_inspect_for(inspect_for)
            inspect_tallying_phrase_dict["tallying"].append(inspect_for_dict)

        return inspect_tallying_phrase_dict

    def extract_inspect_for(
        self,
        inspect_for: Union[
            Cobol85Parser.InspectForContext, CopyBookParser.InspectForContext
        ],
    ):
        identifier = inspect_for.identifier()
        inspect_for_dict = {
            "identifier": identifier.getText(),
            "for_targets": [],
        }

        for child in inspect_for.getChildren():
            if isinstance(
                child,
                (
                    Cobol85Parser.InspectCharactersContext,
                    CopyBookParser.InspectCharactersContext,
                ),
            ):
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
            elif isinstance(
                child,
                (
                    Cobol85Parser.InspectAllLeadingsContext,
                    CopyBookParser.InspectAllLeadingsContext,
                ),
            ):
                leading_type = child.getChild(0).getText().upper()
                inspect_all_leadings_dict = {
                    "leading_type": leading_type,
                    "inspect_all_leading": [],
                }
                inspect_for_dict["for_targets"].append(inspect_all_leadings_dict)

                inspect_all_leading_list = child.inspectAllLeading()

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
        self,
        inspect_before_after: Union[
            Cobol85Parser.InspectBeforeAfterContext,
            CopyBookParser.InspectBeforeAfterContext,
        ],
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

    def extract_inspect_converting_phrase(
        self,
        inspect_converting_phrase: Union[
            Cobol85Parser.InspectConvertingPhraseContext,
            CopyBookParser.InspectConvertingPhraseContext,
        ],
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

    def assess_move_statement(
        self,
        ctx: Union[
            Cobol85Parser.MoveStatementContext, CopyBookParser.MoveStatementContext
        ],
    ):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

        if ctx.ALL():
            res["move_option"] = "ALL"

        move_to_statement = ctx.moveToStatement()

        move_corresponding_to_statement = ctx.moveCorrespondingToStatement()

        if move_to_statement:
            res["move_type"] = "TO"

            move_to_sending_area = move_to_statement.moveToSendingArea()
            res["move_from"] = get_original_code_content(
                ctx.parser,
                move_to_sending_area.start.tokenIndex,
                move_to_sending_area.stop.tokenIndex,
            )

            move_to_sending_area_child = move_to_sending_area.getChild(0)
            if isinstance(move_to_sending_area_child, Cobol85Parser.IdentifierContext):
                res["from_identifier"] = move_to_sending_area_child.getText()
            else:
                res["from_literal"] = get_original_code_content(
                    ctx.parser,
                    move_to_sending_area_child.start.tokenIndex,
                    move_to_sending_area_child.stop.tokenIndex,
                )

            move_to_identifier_list = move_to_statement.identifier()
            res["move_to"] = ""
            res["to_identifiers"] = []
            for move_to_identifier in move_to_identifier_list:
                res["move_to"] += (
                    get_original_code_content(
                        ctx.parser,
                        move_to_identifier.start.tokenIndex,
                        move_to_identifier.stop.tokenIndex,
                    )
                    + " "
                )

                res["to_identifiers"].append(move_to_identifier.getText())
            res["move_to"] = res["move_to"].strip()

        if isinstance(
            move_corresponding_to_statement,
            Cobol85Parser.MoveCorrespondingToStatementContext,
        ):
            res["move_type"] = "CORRESPONDING"

            move_corresponding_to_sending_aarea = (
                move_corresponding_to_statement.moveCorrespondingToSendingArea()
            )

            if move_corresponding_to_sending_aarea:
                res["from_identifier"] = move_corresponding_to_sending_aarea.getText()
                res["move_from"] = move_corresponding_to_sending_aarea.getText()

            move_to_identifier_list = move_corresponding_to_statement.identifier()
            res["move_to"] = ""
            res["to_identifiers"] = []
            for move_to_identifier in move_to_identifier_list:
                res["move_to"] += (
                    get_original_code_content(
                        ctx.parser,
                        move_to_identifier.start.tokenIndex,
                        move_to_identifier.stop.tokenIndex,
                    )
                    + " "
                )

                res["to_identifiers"].append(move_to_identifier.getText())

            res["move_to"] = res["move_to"].strip()

        return res

    def assess_multiply_statement(
        self,
        ctx: Union[
            Cobol85Parser.MultiplyStatementContext,
            CopyBookParser.MultiplyStatementContext,
        ],
    ):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

        multiplier_identifier = ctx.identifier()
        res["multiplier_identifier"] = (
            multiplier_identifier.getText() if multiplier_identifier else None
        )

        multiplier_literal = ctx.literal()
        res["multiplier_literal"] = (
            multiplier_literal.getText() if multiplier_literal else None
        )

        multiply_regular = ctx.multiplyRegular()
        if multiply_regular:
            multiply_regular_operand_ctx_list = (
                multiply_regular.multiplyRegularOperand()
            )

            multiplicant_identifiers = [
                multiply_regular_operand_ctx.identifier().getText()
                for multiply_regular_operand_ctx in multiply_regular_operand_ctx_list
            ]
            res["multiplicand_identifiers"] = multiplicant_identifiers

            res["results"] = multiplicant_identifiers

        multiply_giving = ctx.multiplyGiving()
        if multiply_giving:
            multiplicand_identifier = (
                multiply_giving.multiplyGivingOperand().identifier()
            )
            res["multiplicand_identifiers"] = (
                [multiplicand_identifier.getText()] if multiplicand_identifier else []
            )

            multiplicand_literal = multiply_giving.multiplyGivingOperand().literal()
            res["multiplicand_literal"] = (
                [multiplicand_literal.getText()] if multiplicand_literal else []
            )

            multiply_giving_result = multiply_giving.multiplyGivingResult()
            res["results"] = [result.getText() for result in multiply_giving_result]

        on_size_error_phrase = ctx.onSizeErrorPhrase()
        if on_size_error_phrase:
            res["on_size_error_phrase"] = self._assess_nested_statements(
                on_size_error_phrase
            )

        not_on_size_error_phrase = ctx.notOnSizeErrorPhrase()
        if not_on_size_error_phrase:
            res["not_on_size_error_phrase"] = self._assess_nested_statements(
                not_on_size_error_phrase
            )

        return res

    def assess_search_statement(
        self,
        ctx: Union[
            Cobol85Parser.SearchStatementContext, CopyBookParser.SearchStatementContext
        ],
    ):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

        all_token = ctx.ALL()
        res["is_all"] = True if all_token else False
        record_name = ctx.qualifiedDataName()
        res["record_name"] = get_original_code_content(
            ctx.parser, record_name.start.tokenIndex, record_name.stop.tokenIndex
        )

        search_varying: Cobol85Parser.SearchVaryingContext = ctx.searchVarying()
        if search_varying:
            varying_record_name = search_varying.qualifiedDataName()
            res["varying_record_name"] = get_original_code_content(
                ctx.parser,
                varying_record_name.start.tokenIndex,
                varying_record_name.stop.tokenIndex,
            )

        res["at_end_phrase"] = []
        at_end_phrase = ctx.atEndPhrase()
        if at_end_phrase:
            res["at_end_phrase"] = self._assess_nested_statements(at_end_phrase)

        search_when_list = ctx.searchWhen()
        res["when"] = []
        for search_when in search_when_list:
            condition = search_when.condition()
            res["when"].append(
                {
                    "condition": get_original_code_content(
                        ctx.parser,
                        condition.start.tokenIndex,
                        condition.stop.tokenIndex,
                    ),
                    "statements": [],
                }
            )
            if search_when.statement():
                res["when"][-1]["statements"] = self._assess_nested_statements(
                    search_when
                )
            else:
                res["when"][-1]["statements"] = []

        return res

    def assess_string_statement(
        self,
        ctx: Union[
            Cobol85Parser.StringStatementContext, CopyBookParser.StringStatementContext
        ],
    ):
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
            ctx.parser, start_token.tokenIndex, stop_token.tokenIndex
        )
        res["stringSendingPhrase"] = []
        res["destination_identifier"] = None
        res["pointer_name"] = None

        string_sending_phrase_list = ctx.stringSendingPhrase()

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

            string_sending_list = string_sending_phrase.stringSending()
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

            string_delimited_by_phrase = string_sending_phrase.stringDelimitedByPhrase()

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

            string_for_phrase = string_sending_phrase.stringForPhrase()

            if string_for_phrase:
                identifier = string_for_phrase.identifier()
                literal = string_for_phrase.literal()

                string_sending_phrase_dict["for_identifier"] = (
                    identifier.getText() if identifier else None
                )
                string_sending_phrase_dict["for_literal"] = (
                    literal.getText() if literal else None
                )

        string_into_phrase: Cobol85Parser.StringIntoPhraseContext = (
            ctx.stringIntoPhrase()
        )

        into_identifier = string_into_phrase.identifier()
        res["destination_identifier"] = into_identifier.getText()

        string_pointer_phrase = ctx.stringWithPointerPhrase()

        if string_pointer_phrase:
            pointer_qualified_data_name = string_pointer_phrase.qualifiedDataName()

            res["pointer_name"] = pointer_qualified_data_name.getText()

        res["on_overflow_phrase"] = []
        on_overflow_phrase = ctx.onOverflowPhrase()
        if on_overflow_phrase:
            res["on_overflow_phrase"] = self._assess_nested_statements(
                on_overflow_phrase
            )

        res["not_on_overflow_phrase"] = []
        not_on_overflow_phrase = ctx.notOnOverflowPhrase()
        if not_on_overflow_phrase:
            res["not_on_overflow_phrase"] = self._assess_nested_statements(
                not_on_overflow_phrase
            )

        return res

    def assess_subtract_statement(
        self,
        ctx: Union[
            Cobol85Parser.SubtractStatementContext,
            CopyBookParser.SubtractStatementContext,
        ],
    ):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

        res["subtrahends"] = []
        res["minuends"] = []
        res["results"] = []

        subtract_phrase = ctx.getChild(1)

        if isinstance(
            subtract_phrase,
            (
                Cobol85Parser.SubtractFromStatementContext,
                CopyBookParser.SubtractFromStatementContext,
            ),
        ):

            subtract_from_statement = subtract_phrase
            subtrahend_list = subtract_from_statement.subtractSubtrahend()

            for subtrahend in subtrahend_list:
                subtrahend = subtrahend.getChild(0)
                if isinstance(subtrahend, Cobol85Parser.IdentifierContext):
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
            subtract_phrase,
            (
                Cobol85Parser.SubtractFromGivingStatementContext,
                CopyBookParser.SubtractFromGivingStatementContext,
            ),
        ):
            subtract_from_statement = subtract_phrase
            subtrahend_list = subtract_from_statement.subtractSubtrahend()

            for subtrahend in subtrahend_list:
                subtrahend = subtrahend.getChild(0)
                if isinstance(subtrahend, Cobol85Parser.IdentifierContext):
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
                        or (
                            minuend_giving.figurativeConstant()
                            if isinstance(
                                minuend_giving,
                                Cobol85Parser.SubtractMinuendGivingContext,
                            )
                            else None
                        )
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
            subtract_phrase,
            (
                Cobol85Parser.SubtractCorrespondingStatementContext,
                CopyBookParser.SubtractCorrespondingStatementContext,
            ),
        ):
            subtract_corresponding_statement = subtract_phrase
            qualified_data_name = subtract_corresponding_statement.qualifiedDataName()
            res["subtrahends"].append(
                {
                    "identifier": get_original_code_content(
                        ctx.parser,
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
                        ctx.parser,
                        subtract_minuend_corresponding.start.tokenIndex,
                        subtract_minuend_corresponding.stop.tokenIndex,
                    ),
                    "literal": None,
                }
            )
            res["results"].append(
                {
                    "identifier": get_original_code_content(
                        ctx.parser,
                        subtract_minuend_corresponding.start.tokenIndex,
                        subtract_minuend_corresponding.stop.tokenIndex,
                    ),
                    "is_rounded": subtract_minuend_corresponding.ROUNDED() is not None,
                }
            )

        res["on_size_error_phrase"] = []
        on_size_error_phrase = ctx.onSizeErrorPhrase()
        if on_size_error_phrase:
            res["on_size_error_phrase"] = self._assess_nested_statements(
                on_size_error_phrase
            )

        res["not_on_size_error_phrase"] = []
        not_on_size_error_phrase = ctx.notOnSizeErrorPhrase()
        if not_on_size_error_phrase:
            res["not_on_size_error_phrase"] = self._assess_nested_statements(
                not_on_size_error_phrase
            )

        return res

    def assess_set_statement(
        self,
        ctx: Union[
            Cobol85Parser.SetStatementContext, CopyBookParser.SetStatementContext
        ],
    ):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

        # Get all children of context
        children = ctx.getChildren()
        children = [type(c) for c in children]

        # SetTo
        if (
            Cobol85Parser.SetToStatementContext in children
            or CopyBookParser.SetToStatementContext in children
        ):
            res["set_type"] = "TO"
            res["set_to"] = []
            setToStatement = ctx.setToStatement()
            for s in setToStatement:
                # init
                r = {}
                # setTo
                setTo = s.setTo()
                if setTo:
                    r["source_identifier"] = []
                    for c in setTo:
                        # r["identifier_1"].append(c.getText())
                        r["source_identifier"].append(
                            get_original_code_content(
                                ctx.parser, c.start.tokenIndex, c.stop.tokenIndex
                            )
                        )
                # setToValue
                setToValue = s.setToValue()
                if setToValue:
                    setToValue = setToValue[0]  # type: ignore
                    setToIdentifier = setToValue.identifier()
                    if setToIdentifier:
                        r["target_identifier"] = get_original_code_content(
                            ctx.parser,
                            setToValue.start.tokenIndex,
                            setToValue.stop.tokenIndex,
                        )
                    else:
                        setToLiteral = setToValue.getChild(0)

                        if isinstance(setToLiteral, TerminalNodeImpl):
                            r["target_literal"] = get_original_code_content(
                                ctx.parser,
                                setToLiteral.symbol.tokenIndex,
                                setToLiteral.symbol.tokenIndex,
                            )
                        else:
                            r["target_literal"] = get_original_code_content(
                                ctx.parser,
                                setToLiteral.start.tokenIndex,
                                setToLiteral.stop.tokenIndex,
                            )
                    # r["identifier_2"] = []
                    # for c in setToValue:
                    #     # r["identifier_2"].append(c.getText())
                    #     r["identifier_2"].append(
                    #         get_original_code_content(
                    #             ctx.parser, c.start.tokenIndex, c.stop.tokenIndex
                    #         )
                    #     )
                # collect
                res["set_to"].append(r)
        elif ctx.setUpDownByStatement():
            set_up_down_by_statement = ctx.setUpDownByStatement()

            set_type_ctx = (
                set_up_down_by_statement.UP() or set_up_down_by_statement.DOWN()
            )
            res["set_type"] = set_type_ctx.getText().upper()

            res["set_up_down"] = {}

            setTo = set_up_down_by_statement.setTo()
            if setTo:
                res["set_up_down"]["source_identifier"] = []
                for c in setTo:
                    res["set_up_down"]["source_identifier"].append(
                        get_original_code_content(
                            ctx.parser, c.start.tokenIndex, c.stop.tokenIndex
                        )
                    )

            set_by_value = set_up_down_by_statement.setByValue()

            if set_by_value.identifier():
                res["set_up_down"][
                    "by_identifier"
                ] = set_by_value.identifier().getText()
            else:
                res["set_up_down"]["by_literal"] = get_original_code_content(
                    ctx.parser,
                    set_by_value.start.tokenIndex,
                    set_by_value.stop.tokenIndex,
                )

        return res

    def assess_sort_statement(
        self,
        ctx: Union[
            Cobol85Parser.SortStatementContext, CopyBookParser.SortStatementContext
        ],
    ):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

        file_name = ctx.fileName()
        res["file_name"] = file_name.getText()

        res["sort_keys"] = []
        sort_on_key_clause_list: List[Cobol85Parser.SortOnKeyClauseContext] = (
            ctx.sortOnKeyClause()
        )

        for sort_on_key_clause in sort_on_key_clause_list:
            sort_type = (
                sort_on_key_clause.ASCENDING() or sort_on_key_clause.DESCENDING()
            )
            sort_key = {"sort_type": sort_type.getText().upper(), "keys": []}

            qualified_data_name_list: List[Cobol85Parser.QualifiedDataNameContext] = (
                sort_on_key_clause.qualifiedDataName()
            )

            for qualified_data_name in qualified_data_name_list:
                sort_key["keys"].append(
                    get_original_code_content(
                        ctx.parser,
                        qualified_data_name.start.tokenIndex,
                        qualified_data_name.stop.tokenIndex,
                    )
                )

            res["sort_keys"].append(sort_key)

        sort_output_procedure_phrase: Cobol85Parser.SortOutputProcedurePhraseContext = (
            ctx.sortOutputProcedurePhrase()
        )
        if sort_output_procedure_phrase:
            output_procedure_name = sort_output_procedure_phrase.procedureName()
            res["output_procedure_name"] = get_original_code_content(
                ctx.parser,
                output_procedure_name.start.tokenIndex,
                output_procedure_name.stop.tokenIndex,
            )

            sort_output_through: Cobol85Parser.SortOutputThroughContext = (
                sort_output_procedure_phrase.sortOutputThrough()
            )
            if sort_output_through:
                through_procedure_name = sort_output_through.procedureName()
                res["through_procedure_name"] = get_original_code_content(
                    ctx.parser,
                    through_procedure_name.start.tokenIndex,
                    through_procedure_name.stop.tokenIndex,
                )
            else:
                res["through_procedure_name"] = None

        return res

    def assess_start_statement(
        self,
        ctx: Union[
            Cobol85Parser.StartStatementContext, CopyBookParser.StartStatementContext
        ],
    ):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

        file_name = ctx.fileName()
        res["file_name"] = file_name.getText()

        start_key = ctx.startKey()
        if start_key:
            res["start_key"] = get_original_code_content(
                ctx.parser, start_key.start.tokenIndex, start_key.stop.tokenIndex
            )
        else:
            res["start_key"] = None

        invalid_key_phrase = ctx.invalidKeyPhrase()
        if invalid_key_phrase:
            res["invalid_key_phrase"] = self._assess_nested_statements(
                invalid_key_phrase
            )

        not_invalid_key_phrase = ctx.notInvalidKeyPhrase()
        if not_invalid_key_phrase:
            res["not_invalid_key_phrase"] = self._assess_nested_statements(
                not_invalid_key_phrase
            )

        return res

    def assess_stop_statement(self, ctx):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

        return res

    def assess_write_statement(
        self,
        ctx: Union[
            Cobol85Parser.WriteStatementContext, CopyBookParser.WriteStatementContext
        ],
    ):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

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
            # Check if WriteAdvancingPhraseContext has attribute ADVANCING
            advancing_type = (
                write_advancing_phrase.ADVANCING().getText()
                if write_advancing_phrase.ADVANCING()
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
            res["write_at_end_of_page_phrase"] = self._assess_nested_statements(
                write_at_end_of_page_phrase
            )

        write_not_at_end_of_page_phrase = ctx.writeNotAtEndOfPagePhrase()
        if write_not_at_end_of_page_phrase:
            res["write_not_at_end_of_page_phrase"] = self._assess_nested_statements(
                write_not_at_end_of_page_phrase
            )

        invalid_key_phrase = ctx.invalidKeyPhrase()
        if invalid_key_phrase:
            res["invalid_key_phrase"] = self._assess_nested_statements(
                invalid_key_phrase
            )

        not_invalid_key_phrase = ctx.notInvalidKeyPhrase()
        if not_invalid_key_phrase:
            res["not_invalid_key_phrase"] = self._assess_nested_statements(
                not_invalid_key_phrase
            )

        return res

    def assess_open_statement(
        self,
        ctx: Union[
            Cobol85Parser.OpenStatementContext, CopyBookParser.OpenStatementContext
        ],
    ):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

        # Get all children of context
        children = ctx.getChildren()

        res["open_files"] = []

        for child in children:

            if isinstance(
                child,
                Union[
                    Cobol85Parser.OpenInputStatementContext,
                    CopyBookParser.OpenInputStatementContext,
                ],
            ):
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

            elif isinstance(
                child,
                Union[
                    Cobol85Parser.OpenOutputStatementContext,
                    CopyBookParser.OpenOutputStatementContext,
                ],
            ):
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

            elif isinstance(
                child,
                Union[
                    Cobol85Parser.OpenIOStatementContext,
                    CopyBookParser.OpenIOStatementContext,
                ],
            ):
                file_names = child.fileName()
                for file_name in file_names:
                    res["open_files"].append(
                        {
                            "file_name": file_name.getText(),
                            "open_type": "IO",
                            "on_exception_clause": [],
                        }
                    )

            # elif isinstance(child, Cobol85Parser.OpenInquiryContext):
            #     file_name = child.qualifiedDataName()
            #     on_exception_statements = []
            #     on_exception_clause = child.onExceptionClause()
            #     if on_exception_clause:
            #         statements = on_exception_clause.statement()
            #         for statement in statements:
            #             child = statement.getChild(0)
            #             type_ = type(child).__name__
            #             if type_ in self.func:
            #                 f = self.func[type_]
            #                 on_exception_statements.append(f(child))

            #     res["open_files"].append(
            #         {
            #             "file_name": file_name.getText(),
            #             "open_type": "INQUIRY",
            #             "on_exception_clause": on_exception_statements,
            #         }
            #     )

            elif isinstance(
                child,
                Union[
                    Cobol85Parser.OpenExtendStatementContext,
                    CopyBookParser.OpenExtendStatementContext,
                ],
            ):
                file_names = child.fileName()
                for file_name in file_names:
                    res["open_files"].append(
                        {
                            "file_name": file_name.getText(),
                            "open_type": "EXTEND",
                            "on_exception_clause": [],
                        }
                    )

            # elif isinstance(child, Cobol85Parser.OpenUpdateStatementContext):
            #     file_name = child.qualifiedDataName()

            #     on_exception_clause = child.onExceptionClause()
            #     on_exception_statements = []
            #     if on_exception_clause:
            #         statements = on_exception_clause.statement()
            #         for statement in statements:
            #             child = statement.getChild(0)
            #             type_ = type(child).__name__
            #             if type_ in self.func:
            #                 f = self.func[type_]
            #                 on_exception_statements.append(f(child))

            #     res["open_files"].append(
            #         {
            #             "file_name": file_name.getText(),
            #             "open_type": "UPDATE",
            #             "on_exception_clause": on_exception_statements,
            #         }
            #     )

        return res

    def assess_if_statement(
        self,
        ctx: Union[Cobol85Parser.IfStatementContext, CopyBookParser.IfStatementContext],
    ):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

        condition = ctx.condition()
        if condition:
            start_idx = condition.start.tokenIndex
            stop_idx = condition.stop.tokenIndex
            res["condition"] = get_original_code_content(
                ctx.parser, start_idx, stop_idx
            )

        ifThen = ctx.ifThen()
        if ifThen:
            res["ifThen"] = self._assess_nested_statements(ifThen)

        ifElse = ctx.ifElse()
        if ifElse:
            res["ifElse"] = self._assess_nested_statements(ifElse)

        return res

    def assess_perform_statement(
        self,
        ctx: Union[
            Cobol85Parser.PerformStatementContext,
            CopyBookParser.PerformStatementContext,
        ],
    ):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

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

            perform_times = performType.performTimes() if performType else None

            perform_until = performType.performUntil() if performType else None

            perform_varying = performType.performVarying() if performType else None

            if perform_times:
                res["loop_times"] = get_original_code_content(
                    ctx.parser,
                    perform_times.start.tokenIndex,
                    perform_times.stop.tokenIndex,
                )
                sub_tags.append("TIMES")

            if perform_until:
                condition = perform_until.condition()
                res["condition"] = get_original_code_content(
                    ctx.parser,
                    condition.start.tokenIndex,
                    condition.stop.tokenIndex,
                )
                sub_tags.append("UNTIL")

            if perform_varying:
                perform_varying_clause = perform_varying.performVaryingClause()
                perform_varying_phrase = perform_varying_clause.performVaryingPhrase()
                varying_variable = perform_varying_phrase.getChild(0)
                res["varying_variable"] = get_original_code_content(
                    ctx.parser,
                    varying_variable.start.tokenIndex,
                    varying_variable.stop.tokenIndex,
                )

                from_phrase = perform_varying_phrase.getChild(1)
                res["varying_from"] = get_original_code_content(
                    ctx.parser,
                    from_phrase.getChild(1).start.tokenIndex,
                    from_phrase.getChild(1).stop.tokenIndex,
                )

                by_phrase = perform_varying_phrase.getChild(2)
                res["varying_by"] = get_original_code_content(
                    ctx.parser,
                    by_phrase.getChild(1).start.tokenIndex,
                    by_phrase.getChild(1).stop.tokenIndex,
                )

                sub_tags.append("VARYING")

        res["sub_tags"] = sub_tags

        # performInlineStatement
        performInlineStatement = ctx.performInlineStatement()
        if performInlineStatement:
            perform_inline_type = performInlineStatement.performType()
            # handle nested perform
            perform_times = (
                perform_inline_type.performTimes() if perform_inline_type else None
            )

            perform_until = (
                perform_inline_type.performUntil() if perform_inline_type else None
            )

            perform_varying = (
                perform_inline_type.performVarying() if perform_inline_type else None
            )

            if perform_times:
                res["loop_times"] = get_original_code_content(
                    ctx.parser,
                    perform_times.start.tokenIndex,
                    perform_times.stop.tokenIndex,
                )
                sub_tags.append("TIMES")

            if perform_until:
                condition = perform_until.condition()
                res["condition"] = get_original_code_content(
                    ctx.parser,
                    condition.start.tokenIndex,
                    condition.stop.tokenIndex,
                )
                sub_tags.append("UNTIL")

            if perform_varying:
                perform_varying_clause = perform_varying.performVaryingClause()
                perform_varying_phrase = perform_varying_clause.performVaryingPhrase()
                varying_variable = perform_varying_phrase.getChild(0)
                res["varying_variable"] = get_original_code_content(
                    ctx.parser,
                    varying_variable.start.tokenIndex,
                    varying_variable.stop.tokenIndex,
                )

                from_phrase = perform_varying_phrase.getChild(1)
                res["varying_from"] = get_original_code_content(
                    ctx.parser,
                    from_phrase.getChild(1).start.tokenIndex,
                    from_phrase.getChild(1).stop.tokenIndex,
                )

                by_phrase = perform_varying_phrase.getChild(2)
                res["varying_by"] = get_original_code_content(
                    ctx.parser,
                    by_phrase.getChild(1).start.tokenIndex,
                    by_phrase.getChild(1).stop.tokenIndex,
                )

                sub_tags.append("VARYING")

            res["sub_tags"] = sub_tags

            res["performInlineStatement"] = {}
            performType = performInlineStatement.performType()
            if performType:
                res["performInlineStatement"]["performType"] = (
                    get_original_code_content(
                        ctx.parser,
                        performType.start.tokenIndex,
                        performType.stop.tokenIndex,
                    )
                )

            res["performInlineStatement"]["statement"] = self._assess_nested_statements(
                performInlineStatement
            )

        return res

    def assess_read_statement(
        self,
        ctx: Union[
            Cobol85Parser.ReadStatementContext, CopyBookParser.ReadStatementContext
        ],
    ):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

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
                ctx.parser,
                readInto.identifier().start.tokenIndex,
                readInto.identifier().stop.tokenIndex,
            )

        read_with = ctx.readWith()
        if read_with:
            res["read_with"] = get_original_code_content(
                ctx.parser,
                read_with.start.tokenIndex,
                read_with.stop.tokenIndex,
            ).upper()

        read_key = ctx.readKey()
        if read_key:
            res["read_key"] = get_original_code_content(
                ctx.parser,
                read_key.start.tokenIndex,
                read_key.stop.tokenIndex,
            )

        invalidKeyPhrase = ctx.invalidKeyPhrase()
        if invalidKeyPhrase:
            res["invalid_key_phrase"] = self._assess_nested_statements(invalidKeyPhrase)

        # notInvalidKeyPhrase
        notInvalidKeyPhrase = ctx.notInvalidKeyPhrase()
        if notInvalidKeyPhrase:
            res["not_invalid_key_phrase"] = self._assess_nested_statements(
                notInvalidKeyPhrase
            )

        at_end_phrase = ctx.atEndPhrase()
        if at_end_phrase:
            res["at_end_phrase"] = self._assess_nested_statements(at_end_phrase)

        not_at_end_phrase = ctx.notAtEndPhrase()
        if not_at_end_phrase:
            res["not_at_end_phrase"] = self._assess_nested_statements(not_at_end_phrase)

        return res

    def assess_release_statement(
        self,
        ctx: Union[
            Cobol85Parser.ReleaseStatementContext,
            CopyBookParser.ReleaseStatementContext,
        ],
    ):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

        record_name = ctx.recordName()
        from_data_name = ctx.qualifiedDataName()

        res["record_name"] = get_original_code_content(
            ctx.parser, record_name.start.tokenIndex, record_name.stop.tokenIndex
        )

        if from_data_name:
            res["from_data_name"] = get_original_code_content(
                ctx.parser,
                from_data_name.start.tokenIndex,
                from_data_name.stop.tokenIndex,
            )
        else:
            res["from_data_name"] = None

        return res

    def assess_return_statement(self, ctx):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

        file_name = ctx.fileName()
        res["file_name"] = file_name.getText()

        return_into = ctx.returnInto()

        if return_into:
            data_name = return_into.qualifiedDataName()
            res["into_data_name"] = get_original_code_content(
                ctx.parser, data_name.start.tokenIndex, data_name.stop.tokenIndex
            )

        res["at_end_phrase"] = []
        at_end_phrase = ctx.atEndPhrase()
        if at_end_phrase:
            res["at_end_phrase"] = self._assess_nested_statements(at_end_phrase)

        res["not_at_end_phrase"] = []
        not_at_end_phrase = ctx.notAtEndPhrase()
        if not_at_end_phrase:
            res["not_at_end_phrase"] = self._assess_nested_statements(not_at_end_phrase)

        return res

    def assess_rewrite_statement(
        self,
        ctx: Union[
            Cobol85Parser.RewriteStatementContext,
            CopyBookParser.RewriteStatementContext,
        ],
    ):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

        # recordName
        recordName = ctx.recordName()
        if recordName:
            res["record_name"] = recordName.getText()
        else:
            res["record_name"] = ""

        # rewriteFrom
        rewriteFrom = ctx.rewriteFrom()
        if rewriteFrom:
            res["rewrite_from_identifier"] = get_original_code_content(
                ctx.parser,
                rewriteFrom.identifier().start.tokenIndex,
                rewriteFrom.identifier().stop.tokenIndex,
            )

        invalidKeyPhrase = ctx.invalidKeyPhrase()
        if invalidKeyPhrase:
            res["invalid_key_phrase"] = self._assess_nested_statements(invalidKeyPhrase)

        notInvalidKeyPhrase = ctx.notInvalidKeyPhrase()
        if notInvalidKeyPhrase:
            res["not_invalid_key_phrase"] = self._assess_nested_statements(
                notInvalidKeyPhrase
            )
        return res

    def assess_unstring_statement(
        self,
        ctx: Union[
            Cobol85Parser.UnstringStatementContext,
            CopyBookParser.UnstringStatementContext,
        ],
    ):
        res = {}
        metadata = self._extract_statement_metadata(ctx)
        res.update(metadata)

        unstring_sending_phrase = ctx.unstringSendingPhrase()

        identifier = unstring_sending_phrase.identifier()
        res["identifier"] = identifier.getText()

        res["delimited_by_list"] = []

        unstring_delimited_by_phrase = (
            unstring_sending_phrase.unstringDelimitedByPhrase()
        )

        delimited_by_identifier = unstring_delimited_by_phrase.identifier()
        delimited_by_literal = unstring_delimited_by_phrase.literal()
        is_delimited_all = unstring_delimited_by_phrase.ALL() is not None

        unstring_delimited_by_dict = {
            "literal": delimited_by_literal.getText() if delimited_by_literal else None,
            "identifier": (
                delimited_by_identifier.getText() if delimited_by_identifier else None
            ),
            "is_all": is_delimited_all,
        }
        res["delimited_by_list"].append(unstring_delimited_by_dict)

        unstring_or_all_phrase_list = unstring_sending_phrase.unstringOrAllPhrase()

        for unstring_or_all_phrase in unstring_or_all_phrase_list:
            unstring_or_all_identifier = unstring_or_all_phrase.identifier()
            unstring_or_all_literal = unstring_or_all_phrase.literal()
            unstring_or_all_dict = {
                "literal": (
                    unstring_or_all_literal.getText()
                    if unstring_or_all_literal
                    else None
                ),
                "identifier": (
                    unstring_or_all_identifier.getText()
                    if unstring_or_all_identifier
                    else None
                ),
                "is_all": unstring_or_all_phrase.ALL() is not None,
            }
            res["delimited_by_list"].append(unstring_or_all_dict)

        unstring_into_phrase = ctx.unstringIntoPhrase()
        unstring_into_list = unstring_into_phrase.unstringInto()
        res["into"] = []
        for unstring_into in unstring_into_list:
            unstring_into_identifier = unstring_into.identifier()

            unstring_delimiter_in = unstring_into.unstringDelimiterIn()
            delimiter = (
                unstring_delimiter_in.identifier().getText()
                if unstring_delimiter_in
                else None
            )

            unstring_count_in = unstring_into.unstringCountIn()
            count = (
                unstring_count_in.identifier().getText() if unstring_count_in else None
            )

            unstring_into_dict = {
                "identifier": unstring_into_identifier.getText(),
                "delimiter": delimiter,
                "count": count,
            }
            res["into"].append(unstring_into_dict)

        unstring_with_pointer_phrase = ctx.unstringWithPointerPhrase()
        res["pointer"] = (
            unstring_with_pointer_phrase.qualifiedDataName().getText()
            if unstring_with_pointer_phrase
            else None
        )

        unstring_tallying_phrase = ctx.unstringTallyingPhrase()
        res["tallying"] = (
            unstring_tallying_phrase.qualifiedDataName().getText()
            if unstring_tallying_phrase
            else None
        )

        return res
