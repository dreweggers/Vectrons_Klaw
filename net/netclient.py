
import socket

host='localhost'

mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr=(host,7777)
mysock.connect(addr)

try:
	msg=b"hello world, this is a test\n"
	mysock.sendall(msg)
except socket.errno as e:
	print("Socket error", e)
finally:
	mysock.close()
