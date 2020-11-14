import pygame as pg
from settings import *
from player import Player


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
    
    pg.draw.circle(sc, BLUE_COLOR, player.position, HERO_SIZE)
    
    pg.display.flip()
    clock.tick(FPS)


