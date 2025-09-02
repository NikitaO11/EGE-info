from itertools import *
k=0
a=0
for x in product(sorted("КОМПЬЮТЕР"), repeat=5):
    s="".join(x)
    k+=1
    if k%2!=0 and s[0]!="Ь" and s.count("К")==2:
        a+=1
        print(k,s,a)