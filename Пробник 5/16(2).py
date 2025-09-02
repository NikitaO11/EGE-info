f=[0]*15000
for n in range(15000):
    if n==1:
        f[n] = 3
    if n>1:
        f[n] = 2*n+5 + f[n-1]
print(f[3026]-f[3024])