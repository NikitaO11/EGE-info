for n in range(1,10):
    n2=bin(n)[2:]
    if n2.count("1")%2==0:
        n2= n2 + "10"
        if n2[:2] == "10":
            n3 = "01" + n2[2:]
        else:
            n3 = "00" + n2[2:]
    if n2.count("1")%2!=0:
        n2 = n2 + "11"
        if n2[:2] == "10":
            n3 = "01" + n2[2:]
        else:
            n3 = "00" + n2[2:]
    r = int(n3,2)
    if r >43:
         print(n3,r,n)

