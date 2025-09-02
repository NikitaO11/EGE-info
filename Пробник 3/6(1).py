from turtle import *
c = 15
left(90)
tracer(0)
for _ in range(4):
    forward(16*c)
    right(90)
    forward(22*c)
    right(90)
up()
forward(5*c)
right(90)
forward(5*c)
left(90)
down()
for _ in range(4):
    forward(57*c)
    right(90)
    forward(75*c)
    right(90)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*c,y*c)
        dot(3, "blue")
exitonclick()
update()