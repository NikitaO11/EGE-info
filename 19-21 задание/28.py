def f(a,b,m):
    if a+b>=67: return m%2==0
    if m==0: return 0
    h = [f(a+b,b,m-1),f(a,a+b,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
print("1)", [s for s in range(1,67) if f(12,s,1)])
print("2)", [m for m in range(1,10) if f(15,14,m)])
print("3)", [m for m in range(1,10) if f(2,4,m)])
