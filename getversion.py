#!/usr/bin/python

import sys
from getpass import getpass
from jnpr.junos import Device
from pprint import pprint

devlist = ['10.1.100.22']
username = raw_input('username: ')
passwd = getpass('password: ')

for hostname in devlist:
  dev = Device(host=hostname, user=username, password=passwd)
  dev.open()
  pprint(dev.facts['hostname'] + " " + dev.facts['model'] + " " + dev.facts['version'])
  dev.close()
