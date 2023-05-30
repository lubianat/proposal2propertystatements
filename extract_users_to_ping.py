from wdcuration import render_qs_url
from bs4 import BeautifulSoup

id_name = "attracts"
property_id = "P11801"


proposal_page = f"https://www.wikidata.org/wiki/Wikidata:Property_proposal/{id_name}"

import requests

r = requests.get(
    f"https://www.wikidata.org/w/index.php?title=Wikidata:Property_proposal/{id_name}&action=edit"
)

html = r.text
soup = BeautifulSoup(html, "lxml")

# HTML locator identified with help of https://webscraper.io/
entries = soup.find("textarea")
page = entries.text

import re


a = re.findall("User:(.*?)\|", page)

ping = (
    "{{ping|"
    + "|".join(list(set(a)))
    + "}}"
    + "Created as {{P|"
    + property_id
    + "}} ~~~~"
)
print(ping)
