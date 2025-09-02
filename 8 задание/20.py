from itertools import*
k=0
for x in product("СЛОН", repeat = 5):
    s="".join(x)
    if s.count("С")==1:
        k+=1
print(k)