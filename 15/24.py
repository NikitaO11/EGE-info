def f(a,x):
    return ((x&42==0) <= (x&51!=0)) <= (x&a!=0)

for a in range(1000):
    if all(f(a,x) for x in range(10000)):
        print(a)
        break