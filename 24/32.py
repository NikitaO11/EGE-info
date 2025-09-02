f = open("24re_2.txt").readline()
f = f.replace("Z"," ")
while " " in f:
    f = f.split(" ")
print(len(max(f,key=len)))
