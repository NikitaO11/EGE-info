from turtle import*
tracer(0)
screensize(10000,10000)
k=15
right(300)
for i in range(6):
    forward(5*k)
    right(120)
    forward(5*k)
    right(330)
penup()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*k,y*k)
        dot(3)
done()