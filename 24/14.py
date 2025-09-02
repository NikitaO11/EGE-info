s = open("24_2_4.txt").readline()
s = s.replace("O","N").replace("P","N")
mt,t=0,1
for i in range(len(s)-1):
    if s[i]=="N" and s[i+1]=="N":
        t=1
    else:
        t+=1
        mt = max(mt,t)
print(mt)

while "NN" in s:
    s = s.replace("NN","N N")
s = s.split()
print(len(max(s,key=len)))
