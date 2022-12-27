from distutils.command.clean import clean
import pandas as pd
import requests as req
from bs4 import BeautifulSoup
from cleantext import clean

def main() :

    animals = column_from_csv("akinator.csv")
    animals = clean_animals(animals)
    print(animals)
    url_ids = get_url_with_id(animals)
    #print(url_ids)
    apis_json = get_api_json(url_ids)
    #print(apis_json)

    create_animals_dictionary(apis_json)

def clean_animals(animals) :

    for i in range(len(animals)) :

        animals[i] = clean(animals[i], no_emoji = True)

    return animals

def column_from_csv(csv) :

    file = pd.read_csv(csv)
    df = pd.DataFrame(file)
    animals = list(df["Animal totem"])

    return animals

def get_url_with_id(animals) :

    url_ids = []

    for i in animals :

            url_ids.append(f"https://pixabay.com/api/?key=30680417-3b10aa3edff76c9cf514adcbe&q={i}&lang=fr")

    return url_ids


def get_api_json(url_ids) :
    apis_json = []
    for i in url_ids :
        api = req.get(i)
        api_json = api.json()
        apis_json.append(api_json)

    return apis_json

def create_animals_dictionary(apis_json) :
    animal_dictionaries = []
    for api_json in apis_json :
        animal_dictionaries["a"] = api_json["hits"][0]["webformatURL"]
        print(animal_dictionaries)




main()
