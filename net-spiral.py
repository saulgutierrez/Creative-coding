import turtle
import colorsys
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
turtle.tracer(100)
t.pensize(3)
a = 0
for i in range(210):
    c = colorsys.hsv_to_rgb(a, 1, 1)
    a += 0.01
    t.pencolor(c)
    t.begin_fill()
    t.lt(105)
    t.fd(200-i)
    t.circle(-30, -150)
    t.fd(200-i)
    t.circle(-30)
    t.end_fill()
turtle.done()