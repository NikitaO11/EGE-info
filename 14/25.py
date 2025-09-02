def f(n):
    s=""
    while n>0:
        s = str(n%3)+s
        n//=3
    return s
x = 3**2020-3**1020+9**800-81
print(f(x).count("2"))