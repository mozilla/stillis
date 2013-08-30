#!/usr/bin/env python
import sys
import whois
from optparse import OptionParser
import time
import pickle 
import glob

def diffDomain(domainName):
    '''given a domain name, will compare current whois record to most recent cache of whois entry and report any differences'''
    currRecord=whois.query(domainName)
    currRecordEpoch=time.mktime(time.gmtime())
    sys.stdout.write('Name: {0}\n'.format(currRecord.name))
    sys.stdout.write('Registrar: {0}\n'.format(currRecord.registrar))
    sys.stdout.write('DNS: {0}\n'.format(currRecord.name_servers))
    sys.stdout.write('Exp: {0}\n'.format(currRecord.expiration_date))
    currRecordFile=open('{0}.{1}.stillis'.format(domainName,currRecordEpoch),'w')
    currRecordContent=pickle.dumps(currRecord)
    currRecordFile.write(currRecordContent)
    currRecordFile.close()

  
    for dfile in glob.glob('{0}*stillis'.format(domainName)):
      sys.stdout.write('Examining: {0}'.format(dfile))
      dfileContent=open(dfile).read()
      if dfileContent==currRecordContent:
          sys.stdout.write('\tMatches \n')
      else:
          sys.stdout.write('\tNo match \n')

if __name__ == "__main__":
    parser = OptionParser();
    parser.add_option("-d", "--domain", dest='domain'  , default="", type="str", help="target domain name (sample.com)")

    (options,args) = parser.parse_args()

    sys.stdout.write('Comparing whois records for {0}\n'.format(options.domain))
    diffDomain(options.domain)
