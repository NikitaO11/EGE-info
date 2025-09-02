f = open("24re_5.txt").readline()
f = f.replace("A"," ").replace("E"," ")
f = f.split(" ")
print(len(max(f,key=len)))