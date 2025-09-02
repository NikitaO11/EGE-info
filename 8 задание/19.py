from itertools import*
k=0
for x in product("ЛЕТО", repeat = 4):
    s="".join(x)
    if s[0]=="Л" or s[0]=="Т":
        k+=1
print(k)