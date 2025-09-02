from itertools import*
k=0
for x in product("ЛЕМУР",repeat=4):
    s="".join(x)
    if s.count("М")==1 and s[0]=="М":
        k+=1
print(k)