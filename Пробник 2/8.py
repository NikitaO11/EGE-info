from itertools import*
k=0
for x in product("012345678", repeat=5):
    s="".join(x)
    if s[0]!="1" and s[0]!="3" and s[0]!="5" and s[0]!="7" \
            and s[-1]!="1" and s[-1]!="2" and s.count("8")>=2:
        k+=1
print(k)