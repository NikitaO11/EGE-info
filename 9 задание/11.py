f = open("дз2.txt")
k=0
for q in f:
    a = list(map(int,q.split()))
    found=False
    for i in range(4):
        if (sum(a)-a[i])%2!=0:
            found = True
    if found:
        k+=1
print(k)