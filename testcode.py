import pygame
from pygame.locals import *
import random
import math
import sys

'''Test maincode'''

'''pygame init'''
pygame.init()

'''Window propierties'''
BACKGROUND=(255,255,255)
window_x=1020
window_y=640
FPS=60
window=pygame.display.set_mode((window_x,window_y))
clock = pygame.time.Clock()

'''Pre-defined colors'''
BLACK = (0,0,0)
WHITE = (255,255,255)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill(BACKGROUND)
    pygame.display.update()
    clock.tick(FPS)