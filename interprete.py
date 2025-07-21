from utils import *
from model import *
from tokens import *
from state import *
import codecs

TYPE_NUMBER = 'Tipo_Numero'
TYPE_STRING = 'Tipo_Cadena'
TYPE_BOOL = 'Tipo_Booleano'

class Interprete:
    def interpret(self, node, env):
        if isinstance(node, Integer):
            return (TYPE_NUMBER, float(node.value))

        elif isinstance(node, Float):
            return (TYPE_NUMBER, float(node.value))

        elif isinstance(node, String):
            return (TYPE_STRING, str(node.value))

        elif isinstance(node, Bool):
            return (TYPE_BOOL, node.value)

        elif isinstance(node, Grouping):
            return self.interpret(node.value, env)

        elif isinstance(node, Identifier):
            value = env.get_var (node.name)
            if value is None:
                runtime_error(f'Identificador no declarado {node.name!r}',node.line)
            if value[1] is None:
                runtime_error(f'Identificador no inicializado {node.name!r}',node.line)
            return value

        elif isinstance(node, Assignment):
            righttype, rightval = self.interpret(node.right, env)
            env.set_var(node.left.name, (righttype, rightval))

        elif isinstance(node, BinOp):
            lefttype, leftval  = self.interpret(node.left, env)#se agrego env
            righttype, rightval = self.interpret(node.right, env)#se agrego env
            if node.op.token_type == TOK_PLUS:
                if lefttype == TYPE_NUMBER and righttype == TYPE_NUMBER:
                    return (TYPE_NUMBER, leftval + rightval)
                elif lefttype == TYPE_STRING or righttype == TYPE_STRING:#sustitui el and por el or
                    return (TYPE_STRING, str(leftval) + str(rightval))
                else:
                    runtime_error(f'Operador no soportado {node.op.lexeme!r} entre {lefttype} y {righttype}.', node.op.line)

            elif node.op.token_type == TOK_MINUS:
                if lefttype == TYPE_NUMBER and righttype == TYPE_NUMBER:
                    return (TYPE_NUMBER, leftval - rightval)
                else:
                    runtime_error(f'Operador no soportado {node.op.lexeme!r} entre {lefttype} y {righttype}.',node.op.line)

            elif node.op.token_type == TOK_STAR:
                if lefttype == TYPE_NUMBER and righttype == TYPE_NUMBER:
                    return (TYPE_NUMBER, leftval * rightval)
                else:
                    runtime_error(f'Operador no soportado {node.op.lexeme!r} entre {lefttype} y {righttype}.',node.op.line)

            elif node.op.token_type == TOK_SLASH:
                if rightval == 0:
                    runtime_error(f'División entre cero', node.line)
                if lefttype == TYPE_NUMBER and righttype == TYPE_NUMBER:
                    return (TYPE_NUMBER, leftval / rightval)#se le agrego el TYPE_NUMBER
                else:
                    runtime_error(f'Operador no soportado {node.op.lexeme!r} entre {lefttype} y {righttype}.',node.op.line)

            #agregamos estos elif que faltaban
            elif node.op.token_type == TOK_MOD:
                if lefttype == TYPE_NUMBER and righttype == TYPE_NUMBER:
                    return (TYPE_NUMBER, leftval % rightval)
                else:
                    runtime_error(f'Operador no soportado {node.op.lexeme!r} entre {lefttype} y {righttype}.',node.op.line)

            elif node.op.token_type == TOK_CARET:
                if lefttype == TYPE_NUMBER and righttype == TYPE_NUMBER:
                    return (TYPE_NUMBER, leftval ** rightval)
                else:
                    runtime_error(f'Operador no soportado {node.op.lexeme!r} entre {lefttype} y {righttype}.',node.op.line)

            #Agregar operaciones que nos faltan
            elif node.op.token_type == TOK_GT:
                if(lefttype == TYPE_NUMBER and righttype == TYPE_NUMBER) or (lefttype == TYPE_STRING and righttype == TYPE_STRING):
                    return (TYPE_BOOL, leftval > rightval)
                else:
                    runtime_error(f'Operador no soportado {node.op.lexeme!r} entre {lefttype} y {righttype}.', node.op.line)

            elif node.op.token_type == TOK_GE:
                if(lefttype == TYPE_NUMBER and righttype == TYPE_NUMBER) or (lefttype == TYPE_STRING and righttype == TYPE_STRING):
                    return (TYPE_BOOL, leftval >= rightval)
                else:
                    runtime_error(f'Operador no soportado {node.op.lexeme!r} entre {lefttype} y {righttype}.', node.op.line)

            #aqui nos toca realizar ahora el de < y <=
            elif node.op.token_type == TOK_LT:
                if(lefttype == TYPE_NUMBER and righttype == TYPE_NUMBER) or (lefttype == TYPE_STRING and righttype == TYPE_STRING):
                    return (TYPE_BOOL, leftval < rightval)
                else:
                    runtime_error(f'Operador no soportado {node.op.lexeme!r} entre {lefttype} y {righttype}.', node.op.line)

            elif node.op.token_type == TOK_LE:
                if(lefttype == TYPE_NUMBER and righttype == TYPE_NUMBER) or (lefttype == TYPE_STRING and righttype == TYPE_STRING):
                    return (TYPE_BOOL, leftval <= rightval)
                else:
                    runtime_error(f'Operador no soportado {node.op.lexeme!r} entre {lefttype} y {righttype}.', node.op.line)

            elif node.op.token_type == TOK_EQEQ:
                if(lefttype == TYPE_NUMBER and righttype == TYPE_NUMBER) or (lefttype == TYPE_STRING and righttype == TYPE_STRING) or (lefttype == TYPE_BOOL and righttype == TYPE_BOOL):
                    return (TYPE_BOOL, leftval == rightval)
                else:
                    runtime_error(f'Operador no soportado {node.op.lexeme!r} entre {lefttype} y {righttype}.', node.op.line)

            elif node.op.token_type == TOK_NE:
                if(lefttype == TYPE_NUMBER and righttype == TYPE_NUMBER) or (lefttype == TYPE_STRING and righttype == TYPE_STRING) or (lefttype == TYPE_BOOL and righttype == TYPE_BOOL):
                    return (TYPE_BOOL, leftval != rightval)
                else:
                    runtime_error(f'Operador no soportado {node.op.lexeme!r} entre {lefttype} y {righttype}.', node.op.line)

        elif isinstance(node, UnOp):
            operandtype, operand = self.interpret(node.operand, env)
            if node.op.token_type == TOK_MINUS:
                if operandtype == TYPE_NUMBER:
                    return (TYPE_NUMBER, -operand)
                else:
                    runtime_error(f'Operador no soportado {node.op.lexeme!r} con {operandtype}.',node.op.line)

            if node.op.token_type == TOK_PLUS:
                if operandtype == TYPE_NUMBER:
                    return (TYPE_NUMBER, operand)#se quito el signo +
                else:
                    runtime_error(f'Operador no soportado {node.op.lexeme!r} con {operandtype}.',node.op.line)
            #se agrego este elif
            elif node.op.token_type == TOK_NOT:
                if operandtype == TYPE_BOOL:
                    return (TYPE_BOOL, not operand)
                else:
                    runtime_error(f'Operador no soportado {node.op.lexeme!r} con {operandtype}.',node.op.line)

        elif isinstance(node, LogicalOp):#no estaba en posicion, estaba recorrido a la derecha una posición
            lefttype, leftval = self.interpret(node.left, env)
            if node.op.token_type == TOK_OR:
                if leftval:
                    return (lefttype, leftval)
            elif node.op.token_type == TOK_AND:
                if not leftval:
                    return (lefttype, leftval)
            return self.interpret(node.right, env)

        elif isinstance(node, Stmts):
            for stmt in node.stmts:
                self.interpret(stmt, env)

        elif isinstance(node, PrintStmt):
            exprtype, exprval = self.interpret(node.value, env)
            print(codecs.escape_decode(bytes(str(exprval), "utf-8"))[0].decode("utf-8"), end=node.end)

        elif isinstance(node,IfStmt):
            testtype, testval = self.interpret(node.test, env)
            if testtype != TYPE_BOOL:
                runtime_error('La prueba de condición no es una expresión booleana',node.line)
            if testval:
                self.interpret(node.then_stmts, env.new_env())
            else:
                self.interpret(node.else_stmts, env.new_env())

        elif isinstance(node,WhileStmt):
            new_env = env.new_env()
            while True:
                testtype, testval = self.interpret(node.test, env)
                if testtype != TYPE_BOOL:
                    runtime_error(f'While no es una expresión booleana.', node.line)
                if not testval:
                    break
                self.interpret(node.body_stmts, new_env)

        elif isinstance(node, ForStmt):
            start_type, start_val = self.interpret(node.start, env)
            end_type, end_val = self.interpret(node.end, env)
            if start_type != TYPE_NUMBER or end_type != TYPE_NUMBER:
                runtime_error(f'Los límites del bucle for deben ser números.', node.line)
            if not float(start_val).is_integer() or not float(end_val).is_integer():
                runtime_error(f'Los límites del bucle for deben ser enteros.', node.line)
            start_val = int(start_val)
            end_val = int(end_val)
            new_env = env.new_env()
            for i in range(start_val, end_val + 1):
                new_env.set_var(node.var.name, (TYPE_NUMBER, float(i)))
                self.interpret(node.body_stmts, new_env)

        elif isinstance(node, FuncDecl):
            env.set_func(node.name, (node, env))

        elif isinstance(node, FuncCall):
            func = env.get_func(node.name)
            if not func:
                runtime_error(f'Funcion {node.name!r} no declarada.', node.line)

            func_decl = func[0]

            func_env = func[1]

            if len(node.args) != len(func_decl.params):
                runtime_error(f'Funcion {func_decl.name!r} esperada {len(func_decl.params)} se pasaron parametros pero {len(node.args)} argumentos', node.line)

            args = []
            for arg in node.args:
                args.append(self.interpret(arg, env))

            new_func_env = func_env.new_env()

            for param, argval in zip(func_decl.params, args):
                new_func_env.set_var(param.name, argval)

            self.interpret(func_decl.body_stmts, new_func_env)

        elif isinstance(node, FuncCallStmt):
            self.interpret(node.expr, env)

    def interpret_ast(self, node):
        env = Environment()
        self.interpret(node, env)
