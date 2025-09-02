from turtle import*
tracer(0)
screensize(10000,10000)
k=15
for i in range(9):
    forward(29*k)
    right(90)
    forward(17*k)
    right(90)
penup()
forward(5*k)
right(90)
forward(1*k)
left(90)
pendown()
for i in range(9):
    forward(64*k)
    right(90)
    forward(48*k)
    right(90)
penup()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*k,y*k)
        dot(3)
done()