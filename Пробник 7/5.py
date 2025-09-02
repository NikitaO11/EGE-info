for n in range(1000000):
    n2 = bin(n)[2:]
    if n%2==0:
        n2 = n2 + n2[-2:]
    if n%2!=0:
        n2 = "1" + n2 + "0"
    r = int(n2,2)
    if r==202:
        print(n)