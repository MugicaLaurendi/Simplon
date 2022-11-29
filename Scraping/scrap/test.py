import pandas as pd
from bs4 import BeautifulSoup
import requests as req

def favorite_movies() :

    file = pd.read_csv('akinator.csv')
    df = pd.DataFrame(file)
    favorite_movies = list(df["Film préféré"])

    return favorite_movies

Web = req.get('https://www.imdb.com/find?q=inception&ref_=nv_sr_sm')

S = BeautifulSoup(Web.text, 'lxml')

# print(S.prettify())

# <tr class="findResult odd">
# bob = "tr class=\"findResult odd\""
# print(f'HTML: {S.}, name: {S.bob.name}, text: {S.bob.text}')


bob = S.find_all("div")


print(bob)
