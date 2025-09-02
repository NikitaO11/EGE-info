for n in range(1,430):
    n2 = bin(n)[2:]
    if n2.count("1")%2==0:
        n2 = "10" + n2[2:] + "0"
    else:
        n2 = "11" + n2[2:] + "1"
    r = int(n2,2)
    if r>40:
        print(r,n)
        break