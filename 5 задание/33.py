for n in range(100,1000):
    n2 = str(n)
    s = int(n2[0])*int(n2[1])
    s1 = int(n2[1])*int(n2[2])
    if s>=s1:
        res = str(s1)+str(s)
    else:
        res = str(s)+str(s1)
    if res=="615":
        print(n)