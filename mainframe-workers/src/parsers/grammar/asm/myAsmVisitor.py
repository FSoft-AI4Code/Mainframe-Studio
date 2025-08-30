import re
from antlr4 import *
from typing import List

from parsers.grammar.asm.asmVisitor import asmVisitor
from parsers.grammar.asm.asmParser import asmParser
from parsers.grammar.asm.asm_schema import asmCallStatement
from loguru import logger


class MyAsmVisitor(asmVisitor):
    def __init__(self):
        super().__init__()
        self.call_statements: List[asmCallStatement] = []

    def visitCall_statement(self, ctx: asmParser.Call_statementContext):

        call_statement = asmCallStatement(
            subroutine_called="", parameters=[], operands=[]
        )
        # operand of call statement start form index 1.
        Call_operand_child = ctx.getChild(1)
        orderOperand = 0
        for i in range(Call_operand_child.getChildCount()):
            child = Call_operand_child.getChild(i)
            cType = (type(child)).__name__
            if cType == "Call_operandContext":
                Call_operand_text = Call_operand_child.getChild(i).getText()
                # start from called Subroutine
                if orderOperand == 0:
                    call_statement.subroutine_called = Call_operand_text
                    orderOperand += 1
                # Next is list parameters
                elif orderOperand == 1:
                    parameters = []
                    if Call_operand_text.startswith("(") and Call_operand_text.endswith(
                        ")"
                    ):
                        parameters = Call_operand_text.strip("()").split(",")
                        call_statement.parameter.extend(parameters)
                    else:
                        parameters = Call_operand_text
                        call_statement.parameter.append(parameters)
                    orderOperand += 1
                # Final, List operands
                else:
                    call_statement.operands.append(Call_operand_text)

        self.call_statements.append(call_statement)

        return self.visitChildren(ctx)
