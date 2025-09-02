from ipaddress import*
for mask in range(33):
    net1 = ip_network("193.175.175.231/"+str(mask),0)
    net2 = ip_network("193.175.176.118/" + str(mask), 0)
    if net1!=net2:
        print(net1.netmask)
