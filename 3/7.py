MAC = "AAAA:BBBB:CCCC"
res = ' '.join('{:08b}'.format(int(x, base=16)) for x in MAC.replace(':', ''))
print(res)
