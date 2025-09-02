# #Повтори 9 [Вперёд 22 Направо 90 Вперед 6 Направо 90]
# Поднять хвост
# Вперед 1 Направо 90 Вперёд 5 Налево 90
# Опустить хвост
# Повтори 9 [Вперёд 53 Направо 90 Вперёд 75 Направо 90]
#
# Определите количество точек внутри пересечения фигур, учитывая точки на линиях пересечения.
from turtle import*
count = 0
for x in range(2):
    for y in range(22):
        count +=1
print(count)
k=15
screensize(10000,10000)
tracer(0)
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
        setpos(x*k,y*k)
        dot(3)
done()
