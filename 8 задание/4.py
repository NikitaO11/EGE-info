from itertools import *
k=0
for x in product("АНИМЕ", repeat=4):
    s="".join(x)
    k+=1
for x in product("АНИМЕ", repeat=5):
    s="".join(x)
    k+=1
for x in product("АНИМЕ", repeat=6):
    s="".join(x)
    k+=1
print(k)