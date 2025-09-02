from itertools import*
k=0
for x in product("01234567",repeat=5):
    s="".join(x)
    if s[0]!="0":
        if s[0]=="1" or s[0]=="3" or s[0]=="5" or s[0]=="7":
            if s.count("7")<=2 and (s[-1]=="2" or s[-1]=="6"):
                k+=1
print(k)