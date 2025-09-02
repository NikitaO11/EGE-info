from itertools import*
k=0
for x in product("012345678",repeat=5):
    s="".join(x)
    if s[0]!="0":
        if s.count("5")==1 and "51" not in s and "15" not in s and "25" not in s and "52" not in s and \
                "35" not in s and "53" not in s and "54" not in s and  "45" not in s:
            k+=1
print(k)