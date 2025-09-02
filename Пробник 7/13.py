from ipaddress import*
k=0
num = ip_network("192.168.32.96/255.255.255.224",0)
for ad in num:
    ed = bin(int(ad))[2:].count("1")
    if ed%2==0:
        k+=1
print(k)