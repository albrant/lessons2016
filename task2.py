from drawman import *
drawman_scale(55)

def all4():
    for y1 in range(1,5):
        for y2 in range(1,5):
            pen_up()
            to_point(1,y1)
            pen_down()
            to_point(3,y2)
    pen_up()

all4()

input("жду")