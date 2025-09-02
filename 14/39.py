def f(n):
    s = ""
    while n>0:
        s = str(n%7)+s
        n//=7
    return s
for x in range(25000000,30000000):
    m = 4*7**24+6*7**13+5*49**4+2*343**2+10-x
    z = f(m)
    if z.count("6")>z.count("0"):
        print(x)
