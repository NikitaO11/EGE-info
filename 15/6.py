from itertools import*
def f(x):
    p = 34<=x<=64
    q = 74<=x<=94
    a = a1<=x<=a2
    return a<=(p==q)
ox = [i/4 for i in range(4*4,91*4+1)]
m=[]
for a1,a2 in combinations(ox,2):
    if all(f(x)==1 for x in ox):
        s = a1,a2
        m.append(s)
print(m)