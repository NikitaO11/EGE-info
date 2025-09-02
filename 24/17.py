s = open("24_2_7.txt").readline()
s = s.replace("XZZY","XZZ ZZY")
s = s.split()
print(len(max(s,key=len)))