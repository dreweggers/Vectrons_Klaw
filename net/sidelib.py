# Name lookup
#!/usr/bin/python3
# Some parsing of results should be added in the future
import socket

def NameLookup():
	print(socket.gethostbyaddr("8.8.8.8"))
	print(socket.gethostbyname("www.google.com"))
NameLookup()
# END namelookup

# proclist
#!/usr/bin/python

import psutil

def ProcList():
	l = psutil.process_iter()

	for proc in l:
		print(proc)
		print(proc.name())
		if (proc.name() == "python"):
			print(proc.memory_maps())
ProcList()
# END proclist

# fuzz
#!/usr/bin/python
from pyfuzz.generator import *
import socket

# msg = b"GET /icons/ubuntu-logo.png"+b" / HTTP/1.1\nlocalhost\r\n"
msg = random_ascii() + b" / HTTP/1.1\nlocalhost\r\n"
print(msg)

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	addr = ("192.168.208.146", 80)
	s.connect(addr)
	s.sendall(msg)
	resp = s.recv(4096)
	print(resp)
except Exception as e:
	print(e)
finally:
	s.close()
# END fuzz

# httpcookie
import urllib2

def HttpCookie(url = "https://www.google.com"):
	request = urllib2.Request(url)
	resp = urllib2.urlopen(request)
	cookies = resp.info()['Set-Cookie']
	content = resp.read()
	resp.close()
	print(cookies, content)
HttpCookie()
# END httpcookie

# bannergrab
import socket
import re

# BannerGrab(hostname, portNumber)
# if called with no values --> BannerGrab() then www.microsoft.com and port 80 are used by default

def BannerGrab(h="www.microsoft.com", p=80):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((h, p))
	#sock.connect(("www.microsoft.com", 80))
	http_get = b"GET / HTTP/1.1\nHost: "+ h +"\n\n"
	data = ''

	try:
		sock.sendall(http_get)
		data = sock.recvfrom(1024)
	except socket.error:
		print("Socket error", socket.errno)
	finally:
		print("closing connection")
		sock.close()

	strdata = data[0].decode("utf-8")
	headers = strdata.splitlines()
	for s in headers:
		if re.search('Server:', s):
			s = s.replace("Server: ", "")
			print(s)
BannerGrab()
# END bannergrab

# httpHead
#!/usr/bin/python3

import httplib

def HttpHead(host = "74.125.193.106"):
	req = httplib.HTTP(host)
	req.putrequest("HEAD", "/")
	req.putheader("Host", host)
	req.endheaders()
	req.send("")

	statusCode, statusMsg, headers = req.getreply()
	print("Status: ", statusCode)
	print(statusMsg, headers)
HttpHead()
# END httphead

# http test
#!/usr/bin/env python3
# This module currently only works with Python3

import http.client

def HttpTest(a = "www.semocdc.com"):
	h = http.client.HTTPConnection(a)
	h.request("GET", "/")
	data = h.getresponse()
	print (data.code)
	print (data.headers)
	text = data.readlines()
	for t in text:
		print(t.decode('utf-8'))
HttpTest()
# END httptest

# parse pcap
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
# END parsepcap

# net client
#!/usr/bin/env python
# This function looks like it opens a connection to a specified host and port
#  Then sends a message, in bytes, to that address
import socket

def NetClient(host='localhost', p=7777):
	mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	addr=(host,p)
	mysock.connect(addr)

	try:
		msg=b"hello world, this is a test\n"
		mysock.sendall(msg)
	except socket.errno as e:
		print("Socket error", e)
	finally:
		mysock.close()

NetClient("google.com", 80)
# The script currently crashes with default localhost options
# 	Unless a local webserver is running
NetClient()
# END netclient

