def f(a,m):
    if a>=97: return m%2==0
    if m==0: return 0
    h = [f(a+3,m-1),f(a+5,m-1),f(a*3,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
print("19", [a for a in range(1,97) if not f(a,1) and f(a,2)])
print("20", [a for a in range(1,97) if not f(a,1) and f(a,3)])
print("21", [a for a in range(1,97) if f(a,4) and not f(a,2)])