import turtle
a= turtle.Turtle()
for i in range(4):
    a.forward(100)
    a.right(90)
a.penup()
a.goto(0, 0)
a.pendown()
for i in range(4):
    a.backward(100)
    a.right(90)
a.penup()
a.goto(0, 0)
a.pendown()
for i in range(4):
    a.backward(100)
    a.left(90)
a.penup()
a.goto(0, 0)
a.pendown()
for i in range(4):
    a.forward(100)
    a.left(90)
turtle.done()