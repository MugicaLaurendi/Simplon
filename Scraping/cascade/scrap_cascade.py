import pandas as pd
from bs4 import BeautifulSoup
import requests as req



page = req.get(f"https://www.charlesbordet.com/fr/blog/#")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)
#bob = soup.find(class_="ipc-metadata-list-summary-item__li").get_text()
#print(bob)

bib = soup.find_all("article")
print(bib)
