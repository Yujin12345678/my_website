import turtle

t=turtle.Turtle()

t.pensize(5)
t.color("red")
t.shape("turtle")
for i in range(4):
    t.forward(100)
    t.left(90)

t.color("green")
t.shape("circle")
for i in range(3):
    t.forward(100)
    t.left(120)

t.color("purple")
t.shape("turtle")
for i in range(6):
    t.forward(100)
    t.left(60)
turtle.done()