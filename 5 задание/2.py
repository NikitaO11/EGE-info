for n in range(1,1000):
    a=[]
    n2=bin(n)[2:]
    if n%2 == 0:
        n2= "10" + n2
    else:
        n2= "1" + n2 + "01"
    R = int(n2,2)
    if n<=12:
        print(R)


