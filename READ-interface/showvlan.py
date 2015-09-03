#!/usr/bin/python

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.factory import loadyaml

globals().update( loadyaml('showinterface.yml'))

from getpass import getpass
host = raw_input('hostname or address: ')
username = raw_input('username: ')
passwd = getpass('password: ')

#dev = Device(hostname, user=username, password=passwd)
dev = Device(host, user=username, password=passwd)

dev.open()
dev.timeout = 60

formatter = "{0:<10}{1:<12}{2:<7}{3:<5}{4:<8}{5:<15}"

interface_table = ShowInterface(dev)
interface_table.get()

for i in interface_table:
  if "vlan" in i.name:
    vlanints = zip(i.logicalname, i.logicalinetaddr)
  if ("ge" in i.name or "fe" in i.name) and i.addrfamily == "inet":
    ethints = formatter.format("interface", str(i.logicalname), "status", str(i.status), "address", str(i.logicalinetaddr))
    print ethints
  if ("ge" in i.name or "fe" in i.name) and i.addrfamily == "eth-switch":
    ethints = formatter.format("interface", str(i.logicalname), "status", str(i.status), "family", str(i.addrfamily))
    print ethints

for ints in vlanints:
  formattedints = formatter.format("interface", ints[0], "status", "up", "address", ints[1])
  print formattedints

dev.close()
