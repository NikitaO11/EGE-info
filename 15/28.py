from itertools import*
def f(x):
    b = 74<=x<=194
    c = 152<=x<=223
    a = a1<=x<=a2
    return ((not(a)) and b) <= (b <= (not(c)))
Ox = [i/4 for i in range(60*4,230*4)]
m=[]
for a1,a2 in combinations(Ox,2):
    if all(f(x)==1 for x in Ox):
        s = a2-a1
        m.append(s)
print(min(m))