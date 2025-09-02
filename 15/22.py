def f(a,x):
    return ((x & 42!=0) and (x&34==0)) <= (not(x & a==0))

for a in range(0,10000):
    if all(f(a,x) for x in range(1000)):
        print(a)
        break