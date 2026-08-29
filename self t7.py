import turtle as t

colors = ["red", "blue", "green", "yellow", "orange", "purple",
          "pink", "cyan", "brown", "gray", "lime", "gold"]

for i in range(12):
    t.speed(12)
    t.fillcolor(colors[i])
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    t.right(30)

t.done()