for n in range(1,101):
    n2 = bin(n)[2:]
    if int(n2)%2==0:
        n2 = n2.replace("1","11")
    if int(n2)%2!=0:
        n2 = n2.replace("0","00")
    r = int(n2,2)
    if r>70:
        print(r,n)
        break