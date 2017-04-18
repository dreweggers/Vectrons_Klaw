#!/usr/bin/python3

import http.client

h = http.client.HTTPConnection("www.semocdc.com")
h.request("GET", "/")
data = h.getresponse()
print (data.code)
print (data.headers)
text = data.readlines()
for t in text:
	print(t.decode('utf-8'))

