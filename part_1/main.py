import pygame as pg
from settings import *


pg.init()

sc = pg.display.set_mode((WIDTH,HEIGHT))
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
            
            
    sc.fill(BLACK_COLOR)
    
    pg.draw.circle(sc, BLUE_COLOR, PLAYER_POSITION, HERO_SIZE)
    
    pg.display.flip()
    clock.tick()


