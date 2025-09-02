def f(n):
    s=""
    while n>0:
        s = str(n%3)+s
        n//=3
    return s
maxr=0
for x in range(1,2031):
    m = 3**100-x
    if f(m).count("0")>=maxr:
        maxr=f(m).count("0")
        a=x
print(maxr,a)