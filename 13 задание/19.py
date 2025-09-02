from ipaddress import*
for mask in range(33):
    if ip_network("118.187.59.255/"+str(mask),0)!= ip_network("118.187.65.115/"+str(mask),0):
        print(mask)