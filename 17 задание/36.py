f = open("17-23.txt")
a = [int(x) for x in f]
res=[]
max3=[]
for i in range(len(a)-2):
    if (bin(a[i])[2:].count("1")==2)+(bin(a[i+1])[2:].count("1")==2)+(bin(a[i+2])[2:].count("1")==2)==3:
        s = a[i]+a[i+1]+a[i+2]
        res.append(s)
        max3.append(max(a[i],a[i+1],a[i+2]))
print(len(res),sum(max3))

