from ipaddress import*
for x in range(0,256):
    net = ip_network(f"254.127.{x}.9/255.255.240.0",0)
    for ad in net:
        a = bin(int(ad))[2:]
        l = a[0:16].count("1")
        r = a[16:32].count("1")
        if l<r:
            break
    else:
        print(x)
