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
