from tokens import Token
import unittest
import tokens
from utils import *
from tokens import *
from lexer import *
from parser import *
from interprete import *
import inspect

class TestExpressions(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)

    def test_number_primary(self):
        source = '''14.89'''
        expected_output = (TYPE_NUMBER, 14.89)
        tokens = Lexer(source).tokenize()
        ast = Parser(tokens).parse()
        result = Interprete().interpret(ast)
        self.assertEqual(result, expected_output)

    def test_bool_primary(self):
        source = '''false'''
        expected_output = (TYPE_BOOL, False)
        tokens = Lexer(source).tokenize()
        ast = Parser(tokens).parse()
        result = Interprete().interpret(ast)
        self.assertEqual(result, expected_output)

    def test_Add(self):
        source = '''1+2'''
        expected_output = (TYPE_NUMBER, 3)
        tokens = Lexer(source).tokenize()
        ast = Parser(tokens).parse()
        result = Interprete().interpret(ast)
        self.assertEqual(result, expected_output)

    def test_mul(self):
        source = '''4*2'''
        expected_output = (TYPE_NUMBER, 8)
        tokens = Lexer(source).tokenize()
        ast = Parser(tokens).parse()
        result = Interprete().interpret(ast)
        self.assertEqual(result, expected_output)

    def test_division(self):
        source = '''4/2'''
        expected_output = (TYPE_NUMBER, 2)
        tokens = Lexer(source).tokenize()
        ast = Parser(tokens).parse()
        result = Interprete().interpret(ast)
        self.assertEqual(result, expected_output)

    def test_precedence(self):
        source = '''1+2*3'''
        expected_output = (TYPE_NUMBER, 7)
        tokens = Lexer(source).tokenize()
        ast = Parser(tokens).parse()
        result = Interprete().interpret(ast)
        self.assertEqual(result, expected_output)

    def test_unary_minus(self):
        source = '''2 * 9 - -5'''
        expected_output = (TYPE_NUMBER, 23)
        tokens = Lexer(source).tokenize()
        ast = Parser(tokens).parse()
        result = Interprete().interpret(ast)
        self.assertEqual(result, expected_output)

    def test_caret(self):
        source = '''2 ^ 3'''
        expected_output = (TYPE_NUMBER, 8)
        tokens = Lexer(source).tokenize()
        ast = Parser(tokens).parse()
        result = Interprete().interpret(ast)
        self.assertEqual(result, expected_output)

    def test_mod(self):
        source = '''2 % 3'''
        expected_output = (TYPE_NUMBER, 2)
        tokens = Lexer(source).tokenize()
        ast = Parser(tokens).parse()
        result = Interprete().interpret(ast)
        self.assertEqual(result, expected_output)

    def test_paren_1(self):
        source = '''(2 + 3) * (4*2)'''
        expected_output = (TYPE_NUMBER, 40)
        tokens = Lexer(source).tokenize()
        ast = Parser(tokens).parse()
        result = Interprete().interpret(ast)
        self.assertEqual(result, expected_output)

    def test_paren_2(self):
        source = '''2 * (9+15) + 2^2 + (((3*3)-3)+3.3/2)'''
        expected_output = (TYPE_NUMBER, 59.65)
        tokens = Lexer(source).tokenize()
        ast = Parser(tokens).parse()
        result = Interprete().interpret(ast)
        self.assertEqual(result, expected_output)

    def test_bool_or(self):
        source = '''(53>=3) or true and 1>0'''
        expected_output = (TYPE_BOOL, True)
        tokens = Lexer(source).tokenize()
        ast = Parser(tokens).parse()
        result = Interprete().interpret(ast)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
