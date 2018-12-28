#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ply.yacc as yacc
from lexemes import tokens
import AST

precedence = (
    ('left', 'INTEGER_MINUS'),
    ('right', 'INTEGER_PLUS'),
    ('left', 'INTEGER_DIVIDE'),
    ('left', 'INTEGER_TIMES'),

    ('left', 'BOOL_OR'),
    ('left', 'BOOL_AND'),

    ('left', 'BOOL_EQUAL'),
    ('left', 'BOOL_NOT_EQUAL'),

    ('left', 'BOOL_LT'),
    ('left', 'BOOL_GT'),

    ('right', 'UNARYNUMBER'),
    ('right', 'UNARYBOOL'),
)

binaryOperators = (
    "INTEGER_DIVIDE"
    "INTEGER_TIMES"
    "INTEGER_MINUS"
    "INTEGER_PLUS"
    "BOOL_EQUAL"
    "BOOL_NOT_EQUAL"
    "BOOL_AND"
    "BOOL_OR"
    "BOOL_LT"
    "BOOL_GT"
    "BOOL_EQUAL"
    "BOOL_NOT_EQUAL"
)

unaryOperators = (
    "INTEGER_MINUS"
    "BOOL_NOT"
)


def p_expression_statement(p):
    '''PROGRAM : STATEMENT LINE_BREAK'''
    p[0] = AST.ProgramNode(p[1])


def p_programme_recursive(p):
    '''PROGRAM : STATEMENT LINE_BREAK PROGRAM'''
    p[0] = AST.ProgramNode([p[1]] + p[3].children)


def p_block(p):
    '''PROGRAM : BRACE_OPEN PROGRAM BRACE_CLOSE'''
    p[0] = p[2]

#  ____  _
# / ___|| |__   __ _ _ __   ___
# \___ \| '_ \ / _` | '_ \ / _ \
#  ___) | | | | (_| | |_) |  __/
# |____/|_| |_|\__,_| .__/ \___|
#                   |_|


def p_expression_shape(p):
    '''EXPRESSION : SQUAREBRACKET_OPEN SHAPE_TYPE DESCRIPTION ATTRIBUTES SQUAREBRACKET_CLOSE'''
    p[0] = AST.ShapeNode(p[2], p[4])


def p_shapetype(p):
    '''SHAPE_TYPE : CIRCLE
    | TRIANGLE
    | RECTANGLE'''
    p[0] = p[1]

#   ____      _
#  / ___|___ | | ___  _ __
# | |   / _ \| |/ _ \| '__|
# | |__| (_) | | (_) | |
#  \____\___/|_|\___/|_|


def p_colorvalue_colorhex(p):
    '''COLOR_VALUE : COLOR_HEX'''
    p[0] = p[1]


def p_colorvalue_red(p):
    '''COLOR_VALUE : RED'''
    p[0] = '#ff0000'


def p_colorvalue_green(p):
    '''COLOR_VALUE : GREEN'''
    p[0] = '#00ff00'


def p_colorvalue_blue(p):
    '''COLOR_VALUE : BLUE'''
    p[0] = '#0000ff'


def p_colorvalue_yellow(p):
    '''COLOR_VALUE : YELLOW'''
    p[0] = '#ffff00'


def p_colorvalue_black(p):
    '''COLOR_VALUE : BLACK'''
    p[0] = '#000000'


def p_colorvalue_white(p):
    '''COLOR_VALUE : WHITE'''
    p[0] = '#ffffff'

#     _   _   _        _ _           _
#    / \ | |_| |_ _ __(_) |__  _   _| |_ ___
#   / _ \| __| __| '__| | '_ \| | | | __/ _ \
#  / ___ \ |_| |_| |  | | |_) | |_| | ||  __/
# /_/   \_\__|\__|_|  |_|_.__/ \__,_|\__\___|


def p_attribute(p):
    '''ATTRIBUTES : ATTRIBUTE'''
    p[0] = [p[1]]


def p_attributes(p):
    '''ATTRIBUTES : ATTRIBUTE SEPARATOR ATTRIBUTES'''
    p[0] = [p[1]] + p[3]


def p_attribute_radius(p):
    '''ATTRIBUTE : RADIUS AFFECTATION EXPRESSION'''
    p[0] = AST.RadiusNode(p[3])


def p_attribute_positionX(p):
    '''ATTRIBUTE : POSITIONX AFFECTATION EXPRESSION'''
    p[0] = AST.PositionXNode(p[3])


def p_attribute_positionY(p):
    '''ATTRIBUTE : POSITIONY AFFECTATION EXPRESSION'''
    p[0] = AST.PositionYNode(p[3])


def p_attribute_color(p):
    '''ATTRIBUTE : COLOR AFFECTATION COLOR_VALUE'''
    p[0] = AST.ColorNode(p[3])


def p_attribute_width(p):
    '''ATTRIBUTE : WIDTH AFFECTATION EXPRESSION'''
    p[0] = AST.WidthNode(p[3])


def p_attribute_height(p):
    '''ATTRIBUTE : HEIGHT AFFECTATION EXPRESSION'''
    p[0] = AST.HeightNode(p[3])

#  ____  _        _                            _
# / ___|| |_ __ _| |_ ___ _ __ ___   ___ _ __ | |_
# \___ \| __/ _` | __/ _ \ '_ ` _ \ / _ \ '_ \| __|
#  ___) | || (_| | ||  __/ | | | | |  __/ | | | |_
# |____/ \__\__,_|\__\___|_| |_| |_|\___|_| |_|\__|


def p_statement_draw(p):
    '''STATEMENT : DRAW EXPRESSION'''
    p[0] = AST.DrawNode(p[2])


def p_statement_structure(p):
    '''STATEMENT : IF_STATEMENTS
    | WHILE_STATEMENT'''

#  _____                              _
# | ____|_  ___ __  _ __ ___  ___ ___(_) ___  _ __
# |  _| \ \/ / '_ \| '__/ _ \/ __/ __| |/ _ \| '_ \
# | |___ >  <| |_) | | |  __/\__ \__ \ | (_) | | | |
# |_____/_/\_\ .__/|_|  \___||___/___/_|\___/|_| |_|
#            |_|


def p_int_expression_number(p):
    '''EXPRESSION : VARIABLE_NAME'''
    p[0] = AST.VariableNode(p[1])


def p_expression_unaryOperation(p):
    '''EXPRESSION : INTEGER_MINUS EXPRESSION %prec UNARYNUMBER
    | BOOL_NOT EXPRESSION %prec UNARYBOOL'''
    p[0] = AST.UnaryOperation(p[1], [p[2]])


def p_expression_binaryOperation(p):
    '''EXPRESSION : EXPRESSION INTEGER_DIVIDE EXPRESSION
    | EXPRESSION INTEGER_TIMES EXPRESSION
    | EXPRESSION INTEGER_MINUS EXPRESSION
    | EXPRESSION INTEGER_PLUS EXPRESSION
    | EXPRESSION BOOL_EQUAL EXPRESSION
    | EXPRESSION BOOL_NOT_EQUAL EXPRESSION
    | EXPRESSION BOOL_AND EXPRESSION
    | EXPRESSION BOOL_OR EXPRESSION
    | EXPRESSION BOOL_LT EXPRESSION
    | EXPRESSION BOOL_GT EXPRESSION'''
    p[0] = AST.BinaryOperation(p[2], [p[1], p[3]])


def p_expression_bracket(p):
    '''EXPRESSION : BRACKET_OPEN EXPRESSION BRACKET_CLOSE'''
    p[0] = p[2]


def p_expression_number(p):
    '''EXPRESSION : NUMBER'''
    p[0] = AST.TokenNode(p[1])  # already converted in int in lexemes.py


def p_expression_true(p):
    '''EXPRESSION : TRUE'''
    p[0] = AST.TokenNode(True)


def p_expression_false(p):
    '''EXPRESSION : FALSE'''
    p[0] = AST.TokenNode(False)


# __     __         _       _     _
# \ \   / /_ _ _ __(_) __ _| |__ | | ___  ___
#  \ \ / / _` | '__| |/ _` | '_ \| |/ _ \/ __|
#   \ V / (_| | |  | | (_| | |_) | |  __/\__ \
#    \_/ \__,_|_|  |_|\__,_|_.__/|_|\___||___/


def p_statement_declaration(p):
    '''STATEMENT : BOOLEAN VARIABLE_NAME
    | INTEGER VARIABLE_NAME
    | SHAPE VARIABLE_NAME'''
    p[0] = AST.DeclarationNode(p[1], p[2])


def p_statement_affetation(p):
    '''STATEMENT : VARIABLE_NAME AFFECTATION EXPRESSION'''
    p[0] = AST.AffectationNode(p[1], p[3])


def p_statement_affetation_declaration(p):
    '''STATEMENT : BOOLEAN VARIABLE_NAME AFFECTATION EXPRESSION
    | INTEGER VARIABLE_NAME AFFECTATION EXPRESSION
    | SHAPE VARIABLE_NAME AFFECTATION EXPRESSION'''
    declaration = AST.DeclarationNode(p[1], p[2])
    affectation = AST.AffectationNode(p[2], p[4])
    # micro program for the shorthand
    p[0] = AST.ProgramNode([declaration, affectation])


def p_temp(p):
    '''STATEMENT : EXPRESSION'''
    p[0] = p[1]

#  ____  _                   _
# / ___|| |_ _ __ _   _  ___| |_ _   _ _ __ ___
# \___ \| __| '__| | | |/ __| __| | | | '__/ _ \
#  ___) | |_| |  | |_| | (__| |_| |_| | | |  __/
# |____/ \__|_|   \__,_|\___|\__|\__,_|_|  \___|


def p_ifs(p):
    '''IF_STATEMENTS : IF_STATEMENT
    | IF_STATEMENT ELSE_STATEMENT
    | IF_STATEMENT ELSE_IF_STATEMENTS
    | IF_STATEMENT ELSE_IF_STATEMENTS ELSE_STATEMENT'''


def p_if(p):
    '''IF_STATEMENT : IF BRACKET_OPEN EXPRESSION BRACKET_CLOSE PROGRAM'''


def p_elseifs(p):
    '''ELSE_IF_STATEMENTS : ELSE_IF_STATEMENT
    | ELSE_IF_STATEMENTS ELSE_IF_STATEMENT'''


def p_elseif(p):
    '''ELSE_IF_STATEMENT : ELSEIF BRACKET_OPEN EXPRESSION BRACKET_CLOSE PROGRAM'''


def p_else(p):
    '''ELSE_STATEMENT : ELSE PROGRAM'''


def p_while(p):
    '''WHILE_STATEMENT : WHILE BRACKET_OPEN EXPRESSION BRACKET_CLOSE PROGRAM'''


def p_error(p):
    print(p)
    print("Syntax error in line %d" % p.lineno)
    yacc.yacc().errok()


def parse(program):
    return yacc.parse(program, debug=False)


if __name__ == '__main__':
    import sys
    import os

    yacc.yacc(outputdir='./generated')

    prog = open(sys.argv[1]).read()
    result = parse(prog)
    print(result)
    graph = result.makegraphicaltree()
    name = os.path.splitext(sys.argv[1])[0] + '-ast.pdf'
    graph.write_pdf(name)
