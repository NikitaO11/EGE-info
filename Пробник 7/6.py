from turtle import*
screensize(10000,10000)
tracer(0)
k=15
for i in range(2):
    forward(5*k)
    left(90)
    backward(13*k)
    left(90)
penup()
backward(10*k)
right(90)
forward(9*k)
left(90)
pendown()
for i in range(2):
    forward(11*k)
    right(90)
    forward(7*k)
    right(90)
penup()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*k,y*k)
        dot(3)
done()