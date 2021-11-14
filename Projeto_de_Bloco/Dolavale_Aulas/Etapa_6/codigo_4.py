import nmap

nm = nmap.PortScanner()
print(nm.scan('192.168.1.3'))
