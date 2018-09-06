from whois import whois

def get_whois_info(domain):
    whois_info = whois(domain)
    return whois_info

