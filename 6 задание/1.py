# Повтори 9 [Вперёд 50 Направо 90 Вперёд 35 Направо 90]
# Поднять хвост
# Вперёд 5 Направо 90 Вперёд 10 Направо 90
# Опустить хвост
# Повтори 4 [Вперёд 35 Направо 90 Вперёд 17 Направо 90]
# Определите, сколько точек с целочисленными координатами будут находиться внутри объединения фигур,
# ограниченных заданными алгоритмом линиями, включая точки на границах этого объединения.
from turtle import*
count = 0
for x in range(36):
    for y in range(18):
        count += 1
count1 = 0
for x in range(36):
    for y in range(51):
        count1 += 1
count2 = 0
for x in range(6):
    for y in range(11):
        count2 += 1
b=count+count1-count2
print(b)
k=20
tracer(0)
screensize(5000,5000)
for i in range(9):
    forward(50*k)
    right(90)
    forward(45*k)
    right(90)
penup()
forward(5*k)
right(90)
forward(10*k)
right(90)
pendown()
for i in range(4):
    forward(35*k)
    right(90)
    forward(17*k)
    right(90)
penup()
for x in range(-20,81):
    for y in range(-80,30):
        goto(x*k,y*k)
        dot(3)
done()

