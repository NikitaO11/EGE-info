f = open("дз5.txt")
k=0
for q in f:
    a = sorted(list(map(int,q.split())))
    a1 = [x for x in a if a.count(x)==1]
    if 2*(a[0]+a[4])>(a[1]+a[2]+a[3]):
        if len(a1)==5:
            k+=1
print(k)