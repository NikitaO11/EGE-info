f = open("17-8.8.txt")
a = [int(x) for x in f]
mina=min(a)
res=[]
for i in range(len(a)-1):
    if (a[i]%117==mina)+(a[i+1]%117==mina)>=1:
        s = a[i]+a[i+1]
        res.append(s)
print(len(res),max(res))