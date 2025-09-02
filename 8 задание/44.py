from itertools import*
k=0
for x in sorted(product("ПАРУС",repeat=6)):
    s = "".join(x)
    k+=1
    if s.count("У")==1 and "АУ" not in s and "УА" not in s:
        print(k)