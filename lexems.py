import ply.lex as lex

reserved_words = (
    'if',
    'elseif'
    'else',
    'while',
    'for'
)


tokens = (
    'NUMBER',
    'IDENTIFIER',
    'BRACE_OPEN',
    'BRACE_CLOSE',
    'COMMENT',
) + tuple(map(lambda s: s.upper(), reserved_words))

t_BRACE_OPEN = '{'
t_BRACE_CLOSE = '}'
t_COMMENT = '//'


def t_NUMBER(t):
    r'\d+\.*\d*'
    t.value = float(t.value)
    return t


t_OPENBRACKET = r'\('
t_CLOSEBRACKET = r'\)'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
