#!/usr/bin/python

import yaml
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.factory import loadyaml

from getpass import getpass
hostname = raw_input('hostname or address: ')
username = raw_input('username: ')
passwd = getpass('password: ')

dev = Device(hostname, user=username, password=passwd)

dev.open()
dev.timeout = 60

globals().update( loadyaml('showinterface.yml'))
interface_table = ShowInterface(dev)
interface_table.get()
formatter = "{0:<24}{1:<24}{2:<24}{3:<24}{4:<24}{5:<24}{6:<24}"

for i in interface_table:
  if "ge" in i.name or "fe" in i.name or "vlan" in i.name:
    if i.addrfamily == 'inet' and i.status == 'up':
      ints = formatter.format(i.name, i.status, i.linkmode, i.linkspeed, i.logicalname, i.addrfamily, i.logicalinetaddr)
      print ints

dev.close()
