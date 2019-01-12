#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module used for the SVG code synthesis from an AST by "SVGCompiler"
It is the "main" program for our program and is the only one meant to be directly executed for a non-debugging use
Sergiy Goloviatinski & Raphaël Margueron, inf3dlm-b, HE-Arc
13.01.19
"""

from AST import addToClass
import AST
import nodes
from parser_ import parse  # we cant import a file named 'parser' on Windows systems... ?
import sys
import os
import random
from shapes import *
from threader import thread

# Lambda expressions to be executed for each binary operation
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

# Lambda expressions to be executed for each unary operation
unaryOperations = {
    '!': lambda x: not x,
    '-': lambda x: -x
}

# Intermediate stack used for the synthese (e.g. first we push shape's attributes on the stack, and then we pop the attributes to construct a shape,
#  or first we push a variable value and a variable name and then we pop these two to affect the value to the name)
stack = []

# Dict containing variables: the key is the variable name and the associated value is the variable value (the type is given by the AST node type and is managed by the semantic analysis)
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
            # node.__class__.__bases__[-1] means "any class that inherits from AttributeNode"
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
            # we don't need the varType because it is checked in the semantic analysis but it is in the tree
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

            if not node.evaluated:
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
        print("Compilation aborted")
        exit()

    i = 0
    for program in programs:
        # Each code part delimitated with braces will result in an individual .svg output file
        entry = thread(program)
        shapeList = synthese(entry)

        name = fileName
        if len(programs) > 1:
            name += "-" + str(i)
        name += ".svg"

        print("SVG Generation :", name)

        Shape.buildSVG(shapeList, fileName=name)
        i += 1
