from fnmatch import*
for i in range(2024,10**8,2024):
    if fnmatch(str(i),"1?4*784"):
        print(i,i//2024)