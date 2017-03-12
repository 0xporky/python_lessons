#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    tmp = [
        'Protocol:',
        'Prefix:',
        'AD/Metric:',
        'Next-Hop:',
        'Last update:',
        'Outbound Interface:']

    with open('ospf.txt', 'r') as f:
        for line in f:
            ospf_list = [x for x
                         in line.replace(',', '').split(' ')
                         if len(x) > 1]
            ospf_list.insert(0, 'OSPF')

            for t, o in zip(tmp, ospf_list):
                print('{:25}{}'.format(t, o))

            print('\n\n')
