#Screen settings
WIDTH = 320
HEIGHT = 480
TITLE = "PyScrable"
FPS = 60



#Colors
DARK_BLUE = (0,28,73)
BLACK = (255, 255, 255)
RED = (216, 6, 52)
DARK_RED = (89, 0, 20)
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
    "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB                       BBBBBBBBBBBBBBBB",
    "            BBBBBBBBBBBBBBBBBB                          BBBBBBBBBBBBBB",
    "             RBBBBBB BBBBBBBB              B BBBBBBBBBB  BBBBBBBBBBBBB",
    "              BBB R  R   BBB                  B BBBBB      B BB  BB  B",
    "               B          B                      R                    ",
    "                                                                      ",

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