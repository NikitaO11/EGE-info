from ipaddress import*
for mask in range(33):
    net1 = ip_network("157.127.182.76/"+str(mask),0)
    net2 = ip_network("157.127.190.80/" + str(mask), 0)
    if net1 == net2:
        print(mask)