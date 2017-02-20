NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
res = list(NAT.partition('FastEthernet'))
res[1] = 'GigabitEthernet'
print(''.join(res))
