f = open("9-9.txt")
k = 0
c=0
for i in f:
    a = sorted(list(map(int,i.split())))
    a1 = [x for x in a if a.count(x)==2]
    a2 = [x for x in a if a.count(x)==1]
    c+=1
    if len(a1)==2 and len(a2)==4:
        if a1[0]>=sum(a2)/len(a2):
            k+=1
    print(c,k,a)
