def f(a,x):
    return (not(x%a==0) or not(x%2205==0) or x%2800==0)
for a in range(1,1000):
    if all(f(a,x) for x in range(1000000)):
        print(a)
        break