f = open("9_pr.txt")
k=0
for i in f:
    a = sorted(map(int,i.split()))
    if a[3]<a[0]+a[1]+a[2]:
        if a[0]!=a[1]!=a[2]!=a[3]:
            k+=1
    print(k)

