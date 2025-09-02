f = open("ПРОБНИК_9.txt")
k=0
for i in f:
    a =sorted((map(int,i.split())))
    k+=1
    x1=[x for x in a if a.count(x)==2]
    x2=[x for x in a if a.count(x)==1]
    if len(x1)==2:
        if x1[0]>(sum(x2)//4):
            print(k,a)
