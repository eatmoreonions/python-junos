#!/usr/bin/python

import sys
from getpass import getpass
from jnpr.junos import Device
from jnpr.junos.op.phyport import *
from pprint import pprint

devlist = ['10.1.100.21']
username = raw_input('username: ')
passwd = getpass('password: ')

for hostname in devlist:
#  sys.stdout.write('connecting to %s ... ' % hostname)
#  sys.stdout.flush()

  dev = Device(host=hostname, user=username, password=passwd)
  dev.open()
  ports = PhyPortTable(dev).get()
  print "Port,Status,Flapped"
  for port in ports:
    print("%s,%s,%s" % (port.key, port.oper, port.flapped))

  dev.close()
