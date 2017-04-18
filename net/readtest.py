#!/usr/bin/python

import pcapy
import sys
from struct import *

cap = pcapy.open_live("ens33", 65536, 1, 500)

while 1:
	(header,payload) = cap.next()
	l2hdr = payload[:14]
	print("l2hdr type: ", type(l2hdr), "Size: ", sys.getsizeof(l2hdr), "data: ", l2hdr)
	#l2data = unpack("!6s6sH", l2hdr)
	


