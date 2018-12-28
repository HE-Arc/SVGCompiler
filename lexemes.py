#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ply.lex as lex

reserved_words = (
	"if",
	"elseif",
	"else",
	"while",
	"for",

	"boolean",
	"integer",
	"shape",

	"circle",
	"triangle",
	"rectangle",

	"true",
	"false",

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

def t_KEYWORD(t):
	r'[A-Za-z_]\w*'
	if t.value in reserved_words:
		t.type = t.value.upper()
		return t
	else:
		return t_error(t)

# Separators
t_LINE_BREAK = r';'
t_SEPARATOR = r','
t_AFFECTATION = r'='
t_DESCRIPTION = r':'

# Groups
t_BRACE_OPEN = '{'
t_BRACE_CLOSE = '}'
t_BRACKET_OPEN = r'\('
t_BRACKET_CLOSE = r'\)'
t_SQUAREBRACKET_OPEN = r'\['
t_SQUAREBRACKET_CLOSE = r'\]'

t_DRAW = r'@'

t_VARIABLE_NAME = r'\$[a-zA-Z0-9_]+'

# Integer Arithmetic
t_INTEGER_PLUS = r'\+'
t_INTEGER_MINUS = r'-'
t_INTEGER_TIMES = r'\*'
t_INTEGER_DIVIDE = r'/'

# Boolean Arithmetic
t_BOOL_NOT = r'!'
t_BOOL_OR = r"\|\|"
t_BOOL_AND = r'&&'
t_BOOL_LT = r'<'
t_BOOL_GT = r'>'
t_BOOL_EQUAL = r'=='
t_BOOL_NOT_EQUAL = r'!='

# Values
t_COLOR_HEX = r'\#[0-9A-Fa-f]{6}'

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

t_SHAPE_TYPE = r'circle|triangle|rectangle'

# useful ! : https://stackoverflow.com/a/29595453/9263555
# i wasted a ton of time because i tried to put all in t_ignore with a single regex with pipes
t_ignore_comments = r'//.*\n'
t_ignore_linebreak = r'\n'
t_ignore_spaces = r'\s'

def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)

tokens = (
	'COMMENT',
	'ignore',
	'LINE_BREAK',
	'SEPARATOR',
	'AFFECTATION',
	'DESCRIPTION',

	'BRACE_OPEN',
	'BRACE_CLOSE',
	'BRACKET_OPEN',
	'BRACKET_CLOSE',
	'SQUAREBRACKET_OPEN',
	'SQUAREBRACKET_CLOSE',

	'QUOTE',

	'SHAPE_TYPE',


	'INTEGER_PLUS',
	'INTEGER_MINUS',
	'INTEGER_TIMES',
	'INTEGER_DIVIDE',

	'BOOL_NOT',

	'BOOL_OR',
	'BOOL_AND',
	'BOOL_LT',
	'BOOL_GT',
	'BOOL_EQUAL',
	'BOOL_NOT_EQUAL',

	'COLOR_HEX',

	'DRAW',

	'VARIABLE_NAME',

	'NUMBER',
) + tuple(map(lambda s: s.upper(), reserved_words))

lex.lex()

if __name__=="__main__":
	fileName="testLex2.phsvg"
	lex.input(open(fileName).read())

	while 1:
		tok=lex.token()
		if not tok:
			break
		print (f"Line {tok.lineno}: {tok.type} ({tok.value})")
