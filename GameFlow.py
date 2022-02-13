import pygame
import screen
from time import time
from point import Point
from Hex import Hexagon
import colourChanger

gameScreen = screen.getScreen()
black = 0,0,0
newColour = (0, 255, 0)
origin = Point(60*15/2,60*15/2)
hex = Hexagon(origin,150)
gameTime = 0
while 1:
    gameTime+=0.001
    gameScreen.fill(black)
    newColour = colourChanger.colourChange(newColour,gameTime)
    hex.drawHexagon(gameScreen,newColour)
    hexagons = hex.recusiveDraw(gameScreen,newColour)
    for hexa in hexagons:
        hexi = hexa.recusiveDraw(gameScreen,newColour)
        for hx in hexi:
            hx.recusiveDraw(gameScreen,newColour)
    #hex.updatePosition(gameTime)
    pygame.display.flip()
