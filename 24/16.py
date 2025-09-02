s = open("24_2_6.txt").readline()
s = s.replace("GDE","*").replace("GED","*")
s = s.replace("E","G").replace("D","G")
s =s.split("G")
print(len(max(s,key=len)))



