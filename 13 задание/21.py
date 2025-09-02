from ipaddress import*
for mask in range(33):
    net = ip_network("99.148.161.94/"+str(mask),0)
    if net.network_address==ip_address("99.148.160.0"):
        print(bin(int(net.netmask))[2:].count("0"))
