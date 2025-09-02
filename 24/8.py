f = open("24_8.txt")
s = f.readline()
print(s.count("XVI"))
k=0
for i in range(len(s)-1):
    if s[i]=="X" and s[i+1]=="V" and s[i+2]=="I":
        k+=1
print(k)