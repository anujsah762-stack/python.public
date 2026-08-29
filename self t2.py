import turtle
a= turtle.Turtle()
for i in range(8):
    a.forward(100)
    a.right(45)
    a.color("red")
    a.fillcolor("yellow")
for i in range(8):
    a.right(45)
    a.forward(100)
    a.color("blue")
for i in range(8):
    a.forward(100)
    a.left(45)
    a.color("green")
for i in range(8):
    a.left(45)
    a.forward(100)
    a.color("purple")
turtle.done()
