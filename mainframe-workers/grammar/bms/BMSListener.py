# Generated from grammar/bms/BMS.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BMSParser import BMSParser
else:
    from BMSParser import BMSParser

# This class defines a complete listener for a parse tree produced by BMSParser.
class BMSListener(ParseTreeListener):

    # Enter a parse tree produced by BMSParser#program.
    def enterProgram(self, ctx:BMSParser.ProgramContext):
        pass

    # Exit a parse tree produced by BMSParser#program.
    def exitProgram(self, ctx:BMSParser.ProgramContext):
        pass


    # Enter a parse tree produced by BMSParser#partitionSetDefinition.
    def enterPartitionSetDefinition(self, ctx:BMSParser.PartitionSetDefinitionContext):
        pass

    # Exit a parse tree produced by BMSParser#partitionSetDefinition.
    def exitPartitionSetDefinition(self, ctx:BMSParser.PartitionSetDefinitionContext):
        pass


    # Enter a parse tree produced by BMSParser#partitionDefinition.
    def enterPartitionDefinition(self, ctx:BMSParser.PartitionDefinitionContext):
        pass

    # Exit a parse tree produced by BMSParser#partitionDefinition.
    def exitPartitionDefinition(self, ctx:BMSParser.PartitionDefinitionContext):
        pass


    # Enter a parse tree produced by BMSParser#mapsetDefinition.
    def enterMapsetDefinition(self, ctx:BMSParser.MapsetDefinitionContext):
        pass

    # Exit a parse tree produced by BMSParser#mapsetDefinition.
    def exitMapsetDefinition(self, ctx:BMSParser.MapsetDefinitionContext):
        pass


    # Enter a parse tree produced by BMSParser#mapDefinition.
    def enterMapDefinition(self, ctx:BMSParser.MapDefinitionContext):
        pass

    # Exit a parse tree produced by BMSParser#mapDefinition.
    def exitMapDefinition(self, ctx:BMSParser.MapDefinitionContext):
        pass


    # Enter a parse tree produced by BMSParser#fieldDefinition.
    def enterFieldDefinition(self, ctx:BMSParser.FieldDefinitionContext):
        pass

    # Exit a parse tree produced by BMSParser#fieldDefinition.
    def exitFieldDefinition(self, ctx:BMSParser.FieldDefinitionContext):
        pass


    # Enter a parse tree produced by BMSParser#name.
    def enterName(self, ctx:BMSParser.NameContext):
        pass

    # Exit a parse tree produced by BMSParser#name.
    def exitName(self, ctx:BMSParser.NameContext):
        pass


    # Enter a parse tree produced by BMSParser#attribute_list.
    def enterAttribute_list(self, ctx:BMSParser.Attribute_listContext):
        pass

    # Exit a parse tree produced by BMSParser#attribute_list.
    def exitAttribute_list(self, ctx:BMSParser.Attribute_listContext):
        pass


    # Enter a parse tree produced by BMSParser#attribute.
    def enterAttribute(self, ctx:BMSParser.AttributeContext):
        pass

    # Exit a parse tree produced by BMSParser#attribute.
    def exitAttribute(self, ctx:BMSParser.AttributeContext):
        pass


    # Enter a parse tree produced by BMSParser#endMap.
    def enterEndMap(self, ctx:BMSParser.EndMapContext):
        pass

    # Exit a parse tree produced by BMSParser#endMap.
    def exitEndMap(self, ctx:BMSParser.EndMapContext):
        pass


    # Enter a parse tree produced by BMSParser#type.
    def enterType(self, ctx:BMSParser.TypeContext):
        pass

    # Exit a parse tree produced by BMSParser#type.
    def exitType(self, ctx:BMSParser.TypeContext):
        pass


    # Enter a parse tree produced by BMSParser#valueList.
    def enterValueList(self, ctx:BMSParser.ValueListContext):
        pass

    # Exit a parse tree produced by BMSParser#valueList.
    def exitValueList(self, ctx:BMSParser.ValueListContext):
        pass


    # Enter a parse tree produced by BMSParser#value.
    def enterValue(self, ctx:BMSParser.ValueContext):
        pass

    # Exit a parse tree produced by BMSParser#value.
    def exitValue(self, ctx:BMSParser.ValueContext):
        pass



del BMSParser