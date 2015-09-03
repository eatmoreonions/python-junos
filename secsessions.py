#!/usr/bin/python

import sys
from getpass import getpass
from jnpr.junos import Device

hostname = '192.168.2.254'
username = raw_input('username: ')
passwd = getpass('password: ')

dev = Device(host=hostname, user=username, password=passwd)
dev.open()

int = dev.rpc.get_utmd_status()

print "%s" % int.findtext('utmd-status')

dev.close()
