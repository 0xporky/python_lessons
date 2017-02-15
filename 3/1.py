tmp = [
    'Protocol:',
    'Prefix:',
    'AD/Metric:',
    'Next-Hop:',
    'Last update:',
    'Outbound Interface:']

ospf_route = "O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

ospf_list = [x for x in ospf_route.replace(',', '').split(' ') if len(x) > 1]
ospf_list.insert(0, 'OSPF')

for t, o in zip(tmp, ospf_list):
    print('{:25}{}'.format(t, o))
