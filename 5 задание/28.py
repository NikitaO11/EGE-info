for n in range(100):
    n2 = bin(n)[2:]
    n2 = n2[::-1]
    r = int(n2,2)
    if r ==7:
        print(n)