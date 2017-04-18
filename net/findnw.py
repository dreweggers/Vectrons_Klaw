#!/usr/bin/python

import pcapy

devs = pcapy.findalldevs()
print(devs)
