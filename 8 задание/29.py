from itertools import*
k=0
for x in product("0123456789AB",repeat=5):
    s="".join(x)
    if s[0]!="0":
        s = s.replace("A","9").replace("B","9")
        if s.count("9")<=3 and s.count("7")==1:
            k+=1
            print(k)