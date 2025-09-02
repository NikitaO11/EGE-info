f = open("Дз5.txt").readline()
f = f.replace("N","O").replace("P","O")
while "OO" in f:
    f = f.replace("OO","O O")
f = f.split(" ")
print(len(max(f,key=len)))