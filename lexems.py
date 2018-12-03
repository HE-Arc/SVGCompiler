import ply.lex as lex

tokens = (
	'NUMBER',
	'ADD_OP',
	'MUL_OP',
	'OPENBRACKET',
	'CLOSEBRACKET'
)

t_ADD_OP = r'(\+|-)'
t_MUL_OP = r'(\*|\\)'

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