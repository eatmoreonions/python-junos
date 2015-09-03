#!/usr/bin/python

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.factory import loadyaml

from getpass import getpass
host = raw_input('hostname or address: ')
username = raw_input('username: ')
passwd = getpass('password: ')

formatter = "{0:<16}{1:<20}{2:<50}"

src_addr = raw_input('what source address pattern are you looking for? ')
appl = raw_input('what application port are you looking for [any]? ') or 'any'

globals().update(loadyaml('flowsession.yml'))

dev = Device(host, user=username, password=passwd)

dev.open()
dev.timeout = 60

session_table = SessionTable(dev)
session_table.get()

header = formatter.format("source", "destination", "destination port")
print "\n" + header

for s in session_table:
  if session_table.keys():
    if "any" in appl and s.session_protocol == 'tcp' and s.session_direction == 'In':
      if src_addr in s.source_address:
        session = formatter.format(s.source_address, s.destination_address, s.destination_port)
        print session
    elif not "any" in appl and s.session_protocol == 'tcp' and s.session_direction == 'In':
      if src_addr in s.source_address and s.destination_port == appl:
        session = formatter.format(s.source_address, s.destination_address, s.destination_port)
        print session

dev.close()
