#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module used to thread an AST for "SVGCompiler"
It is not meant to be directly executed for a "normal" use, execute it only for intermediate debugging purposes if you want to see a pdf with the threaded AST
Sergiy Goloviatinski & Raphaël Margueron, inf3dlm-b, HE-Arc
13.01.19
"""

from AST import addToClass
import AST
import nodes
from parser_ import parse  # we cant import a file named 'parser'... ?
import sys
import os


@addToClass(AST.Node)
def thread(self, lastNode):
    for c in self.children:
        lastNode = c.thread(lastNode)
    lastNode.addNext(self)
    return self


@addToClass(nodes.LoopNode)
def thread(self, lastNode):
    beforeCond = lastNode
    exitCond = self.children[0].thread(lastNode)
    exitCond.addNext(self)
    exitBody = self.children[1].thread(self)
    exitBody.addNext(beforeCond.next[-1])

    return self


@addToClass(nodes.IfNode)
def thread(self, lastNode):
    conditionProgram = self.conditionProgram
    trueProgram = self.trueProgram
    falseProgram = self.falseProgram

    exitCondition = conditionProgram.thread(lastNode)
    exitCondition.addNext(self)

    if trueProgram is not None:
        exitTrueProgram = trueProgram.thread(self)
        exitTrueProgram.addNext(self)

    if falseProgram is not None:
        exitFalseProgram = falseProgram.thread(self)
        exitFalseProgram.addNext(self)

    return self


def thread(tree):
    entry = AST.EntryNode()
    tree.thread(entry)
    return entry


if __name__ == '__main__':
    file = sys.argv[1]
    fileSplited = os.path.splitext(file)
    fileName = fileSplited[0]
    fileExtension = fileSplited[1]

    code = open(file).read()
    programs = parse(code)

    for i in range(len(programs)):
        program = programs[i]
        print("Program", i)
        print(program)

        graphName = fileName + "-" + str(i) + ".pdf"
        graph = program.makegraphicaltree()
        print("Generating graphical tree...")
        graph.write_pdf(graphName)

        graphNameThreaded = fileName + "-" + str(i) + "-threaded.pdf"
        programThreaded = thread(program)
        programThreaded.threadTree(graph)

        print("Generating threaded graphical tree...")
        graph.write_pdf(graphNameThreaded)
