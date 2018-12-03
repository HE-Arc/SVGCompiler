import ply.lex as lex

reserved_words = (
	"boolean",
	"true",
	"false",
	"integer",
	"string",
	"shape",
	"radius",
	"positionX",
	"positionY",
	"height",
	"width",
	"color",
	"red",
	"green",
	"blue",
	"yellow",
	"black",
	"white"
)

tokens = (
	'NUMBER',
	'ADD_OP',
	'MUL_OP',
	'OPENBRACKET',
	'CLOSEBRACKET'
)

t_OPENBRACKET = r'\('
t_CLOSEBRACKET = r'\)'
t_OPENSQUAREBRACKET = r'\]'
t_CLOSESQUAREBRACKET = r'\]'

t_LINEBREAK = r';'
t_SEPARATOR = r','
t_AFFECTATION = r'='
t_DESCRIPTION = r':'

t_VARIABLENAME = r'\$[a-zA-Z0-9]'

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

t_ignore = ' \t'

def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)