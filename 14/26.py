def f(n):
    s=""
    while n>0:
        s = str(n%5)+s
        n//=5
    return s
x = 125**300*5**300-25**70-100
print(f(x).count("4"))