f = open("дз6.txt")
k=0
for q in f:
    a = sorted(list(map(int,q.split())))
    a1 = [x for x in a if a.count(x)==1]
    if ((a[0]+a[5])/2)>((a[1]+a[2]+a[3]+a[4])/4):
        if len(a1)==6:
            k+=1
print(k)
