import random
#Screen settings
WIDTH = 640
HEIGHT = 500
TITLE = "PyScrable"
FPS = 60

#Colors
DARK_BLUE = (0,206,209)
BLACK = (255, 255, 255)
RED = (0, 166, 203)
GREEN = (0, 255, 0)
ALPHA = (0, 255, 0)



#Platforms(x, y, img)
#enemyRocket(x,y)
PLATFORMS_LIST_EMPTY = []


platfrom = [
    "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
    "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
    "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
    "B B R B R BB RBB     RBB  BBB    BBBBBBB B B BBBBBBBBBB  BBBBBBBBBBBBB",
    "  B   B    B  B            B      B   B       B BBBBB      B BB  BB  B",
    "                                                  BB                  ",
]

row_y = 0


for row in platfrom:
    row_y += 32
    col_x = 0
    for col in row:
        col_x += 32
        print(col_x)
        if col == "B":
            PLATFORMS_LIST_EMPTY.append((col_x, HEIGHT-row_y, 'Platform.png'))


PLATFORMS_LIST = PLATFORMS_LIST_EMPTY
print(PLATFORMS_LIST)



def collision_detection():
    pass

