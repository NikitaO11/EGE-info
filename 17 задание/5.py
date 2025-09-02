f = open("17-5.txt")
a = [int(x) for x in f]
res = []
for i in range(len(a)-1):
    if (a[i]%3==0)+(a[i+1]%3==0)>=1:
        s = a[i]+a[i+1]
        if s%5==0:
            res.append(s)
print(len(res),max(res))