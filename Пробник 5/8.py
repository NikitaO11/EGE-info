from itertools import*
k=0
for x in product("012345678",repeat=5):
    s="".join(x)
    if s.count("3")==2 and s[0]!="0":
        if ("13" not in s) and ("31" not in s) and ("33" not in s) and ("53" not in s) and ("35" not in s)\
                and ("73" not in s) and ("37" not in s):
            k+=1
            print(k,s)