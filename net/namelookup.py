#!/usr/bin/python3
# Some parsing of results should be added in the future
import socket

def NameLookup():
	print(socket.gethostbyaddr("8.8.8.8"))
	print(socket.gethostbyname("www.google.com"))
NameLookup()
