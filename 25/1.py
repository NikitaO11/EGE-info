from fnmatch import*
for i in range(1991,10**8+1,1991):
    s=str(i)
    if fnmatch(s,"2*1?71") and i%1991==0:
        print(i,i//1991)