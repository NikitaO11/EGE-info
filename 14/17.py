def f(n):
    s = ""
    while n>0:
        s = str(n%3)+s
        n//=3
    return s

x = 9**11*3**20-3**9-27
print(f(x).count("2"))