from itertools import *
k=0
for x in permutations("КОЛУН"):
    s="".join(x)
    s=s.replace("Н","К").replace("Л","К").replace("У","О")
    if "КК" not in s and "ОО" not in s:
        k+=1
print(k)