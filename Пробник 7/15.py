from itertools import*
def f(x):
    p = 24<=x<=90
    q = 47<=x<=115
    a = a1<=x<=a2
    return q<=((p and (not a))<=(not q))
Ox = [i/4 for i in range(22*4,120*4+1)]
m=[]
for a1,a2 in combinations(Ox,2):
    if all(f(x)==1 for x in Ox):
        s = a2-a1
        m.append(s)
print(min(m))