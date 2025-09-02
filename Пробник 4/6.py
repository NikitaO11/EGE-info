from turtle import*
tracer(0)
screensize(10000,100000)
k=15
for i in range(5):
    forward(30*k)
    right(90)
    forward(40*k)
    right(90)
penup()
forward(20*k)
right(90)
forward(5*k)
right(90)
pendown()
for i in range(7):
    forward(10*k)
    right(90)
penup()
for x in range(-30,70):
    for y in range(-70,30):
        goto(x*k,y*k)
        dot(3)
done()