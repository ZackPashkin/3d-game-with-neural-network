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
            # pg.draw.line(sc, DARKGREY_COLOR, player_position, (x,y), 2)
            
            if (x // TILE * TILE, y // TILE * TILE) in word_map:
                # to remove fish eye effect on walls
                depth *= math.cos(player_angle - cur_angle)
                # projection height of wall
                proj_height = PROJ_COEFF / depth
                #add dynamic color
                col = 255 / (1 + depth * depth * 0.0001)
                color = (col // 2, col, col // 2)
                
                pg.draw.rect(sc, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
                
                break
        cur_angle += DELTA_ANGLE
        
    