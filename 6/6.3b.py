#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    with open('CAM_table.txt', 'r') as f:
        lines = [line for line in f.read().split('\n')
                 if '.' in line]

    vlan = str(raw_input('Enter vlan number: '))
    vlan_lines = [line for line in lines if vlan in line]
    for line in vlan_lines:
        print(line)

    if len(vlan_lines) == 0:
        print('No such vlan')
