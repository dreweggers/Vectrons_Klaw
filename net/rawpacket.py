#!/usr/bin/env python
#  Needs more functions to get rid of hardcoded variables
#		such as MAC and IP
from scapy.all import *

def RawPacket():
	frame = Ether(dst="15:16:90:fa:dd:09")/IP(dst="17.6.25.124")/TCP()/"This is my payload"

	print(frame)
	sendp(frame)
RawPacket()
