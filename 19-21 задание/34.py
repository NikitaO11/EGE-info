def f(a,b,m):
    if a*b>=144: return m%2==0
    if m==0: return 0
    h = [f(a+1,b,m-1),f(a*2,b,m-1),f(a,b+1,m-1),f(a,b*2,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
print("1)",[s for s in range(1,141) if f(3,s,2)])
print("2)",[s for s in range(1,141) if not f(3,s,1) and f(3,s,3)])
print("3)",[s for s in range(1,141) if not f(3,s,2) and f(3,s,4)])