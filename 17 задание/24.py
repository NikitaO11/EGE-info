f = open("17_1.3.txt")
a = [int(x) for x in f]
maxa = [x for x in a if x%10==2]
maxa=max(maxa)
res=[]
for i in range(len(a)-1):
    if (a[i]%10==0)+(a[i+1]%10==0)==1:
        s = a[i]+a[i+1]
        if s<maxa:
            res.append(s)
print(len(res),min(res))