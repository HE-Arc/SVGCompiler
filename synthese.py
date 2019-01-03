#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from AST import addToClass
import AST
import nodes
from parser_ import parse  # we cant import a file named 'parser'... ?
import sys
import os
from threader import thread


binaryOperations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y,
    '==': lambda x, y: x == y,
    '!=': lambda x, y: x != y,
    '&&': lambda x, y: x and y,
    '||': lambda x, y: x or y,
    '<': lambda x, y: x < y,
    '>': lambda x, y: x > y
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
            print(f"*** Error: variable {t} undefined !")
    return t


def synthese(node):
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
            if cond:  # si cond vraie, on va à "gauche"
                node = node.next[0]
            else:  # sinon à "droite"
                node = node.next[1]
            continue
        elif node.__class__ == nodes.ShapeNode:
            attrs = {}
            # depiler la pile jusqu'à ce qu'elle soit vide OU qu'on tombe sur le noeud "de début d'une shape" = premier enfant "inutile" de la shape pushé auparavant
            print(attrs)
        elif node.__class__ == nodes.DrawNode:
            shape = valueOfToken(stack.pop())
            # print(shape)
        elif node.__class__ == nodes.IfNode:
            cond = stack.pop()
            if cond:  # si cond vraie, on va à "gauche"
                node = node.next[0]
            else:  # sinon à "droite"
                node = node.next[1]

        if node.next:
            node = node.next[0]
        else:
            node = None


if __name__ == "__main__":
    file = sys.argv[1]
    fileSplited = os.path.splitext(file)
    fileName = fileSplited[0]
    fileExtension = fileSplited[1]

    code = open(file).read()
    programs = parse(code)

    for i in range(len(programs)):
        program = programs[i]

        entry = thread(program)
        synthese(entry)
