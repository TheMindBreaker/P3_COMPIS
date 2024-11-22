from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from antlr4 import *
from morseLexer import morseLexer
from morseParser import morseParser
from morseListener import morseListener

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MorseRequest(BaseModel):
    text: str

class TextRequest(BaseModel):
    text: str

class MorseToTextListener(morseListener):
    def __init__(self):
        self.result = ""

    def enterMorse_letter(self, ctx):
        mapping = {
            morseParser.A: "A", morseParser.B: "B", morseParser.C: "C",
            morseParser.D: "D", morseParser.E: "E", morseParser.F: "F",
            morseParser.G: "G", morseParser.H: "H", morseParser.I: "I",
            morseParser.J: "J", morseParser.K: "K", morseParser.L: "L",
            morseParser.M: "M", morseParser.N: "N", morseParser.O: "O",
            morseParser.P: "P", morseParser.Q: "Q", morseParser.R: "R",
            morseParser.S: "S", morseParser.T: "T", morseParser.U: "U",
            morseParser.V: "V", morseParser.W: "W", morseParser.X: "X",
            morseParser.Y: "Y", morseParser.Z: "Z"
        }
        for child in ctx.getChildren():
            self.result += mapping.get(child.symbol.type, "")

    def enterMorse_digit(self, ctx):
        mapping = {
            morseParser.ZERO: "0", morseParser.ONE: "1", morseParser.TWO: "2",
            morseParser.THREE: "3", morseParser.FOUR: "4", morseParser.FIVE: "5",
            morseParser.SIX: "6", morseParser.SEVEN: "7", morseParser.EIGHT: "8",
            morseParser.NINE: "9"
        }
        for child in ctx.getChildren():
            self.result += mapping.get(child.symbol.type, "")

class TextTomorseListener(morseListener):
    def __init__(self):
        self.result = []

    def enterText_letter(self, ctx):
        mapping = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..'
        }
        for child in ctx.getChildren():
            self.result.append(mapping.get(child.getText(), ""))

    def enterText_digit(self, ctx):
        mapping = {
            '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
            '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
        }
        for child in ctx.getChildren():
            self.result.append(mapping.get(child.getText(), ""))



@app.post("/morse_to_text")
async def morse_to_text(request: MorseRequest):
    input_text = request.text
    if not input_text.strip():
        raise HTTPException(status_code=400, detail="Input text cannot be empty.")

    lexer = morseLexer(InputStream(input_text))
    stream = CommonTokenStream(lexer)
    parser = morseParser(stream)
    tree = parser.morse_code()

    listener = MorseToTextListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    return {"translated_text": listener.result}

@app.post("/text_to_morse")
async def text_to_morse(request: TextRequest):
    input_text = request.text.upper()
    if not input_text.strip():
        raise HTTPException(status_code=400, detail="Input text cannot be empty.")

    lexer = morseLexer(InputStream(input_text))
    stream = CommonTokenStream(lexer)
    parser = morseParser(stream)
    tree = parser.text_to_morse()

    listener = TextTomorseListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    return {"morse_code": " ".join(listener.result)}
