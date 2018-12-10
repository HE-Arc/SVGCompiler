import ply.yacc as yacc
from lexemes import tokens
import AST

precedence = (
)

def p_expression_statement(p):
	'''PROGRAM : STATEMENT'''

def p_programme_revursive(p):
	'''PROGRAM : STATEMENT LINE_BREAK PROGRAM'''

def p_value_number_boolean(p):
	'''VALUE : ABSTRACT_SHAPE
	| NUMBER
	| TRUE
	| FALSE'''

#  ____  _
# / ___|| |__   __ _ _ __   ___
# \___ \| '_ \ / _` | '_ \ / _ \
#  ___) | | | | (_| | |_) |  __/
# |____/|_| |_|\__,_| .__/ \___|
#                   |_|

def p_value_shape(p):
	'''ABSTRACT_SHAPE : SQUAREBRACKET_OPEN SHAPECONTENT SQUAREBRACKET_CLOSE'''

def p_shape_content(p):
	'''SHAPECONTENT : CIRCLECONTENT
	| TRIANGLECONTENT
	| RECTANGLECONTENT'''

def p_circle_content(p):
	'''CIRCLECONTENT : CIRCLE DESCRIPTION ATTRIBUTES'''

def p_triangle_content(p):
	'''TRIANGLECONTENT : TRIANGLE DESCRIPTION ATTRIBUTES'''

def p_rectangle_content(p):
	'''RECTANGLECONTENT : RECTANGLE DESCRIPTION ATTRIBUTES'''

#   ____      _
#  / ___|___ | | ___  _ __
# | |   / _ \| |/ _ \| '__|
# | |__| (_) | | (_) | |
#  \____\___/|_|\___/|_|

def p_colorvalue_colorhex(p):
	'''COLOR_VALUE : COLOR_HEX'''

def p_colorvalue_red(p):
	'''COLOR_VALUE : RED'''

def p_colorvalue_green(p):
	'''COLOR_VALUE : GREEN'''

def p_colorvalue_blue(p):
	'''COLOR_VALUE : BLUE'''

def p_colorvalue_yellow(p):
	'''COLOR_VALUE : YELLOW'''

def p_colorvalue_black(p):
	'''COLOR_VALUE : BLACK'''

def p_colorvalue_white(p):
	'''COLOR_VALUE : WHITE'''

#     _   _   _        _ _           _
#    / \ | |_| |_ _ __(_) |__  _   _| |_ ___
#   / _ \| __| __| '__| | '_ \| | | | __/ _ \
#  / ___ \ |_| |_| |  | | |_) | |_| | ||  __/
# /_/   \_\__|\__|_|  |_|_.__/ \__,_|\__\___|


def p_attribute(p):
	'''ATTRIBUTES : ATTRIBUTE SEPARATOR ATTRIBUTES
	| ATTRIBUTE'''

def p_attribute_radius(p):
	'''ATTRIBUTE : RADIUS AFFECTATION NUMBER'''

def p_attribute_positionX(p):
	'''ATTRIBUTE : POSITIONX AFFECTATION NUMBER'''

def p_attribute_positionY(p):
	'''ATTRIBUTE : POSITIONY AFFECTATION NUMBER'''

def p_attribute_color(p):
	'''ATTRIBUTE : COLOR AFFECTATION COLOR_VALUE'''

def p_attribute_width(p):
	'''ATTRIBUTE : WIDTH AFFECTATION NUMBER'''

def p_attribute_height(p):
	'''ATTRIBUTE : HEIGHT AFFECTATION NUMBER'''

# __     __         _       _     _
# \ \   / /_ _ _ __(_) __ _| |__ | | ___  ___
#  \ \ / / _` | '__| |/ _` | '_ \| |/ _ \/ __|
#   \ V / (_| | |  | | (_| | |_) | |  __/\__ \
#    \_/ \__,_|_|  |_|\__,_|_.__/|_|\___||___/

def p_declaration_boolean(p):
	'''VARIABLE : BOOLEAN VARIABLE_NAME'''

def p_declaration_integer(p):
	'''VARIABLE : INTEGER VARIABLE_NAME'''

def p_declaration_shape(p):
	'''VARIABLE : SHAPE VARIABLE_NAME'''

def p_statement_affetation(p):
	'''STATEMENT : VARIABLE AFFECTATION VALUE'''

def p_statement_draw(p):
	'''STATEMENT : DRAW ABSTRACT_SHAPE'''

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