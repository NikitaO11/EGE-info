for n in range(1,100):
    n2 = bin(n)[2:]
    if n%2==0:
        n2 = "10" + n2
    else:
        n2 = "1" + n2 +"01"
    r= int(n2,2)
    if r>441:
        print(r,n)
        break