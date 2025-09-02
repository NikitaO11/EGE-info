from itertools import*
k=0
c=0
for x in sorted(product("ДЕЛЬФИН",repeat=6)):
    s = "".join(x)
    k+=1
    if s[0]!="Ь" and s.count("Ф")==2:
        if k%2==0:
            c+=1
print(c)


