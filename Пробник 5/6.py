from turtle import*
screensize(10000,10000)
tracer(0)
k=15
for i in range(3):
    forward(33*k)
    right(90)
    forward(30*k)
    right(90)
penup()
forward(9*k)
right(90)
forward(6*k)
left(90)
pendown()
for i in range(2):
    forward(40*k)
    right(90)
    forward(40*k)
    right(90)
penup()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*k,y*k)
        dot(3)
done()


