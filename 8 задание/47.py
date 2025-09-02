from itertools import*
k=0
for x in permutations("0123456789ABCDEF",3):
    s="".join(x)
    if s[0]!="0":
        s = str(s).replace("0", "2").replace("4", "2").replace("6", "2").replace("8", "2") \
            .replace("3", "1").replace("5", "1").replace("7", "1").replace("9", "1")\
            .replace("A","2").replace("C","2").replace("E","2") \
            .replace("B", "1").replace("D","1").replace("F","1")
        if "22" not in s and "11" not in s:
            k+=1
print(k)