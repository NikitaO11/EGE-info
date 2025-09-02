for n in range(1,100):
    n2 = bin(n)[2:]
    n3 = n2 + str(int(n2.count("1"))%2)
    n3 = n3 + str(int(n3.count("1"))%2)
    r = int(n3,2)
    if r>137:
        print(r,n)