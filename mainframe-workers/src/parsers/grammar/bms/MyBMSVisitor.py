# Generated from BMS.g4 by ANTLR 4.13.1
import re

from antlr4 import *

if "." in __name__:
    from .BMSParser import BMSParser
else:
    from BMSParser import BMSParser

from typing import List, Optional, Tuple

from antlr4 import CommonTokenStream, InputStream
from pydantic import BaseModel

from .BMSVisitor import BMSVisitor

# This class defines a complete generic visitor for a parse tree produced by BMSParser.


class MyBMSVisitor(BMSVisitor):

    def __init__(self):
        self.definitions = []
        self.title = ""

    # Visit a parse tree produced by BMSParser#program.
    def visitProgram(self, ctx: BMSParser.ProgramContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BMSParser#partitionSetDefinition.
    def visitPartitionSetDefinition(self, ctx: BMSParser.PartitionSetDefinitionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BMSParser#partitionDefinition.
    def visitPartitionDefinition(self, ctx: BMSParser.PartitionDefinitionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BMSParser#mapsetDefinition.
    def visitMapsetDefinition(self, ctx: BMSParser.MapsetDefinitionContext):

        definition = {"name": "", "cmd": "DFHMSD"}
        for child in ctx.getChildren():
            ctype = str(type(child))
            # print(ctype)
            if "NameContext" in ctype:
                definition["name"] = child.getText()
            elif "Attribute_listContext" in ctype:
                params = []
                for cc in child.getChildren():
                    cctype = str(type(cc))
                    # print('  ' + cctype)
                    if "AttributeContext" in cctype:
                        cc = cc.getText().replace("-\r\n" + " " * cc.start.column, "")
                        params.append(cc)
                definition["params"] = params

        self.definitions.append(definition)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BMSParser#mapDefinition.
    def visitMapDefinition(self, ctx: BMSParser.MapDefinitionContext):
        definition = {"name": "", "cmd": "DFHMDI"}
        for child in ctx.getChildren():
            ctype = str(type(child))
            # print(ctype)
            if "NameContext" in ctype:
                definition["name"] = child.getText()
            elif "Attribute_listContext" in ctype:
                params = []
                for cc in child.getChildren():
                    cctype = str(type(cc))
                    # print('  ' + cctype)
                    if "AttributeContext" in cctype:
                        # delete spaces and continuation character in string
                        cc = cc.getText().replace("-\r\n" + " " * cc.start.column, "")
                        params.append(cc)
                definition["params"] = params

        self.definitions.append(definition)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BMSParser#fieldDefinition.
    def visitFieldDefinition(self, ctx: BMSParser.FieldDefinitionContext):
        definition = {"name": "", "cmd": "DFHMDF"}
        for child in ctx.getChildren():
            ctype = str(type(child))
            # print(ctype)
            if "NameContext" in ctype:
                definition["name"] = child.getText()
            elif "Attribute_listContext" in ctype:
                params = []
                for cc in child.getChildren():
                    cctype = str(type(cc))
                    # print('  ' + cctype)
                    if "AttributeContext" in cctype:
                        # delete spaces and continuation character in string
                        cc = cc.getText().replace("-\r\n" + " " * cc.start.column, "")
                        params.append(cc)
                definition["params"] = params

        self.definitions.append(definition)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BMSParser#name.
    def visitName(self, ctx: BMSParser.NameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BMSParser#attribute_list.
    def visitAttribute_list(self, ctx: BMSParser.Attribute_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BMSParser#attribute.
    def visitAttribute(self, ctx: BMSParser.AttributeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BMSParser#endMap.
    def visitEndMap(self, ctx: BMSParser.EndMapContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BMSParser#type.
    def visitType(self, ctx: BMSParser.TypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BMSParser#valueList.
    def visitValueList(self, ctx: BMSParser.ValueListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BMSParser#value.
    def visitValue(self, ctx: BMSParser.ValueContext):
        return self.visitChildren(ctx)
