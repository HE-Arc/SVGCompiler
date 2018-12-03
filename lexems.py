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
	'LINE_BREAK',
	't_SEPARATOR',
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

	'COLOR_HEX',

	'COMMENT',
	'DRAW',

	'IGNORE',

	'VARIABLE_NAME',

	'NUMBER',
	'KEYWORD',
) + tuple(map(lambda s: s.upper(), reserved_words))


t_LINE_BREAK = r';'
t_SEPARATOR = r','
t_AFFECTATION = r'='
t_DESCRIPTION = r':'

t_BRACE_OPEN = '{'
t_BRACE_CLOSE = '}'
t_BRACKET_OPEN = r'\('
t_BRACKET_CLOSE = r'\)'
t_SQUAREBRACKET_OPEN = r'\['
t_SQUAREBRACKET_CLOSE = r'\]'

t_QUOTE = r'\"|\''

t_COLOR_HEX = r'\#[0-9A-Fa-f]{6};'

t_COMMENT = '//'
t_DRAW = r'@'

t_ignore  = ' |\t|\n'

t_VARIABLE_NAME = r'\$[a-zA-Z0-9]'

def t_KEYWORD(t):
	r'[A-Za-z_]\w*'
	if t.value in reserved_words:
		t.type = t.value.upper()
	return t


def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)

lex.lex()

if __name__=="__main__":
	fileName="testLex.txt"
	lex.input(open(fileName).read())

	while 1:
		tok=lex.token()
		if not tok:
			break
		print (f"Line {tok.lineno}: {tok.type} ({tok.value})")
