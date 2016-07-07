from drawman import *
from time import sleep
A = [(0,0),(100,0),(100,100),(0,100)]

def f(x):
    return x*x


drawman_scale(15)
draw_grid(5,10)
drawman_color("red")
x = -5.0
to_point(x,f(x))
pen_down()
while x<5:
    to_point(x,f(x))
    x +=0.1
pen_up()

q=input("Жду")
#sleep(10)