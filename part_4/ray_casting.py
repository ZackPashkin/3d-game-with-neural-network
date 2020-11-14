import pygame as pg
from settings import *
from game_map import word_map


def ray_casting(sc, player_position, player_angle):
    cur_angle = player_angle - HALF_FOV
    xo, yo = player_position
    
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        
        for depth in range(MAX_DEPTH):
            x = xo + depth * cos_a
            y = yo + depth * sin_a
            #to display rays
            pg.draw.line(sc, DARKGREY_COLOR, player_position, (x,y), 2)
            if (x // TILE * TILE, y // TILE * TILE) in word_map:
                break
        cur_angle += DELTA_ANGLE