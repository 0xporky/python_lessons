MAC = "AAAA:BBBB:CCCC"
res = ' '.join(format(ord(x), 'b') for x in MAC.replace(':', ''))
print(res)
