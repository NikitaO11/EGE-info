b1 = {2,5,10,15,17,20,22,25}
c1 = {2,4,6,8,10,12,15,16,20,25}
def f(a,b,c):
    return (b==a and c) <= (c==a and b)
for a in range(10000):
    if all(f(a,b,c) for b in b1 for c in c1):
        print(a)