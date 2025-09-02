for n in range (0,100):
    n2=bin(n)[2:]
    n3= n2 + str((sum(map(int,n2))%2))
    n4= n3 + str((sum(map(int,n3))%2))
    r=int(n4,2)
    if r>80:
        print(n,r)

