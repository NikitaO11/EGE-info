def f(n):
    s=""
    while n>0:
        s = str(n%5)+s
        n//=5
    return s
mx=0
for x in range(1,2031):
    m = 7**150-7**100-x
    if f(m).count("0")>=mx:
        mx = f(m).count("0")
        sym=x
print(sym)

