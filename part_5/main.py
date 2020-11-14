import pygame as pg
from settings import *
from player import Player
import math
from game_map import word_map
from ray_casting import ray_casting

pg.init()

sc = pg.display.set_mode((WIDTH,HEIGHT))
clock = pg.time.Clock()
player = Player()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
            
    player.movement()       
    sc.fill(BLACK_COLOR)
    
    pg.draw.rect(sc, BLUE_COLOR, (0,0, WIDTH, HALF_HEIGHT))
    pg.draw.rect(sc, DARKGREY_COLOR, (0,HALF_HEIGHT, WIDTH, HALF_HEIGHT))
    
    # add ray casting
    ray_casting(sc, player.position, player.angle)
 
 
    # this is 2d map
    # pg.draw.circle(sc, BLUE_COLOR, (int(player.x), int(player.y)), HERO_SIZE)
    # #add one ray
    # pg.draw.line(sc,WHITE_COLOR, player.position, (player.x + WIDTH * math.cos(player.angle), 
    #                                               player.y + WIDTH * math.sin(player.angle)))
    # #add word_map
    # for x,y in word_map:
    #     pg.draw.rect(sc, DARKGREY_COLOR, (x,y, TILE, TILE), 2)
    
    
    
    pg.display.flip()
    clock.tick(FPS)
 

