import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(900)

col = ['indigo', 'gold', 'blue', 'red', 'orange']

for i in range(300):
    t.pencolor(col[i%5])
    t.forward(i)
    t.right(89)
    t.forward(i)
    t.right(89)

turtle.done()