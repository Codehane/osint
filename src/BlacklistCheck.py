import requests
import socket
import re
from bs4 import BeautifulSoup

class BlacklistCheck:
    def __init__(self, domain_or_ip):
        def is_ip(domain_or_ip):
            ip_pat = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
            return ip_pat.match(domain_or_ip)
        
        if not is_ip(domain_or_ip) :
            self.ip = socket.gethostbyname(domain_or_ip)
        else: 
            self.ip = domain_or_ip
        
        resp = requests.post('http://www.ipvoid.com/ip-blacklist-check/', data={'ip': self.ip})
        soup = BeautifulSoup(resp.text, 'html.parser')
        self.soup = soup
    
    def get_ip_info(self):
        return {row.find_all("td")[0].text: row.find_all("td")[1].text for row in self.soup.table.find_all("tr")}


    def blacklist_report(self):
        engine_list = self.soup.find_all('table')[1].find_all('i', class_="fa fa-minus-circle text-danger")
        return {j.parent.text : j.parent.next_sibling.a['href'] for j in engine_list}