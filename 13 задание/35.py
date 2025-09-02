from ipaddress import*
for x in range(251,256):
    try:
        net = ip_network(f"255.112.128.136/255.255.{x}.0",0)
        for ad in net:
            a = bin(int(ad))[2:]
            l = a[0:16]
            r = a[16:32]
            if l.count("1")<r.count("1"):
                break
        else:
            print(x)
    except:
        pass