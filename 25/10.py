from fnmatch import*
for i in range(0,10**8+1,2024):
    if fnmatch(str(i),"1?4*784"):
        print(i,i//2024)