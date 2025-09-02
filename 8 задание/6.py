from itertools import *
k=0
for x in product("ЖИРАФ", repeat=5):
    s="".join(x)
    if s[0]!="Ф" and s[-1]!="Р" and s.count("Ж")==1:
        k+=1
print(k)