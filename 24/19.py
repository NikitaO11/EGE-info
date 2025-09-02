s = open("24_2_9.txt").readline()
s = s.replace("W","X").replace("V","X")\
    .replace("Y","X").replace("Z","X")
while "XXX" in s:
    s = s.replace("XXX", "XX XX")
s = s.split()
print(len(max(s,key=len)))
# mt,t=0,2
# for i in range(len(s)-2):
#     if s[i]=="X" and s[i+1]=="X" and s[i+2]=="X":
#         t=2
#     else:
#         t+=1
#         mt = max(mt,t)
# print(mt)


