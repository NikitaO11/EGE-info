s = open("24_23dosr.txt").readline()
s = s.replace("C","B").replace("D","B")
mt,t=0,1
for i in range(len(s)-1):
    if s[i]=="B" and s[i+1]=="B":
        t=1
    else:
        t+=1
        mt=max(mt,t)
print(mt)

while "BB" in s:
    s = s.replace("BB","B B")
s = s.split(" ")
print(len(max(s,key=len)))

