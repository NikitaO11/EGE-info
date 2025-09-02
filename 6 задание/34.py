from turtle import*
tracer(0)
screensize(10000,10000)
k=50
right(90)
for i in range(3):
    right(45)
    forward(10*k)
    right(45)
right(315)
forward(10*k)
for i in range(2):
    right(90)
    forward(10*k)
penup()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*k,y*k)
        dot(3)
done()