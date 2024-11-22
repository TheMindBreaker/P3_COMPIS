# Generated from morse.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .morseParser import morseParser
else:
    from morseParser import morseParser

# This class defines a complete listener for a parse tree produced by morseParser.
class morseListener(ParseTreeListener):

    # Enter a parse tree produced by morseParser#morse_code.
    def enterMorse_code(self, ctx:morseParser.Morse_codeContext):
        pass

    # Exit a parse tree produced by morseParser#morse_code.
    def exitMorse_code(self, ctx:morseParser.Morse_codeContext):
        pass


    # Enter a parse tree produced by morseParser#text_to_morse.
    def enterText_to_morse(self, ctx:morseParser.Text_to_morseContext):
        pass

    # Exit a parse tree produced by morseParser#text_to_morse.
    def exitText_to_morse(self, ctx:morseParser.Text_to_morseContext):
        pass


    # Enter a parse tree produced by morseParser#morse_letter.
    def enterMorse_letter(self, ctx:morseParser.Morse_letterContext):
        pass

    # Exit a parse tree produced by morseParser#morse_letter.
    def exitMorse_letter(self, ctx:morseParser.Morse_letterContext):
        pass


    # Enter a parse tree produced by morseParser#morse_digit.
    def enterMorse_digit(self, ctx:morseParser.Morse_digitContext):
        pass

    # Exit a parse tree produced by morseParser#morse_digit.
    def exitMorse_digit(self, ctx:morseParser.Morse_digitContext):
        pass


    # Enter a parse tree produced by morseParser#text_letter.
    def enterText_letter(self, ctx:morseParser.Text_letterContext):
        pass

    # Exit a parse tree produced by morseParser#text_letter.
    def exitText_letter(self, ctx:morseParser.Text_letterContext):
        pass


    # Enter a parse tree produced by morseParser#text_digit.
    def enterText_digit(self, ctx:morseParser.Text_digitContext):
        pass

    # Exit a parse tree produced by morseParser#text_digit.
    def exitText_digit(self, ctx:morseParser.Text_digitContext):
        pass



del morseParser