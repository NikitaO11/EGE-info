for n in range(1000):
    s = "2" + "5" * n
    while "25" in s or "355" in s or "555" in s:
        s = s.replace("25","5",1)
        s = s.replace("355", "25", 1)
        s = s.replace("555", "3", 1)
    if sum(map(int,s))==17:
        print(n)
        break