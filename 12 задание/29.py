k=0
for n in range(200,1000):
    s = "1"*n
    while "111" in s or "222" in s:
        s = s.replace("111","22",1)
        s = s.replace("222","1",1)
    if (sum(map(int,s))/len(s)) == 1:
        print(n)
        break