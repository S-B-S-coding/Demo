import pygame

# Color Constants
WHITE = (255, 255, 255)  # (r, g, b)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
BRIGHT_BLUE = (46, 192, 255)
GREY = (140, 140, 140)
BROWN = (59, 33, 1)
DARK_GREEN = (1, 36, 2)
LIGHT_GREY = (203, 204, 200)
DARK_GREY = (29, 29, 29)
GOLD = (162, 136, 1)

BG_COLOR = WHITE

GRAVITY = 1

# Frames Per Second
FPS = 60

LEVELS = [["11111111111111111111111111111111111111111111111", 
          "1                                             1",
          "1                                             1",
          "1gggggggggggggg                               1",
          "1               b   e   b                     1",
          "1                ggggggg                      1",
          "1                                             1",
          "1                        gggggg               1",
          "1                                             1",
          "1                                   ggggggg   1",
          "1                                             1",
          "1                        gggggg               1",
          "1                                             1",
          "1                                   ggggggg   1",
          "1       p                                     1",
          "1                    gggggggggg               1",
          "1                                             1",
          "1             ggggg                           1",
          "1                                             1",
          "            d                                 e",
          "ggggggggggggggggggggggggggggggggggggggggggggggg"
          
], 
["11111111111111111111111111111111111111111111111",
 "1  p       111111111111111111111              1",
 "1gggggggg  111111111111111111111  gggggggggg  1",
 "1      k1                         1           1",
 "1     gg1e                       e1           1",
 "1  ggg111ggggggggggggggggggggggggg1     gggggg1",
 "1                                             1",
 "1 gggggggggg     e       ggggggggggggggggggggg1",
 "1          1ggggggggggggg1                    1",
 "1                                             1",
 "1ggggggggggggggggggggggggggggggggggggg        1",
 "1                                             1",
 "1    ggggggggggggggggggggggggggggggggggggggggg1",
 "1                                             1",
 "1               e    ggggggggggggggggggggggg  1",
 "1gggggggggggggggggggg1                        1",
 "1                                             1",
 "1    be                                     eg1",
 "1     ggggggggggggggggggggggggggggggggggggggg 1",
 "1                                     L      d1",
 "1ggggggggggggggggggggggggggggggggggggggggggggg1"

]]


# print(f"Rows: {len(LAYOUT)}, Cols: {len(LAYOUT[0])}")
BRICK_WIDTH = 30
BRICK_HEIGHT = 30

PLAYER_WIDTH = 25
PLAYER_HEIGHT = 25

ENEMY_WIDTH = 23
ENEMY_HEIGHT = 15

DOOR_WIDTH = 30
DOOR_HEIGHT = 50

E_BARRIER_WIDTH = BRICK_WIDTH
E_BARRIER_HEIGHT = BRICK_HEIGHT

LOCKED_DOOR_WIDTH = BRICK_WIDTH
LOCKED_DOOR_HEIGHT = BRICK_HEIGHT

KEY_HEIGHT = 15
KEY_WIDTH = BRICK_WIDTH
# print(f'Rows')


# Display parameters
DISPLAY_WIDTH = BRICK_WIDTH * len(LEVELS[0][0])
DISPLAY_HEIGHT = BRICK_HEIGHT * len(LEVELS[0])

DISPLAY_WIDTH2 = BRICK_WIDTH * len(LEVELS[1][0])
DISPLAY_HEIGHT2 = BRICK_HEIGHT * len(LEVELS[1])



