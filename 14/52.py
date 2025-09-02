def f(n):
    s=""
    while n>0:
        s = str(n%7)+s
        n//=7
    return s
for x in range(2031):
    m = 7**170+7**100-x
    if f(m).count("0")==71:
        print(x)
        