import pygame as py
import math
from point import Point
import sys, pygame

class Hexagon():
    def __init__(self,origin,length):
        self.origin = origin
        self.length = length
        self.pA , self.pB , self.pC, self.pD, self.pE , self.pF = self.calcHexPoints()
        self.points = [self.pA , self.pB , self.pC, self.pD, self.pE , self.pF]

    def calcHexPoints(self):
        pA = Point(self.origin.x + self.length , self.origin.y)
        pB = Point(self.origin.x + self.length/2 , self.origin.y + (math.sqrt(3)/2) * self.length)
        pC = Point(self.origin.x - self.length/2 , self.origin.y + (math.sqrt(3)/2) * self.length)
        pD = Point(self.origin.x - self.length , self.origin.y)
        pE = Point(self.origin.x - self.length/2 , self.origin.y - (math.sqrt(3)/2) * self.length)
        pF = Point(self.origin.x + self.length/2 , self.origin.y - (math.sqrt(3)/2) * self.length)
        return pA , pB , pC, pD , pE , pF

    def drawHexagon(self,screen,colour):
        linewidth = 3
        try:
            pygame.draw.line(surface=screen,start_pos=self.pA.get(),end_pos=self.pB.get(),color=colour,width=linewidth)
            pygame.draw.line(surface=screen,start_pos=self.pB.get(),end_pos=self.pC.get(),color=colour,width=linewidth)
            pygame.draw.line(surface=screen,start_pos=self.pC.get(),end_pos=self.pD.get(),color=colour,width=linewidth)
            pygame.draw.line(surface=screen,start_pos=self.pD.get(),end_pos=self.pE.get(),color=colour,width=linewidth)
            pygame.draw.line(surface=screen,start_pos=self.pE.get(),end_pos=self.pF.get(),color=colour,width=linewidth)
            pygame.draw.line(surface=screen,start_pos=self.pF.get(),end_pos=self.pA.get(),color=colour,width=linewidth)
        except:
            print("An exception occurred")
    def updatePosition(self,time):
        for point in self.points:
            point.x += point.x * math.cos(time)/200
            point.y += point.y * math.cos(time)/200

    def recusiveDraw(self,screen,colour):
        hexagons = []
        for point in self.points:
            hexagons.append(Hexagon(point,self.length))
        for hexagon in hexagons:
            hexagon.drawHexagon(screen,colour)
        return hexagons
