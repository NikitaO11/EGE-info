for n in range(1,100):
    n3=n2=bin(n)[2:]
    n2 = n2 + n2[-1]
    if n3.count("1") % 2 ==0:
        n2 += "0"
    else:
        n2 += "1"
    if n2.count("1") % 2 == 0:
        n2 += "1"
    else:
        n2 +="0"
    r=int(n2,2)
    if r>90:
        print(n,r)