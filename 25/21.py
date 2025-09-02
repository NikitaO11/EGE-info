def f(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
k=0
for n in range(2943444,2943529+1):
    k+=1
    if f(n) == True:
        print(n,k)