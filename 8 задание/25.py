from itertools import*
k=0
for x in product("АНДРЕЙ",repeat=7):
    s="".join(x)
    if s.count("А")==1 and s.count("Й")==1:
        if s[0]!="Й":
            k+=1
print(k)