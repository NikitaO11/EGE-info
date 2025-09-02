from itertools import*
def f(x):
    p = 117<=x<=158
    q = 129<=x<=180
    a = a1<=x<=a2
    return p <= ((q and (not(a))) <= (not(p)))
Ox = [i/4 for i in range(100*4,200*4)]
m=[]
for a1,a2 in combinations(Ox,2):
    if all(f(x)==1 for x in Ox):
        s = a2-a1
        m.append(s)
print(min(m))
