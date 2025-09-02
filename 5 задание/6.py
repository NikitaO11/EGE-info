a=[]
for n in range(1,100):
    n2=bin(n)[2:]
    if n % 2 != 0:
        n2 = "1" + n2 + "11"
    else:
        n2 = "11" + n2 + "00"
    r=int(n2,2)
    if r<127:
        a.append(r)
print(a)
print(f'max:{max(a)}')


