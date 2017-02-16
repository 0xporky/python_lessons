config = "switchport trunk allowed vlan 1,3,10,20,30,100"

c_list = config.split(' ')[-1::][0].split(',')
print(c_list)
