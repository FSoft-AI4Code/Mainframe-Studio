# Generated from src/parsers/grammar/bms/BMS.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BMSParser import BMSParser
else:
    from BMSParser import BMSParser

# This class defines a complete generic visitor for a parse tree produced by BMSParser.

class BMSVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BMSParser#program.
    def visitProgram(self, ctx:BMSParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BMSParser#partitionSetDefinition.
    def visitPartitionSetDefinition(self, ctx:BMSParser.PartitionSetDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BMSParser#partitionDefinition.
    def visitPartitionDefinition(self, ctx:BMSParser.PartitionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BMSParser#mapsetDefinition.
    def visitMapsetDefinition(self, ctx:BMSParser.MapsetDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BMSParser#mapDefinition.
    def visitMapDefinition(self, ctx:BMSParser.MapDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BMSParser#fieldDefinition.
    def visitFieldDefinition(self, ctx:BMSParser.FieldDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BMSParser#name.
    def visitName(self, ctx:BMSParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BMSParser#attribute_list.
    def visitAttribute_list(self, ctx:BMSParser.Attribute_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BMSParser#attribute.
    def visitAttribute(self, ctx:BMSParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BMSParser#endMap.
    def visitEndMap(self, ctx:BMSParser.EndMapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BMSParser#type.
    def visitType(self, ctx:BMSParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BMSParser#valueList.
    def visitValueList(self, ctx:BMSParser.ValueListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BMSParser#value.
    def visitValue(self, ctx:BMSParser.ValueContext):
        return self.visitChildren(ctx)



del BMSParser