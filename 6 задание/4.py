from turtle import*
k=50
tracer(0)
screensize(10000,10000)
for i in range(12):
    begin_fill()
    forward(5*k)
    fillcolor("red")
    right(90)
    forward(3*k)
    fillcolor("red")
    right(90)
    forward(2*k)
    fillcolor("red")
    right(90)
penup()
for x in range(-30,30):
    for y in range(-30,30):
        setpos(x*k,y*k)
        dot(3)
done()

