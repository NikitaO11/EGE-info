def cc(x):
    s = ""
    d="0123456789ab"
    while x>0:
        s = d[x%12] + s
        x = x // 12
    return s
a=[]
for n in range(12,200):
    n2 = cc(n)
    if n%12 == 0:
        n2 = n2 + n2[-2] + n2[-1]
    else:
        n2 = n2 + cc(n%12*9)
    r=int(n2,12)
    if r>300:
        a.append(r)
        print(n,r)
print(min(a))

