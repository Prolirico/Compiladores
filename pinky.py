import sys
from tokens import *
from lexer import *
from utils import *
from interprete import *
from parser import Parser

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Usa: python3 pinky.py <filename>')
    filename = sys.argv[1]
    print(filename)

    with open(filename) as file:
        source = file.read()

        print(f'{Colors.BLUE}***************{Colors.WHITE}')
        print(f'{Colors.BLUE}Código:{Colors.WHITE}')
        print(f'{Colors.BLUE}***************{Colors.WHITE}')
        print(source)

        print(f'{Colors.BLUE}***************{Colors.WHITE}')
        print(f'{Colors.BLUE}LÉXICO:{Colors.WHITE}')
        print(f'{Colors.BLUE}***************{Colors.WHITE}')
        tokens = Lexer(source).tokenize()
        for tok in tokens: print(tok)

        print()
        print(f'{Colors.BLUE}***************{Colors.WHITE}')
        print(f'{Colors.BLUE}ANALIZADOR AST:{Colors.WHITE}')
        print(f'{Colors.BLUE}***************{Colors.WHITE}')

        parser = Parser(tokens)
        ast = Parser(tokens).parse()
        print_pretty_ast(ast)

        print(f'{Colors.GREEN}***************{Colors.WHITE}')
        print(f'{Colors.GREEN}INTERPRETE:{Colors.WHITE}')
        print(f'{Colors.GREEN}***************{Colors.WHITE}')

        interprete = Interprete()
        val = interprete.interpret(ast)
        print(val)
