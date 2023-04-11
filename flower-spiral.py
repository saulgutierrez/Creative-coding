import turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
t.speed(0)
t.width(2)
t.pencolor('cyan')
def star():
    for star in range(7):
        t.lt(45)
        t.circle(150, 90)
for i in range(24):
    star()
    t.lt(1)
    t.penup()
    t.fd(i * 4)
    t.pendown()
    t.rt(121)
    t.penup()
    t.goto(0, 0)
    t.pendown()
turtle.done()