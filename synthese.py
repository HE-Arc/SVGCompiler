#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from AST import addToClass
import AST
import nodes
from parser_ import parse  # we cant import a file named 'parser'... ?
import sys
import os
import random
from shapes import *
from threader import thread

binaryOperations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y,
    '%': lambda x, y: x % y,
    '==': lambda x, y: x == y,
    '!=': lambda x, y: x != y,
    '&&': lambda x, y: x and y,
    '||': lambda x, y: x or y,
    '<': lambda x, y: x < y,
    '>': lambda x, y: x > y,
    '~': lambda min, max: random.randint(min, max)
}

unaryOperations = {
    '!': lambda x: not x,
    '-': lambda x: -x
}

stack = []
vars = {}


def valueOfToken(t):
    if isinstance(t, str):
        try:
            return vars[t]
        except KeyError:
            return t
    return t


def synthese(node):
    shapeList = []
    while node:
        if node.__class__ in [AST.EntryNode, nodes.ProgramNode, nodes.BlockNode]:
            pass
        elif node.__class__ in [nodes.TokenNumberNode, nodes.TokenBooleanNode, nodes.TokenColorNode]:
            stack.append(node.value)
        elif node.__class__ == nodes.TokenVariableNameNode:
            stack.append(node.variableName)
        elif node.__class__ in [nodes.TypeBooleanNode, nodes.TypeIntegerNode, nodes.TypeShapeNode] or node.__class__.__bases__[-1] is nodes.AttributeNode:
            stack.append(node)
        elif node.__class__ == nodes.BinaryOperation:
            arg2 = valueOfToken(stack.pop())
            arg1 = valueOfToken(stack.pop())
            stack.append(binaryOperations[node.operation](arg1, arg2))
        elif node.__class__ == nodes.UnaryOperation:
            arg1 = valueOfToken(stack.pop())
            stack.append(unaryOperations[node.operation](arg1))
        elif node.__class__ == nodes.DeclarationNode:
            varName = stack.pop()
            # we don't need the type because it is checked in the semantic analysis but it is in the tree
            varType = stack.pop()
            vars[varName] = None
        elif node.__class__ == nodes.AffectationNode:
            varValue = stack.pop()
            varName = stack.pop()
            vars[varName] = varValue
        elif node.__class__ == nodes.LoopNode:
            cond = stack.pop()
            if cond:
                node = node.next[0]
            else:
                node = node.next[1]
            continue
        elif node.__class__ == nodes.ShapeNode:
            attrs = {}
            shapeType = node.shapetype
            # fetching attributes
            for child in node.children:
                attributeTypeNode = valueOfToken(stack.pop())
                attributeValueNode = valueOfToken(stack.pop())
                attrs[attributeTypeNode.__class__] = attributeValueNode

            # default values
            try:
                color = attrs[nodes.ColorNode]
            except KeyError:
                color = "#000000"

            try:
                posX = attrs[nodes.PositionXNode]
            except KeyError:
                posX = 0

            try:
                posY = attrs[nodes.PositionYNode]
            except KeyError:
                posY = 0

            if shapeType == 'circle':
                try:
                    radius = attrs[nodes.RadiusNode]
                except KeyError:
                    radius = 1
            elif shapeType in ['rectangle', 'triangle']:
                try:
                    width = attrs[nodes.WidthNode]
                except KeyError:
                    width = 1
                try:
                    height = attrs[nodes.HeightNode]
                except KeyError:
                    height = 1

            # shape creation
            if shapeType == 'circle':
                shape = Circle(color=color, posX=posX,
                               posY=posY, radius=radius)
            elif shapeType == 'rectangle':
                shape = Rectangle(color=color, posX=posX,
                                  posY=posY, width=width, height=height)
            elif shapeType == 'triangle':
                shape = Triangle(color=color, posX=posX,
                                 posY=posY, width=width, height=height)

            stack.append(shape)

        elif node.__class__ == nodes.DrawNode:
            shape = valueOfToken(stack.pop())
            shapeList.append(shape)
        elif node.__class__ == nodes.IfNode:
            ifnode = node

            if node.evaluated == False:
                cond = stack.pop()
                if cond:
                    node = node.next[0]
                elif len(node.next) == 3:
                    node = node.next[1]
                ifnode.evaluated = True
            else:
                node = node.next[-1]
                ifnode.evaluated = False
            continue

        if node.next:
            node = node.next[0]
        else:
            node = None

    return shapeList


if __name__ == "__main__":
    file = sys.argv[1]
    fileSplited = os.path.splitext(file)
    fileName = fileSplited[0]
    fileExtension = fileSplited[1]

    code = open(file).read()
    print("Parsing file :", file)
    programs, errors = parse(code)

    if len(errors) > 0:
        print("Errors :")
        print("\n".join(errors))
        exit()

    i = 0
    for program in programs:

        entry = thread(program)
        shapeList = synthese(entry)

        name = fileName
        if len(programs) > 1:
            name += "-" + str(i)
        name += ".svg"

        print("SVG Generation :", name)

        Shape.buildSVG(shapeList, fileName=name)
        i += 1
