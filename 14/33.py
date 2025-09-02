def f(n):
    s = []
    while n>0:
        s += [n%9]
        n//=9
    sp = s[::-1]
    return sp
for x in range(5770):
    m = 9**2025+9**1000-x
    print(f(m))
    m = list(map(str,f(m)))
    if m.count("0")==1026:
        print(x)
