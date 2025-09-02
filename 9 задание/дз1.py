f = open("дз1.txt")
k=0
for i in f:
    a = sorted(list(map(int,i.split())))
    if (a[0]+a[3])<(a[1]+a[2]):
        k+=1
print(k)
