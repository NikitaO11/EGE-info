def f(n):
    s=""
    while n>0:
        s = str(n%3)+s
        n//=3
    return s

for n in range(1000):
    n2 = f(n)
    if n%3==0:
        n2 = "1"+n2+"02"
    if n%3!=0:
        ost = f((n%3)*4)
        n2 = n2+str(ost)
    r = int(n2,3)
    if r<199:
        print(n)

