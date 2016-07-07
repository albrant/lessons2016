from turtle import Turtle
from draw_number import draw_number
default_scale = 10


def init_drawman():
    global t,x_current,y_current, _drawman_scale
    t = Turtle()
    t.speed(100)
    t.penup()
    x_current = 0
    y_current = 0
    t.goto(x_current,y_current)
    drawman_scale(default_scale)

def drawman_color(color):
    global t
    t.color(color)


def drawman_scale(scale):
    global _drawman_scale
    _drawman_scale = scale


def draw_grid(x_grid_scale=10,y_grid_scale=10):
    t.color("lightgrey")
    for x in range(0,500,x_grid_scale * _drawman_scale):
        t.penup()
        t.goto(x,-500)
        t.pendown()
        t.goto(x,500)
    for x in range(0,-500,-x_grid_scale * _drawman_scale):
        t.penup()
        t.goto(x,-500)
        t.pendown()
        t.goto(x,500)
    for y in range(0,500,y_grid_scale * _drawman_scale):
        t.penup()
        t.goto(-500,y)
        t.pendown()
        t.goto(500,y)
    for y in range(0,-500,-y_grid_scale * _drawman_scale):
        t.penup()
        t.goto(-500,y)
        t.pendown()
        t.goto(500,y)
    t.color("black")
    t.penup()
    t.goto(-500,0)
    t.pendown()
    t.goto(500,0)
    t.penup()
    t.goto(0,-500)
    t.pendown()
    t.goto(0,500)

    t.penup()
    xx = -x_grid_scale
    for x in range(0,500,x_grid_scale * _drawman_scale):
        t.goto(x+2,-15)
        xx += x_grid_scale
        draw_number(t,xx)
    xx = x_grid_scale
    for x in range(0,-500,-x_grid_scale * _drawman_scale):
        t.goto(x+2,-15)
        xx -= x_grid_scale
        draw_number(t,-xx)
    yy = -y_grid_scale
    for y in range(0,500,y_grid_scale * _drawman_scale):
        t.goto(2,y)
        yy += y_grid_scale
        draw_number(t,yy)
    yy = y_grid_scale
    for y in range(0,-500,-y_grid_scale * _drawman_scale):
        t.goto(2,y)
        yy -= y_grid_scale
        draw_number(t,-yy)

def test_drawman():
    """
    тестирование работы чертежнжика
    :return:
    """
    pen_down()
    for i in range(5):
        on_vector(10,20)
        on_vector(0,-20)
    pen_up()
    to_point(0,0)


def pen_down():
    t.pendown()


def pen_up():
    t.penup()


def on_vector(dx,dy):
    to_point(x_current + dx, y_current + dy)


def to_point(x,y):
    global x_current,y_current
    x_current = x
    y_current = y
    t.goto(_drawman_scale*x_current,_drawman_scale*y_current)


init_drawman()

if __name__ == '__main__':
    import time
    test_drawman()
    time.sleep(10)

