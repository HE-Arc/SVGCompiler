#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Shape(object):

    def __init__(self, color="#000000", posX=0, posY=0):
        self.color = color
        self.posX = posX
        self.posY = posY

    @staticmethod
    def buildSVG(shapeList, fileName):
        with open(fileName, 'w') as file: 
            file.write('<svg xmlns="http://www.w3.org/2000/svg">\n') 
            for shape in shapeList:
                file.write(f'{shape}\n')
            file.write('</svg>')


class Circle(Shape):

    def __init__(self, color="#000000", posX=0, posY=0, radius=1):
        self.radius = radius
        super(Circle, self).__init__(color=color, posX=posX, posY=posY)

    def __str__(self):
        return f'<circle cx="{self.posX}" cy="{self.posY}" r="{self.radius}" fill="{self.color}" />'


class Rectangle(Shape):

    def __init__(self, color="#000000", posX=0, posY=0, width=1, height=1):
        self.width = width
        self.height = height
        super(Rectangle, self).__init__(color=color, posX=posX, posY=posY)

    def __str__(self):
        return f'<rect width="{self.width}" height="{self.height}" x="{self.posX}" y="{self.posY}" fill="{self.color}" />'


class Triangle(Rectangle):

    def __init__(self, color="#000000", posX=0, posY=0, width=1, height=1):
        super(Triangle, self).__init__(color=color, posX=posX,
                                       posY=posY, width=width, height=height)

    def __str__(self):
        return f'<polygon points="{self.posX} {self.posY+self.height}, {self.posX+self.width} {self.posY+self.height}, {self.posX+self.width/2} {self.posY}" fill="{self.color}"/>'
