def f(s,m):
    if 42<=s<=74: return m%2==0
    if s>74: return m%2!=0
    if m==0: return 0
    h = [f(s+1,m-1),f(s*2,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
print("1", [s for s in range(1,42) if f(s,1)])
print("2", [m for m in range(1,5) if f(38,m)])
print("3", [m for m in range(1,5) if f(39,m)])
print("4", [m for m in range(1,5) if f(40,m)])
print("5", [m for m in range(1,5) if f(19,m)])
print("5", [m for m in range(1,5) if f(20,m)])
print("6", [m for m in range(1,8) if f(18,m)])


