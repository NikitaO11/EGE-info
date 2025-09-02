def f(n):
    s=""
    while n>0:
        s = str(n%7)+s
        n//=7
    return s
x = 49**7+7**21-7
print(f(x).count("6"))