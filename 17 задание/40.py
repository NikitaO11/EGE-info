f = open("17_17530.txt")
a = [int(x) for x in f]
res=[]
mina = min(a)
for i in range(len(a)-1):
    if (a[i]%55==mina)+(a[i+1]%55==mina)>=1:
        s = a[i]+a[i+1]
        res.append(s)
print(len(res),min(res))