f = open("Дз11.txt")
k=0
for a in f:
    if a.count("YZ")>1:
        k+=1
print(k)