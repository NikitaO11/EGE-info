f = open("9-5.txt")
k=0
for i in f:
    a = sorted(list(map(int,i.split())))
    a1 = [x for x in a if a.count(x)==2]
    a2 = [x for x in a if a.count(x)==1]
    if a[3]<a[0]+a[1]+a[2]:
        if len(a2) == 2 and len(a1)==2:
            k+=1
    print(k)
