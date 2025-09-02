for n in range(100,1000):
    n = str(n)
    n1 = int(n[0])*int(n[1])
    n2 = int(n[1])*int(n[2])
    if n1>=n2:
        s = str(n2)+str(n1)
    else:
        s = str(n1)+str(n2)
    if s == "615":
        print(s,n)