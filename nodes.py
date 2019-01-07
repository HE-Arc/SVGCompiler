from AST import Node

# variable used to determinate if a variable have the right type while creating the tree
variablesTypes = dict()


class ProgramNode(Node):
    type = "Program"


class BlockNode(Node):
    type = "Block"

    def __init__(self, content, name=None):
        Node.__init__(self, content)
        self.name = name

    def __repr__(self):
        repr = self.type
        if self.name != None:
            repr = self.type + " : " + self.name
        return repr


#  _____     _
# |_   _|__ | | _____ _ __
#   | |/ _ \| |/ / _ \ '_ \
#   | | (_) |   <  __/ | | |
#   |_|\___/|_|\_\___|_| |_|

class TokenVariableNameNode(Node):
    type = "Token VariableName"

    def __init__(self, variableName):
        Node.__init__(self)
        self.variableName = variableName

    def __repr__(self):
        return Node.__repr__(self) + " : " + str(self.variableName)

    def __copy__(self):
        return TokenVariableNameNode(self.variableName)

    def getOperationType(self):
        return variablesTypes[self.variableName]


class TokenNumberNode(Node):
    type = "Token Number"

    def __init__(self, value):
        Node.__init__(self)
        self.value = value

    def __repr__(self):
        return Node.__repr__(self) + " : " + str(self.value)

    def getOperationType(self):
        return TypeIntegerNode


class TokenBooleanNode(Node):
    type = "Token Boolean"

    def __init__(self, value):
        Node.__init__(self)
        self.value = value

    def __repr__(self):
        return Node.__repr__(self) + " : " + str(self.value)

    def getOperationType(self):
        return TypeBooleanNode


class TokenColorNode(Node):
    type = "Token Color"

    def __init__(self, value):
        Node.__init__(self)
        self.value = value

    def __repr__(self):
        return Node.__repr__(self) + " : " + str(self.value)

# __     __         _       _     _
# \ \   / /_ _ _ __(_) __ _| |__ | | ___  ___
#  \ \ / / _` | '__| |/ _` | '_ \| |/ _ \/ __|
#   \ V / (_| | |  | | (_| | |_) | |  __/\__ \
#    \_/ \__,_|_|  |_|\__,_|_.__/|_|\___||___/


class TypeBooleanNode(Node):
    type = "Type Boolean"


class TypeIntegerNode(Node):
    type = "Type Integer"


class TypeShapeNode(Node):
    type = "Type Shape"


class DeclarationNode(Node):
    def __init__(self, variableType, tokenVariableName):
        Node.__init__(self, [variableType, tokenVariableName])
        variablesTypes[tokenVariableName.variableName] = type(variableType)

    def __repr__(self):
        return "Declaration"


class AffectationNode(Node):
    def __init__(self, tokenVariableName, value, lineno=0):
        variableName = tokenVariableName.variableName
        self.lineno = lineno
        if variableName not in variablesTypes.keys():
            print(
                f'UndeclaredVariableException at line {self.lineno} : Variable \'{variableName}\' not declared')
            exit()

        valueType = value.getOperationType()
        variableType = variablesTypes[variableName]
        if valueType != variableType:

            print(
                f'InvalidTypeException at line {self.lineno} : Variable \'{variableName}\' is of type \'{createErrorStringFromClassName(valueType)}\' instead of \'{createErrorStringFromClassName(variableType)}\'')
            exit()

        Node.__init__(self, [tokenVariableName, value])

    def __repr__(self):
        return "Affectation"


#  ____  _
# / ___|| |__   __ _ _ __   ___
# \___ \| "_ \ / _` | "_ \ / _ \
#  ___) | | | | (_| | |_) |  __/
# |____/|_| |_|\__,_| .__/ \___|
#                   |_|

class ShapeNode(Node):
    def __init__(self, shapetype, attr):
        Node.__init__(self, attr)
        self.shapetype = shapetype

    def __repr__(self):
        return self.shapetype

    def getOperationType(self):
        return TypeShapeNode


class DrawNode(Node):
    type = "draw"

    def __init__(self, value, lineno=0):
        valueType = value.getOperationType()
        self.lineno = lineno
        if valueType is not TypeShapeNode:
            print(
                f'InvalidTypeException at line {self.lineno} : Must be a shape to draw instead of {createErrorStringFromClassName(valueType)}')
            exit()

        Node.__init__(self, [value])


#     _   _   _        _ _           _
#    / \ | |_| |_ _ __(_) |__  _   _| |_ ___
#   / _ \| __| __| "__| | "_ \| | | | __/ _ \
#  / ___ \ |_| |_| |  | | |_) | |_| | ||  __/
# /_/   \_\__|\__|_|  |_|_.__/ \__,_|\__\___|

def createAttributeErrorStringFromClassName(className):
    return str(className).split("Node")[0].split(".")[-1]

class AttributeNode(Node):
    def __init__(self, values, lineno=0):
        self.lineno = lineno
        Node.__init__(self, values)

    def checkType(self, allowedType):
        valueType = self.value.getOperationType()
        if valueType not in allowedType:
            print(
                f'InvalidTypeException at line {self.lineno} : Must be a {createErrorStringFromClassName(allowedType[0])} for this attribute ({createAttributeErrorStringFromClassName(self.__class__)})')
            exit()


class ColorNode(AttributeNode):
    def __repr__(self):
        return "Color"


class RadiusNode(AttributeNode):
    def __init__(self, value,lineno=0):
        self.value = value
        AttributeNode.__init__(self, [value],lineno)
        self.checkType([TypeIntegerNode])

    def __repr__(self):
        return "Radius"


class PositionXNode(AttributeNode):
    def __init__(self, value,lineno=0):
        self.value = value
        AttributeNode.__init__(self, [value],lineno)
        self.checkType([TypeIntegerNode])

    def __repr__(self):
        return "PositionX"


class PositionYNode(AttributeNode):
    def __init__(self, value,lineno=0):
        self.value = value
        AttributeNode.__init__(self, [value],lineno)
        self.checkType([TypeIntegerNode])

    def __repr__(self):
        return "PositionY "


class WidthNode(AttributeNode):
    def __init__(self, value,lineno=0):
        self.value = value
        AttributeNode.__init__(self, [value],lineno)
        self.checkType([TypeIntegerNode])

    def __repr__(self):
        return "Width"


class HeightNode(AttributeNode):
    def __init__(self, value,lineno=0):
        self.value = value
        AttributeNode.__init__(self, [value],lineno)
        self.checkType([TypeIntegerNode])

    def __repr__(self):
        return "Height"


#   ___                       _   _
#  / _ \ _ __   ___ _ __ __ _| |_(_) ___  _ __  ___
# | | | | '_ \ / _ \ '__/ _` | __| |/ _ \| '_ \/ __|
# | |_| | |_) |  __/ | | (_| | |_| | (_) | | | \__ \
#  \___/| .__/ \___|_|  \__,_|\__|_|\___/|_| |_|___/
#       |_|

'''
Input: a list of tuples for a binary operation, a single object for unary operation
Output: a formatted string of types
This method is used for the errors
'''


def createErrorStringFromClassName(className):
    if type(className) is list:
        return " or ".join(map(lambda tup: "/".join(map(lambda x: x().type.split(" ")[-1], tup)), className))
    else:
        return className().type.split(" ")[-1]


class UnaryOperation(Node):
    operationTable = {
        '!': (TypeBooleanNode, [TypeBooleanNode]),
        '-': (TypeIntegerNode, [TypeIntegerNode]),
    }

    def __init__(self, operation, operande,lineno=0):
        Node.__init__(self, operande)
        self.operande = operande
        self.operation = operation
        self.lineno=lineno

        constraints = UnaryOperation.operationTable[self.operation][1]
        op = self.getOperandeType()
        if op not in constraints:
            print(
                f'InvalidOperandeException at line {self.lineno} : For unary operation \'{self.operation}\' use \'{createErrorStringFromClassName(constraints[0])}\' instead of \'{createErrorStringFromClassName(op)}\'')
            exit()

    def getOperandeType(self):
        op = self.operande[0].getOperationType()
        return op

    def getOperationType(self):
        operationLine = BinaryOperation.operationTable[self.operation]
        return operationLine[0]

    def __repr__(self):
        return "UnaryOp : " + self.operation


class BinaryOperation(Node):
    operationTable = {
        '+': (TypeIntegerNode, [(TypeIntegerNode, TypeIntegerNode)]),
        '-': (TypeIntegerNode, [(TypeIntegerNode, TypeIntegerNode)]),
        '*': (TypeIntegerNode, [(TypeIntegerNode, TypeIntegerNode)]),
        '/': (TypeIntegerNode, [(TypeIntegerNode, TypeIntegerNode)]),
        '%': (TypeIntegerNode, [(TypeIntegerNode, TypeIntegerNode)]),
        '~': (TypeIntegerNode, [(TypeIntegerNode, TypeIntegerNode)]),
        '==': (TypeBooleanNode, [(TypeIntegerNode, TypeIntegerNode), (TypeBooleanNode, TypeBooleanNode)]),
        '!=': (TypeBooleanNode, [(TypeIntegerNode, TypeIntegerNode), (TypeBooleanNode, TypeBooleanNode)]),
        '&&': (TypeBooleanNode, [(TypeBooleanNode, TypeBooleanNode)]),
        '||': (TypeBooleanNode, [(TypeBooleanNode, TypeBooleanNode)]),
        '<': (TypeBooleanNode, [(TypeIntegerNode, TypeIntegerNode)]),
        '>': (TypeBooleanNode, [(TypeIntegerNode, TypeIntegerNode)]),
    }

    def __init__(self, operation, operandes, lineno):
        Node.__init__(self, operandes)
        self.operandes = operandes
        self.operation = operation
        self.lineno = lineno

        constraints = BinaryOperation.operationTable[self.operation][1]
        op = self.getOperandeType()
        if op not in constraints:
            print(
                f'InvalidOperandeException at line {self.lineno} : For binary operation \'{self.operation}\' use \'{createErrorStringFromClassName(constraints)}\' instead of \'{createErrorStringFromClassName([op])}\'')
            exit()

    def getOperandeType(self):
        op1 = self.operandes[0].getOperationType()
        op2 = self.operandes[1].getOperationType()
        return (op1, op2)

    def getOperationType(self):
        operationLine = BinaryOperation.operationTable[self.operation]
        return operationLine[0]

    def __repr__(self):
        return "BinaryOp : " + self.operation

#  ____  _                   _
# / ___|| |_ _ __ _   _  ___| |_ _   _ _ __ ___  ___
# \___ \| __| '__| | | |/ __| __| | | | '__/ _ \/ __|
#  ___) | |_| |  | |_| | (__| |_| |_| | | |  __/\__ \
# |____/ \__|_|   \__,_|\___|\__|\__,_|_|  \___||___/


class IfNode(Node):
    def __init__(self, conditionProgram, trueProgram=None, falseProgram=None, lineno=0):
        self.evaluated = False
        self.lineno = lineno
        l = [conditionProgram]
        self.conditionProgram = conditionProgram
        conditionProgramType = self.conditionProgram.getOperationType()
        if conditionProgramType is not TypeBooleanNode:
            print(
                f"NotBooleanException at line {self.lineno} : Must be a boolean for a If")
            exit()

        self.trueProgram = trueProgram
        self.falseProgram = falseProgram
        if trueProgram != None:
            l.append(trueProgram)

        if falseProgram != None:
            l.append(falseProgram)
        Node.__init__(self, l)

    def __repr__(self):
        return "If"


class LoopNode(Node):
    def __init__(self, conditionProgram, trueProgram, lineno=0):
        self.lineno = lineno
        self.conditionProgram = conditionProgram
        Node.__init__(self, [conditionProgram, trueProgram])
        conditionProgramType = self.conditionProgram.getOperationType()
        if conditionProgramType is not TypeBooleanNode:
            print(
                f"NotBooleanException at line {self.lineno} : Must be a boolean for a Loop")
            exit()

    def __repr__(self):
        return "Loop"
