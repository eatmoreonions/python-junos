#!/usr/bin/python

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.factory import loadyaml

from getpass import getpass
host = raw_input('hostname or address: ')
username = raw_input('username: ')
passwd = getpass('password: ')

globals().update( loadyaml('showinterface.yml'))

dev = Device(host, user=username, password=passwd)
#dev = Device(hostname, user=username, password=passwd)

dev.open()
dev.timeout = 60

interface_table = ShowInterface(dev)
interface_table.get()

for i in interface_table:
  if "ge" in i.name or "fe" in i.name or "vlan" in i.name:
    if i.addrfamily == 'inet' and i.status == 'up':
      print str(i.logicalname) +  " " + str(i.logicalinetaddr)
#      print i.name + " " + str(i.description) + " " + str(i.linkmode) + " " + str(i.linkspeed) + " " + str(i.logicalname) + " " + str(i.logicalinetaddr)

dev.close()
