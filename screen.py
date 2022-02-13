import pygame
def getScreen():
    pygame.init()
    size = width, height = 60 * 15 , 60 * 15
    screen = pygame.display.set_mode(size)
    return screen
