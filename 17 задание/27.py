f = open("17_1.5.txt")
a = [int(x) for x in f]
maxa = [x for x in a if abs(x)%100==25]
maxa= max(maxa)
res=[]
for i in range(len(a)-2):
    if (1000<=abs(a[i])<=9999)+(1000<=abs(a[i+1])<=9999)+(1000<=abs(a[i+2])<=9999)>=2:
        s =a[i]+a[i+1]+a[i+2]
        if s<=maxa:
            res.append(s)
print(len(res),max(res))