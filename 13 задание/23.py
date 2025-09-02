from ipaddress import*
for x in range(0,256):
    net = ip_network("64.0." + str(x) + ".6/255.255.248.0",0)
    for ad in net:
        ed = bin(int(ad))[2:]
        l = ed[0:17].count("1")
        r = ed[17:33].count("1")
        if l>r:
            break
    else:
        print(x)
