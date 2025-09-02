from ipaddress import*
k=0
net = ip_network("192.168.32.48/255.255.255.240",0)
for ad in net:
    a = bin(int(ad))[2:].count("1")
    if a%2!=0:
        k+=1
print(k)