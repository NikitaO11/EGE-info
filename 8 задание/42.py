from itertools import*
k=0
for x in product("ВИШНЯ",repeat=6):
    s = "".join(x)
    if s.count("В")<=1:
        if s[0]!="Ш" and s[-1]!="И" and s[-1]!="Я":
            k+=1
print(k)