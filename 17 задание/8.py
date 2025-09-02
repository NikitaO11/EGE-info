from math import*
f = open("17-8.txt")
a = [int(x) for x in f]
res = []
k=0
k1=0
res1=[]
for i in range(len(a)-1):
    if a[i]>=0 and sqrt(a[i])==isqrt(a[i]):
        k+=1
        s = a[i]+a[i+1]
        res.append(s)
    if a[i+1]>=0 and sqrt(a[i+1])==isqrt(a[i+1]):
        k1+=1
        s1=a[i]+a[i+1]
        res1.append(s1)
a=max(res)
b=max(res1)
print((k+k1),max(a,b))

