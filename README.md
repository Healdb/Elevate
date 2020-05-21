# Elevate
Vertical domain discovery tool

Requirements:
requests

Install requirements with the command `pip install -r requirements.txt`

API keys from WHOXY and whoisXML are also needed, but the accounts are free to signup for.
Place these keys in the config.txt file.
Sign up for these accounts here - https://www.whoxy.com/ and here - https://www.whoisxmlapi.com/

USAGE:

Elevate takes in a partial organization name, an email address, or a domain name, and finds all other domain names owned by that organization.

Sample Usage with a known domain name and email address: 
`python elevate.py -o "reddit_domains.txt" -d "reddit.com" -e "domainadmin@reddit.com"`

Search with only a domain name: 
`python elevate.py -o "reddit_domains.txt" -d "reddit.com"`

Search with only an email address: 
`python elevate.py -o "reddit_domains.txt" -e "domainadmin@reddit.com"`

If you only know the Organization's name, such as 'Uber', you can search the ASN registry for a match.
Searching with only a partial name:
`python elevate.py -o "reddit_domains.txt" -n "uber"`

You will then be prompted to select the ASN names that closely match your search term. Elevate will then search for domains registered to that company name.


