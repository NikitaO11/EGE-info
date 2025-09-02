for n in range(1,100000):
    n2=bin(n)[2:]
    n2 = n2.replace("1", "2").replace("0", "1").replace("2","0")
    c=int(n2)
    r=int(n2,2)
    r1=n-r
    if r1==979:
        print(n,r1)