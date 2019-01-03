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


class InvalidTypeException(Exception):
    pass


class AffectationNode(Node):
    def __init__(self, tokenVariableName, value):
        variableName = tokenVariableName.variableName
        if variableName not in variablesTypes.keys():
            raise UndeclaredVariableException(
                f'Variable \'{variableName}\' not declared')

        valueType = value.getOperationType()
        variableType = variablesTypes[variableName]
        if valueType != variableType:
            raise InvalidTypeException(
                f'Variable \'{variableName}\' is of type \'{variableType}\' instead of \'{valueType}\'')

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

    def __init__(self, value):
        valueType = value.getOperationType()
        if valueType is not TypeShapeNode:
            raise InvalidTypeException(
                f'Must be a shape to draw instead of {valueType}')

        Node.__init__(self, [value])


#     _   _   _        _ _           _
#    / \ | |_| |_ _ __(_) |__  _   _| |_ ___
#   / _ \| __| __| "__| | "_ \| | | | __/ _ \
#  / ___ \ |_| |_| |  | | |_) | |_| | ||  __/
# /_/   \_\__|\__|_|  |_|_.__/ \__,_|\__\___|

class AttributeNode(Node):
    def checkType(self, allowedType):
        valueType = self.value.getOperationType()
        if valueType not in allowedType:
            raise InvalidTypeException(
                f'Must be a {allowedType} for this attribute')


class ColorNode(AttributeNode):
    def __repr__(self):
        return "Color"


class RadiusNode(AttributeNode):
    def __init__(self, value):
        self.value = value
        self.checkType([TypeIntegerNode])
        Node.__init__(self, [value])

    def __repr__(self):
        return "Radius"


class PositionXNode(AttributeNode):
    def __init__(self, value):
        self.value = value
        self.checkType([TypeIntegerNode])
        Node.__init__(self, [value])

    def __repr__(self):
        return "PositionX"


class PositionYNode(AttributeNode):
    def __init__(self, value):
        self.value = value
        self.checkType([TypeIntegerNode])
        Node.__init__(self, [value])

    def __repr__(self):
        return "PositionY "


class WidthNode(AttributeNode):
    def __init__(self, value):
        self.value = value
        self.checkType([TypeIntegerNode])
        Node.__init__(self, [value])

    def __repr__(self):
        return "Width"


class HeightNode(AttributeNode):
    def __init__(self, value):
        self.value = value
        self.checkType([TypeIntegerNode])
        Node.__init__(self, [value])

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

        constraints = UnaryOperation.operationTable[self.operation][1]
        op = self.getOperandeType()
        if op not in constraints:
            raise InvalidOperandeException(
                f'For unary operation \'{self.operation}\' use \'{constraints}\' instead of \'{op}\'')

    def getOperandeType(self):
        op = self.operande[0].getOperationType()
        return op

    def getOperationType(self):
        operationLine = BinaryOperation.operationTable[self.operation]
        return operationLine[0]

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
            raise InvalidOperandeException(
                f'For binary operation \'{self.operation}\' use \'{constraints}\' instead of \'{op}\'')

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


class NotBooleanException(Exception):
    pass


class IfNode(Node):
    def __init__(self, conditionProgram, trueProgram=None, falseProgram=None):
        l = [conditionProgram]
        self.conditionProgram = conditionProgram
        conditionProgramType = self.conditionProgram.getOperationType()
        if conditionProgramType is not TypeBooleanNode:
            raise NotBooleanException("Must be a boolean for a If")

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
        self.conditionProgram = conditionProgram
        Node.__init__(self, [conditionProgram, trueProgram])
        conditionProgramType = self.conditionProgram.getOperationType()
        if conditionProgramType is not TypeBooleanNode:
            raise NotBooleanException("Must be a boolean for a Loop")

    def __repr__(self):
        return "Loop"
