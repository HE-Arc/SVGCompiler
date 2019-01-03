from AST import Node


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


class TokenNumberNode(Node):
    type = "Token Number"

    def __init__(self, value):
        Node.__init__(self)
        self.value = value

    def __repr__(self):
        return Node.__repr__(self) + " : " + str(self.value)


class TokenBooleanNode(Node):
    type = "Token Boolean"

    def __init__(self, value):
        Node.__init__(self)
        self.value = value

    def __repr__(self):
        return Node.__repr__(self) + " : " + str(self.value)

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
    def __init__(self, variableType, variableName):
        Node.__init__(self, [variableType, variableName])

    def __repr__(self):
        return "Declaration"


class AffectationNode(Node):
    def __init__(self, variableName, value):
        Node.__init__(self, [variableName, value])

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
        Node.__init__(self [value])

    def __repr__(self):
        return "Height"


#   ___                       _   _
#  / _ \ _ __   ___ _ __ __ _| |_(_) ___  _ __  ___
# | | | | '_ \ / _ \ '__/ _` | __| |/ _ \| '_ \/ __|
# | |_| | |_) |  __/ | | (_| | |_| | (_) | | | \__ \
#  \___/| .__/ \___|_|  \__,_|\__|_|\___/|_| |_|___/
#       |_|


class UnaryOperation(Node):
    def __init__(self, operation, operande):
        Node.__init__(self, operande)
        self.operation = operation

    def __repr__(self):
        return "UnaryOp : " + self.operation


class BinaryOperation(Node):
    def __init__(self, operation, operande):
        Node.__init__(self, operande)
        self.operation = operation

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
