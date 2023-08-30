import turtle

t=turtle.Turtle()

t.speed(15)
t.shape("turtle")
colors=['red', 'blue']
for i in range(300):
    t.forward(i+1)
    t.right(89)
    t.color(colors[i%2])

t.speed(15)
colors=['red', 'dark red']
for i in range(180):
    t.forward(i+1)
    t.right(50)
    t.color(colors[i%2])

t.speed(15)
colors=['red', 'orange', 'yellow', 'green', 'blue', 'purple']
for i in range(180):
    t.forward(i+1)
    t.right(15)
    t.color(colors[i%6])

colors=['black','gray']
for i in range(50):
     t.circle(100, 360)
     t.left(8)
     t.color(colors[i%2])

t.speed(15)
colors=['green', 'blue', 'purple']
for i in range(300):
    t.forward(i+1)
    t.right(10)
    t.color(colors[i%3])

colors=('red','orange','yellow','green','blue','purple','pink')
t.speed(15)
for i in range(100):
    t.color(colors[i%7])
    t.forward(i*4)
    t.left(150)
    t.width(5)

colors=('red','orange','yellow','green','blue','purple','pink')
t.speed(15)
for i in range(100):
    t.color(colors[i%7])
    t.forward(i*4)
    t.left(150)
    t.width(5)

t.done()