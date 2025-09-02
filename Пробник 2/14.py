def f(n):
    s=""
    while n>0:
        s = s+str((n%3))
        n//=3
    return s
for x in range(1,2031):
    pres = 3**100-x
    if str(f(pres)).count("0")==5:
        print(x)
