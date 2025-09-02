from itertools import *
k=0
for x in permutations("ПЕСКАРЬ"):
    s="".join(x)
    s = s.replace("Е","А").replace("Р","А")
    if s[0]!="Ь" and "ЬА" not in s:
        k+=1
print(k)