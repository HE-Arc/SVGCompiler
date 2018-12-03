import ply.yacc as yacc
from lexemes import tokens
import AST

precedence = (
)

def p_expression_statement(p):
	'''program : statement'''

def p_programme_revursive(p):
	'''program : statement LINE_BREAK program'''

def p_statement_affetation(p):
	'''VARIABLE_NAME AFFECTATION NUMBER'''

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