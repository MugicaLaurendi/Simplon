from distutils.command.clean import clean
import pandas as pd
import requests as req
from bs4 import BeautifulSoup
from cleantext import clean

def create_animals_dictionary(csv):

    file = pd.read_csv(csv)
    df = pd.DataFrame(file)
    animals = list(df["Animal totem"])

    urls = []
    apis = []
    animals_dict = {}

    for i in range(len(animals)) :

        animals[i] = clean(animals[i],no_emoji=True)

        urls.append(f"https://pixabay.com/api/?key=30680417-3b10aa3edff76c9cf514adcbe&q={animals[i]}&lang=fr")

        apis.append(req.get(urls[i]).json())

        animals_dict[animals[i]] = apis[i]["hits"][0]["webformatURL"]

    print(animals_dict)

create_animals_dictionary("akinator.csv")
