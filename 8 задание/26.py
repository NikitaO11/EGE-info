from itertools import*
k=0
for x in sorted(product("МАНГУСТ",repeat=6)):
    s="".join(x)
    k+=1
    if s[0]!="А" and s.count("М")==2 and s.count("У")<=1:
        print(k,s)