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
