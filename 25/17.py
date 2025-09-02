from fnmatch import*
for i in range(0,10**10,2023):
    if fnmatch(str(i),"1?2139*4") and sum(map(int,str(i)))%2!=0:
        print(i,i//2023)