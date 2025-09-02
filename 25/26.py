from fnmatch import*
for i in range(31,10**9,31):
    if fnmatch(str(i),"12345?7?8"):
        print(i,i//31)