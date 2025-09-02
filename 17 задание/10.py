f = open("17-10.txt")
a = [int(x) for x in f]
res=[]
k=0
for i in range(len(a)-2):
    if a[i]<a[i+1]<a[i+2]:
        k+=1
        s = a[i+2]-a[i]
        res.append(s)
print(k,min(res))