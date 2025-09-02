f = open("дз7.txt")
k=0
for i in f:
    a = sorted(list(map(int,i.split())))
    a1 = [x for x in a if a.count(x)==3]
    a2 = [x for x in a if a.count(x)==1]
    if len(a1)==3 and len(a2)==4:
        if (sum(a2)/4)<=a1[0]:
            k+=1
print(k)