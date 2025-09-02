from itertools import*
k=0
for x in sorted(product("КОФЕ",repeat=5)):
    s="".join(x)
    k+=1
    if s.count("E")==0 and s.count("Ф")==1:
        print(k)

