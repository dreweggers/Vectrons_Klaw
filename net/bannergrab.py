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
