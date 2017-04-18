#!/usr/bin/python

import pcapy
def FindNw():
	devs = pcapy.findalldevs()
	print(devs)
FindNw()
