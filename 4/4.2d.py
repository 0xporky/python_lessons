#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    london_co = {
        'r1': {
            'location': '21 New Globe Walk',
            'vendor': 'Cisco',
            'model': '4451',
            'ios': '15.4',
            'ip': '10.255.0.1'
        },
        'r2': {
            'location': '21 New Globe Walk',
            'vendor': 'Cisco',
            'model': '4451',
            'ios': '15.4',
            'ip': '10.255.0.2'
        },
        'sw1': {
            'location': '21 New Globe Walk',
            'vendor': 'Cisco',
            'model': '3850',
            'ios': '3.6.XE',
            'ip': '10.255.0.101',
            'vlans': '10,20,30',
            'routing': True
        }
    }

    device_name = raw_input('Enter device name: ')
    device_dict = london_co.get(device_name)
    keys = ','.join(device_dict.keys())
    dev_parameter = raw_input('Enter device parameter ({}): '.format(keys))
    print(device_dict.get(dev_parameter.lower(), 'No parameter'))
