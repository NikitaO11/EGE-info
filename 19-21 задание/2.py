def f(a,b,m):
    if a+b>=45: return m%2==0
    if m==0: return 0
    h = [f(a+1,b,m-1), f(a*3,b,m-1 ), f(b+1,a,m-1), f(b*3,a,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
print("19)", [s for s in range(1,40) if f(4,s,2)])
print("20)", [s for s in range(1,40) if not f(4,s,1) and f(4,s,3)])
print("21)", [s for s in range(1,40) if not f(4,s,2) and f(4,s,4)])