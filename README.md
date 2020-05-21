# Elevate
Elevate is a vertical domain discovery tool you can use to discover other domains owned by a given company. Domains owned by Reddit are discovered with the tool below.

![output](/images/elevate.gif)

# Requirements:

Install requirements with the command `pip install -r requirements.txt`

API keys from WHOXY and whoisXML are also needed, but the accounts are free to signup for.
Place these keys in the config.txt file.
Sign up for these accounts here - https://www.whoxy.com/ and here - https://www.whoisxmlapi.com/

# Usage:

Elevate takes in a partial organization name, an email address, or a domain name, and finds all other domain names owned by that organization.

Sample use: 
`python elevate.py -o "reddit_domains.txt" -d "reddit.com" -e "domainadmin@reddit.com"`

![domain email output](/images/domain_email_image.PNG)

Search with only a domain name: 
`python elevate.py -o "reddit_domains.txt" -d "reddit.com"`

![domain output](/images/domain_image.PNG)

Search with only an email address: 
`python elevate.py -o "reddit_domains.txt" -e "domainadmin@reddit.com"`
![domain output](/images/email_image.PNG)

If you only know the Organization's name, such as 'Uber', you can search the ASN registry for a match.
Searching with only a partial name:
`python elevate.py -o "reddit_domains.txt" -n "uber"`

You will then be prompted to select the ASN names that closely match your search term. Elevate will then search for domains registered to that company name.

![domain output](/images/partial_image.PNG)

