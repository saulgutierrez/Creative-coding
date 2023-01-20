from turtle import Turtle, Screen

t = Turtle()
s = Screen()

t.speed(0)
s.bgcolor("black")

colors = ['yellow', 'green', 'red', 'white', 'cyan', 'blue']

for i in range(1000):
    t.pencolor(colors[i%6])
    t.circle(5*i)
    t.left(200)
    t.width()