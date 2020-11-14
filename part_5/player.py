from settings import *
import pygame as pg
import math


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
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
         
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.x += PLAYER_SPEED * cos_a
            self.y += PLAYER_SPEED * sin_a
            print("UP")
        if keys[pg.K_DOWN]:
            self.x += -PLAYER_SPEED * cos_a
            self.y += -PLAYER_SPEED * sin_a
            print("DOWN")
        if keys[pg.K_LEFT]:
            self.x += PLAYER_SPEED * sin_a
            self.y += -PLAYER_SPEED * cos_a
            print("LEFT")
        if keys[pg.K_RIGHT]:
            self.x += -PLAYER_SPEED * sin_a
            self.y += PLAYER_SPEED * cos_a
            print("RIGHT")
            
        # to turn    
        if keys[pg.K_a]:
            self.angle -= 0.03
        if keys[pg.K_d]:
            self.angle += 0.03
      