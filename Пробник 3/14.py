def f(n):
    s=""
    while n>0:
        s = str(n%5)+s
        n//=5
    return s
res=[]
for x in range(1,2501):
    a=(5**100)-x
    ans = f(a)
    null = int(str(ans).count("0"))
    if null == 4:
        print(x)


