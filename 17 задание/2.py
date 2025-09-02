f = open("17-2.txt")
a = [int(x) for x in f]
res=[]
for i in range(len(a)-1):
    if (a[i]%10==0 and a[i+1]%13!=0) or (a[i+1]%10==0 and a[i]%13!=0):
        s=a[i]+a[i+1]
        res.append(s)
print(len(res),max(res))