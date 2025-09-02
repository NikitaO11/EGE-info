f = open("24re_3.txt").readline()
f = f.replace("D"," ").replace("E"," ")
while " " in f:
    f = f.split(" ")
print(len(max(f,key=len)))