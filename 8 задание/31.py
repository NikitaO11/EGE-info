from itertools import*
k=0
for x in sorted(product("АОУ",repeat=5)):
    s = "".join(x)
    k+=1
    if k==101:
        print(s)
