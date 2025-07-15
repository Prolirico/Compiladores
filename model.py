from tokens import *
class Node:
    pass

class Expr(Node):
    pass

class Stmt(Node):
    pass

class Decl(Stmt):
    pass

class Integer(Expr):
    def __init__(self, value, line):
        assert isinstance(value, int), value
        self.value = value
        self.line = line
    def __repr__(self):
        return f'Integer[{self.value}]'

class Float(Expr):
    def __init__(self, value, line):
        assert isinstance(value, float), value
        self.value = value
        self.line = line
    def __repr__(self):
        return f'Float[{self.value}]'

class Bool(Expr):
    def __init__(self, value, line):
        assert isinstance(value, bool), value
        self.value = value
        self.line = line
    def __repr__(self):
        return f'Bool[{self.value}]'

class String(Expr):
    def __init__(self, value, line):
        assert isinstance(value, str), value
        self.value = value
        self.line = line
    def __repr__(self):
        return f'String[{self.value}]'


class UnOp(Expr):
    def __init__(self, op: Token, operand: Expr, line):
        assert isinstance(op, Token), op
        assert isinstance(operand, Expr), operand
        self.op = op
        self.operand = operand
        self.line = line
    def __repr__(self):
        return f'UnOp({self.op.lexeme!r}, {self.operand})'

class BinOp(Expr):
    def __init__(self, op: Token, left: Expr, right: Expr, line):
        assert isinstance(op, Token), op
        assert isinstance(left, Expr), left
        assert isinstance(right, Expr), right
        self.op = op
        self.left = left
        self.right = right#se cambiaron de posicion
        self.line = line
    def __repr__(self):
        return f'BinOp({self.op.lexeme!r}, {self.left}, {self.right})'

class LogicalOp(Expr):
    def __init__(self, op: Token, left: Expr, right: Expr, line):
        assert isinstance(op, Token), op
        assert isinstance(left, Expr), left
        assert isinstance(right, Expr), right
        self.op = op
        self.left = left
        self.right = right
        self.line = line
    def __repr__(self):
        return f'LogicalOp({self.op.lexeme!r}, {self.left}, {self.right})'


class Grouping(Expr):
    def __init__(self, value, line):
        assert isinstance(value, Expr), value
        self.value = value
        self.line = line
    def __repr__(self):
        return f'Grouping({self.value})'

class Identifier(Expr):
    def __init__(self, name, line):
        assert isinstance(name, str), name
        self.name = name
        self.line = line

    def __repr__(self):
        return f'Identificador[{self.name!r}]'

class Stmts(Node):
    def __init__(self, stmts, line):
        assert all(isinstance(stmt, Stmt) for stmt in stmts), stmts
        self.stmts = stmts
        self.line = line
    def __repr__(self):
        return f'Stmts({self.stmts})'

class PrintStmt(Stmt):
    def __init__(self, value, end,line):
        assert isinstance(value, Expr), value
        self.value = value
        self.end = end
        self.line = line
    def __repr__(self):
        return f'PrintStmt({self.value}, end={self.end!r})'

class WhileStmt(Stmt):
    def __init__(self,test, body_stmts,line):
        assert isinstance(test, Expr), test
        assert isinstance(body_stmts, Stmts), body_stmts
        self.test = test
        self.body_stmts = body_stmts
        self.line = line

    def __repr__(self):
        return f'WhileStmt({self.test}, {self.body_stmts})'

class Assignment(Stmt):
    def __init__(self,left,right,line):
        assert isinstance(left, Expr), left
        assert isinstance(right, Expr), right
        self.left = left
        self.right = right
        self.line = line

    def __repr__(self):
        return f'Assignment({self.left}, {self.right})'

class IfStmt(Stmt):
    def __init__(self, test, then_stmts, else_stmts, line):
        assert isinstance(test, Expr), test
        assert isinstance(then_stmts, Stmts), then_stmts
        assert else_stmts is None or isinstance(else_stmts, Stmts), else_stmts
        self.test = test
        self.then_stmts = then_stmts
        self.else_stmts = else_stmts
        self.line = line
    def __repr__(self):
        return f'IfStmt({self.test}, entonces:{self.then_stmts}, si no:{self.else_stmts})'

class ForStmt(Stmt):
    #desarrollar
    pass

class FuncDecl(Decl):
    def __init__(self,name,params,body_stmts,line):
        assert isinstance(name, str), name
        assert all(isinstance(param, Param) for param in params), params
        assert isinstance(body_stmts, Stmts), body_stmts
        self.name = name
        self.params = params
        self.body_stmts = body_stmts
        self.line = line
    def __repr__(self):
        return f'FuncDecl({self.name!r}, {self.params}, {self.body_stmts})'

class Param(Decl):
    def __init__(self,name,line):
        assert isinstance(name, str), name
        self.name = name
        self.line = line
    def __repr__(self):
        return f'Param({self.name!r}, {self.type})'

def FunCall(Expr):
    def __init__(self,name,args,line):
        self.name = name
        self.args = args
        self.line = line
    def __repr__(self):
        return f'FunCall({self.name!r}, {self.args})'

class FuncCallStmt(Stmt):
    def __init__(self,expr):
        assert isinstance(expr, FuncCall), expr
        self.expr = expr
    def __repr__(self):
        return f'FuncCallStmt({self.expr})'
