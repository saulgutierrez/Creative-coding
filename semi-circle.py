import turtle
t = turtle.Turtle()
sscreen = turtle.Screen()
sscreen.bgcolor('black')
t.pensize(5)
t.speed(0)
color = ['green', 'red', 'brown', 'purple', 'gold', 'silver']
t.goto(150, -100)
for i in range(10):
    t.lt(45)
    for i in range(5):
        t.color(color[i % 6])
        t.circle(60, 120)
        t.rt(72)
turtle.done()