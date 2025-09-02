s = open("24_2_1.txt").readline()
s = s.replace("R","W").replace("Q","W")
mt,t=0,0
for i in range(len(s)):
    if s[i]=="W":
        t=0
    else:
        t+=1
        mt=max(mt,t)
print(mt)

s=s.split("W")
print(len(max(s,key=len)))

