from itertools import*
def f(x):
    p = 54<=x<=84
    q = 64<=x<=94
    a = a1<=x<=a2
    return a<=(p==q)
Ox = [i/4 for i in range(24*4,95*4+1)]
m=[]
for a1,a2 in combinations(Ox,2):
    if all(f(x)==1 for x in Ox):
        s = a1,a2
        m.append(s)
print(m)