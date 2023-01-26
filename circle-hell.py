from turtle import *
import colorsys
speed(8)
bgcolor("black")
hue = 0
pensize(1.5)
for j in range(400):
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    pencolor(color)
    hue += 0.005
    fd(j)
    lt(90)
    circle(30*2+1)
done()