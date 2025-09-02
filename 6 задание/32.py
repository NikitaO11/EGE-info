from turtle import*
tracer(0)
screensize(10000,10000)
k=30
for i in range(2):
    forward(14*k)
    right(90)
    forward(10*k)
    right(90)
penup()
forward(8*k)
right(90)
backward(4*k)
left(90)
pendown()
for i in range(2):
    forward(9*k)
    right(90)
    forward(8*k)
    right(90)
penup()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*k,y*k)
        dot(3)
done()