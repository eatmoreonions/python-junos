#!/usr/bin/python

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.factory import loadyaml

from getpass import getpass
host = raw_input('hostname or address: ')
username = raw_input('username: ')
passwd = getpass('password: ')

globals().update(loadyaml('vlaninfo.yml'))

dev = Device(host, user=username, password=passwd)

dev.open()
dev.timeout = 60

formatter = "{0:<14}{1:<14}{2:<17}{3:<8}{4:<30}"
header = formatter.format("Name", "L3 Int", "L3 Address", "Count", "Member List")
print header

vlan_table = ShowInterface(dev)
vlan_table.get()

for i in vlan_table:
    memberlist = formatter.format(str(i.name), str(i.l3int), str(i.l3addr), str(i.membercount), str(i.memberlist))
    print memberlist

dev.close()
