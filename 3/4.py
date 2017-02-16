command1 = "switchport trunk allowed vlan 1,3,10,20,30,100"
command2 = "switchport trunk allowed vlan 1,3,100,200,300"


set1 = set(command1.split(' ')[-1::][0].split(','))
set2 = set(command2.split(' ')[-1::][0].split(','))

print(set1 & set2)
