from itertools import*
k=0
for x in product("0123456789ABCDE",repeat=5):
    s="".join(x)
    if s[0]!="0":
        if s.count("8")==1:
            s = s.replace("B","A").replace("C","A").replace("D","A").replace("E","A")
            if s.count("A")>2:
                k+=1
print(k)