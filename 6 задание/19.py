from turtle import*
tracer(0)
screensize(10000,10000)
k=15
for i in range(9):
    forward(22*k)
    right(90)
    forward(6*k)
    right(90)
penup()
forward(1*k)
right(90)
forward(5*k)
left(90)
pendown()
for i in range(9):
    forward(53*k)
    right(90)
    forward(75*k)
    right(90)
penup()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*k,y*k)
        dot(3)
done()