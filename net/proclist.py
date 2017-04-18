#!/usr/bin/python

import psutil

l = psutil.process_iter()

for proc in l:
	print(proc)
	print(proc.name())
	if (proc.name() == "python"):
		print(proc.memory_maps())
