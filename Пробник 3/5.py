def f(n):
    s=""
    while n>0:
        s = str(n%3)+s
        n//=3
    return s
for n in range(1,100):
    n2 = f(n)
    if n%3==0:
        n2 = n2 + n2[-2:]
    else:
        sum3 = sum(map(int,n2))
        n2 = n2 + str(f(sum3))
    r = int(n2,3)
    if r > 220 and r%2==0:
        print(n,r)