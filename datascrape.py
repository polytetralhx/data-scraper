import requests
from bs4 import BeautifulSoup
import pandas as pd
import regex as re

variables = ['list', 'cd', 'eh', 'il', 'mo', 'pr', 'su', 'vz']
company, address, website, numbers = [], [], [], []
for code in variables:
    webpage = requests.get("https://www.songwriteruniverse.com/label" + f"{code}" + ".htm").text
    soup = BeautifulSoup(webpage, "html.parser")
    for cmpy in soup.find_all("h3"):
        company.append(cmpy.text.strip())
    for site in soup.find_all("p"):
        address.append(site.text.strip())
    address = list(filter(lambda x: not x.startswith("www.") and not x.startswith('Here') and not x.startswith('[email') and not x.startswith("http"), address[1:]))
    for link in soup.find_all("a"):
        website.append(link.text.strip())
address = [sub_item.replace("\xa0protected", 'protected') for item in address for sub_item in item.split("\n")]
address = [string.replace("\xa0", "protected") for string in address]
address = list(filter(lambda x: x and x != "[email]", address))
address = [string.replace("# ", "#") for string in address]

for val in address:
    if "-" in val and not re.search("[a-zA-Z]", val):
        numbers.append(val)
    elif "Fax" in val:
        numbers.append(val)
for no in numbers:
    address.remove(no)
    no.replace("Fax:", ",")
numbers = [sub_item for item in numbers for sub_item in item.split("Fax:")]
numbers = [no.replace(".", "") for no in numbers]
website = list(filter(lambda x: x.startswith("www."), website))

print(len(company))
print(len(address))
print(len(numbers))
print(len(website))
features = {"Company Name": company, "Address": address, "Fax/Phone Number": numbers, "Website": website}
df = pd.DataFrame(features)


        




