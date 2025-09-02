s = open("24_08.txt").readline()
k=0
for i in range(len(s)-2):
    if s[i]<=s[i+1]<=s[i+2]:
        k+=1
print(k)
s = open("24_08.txt").readline()
for i in range(len(s)-1,-1,-1):
    if s[i]>=s[i-1]>=s[i+2]:
        print(i-2)
        break
