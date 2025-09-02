def f(a,m):
    if a<=19: return m%2==0
    if m==0: return 0
    h = [f(a-2,m-1),f(a-5,m-1),f(a//3,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
print("1)",[s for s in range(20,101) if not f(s,1) and f(s,2)])
print("2)",[s for s in range(20,101) if not f(s,1) and f(s,3)])
print("3)",[s for s in range(20,101) if f(s,4) and not f(s,2)])