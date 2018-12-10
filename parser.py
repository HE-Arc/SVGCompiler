import ply.yacc as yacc
from lexemes import tokens
import AST

precedence = (
)

def p_expression_statement(p):
	'''program : statement'''

def p_programme_revursive(p):
	'''program : statement LINE_BREAK program'''

def p_value_number_boolean(p):
	'''VALUE : SHAPE | NUMBER | TRUE | FALSE'''

def p_value_shape(p):
	'''SHAPE : SQUAREBRACKET_OPEN SHAPECONTENT SQUAREBRACKET_CLOSE'''

def p_shape_content(p):
	'''SHAPECONTENT : CIRCLECONTENT | TRIANGLECONTENT | RECTANGLECONTENT'''

def p_circle_content(p):
	'''CIRCLECONTENT : '''

def p_triangle_content(p):
	'''TRIANGLECONTENT : '''

def p_rectangle_content(p):
	'''RECTANGLECONTENT : '''

def p_declaration_boolean(p):
	'''VARIABLE : BOOLEAN VARIABLE_NAME'''


def p_declaration_integer(p):
	'''VARIABLE : INTEGER VARIABLE_NAME'''


def p_declaration_shape(p):
	'''VARIABLE : SHAPE VARIABLE_NAME'''


def p_statement_affetation(p):
	'''VARIABLE : VARIABLE AFFECTATION VALUE'''

def p_error(p):
	print("Syntax error in line %d" % p.lineno)
	yacc.errok()

yacc.yacc(outputdir='.')

def parse(program):
	return yacc.parse(program)

if __name__ == '__main__':
	import sys
	import os

	prog = open(sys.argv[1]).read()
	result = parse(prog)
	print(result)