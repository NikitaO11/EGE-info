from fnmatch import*
for i in range(98591,10**11+1,98591):
    if fnmatch(str(i),"123*45??1?"):
        print(i,i//98591)