#Screen settings
WIDTH = 320
HEIGHT = 480
TITLE = "PyScrable"
FPS = 60



#Colors
DARK_BLUE = (0,28,73)
BLACK = (255, 255, 255)
RED = (0, 166, 203)
GREEN = (0, 255, 0)
YELLOW = (249, 215, 28)
ALPHA = (0, 255, 0)



#Platforms(x, y, img)
#enemyRocket(x,y)
PLATFORMS_LIST_EMPTY = []
ENEMY_LIST_EMPTY = []


platfrom = [
    "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
    "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
    "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
    "B B R B R BB RBB  R  RBB  BBB    BBBBBBB B B BBBBBBBBBB  BBBBBBBBBBBBB",
    "  B   B    B  B            B      B R B       B BBBBB      B BB  BB  B",
    "                                                 RBB                  ",
]

row_y = 0


for row in platfrom:
    row_y += 32
    col_x = 0
    for col in row:
        col_x += 32
        if col == "B":
            PLATFORMS_LIST_EMPTY.append((col_x, HEIGHT-row_y, 'Platform.png'))
        if col == "R":
            ENEMY_LIST_EMPTY.append((col_x, HEIGHT-row_y, 'EnemyRocket.png'))


PLATFORMS_LIST = PLATFORMS_LIST_EMPTY
ENEMY_LIST = ENEMY_LIST_EMPTY