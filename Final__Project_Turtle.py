import turtle

t=turtle.Turtle()


colors=('red','orange','yellow','green','blue','purple','pink')
t.speed(15)
for i in range(100):
    t.color(colors[i%7])
    t.forward(i*4)
    t.left(150)
    t.width(5)

t.done()