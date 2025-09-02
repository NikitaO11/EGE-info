f = open("17-7.7.txt")
a = [int(x) for x in f]
maxa = [x for x in a if x%171==0]
maxa=max(maxa)
res=[]
for i in range(len(a)-1):
    if a[i]<maxa or a[i+1]<maxa:
        if (a[i]%2==0)+(a[i+1]%2==0)>=1:
            s = a[i]+a[i+1]
            res.append(s)
print(len(res),max(res))