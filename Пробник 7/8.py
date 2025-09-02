from itertools import*
k=0
for x in product("0123456",repeat=6):
    s = "".join(x)
    if s[0]!="0":
        if s.count("3")==1 and ("13" not in s) and ("31" not in s) and ("15" not in s) and ("51" not in s) and ("35" not in s) and ("53" not in s) and ("11" not in s)\
                and ("33" not in s) and ("55" not in s):
            k+=1
            print(s,k)



