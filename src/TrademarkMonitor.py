import requests
import socket
import re
from bs4 import BeautifulSoup
from pprint import pprint

class TrademarkMonitor:
    def __init__(self, domain):
        self.domain = domain       
        resp = requests.post('https://www.htbridge.com/radar/', data={'name':self.domain})
        soup = BeautifulSoup(resp.text, 'html.parser')
        self.soup = soup
    
    def get_ip_info(self):
        return [{row.find_all("td")[0].text: row.find_all("td")[1].text} for row in self.soup.table.find_all("tr")]

    def blacklist_report(self):
        engine_list = self.soup.find_all('table')[1].find_all('i', class_="fa fa-minus-circle text-danger")
        return [{j.parent.text : j.parent.next_sibling.a['href']} for j in engine_list]

t = TrademarkMonitor('google.com')
pprint(t.soup.text)
