def f(n):
    s=""
    while n>0:
        s = str(n%5)+s
        n//=5
    return s
x = 5**36+5**24-25
print(f(x).count("4"))