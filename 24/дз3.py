f = open("Дз3.txt").readline()
while "QQ" in f:
    f = f.replace("QQ","Q Q")
f = f.split(" ")
print(len(max(f,key=len)))
