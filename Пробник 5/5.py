for n in range(1,100):
    n2=bin(n)[2:]
    if n%3==0:
        n2 = n2[-3:] + n2
    else:
        n2 = bin(3*(n%3))[2:] + n2
    r = int(n2,2)
    if r>92:
        print(n)
        break
