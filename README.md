stillis: 
	Is your whois record still what it last was? 

Usage: 

	stillis.py --domain someone.com

Sample: 

	stillis.py --domain mozilla.com
	Comparing whois records for mozilla.com
	Name: mozilla.com
	Registrar: MARKMONITOR INC.
	DNS: set(['ns1-240.akam.net', 'ns5-65.akam.net', 'ns4-64.akam.net', 'ns7-66.akam.net'])
	Exp: 2013-10-17 00:00:00
	Examining: mozilla.com.12345.fake.stillis	No match
	Examining: mozilla.com.1377926193.0.stillis	Matches

Details: 

	stillis retrieves the current record for a domain name, prints out selected attributes then
	stores the record as a python pickle structure with the current epoch time stamp. 

	It then looks in the current directory for any other files matching this domain name and compares the current
	record to those records, printing a simple status of match/no match. 

Prereqs: 

	python whois (pip install whois)

