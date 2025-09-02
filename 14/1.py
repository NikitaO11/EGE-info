def f(n):
    s=""
    while n>0:
        s = str(n%5) + s
        n=n//5
    return s

x = 125 + 25**3 + 5**9
print(f(x).count("0"))