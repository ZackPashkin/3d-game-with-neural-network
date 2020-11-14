from settings import *

simple_text_map = [
    'WWWWWWWWWWWWW',
    'W...........W',
    'W....WW.....W',
    'W...........W',
    'W...........W',
    'W.......WW..W',
    'W.WW........W',
    'W...........W',
    'WWWWWWWWWWWWW'
]
word_map = set()

for j, row in enumerate(simple_text_map):
    for i, char in enumerate(row):
        if char == 'W':
            word_map.add((i * TILE, j * TILE))
        