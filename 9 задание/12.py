f = open("дз3.txt")
k=0
for q in f:
    a = sorted(list(map(int,q.split())))
    a1 = [x for x in a if a.count(x)==2]
    if a[3]<(a[0]+a[1]+a[2]):
        if len(a1)==2:
            k+=1
print(k)