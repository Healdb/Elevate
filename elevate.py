#!/usr/bin/python
# -*- coding: utf-8 -*-

from utils import Utilities
import sys
import getopt
def printLogo():
    print("""
___________.__                       __          
\_   _____/|  |   _______  _______ _/  |_  ____  
 |    __)_ |  | _/ __ \  \/ /\__  \\   __\/ __ \ 
 |        \|  |_\  ___/\   /  / __ \|  | \  ___/ 
/_______  /|____/\___  >\_/  (____  /__|  \___  >
        \/           \/           \/          \/
        by Ben Heald
        https://healdb.tech
        https://github.com/Healdb/Elevate
        https://twitter.com/heald_ben
        """)
    print("Vertical Domain Discovery\n")
def asnSearch(utils,partialOrgName,verbose):
    #Search for domains using organization name
    orgNames = utils.getOrgASN(partialOrgName)
    for index in orgNames:
        print(str(index) + ": " + orgNames[index])
    orgChoices = []
    orgIndexes = input("Select CSV indexes for Organizations you want to investigate. Ex: 1,7,13\n").split(",")
    for orgIndex in orgIndexes:
        orgChoices.append(orgNames[int(orgIndex)].split(" - ")[-1]) 
    for orgChoice in orgChoices:
        totalDomains = utils.getOrgNameDomains(orgChoice,verbose)
    print(str(len(totalDomains)) + " Domains discovered using organization names\n")
    return totalDomains
def whoisSearch(utils, domainName,verbose):
    orgName = utils.orgNameFromWHOIS(domainName)
    totalDomains = set([])
    if orgName != "":
        print("Found Organization Name: " + orgName+ " from provided domain name.")
        totalDomains = utils.getOrgNameDomains(orgName,verbose)
        print(str(len(totalDomains)) + " Domains discovered using domain name\n")
    return totalDomains
def emailSearch(utils, email,verbose):
    totalDomains = utils.getEmailDomains(email,verbose)
    print(str(len(totalDomains)) + " Domains discovered using email address\n")
    return totalDomains
def elevate(argv):
    totalDomains = set([])
    outputFileName = ''
    targetDomain = ''
    targetEmail = ''
    partialOrgName = ''
    checkEmails = False
    verbose = False
    try:
        (opts, args) = getopt.getopt(argv, 'h:o:d:e:n:v')
    except getopt.GetoptError:
        print('elevate.py -o <outputfile> -d <domain name> -e <email address> -n <partial name> -v <verbose mode>')
        sys.exit(2)
    for (opt, arg) in opts:
        if opt == '-h':
            print('elevate.py -o <outputfile>')
            sys.exit()
        elif opt in '-o':
            outputFileName = arg
        elif opt in '-d':
            targetDomain = arg
        elif opt in '-e':
            targetEmail = arg
        elif opt in '-n':
            partialOrgName = arg
        elif opt in '-v':
            verbose = True
    if(outputFileName == ''):
        raise Exception("Output file must be set with '-o' flag")
    utils = Utilities()
    if(targetDomain != ''):
        totalDomains = totalDomains.union(whoisSearch(utils,targetDomain,verbose))
    if(partialOrgName != ''):
        totalDomains = totalDomains.union(asnSearch(utils,partialOrgName,verbose))
    if(targetEmail != ''):
        totalDomains = totalDomains.union(emailSearch(utils,targetEmail,verbose))
    print(str(len(totalDomains)) + " unique domain names discovered.")
    utils.writeToFile(list(totalDomains),outputFileName)   
if __name__ == '__main__':
    printLogo()
    elevate(sys.argv[1:])
