f = open("24_01.txt")
k=0
for s in f:
    if s.count("E")>s.count("A"):
        k+=1
print(k)