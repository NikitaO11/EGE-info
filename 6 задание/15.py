from turtle import*
tracer(0)
screensize(10000,10000)
k=15
for i in range(2):
    right(120)
    forward(7*k)
right(300)
for i in range(2):
    right(120)
    forward(7*k)
penup()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*k,y*k)
        dot(3)
done()