import turtle as t

t.speed(0)

# Draw the 12 circles
for i in range(12):
    t.circle(40)
    t.right(30)

# Colors
colors = ["red", "blue", "green", "yellow", "orange", "purple",
          "pink", "cyan", "brown", "gray", "lime", "gold"]

# Go back to the center
t.penup()
t.home()
t.pendown()

# Fill the intersection/petal regions
for i in range(12):
    t.fillcolor(colors[i])
    t.begin_fill()

    t.circle(40)
    t.right(30)

    t.end_fill()

t.done()