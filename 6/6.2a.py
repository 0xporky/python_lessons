#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    ignore = ['duplex', 'alias', 'Current configuration']
    with open('config_sw1.txt', 'r') as f:
        lines = [line for line in f.read().split('\n')
                 if '!' not in line and
                 reduce(lambda x, y: x + int(y in line), ignore, 0) > 0]

    for line in lines:
        print(line)
