import re
import requests
import json
from sources import Sources
import random
class Utilities:
    masterDomainList = []
    email = ""
    orgName = ""
    keys = Sources()
    def getOrgASN(self, partialOrgName):
        ASNFile =  open("asnlist.txt","r")
        index = 0
        possibleMatches = {}
        for line in ASNFile:
            try:
                name = re.match(r"\d+,(.+), \w\w",line).group(1)
                if(re.search(partialOrgName, name, re.IGNORECASE)):
                    #name = name.split(" - ")[-1]
                    possibleMatches[index] = name
                    index+=1
            except:
                pass
        return possibleMatches
    def getWhoxy(self, orgName,verbose):
        total = []
        baseUrl = "https://api.whoxy.com/?key="+self.keys.whoxyKey+"&reverse=whois"
        try:
            search = "&company="+orgName.replace(" ","+")
            url = baseUrl + search
            response = requests.get(url+"&mode=mini")
            data = json.loads(response.text)
            totalPages = data["total_pages"]
            i=0
            while i<totalPages:
                i+=1
                response = requests.get(url + "&mode=mini&page="+str(i))
                data = json.loads(response.text)
                for domain in data["search_result"]:
                    total.append(domain["domain_name"])
                    if verbose:
                        print(domain["domain_name"])
        except KeyError:
            print("ERROR: Skipping WHOXY, no API credits remaining.")
        return total
    def getWhoisXML(self,orgName,verbose):
        total = []
        baseUrl = "https://reverse-whois-api.whoisxmlapi.com/api/v2"
        params = {"apiKey": self.keys.whoisXmlKey,"searchType": "current","mode": "purchase","basicSearchTerms": {"include": [ orgName,"US"],"exclude": ["Europe","EU"]}}
        response = json.loads(requests.post(baseUrl, data=json.dumps(params)).text)
        try:
            for domain in response["domainsList"]:
                total.append(domain)
                if verbose:
                    print(domain)
        except KeyError:
            print("ERROR: Skipping whoisXML, no API credits remaining.")
        return total
    def orgNameFromWHOIS(self,domainName):
        response = requests.get("http://api.whoxy.com/?key="+self.keys.whoxyKey+"&whois="+str(domainName))
        data = json.loads(response.text)
        try:
            return data["registrant_contact"]["company_name"]
        except:
            print("No organization found from domain name.\n")
            return ""
    def getWhoxyEmail(self, emailAddress,verbose):
        total = []
        baseUrl = "https://api.whoxy.com/?key="+self.keys.whoxyKey+"&reverse=whois"
        try:
            search = "&email="+emailAddress.replace(" ","+")
            url = baseUrl + search
            response = requests.get(url+"&mode=mini")
            data = json.loads(response.text)
            totalPages = data["total_pages"]
            i=0
            while i<totalPages:
                i+=1
                response = requests.get(url + "&mode=mini&page="+str(i))
                data = json.loads(response.text)
                for domain in data["search_result"]:
                    total.append(domain["domain_name"])
                    if verbose:
                        print(domain["domain_name"])
        except KeyError:
            print("ERROR: Skipping WHOXY, no API credits remaining.")
        return total
    def getWhoisXMLEmail(self,email,verbose):
        email = "@" + email.split("@")[1]
        total = []
        baseUrl = "https://reverse-whois-api.whoisxmlapi.com/api/v2"
        params = {"apiKey": self.keys.whoisXmlKey,"searchType": "current","mode": "purchase","basicSearchTerms": {"include": [ email,"US"],"exclude": ["Europe","EU"]}}
        response = json.loads(requests.post(baseUrl, data=json.dumps(params)).text)
        try:
            for domain in response["domainsList"]:
                total.append(domain)
                if verbose:
                    print(domain)
        except KeyError:
            print("ERROR: Skipping whoisXML, no API credits remaining.")
        return total
    def getOrgNameDomains(self, orgName,verbose):
        whoxyDomains = set(self.getWhoxy(orgName,verbose))
        whoisXMLDomains = set(self.getWhoisXML(orgName,verbose))
        self.masterDomainList = whoxyDomains.union(whoisXMLDomains)
        return self.masterDomainList
    def getEmailDomains(self, emailAddress,verbose):
        whoxyDomains = set(self.getWhoxyEmail(emailAddress,verbose))
        whoisXMLDomains = set(self.getWhoisXMLEmail(emailAddress,verbose))
        self.masterDomainList = whoxyDomains.union(whoisXMLDomains)
        return self.masterDomainList
    def writeToFile(self,domainList,outputFileName):
        outputFile = open(outputFileName, "w")
        for domain in domainList:
            outputFile.write(domain+"\n")
        outputFile.close()
