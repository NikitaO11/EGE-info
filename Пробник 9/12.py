for n in range(4,100):
    s = "3"+"5"*n
    while "25" in s or "355" in s or "555" in s:
        if "25" in s:
            s = s.replace("25","5",1)
        if "355" in s:
            s = s.replace("355","52",1)
        if "555" in s:
            s = s.replace("555","3",1)
    if s.count("5")==len(s):
        print(n)