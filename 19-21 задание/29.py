def f(a,m):
    if a==0: return m%2==0
    if m==0: return 0
    h = [f(a-any(b),m-1)]
    return h if (m-1)%2==0
b=[]
for i in range(1,11):
    b.append(i)
print([m for m in range(1,10) if f(20,m)])


