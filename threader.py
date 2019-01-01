from AST import addToClass
import AST
import nodes
from parser_ import parse # we cant import a file named 'parser'... ?
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
        # print(program)

        graphName = fileName + "-" + str(i) + ".pdf"
        graph = program.makegraphicaltree()
        graph.write_pdf(graphName)


        graphNameThreaded = fileName + "-" + str(i) + "-threaded.pdf"
        programThreaded = thread(program)
        programThreaded.threadTree(graph)

        graph.write_pdf(graphNameThreaded)



    # exit()
