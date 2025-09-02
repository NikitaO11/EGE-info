from ipaddress import*
k=0
net = ip_network("172.16.176.0/255.255.240.0",0)
for ad in net:
    ed = bin(int(ad)).count("1")
    if ed%3==0:
        k+=1
print(k)