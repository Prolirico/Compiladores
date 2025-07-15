def print_pretty_ast(ast_text):
    i = 0
    newline = False
    for ch in str(ast_text):
        if ch == '(':
            if not newline:
                print(end=' ')
            print(ch)
            i += 2
            newline = True
        elif ch == ')':
            if not newline:
                print()
            i -= 2
            newline = True
            print(' '*i + ch)
        else:
            if newline:
                print(' '*i, end='')
            print(ch, end='')
            newline = False

def lexing_error(message, lineno):
    print(f'{Colors.RED}[linea {lineno}]:{message}{Colors.WHITE}')
    import sys
    sys.exit(1)

def parse_error(message, lineno):
    print(f'{Colors.RED}[linea {lineno}]:{message}{Colors.WHITE}')
    import sys
    sys.exit(1)

def runtime_error(message, lineno):
    print(f'{Colors.RED}[linea {lineno}]:{message}{Colors.WHITE}')
    import sys
    sys.exit(1)

class Colors:
    WHITE = '\033[0m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    LIGHT_GRAY = '\033[37m'
    DARK_GRAY = '\033[90m'
