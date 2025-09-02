def f(s,m):
    if s>=27: return m%2==0
    if m==0: return 0
    h = [f(s+1,m-1),f(s+2,m-1),f(s*2,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
print("1",[s for s in range(1,27) if f(s,1)])
print("2",[s for s in range(1,27) if not f(s,1) and f(s,2)])
print("3",[s for s in range(1,27) if not f(s,1) and f(s,3)])
print("4",[s for s in range(1,27) if not f(s,2) and f(s,4)])
