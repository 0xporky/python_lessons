#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    mac = ['aabb:cc80:7000',
           'aabb:dd80:7340',
           'aabb:ee80:7000',
           'aabb:ff80:7000']
    mac_cisco = [ x.replace(':', '.') for x in mac ]
    print(mac_cisco)
