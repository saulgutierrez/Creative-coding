import turtle
from turtle import *

s = Screen()
s.setup(width=1200, height=680)
t = Turtle()
s.bgcolor('black')
t.speed(0)
colors = ['blue', 'red']

for i in range(180):
    t.pencolor(colors[i%len(colors)])
    t.rt(i)
    t.circle(100,i)
    t.fd(i)
    t.rt(180)
    t.fd(i)

s.mainloop()