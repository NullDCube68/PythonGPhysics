import pygame
from pygame.locals import *
import random
import math
import sys

'''pygame init'''
pygame.init()

'''Window propierties'''
BACKGROUND=(255,255,255)
window_x=1020
window_y=640
FPS=60
window=pygame.display.set_mode((window_x,window_y))
clock = pygame.time.Clock()

'''By-default ground'''
ground_height=120
startground_x=0
startground_y=window_y-ground_height
endground_x=window_x
endground_y=window_y-ground_height

'''Testing'''
box_shape_xy=200
absolute_starting_box_xpos=300
absolute_starting_box_ypos=window_y-ground_height-box_shape_xy

'''Pre-defined colors'''
BLACK = (0,0,0)
WHITE = (255,255,255)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill(BACKGROUND)
    pygame.draw.line(window,BLACK,(startground_x,startground_y),(endground_x,endground_y),3)
    pygame.draw.rect(window,BLACK,((absolute_starting_box_xpos,absolute_starting_box_ypos),(box_shape_xy,box_shape_xy)),3)
    pygame.display.update()
    clock.tick(FPS)