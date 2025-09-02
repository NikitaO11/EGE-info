f = open("Дз6.txt").readline()
f = f.replace("O","A").replace("D","C").replace("F","C")
f = f.replace("CCA","1")
f = f.replace("C","A")
f = f.replace("A"," ")
f = f.split(" ")
print(len(max(f,key=len)))

