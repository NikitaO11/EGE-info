from itertools import*
k=0
for x in sorted(product("СВЕТА",repeat=5)):
    s = "".join(x)
    k+=1
    if s == "СВЕТА":
        print(k)