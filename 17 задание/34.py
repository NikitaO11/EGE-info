f = open("17-22.txt")
a = [int(x) for x in f]
maxa=max(a)
res = []
for i in range(len(a)-2):
    if (a[i]%10==3)+(a[i+1]%10==3)+(a[i+2]%10==3)==0:
        s = a[i]**2+a[i+1]**2+a[i+2]**2
        if s>maxa:
            res.append(s)
print(len(res),min(res))
