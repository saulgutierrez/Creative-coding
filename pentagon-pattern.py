import turtle
screen = turtle.Screen()
turtle.pensize(2)
turtle.speed(0)
turtle.bgcolor('black')
for i in range(140):
    turtle.pencolor('red')
    turtle.fd(2*i)
    turtle.right(75)
    turtle.pencolor('purple')
    turtle.circle(5)

turtle.done()