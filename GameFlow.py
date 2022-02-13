import pygame
import screen
from time import time
from point import Point
from Hex import Hexagon

gameScreen = screen.getScreen()
black = 0,0,0
green = (0, 255, 0)
origin = Point(60*15/2,60*15/2)
hex = Hexagon(origin,150)
gameTime = 0
while 1:
    gameTime+=0.001
    gameScreen.fill(black)
    hex.drawHexagon(gameScreen,green)
    hex.updatePosition(gameTime)
    pygame.display.flip()
