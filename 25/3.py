from fnmatch import*
for i in range(0,10**10,2024):
    if fnmatch(str(i),"3?2758*4"):
        print(i)