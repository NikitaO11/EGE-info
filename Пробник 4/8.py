from itertools import*
k=0
for x in product("012345",repeat = 6):
    s="".join(x)

    if s.count("0")==1 and s[0]!="0":
        if ("10" not in s) and ("01" not in s) and ("30" not in s) and ("03" not in s) and ("50" not in s) and ("05" not in s):
            k+=1
            print(s,k)