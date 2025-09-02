for n in range(100,1000):
    n2 = str(n)
    s = int(n2[0])*int(n2[1])
    s2 = int(n2[1])*int(n2[2])
    res = str(s2)+str(s)
    if res=="123":
        print(n)
        break
