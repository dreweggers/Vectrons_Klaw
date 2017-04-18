#!/usr/bin/python3


import ssl
import socket

def Mtls(a = "portal.semo.edu"):
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
Mtls()
