from itertools import*
def f(x):
    v1 = x[:13]
    v2 = x[-13:]
    if v1 == v2[::-1]:
        return 1
    else:
        return 0

k=0
for x in product("01234567",repeat=27):
    s ="".join(x)
    if (s[0]==s[-1]) and (s[1]==s[-2]) and (s[2]==s[-3]) and (s[3]==s[-4]) and s[0]!="0":
        if f(s)==1:
            k+=1
print(k/(10**9+7))







