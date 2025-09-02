for n in range(100):
    n2 = bin(n)[2:]
    s = sum(map(int,n2))
    n2 = n2 + str(s%2)
    s2 = sum(map(int,n2))
    n2 = n2+str(s2%2)
    r = int(n2,2)
    if r>137:
        print(n)
        break