from rply import ParserGenerator, Token
from ast import Sum, Sub, Print, Number, BinaryOp, Mul, Div
from lexer import Lexer


class Parser:

    def __init__(self, module, builder, printf):
        self.pg = ParserGenerator([x for x, y in Lexer.tokens])
        self.module = module
        self.builder = builder
        self.printf = printf

    def parse(self):
        @self.pg.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def program(p) -> Print:
            return Print(p[2])

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MUL expression')
        @self.pg.production('expression : expression DIV expression')
        def expression(p) -> BinaryOp:
            left = p[0]
            right = p[2]
            operator = p[1]

            t = operator.gettokentype()
            if t == 'SUM':
                return Sum(self.builder, self.module, left, right)
            elif t == 'SUB':
                return Sub(self.builder, self.module, left, right)
            elif t == 'MUL':
                return Mul(self.builder, self.module, left, right)
            elif t == 'DIV':
                return Div(self.builder, self.module, left, right)

        @self.pg.production('expression : NUMBER')
        def number(p) -> Number:
            return Number(self.builder, self.module, p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
