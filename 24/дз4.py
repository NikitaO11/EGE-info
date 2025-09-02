f = open("Дз4.txt").readline()
# f = f.replace("W"," ").replace("R"," ").replace("Q"," ")
# f = f.split(" ")
# print(len(max(f,key=len)))
mt,t=0,0
for i in range(len(f)):
    if f[i]=="W" or f[i]=="R" or f[i]=="Q":
        t=0
    else:
        t+=1
        mt=max(mt,t)
print(mt)