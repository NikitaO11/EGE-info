from itertools import*
k=0
for x in permutations("КАБИНЕТ",7):
    s="".join(x)
    if s[0]!="Б" and "ЕА" not in s:
        k+=1
print(k)
