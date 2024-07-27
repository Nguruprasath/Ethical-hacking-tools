import socket  # able to communicate with other computer using tcp or udp
import termcolor # print is different color 


def scan(target, ports):
    for port in range(1, ports):
        scan_port(target, port)
    print(termcolor.colored("[+] Scanning completed.", 'red'))




def scan_port(ipaddress, port):
   try:	
     #initate a socket object
     sock = socket.socket() # calling the socket fuction
     # to connect function ip address 
     sock.connect((ipaddress, port))
     print(" port open "+ str(port))
     sock.close()
   except: 
     pass 


targets = input(" Enter targets to scan (split them by ,):  ") # 192.168.1.1,192168.9.1
ports = int(input(" Enter how many ports you wants to scan: ")) #int get ports eg: 100

if ',' in targets:
	print(termcolor.colored(("[+] scanning multiple targets"), 'green'))
	for ip_addr in targets.split(','): # split ,
		scan(ip_addr,ports)
else:
  print(termcolor.colored(("[+] scanning targets...."), 'green'))
  scan(targets,ports)
