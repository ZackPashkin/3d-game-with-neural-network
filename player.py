from settings import *
import pygame as pg


class Player:
    def __init__(self):
        self.x, self.y = PLAYER_POSITION
        self.angle = PLAYER_ANGLE
        
        
    @property
    def position(self):
        return (self.x, self.y)
        
    
    def movement(self):
        """
        Player control here
        
        K_UP --> up arrow,
        K_DOWN  --> down arrow,
        K_RIGHT --> right arrow,
        K_LEFT --> left arrow
        """
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.y -= PLAYER_SPEED
        if keys[pg.K_DOWN]:
            self.y += PLAYER_SPEED
        if keys[pg.K_LEFT]:
            self.x -= PLAYER_SPEED
        if keys[pg.K_RIGHT]:
            self.x += PLAYER_SPEED
      