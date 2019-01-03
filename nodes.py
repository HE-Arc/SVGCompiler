from AST import Node

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

class UndeclaredVariableException(Exception):
    pass

class InvalidAffectationTypeException(Exception):
    pass

class AffectationNode(Node):
    def __init__(self, tokenVariableName, value):
        variableName = tokenVariableName.variableName
        if variableName not in variablesTypes.keys():
            raise UndeclaredVariableException(f'Variable \'{variableName}\' not declared')

        valueType = value.getOperationType()
        variableType = variablesTypes[variableName]
        print(valueType, variableType)
        if valueType != variableType:
            raise InvalidAffectationTypeException(f'Variable \'{variableName}\' is of type \'{variableType}\' instead of \'{valueType}\'')

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


class DrawNode(Node):
    type = "draw"


#     _   _   _        _ _           _
#    / \ | |_| |_ _ __(_) |__  _   _| |_ ___
#   / _ \| __| __| "__| | "_ \| | | | __/ _ \
#  / ___ \ |_| |_| |  | | |_) | |_| | ||  __/
# /_/   \_\__|\__|_|  |_|_.__/ \__,_|\__\___|


class ColorNode(Node):
    def __init__(self, value):
        Node.__init__(self, [value])

    def __repr__(self):
        return "Color"


class RadiusNode(Node):
    def __init__(self, value):
        Node.__init__(self, [value])

    def __repr__(self):
        return "Radius"


class PositionXNode(Node):
    def __init__(self, value):
        Node.__init__(self, [value])

    def __repr__(self):
        return "PositionX"


class PositionYNode(Node):
    def __init__(self, value):
        Node.__init__(self, [value])

    def __repr__(self):
        return "PositionY "


class WidthNode(Node):
    def __init__(self, value):
        Node.__init__(self, [value])

    def __repr__(self):
        return "Width"


class HeightNode(Node):
    def __init__(self, value):
        Node.__init__(self[value])

    def __repr__(self):
        return "Height"


#   ___                       _   _
#  / _ \ _ __   ___ _ __ __ _| |_(_) ___  _ __  ___
# | | | | '_ \ / _ \ '__/ _` | __| |/ _ \| '_ \/ __|
# | |_| | |_) |  __/ | | (_| | |_| | (_) | | | \__ \
#  \___/| .__/ \___|_|  \__,_|\__|_|\___/|_| |_|___/
#       |_|


class UnaryOperation(Node):
    operationTable = {
        '!': (TypeBooleanNode, [TypeBooleanNode]),
        '-': (TypeIntegerNode, [TypeIntegerNode]),
    }

    def __init__(self, operation, operande):
        Node.__init__(self, operande)
        self.operande = operande
        self.operation = operation

    def __repr__(self):
        return "UnaryOp : " + self.operation


class InvalidOperandeException(Exception):
    pass

class BinaryOperation(Node):
    operationTable = {
        '+': (TypeIntegerNode, [(TypeIntegerNode, TypeIntegerNode)]),
        '-': (TypeIntegerNode, [(TypeIntegerNode, TypeIntegerNode)]),
        '*': (TypeIntegerNode, [(TypeIntegerNode, TypeIntegerNode)]),
        '/': (TypeIntegerNode, [(TypeIntegerNode, TypeIntegerNode)]),
        '==': (TypeBooleanNode, [(TypeIntegerNode, TypeIntegerNode), (TypeBooleanNode, TypeBooleanNode)]),
        '!=': (TypeBooleanNode, [(TypeIntegerNode, TypeIntegerNode), (TypeBooleanNode, TypeBooleanNode)]),
        '&&': (TypeBooleanNode, [(TypeBooleanNode, TypeBooleanNode)]),
        '||': (TypeBooleanNode, [(TypeBooleanNode, TypeBooleanNode)]),
        '<': (TypeBooleanNode, [(TypeIntegerNode, TypeIntegerNode)]),
        '>': (TypeBooleanNode, [(TypeIntegerNode, TypeIntegerNode)]),
    }

    def __init__(self, operation, operandes):
        Node.__init__(self, operandes)
        self.operandes = operandes
        self.operation = operation

        constraints = BinaryOperation.operationTable[self.operation][1]
        op = self.getOperandeType()
        if op not in constraints:
            raise InvalidOperandeException(f'For binary operation \'{self.operation}\' use \'{constraints}\' instead of \'{op}\'')

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
    def __init__(self, conditionProgram, trueProgram=None, falseProgram=None):
        l = [conditionProgram]
        self.conditionProgram = conditionProgram
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
    def __init__(self, conditionProgram, trueProgram):
        Node.__init__(self, [conditionProgram, trueProgram])

    def __repr__(self):
        return "Loop"
