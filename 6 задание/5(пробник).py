# Повтори 9 [Вперёд 29 Направо 90 Вперёд 17 Направо 90]
# Поднять хвост
# Вперёд 5 Направо 90 Вперёд 1 Налево 90
# Опустить хвост
# Повтори 9 [Вперёд 64 Направо 90 Вперёд 48 Направо 90]
from turtle import*
k=20
tracer(0)
screensize(10000,10000)
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
for x in range(-10,40):
    for y in range(-40, 20):
        goto(x*k,y*k)
        dot(3)
done()

