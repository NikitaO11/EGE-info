f = open("дз7.txt")
k=0
for q in f:
    a = sorted(list(map(int,q.split())))
    a1 = [x for x in a if a.count(x)==3]
    a2 = [x for x in a if a.count(x)==1]
    if len(a1)==3 and len(a2)==4:
        if (sum(a2)/4)<=a1[1]:
            k+=1
print(k)