def f(n):
    s=""
    while n>0:
        s = str(n%25)+s
        n//=25
    return s

x = 3*3125**8+2*625**7-4*625**6+3*125**5-2*25**4-2025
print(f(x).count("0"))
