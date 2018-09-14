## Blacklist Check Module
This module takes a domain name or IP address and lists IP adress information and blacklist check result from multiple engines.

### Methods 

*BlacklistCheck.get_ip_info()*

> **EXPLANATION:** 
> - Returns IP adress information of the given domain name or IP adress.
> 
> **PARAMATERS:**
> - No parameter
> 
> **RESPONSE:** 
> - json 
>
> *Example output:* 
>
>```json
>{"Analysis Date": "2018-09-05 07:19:22", "Elapsed Time": "1 seconds", "Blacklist Status": "BLACKLISTED 1/96", "IP Address": "172.217.23.238 Find Sites | IP Whois", "Reverse DNS": "prg03s06-in-f238.1e100.net", "ASN": "AS15169", "ASN Owner": "Google LLC", "ISP": "Google", "Continent": "North America", "Country Code": " (US) United States", "Latitude / Longitude": "37.751 / -97.822 Google Map", "City": "Unknown", "Region": "Unknown "}
```

*BlacklistCheck.blacklist_report()*

> **EXPLANATION:** 
> - Returns a dictonary with engine names which marked the given IP as blacklisted and link of their detail pages.
> 
> **PARAMATERS:**
> - No parameter
> 
> **RESPONSE:** 
> - json 
>
> *Example output:* 
>
>```json
> {"Engine1": "http://www.engine1/content.html", "Engine2": "http://www.engine2/content.html"}
```

## Reverse Ip Lookup Module

This module takes a domain name or IP address and lists other sites known to be hosted on that same web server.

### Methods 

*Reverse_Ip_Check.get_domains(domain_or_ip) - Static*

> **EXPLANATION:** 
> - Returns domain adresses of the websites hosted on the given web server.
> 
> **PARAMATERS:**
> - **domain_or_ip** : domain or ip adress (*string, Required*)
> 
> **RESPONSE:** 
> - json
>
> *Example output:* 
>
>```json
>{"status": "Success", "domains": ["google.com"], "host_ip": "172.217.14.238"}
