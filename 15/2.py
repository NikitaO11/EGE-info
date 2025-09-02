from binascii import a2b_qp
from itertools import*
def f(x):
    p = 10<=x<=25
    q = 0<=x<=12
    a = a1<=x<=a2
    return ((not a)<= (not p)) or q
Ox = [i/4 for i in range(0*4,41*4+1)]
m=[]
for a1,a2 in combinations(Ox,2):
    if all(f(x)==1 for x in Ox):
        s = a1,a2
        m.append(s)
print(m)
