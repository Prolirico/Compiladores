from tokens import *
from model import *
from utils import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.curr = 0

    def advance(self):
        token = self.tokens[self.curr]
        self.curr = self.curr + 1
        return token

    def peek(self):
        return self.tokens[self.curr]

    def is_next(self, expected_type):
        if self.curr >= len(self.tokens):
            return False
        return self.peek().token_type == expected_type

    def expect(self, expected_type):
        if self.curr >= len(self.tokens):
            parse_error(f'Se encontro {self.previous_token().lexeme!r} al final del análisis', self.previous_token().line())#me falto () en previous_token
        elif self.peek().token_type == expected_type:
            token = self.advance()
            return token
        else:
            parse_error(f'Se esperaba {expected_type!r}, se encontro {self.peek().lexeme!r}.', self.peek().line)
    def previous_token(self):
        return self.tokens[self.curr - 1]

    def match(self,expected_type):
        if self.curr >= len(self.tokens):
            return False
        if self.peek().token_type != expected_type:
            return False
        self.curr = self.curr + 1
        return True


    def primary(self):
        if self.match(TOK_INTEGER):
            return Integer(int(self.previous_token().lexeme),line=self.previous_token().line)#se agrego el line=self.
        elif self.match(TOK_FLOAT):
            return Float(float(self.previous_token().lexeme),line=self.previous_token().line)#Se agrego el line=self.
        elif self.match(TOK_TRUE):
            return Bool(True,line=self.previous_token().line)
        elif self.match(TOK_FALSE):
            return Bool(False, line=self.previous_token().line)
        elif self.match(TOK_STRING):
            return String(str(self.previous_token().lexeme[1:-1]),line=self.previous_token().line)
        elif self.match(TOK_LPAREN):
            expr = self.expr()
            if(not self.match(TOK_RPAREN)):
                parse_error(f'Error: se esperaba ")"', self.previous_token().line)
            else:
                return Grouping(expr,line=self.previous_token().line)#se agrego el line=self.

    def unary(self):
        if self.match(TOK_NOT) or self.match(TOK_MINUS) or self.match(TOK_PLUS):
            op = self.previous_token()
            operand = self.unary()
            return UnOp(op, operand, line=op.line)# se cambio por line=op.line
        return self.primary()

    def exponent(self):
        expr = self.unary()
        while self.match(TOK_CARET):
            op = self.previous_token()
            right = self.exponent()
            expr = BinOp(op, expr, right, line=op.line)
        return expr

    def modulo(self):
        expr = self.exponent()
        while self.match(TOK_MOD):
            op = self.previous_token()
            right = self.exponent()
            expr = BinOp(op, expr, right, line=op.line)
        return expr

    def multiplication(self):
        expr = self.modulo()#tenia unary
        while self.match(TOK_STAR) or self.match(TOK_SLASH):
            op = self.previous_token()
            right = self.modulo()#tenia unary
            expr = BinOp(op, expr, right,line=op.line)#Cambie por line=op.line
        return expr
    def addition(self):
        expr = self.multiplication()
        while self.match(TOK_PLUS) or self.match(TOK_MINUS):
            op = self.previous_token()
            right = self.multiplication()
            expr = BinOp(op, expr, right, line=op.line)
        return expr

    def comparison(self):
        expr = self.addition()
        while self.match(TOK_GT) or self.match(TOK_GE) or self.match(TOK_LT) or self.match(TOK_LE):
            op = self.previous_token()
            right = self.addition()
            expr = BinOp(op, expr, right, line=op.line)
        return expr

    def equality(self):
        expr = self.comparison()
        while self.match(TOK_NE) or self.match(TOK_EQEQ):
            op = self.previous_token()
            right = self.comparison()
            expr = BinOp(op, expr, right, line=op.line)
        return expr

    def logical_and(self):
        expr = self.equality()
        while self.match(TOK_AND):
            op = self.previous_token()
            right = self.equality()
            expr = LogicalOp(op, expr, right, line=op.line)
        return expr

    def logical_or(self):
        expr = self.logical_and()
        while self.match(TOK_OR):
            op = self.previous_token()
            right = self.logical_and()
            expr = LogicalOp(op, expr, right, line=op.line)
        return expr

    def expr(self):
        return self.logical_or()

    def print_stmt(self, end):
        if self.match(TOK_PRINT) or self.match(TOK_PRINTLN):
            val = self.expr()
            return PrintStmt(val, end, line=self.previous_token().line)
    def if_stmt(self):
        self.expect(TOK_IF)
        test = self.expr()
        self.expect(TOK_THEN)
        then_stmts = self.stmts()
        if self.is_next(TOK_ELSE):
            self.advance()
            else_stmts = self.stmts()
        else:
            else_stmts = None
        self.expect(TOK_END)
        return IfStmt(test, then_stmts, else_stmts, line=self.previous_token().line)

    def while_stmt(self):
        self.expect(TOK_WHILE)
        test = self.expr()
        self.expect(TOK_DO)
        body_stmts = self.stmts()
        self.expect(TOK_END)
        return WhileStmt(test, body_stmts, line=self.previous_token().line)

    def for_stmt(self):
        #desarrollar
        pass

    def args(self):
        args = []
        while not self.is_next(TOK_RPAREN):
            args.append(self.expr())
            if not self.is_next(TOK_RPAREN):
                self.expect(TOK_COMMA)
        return args

    def params(self):
        params = []
        while not self.is_next(TOK_RPAREN):
            name = self.expect(TOK_IDENTIFIER)
            params.append(Param(name.lexeme, line=self.previous_token().line))
            if not self.is_next(TOK_RPAREN):
                self.expect(TOK_COMMA)
        return params

    def fun_decl(self):
        self.expect(TOK_FUNC)
        name = self.expect(TOK_IDENTIFIER)
        self.expect(TOK_LPAREN)
        params = self.params()
        self.expect(TOK_RPAREN)
        body_stmts = self.stmts()
        self.expect(TOK_END)
        return FunDecl(name.lexeme, params, body_stmts, line=self.previous_token().line)

    def stmt(self):
        if self.peek().token_type == TOK_PRINT:
            return self.print_stmt(end='')
        if self.peek().token_type == TOK_PRINTLN:
            return self.print_stmt(end='\n')
        elif self.peek().token_type == TOK_IF:
            return self.if_stmt()
        elif self.peek().token_type == TOK_WHILE:
            return self.while_stmt()
        elif self.peek().token_type == TOK_FOR:
            return self.for_stmt()
        elif self.peek().token_type == TOK_FUNC:
            return self.fun_decl()
        else:
            left = self.expr()
            if self.match(TOK_ASSIGN):
                right = self.expr()
                return Assignment(left,right, line=self.previous_token().line)
            else:
                return FuncCallStmt(self)

    def stmts(self):
        stmts = []
        while self.curr < len(self.tokens) and not self.is_next(TOK_ELSE) and not self.is_next(TOK_END):
            stmt = self.stmt()
            stmts.append(stmt)
        return Stmts(stmts, line=self.previous_token().line)

    def program(self):
        stmts = self.stmts()
        return stmts

    def parse(self):
        ast = self.program()#se pone program porque es la ultima funcion en lugar de expr
        return ast
