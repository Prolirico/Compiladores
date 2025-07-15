from lexer import Lexer

def main():
    with open('myscript.pinky', 'r') as f:
        source = f.read()
        
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    print("Tokens found:")
    for token in tokens:
        print(token)
        
if __name__ == "__main__":
    main()