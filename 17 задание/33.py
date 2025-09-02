f = open("17-21.txt")
a = [int(x) for x in f]
maxa = [x for x in a if 10000<=x<=99999 and x%10==3]
maxa=max(maxa)
res = []
for i in range(len(a)-2):
    if (abs(a[i])%10==3)+(abs(a[i+1])%10==3)+(abs(a[i+2])%10==3)>=1:
        s = a[i]+a[i+1]+a[i+2]
        if s<=maxa:
            res.append(s)
print(len(res),max(res))
