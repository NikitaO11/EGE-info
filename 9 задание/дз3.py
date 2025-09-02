f = open("дз3.txt")
k=0
for i in f:
    a = sorted(list(map(int,i.split())))
    a2 = [x for x in a if a.count(x)==2]
    if (a[0]+a[1]+a[2])>a[3] and len(a2)==2:
        k+=1
print(k)
