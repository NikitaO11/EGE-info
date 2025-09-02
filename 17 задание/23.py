f = open("17-1.2.txt")
a = [int(x) for x in f]
maxa = [x for x in a if abs(x)%3]
maxa = max(maxa)
res=[]
for i in range(len(a)-1):
    if (abs(a[i])%3==0)+(abs(a[i+1])%3==0)>=1:
        s = a[i]+a[i+1]
        if s<=maxa:
            res.append(s)
print(len(res),max(res))