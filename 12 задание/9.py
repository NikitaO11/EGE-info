summax=0
for n in range(4,10000):
    s="4" + "8" * n
    while "48" in s or "588" in s or "888" in s:
        if "48" in s:
            s=s.replace("48","8",1)
        if "588" in s:
            s=s.replace("588","84",1)
        if "888" in s:
            s=s.replace("888","5",1)
    sum = 4*s.count("4")+5*s.count("5") + 8*s.count("8")
#     if sum>summax:
# #         summax=sum
# # print(summax)
    summax=max(summax,sum)
print(summax)