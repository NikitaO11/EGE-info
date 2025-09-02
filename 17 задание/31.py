f = open("17-19.txt")
a = [int(x) for x in f]
res = []
for k in range(len(a)-1):
    for n in range(k+1,len(a)):
        if (abs(a[k])%3==0)+(abs(a[n])%3==0)>=1:
            s = a[k]+a[n]
            res.append(s)
print(len(res),max(res))
