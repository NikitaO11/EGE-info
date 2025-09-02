f = open("17-15.txt")
a = [int(x) for x in f]
res=[]
v=0
for k in range(0,len(a)-2):
    for g in range(k+1,len(a)-1):
        for f in range(g+1,len(a)):
            if (a[k]%3==2) + (a[g]%3==2) + (a[f]%3==2)>=1:
                v+=1
                a1=a[k]+a[g]+a[f]
                res.append(a1)
print(v,min(res))