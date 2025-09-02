for n in range(0,256):
    n2 = bin(n)[2:].zfill(8)
    n2 = n2.replace("0","2").replace("1","0")\
        .replace("2","1")
    r = int(n2,2)
    if (r-n)==113:
        print(r-n,r,n)