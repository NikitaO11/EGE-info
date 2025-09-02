from turtle import*
tracer(0)
screensize(10000,10000)
k=15
for i in range(4):
    for x in range(4):
        forward(6*k)
        right(90)
    forward(10*k)
    right(90)
    forward(3*k)
penup()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*k,y*k)
        dot(3)
done()