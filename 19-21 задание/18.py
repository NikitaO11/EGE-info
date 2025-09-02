def f(s,m):
    if 20<=s<=30: return m%2==0
    if s>30: return m%2!=0
    if m==0: return 0
    h = [f(s+1,m-1),f(s*2,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
print("1" , [s for s in range(1,20) if f(s,1)])
print("2" , [m for m in range(1,5) if f(18,m)])
print("3" , [m for m in range(1,5) if f(19,m)])
print("4" , [m for m in range(1,5) if f(16,m)])
print("5" , [m for m in range(1,8) if f(9,m)])
print("6" , [m for m in range(1,9) if f(8,m)])
print("7" , [m for m in range(1,9) if f(7,m)])