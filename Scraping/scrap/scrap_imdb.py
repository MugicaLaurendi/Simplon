import pandas as pd
from bs4 import BeautifulSoup
import requests as req

df = pd.read_csv('akinator.csv', usecols=["Film préféré"])
print(df.values.tolist())
for i in df.values.tolist():
    print(i)
    page = req.get(f"https://www.imdb.com/find?q={str(i)}")
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        print(soup.find(class_="ipc-metadata-list-summary-item__li").get_text())
    except:
        print("film pas trouvé")
