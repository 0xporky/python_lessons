P = '192.168.3.1'
L = P.split('.')

print(''.join('{:10}'.format(x) for x in L))
print(''.join('{:08b}  '.format(int(x)) for x in L))
