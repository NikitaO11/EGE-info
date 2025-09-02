from turtle import*
from math import sqrt
tracer(0)
screensize(10000,10000)
k=30
right(30)
for i in range(10):
    forward(30*k)
    right(60)
    forward(30*k)
    right(120)
penup()
for x in range(-30,30):
    for y in range(-60,30):
        goto(x*k,y*k)
        dot(3)
done()