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
box_shape_xy=20
absolute_starting_box_xpos=300
absolute_starting_box_ypos=window_y-ground_height-box_shape_xy
time_in_air=0
jumping = False
character_rect=pygame.Rect((absolute_starting_box_xpos,absolute_starting_box_ypos),(box_shape_xy,box_shape_xy))
ground_rect=pygame.Rect((startground_x,startground_y),(ground_height,window_x))

print(pygame.display.Info())

'''Pre-defined colors'''
BLACK = (0,0,0)
WHITE = (255,255,255)

'''Movement variables'''
constant_movement=20
movement_x_positive=False
movement_x_negative=False
movement_y_positive=False
movement_y_negative=False
jump=False

'''Movement functions (not in use for now)'''
#Gravity functions
def gravity_acceleration(ABSX,ABSY):
    return 0

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                movement_y_positive=True
            if event.key==pygame.K_s:
                movement_y_negative=True
            if event.key==pygame.K_a:
                movement_x_negative=True
            if event.key==pygame.K_d:
                movement_x_positive=True
            if event.key==pygame.K_SPACE:
                jump = True
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_w:
                movement_y_positive=False
            if event.key==pygame.K_s:
                movement_y_negative=False
            if event.key==pygame.K_a:
                movement_x_negative=False
            if event.key==pygame.K_d:
                movement_x_positive=False
            if event.key==pygame.K_SPACE:
                jump=False
    
    if jump:
        jumping=True
    if jumping:
        time_in_air += 1
        inicialvelocity=15
        velocity=inicialvelocity-(0.1*time_in_air)
        relativepos=int((velocity)-(0.5*(0.1)*(time_in_air**2)))
        absolute_starting_box_ypos-=relativepos
    if absolute_starting_box_ypos+box_shape_xy >= startground_y:
        time_in_air=0
        absolute_starting_box_ypos=startground_y-box_shape_xy
        jumping=False
    if movement_x_negative:
        absolute_starting_box_xpos-=constant_movement
    if movement_x_positive:
        absolute_starting_box_xpos+=constant_movement
    window.fill(BACKGROUND)
    pygame.draw.line(window,BLACK,(startground_x,startground_y),(endground_x,endground_y),3)
    pygame.draw.rect(window,BLACK,((absolute_starting_box_xpos,absolute_starting_box_ypos),(box_shape_xy,box_shape_xy)),3)
    pygame.display.flip()
    clock.tick(FPS)