from turtle import*
tracer(0)
screensize(10000,10000)
k=40
for i in range(8):
    right(45)
    forward(8*k)
penup()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*k,y*k)
        dot(3)
done()
