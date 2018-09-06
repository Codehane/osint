import string
import httplib
from socket import *
import re
import getopt
import stash

from discovery import *
from lib import htmlExport
from lib import hostchecker

    start = 0
    host_ip = []
    filename = ""
    bingapi = "yes"
    dnslookup = False
    dnsbrute = False
    dnstld = False
    shodan = False
    vhost = []
    virtual = False
    ports_scanning = False
    takeover_check = False
    limit = 500
    dnsserver = ""

   def search_adresses()
        search = googlesearch.search_google(word, limit, start)
        search.process()
        all_emails = search.get_emails()
        all_hosts = search.get_hostnames()
        for x in all_hosts:
            try:
                db=stash.stash_manager()
                db.store(word,x,'host','google')
            except Exception, e:
                print e


    elif engine == "linkedin":
        print "[-] Searching in Linkedin.."
        search = linkedinsearch.search_linkedin(word, limit)
        search.process()
        people = search.get_people()
        print "Users from Linkedin:"
       	print "-------------------"
       	for user in people:
            print user
    
    #Results############################################################
    print("\n\033[1;32;40m Harvesting results")
    print "\n\n[+] Emails found:"
    print "------------------"
    if all_emails == []:
        print "No emails found"
    else:
        print "\n".join(all_emails)

    print("\033[1;33;40m \n[+] Hosts found in search engines:")
    print "------------------------------------"
    if all_hosts == []:
        print "No hosts found"
    else:
        total = len(all_hosts)
        print "\nTotal hosts: " + str(total) + "\n"
        all_hosts=sorted(set(all_hosts))
        print "\033[94m[-] Resolving hostnames IPs...\033[1;33;40m \n "
        full_host = hostchecker.Checker(all_hosts)
        full = full_host.check()
        for host in full:
            ip = host.split(':')[1]
            print host
            if ip != "empty":
                if host_ip.count(ip.lower()):
                    pass
                else:
                    host_ip.append(ip.lower())



    recursion = None
    if recursion:
        start = 0
        for word in vhost:
            search = googlesearch.search_google(word, limit, start)
            search.process()
            emails = search.get_emails()
            hosts = search.get_hostnames()
            print emails
            print hosts
    else:
        pass



