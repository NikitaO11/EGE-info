from itertools import*
k=0
for x in sorted(product("ТЕОРИЯ",repeat=6)):
    s = "".join(x)
    k+=1
    if k%2!=0 and s[0] not in "ЕОР" and s.count("Т")==1:
        print(k)
