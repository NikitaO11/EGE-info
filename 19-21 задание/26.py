def f(a,b,m):
    if a+b<=30: return m%2==0
    if m==0: return 0
    h = [f(a-1,b,m-1),f((a+1)//2,b,m-1),f(a,b-1,m-1),f(a,(b+1)//2,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
print("1)",[s for s in range(13,100) if f(18,s,2)])
print("2)",[s for s in range(13,100) if not f(18,s,1) and f(18,s,3)])
print("3)",[s for s in range(13,100) if not f(18,s,2) and f(18,s,4)])
