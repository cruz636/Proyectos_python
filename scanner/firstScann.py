import nmap
import sys

def main():
	if len(sys.argv) == 1:
		noArg()
	if len(sys.argv) == 3 or len(sys.argv) == 2:
		help()
		exit()
	if len(sys.argv) > 4:
		help()
		exit()
	if len(sys.argv) > 1 & len(sys.argv) < 4:
		scan(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))
		exit()




def help():
	print "USAGE: sudo python scan.py <host> <first port> <last port>"
	print "HOST eg: 192.168.0. (dont forget the last dot)"
def noArg():
	print "[+] Host: "
	print "eg: 192.168.0."
	host = raw_input("[>] ")
	iniRange= input("[>] From: ")
	endRange = input("[>] To: ")
	scan(host,iniRange,endRange)

def scan(host,iniRange,endRange):
	nm = nmap.PortScanner()

	while iniRange < endRange:
		ip = host + str(iniRange)
		results = nm.scan(hosts=ip,arguments='-sSV -A -n',ports='22,25,80,443')

		try:
			nm[ip].state()
			print "--"*30
			print('[+] HOST %s is up' %ip)
			print nm.csv()
			print "--" *30
		except:
			pass

		iniRange += 1


main()
