#!/usr/bin/python

# IMPORTS
# findnw
import pcapy
	
# Thread
import socket
import threading
import urllib2

# mtls
import ssl
import socket

# spider
from HTMLParser import HTMLParser
import urllib2

# Outputs all network devices on machine
def findnw():
	devs = pcapy.findalldevs()
	print(devs)


# Thread
def threadconnect(site = "www.google.com", p = 443):
	class clientConnect(threading.Thread):
		def __init__(self):
			threading.Thread.__init__(self)

		def run(self):
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			addr = (site, p)
			sock.connect(addr)
			print("Connected")

	sockClients = []
	for i in range(1,100):
		s = clientConnect()
		s.start()
		print("started ", i)
		sockClients.append(s)
	return
# End Thread


# mtls python3 ?
def mtls(a = "portal.semo.edu"):
	s = sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	ssock = ssl.wrap_socket(s)

	try:
		# Broken pipe error if ssock.connect includes 'www' prefix
		ssock.connect((a, 443))
		print(ssock.cipher())
	except:
		print("error")

	try:
		ssock.write(b"GET / HTTP/1.1 \r\n")
		ssock.write(b"Host: www.portal.semo.edu\n\n")
	except Exception as e:
		print("write error: ", e)

	data = bytearray()
	try:
		data = ssock.read()
	except Exception as e:
		print("read error", e)

	print(data.decode("utf-8"))

# end mtls


# spider
def spider():
	class myParser(HTMLParser):
		def handle_starttag(self, tag, attrs):
			if (tag == "a"):
				for a in attrs:
					if (a[0] == 'href'):
						link = a[1]
						if (link.find('http') >= 0):
							print(link)
							newParse = myParser()
							newParse.feed(link)

	url = "http://www.semo.edu"
	request = urllib2.Request(url)
	handle = urllib2.urlopen(request)
	parser = myParser()
	parser.feed(handle.read())
# END spider

# raw packet
#!/usr/bin/env python
#  Needs more functions to get rid of hardcoded variables
#		such as MAC and IP
from scapy.all import *

def rawpacket():
	frame = Ether(dst="15:16:90:fa:dd:09")/IP(dst="17.6.25.124")/TCP()/"This is my payload"

	print(frame)
	sendp(frame)


# END rawpacket

# readHdr
#!/usr/bin/python

import pcapy
from struct import *

def readhdr():
	cap = pcapy.open_live("ens33", 65536, 1, 500)

	while 1:
		(header,payload) = cap.next()
		l2hdr = payload[:14]
		if l2hdr != '':
			l2data = unpack("!6s6sH", l2hdr)
			srcmac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(l2hdr[0]), ord(l2hdr[1]), ord(l2hdr[2]), ord(l2hdr[3]), ord(l2hdr[4]), ord(l2hdr[5]))
			dstmac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(l2hdr[6]), ord(l2hdr[7]), ord(l2hdr[8]), ord(l2hdr[9]), ord(l2hdr[10]), ord(l2hdr[11]))
			print("Source MAC: ", srcmac, " Destination MAC: ", dstmac)
	
		#get IP header, which is 20 bytes long
		#then unpack it into what it is
			ipheader = unpack('!BBHHHBBH4s4s', payload[14:34])
			timetolive = ipheader[5]
			protocol = ipheader[6]
			print("Protocol ", str(protocol), "Time To Live: ", str(timetolive))

# END readhdr

