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

'''Movement variables'''
constant_movement=10
movement_x_positive=False
movement_x_negative=False
movement_y_positive=False
movement_y_negative=False

'''Movement functions (not in use for now)'''
#Gravity functions
def gravity_acceleration(ABSX,ABSY):
    return 0

def objectisintheair():
    global absolute_starting_box_ypos
    global startground_y
    global box_shape_xy
    if absolute_starting_box_ypos==startground_y-box_shape_xy:
        return False
    return True

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                movement_y_positive=True
            if event.key==pygame.K_DOWN:
                movement_y_negative=True
            if event.key==pygame.K_LEFT:
                movement_x_negative=True
            if event.key==pygame.K_RIGHT:
                movement_x_positive=True
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_UP:
                movement_y_positive=False
            if event.key==pygame.K_DOWN:
                movement_y_negative=False
            if event.key==pygame.K_LEFT:
                movement_x_negative=False
            if event.key==pygame.K_RIGHT:
                movement_x_positive=False
    if objectisintheair() and movement_y_positive is not True:
        absolute_starting_box_ypos+=constant_movement
    if movement_y_positive:
        absolute_starting_box_ypos-=constant_movement
    window.fill(BACKGROUND)
    pygame.draw.line(window,BLACK,(startground_x,startground_y),(endground_x,endground_y),3)
    pygame.draw.rect(window,BLACK,((absolute_starting_box_xpos,absolute_starting_box_ypos),(box_shape_xy,box_shape_xy)),3)
    pygame.display.flip()
    clock.tick(FPS)