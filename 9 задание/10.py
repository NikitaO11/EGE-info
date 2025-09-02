f = open("дз1.txt")
k=0
for i in f:
    a = sorted(list(map(int,i.split())))
    s1 = a[0]+a[3]
    s2 = a[1]+a[2]
    if s1<s2:
        k+=1
print(k)
