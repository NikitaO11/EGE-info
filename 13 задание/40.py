from ipaddress import*
for mask in range(33):
    net1 = ip_network(f"118.187.59.255/{mask}",0)
    net2 = ip_network(f"118.187.65.115/{mask}", 0)
    if net1!=net2:
        print(mask)
