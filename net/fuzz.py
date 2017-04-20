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

