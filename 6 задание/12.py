from turtle import*
from math import sqrt
tracer(0)
screensize(10000,10000)
k=100
right(60)
for i in range(4):
    forward(8*k)
    right(120)
    forward(4*k)
    right(240)
right(120)
forward(2*k)
right(90)
forward((16*sqrt(3))*k)
right(90)
forward(2*k)
penup()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*k,y*k)
        dot(3)
done()
