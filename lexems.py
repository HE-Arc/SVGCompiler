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
	'NUMBER',
	'IDENTIFIER',
	'BRACE_OPEN',
	'BRACE_CLOSE',
	'COMMENT',
	'OPENBRACKET',
	'CLOSEBRACKET',
) + tuple(map(lambda s: s.upper(), reserved_words))

t_BRACE_OPEN = '{'
t_BRACE_CLOSE = '}'
t_COMMENT = '//'


t_OPENBRACKET = r'\('
t_CLOSEBRACKET = r'\)'
t_OPENSQUAREBRACKET = r'\]'
t_CLOSESQUAREBRACKET = r'\]'


t_LINEBREAK = r';'
t_SEPARATOR = r','
t_AFFECTATION = r'='
t_DESCRIPTION = r':'

t_VARIABLENAME = r'\$[a-zA-Z0-9]'

t_DRAW = r'@' 

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

t_ignore = ' \t'


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
