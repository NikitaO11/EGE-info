from fnmatch import*
for i in range(1921,10**8+1,1921):
    if fnmatch(str(i),"2*1?5?1"):
        print(i,i//1921)