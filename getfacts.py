#!/usr/bin/python

import sys
from getpass import getpass
from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable
from pprint import pprint

devlist = ['192.168.2.254']
username = raw_input('username: ')
passwd = getpass('password: ')

for hostname in devlist:
  dev = Device(host=hostname, user=username, password=passwd)
  dev.open()
  pprint(dev.facts['hostname'] + " uptime " + dev.facts['RE0']['up_time'])
  dev.close()
