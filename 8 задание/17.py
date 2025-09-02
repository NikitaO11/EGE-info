from itertools import*
k=0
for x in product(sorted("УЧЕНИК"), repeat=3):
    s = "".join(x)
    k+=1
    if s[0]=="К":
        print(k)
        break