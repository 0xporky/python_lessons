#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

if __name__ == '__main__':

    inp, out = argv[1:]

    ignore = ['duplex', 'alias', 'Current configuration']
    with open(inp, 'r') as f:
        lines = [line for line in f.read().split('\n')
                 if reduce(lambda x, y: x + int(y in line), ignore, 0) > 0]

    with open(out, 'w') as f:
        f.writelines(lines)
