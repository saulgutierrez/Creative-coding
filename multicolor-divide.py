import turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
t.lt(90)
color = ['green', 'yellow', 'brown', 'purple', 'gold', 'silver']
for i in range(24):
    t.begin_fill()
    t.fillcolor(color[i%6])
    t.fd(100)
    t.circle(15, 180)
    t.lt(15)
    t.fd(105)
    t.lt(180)
    t.end_fill()
turtle.done()