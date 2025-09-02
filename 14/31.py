def f(n):
    s=""
    while n>0:
        s  = str(n%7)+s
        n//=7
    return s
for x in range(1000):
    m = 343 ** 5 + 7 ** 3 - 1 - x
    m = f(m)
    if m.count("6")==12:
        print(x)
        break