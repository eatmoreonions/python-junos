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
#  sys.stdout.write('connecting to %s ... ' % hostname)
#  sys.stdout.flush()

  dev = Device(host=hostname, user=username, password=passwd)
  dev.open()

  ints = EthPortTable(dev).get()
  for int in ints:
    print("%s,%s" % (int.key, int.oper))

  dev.close()
