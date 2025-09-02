f = [0]*35000
for n in range(35000):
    if n<10:
        f[n]=n*n
    if n>=10:
        f[n]=(n-1)*f[n-2]
print((f[34652] - 250 * f[34650]) / f[34648])