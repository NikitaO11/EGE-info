from fnmatch import*
for i in range(0,10**8,3123):
    if fnmatch(str(i), "3?1*57"):
        if bin(i)[2:].count("1")<11:
            print(i)