f = open("24_30.txt")
k=0
for s in f:
    if s.count("YZ") >=2:
        k+=1
print(k)