from itertools import*
k=0
for x in sorted(product("УЧЕНИК",repeat=3)):
    s = "".join(x)
    k+=1
    if s[0]=="К":
        k+=1
print(k)