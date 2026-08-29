import turtle 
t=turtle.Turtle("circle")
t.speed(0)
cs=["red","green","blue"]
for i in range(0,300,2):
    t.color(cs[i%len(cs)])
    t.left(59)
    t.forward(2+i)
turtle.done()