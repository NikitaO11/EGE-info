f = open("24_4.txt")
s = f.readline()
mt,t=0,0
for i in range(len(s)):
    if s[i]=="A" or s[i]=="B" or s[i]=="C":
        t+=1
        mt = max(mt,t)
    else:
        t=0
print(mt)

s = s.replace("D","E")
s = s.split("E")
print(len(max(s,key=len)))