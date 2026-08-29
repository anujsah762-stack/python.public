import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("gray")

# Create turtle
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

# Draw outer circle
pen.color("black", "black")
pen.begin_fill()
pen.circle(100)
pen.end_fill()

# Draw white half
pen.penup()
pen.goto(0, 100)
pen.setheading(180)
pen.pendown()

pen.color("white", "white")
pen.begin_fill()
pen.circle(50, 180)
pen.circle(100, 180)
pen.circle(50, -180)
pen.end_fill()

# Draw black small circle
pen.penup()
pen.goto(0, 50)
pen.setheading(0)
pen.pendown()

pen.color("black", "black")
pen.begin_fill()
pen.circle(12)
pen.end_fill()

# Draw white small circle
pen.penup()
pen.goto(0, -50)
pen.setheading(0)
pen.pendown()

pen.color("white", "white")
pen.begin_fill()
pen.circle(12)
pen.end_fill()

# Hide turtle
pen.hideturtle()

turtle.done()
