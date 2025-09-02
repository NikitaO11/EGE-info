def f(n):
    s=""
    while n>0:
        s = str(n%7)+s
        n//=7
    return s


a=-1
for x in range(1,2031):
    n = 7**170+7**100-x
    m = f(n)
    if m.count("0")>=a:
        a=m.count("0")
        b=x
print(b)