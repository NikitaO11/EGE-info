from fnmatch import*
for i in range(0,10**8,122):
    if fnmatch(str(i),"3??54*34") and bin(i)[2:].count("1")<=10:
        print(i,i//122)
