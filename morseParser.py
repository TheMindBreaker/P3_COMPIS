# Generated from morse.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3K")
        buf.write("\'\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\7\2\22\n\2\f\2\16\2\25\13\2\3\3\3\3\3\3\7\3\32")
        buf.write("\n\3\f\3\16\3\35\13\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\7\2\2\b\2\4\6\b\n\f\2\6\3\2\'@\3\2AJ\3\2\3\34\3\2\35")
        buf.write("&\2&\2\23\3\2\2\2\4\33\3\2\2\2\6\36\3\2\2\2\b \3\2\2\2")
        buf.write("\n\"\3\2\2\2\f$\3\2\2\2\16\22\5\6\4\2\17\22\5\b\5\2\20")
        buf.write("\22\7K\2\2\21\16\3\2\2\2\21\17\3\2\2\2\21\20\3\2\2\2\22")
        buf.write("\25\3\2\2\2\23\21\3\2\2\2\23\24\3\2\2\2\24\3\3\2\2\2\25")
        buf.write("\23\3\2\2\2\26\32\5\n\6\2\27\32\5\f\7\2\30\32\7K\2\2\31")
        buf.write("\26\3\2\2\2\31\27\3\2\2\2\31\30\3\2\2\2\32\35\3\2\2\2")
        buf.write("\33\31\3\2\2\2\33\34\3\2\2\2\34\5\3\2\2\2\35\33\3\2\2")
        buf.write("\2\36\37\t\2\2\2\37\7\3\2\2\2 !\t\3\2\2!\t\3\2\2\2\"#")
        buf.write("\t\4\2\2#\13\3\2\2\2$%\t\5\2\2%\r\3\2\2\2\6\21\23\31\33")
        return buf.getvalue()


class morseParser ( Parser ):

    grammarFileName = "morse.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'A'", "'B'", "'C'", "'D'", "'E'", "'F'", 
                     "'G'", "'H'", "'I'", "'J'", "'K'", "'L'", "'M'", "'N'", 
                     "'O'", "'P'", "'Q'", "'R'", "'S'", "'T'", "'U'", "'V'", 
                     "'W'", "'X'", "'Y'", "'Z'", "'0'", "'1'", "'2'", "'3'", 
                     "'4'", "'5'", "'6'", "'7'", "'8'", "'9'", "'.-'", "'-...'", 
                     "'-.-.'", "'-..'", "'.'", "'..-.'", "'--.'", "'....'", 
                     "'..'", "'.---'", "'-.-'", "'.-..'", "'--'", "'-.'", 
                     "'---'", "'.--.'", "'--.-'", "'.-.'", "'...'", "'-'", 
                     "'..-'", "'...-'", "'.--'", "'-..-'", "'-.--'", "'--..'", 
                     "'-----'", "'.----'", "'..---'", "'...--'", "'....-'", 
                     "'.....'", "'-....'", "'--...'", "'---..'", "'----.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "A", "B", "C", "D", "E", "F", "G", "H", 
                      "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", 
                      "S", "T", "U", "V", "W", "X", "Y", "Z", "ZERO", "ONE", 
                      "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", 
                      "NINE", "WS" ]

    RULE_morse_code = 0
    RULE_text_to_morse = 1
    RULE_morse_letter = 2
    RULE_morse_digit = 3
    RULE_text_letter = 4
    RULE_text_digit = 5

    ruleNames =  [ "morse_code", "text_to_morse", "morse_letter", "morse_digit", 
                   "text_letter", "text_digit" ]

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
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    A=37
    B=38
    C=39
    D=40
    E=41
    F=42
    G=43
    H=44
    I=45
    J=46
    K=47
    L=48
    M=49
    N=50
    O=51
    P=52
    Q=53
    R=54
    S=55
    T=56
    U=57
    V=58
    W=59
    X=60
    Y=61
    Z=62
    ZERO=63
    ONE=64
    TWO=65
    THREE=66
    FOUR=67
    FIVE=68
    SIX=69
    SEVEN=70
    EIGHT=71
    NINE=72
    WS=73

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Morse_codeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def morse_letter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(morseParser.Morse_letterContext)
            else:
                return self.getTypedRuleContext(morseParser.Morse_letterContext,i)


        def morse_digit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(morseParser.Morse_digitContext)
            else:
                return self.getTypedRuleContext(morseParser.Morse_digitContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(morseParser.WS)
            else:
                return self.getToken(morseParser.WS, i)

        def getRuleIndex(self):
            return morseParser.RULE_morse_code

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMorse_code" ):
                listener.enterMorse_code(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMorse_code" ):
                listener.exitMorse_code(self)




    def morse_code(self):

        localctx = morseParser.Morse_codeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_morse_code)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 37)) & ~0x3f) == 0 and ((1 << (_la - 37)) & ((1 << (morseParser.A - 37)) | (1 << (morseParser.B - 37)) | (1 << (morseParser.C - 37)) | (1 << (morseParser.D - 37)) | (1 << (morseParser.E - 37)) | (1 << (morseParser.F - 37)) | (1 << (morseParser.G - 37)) | (1 << (morseParser.H - 37)) | (1 << (morseParser.I - 37)) | (1 << (morseParser.J - 37)) | (1 << (morseParser.K - 37)) | (1 << (morseParser.L - 37)) | (1 << (morseParser.M - 37)) | (1 << (morseParser.N - 37)) | (1 << (morseParser.O - 37)) | (1 << (morseParser.P - 37)) | (1 << (morseParser.Q - 37)) | (1 << (morseParser.R - 37)) | (1 << (morseParser.S - 37)) | (1 << (morseParser.T - 37)) | (1 << (morseParser.U - 37)) | (1 << (morseParser.V - 37)) | (1 << (morseParser.W - 37)) | (1 << (morseParser.X - 37)) | (1 << (morseParser.Y - 37)) | (1 << (morseParser.Z - 37)) | (1 << (morseParser.ZERO - 37)) | (1 << (morseParser.ONE - 37)) | (1 << (morseParser.TWO - 37)) | (1 << (morseParser.THREE - 37)) | (1 << (morseParser.FOUR - 37)) | (1 << (morseParser.FIVE - 37)) | (1 << (morseParser.SIX - 37)) | (1 << (morseParser.SEVEN - 37)) | (1 << (morseParser.EIGHT - 37)) | (1 << (morseParser.NINE - 37)) | (1 << (morseParser.WS - 37)))) != 0):
                self.state = 15
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [morseParser.A, morseParser.B, morseParser.C, morseParser.D, morseParser.E, morseParser.F, morseParser.G, morseParser.H, morseParser.I, morseParser.J, morseParser.K, morseParser.L, morseParser.M, morseParser.N, morseParser.O, morseParser.P, morseParser.Q, morseParser.R, morseParser.S, morseParser.T, morseParser.U, morseParser.V, morseParser.W, morseParser.X, morseParser.Y, morseParser.Z]:
                    self.state = 12
                    self.morse_letter()
                    pass
                elif token in [morseParser.ZERO, morseParser.ONE, morseParser.TWO, morseParser.THREE, morseParser.FOUR, morseParser.FIVE, morseParser.SIX, morseParser.SEVEN, morseParser.EIGHT, morseParser.NINE]:
                    self.state = 13
                    self.morse_digit()
                    pass
                elif token in [morseParser.WS]:
                    self.state = 14
                    self.match(morseParser.WS)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Text_to_morseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def text_letter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(morseParser.Text_letterContext)
            else:
                return self.getTypedRuleContext(morseParser.Text_letterContext,i)


        def text_digit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(morseParser.Text_digitContext)
            else:
                return self.getTypedRuleContext(morseParser.Text_digitContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(morseParser.WS)
            else:
                return self.getToken(morseParser.WS, i)

        def getRuleIndex(self):
            return morseParser.RULE_text_to_morse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterText_to_morse" ):
                listener.enterText_to_morse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitText_to_morse" ):
                listener.exitText_to_morse(self)




    def text_to_morse(self):

        localctx = morseParser.Text_to_morseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_text_to_morse)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << morseParser.T__0) | (1 << morseParser.T__1) | (1 << morseParser.T__2) | (1 << morseParser.T__3) | (1 << morseParser.T__4) | (1 << morseParser.T__5) | (1 << morseParser.T__6) | (1 << morseParser.T__7) | (1 << morseParser.T__8) | (1 << morseParser.T__9) | (1 << morseParser.T__10) | (1 << morseParser.T__11) | (1 << morseParser.T__12) | (1 << morseParser.T__13) | (1 << morseParser.T__14) | (1 << morseParser.T__15) | (1 << morseParser.T__16) | (1 << morseParser.T__17) | (1 << morseParser.T__18) | (1 << morseParser.T__19) | (1 << morseParser.T__20) | (1 << morseParser.T__21) | (1 << morseParser.T__22) | (1 << morseParser.T__23) | (1 << morseParser.T__24) | (1 << morseParser.T__25) | (1 << morseParser.T__26) | (1 << morseParser.T__27) | (1 << morseParser.T__28) | (1 << morseParser.T__29) | (1 << morseParser.T__30) | (1 << morseParser.T__31) | (1 << morseParser.T__32) | (1 << morseParser.T__33) | (1 << morseParser.T__34) | (1 << morseParser.T__35))) != 0) or _la==morseParser.WS:
                self.state = 23
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [morseParser.T__0, morseParser.T__1, morseParser.T__2, morseParser.T__3, morseParser.T__4, morseParser.T__5, morseParser.T__6, morseParser.T__7, morseParser.T__8, morseParser.T__9, morseParser.T__10, morseParser.T__11, morseParser.T__12, morseParser.T__13, morseParser.T__14, morseParser.T__15, morseParser.T__16, morseParser.T__17, morseParser.T__18, morseParser.T__19, morseParser.T__20, morseParser.T__21, morseParser.T__22, morseParser.T__23, morseParser.T__24, morseParser.T__25]:
                    self.state = 20
                    self.text_letter()
                    pass
                elif token in [morseParser.T__26, morseParser.T__27, morseParser.T__28, morseParser.T__29, morseParser.T__30, morseParser.T__31, morseParser.T__32, morseParser.T__33, morseParser.T__34, morseParser.T__35]:
                    self.state = 21
                    self.text_digit()
                    pass
                elif token in [morseParser.WS]:
                    self.state = 22
                    self.match(morseParser.WS)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Morse_letterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def A(self):
            return self.getToken(morseParser.A, 0)

        def B(self):
            return self.getToken(morseParser.B, 0)

        def C(self):
            return self.getToken(morseParser.C, 0)

        def D(self):
            return self.getToken(morseParser.D, 0)

        def E(self):
            return self.getToken(morseParser.E, 0)

        def F(self):
            return self.getToken(morseParser.F, 0)

        def G(self):
            return self.getToken(morseParser.G, 0)

        def H(self):
            return self.getToken(morseParser.H, 0)

        def I(self):
            return self.getToken(morseParser.I, 0)

        def J(self):
            return self.getToken(morseParser.J, 0)

        def K(self):
            return self.getToken(morseParser.K, 0)

        def L(self):
            return self.getToken(morseParser.L, 0)

        def M(self):
            return self.getToken(morseParser.M, 0)

        def N(self):
            return self.getToken(morseParser.N, 0)

        def O(self):
            return self.getToken(morseParser.O, 0)

        def P(self):
            return self.getToken(morseParser.P, 0)

        def Q(self):
            return self.getToken(morseParser.Q, 0)

        def R(self):
            return self.getToken(morseParser.R, 0)

        def S(self):
            return self.getToken(morseParser.S, 0)

        def T(self):
            return self.getToken(morseParser.T, 0)

        def U(self):
            return self.getToken(morseParser.U, 0)

        def V(self):
            return self.getToken(morseParser.V, 0)

        def W(self):
            return self.getToken(morseParser.W, 0)

        def X(self):
            return self.getToken(morseParser.X, 0)

        def Y(self):
            return self.getToken(morseParser.Y, 0)

        def Z(self):
            return self.getToken(morseParser.Z, 0)

        def getRuleIndex(self):
            return morseParser.RULE_morse_letter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMorse_letter" ):
                listener.enterMorse_letter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMorse_letter" ):
                listener.exitMorse_letter(self)




    def morse_letter(self):

        localctx = morseParser.Morse_letterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_morse_letter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << morseParser.A) | (1 << morseParser.B) | (1 << morseParser.C) | (1 << morseParser.D) | (1 << morseParser.E) | (1 << morseParser.F) | (1 << morseParser.G) | (1 << morseParser.H) | (1 << morseParser.I) | (1 << morseParser.J) | (1 << morseParser.K) | (1 << morseParser.L) | (1 << morseParser.M) | (1 << morseParser.N) | (1 << morseParser.O) | (1 << morseParser.P) | (1 << morseParser.Q) | (1 << morseParser.R) | (1 << morseParser.S) | (1 << morseParser.T) | (1 << morseParser.U) | (1 << morseParser.V) | (1 << morseParser.W) | (1 << morseParser.X) | (1 << morseParser.Y) | (1 << morseParser.Z))) != 0)):
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


    class Morse_digitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ZERO(self):
            return self.getToken(morseParser.ZERO, 0)

        def ONE(self):
            return self.getToken(morseParser.ONE, 0)

        def TWO(self):
            return self.getToken(morseParser.TWO, 0)

        def THREE(self):
            return self.getToken(morseParser.THREE, 0)

        def FOUR(self):
            return self.getToken(morseParser.FOUR, 0)

        def FIVE(self):
            return self.getToken(morseParser.FIVE, 0)

        def SIX(self):
            return self.getToken(morseParser.SIX, 0)

        def SEVEN(self):
            return self.getToken(morseParser.SEVEN, 0)

        def EIGHT(self):
            return self.getToken(morseParser.EIGHT, 0)

        def NINE(self):
            return self.getToken(morseParser.NINE, 0)

        def getRuleIndex(self):
            return morseParser.RULE_morse_digit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMorse_digit" ):
                listener.enterMorse_digit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMorse_digit" ):
                listener.exitMorse_digit(self)




    def morse_digit(self):

        localctx = morseParser.Morse_digitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_morse_digit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            _la = self._input.LA(1)
            if not(((((_la - 63)) & ~0x3f) == 0 and ((1 << (_la - 63)) & ((1 << (morseParser.ZERO - 63)) | (1 << (morseParser.ONE - 63)) | (1 << (morseParser.TWO - 63)) | (1 << (morseParser.THREE - 63)) | (1 << (morseParser.FOUR - 63)) | (1 << (morseParser.FIVE - 63)) | (1 << (morseParser.SIX - 63)) | (1 << (morseParser.SEVEN - 63)) | (1 << (morseParser.EIGHT - 63)) | (1 << (morseParser.NINE - 63)))) != 0)):
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


    class Text_letterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return morseParser.RULE_text_letter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterText_letter" ):
                listener.enterText_letter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitText_letter" ):
                listener.exitText_letter(self)




    def text_letter(self):

        localctx = morseParser.Text_letterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_text_letter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << morseParser.T__0) | (1 << morseParser.T__1) | (1 << morseParser.T__2) | (1 << morseParser.T__3) | (1 << morseParser.T__4) | (1 << morseParser.T__5) | (1 << morseParser.T__6) | (1 << morseParser.T__7) | (1 << morseParser.T__8) | (1 << morseParser.T__9) | (1 << morseParser.T__10) | (1 << morseParser.T__11) | (1 << morseParser.T__12) | (1 << morseParser.T__13) | (1 << morseParser.T__14) | (1 << morseParser.T__15) | (1 << morseParser.T__16) | (1 << morseParser.T__17) | (1 << morseParser.T__18) | (1 << morseParser.T__19) | (1 << morseParser.T__20) | (1 << morseParser.T__21) | (1 << morseParser.T__22) | (1 << morseParser.T__23) | (1 << morseParser.T__24) | (1 << morseParser.T__25))) != 0)):
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


    class Text_digitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return morseParser.RULE_text_digit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterText_digit" ):
                listener.enterText_digit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitText_digit" ):
                listener.exitText_digit(self)




    def text_digit(self):

        localctx = morseParser.Text_digitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_text_digit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << morseParser.T__26) | (1 << morseParser.T__27) | (1 << morseParser.T__28) | (1 << morseParser.T__29) | (1 << morseParser.T__30) | (1 << morseParser.T__31) | (1 << morseParser.T__32) | (1 << morseParser.T__33) | (1 << morseParser.T__34) | (1 << morseParser.T__35))) != 0)):
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





