def f(n):
    s=""
    while n>0:
        s = str(n%6)+s
        n//=6
    return s

for x in range(10000):
    v = 216**5+6**3-1-x
    m = f(v)
    if m.count("5")==12:
        print(x)
        break
