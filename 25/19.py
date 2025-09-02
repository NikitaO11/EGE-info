from fnmatch import*
for i in range(0,10**9+1,33847):
    if fnmatch(str(i),"2*1?71") and i%1991==0 and i%17==0:
        print(i,i//1991)