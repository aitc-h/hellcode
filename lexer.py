from rply import LexerGenerator


class Lexer:

    tokens = [
            ('PRINT', r'☼'),
            ('OPEN_PAREN', r'\('),
            ('CLOSE_PAREN', r'\)'),
            ('SEMI_COLON', r'\;'),
            ('SUM', r'\♥'),
            ('MUL', r'\♦'),
            ('DIV', r'\♣'),
            ('SUB', r'\♠'),
            ('NUMBER', r'\d+')
        ]

    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        for s, t in Lexer.tokens:
            self.lexer.add(s, t)
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
