"""
Game settings here
    
"""
import math


# for main.py
WIDTH = 1300
HEIGHT = 900

HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2

FPS = 60


# ray casting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 120
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS

# for map.py
TILE = 100

# for 3d 
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE 
SCALE = WIDTH // NUM_RAYS





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
DARKGREY_COLOR = (40,40,40)
PURPLE_COLOR = (120,0,120)
