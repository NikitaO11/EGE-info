f = open("Дз10.txt")
k=0
for a in f:
    if a.count("E")>a.count("A"):
        k+=1
print(k)
