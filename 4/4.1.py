inp = str(raw_input('Enter net ip in format "10.1.1.0/24": '))
inp_list = inp.split('/')

net_ip = inp_list[0]
net_mask = inp_list[1]

print('Network:')
print(''.join(('{:<10}'.format(x) for x in net_ip.split('.'))))

bit_string = (('1' * int(net_mask)+('0' * 32)))[:32]
bit_list = [bit_string[i:i+8] for i in range(0, 32, 8)]

print('\nMask:')
print(''.join('{:<10}'.format(int(x, 2)) for x in bit_list))
print(''.join('{:<10}'.format(x) for x in bit_list))
