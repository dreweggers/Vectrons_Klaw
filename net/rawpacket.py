from scapy.all import *

frame = Ether(dst="15:16:90:fa:dd:09")/IP(dst="17.6.25.124")/TCP()/"This is my payload"

print(frame)
sendp(frame)

