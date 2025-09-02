def f(n):
    s=""
    while n>0:
        s = str(n%4)+s
        n//=4
    return s
x=16**18*4**10-4**6-16
print(f(x).count("3"))