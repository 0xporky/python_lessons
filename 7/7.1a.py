#!/usr/bin/env python
# -*- coding: utf-8 -*-

access_dict = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17,
    'FastEthernet0/17': 150,
}


def generate_access_config(access, psecurity=False):
    access_template = [
        'switchport mode access',
        'switchport access vlan',
        'switchport nonegotiate',
        'spanning-tree portfast',
        'spanning-tree bpduguard enable'
    ]

    port_security = [
        'switchport port-security maximum 2',
        'switchport port-security violation restrict',
        'switchport port-security'
    ]

    result = []
    for key, value in access.iteritems():
        result.append(key)
        for tmp in access_template:
            if access_template.index(tmp) == 1:
                result.append(' '.join([tmp, str(value)]))
            else:
                result.append(tmp)

        if psecurity is True:
            for p in port_security:
                result.append(p)

    return result

if __name__ == '__main__':
    print(generate_access_config(access_dict))
    print(generate_access_config(access_dict, psecurity=True))
