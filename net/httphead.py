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
HttpHead()
