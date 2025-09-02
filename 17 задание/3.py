f = open("17-3.txt")
a = [int(x) for x in f]
res=[]
prom=[]
for i in range(len(a)-1):
    if (abs(a[i])%10==7 and a[i]%3==0) or (abs(a[i+1])%10==7 and a[i+1]%3==0):
        prom.append(a[i])
        prom.append(a[i+1])
        res.append(a[i]+a[i+1])
print(len(res),min(prom))