def f(n):
    if n<=3: return n
    if n>3 and n%2==0: return n+3+f(n-1)
    if n>3 and n%2!=0: return n*n+f(n-2)
k=0
for n in range(1,1001):
    if f(n)%7==0:
        k+=1
print(k)