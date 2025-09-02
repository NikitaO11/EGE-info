def f(n):
    s=""
    while n>0:
        s = str(n%3)+s
        n//=3
    return s
res=[]
for n in range(1,1000):
    n2 = f(n)
    if n%3==0:
        n2 = "1"+n2+"02"
    else:
        n2 = n2 + f((n%3)*4)
    r=int(n2,3)
    if r<199:
        res.append(n)
print(max(res))