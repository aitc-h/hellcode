from lexer import Lexer
from my_parser import Parser

if __name__ == '__main__':
    text_input = "☼(5♦4);"

    lexer = Lexer().get_lexer()
    tokens = lexer.lex(text_input)

    pg = Parser()
    pg.parse()
    parser = pg.get_parser()
    parser.parse(tokens).eval()
