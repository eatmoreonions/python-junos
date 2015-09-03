#!/usr/bin/python

from pprint import pprint as pp
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.factory import loadyaml

dev = Device('10.9.5.201', user='xxxx', password='xxxxxxx')

dev.open()
dev.timeout = 60

globals().update(loadyaml('partitioninfo-tfc.yml'))
partition_table = PartitionTable(dev)
partition_table.get()

pp(partition_table[0])
pp(partition_table[0].items())

pp(partition_table[1])
pp(partition_table[1].items())

#for s in partition_table:
#  if partition_table.keys():
#    pprint(partition_table.values())

dev.close()
