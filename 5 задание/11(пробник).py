for n in range(0,1000):
    n2=bin(n)[2:]
    if sum(map(int,n2))%2==0:
        n2 = "10" + n2[2:] + "0"
    else:
        n2 = "11" + n2[2:] + "1"
    r= int(n2,2)
    if r<20:
        print(n,r)