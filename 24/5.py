f = open("24_5.txt")
s = f.readline()
k=0
print(s.count("KOT"))
for i in range(len(s)-2):
    if s[i]=="K" and s[i+1]=="O" and s[i+2]=="T":
        k+=1
print(k)