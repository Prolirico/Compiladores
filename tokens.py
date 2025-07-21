# Constantes para diferentes tipos de tokens
TOK_LPAREN = 'TOKEN_LPAREN' # (
TOK_RPAREN = 'TOKEN_RPAREN' # )
TOK_LCURLY = 'TOKEN_LCURLY' # {
TOK_RCURLY = 'TOKEN_RCURLY' # }
TOK_LSQUAR = 'TOKEN_LSQUAR' # [
TOK_RSQUAR = 'TOKEN_RSQUAR' # ]
TOK_COMMA = 'TOKEN_COMMA' # ,
TOK_DOT = 'TOKEN_DOT' # .
TOK_PLUS = 'TOKEN_PLUS' # +
TOK_MINUS = 'TOKEN_MINUS' # -
TOK_STAR = 'TOKEN_STAR' # *
TOK_SLASH = 'TOKEN_SLASH' # /
TOK_CARET = 'TOKEN_CARET' # ^
TOK_MOD = 'TOKEN_MOD' # %
TOK_COLON = 'TOKEN_COLON' # :
TOK_SEMICOLON = 'TOKEN_SEMICOLON' # ;
TOK_QUESTION = 'TOKEN_QUESTION' # ?
TOK_NOT = 'TOKEN_NOT' # !
TOK_GT = 'TOKEN_GT' # >
TOK_LT = 'TOKEN_LT' # <
# Dos caracteres
TOK_GE         = 'TOK_GE'         #  >=
TOK_LE         = 'TOK_LE'         #  <=
TOK_NE         = 'TOK_NE'         #  ~=
TOK_EQEQ         = 'TOK_EQ'         #  ==
TOK_ASSIGN     = 'TOK_ASSIGN'     #  :=
TOK_GTGT       = 'TOK_GTGT'       #  >>
TOK_LTLT       = 'TOK_LTLT'       #  <<
# Literales
TOK_IDENTIFIER = 'TOK_IDENTIFIER'
TOK_STRING     = 'TOK_STRING'
TOK_INTEGER    = 'TOK_INTEGER'
TOK_FLOAT      = 'TOK_FLOAT'
# Palabras
TOK_IF         = 'TOK_IF'
TOK_THEN       = 'TOK_THEN'
TOK_ELSE       = 'TOK_ELSE'
TOK_TRUE       = 'TOK_TRUE'
TOK_FALSE      = 'TOK_FALSE'
TOK_AND        = 'TOK_AND'
TOK_OR         = 'TOK_OR'
TOK_WHILE      = 'TOK_WHILE'
TOK_DO         = 'TOK_DO'
TOK_FOR        = 'TOK_FOR'
TOK_FUNC       = 'TOK_FUNC'
TOK_NULL       = 'TOK_NULL'
TOK_END        = 'TOK_END'
TOK_PRINT      = 'TOK_PRINT'
TOK_PRINTLN    = 'TOK_PRINTLN'
TOK_RET        = 'TOK_RET'
TOK_EOF        = 'TOKEN_EOF'  # Added for end-of-stream
TOK_IN = 'TOK_IN'  # in
TOK_TO = 'TOK_TO'  # to

palabras = {
    'if': TOK_IF,
    'then': TOK_THEN,
    'else': TOK_ELSE,
    'true': TOK_TRUE,
    'false': TOK_FALSE,
    'and': TOK_AND,
    'or': TOK_OR,
    'while': TOK_WHILE,
    'do': TOK_DO,
    'for': TOK_FOR,
    'func': TOK_FUNC,
    'null': TOK_NULL,
    'end': TOK_END,
    'print': TOK_PRINT,
    'println': TOK_PRINTLN,
    'ret': TOK_RET,
    'in': TOK_IN,
    'to': TOK_TO
}

class Token:
    def __init__(self, token_type, lexeme, line):
        self.token_type = token_type
        self.lexeme = lexeme
        self.line = line

    def __repr__(self) -> str:
        return f'({self.token_type},{self.lexeme!r}, {self.line})'
