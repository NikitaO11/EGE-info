def f(n):
    s=""
    while n>0:
        s = str(n%3)+s
        n//=3
    return s
res=[]
for x in range(1,100):
    n2 = f(x)
    if x%3==0:
        n2 = n2+n2[-2:]
    else:
        n1 = f((x%3)*5)
        n2 = n2 + n1
    r =int(n2,3)
    if r<=242:
        res.append(r)
print(max(res))