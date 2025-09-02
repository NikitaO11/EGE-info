def f(x):
    a = 80<=x<=90
    b = 30<=x<=50
    c = 10<=x<=n
    return ((not a)<=b) and ((not c)<=a)
ox = [i for i in range(0,10000+1)]
k=0
for n in range(10,1000):
    for x in ox:
        if f(x)==1:
            k+=1
        else:
            break
    if k>=25:
        print(n)

