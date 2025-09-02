from itertools import*
def f(x):
    p = 8<=x<=12
    q = 4<=x<=30
    a = a1<=x<=a2
    return (p==q)<=(not a)
ox = [i/4 for i in range(0*4,55*4+1)]
m=[]
for a1,a2 in combinations(ox,2):
    if all(f(x)==1 for x in ox):
        m.append(a2-a1)
print(max(m))