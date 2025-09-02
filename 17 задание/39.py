f = open("17-26.txt")
a = [int(x) for x in f]
odd = [x for x in a if x%2!=0]
arif = sum(odd)/len(odd)
res=[]
for i in range(len(a)-2):
    if a[i]%3!=a[i+1]%3 and a[i]%3!=a[i+2]%3 and a[i+1]%3!=a[i+2]%3:
        if (a[i]<arif)+(a[i+1]<arif)+(a[i+2]<arif)==1:
            s = a[i]+a[i+1]+a[i+2]
            res.append(s)
print(len(res),max(res))
