f = open("24re_4.txt").readline()
f = f.replace("12","1 2").replace("21","2 1")
f = f.split(" ")
print(len(max(f,key=len)))