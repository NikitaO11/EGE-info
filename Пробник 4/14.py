def f(n):
    s = ""
    while n > 0:
        s = str(n % 9) + s
        n = n // 9
    return s
res=[]
for x in range(1,5770):
    a=(9**2025)+(9**1000)-x
    ans = f(a)
    if ans.count("0")==1026:
        res.append(x)
print(max(res))

