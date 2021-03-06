#!/usr/bin/env python
# We need to add support for specifying a certain .pcap file
# Current script does not work unless 'test.pcap' is in same directory
import pcapy
from struct import *

def ParsePcap():
	pcap_file = pcapy.open_offline("test.pcap")
	count = 1

	while count:
		print("Packet #: ", count)
		count = count + 1
		(header,payload) = pcap_file.next()
		l2hdr = payload[:14]
		l2data = unpack("!6s6sH", l2hdr)
		srcmac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(l2hdr[0]), ord(l2hdr[1]), ord(l2hdr[2]), ord(l2hdr[3]), ord(l2hdr[4]), ord(l2hdr[5]))
		dstmac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(l2hdr[6]), ord(l2hdr[7]), ord(l2hdr[8]), ord(l2hdr[9]), ord(l2hdr[10]), ord(l2hdr[11]))
		print("Source MAC: ", srcmac, " Destination MAC: ", dstmac)
		ipheader = unpack('!BBHHHBBH4s4s', payload[14:34])
		timetolive = ipheader[5]
		protocol = ipheader[6]
		print("Protocol ", str(protocol), "Time To Live: ", str(timetolive))
ParsePcap()
