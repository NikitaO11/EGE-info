f = open("24_1.txt")
s = f.readline()
mt,t=0,0
for i in range(len(s)):
    if s[i]=="C":
        t+=1
        mt = max(mt,t)
    else:
        t=0
print(mt)

s = s.replace("A"," ").replace("B"," ")
s=s.split(" ")
print(len(max(s,key=len)))