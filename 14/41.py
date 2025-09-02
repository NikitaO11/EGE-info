def f(n):
    s=""
    while n>0:
        s = str(n%5)+s
        n//=5
    return s

x = 125+25**3+5**9
x1 = f(x)
print(f(x).count("0"))