from fnmatch import*
for i in range(0,10**8+1,2321):
    if fnmatch(str(i),"1*2??76"):
        print(i,i//2321)