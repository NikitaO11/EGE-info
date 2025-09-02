f = open("24_9.txt")
s = f.readline()
s = s.split(" ")
print(len(max(s,key=len)))
