from itertools import*
k=0
for x in product("ДЕЖЗ",repeat=4):
    s = "".join(x)
    if s.count("Д")==1:
        k+=1
print(k)