from itertools import*
k=0
for x in product(sorted("ПАМЯТЬ"), repeat = 5):
    s = ''.join(x)
    k+=1
    if k%2==0 and "Ь" not in s and s.count("Я")==2:
        print(k,s)