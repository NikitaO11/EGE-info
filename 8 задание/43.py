from itertools import*
k=0
for x in product("012345678",repeat=5):
    s="".join(x)
    if s.count("1")==1 and s[0]!="0":
        if "01" not in s and "10" not in s and "21" not in s and "12" not in s and "41" not in s and \
                "14" not in s and "61" not in s and "16" not in s and "81" not in s and "18" not in s:
            k+=1
print(k)