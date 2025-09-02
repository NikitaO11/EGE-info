from itertools import*
k=0
for x in product("ЕГЭ", repeat = 5):
    s="".join(x)
    if s[0]=="Е" or s[0]=="Э":
        k+=1
print(k)
