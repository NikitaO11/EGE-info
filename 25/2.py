from fnmatch import*
for i in range(0,10**8+1,3123):
    s = str(i)
    if fnmatch(s,"3?1*57") and i%3123==0:
        print(i,i//3123)