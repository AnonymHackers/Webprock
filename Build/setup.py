import os
import time

print()
value = input("[?] Want run the setup for installation? [Y/n]: ")
if value == 'Y':
	os.system("pip install requests")
	os.system("pip install time")
	os.system("pip install datetime")
	os.system("pip install socket")
	os.system("pip install sys")
elif value == 'y':
	os.system("pip install requests")
	os.system("pip install time")
	os.system("pip install datetime")
	os.system("pip install socket")
	os.system("pip install sys")
else:
	sys.exit()

print()
print("[+] Program Webprock is installed you can run it")
while True:
	time.sleep(9)