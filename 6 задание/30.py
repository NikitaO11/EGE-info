from turtle import*
tracer(0)
screensize(10000,10000)
k=30
for i in range(4):
    forward(10*k)
    right(270)
penup()
forward(3*k)
right(270)
forward(5*k)
right(90)
pendown()
for i in range(2):
    forward(10*k)
    right(270)
    forward(12*k)
    right(270)
penup()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*k,y*k)
        dot(3)
done()
