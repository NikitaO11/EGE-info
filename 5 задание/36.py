for n in range(100):
    n2 = bin(n)[2:]
    n2 = n2.replace("0","00").replace("1","11")
    r = int(n2,2)
    if r>32:
        print(r)
        break