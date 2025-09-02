for n in range(1,100):
    n2 = bin(n)[2:]
    n3 = n2+n2[-1]
    if n2.count("1")%2==0:
        n3 = n3+"0"
    else:
        n3 = n3+"1"
    if n3.count("1")%2==0:
        n3 = n3+"0"
    else:
        n3 = n3+"1"

    r=int(n3,2)
    if r>80:
        print(r)
        break
