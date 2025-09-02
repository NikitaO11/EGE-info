from turtle import*
tracer(0)
screensize(10000,10000)
k=30
for i in range(2):
    forward(13*k)
    right(90)
    forward(20*k)
    right(90)
penup()
forward(8*k)
right(90)
backward(3*k)
left(90)
pendown()
for i in range(2):
    forward(16*k)
    right(90)
    forward(8*k)
    right(90)
penup()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*k,y*k)
        dot(3)
done()