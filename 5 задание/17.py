for i in range(100,1000):
    i = str(i)
    n1=int(i[0])*int(i[1])
    n2 = int(i[1]) * int(i[2])
    if n1>=n2:
        s = str(n1)+str(n2)
    else:
        s = str(n2)+str(n1)
    if s=="123":
        print(s,i)
