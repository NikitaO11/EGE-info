from ipaddress import*
k=0
net = ip_network("253.112.169.12/255.255.254.0",0)
for ad in net:
    a = bin(int(ad))[2:]
    a1 = a[0:16].count("1")
    a2 = a[16:32].count("1")
    print(a1,a2)
    if a2>=a1:
        k+=1
print(k)
