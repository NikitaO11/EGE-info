def prost(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return True
    return False
for n in range(2943444,2943529+1):
    if prost(n)==False:
        print(n)