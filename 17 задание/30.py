f = open("17-9.9.txt")
a = [int(x) for x in f]
mina = [x for x in a if x%100==25]
mina=min(mina)
res=[]
for i in range(len(a)-2):
    if (10<=a[i]<=99)+(10<=a[i+1]<=99)+(10<=a[i+2]<=99)==1:
        s = a[i]+a[i+1]+a[i+2]
        if s<mina:
            res.append(s)
print(len(res),max(res))