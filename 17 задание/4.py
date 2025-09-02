f = open("17-4.txt")
a = [int(x) for x in f]

max3=max([x for x in a if x%3==0])

res = []
for i in range(len(a)-1):
    if (a[i]%3==0)+(a[i+1]%3==0)>=1:
        s = a[i]+a[i+1]
        if s<=max3:
            res.append(s)
print(len(res),max(res))