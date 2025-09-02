def f(n):
    s=""
    while n>0:
        s = str(n%5)+s
        n//=5
    return s
x =5**2019-5**1019+25**600-125
print(f(x).count("4"))