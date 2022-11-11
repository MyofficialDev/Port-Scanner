import socket
import termcolor

def scan(ip,ports):
	for i in range(1,ports):
		scaning(ip,i)
def scaning(ip,ports):
	try:
		sock=socket.socket()
		sock.connect((ip,ports))
		print("Ports Open" + str(ports))
		sock.close()
	except:
		pass

ip=input("Enter the Target :")
ports=int(input("Number of ports be scanned :"))

if ',' in ip:
	print(termcolor.coloured(("[*] Scanning Multiple targets"),'green'))
	
	for i in ip.split(','):
		scan(i,ports)
else:
	scan(ip,ports)
