#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module used for the lexical analysis by "SVGCompiler"
It is not meant to be directly executed for a "normal" use, execute it only for intermediate debugging purposes
Sergiy Goloviatinski & Raphaël Margueron, inf3dlm-b, HE-Arc
13.01.19
"""

import ply.lex as lex
import sys
from functools import reduce
import re

conversion_table = {
    "BOOL_VALUE" : {
        "true" : True,
        "false" : False,
    },
    "COLOR_HEX" : {
        "red" : '#ff0000',
        "green" : '#00ff00',
        "blue" : '#0000ff',
        "yellow" : '#ffff00',
        "black" : '#000000',
        "white" : '#ffffff',
    }
}

conversion_table_words = reduce(lambda a1, a2: list(a1[1].keys()) + list(a2[1].keys()), conversion_table.items()); # grab all the keys in the conversion_table of the subtables

reserved_words = (
    "if",
    "else",
    "while",

    "boolean",
    "integer",
    "shape",

    "circle",
    "triangle",
    "rectangle",

    "radius",
    "positionX",
    "positionY",
    "height",
    "width",
    "color"
)

def t_keywords(t):
    r'[A-Za-z_]\w*'
    if t.value in reserved_words: # for the keywords juste get them
        t.type = t.value.upper()
        return t
    elif t.value in conversion_table_words: # in the conversion_table so where is it?
        for subTableName, subTable in conversion_table.items(): # in which subTable is it ?
            if t.value in subTable:
                t.value = subTable[t.value]
                t.type = subTableName
        return t
    else: # letters unknown
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
t_INTEGER_MODULO = r'%'
t_INTEGER_RANDOM = r'~'

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


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# useful ! : https://stackoverflow.com/a/29595453/9263555
# i wasted a ton of time because i tried to put all in t_ignore with a single regex with pipes
def t_ignore_comments(t):
    r'//.*\n'
    t.lexer.lineno += 1

t_ignore_spaces = r'\s'

def t_error(t):
    print(f'Illegal character \'{t.value[0]}\' at line {t.lineno}')
    t.lexer.skip(1)

functions = []
for key in list(locals().keys()):
    match = re.search("t_[A-Z]+", key)
    if match:
        functions.append(key[2:])

tokens = tuple(set(tuple(functions) + tuple(map(lambda s: s.upper(), reserved_words)) + tuple(conversion_table.keys())))

lex.lex()

if __name__ == "__main__":
    prog = open(sys.argv[1]).read()
    lex.input(prog)

    while 1:
        tok = lex.token()
        if not tok:
            break
        print(f"Line {tok.lineno}: {tok.type} ({tok.value})")
