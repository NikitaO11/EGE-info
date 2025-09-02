f = open("17-20.txt")
a = [int(x) for x in f]
sqrt=[]
for n in range(1,101):
    b = n**2
    sqrt.append(b)
res=[]
for i in range(len(a)-1):
    if a[i] in sqrt or a[i+1] in sqrt:
        s = a[i]+a[i+1]
        res.append(s)
print(len(res),min(res))
