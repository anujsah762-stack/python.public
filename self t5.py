import colorsys
import turtle
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
for i in range(360):
    t.right(10)
    for j in range(9):
        c = colorsys.hsv_to_rgb(i/360, 1, 1)
        t.color(c)
        t.forward(100)
        t.right(45)
turtle.done()