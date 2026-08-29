import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("gray")
screen.title("Yin Yang")

# Create turtle
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.hideturtle()

# Draw large black circle
pen.penup()
pen.goto(0, -100)
pen.pendown()
pen.color("black", "black")
pen.begin_fill()
pen.circle(100)
pen.end_fill()

# Draw top white half shape
pen.penup()
pen.goto(0, 0)
pen.pendown()
pen.color("white", "white")
pen.begin_fill()
pen.circle(50)
pen.end_fill()

# Draw bottom black half shape
pen.penup()
pen.goto(0, -100)
pen.pendown()
pen.color("black", "black")
pen.begin_fill()
pen.circle(50)
pen.end_fill()

# Draw black dot in white area
pen.penup()
pen.goto(0, 38)
pen.pendown()
pen.color("black", "black")
pen.begin_fill()
pen.circle(12)
pen.end_fill()

# Draw white dot in black area
pen.penup()
pen.goto(0, -62)
pen.pendown()
pen.color("white", "white")
pen.begin_fill()
pen.circle(12)
pen.end_fill()

# Draw outer circle border
pen.penup()
pen.goto(0, -100)
pen.pendown()
pen.color("black")
pen.width(3)
pen.circle(100)

pen.hideturtle()

turtle.done()