# This script allow to know if a DNS server has transfer zone activated
# By David Galisteo 
# @darkvidhck
# https://github.com/darkvid

import sys
import dns
import dns.resolver
import dns.query
import dns.zone

answerString = ";ANSWER"
authorityString = ";AUTHORITY"
InAString = "IN NS "

#get first parameter - domain name
nameserver = sys.argv[1]

ns = (dns.resolver.query(nameserver, 'NS'))
ns_text = ns.response.to_text()

init_position = ns_text.find(answerString) + len(answerString) + 1
end_position = ns_text.find(authorityString) - 1

dns_servers_raw = ns_text[init_position : end_position]

lines = dns_servers_raw.split('\n')

for line in lines:
	server_position = line.find(InAString) + len(InAString)
	server_name = line[server_position:-1]
	
	#I have already the dns server names, so, I'm going to check if transfer zone is active