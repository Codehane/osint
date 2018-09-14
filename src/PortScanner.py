import nmap

host = 'google.com'
nm = nmap.PortScanner()
nm.scan(host)
print(nm.scaninfo())
