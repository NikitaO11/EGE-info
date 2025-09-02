def f(n):
    s = ""
    while n>0:
        s = str(n%6)+s
        n//=6
    return s
mx=-1
for x in range(1,2031):
    r = 62030 + 6100 - x
    m = f(r)
    if m.count("0")>=mx:
        mx = m.count("0")
        print(x)