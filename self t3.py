import turtle
a = turtle.Turtle()
for i in range(8):
    a.forward(100)
    a.right(45)
    a.color("red")
for i in range(8):
    a.right(45)
    a.forward(100)
    a.color("blue")
a.left(135)
for i in range(8):
    a.forward(100)
    a.left(45)
    a.color("green")
a.left(180)
for i in range(8):
    a.forward(100)
    a.left(45)
    a.color("yellow")
a.left(90)
for i in range(8):
    a.forward(100)
    a.left(45)
    a.color("purple")
a.left(45)
for i in range(8):
    a.forward(100)
    a.left(45)
    a.color("orange")
a.right(90)
for i in range(8):
    a.forward(100)
    a.left(45)
    a.color("pink")
a.right(90)
for i in range(8):
    a.forward(100)
    a.left(45)
    a.color("brown")
turtle.done()