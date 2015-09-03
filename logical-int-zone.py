#!/usr/bin/python

import sys
from getpass import getpass
from jnpr.junos import Device
from pprint import pprint

hostname = '192.168.2.254'
username = raw_input('username: ')
passwd = getpass('password: ')
intname = raw_input('find zone of interface: ')

dev = Device(host=hostname, user=username, password=passwd)
dev.open()

int = dev.rpc.get_interface_information(interface_name=intname)

print "name: %s zone: %s" % (int.findtext('logical-interface/name'), int.findtext('logical-interface/logical-interface-zone-name'))

dev.close()
