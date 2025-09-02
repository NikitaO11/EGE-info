f = open("17.txt")
a = [int(x) for x in f]
maxa = [x for x in a if x%100==19]
maxa = max(maxa)
res=[]
for i in range(len(a)-2):
    if (1000<=a[i]<=9999)+(1000<=a[i+1]<=9999)+(1000<=a[i+2]<=9999)==2:
        if (a[i]%3==0)+(a[i+1]%3==0)+(a[i+2]%3==0)>=1:
            s = a[i]+a[i+1]+a[i+2]
            if s>maxa:
                res.append(s)
print(len(res),max(res))