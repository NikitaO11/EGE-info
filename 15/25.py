def f(a,x):
    return ((x%a==0) <= (x%54==0) or x%130==0) and a>60
for a in range(1,10000):
    if all(f(a,x) for x in range(10000)):
        print(a)
        break
