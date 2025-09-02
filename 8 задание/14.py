from itertools import *
k=0
a=0
for x in product(sorted("МАНГУСТ"), repeat=6):
    s="".join(x)
    k+=1
    if s[0]!="У" and s.count("М")==2 and s.count("Г")<=1:
        print(k)