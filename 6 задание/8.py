from turtle import*
tracer(0)
screensize(10000,10000)
k=30
for i in range(3):
    forward(7*k)
    right(90)
forward(10*k)
for i in range(3):
    left(90)
    forward(6*k)
penup()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*k,y*k)
        dot(3)
done()