class Sources:
    whoxyKey = ""
    whoisXmlKey = ""
    def __init__(self):
        configFile = open("config.txt","r")
        apiKeys = {}
        for line in configFile.readlines():
            line = line.split(":")
            apiKeys[line[0]] = line[1].strip()
        try:
            self.whoxyKey = apiKeys["whoxy"]
            self.whoisXmlKey = apiKeys["whoisxml"]
        except KeyError:
            raise Exception("API Key found in config. Ensure WHOXY and WhoisXML keys are present.")
