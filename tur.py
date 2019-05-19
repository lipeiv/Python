import turtle
t=turtle.Pen()
for x in range(1,19):
    t.forward(100)
    if x % 2 == 0:
        t.left(175)
    else:
        t.left(225)
        
t.reset()
for x in range(1,20):
    t.forward(200)
    t.left(95)

t.reset()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)

t.reset()
for x in range(1,5):
    t.forward(50)
    t.left(90)

t.reset()
for x in range(1,9):
    t.forward(200)
    t.left(135)

t.reset()
for x in range(1,38):
    t.forward(200)
    t.left(175)
