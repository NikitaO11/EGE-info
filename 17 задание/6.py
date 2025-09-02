f = open("17-6.txt")
a = [int(x) for x in f]
res  = []
for i in range(len(a)-1):
    if (a[i]%5==0)+(a[i+1]%5==0)==2:
        s = a[i]+a[i+1]
        res.append(s)
print(len(res),max(res))
