grammar morse;

morse_code : (morse_letter | morse_digit | WS)* ;
text_to_morse : (text_letter | text_digit | WS)* ;

morse_letter : A | B | C | D | E | F | G | H | I | J | K | L | M |
               N | O | P | Q | R | S | T | U | V | W | X | Y | Z ;
morse_digit : ZERO | ONE | TWO | THREE | FOUR | FIVE | SIX | SEVEN | EIGHT | NINE ;

text_letter : 'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'G' | 'H' | 'I' | 'J' | 'K' | 'L' | 'M' |
              'N' | 'O' | 'P' | 'Q' | 'R' | 'S' | 'T' | 'U' | 'V' | 'W' | 'X' | 'Y' | 'Z' ;
text_digit : '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' ;

// Lexer rules for Morse code
A : '.-' ;
B : '-...' ;
C : '-.-.' ;
D : '-..' ;
E : '.' ;
F : '..-.' ;
G : '--.' ;
H : '....' ;
I : '..' ;
J : '.---' ;
K : '-.-' ;
L : '.-..' ;
M : '--' ;
N : '-.' ;
O : '---' ;
P : '.--.' ;
Q : '--.-' ;
R : '.-.' ;
S : '...' ;
T : '-' ;
U : '..-' ;
V : '...-' ;
W : '.--' ;
X : '-..-' ;
Y : '-.--' ;
Z : '--..' ;

ZERO : '-----' ;
ONE : '.----' ;
TWO : '..---' ;
THREE : '...--' ;
FOUR : '....-' ;
FIVE : '.....' ;
SIX : '-....' ;
SEVEN : '--...' ;
EIGHT : '---..' ;
NINE : '----.' ;

// Skip whitespace
WS : [ \t\r\n]+ -> skip ;
