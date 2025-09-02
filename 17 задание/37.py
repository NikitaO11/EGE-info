f = open("17-24.txt")
a = [int(x) for x in f]
even = [x for x in a if x%2==0]
arif = sum(even)/len(even)
res=[]
for i in range(len(a)-1):
    if (a[i]%3==0 and a[i+1]<arif) or (a[i]<arif and a[i+1]%3==0):
        s = a[i]+a[i+1]
        res.append(s)
print(len(res),max(res))
