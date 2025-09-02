from itertools import *
k=0
for x in set(permutations("АССАСИН")):
    s="".join(x)
    k+=1
print(k)