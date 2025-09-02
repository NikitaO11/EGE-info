f = open("24re_6.txt")
k=0
for i in f:
    for m in range(len(i)-2):
        if i[m]=="F" and i[m+2]=="O":
            k+=1
            break
print(k)
