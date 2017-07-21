#!/usr/bin/python2
# Vectrons_Klaw main file

import mainlib
import os
import time

def welcome():
	# mainlib options
	menu_main = [
		"Find network devices",
		"Multi-thread connection",
		"MTLS",
		"Spider",
		"Raw packet",
		"Read header",

		"Exit",
	]
	# sidelib options will go here
	menu_side = [] 
	print("~"*18+"Vectrons_Klaw"+"~"*18+"\n")
	i = 0
	for menus in menu_main:
		i = i+1
		print(str(i)+" - "+menus.title())
	print("\n"+"~"*49)
	
# Function to clear terminal screen
def clearscreen():
	os.system('cls' if os.name == 'nt' else 'clear')

def main():
	# Clear console
	clearscreen()
	while True:
		welcome()
		try:
			choice = int(raw_input("Enter your selection: "))
			if choice == 1:
				mainlib.findnw()
				time.sleep(3)
			elif choice == 2:
				mainlib.threadconnect()
				time.sleep(3)
			elif choice == 3:
				mainlib.mtls()
				time.sleep(3)
			elif choice == 4:
				mainlib.spider()
				time.sleep(3)
			elif choice == 5:
				mainlib.rawpacket()
				time.sleep(3)
			elif choice == 6:
				mainlib.readhdr()
				time.sleep(3)
			elif choice == 7:
				break
				return
			else:
				print("Invalid selection...try again")
				time.sleep(2)
				clearscreen()
		except ValueError:
			print("You must enter an integer!")
			time.sleep(3)
			clearscreen()
			continue
	print("Graceful exit")


if __name__ == '__main__':
	main()
