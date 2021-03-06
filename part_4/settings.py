"""
Game settings here
    
"""

# for main.py

import math 

WIDTH = 1300
HEIGHT = 900

HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2

FPS = 60


# for map.py
TILE = 100

# ray casting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 120
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS


# player settings
PLAYER_POSITION = (HALF_WIDTH, HALF_HEIGHT)
PLAYER_ANGLE = 0
PLAYER_SPEED = 3
HERO_SIZE = 10

# colors
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
RED_COLOR = (220,0, 0)
GREEN_COLOR = (0,220,0)
BLUE_COLOR = (0,0,220)
DARKGREY_COLOR = (110,110,110)
PURPLE_COLOR = (120,0,120)
