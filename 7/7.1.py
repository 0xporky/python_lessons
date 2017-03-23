#!/usr/bin/env python
# -*- coding: utf-8 -*-

access_dict = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17,
    'FastEthernet0/17': 150,
}


def generate_access_config(access):
    access_template = [
        'switchport mode access',
        'switchport access vlan',
        'switchport nonegotiate',
        'spanning-tree portfast',
        'spanning-tree bpduguard enable'
    ]

    result = []
    for key, value in access.iteritems():
        result.append(key)
        for tmp in access_template:
            if access_template.index(tmp) == 1:
                result.append(' '.join([tmp, str(value)]))
            else:
                result.append(tmp)

    return result

if __name__ == '__main__':
    print(generate_access_config(access_dict))
