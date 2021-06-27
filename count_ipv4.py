import ipaddress
def ips_between(ip1,ip2):
    return int(ipaddress.IPv4Address(ip2)) - int(ipaddress.IPv4Address(ip1))

'''
def ipsBetween(s,e): #Ipv4
    if s == e : return 0
    s,e,n=s.split('.'),e.split('.'),0
    for i in range(len(s)):
        if s[i]  < e[i]:    n+=int(e[i])
        elif s[i] == e[i] and n>0:  n+=255
        elif s[i]>e[i]: n+=255-int(s[i])
    return n'''



print(ips_between("20.0.0.10", "20.0.1.0"))
