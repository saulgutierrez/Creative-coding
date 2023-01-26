import colorsys
from turtle import *
tracer(100)
bgcolor('black')
pensize(4)
h = 0.4
for i in range(1000):
    c = colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h += 0.005
    goto(0, 0)
    forward(i)
    circle(i, -120)
    left(180)
done()