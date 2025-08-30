# Generated from grammar/bms/BMS.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,18,153,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,0,5,0,30,8,0,10,0,12,0,33,9,0,1,0,5,0,36,8,0,10,0,12,0,39,9,0,
        1,0,1,0,1,1,3,1,44,8,1,1,1,1,1,5,1,48,8,1,10,1,12,1,51,9,1,1,2,3,
        2,54,8,2,1,2,1,2,5,2,58,8,2,10,2,12,2,61,9,2,1,3,3,3,64,8,3,1,3,
        1,3,5,3,68,8,3,10,3,12,3,71,9,3,1,3,5,3,74,8,3,10,3,12,3,77,9,3,
        1,3,3,3,80,8,3,1,3,1,3,1,3,1,4,3,4,86,8,4,1,4,1,4,5,4,90,8,4,10,
        4,12,4,93,9,4,1,4,5,4,96,8,4,10,4,12,4,99,9,4,1,5,3,5,102,8,5,1,
        5,1,5,5,5,106,8,5,10,5,12,5,109,9,5,1,6,1,6,1,7,1,7,1,7,5,7,116,
        8,7,10,7,12,7,119,9,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,129,8,
        8,3,8,131,8,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,
        3,11,144,8,11,5,11,146,8,11,10,11,12,11,149,9,11,1,12,1,12,1,12,
        0,0,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,2,2,0,7,7,13,13,1,0,13,
        16,161,0,31,1,0,0,0,2,43,1,0,0,0,4,53,1,0,0,0,6,63,1,0,0,0,8,85,
        1,0,0,0,10,101,1,0,0,0,12,110,1,0,0,0,14,112,1,0,0,0,16,130,1,0,
        0,0,18,132,1,0,0,0,20,136,1,0,0,0,22,140,1,0,0,0,24,150,1,0,0,0,
        26,30,3,2,1,0,27,30,3,4,2,0,28,30,3,6,3,0,29,26,1,0,0,0,29,27,1,
        0,0,0,29,28,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,
        37,1,0,0,0,33,31,1,0,0,0,34,36,5,1,0,0,35,34,1,0,0,0,36,39,1,0,0,
        0,37,35,1,0,0,0,37,38,1,0,0,0,38,40,1,0,0,0,39,37,1,0,0,0,40,41,
        5,0,0,1,41,1,1,0,0,0,42,44,3,12,6,0,43,42,1,0,0,0,43,44,1,0,0,0,
        44,45,1,0,0,0,45,49,5,2,0,0,46,48,3,14,7,0,47,46,1,0,0,0,48,51,1,
        0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,3,1,0,0,0,51,49,1,0,0,0,52,
        54,3,12,6,0,53,52,1,0,0,0,53,54,1,0,0,0,54,55,1,0,0,0,55,59,5,3,
        0,0,56,58,3,14,7,0,57,56,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,59,
        60,1,0,0,0,60,5,1,0,0,0,61,59,1,0,0,0,62,64,3,12,6,0,63,62,1,0,0,
        0,63,64,1,0,0,0,64,65,1,0,0,0,65,69,5,4,0,0,66,68,3,14,7,0,67,66,
        1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,75,1,0,0,0,
        71,69,1,0,0,0,72,74,3,8,4,0,73,72,1,0,0,0,74,77,1,0,0,0,75,73,1,
        0,0,0,75,76,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,78,80,3,12,6,0,79,
        78,1,0,0,0,79,80,1,0,0,0,80,81,1,0,0,0,81,82,5,4,0,0,82,83,3,18,
        9,0,83,7,1,0,0,0,84,86,3,12,6,0,85,84,1,0,0,0,85,86,1,0,0,0,86,87,
        1,0,0,0,87,91,5,5,0,0,88,90,3,14,7,0,89,88,1,0,0,0,90,93,1,0,0,0,
        91,89,1,0,0,0,91,92,1,0,0,0,92,97,1,0,0,0,93,91,1,0,0,0,94,96,3,
        10,5,0,95,94,1,0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,
        9,1,0,0,0,99,97,1,0,0,0,100,102,3,12,6,0,101,100,1,0,0,0,101,102,
        1,0,0,0,102,103,1,0,0,0,103,107,5,6,0,0,104,106,3,14,7,0,105,104,
        1,0,0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,11,1,
        0,0,0,109,107,1,0,0,0,110,111,7,0,0,0,111,13,1,0,0,0,112,117,3,16,
        8,0,113,114,5,8,0,0,114,116,3,16,8,0,115,113,1,0,0,0,116,119,1,0,
        0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,15,1,0,0,0,119,117,1,0,0,
        0,120,131,3,20,10,0,121,122,5,13,0,0,122,128,5,9,0,0,123,129,3,24,
        12,0,124,125,5,10,0,0,125,126,3,22,11,0,126,127,5,11,0,0,127,129,
        1,0,0,0,128,123,1,0,0,0,128,124,1,0,0,0,129,131,1,0,0,0,130,120,
        1,0,0,0,130,121,1,0,0,0,131,17,1,0,0,0,132,133,5,7,0,0,133,134,5,
        9,0,0,134,135,5,12,0,0,135,19,1,0,0,0,136,137,5,7,0,0,137,138,5,
        9,0,0,138,139,5,13,0,0,139,21,1,0,0,0,140,147,3,24,12,0,141,143,
        5,8,0,0,142,144,3,24,12,0,143,142,1,0,0,0,143,144,1,0,0,0,144,146,
        1,0,0,0,145,141,1,0,0,0,146,149,1,0,0,0,147,145,1,0,0,0,147,148,
        1,0,0,0,148,23,1,0,0,0,149,147,1,0,0,0,150,151,7,1,0,0,151,25,1,
        0,0,0,21,29,31,37,43,49,53,59,63,69,75,79,85,91,97,101,107,117,128,
        130,143,147
    ]

class BMSParser ( Parser ):

    grammarFileName = "BMS.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'END'", "'DFHPSD'", "'DFHPDI'", "'DFHMSD'", 
                     "'DFHMDI'", "'DFHMDF'", "'TYPE'", "','", "'='", "'('", 
                     "')'", "'FINAL'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "IDENTIFIER", "STRING", "STRING2", "NUMBER", 
                      "WS", "LineComment" ]

    RULE_program = 0
    RULE_partitionSetDefinition = 1
    RULE_partitionDefinition = 2
    RULE_mapsetDefinition = 3
    RULE_mapDefinition = 4
    RULE_fieldDefinition = 5
    RULE_name = 6
    RULE_attribute_list = 7
    RULE_attribute = 8
    RULE_endMap = 9
    RULE_type = 10
    RULE_valueList = 11
    RULE_value = 12

    ruleNames =  [ "program", "partitionSetDefinition", "partitionDefinition", 
                   "mapsetDefinition", "mapDefinition", "fieldDefinition", 
                   "name", "attribute_list", "attribute", "endMap", "type", 
                   "valueList", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    IDENTIFIER=13
    STRING=14
    STRING2=15
    NUMBER=16
    WS=17
    LineComment=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BMSParser.EOF, 0)

        def partitionSetDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BMSParser.PartitionSetDefinitionContext)
            else:
                return self.getTypedRuleContext(BMSParser.PartitionSetDefinitionContext,i)


        def partitionDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BMSParser.PartitionDefinitionContext)
            else:
                return self.getTypedRuleContext(BMSParser.PartitionDefinitionContext,i)


        def mapsetDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BMSParser.MapsetDefinitionContext)
            else:
                return self.getTypedRuleContext(BMSParser.MapsetDefinitionContext,i)


        def getRuleIndex(self):
            return BMSParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BMSParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8348) != 0):
                self.state = 29
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 26
                    self.partitionSetDefinition()
                    pass

                elif la_ == 2:
                    self.state = 27
                    self.partitionDefinition()
                    pass

                elif la_ == 3:
                    self.state = 28
                    self.mapsetDefinition()
                    pass


                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 34
                self.match(BMSParser.T__0)
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
            self.match(BMSParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PartitionSetDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(BMSParser.NameContext,0)


        def attribute_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BMSParser.Attribute_listContext)
            else:
                return self.getTypedRuleContext(BMSParser.Attribute_listContext,i)


        def getRuleIndex(self):
            return BMSParser.RULE_partitionSetDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPartitionSetDefinition" ):
                listener.enterPartitionSetDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPartitionSetDefinition" ):
                listener.exitPartitionSetDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPartitionSetDefinition" ):
                return visitor.visitPartitionSetDefinition(self)
            else:
                return visitor.visitChildren(self)




    def partitionSetDefinition(self):

        localctx = BMSParser.PartitionSetDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_partitionSetDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7 or _la==13:
                self.state = 42
                self.name()


            self.state = 45
            self.match(BMSParser.T__1)
            self.state = 49
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 46
                    self.attribute_list() 
                self.state = 51
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PartitionDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(BMSParser.NameContext,0)


        def attribute_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BMSParser.Attribute_listContext)
            else:
                return self.getTypedRuleContext(BMSParser.Attribute_listContext,i)


        def getRuleIndex(self):
            return BMSParser.RULE_partitionDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPartitionDefinition" ):
                listener.enterPartitionDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPartitionDefinition" ):
                listener.exitPartitionDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPartitionDefinition" ):
                return visitor.visitPartitionDefinition(self)
            else:
                return visitor.visitChildren(self)




    def partitionDefinition(self):

        localctx = BMSParser.PartitionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_partitionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7 or _la==13:
                self.state = 52
                self.name()


            self.state = 55
            self.match(BMSParser.T__2)
            self.state = 59
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 56
                    self.attribute_list() 
                self.state = 61
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MapsetDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def endMap(self):
            return self.getTypedRuleContext(BMSParser.EndMapContext,0)


        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BMSParser.NameContext)
            else:
                return self.getTypedRuleContext(BMSParser.NameContext,i)


        def attribute_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BMSParser.Attribute_listContext)
            else:
                return self.getTypedRuleContext(BMSParser.Attribute_listContext,i)


        def mapDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BMSParser.MapDefinitionContext)
            else:
                return self.getTypedRuleContext(BMSParser.MapDefinitionContext,i)


        def getRuleIndex(self):
            return BMSParser.RULE_mapsetDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapsetDefinition" ):
                listener.enterMapsetDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapsetDefinition" ):
                listener.exitMapsetDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMapsetDefinition" ):
                return visitor.visitMapsetDefinition(self)
            else:
                return visitor.visitChildren(self)




    def mapsetDefinition(self):

        localctx = BMSParser.MapsetDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_mapsetDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7 or _la==13:
                self.state = 62
                self.name()


            self.state = 65
            self.match(BMSParser.T__3)
            self.state = 69
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 66
                    self.attribute_list() 
                self.state = 71
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 75
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 72
                    self.mapDefinition() 
                self.state = 77
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7 or _la==13:
                self.state = 78
                self.name()


            self.state = 81
            self.match(BMSParser.T__3)
            self.state = 82
            self.endMap()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MapDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(BMSParser.NameContext,0)


        def attribute_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BMSParser.Attribute_listContext)
            else:
                return self.getTypedRuleContext(BMSParser.Attribute_listContext,i)


        def fieldDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BMSParser.FieldDefinitionContext)
            else:
                return self.getTypedRuleContext(BMSParser.FieldDefinitionContext,i)


        def getRuleIndex(self):
            return BMSParser.RULE_mapDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapDefinition" ):
                listener.enterMapDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapDefinition" ):
                listener.exitMapDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMapDefinition" ):
                return visitor.visitMapDefinition(self)
            else:
                return visitor.visitChildren(self)




    def mapDefinition(self):

        localctx = BMSParser.MapDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_mapDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7 or _la==13:
                self.state = 84
                self.name()


            self.state = 87
            self.match(BMSParser.T__4)
            self.state = 91
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 88
                    self.attribute_list() 
                self.state = 93
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

            self.state = 97
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 94
                    self.fieldDefinition() 
                self.state = 99
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(BMSParser.NameContext,0)


        def attribute_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BMSParser.Attribute_listContext)
            else:
                return self.getTypedRuleContext(BMSParser.Attribute_listContext,i)


        def getRuleIndex(self):
            return BMSParser.RULE_fieldDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldDefinition" ):
                listener.enterFieldDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldDefinition" ):
                listener.exitFieldDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldDefinition" ):
                return visitor.visitFieldDefinition(self)
            else:
                return visitor.visitChildren(self)




    def fieldDefinition(self):

        localctx = BMSParser.FieldDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_fieldDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7 or _la==13:
                self.state = 100
                self.name()


            self.state = 103
            self.match(BMSParser.T__5)
            self.state = 107
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 104
                    self.attribute_list() 
                self.state = 109
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BMSParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return BMSParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName" ):
                return visitor.visitName(self)
            else:
                return visitor.visitChildren(self)




    def name(self):

        localctx = BMSParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            _la = self._input.LA(1)
            if not(_la==7 or _la==13):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BMSParser.AttributeContext)
            else:
                return self.getTypedRuleContext(BMSParser.AttributeContext,i)


        def getRuleIndex(self):
            return BMSParser.RULE_attribute_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute_list" ):
                listener.enterAttribute_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute_list" ):
                listener.exitAttribute_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_list" ):
                return visitor.visitAttribute_list(self)
            else:
                return visitor.visitChildren(self)




    def attribute_list(self):

        localctx = BMSParser.Attribute_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attribute_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.attribute()
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 113
                self.match(BMSParser.T__7)
                self.state = 114
                self.attribute()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(BMSParser.TypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(BMSParser.IDENTIFIER, 0)

        def value(self):
            return self.getTypedRuleContext(BMSParser.ValueContext,0)


        def valueList(self):
            return self.getTypedRuleContext(BMSParser.ValueListContext,0)


        def getRuleIndex(self):
            return BMSParser.RULE_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute" ):
                listener.enterAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute" ):
                listener.exitAttribute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = BMSParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attribute)
        try:
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.type_()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.match(BMSParser.IDENTIFIER)
                self.state = 122
                self.match(BMSParser.T__8)
                self.state = 128
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [13, 14, 15, 16]:
                    self.state = 123
                    self.value()
                    pass
                elif token in [10]:
                    self.state = 124
                    self.match(BMSParser.T__9)
                    self.state = 125
                    self.valueList()
                    self.state = 126
                    self.match(BMSParser.T__10)
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndMapContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BMSParser.RULE_endMap

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEndMap" ):
                listener.enterEndMap(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEndMap" ):
                listener.exitEndMap(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndMap" ):
                return visitor.visitEndMap(self)
            else:
                return visitor.visitChildren(self)




    def endMap(self):

        localctx = BMSParser.EndMapContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_endMap)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(BMSParser.T__6)
            self.state = 133
            self.match(BMSParser.T__8)
            self.state = 134
            self.match(BMSParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BMSParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return BMSParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = BMSParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(BMSParser.T__6)
            self.state = 137
            self.match(BMSParser.T__8)
            self.state = 138
            self.match(BMSParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BMSParser.ValueContext)
            else:
                return self.getTypedRuleContext(BMSParser.ValueContext,i)


        def getRuleIndex(self):
            return BMSParser.RULE_valueList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValueList" ):
                listener.enterValueList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValueList" ):
                listener.exitValueList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValueList" ):
                return visitor.visitValueList(self)
            else:
                return visitor.visitChildren(self)




    def valueList(self):

        localctx = BMSParser.ValueListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_valueList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.value()
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 141
                self.match(BMSParser.T__7)
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 122880) != 0):
                    self.state = 142
                    self.value()


                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(BMSParser.STRING, 0)

        def STRING2(self):
            return self.getToken(BMSParser.STRING2, 0)

        def NUMBER(self):
            return self.getToken(BMSParser.NUMBER, 0)

        def IDENTIFIER(self):
            return self.getToken(BMSParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return BMSParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = BMSParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 122880) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





