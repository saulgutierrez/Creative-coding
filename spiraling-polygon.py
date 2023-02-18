import turtle as t
t.bgcolor("black")
t.color("red")
t.speed(140)
t.pensize(2)
side = 8
length = 4
angle = 360 / side
for i in range(100):
    t.forward(length)
    t.right(angle)
    length = length - 2
t.hideturtle()
t.done()