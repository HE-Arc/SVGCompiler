import ply.yacc as yacc
from lexemes import tokens
import AST

precedence = (
    ('left', 'INTEGER_MINUS'),
    ('left', 'INTEGER_PLUS'),
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

def p_expression_statement(p):
    '''PROGRAM : STATEMENT'''
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


def p_value_shape(p):
    '''ABSTRACT_SHAPE : SQUAREBRACKET_OPEN SHAPE_CONTENT SQUAREBRACKET_CLOSE'''
    p[0] = p[2]


def p_shape_content(p):
    '''SHAPE_CONTENT : CIRCLE_CONTENT
    | TRIANGLE_CONTENT
    | RECTANGLE_CONTENT'''
    p[0] = p[1]


def p_circle_content(p):
    '''CIRCLE_CONTENT : CIRCLE DESCRIPTION ATTRIBUTES'''
    p[0] = AST.CircleNode(p[3])


def p_triangle_content(p):
    '''TRIANGLE_CONTENT : TRIANGLE DESCRIPTION ATTRIBUTES'''
    p[0] = AST.TriangleNode(p[3])


def p_rectangle_content(p):
    '''RECTANGLE_CONTENT : RECTANGLE DESCRIPTION ATTRIBUTES'''
    p[0] = AST.RectangleNode(p[3])

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
    '''ATTRIBUTE : RADIUS AFFECTATION NUMBER'''
    p[0] = AST.RadiusNode(p[3])

def p_attribute_positionX(p):
    '''ATTRIBUTE : POSITIONX AFFECTATION NUMBER'''
    p[0] = AST.PositionXNode(p[3])


def p_attribute_positionY(p):
    '''ATTRIBUTE : POSITIONY AFFECTATION NUMBER'''
    p[0] = AST.PositionYNode(p[3])


def p_attribute_color(p):
    '''ATTRIBUTE : COLOR AFFECTATION COLOR_VALUE'''
    p[0] = AST.ColorNode(p[3])


def p_attribute_width(p):
    '''ATTRIBUTE : WIDTH AFFECTATION NUMBER'''
    p[0] = AST.WidthNode(p[3])


def p_attribute_height(p):
    '''ATTRIBUTE : HEIGHT AFFECTATION NUMBER'''
    p[0] = AST.HeightNode(p[3])

# __     __         _       _     _
# \ \   / /_ _ _ __(_) __ _| |__ | | ___  ___
#  \ \ / / _` | '__| |/ _` | '_ \| |/ _ \/ __|
#   \ V / (_| | |  | | (_| | |_) | |  __/\__ \
#    \_/ \__,_|_|  |_|\__,_|_.__/|_|\___||___/


def p_declaration_boolean(p):
    '''VARIABLE : BOOLEAN VARIABLE_NAME'''
    p[0] = AST.DeclarationNode(p[1], p[2])


def p_declaration_integer(p):
    '''VARIABLE : INTEGER VARIABLE_NAME'''
    p[0] = AST.DeclarationNode(p[1], p[2])


def p_declaration_shape(p):
    '''VARIABLE : SHAPE VARIABLE_NAME'''
    p[0] = AST.DeclarationNode(p[1], p[2])


def p_value_number_boolean(p):
    '''VALUE : ABSTRACT_SHAPE
    | INT_EXPRESSION
    | BOOL_EXPRESSION'''
    p[0] = p[1]

#  ____  _        _                            _
# / ___|| |_ __ _| |_ ___ _ __ ___   ___ _ __ | |_
# \___ \| __/ _` | __/ _ \ '_ ` _ \ / _ \ '_ \| __|
#  ___) | || (_| | ||  __/ | | | | |  __/ | | | |_
# |____/ \__\__,_|\__\___|_| |_| |_|\___|_| |_|\__|

# def p_statement_affetation(p):
#     '''STATEMENT : VARIABLE AFFECTATION VALUE'''
#     p[0] = AST.AffectationNode(p[1], p[3])

def p_statement_draw(p):
    '''STATEMENT : DRAW ABSTRACT_SHAPE'''
    p[0] = AST.DrawNode(p[2])


def p_statement_structure(p):
    '''STATEMENT : IF_STATEMENTS
    | WHILE_STATEMENT'''

#  ___       _          _         _ _   _                    _   _
# |_ _|_ __ | |_       / \   _ __(_) |_| |__  _ __ ___   ___| |_(_) ___
#  | || '_ \| __|     / _ \ | '__| | __| '_ \| '_ ` _ \ / _ \ __| |/ __|
#  | || | | | |_     / ___ \| |  | | |_| | | | | | | | |  __/ |_| | (__
# |___|_| |_|\__|___/_/   \_\_|  |_|\__|_| |_|_| |_| |_|\___|\__|_|\___|
#              |_____|


def p_int_expression_unary(p):
    'INT_EXPRESSION : INTEGER_MINUS INT_EXPRESSION %prec UNARYNUMBER'
    p[0] = AST.OpNode(p[1], [p[2]])


def p_int_expression_bracket(p):
    'INT_EXPRESSION : BRACKET_OPEN INT_EXPRESSION BRACKET_CLOSE'
    p[0] = p[2]


def p_int_expression_number(p):
    '''INT_EXPRESSION : NUMBER
    | VARIABLE'''
    if p[1] is AST.IntegerNode:
        p[0] = p[1]
    else:
        raise Exception("Invalide type")


def p_int_expression_op(p):
    '''INT_EXPRESSION : INT_EXPRESSION INTEGER_PLUS INT_EXPRESSION
    | INT_EXPRESSION INTEGER_MINUS INT_EXPRESSION
    | INT_EXPRESSION INTEGER_TIMES INT_EXPRESSION
    | INT_EXPRESSION INTEGER_DIVIDE INT_EXPRESSION'''
    p[0] = AST.OpNode(p[2], [p[1], p[3]])


def p_int_bool_expression_op(p):
    '''BOOL_EXPRESSION : INT_EXPRESSION BOOL_LT INT_EXPRESSION
    | INT_EXPRESSION BOOL_GT INT_EXPRESSION
    | INT_EXPRESSION BOOL_EQUAL INT_EXPRESSION
    | INT_EXPRESSION BOOL_NOT_EQUAL INT_EXPRESSION'''
    p[0] = AST.OpNode(p[2], [p[1], p[3]])

#  ____              _        _         _ _   _                    _   _
# | __ )  ___   ___ | |      / \   _ __(_) |_| |__  _ __ ___   ___| |_(_) ___
# |  _ \ / _ \ / _ \| |     / _ \ | '__| | __| '_ \| '_ ` _ \ / _ \ __| |/ __|
# | |_) | (_) | (_) | |    / ___ \| |  | | |_| | | | | | | | |  __/ |_| | (__
# |____/ \___/ \___/|_|___/_/   \_\_|  |_|\__|_| |_|_| |_| |_|\___|\__|_|\___|
#                    |_____|


def p_bool_expression_unary(p):
    'BOOL_EXPRESSION : BOOL_NOT BOOL_EXPRESSION %prec UNARYBOOL'
    p[0] = AST.OpNode(p[1], [p[2]])


def p_bool_expression_bracket(p):
    'BOOL_EXPRESSION : BRACKET_OPEN BOOL_EXPRESSION BRACKET_CLOSE'
    p[0] = p[2]


def p_bool_value(p):
    '''BOOL_VALUE : TRUE
    | FALSE'''
    p[0] = AST.BooleanNode(p[1])


def p_bool_expression_number(p):
    '''BOOL_EXPRESSION : BOOL_VALUE
    | VARIABLE'''
    if p[1] is AST.BooleanNode:
        p[0] = p[1]
    else:
        raise Exception("Invalide type")


def p_bool_expression_op(p):
    '''BOOL_EXPRESSION : BOOL_EXPRESSION BOOL_EQUAL BOOL_EXPRESSION
    | BOOL_EXPRESSION BOOL_NOT_EQUAL BOOL_EXPRESSION
    | BOOL_EXPRESSION BOOL_AND BOOL_EXPRESSION
    | BOOL_EXPRESSION BOOL_OR BOOL_EXPRESSION'''
    p[0] = AST.OpNode(p[2], [p[1], p[3]])

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
    '''IF_STATEMENT : IF BRACKET_OPEN BOOL_EXPRESSION BRACKET_CLOSE PROGRAM'''


def p_elseifs(p):
    '''ELSE_IF_STATEMENTS : ELSE_IF_STATEMENT
    | ELSE_IF_STATEMENTS ELSE_IF_STATEMENT'''


def p_elseif(p):
    '''ELSE_IF_STATEMENT : ELSEIF BRACKET_OPEN BOOL_EXPRESSION BRACKET_CLOSE PROGRAM'''


def p_else(p):
    '''ELSE_STATEMENT : ELSE PROGRAM'''


def p_while(p):
    '''WHILE_STATEMENT : WHILE BRACKET_OPEN BOOL_EXPRESSION BRACKET_CLOSE PROGRAM'''

yacc.yacc(outputdir='.')


def parse(program):
    return yacc.parse(program, debug=False)


if __name__ == '__main__':
    import sys
    import os

    prog = open(sys.argv[1]).read()
    result = parse(prog)
    print(result)
    # graph = result.makegraphicaltree()
    # name = os.path.splitext(sys.argv[1])[0] + '-ast.pdf'
    # graph.write_pdf(name)
